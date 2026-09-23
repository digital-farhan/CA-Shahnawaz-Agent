from __future__ import annotations

import json
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build


ROOT = Path(__file__).resolve().parents[1]
CREDS = ROOT.parent / ".secrets" / "google-service-account.json"
SITE = "https://cashahnawaz.com/"
URLS = [
    SITE,
    SITE + "accounting-services/",
    SITE + "gst-registration-online/",
    SITE + "gst-return-filing/",
    SITE + "income-tax-return-filing-in-mumbai/",
    SITE + "itr-filing-for-nri-guide-for-non-resident-taxation/",
    SITE + "audit-services/",
    SITE + "private-limited-company-registration/",
    SITE + "llp-annual-filing/",
    SITE + "section-8-company-registration/",
    SITE + "startup-registration-india/",
    SITE + "tds-return-filing-services/",
    SITE + "contact-us/",
    SITE + "gst-registration-services-india-a-guide-to-gst/",
    SITE + "?jkit-ajax-request=jkit_elements",
]


def main() -> None:
    credentials = service_account.Credentials.from_service_account_file(
        CREDS, scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
    )
    service = build("searchconsole", "v1", credentials=credentials, cache_discovery=False)
    output = []
    for url in URLS:
        try:
            response = service.urlInspection().index().inspect(
                body={"inspectionUrl": url, "siteUrl": SITE, "languageCode": "en-US"}
            ).execute()
            status = response.get("inspectionResult", {}).get("indexStatusResult", {})
            output.append({
                "url": url,
                "verdict": status.get("verdict"),
                "coverageState": status.get("coverageState"),
                "robotsTxtState": status.get("robotsTxtState"),
                "indexingState": status.get("indexingState"),
                "pageFetchState": status.get("pageFetchState"),
                "lastCrawlTime": status.get("lastCrawlTime"),
                "googleCanonical": status.get("googleCanonical"),
                "userCanonical": status.get("userCanonical"),
                "sitemap": status.get("sitemap", []),
                "crawledAs": status.get("crawledAs"),
            })
        except Exception as exc:
            output.append({"url": url, "error": str(exc)})
    path = ROOT / "data" / "gsc" / "gsc-url-inspection-actual-priority-2026-08-28.json"
    path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
