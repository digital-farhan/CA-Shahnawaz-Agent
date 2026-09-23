# WordPress Technology Fingerprint — cashahnawaz.com

Session date: 2026-08-27
**Access mode: Fingerprint-only.** No WordPress Admin login was attempted or available this session (no admin/login tool present). Every item below is inferred from live-site evidence (primarily the public `/wp-json/` REST API discovery document plus homepage/interior-page content), not from confirmed admin access. Per wordpress-seo.md's discipline, this must not be upgraded to "confirmed via admin" in any later report without an actual admin session.

## Primary evidence source

`https://cashahnawaz.com/wp-json/` returns a live, public WordPress REST API root discovery document. Quoted fields observed:
- `"name": "Shahnawaz and Associates"`
- `"description": "Chartered Accountant"`
- `"namespaces"` array (48 entries) — full raw list captured:

```
oembed/1.0, contact-form-7/v1, litespeed/v1, litespeed/v3, notibar/v1, oceanwp/v1,
rankmath/v1, rankmath/v1/setupWizard, string-locator/v1, elementor-one/v1,
chatway/v1/user, elementor/v1, jkit/v1, elementskit/v1/ajaxselect2,
rankmath/v1/ai-visibility, rankmath/v1/ca, rankmath/v1/an, rankmath/v1/in,
rankmath/v1/status, elementor/v1/documents, elementor-ai/v1, elementor/v1/feedback,
elementor-pro/v1, elementskit/v1/widget/mailchimp, elementskit/v1/dynamic-content,
elementskit/v1/layout-manager-api, elementskit/v1/my-template, elementskit/v1/megamenu,
elementskit/v1/widget-builder, elementskit/v1, hub-connector/v1, forminator/v1,
eap-accordion/v2, wpmudev_pcs/v1, elementskit, mcp, wp/v2, wp-site-health/v1,
wp-block-editor/v1, wp-abilities/v1
```

## Findings

| Component | Value | Confidence | Evidence |
|---|---|---|---|
| **CMS** | WordPress | **CONFIRMED** | `/wp-json/` REST API root is live and returns a standard WP discovery document with `wp/v2`, `wp-site-health/v1`, `wp-block-editor/v1` namespaces. |
| **SEO plugin** | Rank Math SEO | **CONFIRMED** | (1) XML comment inside `sitemap_index.xml` and all 3 child sitemaps explicitly states "Rank Math SEO Plugin" as generator. (2) `rankmath/v1`, `rankmath/v1/setupWizard`, `rankmath/v1/ai-visibility`, `rankmath/v1/status` namespaces present in `/wp-json/`. No second SEO plugin's namespace (e.g., `yoast`, `aioseo`) was found — no evidence of a conflicting second SEO plugin this session. |
| **Page builder** | Elementor (+ Elementor Pro, Elementor AI) | **CONFIRMED** | `elementor/v1`, `elementor-pro/v1`, `elementor-ai/v1`, `elementor/v1/documents`, `elementor/v1/feedback`, `elementor-one/v1` namespaces present; homepage/interior-page popup CTAs use `elementor-action%3Aaction%3Dpopup`-style URL parameters, consistent with Elementor Pro's popup builder. |
| **Elementor add-ons** | ElementsKit, JetKit (jkit) | **LIKELY** | `elementskit/v1` (with multiple sub-routes: megamenu, widget-builder, mailchimp widget, dynamic-content) and `jkit/v1` namespaces present — both are known third-party Elementor widget-addon plugin families. Not confirmed via admin plugin list. |
| **Theme** | OceanWP | **LIKELY** | `oceanwp/v1` REST namespace present, which is specific to the OceanWP theme's own API routes. Not confirmed via Appearance → Themes (no admin access), so kept at LIKELY rather than CONFIRMED. |
| **Caching / performance plugin** | LiteSpeed Cache | **LIKELY** | `litespeed/v1` and `litespeed/v3` namespaces present, consistent with the LiteSpeed Cache plugin. (This also implies the site is likely hosted on LiteSpeed-compatible infrastructure, though hosting-level confirmation is `DATA NOT AVAILABLE`.) |
| **Form plugin(s)** | Contact Form 7 AND Forminator both appear installed | **POSSIBLE — ambiguous, flagged** | `contact-form-7/v1` and `forminator/v1` namespaces are BOTH present in `/wp-json/`. However, when the visible enquiry form on the homepage, GST Registration page, and Contact page was inspected, **no `wpcf7-form`, `forminator-custom-form`, or other identifying CSS class was surfaced** by WebFetch's extraction (a genuine tool limitation — class attributes are often stripped in markdown conversion). It cannot be determined this session which plugin actually powers the live enquiry form, or whether one of the two is installed-but-inactive/unused. This ambiguity should be resolved by wordpress-seo.md in a later phase before writing form-specific implementation steps (per that skill's explicit warning against mixing instructions across plugins). |
| **Live chat / chat widget plugin** | Chatway | **POSSIBLE** | `chatway/v1/user` namespace present — Chatway is a live-chat widget plugin. No chat widget button/element was actually observed in any fetched page's visible content this session (script-injected widgets are a known WebFetch blind spot — see capability-check.md). Cannot confirm whether it's actively displayed on the live site. |
| **Notification bar plugin** | Likely a "Notification Bar" style plugin | **POSSIBLE** | `notibar/v1` namespace present. No corresponding visible notification bar was observed in fetched content. |
| **Misc / low-relevance plugins detected** | `string-locator` (developer string-search utility), `hub-connector` (theme/plugin hub connector, commonly bundled with multi-plugin theme frameworks), `wpmudev_pcs` (WPMU DEV Plugin/Compatibility service), `eap-accordion` (an accordion/FAQ widget), `mcp` (unclear purpose — possibly a Model Context Protocol integration plugin) | **NOT DETERMINED** (purpose/impact) | Namespace strings observed in `/wp-json/`; no further investigation performed as these are outside Phase 0 discovery scope. |
| **Permalink structure** | Clean "post name"-style permalinks (no `?p=123` query strings observed) | **LIKELY** | Every URL in the sitemap and navigation uses descriptive slugs, not query-string IDs. Not confirmed via Settings → Permalinks (no admin access). |
| **GTM container** | Not detected in fetched content this session | **NOT DETERMINED** | Homepage and Contact Us page were explicitly searched (via a targeted WebFetch prompt) for any `GTM-XXXXXXX` string or `googletagmanager.com` script reference — none was found. **This is NOT evidence that GTM is absent** — WebFetch's HTML-to-markdown conversion does not reliably surface `<script>` tag contents (confirmed limitation, see capability-check.md), so a GTM snippet embedded via `<script>` in the `<head>`/`<body>` could simply be invisible to this extraction method. CLAUDE.md lists container ID `GTM-N2LHGRCX` as believed-connected; this session could neither confirm nor deny its presence on the live site. A raw-HTML or browser-based check is needed to settle this — route to gtm-conversion-audit.md. |
| **Schema/JSON-LD (structured data)** | Not detected in fetched content this session | **NOT DETERMINED** | No `<script type="application/ld+json">` block was surfaced by WebFetch on the homepage, GST Registration page, or Contact page despite Rank Math (which by default injects Organization/LocalBusiness/WebSite schema) being confirmed active. Given the same script-tag extraction limitation noted above for GTM, this must be read as "not captured by this tool," not "confirmed absent." Route a dedicated raw-HTML/view-source check to schema-audit.md before concluding schema is missing. |
| **Meta generator tag / title tag (head-level)** | Not detected on homepage; WAS detected on interior pages | **PARTIAL** | Interior-page title tags (e.g., GST Registration page: "GST Registration Online In Mumbai \| Expert CA Consultant") were successfully surfaced by WebFetch, but the homepage's own `<title>`, meta description, and meta generator tag were NOT surfaced despite a dedicated targeted attempt. This inconsistency (rather than a clean pass/fail) is itself worth noting for on-page-seo.md — it may reflect a genuine difference in how the homepage template renders vs. interior Elementor templates, or simply an extraction artifact. Flagged, not diagnosed. |
| **Plugin conflict (two SEO plugins active)** | No evidence of a second SEO plugin | **LIKELY NOT PRESENT** | Only `rankmath/*` namespaces found; no `yoast`, `aioseo`, `wp-seo`, or similar second-SEO-plugin namespace appeared in the 48-entry list. This is a reasonably strong (though not admin-confirmed) signal against the classic "two SEO plugins active" anti-pattern flagged as CRITICAL in technical-seo.md. |

## Summary for downstream skills

- **wordpress-seo.md** should treat this file as a fingerprint-only starting point and should attempt actual WordPress Admin access (if credentials become available) to upgrade LIKELY/POSSIBLE items to CONFIRMED, particularly: theme identity, form plugin identity, permalink structure, and whether Chatway/notification-bar/ElementsKit/JetKit are actually active vs. merely installed.
- **gtm-conversion-audit.md** should perform its own dedicated GTM-detection pass (ideally with header/raw-HTML or browser-based access) rather than relying on this session's "not detected" result, since that result is confidence-limited by a known tool blind spot, not a clean negative.
- **schema-audit.md** likewise needs a dedicated raw-HTML pass to determine actual JSON-LD presence/correctness — Rank Math being active makes some schema output likely, but this was not observable this session.
