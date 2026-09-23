# Phase 0 — Capability Check

**Session date:** 2026-08-27
**Site under audit:** https://cashahnawaz.com/

This table documents capabilities actually tested in this session. Nothing below is carried over from a prior session's assumptions or from CLAUDE.md's connector table without a fresh test.

| Capability | Verified Available | Test Performed | Limitation |
|---|---|---|---|
| WebFetch / general web access | Yes | Fetched `https://cashahnawaz.com/robots.txt`, homepage, multiple interior service pages, and 4 sitemap files — all returned usable content. | Content is AI-summarized/markdown-converted, not raw HTML. |
| Fetching live pages | Yes | Successfully fetched homepage and 10 interior pages (GST Registration, GST Return Filing, ITR Filing Mumbai, Accounting Services, Audit Services, Startup Registration, Section 8 Company, Public Limited Company, LLP Annual Filing, About Us, Contact Us) — all loaded with visible content. | None of the failures observed this session; cannot rule out failures on untested pages. |
| HTML/source inspection | Partial | Asked WebFetch to surface `<head>` contents (title tag, meta generator, JSON-LD, `<script>` src paths) on the homepage. Body-level content (nav, forms, CTAs, tel/mailto links, H1) was reliably surfaced; `<head>`-level tags (title, meta description, meta generator, JSON-LD, GTM script) were NOT surfaced — returned "NOT VISIBLE" by the tool. | WebFetch's HTML→markdown conversion appears to strip or not reliably expose `<head>`/`<script>` content. Confirmed genuine limitation, not a one-off failure (tested twice with different prompts). Interior pages did surface `<title>` text successfully (e.g., GST Registration page title came through), so title extraction is inconsistent rather than fully blocked. |
| HTTP response/status inspection | No | Attempted to get raw HTTP status codes / header data; WebFetch responses never included status codes, `X-Robots-Tag`, or other raw headers — only qualitative "loads successfully" statements from the summarizing model. | No header-capable tool available this session. All status-code claims in this audit are "page content loaded / no error page observed," not confirmed HTTP 200 from a raw response. |
| robots.txt access | Yes | Fetched `https://cashahnawaz.com/robots.txt`, `http://cashahnawaz.com/robots.txt`, and `https://www.cashahnawaz.com/robots.txt` — all three returned identical, valid robots.txt content. | Cannot confirm via WebFetch whether the http/www variants served this directly or were silently redirected first (see domain canonicalization notes). |
| XML sitemap access | Yes | Fetched `sitemap.xml`, `sitemap_index.xml`, `wp-sitemap.xml`, and all 3 child sitemaps (`post-sitemap.xml`, `page-sitemap.xml`, `category-sitemap.xml`) — all returned valid, parseable XML with `<loc>`/`<lastmod>` entries. | `sitemap.xml` and `wp-sitemap.xml` returned content identical to `sitemap_index.xml`; likely server-side redirects/aliases to the Rank Math sitemap, but this could not be confirmed at the header level (see task 2 notes). |
| Following/inspecting internal links | Yes | Extracted main navigation (29 links), footer links (20 links), and in-page internal links from multiple service pages. | Link extraction is from the AI-summarized rendering, not a raw `<a href>` parse — a small number of links could theoretically be missed if visually deprioritized in the source. |
| Terminal access | Yes | Used PowerShell to list the project directory structure (`Get-ChildItem`). | Confirmed for local file/folder operations only; not used and not usable for making HTTP requests to the live site. |
| Running local commands | Yes | Same as above. | N/A |
| Browser automation | No | Not attempted — no browser automation tool is present in this session's tool list, and no screenshot capability exists. | No visual/rendered screenshot of the site could be taken this session. Any visual layout, color, or above-the-fold claim is a limitation, not a finding. |
| Available MCP servers | No SEO-relevant ones | Checked the MCP server list surfaced this session: Asana, Atlassian, Box, Canva, Figma, Gmail, Higgsfield, HubSpot, Intercom, Linear, Notion, Supermetrics, monday.com — all require authorization and none are GSC/GA4/GTM/WordPress connectors. | None usable for this audit even if authorized (wrong tool category). |
| GSC connector | No | No GSC-specific tool appeared in the tool list or deferred-tool search this session. | Per CLAUDE.md, GSC access is never assumed; confirmed not available this session. Mark all GSC-dependent items `DATA NOT AVAILABLE`. |
| GA4 connector | No | Same as above — no GA4 tool present. | `DATA NOT AVAILABLE`. |
| GTM connector | No | Same as above — no GTM tool present. | `DATA NOT AVAILABLE`. |
| WordPress Admin connector | No | No WordPress admin/login tool present; not attempted since no credentials/tool exists this session. | All WordPress facts this session come from live-site fingerprinting only (see `wordpress-fingerprint.md`), never from confirmed admin access. |
| Hosting access connector | No | No hosting/server tool present. | `DATA NOT AVAILABLE`. Cannot confirm PHP version, server config, .htaccess, or raw headers. |
| Lighthouse/PageSpeed connector | No | No performance-testing tool present or found via tool search. | `DATA NOT AVAILABLE`. No Core Web Vitals or PageSpeed data this session. |

## Summary

Working this session: WebFetch (page content, robots.txt, XML sitemaps, internal link extraction), PowerShell (local file operations only).

Not working / not available this session: raw HTTP headers, browser automation/screenshots, GSC, GA4, GTM, WordPress Admin, hosting access, Lighthouse/PageSpeed. This matches the "ground truth" summary provided at the start of this task, and is now independently re-verified rather than assumed.
