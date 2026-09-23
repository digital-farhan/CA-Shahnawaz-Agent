from __future__ import annotations

import json
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "Cashahnawaz-Comprehensive-SEO-Audit-2026-08-28.html"
SHOT = ROOT / "reports" / "_qa-report-cover.png"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        errors = []
        page.on("console", lambda message: errors.append(message.text) if message.type == "error" else None)
        page.goto(REPORT.as_uri(), wait_until="load")
        page.screenshot(path=str(SHOT), full_page=False)
        result = page.evaluate("""
() => {
  const ids=[...document.querySelectorAll('[id]')].map(x=>x.id);
  const duplicates=ids.filter((x,i)=>ids.indexOf(x)!==i);
  const toc=[...document.querySelectorAll('.toc a')];
  return {
    title:document.title,
    headings:document.querySelectorAll('h1,h2,h3').length,
    tables:document.querySelectorAll('table').length,
    tocLinks:toc.length,
    brokenToc:toc.filter(a=>!document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)))).map(a=>a.getAttribute('href')),
    duplicateIds:[...new Set(duplicates)],
    hasCriticalFinding:(document.body.innerText||'').includes('External redirect transfers a priority service'),
    bodyChars:(document.body.innerText||'').length,
  };
}
""")
        result["consoleErrors"] = errors
        browser.close()
    print(json.dumps(result, indent=2))
    if result["brokenToc"] or result["duplicateIds"] or errors or not result["hasCriticalFinding"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
