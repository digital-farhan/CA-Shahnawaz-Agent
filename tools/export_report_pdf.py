from __future__ import annotations

import asyncio
from pathlib import Path

from playwright.async_api import async_playwright


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "reports" / "Cashahnawaz-Comprehensive-SEO-Audit-2026-08-28.html"
TARGET = ROOT / "reports" / "Cashahnawaz-Comprehensive-SEO-Audit-2026-08-28.pdf"


async def main() -> None:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page()
        await page.goto(SOURCE.as_uri(), wait_until="networkidle")
        await page.emulate_media(media="print")
        await page.pdf(
            path=str(TARGET),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=(
                '<div style="width:100%;padding:0 13mm;color:#71808c;'
                'font:8px Segoe UI,Arial,sans-serif;text-align:right">'
                '<span class="pageNumber"></span> / <span class="totalPages"></span>'
                "</div>"
            ),
        )
        await browser.close()
    print(f"Exported {TARGET} ({TARGET.stat().st_size:,} bytes)")


if __name__ == "__main__":
    asyncio.run(main())
