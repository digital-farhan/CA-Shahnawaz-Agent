# Site Inventory Notes — cashahnawaz.com

Session date: 2026-08-27

## Inventory completeness label: **PARTIAL INVENTORY**

This is labeled PARTIAL, not COMPLETE, for the following specific reasons:

1. **All three child sitemaps referenced by `sitemap_index.xml` were successfully fetched and every `<loc>` entry within them was enumerated** (42 in `page-sitemap.xml`, 58 in `post-sitemap.xml`, 8 in `category-sitemap.xml` — 108 sitemap-listed URLs total, no pagination or truncation encountered). In that narrow sense, sitemap enumeration itself is complete.
2. It is still marked PARTIAL overall because:
   - **Navigation/footer cross-check surfaced URLs not present in the sitemap at all** (3 footer links with different slugs than their sitemap counterparts — see rows flagged "Not found in XML sitemap" in `site-inventory.csv`). These represent real, linked-to URLs on the live site whose actual current status (200/404/redirect) was **not verified**, since verifying them was outside the "homepage + Tier 1" individual-fetch scope set for this phase. A live status check of these 3 is recommended for the technical-seo pass.
   - **Only the homepage and the 13 Tier 1 priority URLs were individually fetched and status/title/CTA-verified this session** (per the task's explicit scope). The remaining ~98 sitemap-listed URLs (Tier 2 support pages, Tier 3 blog articles, category archives) were enumerated from the sitemap XML only — their live HTTP status, noindex state, and content were **not individually confirmed**. This is stated explicitly in every such row's "Indexability Signal" column as `Listed in XML sitemap (not individually verified)`.
   - **No JS-rendering / browser-based crawl was performed** — if any part of the site's navigation or content is client-side-injected, additional URLs could exist that neither the sitemap nor a WebFetch-based nav/footer extraction would surface. This cannot be ruled out with the tools available this session.
   - **Raw HTTP header/status-code data is unavailable** (see `reports/00-capability-check.md`), so even the "200" statements for individually-fetched pages mean "page content loaded without an error page" as reported by WebFetch's summarizing model, not a confirmed raw HTTP 200 status code.

## Total counts

- Sitemap-listed URLs (all 3 child sitemaps combined): **108** (107 unique paths — one URL, `/trademark-registration/`, appears twice: once as a page, once as a category-archive entry; see anomaly note in `sitemap-discovery.md`)
- Footer-discovered URLs not present in the sitemap: **3**
- **Total rows in `site-inventory.csv`: 111**
- URLs individually live-fetched and verified this session: **11** (homepage + 10 interior pages: GST Registration Online, GST Return Filing, Income Tax Return Filing Mumbai, Accounting Services, Audit Services, Startup Registration India, Section 8 Company Registration, Public Limited Company, LLP Annual Filing, About Us, Contact Us). Two further Tier 1 URLs (ITR Filing for NRI, TDS Return Filing Services, 12A/80G Registration) were sitemap-listed and nav-linked but not individually fetched this session — their rows are marked accordingly.

## Other observations from the cross-check (evidence only, not diagnosed)

- Several footer links use a literal `http://` scheme in their `href` even though the site serves over HTTPS (e.g., `http://cashahnawaz.com/contact-us/`, `http://cashahnawaz.com/accounting-services/`). Their destination slugs matched the sitemap in most cases, so they are not flagged as broken in the CSV, but the mixed protocol in internal link markup is itself worth a technical-seo look.
- The About Us page's rendered content included what read as placeholder statistics ("0 completed projects, 0% satisfaction rate") rather than real figures — noted here as a raw observation from the individual fetch, not scored as a finding (that judgment belongs to on-page-seo/content-audit/cro-audit).
