# Sitemap Discovery — cashahnawaz.com

Session date: 2026-08-27
Method: WebFetch, fresh this session (not reused from any prior session's data).

## robots.txt directive

`https://cashahnawaz.com/robots.txt` fetched fresh this session — content:

```
User-agent: *
Disallow: /wp-admin/
Disallow: /wp-admin/admin-ajax.php

Sitemap: https://cashahnawaz.com/sitemap_index.xml
```

Confirms the same sitemap directive noted earlier this session; disallow rules only cover `/wp-admin/` and its AJAX endpoint — no accidental blocking of service/content paths detected.

## Sitemap URLs tested (all three attempted, per instructions, even though robots.txt already named one)

| URL tried | Result | Content Type |
|---|---|---|
| `https://cashahnawaz.com/sitemap.xml` | 200 / valid XML | Returned a sitemap index listing the same 3 child sitemaps as `sitemap_index.xml` (post-sitemap.xml, page-sitemap.xml, category-sitemap.xml). Byte-level identity with `sitemap_index.xml` could not be confirmed (WebFetch doesn't expose raw bytes), but the extracted `<loc>` list and generator comment were identical. **LIKELY** this is a server-side alias/redirect to `sitemap_index.xml` rather than a separate file, since Rank Math's canonical sitemap entry point is `/sitemap_index.xml` — not confirmed at the header level (no header inspection tool available). |
| `https://cashahnawaz.com/sitemap_index.xml` | 200 / valid XML | **Confirmed primary sitemap**, matches robots.txt's `Sitemap:` directive. Contains an `<?xml-stylesheet type="text/xsl" href="//cashahnawaz.com/main-sitemap.xsl"?>` reference and an XML comment identifying "Rank Math SEO Plugin" as generator. Lists 3 child sitemaps. |
| `https://cashahnawaz.com/wp-sitemap.xml` | 200 / valid XML | Also returned the same 3-child-sitemap list in the Rank Math naming pattern (`post-sitemap.xml`, `page-sitemap.xml`, `category-sitemap.xml`) rather than WordPress-native naming (`wp-sitemap-posts-post-1.xml`, etc.). This indicates Rank Math has overridden/disabled WordPress's native `wp-sitemap.xml` output and either serves its own sitemap at this URL or redirects to it — exact mechanism (redirect vs. direct override) is **NOT VERIFIABLE** via WebFetch (no raw header/redirect-chain visibility). |

**Conclusion: primary, confirmed-live sitemap = `https://cashahnawaz.com/sitemap_index.xml`** (matches robots.txt directive). Generator: **Rank Math SEO Plugin** (CONFIRMED — named explicitly in an XML comment inside the sitemap file itself, and corroborated by the `rankmath/v1` namespace found in the site's `/wp-json/` REST API discovery document).

## Child sitemaps

| Child sitemap | URLs contained | Lastmod range observed |
|---|---|---|
| `page-sitemap.xml` | 42 | 2024-01-09 to 2026-08-21 |
| `post-sitemap.xml` | 58 | 2022-08-26 to 2026-07-22 |
| `category-sitemap.xml` | 8 | 2026-05-06 to 2026-07-22 |

**Total sitemap-listed URLs: 108** (see note below on one duplicate slug across two child sitemaps).

## Anomaly noted

`https://cashahnawaz.com/trademark-registration/` appears in **both** `page-sitemap.xml` (lastmod 2026-07-22T12:34:02+00:00) and `category-sitemap.xml` (lastmod 2026-05-06T08:26:09+00:00) as the identical URL string. This suggests either a taxonomy term and a page/post share the exact same slug (a common WordPress permalink collision), or the category-sitemap entry is stale/mistaken. This is recorded as an observation only — diagnosing the cause is out of scope for this discovery phase (would route to technical-seo.md).

## Major URL groups visible from sitemap structure

- Core registration/tax/accounting/audit service pages (in `page-sitemap.xml`)
- Industry-specific ITR filing variant pages (9 pages: NRI, content creators/influencers, event management, healthcare, food & beverage, crypto trading, wholesale/retail trade, real estate/construction, e-commerce, beauty & wellness)
- Tax Guides sub-section (`/tax-guides/` index + 7 individual guide articles)
- Blog articles (58, in `post-sitemap.xml`) — mix of case-law summaries, due-date reminders, and general tax/accounting explainer content
- Category/taxonomy archives (8, in `category-sitemap.xml`): `/income-tax/`, `/gst/`, `/mca/`, `/accounting-services-blog/`, `/trademark-registration/` (dup), `/others/`, `/donation/`, `/gst-case-law/`
- Utility/reference pages: `/due-date/` + monthly sub-pages, `/trademark-classes/`, `/career/`, `/privacy-and-policy/`

## WordPress URL structures observed

- Clean "post name" permalinks throughout (no `/?p=123` query-string URLs seen in sitemap or navigation) — **LIKELY** Post name permalink structure is active, consistent with SEO-friendly WordPress setup. Not confirmed via WordPress Admin (no admin access this session).
- `/category/...`-style paths were NOT used; instead the site uses flat top-level slugs for its taxonomy archives (e.g., `/gst/`, `/income-tax/`) rather than the WordPress default `/category/gst/`. This suggests a custom permalink/rewrite structure for the Category taxonomy, or these may be Pages rather than true category archives — **NOT DETERMINED** without admin access; flagged for technical-seo.md to investigate.
- `/wp-json/` REST API root is live and publicly reachable at `https://cashahnawaz.com/wp-json/` (200, JSON response) — confirms WordPress. Not found listed in the sitemap or internal navigation, so no evidence it is being treated as indexable content.
- No `/wp-content/`, `/tag/`, `/author/`, `/?attachment_id=`, or `/page/2/`-style URLs were observed in the sitemap or navigation extraction this session. Their absence from what was surfaced is not proof they don't exist (WebFetch's markdown conversion may not expose asset paths) — see wordpress-fingerprint.md and capability-check.md limitations.

## Domain / protocol canonicalization

| Variant tested | Result |
|---|---|
| `https://cashahnawaz.com/` | Loads homepage content directly. |
| `http://cashahnawaz.com/` | WebFetch auto-upgrades `http://` to `https://` before fetching (documented tool behavior), so this test could not isolate the origin server's own HTTP→HTTPS redirect behavior. Fetching `http://cashahnawaz.com/robots.txt` returned the same content as the https version. |
| `https://www.cashahnawaz.com/` | Returned the same homepage content as the non-www version, with no cross-host redirect notice from WebFetch. |
| `https://www.cashahnawaz.com/robots.txt` | Returned identical content to the non-www robots.txt. |

**Conclusion:** All four tested variants resolve to what appears to be the same site content. **However, the exact mechanism (a real 301/302 redirect vs. the server directly answering all variants vs. WebFetch silently normalizing the request) is NOT VERIFIABLE this session** — WebFetch does not expose raw HTTP status codes or the `Location` header, and its documented "cross-host redirect" notice never appeared during any of these fetches, which is inconclusive rather than proof of "no redirect." This must be flagged as `DATA NOT AVAILABLE` for exact redirect-chain / status-code purposes; a header-capable tool (e.g., `curl -I`, browser dev tools, or a dedicated redirect-checker) is needed for technical-seo.md to state this as confirmed fact.
