from __future__ import annotations

import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
URLS = [
    "https://cashahnawaz.com/",
    "https://cashahnawaz.com/accounting-services/",
    "https://cashahnawaz.com/gst-registration-online/",
    "https://cashahnawaz.com/gst-return-filing/",
    "https://cashahnawaz.com/income-tax-return-filing-in-mumbai/",
    "https://cashahnawaz.com/itr-filing-for-nri-guide-for-non-resident-taxation/",
    "https://cashahnawaz.com/audit-services/",
    "https://cashahnawaz.com/contact-us/",
]


def types(value):
    output = []
    if isinstance(value, dict):
        kind = value.get("@type")
        if isinstance(kind, str):
            output.append(kind)
        elif isinstance(kind, list):
            output.extend(kind)
        for child in value.values():
            output.extend(types(child))
    elif isinstance(value, list):
        for child in value:
            output.extend(types(child))
    return output


def main():
    results = []
    for url in URLS:
        html = requests.get(url, timeout=45, headers={"User-Agent": "CashahnawazSEOAudit/1.0"}).text
        soup = BeautifulSoup(html, "lxml")
        page = {"url": url, "blocks": []}
        for index, script in enumerate(soup.find_all("script", attrs={"type": "application/ld+json"}), start=1):
            raw = script.string or script.get_text()
            item = {"block": index, "bytes": len(raw)}
            try:
                data = json.loads(raw)
                item.update({"valid_json": True, "types": sorted(set(types(data)))})
            except Exception as exc:
                item.update({"valid_json": False, "error": str(exc), "sample": raw[:500]})
            page["blocks"].append(item)
        results.append(page)
    out = ROOT / "data" / "crawl" / "schema-validation-priority-2026-08-28.json"
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
