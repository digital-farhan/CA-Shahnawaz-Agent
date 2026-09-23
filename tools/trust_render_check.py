from __future__ import annotations

import json
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "performance"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        results = {}
        for name, url in {
            "about": "https://cashahnawaz.com/about-us/",
            "home": "https://cashahnawaz.com/",
        }.items():
            page.goto(url, wait_until="domcontentloaded", timeout=90_000)
            page.wait_for_timeout(8_000)
            results[name] = page.evaluate("""
() => {
  const body = document.body.innerText || '';
  const textAround = term => {
    const i = body.toLowerCase().indexOf(term.toLowerCase());
    return i >= 0 ? body.slice(Math.max(0, i - 250), i + 1200) : '';
  };
  return {
    url: location.href,
    title: document.title,
    aboutCounters: textAround('COMPLETED PROJECTS'),
    testimonials: textAround('TESTIMONIALS'),
    practitionerTerms: [...body.matchAll(/(?:CA\s+Shahnawaz|Shahnawaz Shaikh|FRN|membership no|ICAI)/gi)].map(x => x[0]),
  };
}
""")
        browser.close()
    path = OUT / "trust-render-check-2026-08-28.json"
    path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(results, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
