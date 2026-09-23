from __future__ import annotations

import argparse
import calendar
import csv
import json
import os
import re
import sys
import uuid
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Filter,
    FilterExpression,
    Metric,
    RunReportRequest,
)


ROOT = Path(__file__).resolve().parents[1]
credential_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
if not credential_path:
    raise RuntimeError("GOOGLE_APPLICATION_CREDENTIALS is not set")

CREDENTIALS = Path(credential_path).expanduser()
if not CREDENTIALS.is_file():
    raise FileNotFoundError(
        "GOOGLE_APPLICATION_CREDENTIALS does not reference an existing file"
    )

SITE_URL = "https://cashahnawaz.com/"
GA4_PROPERTY = "546098812"
GSC_FINALIZATION_DELAY_DAYS = 3
MONTH_PATTERN = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
MONTHLY_ROOT = ROOT / "data" / "monthly"


@dataclass(frozen=True)
class ReportingPeriod:
    reporting_month: str
    current_start: date
    current_end: date
    comparison_start: date
    comparison_end: date


def parse_reporting_month(value: str, today: date | None = None) -> ReportingPeriod:
    if not MONTH_PATTERN.fullmatch(value):
        raise ValueError("--month must use the strict YYYY-MM format")
    year, month = (int(part) for part in value.split("-"))
    today = today or date.today()
    selected_start = date(year, month, 1)
    current_month_start = date(today.year, today.month, 1)
    if selected_start > current_month_start:
        raise ValueError("--month cannot be in the future")
    if selected_start == current_month_start:
        raise ValueError("--month cannot be the current incomplete month")
    selected_end = date(year, month, calendar.monthrange(year, month)[1])
    if selected_end > today - timedelta(days=GSC_FINALIZATION_DELAY_DAYS):
        raise ValueError("--month is too recent for the configured GSC data-finalisation delay")
    if month == 1:
        comparison_year, comparison_month = year - 1, 12
    else:
        comparison_year, comparison_month = year, month - 1
    comparison_start = date(comparison_year, comparison_month, 1)
    comparison_end = date(comparison_year, comparison_month, calendar.monthrange(comparison_year, comparison_month)[1])
    return ReportingPeriod(value, selected_start, selected_end, comparison_start, comparison_end)


def write_csv(path: Path, headers: list[str], rows: Iterable[Iterable[Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, default=str), encoding="utf-8")


def gsc_rows(service: Any, start: date, end: date, dimensions: list[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    start_row = 0
    while True:
        body = {
            "startDate": start.isoformat(),
            "endDate": end.isoformat(),
            "dimensions": dimensions,
            "rowLimit": 25000,
            "startRow": start_row,
            "dataState": "final",
        }
        response = service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()
        batch = response.get("rows", [])
        rows.extend(batch)
        if len(batch) < 25000:
            break
        start_row += len(batch)
    return rows


def export_gsc(period: ReportingPeriod, out: Path) -> dict[str, Any]:
    scopes = ["https://www.googleapis.com/auth/webmasters.readonly"]
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS, scopes=scopes)
    service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    exports: dict[str, int] = {}
    output_files: list[str] = []
    for label, start, end in (
        ("current", period.current_start, period.current_end),
        ("comparison", period.comparison_start, period.comparison_end),
    ):
        target = out / label
        target.mkdir(parents=True, exist_ok=True)
        for dimensions in (["date"], ["query"], ["page"], ["device"], ["country"], ["searchAppearance"]):
            key = "-".join(dimensions)
            rows = gsc_rows(service, start, end, list(dimensions))
            headers = list(dimensions) + ["clicks", "impressions", "ctr", "position"]
            output_rows = []
            for row in rows:
                values = list(row.get("keys", []))
                values.extend([row.get("clicks", 0), row.get("impressions", 0), row.get("ctr", 0), row.get("position", 0)])
                output_rows.append(values)
            output_path = target / f"{key}.csv"
            write_csv(output_path, headers, output_rows)
            exports[f"{label}/{key}"] = len(rows)
            output_files.append(str(output_path.relative_to(out.parent)))

    sites = service.sites().list().execute()
    sitemaps = service.sitemaps().list(siteUrl=SITE_URL).execute()
    metadata_path = out / "property-sitemaps.json"
    write_json(metadata_path, {"sites": sites, "sitemaps": sitemaps})
    output_files.append(str(metadata_path.relative_to(out.parent)))
    return {"status": "ok", "output_files": output_files, "row_counts": exports, "site_count": len(sites.get("siteEntry", []))}


def ga_report(
    client: BetaAnalyticsDataClient,
    start: date,
    end: date,
    dimensions: list[str],
    metrics: list[str],
    dimension_filter: FilterExpression | None = None,
    limit: int = 100000,
) -> tuple[list[str], list[list[str]]]:
    request = RunReportRequest(
        property=f"properties/{GA4_PROPERTY}",
        dimensions=[Dimension(name=x) for x in dimensions],
        metrics=[Metric(name=x) for x in metrics],
        date_ranges=[DateRange(start_date=start.isoformat(), end_date=end.isoformat())],
        dimension_filter=dimension_filter,
        limit=limit,
    )
    response = client.run_report(request)
    headers = dimensions + metrics
    rows: list[list[str]] = []
    for row in response.rows:
        rows.append([v.value for v in row.dimension_values] + [v.value for v in row.metric_values])
    return headers, rows


def export_ga4(period: ReportingPeriod, out: Path) -> dict[str, Any]:
    scopes = ["https://www.googleapis.com/auth/analytics.readonly"]
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS, scopes=scopes)
    client = BetaAnalyticsDataClient(credentials=creds)
    organic = FilterExpression(
        filter=Filter(
            field_name="sessionDefaultChannelGroup",
            string_filter=Filter.StringFilter(value="Organic Search", match_type=Filter.StringFilter.MatchType.EXACT),
        )
    )
    jobs = [
        ("daily", ["date"], ["activeUsers", "newUsers", "sessions", "engagedSessions", "keyEvents"], None),
        ("channels", ["sessionDefaultChannelGroup"], ["activeUsers", "newUsers", "sessions", "engagedSessions", "engagementRate", "averageSessionDuration", "keyEvents"], None),
        ("organic-landing-pages", ["landingPagePlusQueryString"], ["activeUsers", "newUsers", "sessions", "engagedSessions", "engagementRate", "averageSessionDuration", "keyEvents"], organic),
        ("organic-devices", ["deviceCategory"], ["activeUsers", "sessions", "engagedSessions", "engagementRate", "keyEvents"], organic),
        ("organic-countries", ["country"], ["activeUsers", "sessions", "engagedSessions", "keyEvents"], organic),
        ("events", ["eventName"], ["eventCount", "totalUsers", "keyEvents"], None),
        ("organic-events", ["eventName"], ["eventCount", "totalUsers", "keyEvents"], organic),
        ("organic-pages", ["pagePathPlusQueryString"], ["screenPageViews", "activeUsers", "userEngagementDuration", "keyEvents"], organic),
    ]
    summary: dict[str, int] = {}
    output_files: list[str] = []
    for label, start, end in (("current", period.current_start, period.current_end), ("comparison", period.comparison_start, period.comparison_end)):
        target = out / label
        target.mkdir(parents=True, exist_ok=True)
        for name, dims, metrics, filter_expr in jobs:
            headers, rows = ga_report(client, start, end, dims, metrics, filter_expr)
            output_path = target / f"{name}.csv"
            write_csv(output_path, headers, rows)
            summary[f"{label}/{name}"] = len(rows)
            output_files.append(str(output_path.relative_to(out.parent)))

    admin = build("analyticsadmin", "v1beta", credentials=creds, cache_discovery=False)
    prop = admin.properties().get(name=f"properties/{GA4_PROPERTY}").execute()
    streams = admin.properties().dataStreams().list(parent=f"properties/{GA4_PROPERTY}").execute()
    metadata_path = out / "property-streams.json"
    write_json(metadata_path, {"property": prop, "dataStreams": streams})
    output_files.append(str(metadata_path.relative_to(out.parent)))
    return {"status": "ok", "output_files": output_files, "row_counts": summary}


def export_gtm(out: Path) -> dict[str, Any]:
    scopes = ["https://www.googleapis.com/auth/tagmanager.readonly"]
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS, scopes=scopes)
    service = build("tagmanager", "v2", credentials=creds, cache_discovery=False)
    out.mkdir(parents=True, exist_ok=True)
    inventory: dict[str, Any] = {"accounts": []}
    accounts = service.accounts().list().execute().get("account", [])
    collection_errors: list[str] = []
    for account in accounts:
        account_item: dict[str, Any] = {"account": account, "containers": []}
        containers = service.accounts().containers().list(parent=account["path"]).execute().get("container", [])
        for container in containers:
            container_item: dict[str, Any] = {"container": container}
            parent = container["path"]
            try:
                container_item["liveVersion"] = service.accounts().containers().versions().live(parent=parent).execute()
            except Exception:
                collection_errors.append("live version")
            workspaces = service.accounts().containers().workspaces().list(parent=parent).execute().get("workspace", [])
            container_item["workspaces"] = []
            for workspace in workspaces:
                wpath = workspace["path"]
                witem: dict[str, Any] = {"workspace": workspace}
                for resource in ("tags", "triggers", "variables", "built_in_variables"):
                    try:
                        endpoint = getattr(service.accounts().containers().workspaces(), resource)()
                        response = endpoint.list(parent=wpath).execute()
                        singular = {"tags": "tag", "triggers": "trigger", "variables": "variable", "built_in_variables": "builtInVariable"}[resource]
                        witem[resource] = response.get(singular, [])
                    except Exception:
                        collection_errors.append(resource)
                container_item["workspaces"].append(witem)
            account_item["containers"].append(container_item)
        inventory["accounts"].append(account_item)
    if collection_errors:
        raise RuntimeError("GTM inventory collection was incomplete")
    write_json(out / "live-inventory.json", inventory)

    compact = []
    for account_item in inventory["accounts"]:
        for container_item in account_item["containers"]:
            live = container_item.get("liveVersion", {})
            compact.append({
                "account_name": account_item["account"].get("name"),
                "container_name": container_item["container"].get("name"),
                "public_id": container_item["container"].get("publicId"),
                "live_version": live.get("containerVersionId"),
                "live_tags": len(live.get("tag", [])),
                "live_triggers": len(live.get("trigger", [])),
                "live_variables": len(live.get("variable", [])),
                "workspace_count": len(container_item.get("workspaces", [])),
            })
    summary_path = out / "container-summary.csv"
    write_csv(summary_path, list(compact[0].keys()) if compact else ["status"], [list(x.values()) for x in compact] if compact else [["none"]])
    return {
        "status": "ok",
        "output_files": [
            str((out / "live-inventory.json").relative_to(out.parent)),
            str(summary_path.relative_to(out.parent)),
        ],
        "account_count": len(accounts),
        "row_counts": {"container-summary": len(compact)},
    }


def required_output_paths() -> set[Path]:
    gsc_reports = ("date", "query", "page", "device", "country", "searchAppearance")
    ga4_reports = (
        "daily", "channels", "organic-landing-pages", "organic-devices",
        "organic-countries", "events", "organic-events", "organic-pages",
    )
    required = {
        Path("gsc") / period_name / f"{name}.csv"
        for period_name in ("current", "comparison")
        for name in gsc_reports
    }
    required.update(
        Path("ga4") / period_name / f"{name}.csv"
        for period_name in ("current", "comparison")
        for name in ga4_reports
    )
    required.update({
        Path("gsc/property-sitemaps.json"),
        Path("ga4/property-streams.json"),
        Path("gtm/live-inventory.json"),
        Path("gtm/container-summary.csv"),
    })
    return required


def validate_required_outputs(staging_directory: Path) -> list[str]:
    missing = [path for path in required_output_paths() if not (staging_directory / path).is_file()]
    if missing:
        raise RuntimeError("Required monthly outputs were not created")
    return sorted(str(path) for path in required_output_paths())


def build_manifest(period: ReportingPeriod, run_id: str, source_status: dict[str, Any], output_files: list[str]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "run_id": run_id,
        "status": "complete",
        "reporting_month": period.reporting_month,
        "current_period": {"start": period.current_start.isoformat(), "end": period.current_end.isoformat()},
        "comparison_period": {"start": period.comparison_start.isoformat(), "end": period.comparison_end.isoformat()},
        "collection_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source_status": source_status,
        "output_files": output_files,
        "limitations": [
            f"GSC data is collected with a {GSC_FINALIZATION_DELAY_DAYS}-day finalisation delay.",
            "GSC uses a URL-prefix property, so coverage is limited to that property scope.",
            "GA4 reports may be affected by thresholding, cardinality, or API row limits.",
            "GTM is a live configuration snapshot at collection time, not a month-end history or change log.",
        ],
    }


def collect_month(period: ReportingPeriod) -> None:
    final_directory = MONTHLY_ROOT / period.reporting_month
    if final_directory.exists():
        if (final_directory / "manifest.json").is_file():
            raise RuntimeError("A published monthly report already exists for this month")
        raise RuntimeError("The target monthly output directory already exists and will not be replaced")
    run_id = f"{period.reporting_month}-{uuid.uuid4().hex}"
    staging_directory = MONTHLY_ROOT / ".staging" / run_id
    staging_directory.mkdir(parents=True, exist_ok=False)
    source_status: dict[str, Any] = {}
    for source_name, collect in (
        ("gsc", lambda: export_gsc(period, staging_directory / "gsc")),
        ("ga4", lambda: export_ga4(period, staging_directory / "ga4")),
        ("gtm", lambda: export_gtm(staging_directory / "gtm")),
    ):
        try:
            source_status[source_name] = collect()
        except Exception:
            raise RuntimeError(f"Monthly collection failed for {source_name}; the staging directory was retained") from None
    output_files = validate_required_outputs(staging_directory)
    write_json(staging_directory / "manifest.json", build_manifest(period, run_id, source_status, output_files))
    staging_directory.rename(final_directory)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Collect read-only Google monthly reporting data.")
    parser.add_argument("--month", required=True, metavar="YYYY-MM", help="Completed reporting month")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        period = parse_reporting_month(args.month)
        collect_month(period)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
