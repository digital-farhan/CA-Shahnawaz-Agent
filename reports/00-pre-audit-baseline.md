# Phase 0 — Pre-Audit Baseline Summary

**Site:** https://cashahnawaz.com/
**Session date:** 2026-08-27
**Phase type:** Discovery and baseline only — no SEO analysis, severity scoring, or live-site changes were performed. This document synthesizes `reports/00-capability-check.md` and the `data/crawl/` outputs from this session.

## 1. Website access status

Live and reachable this session. Homepage and 10 interior pages (11 total) were individually fetched and loaded successfully via WebFetch. No error pages, login walls, or bot-block behavior were encountered on any URL fetched this session.

## 2. Crawl method used

WebFetch (AI-summarized HTML→markdown extraction) against live URLs, per targeted extraction prompts for each data point needed (sitemap enumeration, navigation/footer link extraction, technical fingerprinting, conversion-element inventory). No browser automation, no raw HTTP header inspection tool, no JS rendering guarantee. PowerShell was used only for local file operations, never against the live site.

## 3. Sitemap status

Primary sitemap **confirmed live**: `https://cashahnawaz.com/sitemap_index.xml` (matches the `Sitemap:` directive in `robots.txt`, fetched fresh this session). Generator confirmed as **Rank Math SEO Plugin** via an XML comment inside the sitemap and corroborated by `rankmath/v1` REST namespaces. It lists 3 child sitemaps: `post-sitemap.xml` (58 URLs), `page-sitemap.xml` (42 URLs), `category-sitemap.xml` (8 URLs). `sitemap.xml` and `wp-sitemap.xml` also returned 200 with the same 3-child-sitemap content — likely aliases/redirects to `sitemap_index.xml`, but the exact mechanism is NOT VERIFIABLE without raw header access.

## 4. URL inventory status: **PARTIAL**

All 108 sitemap-listed URLs across all 3 child sitemaps were fully enumerated (no pagination or truncation hit) — sitemap enumeration itself is complete. It is marked PARTIAL overall because: (a) only 11 URLs (homepage + 10 Tier 1 pages) were individually live-fetched and status/title-verified; the other ~100 rows are sitemap-listed only, explicitly labeled "not individually verified"; (b) 3 footer-linked URLs were found that don't match any sitemap entry and were not live-status-checked; (c) no JS-rendering crawl was possible, so any client-side-injected links can't be ruled out. Full reasoning in `data/crawl/site-inventory-notes.md`.

## 5. Estimated number of discoverable URLs

**111 total** in the inventory (108 sitemap-listed + 3 footer-only, non-sitemap URLs). Note one duplicate: `/trademark-registration/` appears as both a page and a category-archive entry (same URL, two sitemap sources).

## 6. URLs actually individually reviewed (live-fetched)

**11**: Homepage, GST Registration Online, GST Return Filing, Income Tax Return Filing (Mumbai), Accounting Services, Audit Services, Startup Registration India, Section 8 Company Registration, Public Limited Company, LLP Annual Filing, About Us, Contact Us.

## 7. Priority commercial URLs identified — Tier 1: 13

1. Homepage
2. GST Registration Online
3. GST Return Filing
4. Income Tax Return Filing (Mumbai)
5. ITR Filing for NRI
6. Accounting Services
7. Audit Services
8. Startup Registration India
9. Section 8 Company Registration
10. Public Limited Company
11. LLP Annual Filing
12. TDS Return Filing Services
13. 12A/12AA/80G Registration

Full rationale (commercial importance, user intent, conversion goal) per URL is in `data/crawl/priority-urls.md`, which also notes apparent gaps: no dedicated pages found for Private Limited Company Registration, LLP Registration (formation), Partnership Registration, or Proprietorship Registration, despite these being named CLAUDE.md priority services.

## 8. WordPress technology findings

- **CMS: WordPress — CONFIRMED** (public `/wp-json/` REST discovery document, site name "Shahnawaz and Associates," description "Chartered Accountant").
- **SEO plugin: Rank Math — CONFIRMED** (sitemap generator comment + REST namespace). No second SEO plugin's signature found — LIKELY NOT a plugin-conflict situation, though not admin-confirmed.
- **Page builder: Elementor (+ Pro, AI) — CONFIRMED** via REST namespaces and popup-action URL parameters.
- **Theme: OceanWP — LIKELY** (REST namespace only, not admin-confirmed).
- **Caching: LiteSpeed Cache — LIKELY** (REST namespace).
- **Form plugin: ambiguous — POSSIBLE both Contact Form 7 and Forminator installed**; which actually powers the live enquiry form could not be determined this session (no CSS class evidence surfaced).
- **GTM container / JSON-LD schema: NOT DETERMINED** — actively searched for and not found in fetched content, but this is a known WebFetch blind spot (script/head content isn't reliably surfaced), not a confirmed absence. Needs a raw-HTML or browser-based recheck before being treated as fact.

Full detail with quoted evidence: `data/crawl/wordpress-fingerprint.md`.

## 9. Visible conversion entry points

Phone/click-to-call (`tel:+919819267015`, sitewide), email (`mailto:ca.shahnawazshaikh@gmail.com`), a recurring multi-field enquiry form (Name/Email/Mobile/City/Service dropdown, sitewide), and a "GET IT NOW" popup CTA (sitewide). **No WhatsApp/`wa.me` link and no map embed were found anywhere checked** — notable given CLAUDE.md's explicit goal to improve WhatsApp contacts. A `chatway` (live chat) plugin namespace was detected but no chat widget was visibly confirmed on any fetched page. All items carry **TRACKING STATUS: UNKNOWN** — no tracking verification was performed this phase. Full detail: `data/crawl/conversion-entry-points.md`.

## 10. Brand findings + recommended audit color system

**Brand findings: effectively NOT DETERMINED.** Only one hex value (`#cfd4db`, a minor SVG placeholder fill) was actually observed; no CSS custom properties, button colors, or font-family declarations were surfaced — a genuine WebFetch/no-screenshot limitation, not a completed brand audit.

**Recommended report color system (design recommendation, not a scraped fact):** Primary `#1B3A5C` (navy), Secondary `#2F5233` (forest green), Accent `#C99B3B` (restrained gold), Background `#F7F8FA`, Heading/text `#1A1D23`. Severity colors: CRITICAL `#B3261E`, HIGH `#D2691E`, MEDIUM `#C99B3B`, LOW `#6B7280`, OPPORTUNITY `#2F5233`, COMPLETED `#1B7A43`, NOT STARTED `#9CA3AF`. Full rationale: `data/crawl/brand-style-discovery.md`.

## 11. Data sources currently unavailable

GSC, GA4, GTM, WordPress Admin, hosting access, Lighthouse/PageSpeed — none have a working connector this session (confirmed by attempted tool search, not merely assumed). Raw HTTP headers/status codes and browser-rendered/screenshot views are also unavailable. Confirmed in `reports/00-capability-check.md`.

## 12. Important audit limitations

- WebFetch's HTML→markdown conversion does not reliably surface `<head>`/`<script>`/`<style>` content — title tags, meta descriptions, JSON-LD, GTM snippets, and CSS were inconsistently or not at all visible, even when confirmed present elsewhere (e.g., Rank Math is confirmed active but its schema output couldn't be observed).
- No raw HTTP status codes, redirect chains, or response headers are available — all "200"/"loads successfully" statements reflect WebFetch's qualitative read, not a confirmed status code.
- Domain/protocol canonicalization (www vs. non-www, HTTP vs. HTTPS) could not be conclusively verified — all tested variants returned the same content, but the underlying mechanism (redirect vs. multiple live origins vs. WebFetch normalization) is unconfirmed.
- No JS-rendering/browser crawl — any client-side-injected content or links would be invisible to this crawl.
- Only 11 of 111 inventoried URLs were individually verified; the rest rely on sitemap metadata alone.
- 3 footer-linked URLs point to slugs not found anywhere in the sitemap and were not live-checked (candidate broken/outdated links).
- A URL (`/trademark-registration/`) appears to be shared between a page and a category archive — unexplained, flagged for technical-seo.md.
- Form plugin identity (Contact Form 7 vs. Forminator) is ambiguous.

## 13. Recommended Phase 1 audit scope

Given the findings above:

1. **wordpress-seo.md should run first** (or in tandem with technical-seo.md) specifically to resolve the fingerprint-only ambiguities flagged here — form plugin identity, theme confirmation, and whether the `/trademark-registration/` page/category collision is a real conflict — since technical-seo.md and cro-audit.md's implementation steps both depend on this being settled, per those skills' own stated dependencies.
2. **technical-seo.md next**, focused on: (a) confirming actual HTTP status/redirect behavior for www/non-www and HTTP/HTTPS (needs a header-capable tool this session lacked), (b) checking the 3 unmatched footer links, (c) investigating the sitemap.xml/wp-sitemap.xml aliasing behavior, (d) resolving whether GTM and JSON-LD schema are truly absent or just unobserved (may need to hand off a targeted raw-HTML check).
3. **content-audit.md** should review the priority-service coverage gaps noted in `priority-urls.md` (missing dedicated pages for Private Ltd/LLP/Partnership/Proprietorship registration).
4. **gtm-conversion-audit.md and ga4-analysis.md will run in inspection-only/unavailable mode** — no connector exists this session, so all their outputs must be marked `DATA NOT AVAILABLE` until connectivity is established; this also means **cro-audit.md**, when it runs, must downgrade all findings to inspection-only/OPPORTUNITY-tier per its own stated dependency rule, and should prioritize the confirmed-absent WhatsApp entry point and the ambiguous form-plugin/tracking situation as its first inspection targets.
5. **local-seo.md** should verify the NAP (name/address/phone) consistency using the address captured here, and check whether the missing WhatsApp link and lack of ICAI registration number visibility (noted on About Us) are consistent findings.

No further phase should proceed under the assumption that GSC/GA4/GTM/WordPress Admin/hosting/Lighthouse access exists — each must be re-verified independently when that phase begins, per CLAUDE.md's session-verification rule.
