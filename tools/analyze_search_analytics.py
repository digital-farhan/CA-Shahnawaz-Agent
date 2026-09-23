from __future__ import annotations

import csv
import json
import math
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-28"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def f(value: str | None) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0


def aggregate(rows: list[dict[str, str]]) -> dict[str, float]:
    clicks = sum(f(x.get("clicks")) for x in rows)
    impressions = sum(f(x.get("impressions")) for x in rows)
    return {
        "clicks": round(clicks),
        "impressions": round(impressions),
        "ctr": clicks / impressions if impressions else 0,
        "weighted_position": sum(f(x.get("position")) * f(x.get("impressions")) for x in rows) / impressions if impressions else 0,
    }


def pct_change(new: float, old: float) -> float | None:
    return (new - old) / old if old else None


def write_csv(path: Path, headers: list[str], rows: list[list[Any]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)


def main() -> None:
    gsc = ROOT / "data" / "gsc"
    ga = ROOT / "data" / "ga4"
    daily = sorted(read_csv(gsc / f"gsc-90d-date-{DATE}.csv"), key=lambda x: x["date"])
    first30 = aggregate(daily[:30])
    last30 = aggregate(daily[-30:])
    gsc_trend = {
        "data_start": daily[0]["date"],
        "data_end": daily[-1]["date"],
        "total_90d": aggregate(daily),
        "first_30d": first30,
        "last_30d": last30,
        "change_last_vs_first": {
            "clicks": pct_change(last30["clicks"], first30["clicks"]),
            "impressions": pct_change(last30["impressions"], first30["impressions"]),
            "ctr": pct_change(last30["ctr"], first30["ctr"]),
            "weighted_position": last30["weighted_position"] - first30["weighted_position"],
        },
    }

    queries = read_csv(gsc / f"gsc-90d-query-{DATE}.csv")
    branded = [x for x in queries if re.search(r"shahnawaz|cashahnawaz", x["query"], re.I)]
    nonbranded = [x for x in queries if x not in branded]
    commercial_rx = re.compile(r"\b(service|services|consultant|consultancy|ca|chartered accountant|filing|registration|compliance|bookkeeping|accounting|audit|return|itr|gst|tds|nri|company|llp|tax)\b", re.I)
    opportunities = []
    for row in nonbranded:
        imp = f(row["impressions"])
        pos = f(row["position"])
        ctr = f(row["ctr"])
        if imp < 50 or not (3 <= pos <= 20):
            continue
        commercial = bool(commercial_rx.search(row["query"]))
        opportunity_index = imp * (1 - min(ctr, 1)) / math.sqrt(max(pos, 1)) * (1.35 if commercial else 1)
        opportunities.append({**row, "commercial_intent": commercial, "opportunity_index": opportunity_index})
    opportunities.sort(key=lambda x: x["opportunity_index"], reverse=True)
    write_csv(
        gsc / f"gsc-query-opportunities-{DATE}.csv",
        ["query", "clicks", "impressions", "ctr", "position", "commercial_intent", "opportunity_index"],
        [[x["query"], x["clicks"], x["impressions"], x["ctr"], x["position"], x["commercial_intent"], round(x["opportunity_index"], 2)] for x in opportunities],
    )

    pairs = read_csv(gsc / f"gsc-90d-query-page-{DATE}.csv")
    query_pages: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in pairs:
        query_pages[row["query"]].append(row)
    top_opportunity_pairs = []
    for op in opportunities[:150]:
        mapped = sorted(query_pages.get(op["query"], []), key=lambda x: f(x["impressions"]), reverse=True)
        if mapped:
            top_opportunity_pairs.append({**op, "page": mapped[0]["page"], "page_impressions": f(mapped[0]["impressions"])})
    write_csv(
        gsc / f"gsc-query-page-opportunities-{DATE}.csv",
        ["query", "page", "clicks", "impressions", "ctr", "position", "commercial_intent", "opportunity_index"],
        [[x["query"], x["page"], x["clicks"], x["impressions"], x["ctr"], x["position"], x["commercial_intent"], round(x["opportunity_index"], 2)] for x in top_opportunity_pairs],
    )

    pages = read_csv(gsc / f"gsc-90d-page-{DATE}.csv")
    pages_sorted = sorted(pages, key=lambda x: f(x["clicks"]), reverse=True)
    top10_clicks = sum(f(x["clicks"]) for x in pages_sorted[:10])
    total_page_clicks = sum(f(x["clicks"]) for x in pages_sorted)

    channels = read_csv(ga / f"ga4-channels-90d-{DATE}.csv")
    organic = next((x for x in channels if x["sessionDefaultChannelGroup"] == "Organic Search"), {})
    total_sessions = sum(f(x.get("sessions")) for x in channels)
    events = read_csv(ga / f"ga4-events-90d-{DATE}.csv")
    event_map = {x["eventName"]: x for x in events}
    ga_daily = sorted(read_csv(ga / f"ga4-daily-16m-{DATE}.csv"), key=lambda x: x["date"])
    ga_summary = {
        "data_start": datetime.strptime(ga_daily[0]["date"], "%Y%m%d").date().isoformat() if ga_daily else None,
        "data_end": datetime.strptime(ga_daily[-1]["date"], "%Y%m%d").date().isoformat() if ga_daily else None,
        "organic_sessions": f(organic.get("sessions")),
        "total_sessions": total_sessions,
        "organic_session_share": f(organic.get("sessions")) / total_sessions if total_sessions else 0,
        "organic_engagement_rate": f(organic.get("engagementRate")),
        "organic_average_session_duration_seconds": f(organic.get("averageSessionDuration")),
        "organic_key_events_reported": f(organic.get("keyEvents")),
        "events": {name: {"event_count": f(row.get("eventCount")), "users": f(row.get("totalUsers")), "key_events": f(row.get("keyEvents"))} for name, row in event_map.items()},
        "measurement_warning": "Published GTM WhatsApp link-click trigger has no filter; whatsapp_click and aggregate key-event metrics are not reliable conversion counts.",
    }
    summary = {
        "gsc": gsc_trend,
        "gsc_brand_split_visible_query_rows": {
            "branded": aggregate(branded),
            "nonbranded": aggregate(nonbranded),
            "note": "Query exports omit anonymized queries, so this split does not equal the complete Search Console totals.",
        },
        "gsc_concentration": {"top_10_page_click_share": top10_clicks / total_page_clicks if total_page_clicks else 0},
        "gsc_top_pages": pages_sorted[:20],
        "gsc_top_commercial_opportunities": [x for x in top_opportunity_pairs if x["commercial_intent"]][:30],
        "ga4": ga_summary,
    }
    (ROOT / "data" / f"search-analytics-analysis-{DATE}.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
