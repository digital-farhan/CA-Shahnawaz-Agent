# CASH AHNAWAZ & ASSOCIATES
## INTERIM WEBSITE & SEO AUDIT REPORT

Website: https://cashahnawaz.com/
Prepared for Website SEO Review & Manual Implementation
Audit Scope: Phases 0, 1A and 1B
Report Date: 2026-08-27

> This is an interim audit report based on the completed audit phases. Additional analysis may be added following Internal Linking, Schema, Performance, Competitor, Local SEO, CRO and analytics audits.

---

## 1. Executive Summary

This report consolidates every audit finding produced to date for **https://cashahnawaz.com/**, a WordPress-based Chartered Accountancy / tax / compliance firm site, across three completed phases:

- **Phase 0 — Discovery:** full sitemap enumeration, technology fingerprinting, and baseline capability assessment.
- **Phase 1A — Technical & WordPress SEO:** crawlability, indexation, sitemap structure, and WordPress/plugin/theme audit.
- **Phase 1B — On-Page & Content Audit:** title/heading/CTA mechanics, content depth and accuracy, priority-service coverage, and content overlap analysis.

No live-site changes have been made or will be made by Claude at any point in this project (see CLAUDE.md's Implementation Policy). Every finding below traces to actual evidence gathered from the live site this session — no keyword, ranking, traffic, conversion, or backlink data exists anywhere in this project, and none is claimed.

### Overall characterization

The website sits on a **clean, low-risk technical and WordPress foundation** with **real, addressable content-accuracy and service-coverage gaps**. These are two different categories of problem, and this report keeps them distinct throughout:

- **Phase 1A (technical/WordPress) found zero CRITICAL and zero HIGH severity issues.** All 8 Phase 1A findings are MEDIUM or LOW — sitemap hygiene items, a footer-link cleanup, and one template-consistency note. Rank Math is confirmed as the sole active SEO plugin with no evidence of a conflicting second SEO plugin, the sitemap is well-formed and correctly segmented, and `robots.txt` has no accidental blocking.
- **All 8 CRITICAL and all 12 HIGH severity findings come from Phase 1B (content and on-page).** These are not structural technical failures — they are content-accuracy issues (stale dates/deadlines presented as current, one wrong firm name in a live FAQ, a self-contradicting figure) and service-coverage gaps (several CLAUDE.md priority services, most notably Private Limited Company Registration, have no dedicated page).

### Findings by severity (39 total tracked findings)

| Severity | Count | Phase 1A (Technical/WordPress) | Phase 1B (On-Page/Content) |
|---|---|---|---|
| CRITICAL | 8 | 0 | 8 |
| HIGH | 12 | 0 | 12 |
| MEDIUM | 14 | 4 | 10 |
| LOW | 5 | 4 | 1 |
| OPPORTUNITY (formal) | 0 | 0 | 0 |
| **Total** | **39** | **8** | **31** |

8 additional **informal enhancement opportunities** (not defects, not formal findings) are documented in `implementation/CONTENT-ACTION-PLAN.md`'s Opportunity tier — e.g., a possible standalone Bookkeeping page, a Tax Audit/Statutory Audit title-tag consideration. These are separate from the 39 tracked findings.

### Genuine strengths (verified, not assumed)

- **CMS and SEO plugin are clean and unambiguous.** WordPress (CONFIRMED), Rank Math SEO (CONFIRMED, sole active SEO plugin — no second-plugin conflict signature found).
- **Sitemap structure is well-formed.** `sitemap_index.xml` correctly segments 108 URLs across `page-sitemap.xml`, `post-sitemap.xml`, and `category-sitemap.xml`; `robots.txt` blocks nothing it shouldn't.
- **No priority service page was found noindexed, blocked, or in an error state.**
- **Strong content depth on several flagship pages:** GST Registration (documents table, 5-Q&A FAQ, and the site's clearest published fee — the only pages this transparent are 2 of 13); NRI Taxation (15 H2 sections covering DTAA treaties, FEMA, residential-status determination, and case law); the Section 8 Company + 12A/80G pair, which accurately maps the real two-step NGO formation-then-exemption lifecycle.
- **Accounting and Audit are cleanly differentiated** — confirmed zero cross-mentions of Tax/Statutory/Internal Audit on the Accounting Services page, clearing a conflation risk common on thin CA-firm sites.
- **All 13 Tier 1 (highest-commercial-value) pages received full content-quality review** — the highest-confidence coverage tier in this audit.

### Main areas requiring attention

1. **Content accuracy on regulated/financial content.** 15 items across the site carry a `PROFESSIONAL / CURRENT REGULATORY VERIFICATION REQUIRED` flag — dates, deadlines, and thresholds that are either confirmed stale or lack a currency signal. This is the single largest concentration of risk in the audit.
2. **Priority service coverage gaps.** Of the services named in CLAUDE.md, 12 have no dedicated page — most severely **Private Limited Company Registration**, the dominant entity type for Indian SMEs, which has zero coverage despite less-common entity types (Public Limited, Section 8) being fully built out.
3. **Trust-signal gaps.** No individually named, checkable CA/CS credential exists anywhere on the site; the homepage's own "TESTIMONIALS" section renders empty; 8 of 13 Tier 1 pages carry no testimonials at all.
4. **Minor technical hygiene.** A likely page/taxonomy slug collision, outdated footer links, and two thin category archives — all MEDIUM or LOW, all straightforward to fix.

### Immediate priorities

1. Correct the wrong firm name ("TAXZONA Consultancy") published in the Accounting Services FAQ — a single-sentence fix with outsized trust impact.
2. Route the three stale Tier 1 compliance pages (ITR Mumbai, LLP Annual Filing, 12A/80G) and three stale Tier 3 due-date articles to a qualified CA/tax professional for verification and relabeling.
3. Resolve the Public Limited Company page's self-contradicting paid-up-capital figures.
4. Begin scoping a dedicated Private Limited Company Registration page — the highest-priority content gap identified.

---

## 2. Audit Objectives

Per CLAUDE.md's Main SEO Goal, this audit (and the eventual implementation it supports) exists to help the firm:

- Rank higher in Google for its priority services.
- Increase qualified organic traffic.
- Improve website engagement and user numbers.
- Increase form submissions and genuine (non-spam) enquiries.
- Improve phone and WhatsApp contacts.
- Improve visibility and conversion for all 25 priority services named in CLAUDE.md, including registration and compliance services.

Every finding in this report is mapped to the stage(s) of the site's success funnel it affects, so recommendations tie to a business outcome rather than a technical checkbox in isolation:

```
Organic Visibility
↓
Qualified Traffic
↓
Relevant Service Page
↓
Trust & Engagement
↓
Contact / Form Submission
↓
Genuine Enquiry
```

A technical crawlability issue typically affects the top of this funnel (Organic Visibility). A stale FAQ or a self-contradicting figure typically affects the middle-to-bottom (Trust & Engagement, Genuine Enquiry) — a visitor who already found the page loses confidence at the exact point they would otherwise convert. A missing service page affects the very top — the visitor never reaches the site at all for that query.

---

## 3. Audit Scope & Methodology

**Method used throughout:** WebFetch (AI-summarized HTML→markdown extraction) against live URLs — no browser automation, no raw HTTP header inspection, no guaranteed JavaScript rendering. PowerShell was used only for local file operations, never against the live site. No GSC, GA4, GTM, WordPress Admin, or hosting connector was available in any session to date; each was independently re-verified as unavailable rather than assumed (see `reports/00-capability-check.md`).

| Audit Area | Status | Coverage |
|---|---|---|
| Website Discovery | Completed | 111 URLs discovered (108 sitemap + 3 footer-only), full sitemap enumeration |
| Technical SEO | Completed (Phase 1A) | 53/111 URLs (48%) individually fetched this phase; 100% of Tier 1 + Tier 2; Tier 3 sampled 15/66 (23%) |
| WordPress SEO | Completed (Phase 1A) | Fingerprint-only evidence (public REST API + sitemap comments) — no admin access |
| On-Page SEO | Completed (Phase 1B) | Tier 1: 13/13 (100%) full content-quality review; Tier 2: title-level only (1/15 content-quality pass); Tier 3: partial sample |
| Content Audit | Completed (Phase 1B) | Same coverage pattern as On-Page SEO above |
| Service Coverage | Completed (Phase 1B) | All named CLAUDE.md priority services classified (see Section 9) |
| GSC | Data Not Available | No connector this session |
| GA4 | Data Not Available | No connector this session |
| GTM | Data Not Available | No connector this session |
| Performance / Core Web Vitals | Data Not Available | No testing tool this session |
| Internal Linking | Not Yet Audited | Scheduled next phase |
| Schema | Not Yet Fully Audited | JSON-LD presence not visible this session (tool limitation, not confirmed absence) |
| Competitor Analysis | Not Yet Audited | Scheduled future phase |
| Local SEO | Not Yet Audited | Scheduled future phase |
| CRO | Not Yet Fully Audited | Content-alignment only checked (Section 9 of `reports/03-on-page-seo.md`); design/UX-level CRO not performed |

**Cumulative individual-fetch coverage across both phases: 62 of 111 URLs (56%).** Tier 1 (13 URLs) is at 100% depth on both technical and content-quality dimensions — the highest-confidence tier in this audit. Tier 2 (15 URLs) is at 100% title-level verification but only 1 of 15 received a full content-quality pass. Tier 3 (66 blog/article URLs) is a disclosed 35% sample (23 of 66), not a full crawl.

**Key limitation carried through every phase:** WebFetch's HTML→markdown conversion does not reliably surface `<head>`/`<script>`-level content. Meta robots tags, canonical tag targets, and JSON-LD structured data were `NOT VISIBLE` on effectively every fetch this session, sitewide — this is treated throughout as a tool limitation, never as evidence that these elements are absent. See Section 14 for the full limitations list.

---

## 4. Website Discovery Overview

| Item | Finding | Confidence |
|---|---|---|
| CMS | WordPress | **CONFIRMED** — public `/wp-json/` REST discovery document; site name "Shahnawaz and Associates," description "Chartered Accountant" |
| SEO plugin | Rank Math SEO | **CONFIRMED** — named explicitly in an XML comment inside `sitemap_index.xml` and all 3 child sitemaps, corroborated by `rankmath/v1` REST namespaces. No second SEO plugin's namespace (Yoast, AIOSEO) found — LIKELY not a plugin-conflict situation |
| Page builder | Elementor + Elementor Pro + Elementor AI | **CONFIRMED** — REST namespaces present; popup CTAs use Elementor Pro popup-action URL parameters |
| Theme | OceanWP | **LIKELY** — REST namespace only, not admin-confirmed |
| Caching | LiteSpeed Cache | **LIKELY** — REST namespace only |
| Form plugin | Contact Form 7 and/or Forminator | **POSSIBLE, ambiguous** — both namespaces present in `/wp-json/`; which actually renders the live enquiry form (or whether it's native Elementor Forms) could not be determined |
| GTM container / JSON-LD schema | Not detected in any fetch | **NOT DETERMINED** — actively searched for, not found; this is a known WebFetch blind spot, not confirmed absence |

**Sitemap:** `sitemap_index.xml` confirmed live and Rank Math-generated. Lists 3 child sitemaps: `page-sitemap.xml` (42 URLs), `post-sitemap.xml` (58 URLs), `category-sitemap.xml` (8 URLs) — 108 URLs total. `sitemap.xml` and `wp-sitemap.xml` return identical content, likely aliases, but the exact mechanism (redirect vs. multiple live origins vs. tool normalization) is `RAW HEADER / REDIRECT VERIFICATION NOT AVAILABLE`.

**Total URL inventory: 111** (108 sitemap-listed + 3 footer-linked URLs absent from every sitemap). One duplicate is present: `/trademark-registration/` appears as both a page and a category-archive entry (see TECH-001, Section 5).

**Coverage tier breakdown:**

| Tier | URLs | Individually Verified |
|---|---|---|
| Tier 1 — Critical Commercial | 13 | 13/13 (100%) |
| Tier 2 — Supporting | 15 | 15/15 title-level (100%); 1/15 content-quality |
| Tier 3 — Blog/Article | 66 | 23/66 (35%), disclosed sample |
| Not Prioritized (legal/tools/archives) | 18 | Sitemap metadata only |

**URLs individually fetched across both phases: 62 of 111 (56%).** The remaining 44% rely on XML sitemap metadata (URL + lastmod) only, with no independently confirmed live content, status, or on-page elements.

---

## 5. Technical SEO Findings

**7 TECH findings total (from Phase 1A). 0 CRITICAL, 0 HIGH — all TECH findings are MEDIUM or LOW.** No priority service page was found noindexed, blocked, or in an error state.

### A. Confirmed Issues

#### [MEDIUM] TECH-003 — Two thin, single-item category archives indexed via the sitemap
- **Confidence:** CONFIRMED
- **Affected Area:** `https://cashahnawaz.com/mca/`, `https://cashahnawaz.com/donation/`
- **Evidence Summary:** Both are listed in `category-sitemap.xml` but each resolves to exactly one post, with no pagination — versus 8–10 items on the site's other 5 checked category archives.
- **SEO Impact:** Crawlability/Indexability. Thin single-item archives are classic low-value indexed content that can dilute overall site quality signals; "MCA" also maps to a priority-service group, so this is an under-built opportunity as well as a hygiene issue.
- **Recommended Fix:** Exclude both taxonomies from the XML sitemap, merge each single article into a broader category with a redirect, or build out substantive content for `/mca/` given its priority-service relevance.
- **Manual Implementation Guide:** In Rank Math → Sitemap Settings → Taxonomies, toggle off sitemap inclusion for the `mca` and `donation` terms; alternatively, in Rank Math → Titles & Meta → Taxonomies, set a noindex directive on these two terms while keeping the archive reachable to visitors.
- **Validation:** Re-fetch `category-sitemap.xml` and confirm the toggled term(s) no longer appear.
- **Evidence Source:** `data/crawl/_batch-b-archives-footer.md`.

#### [MEDIUM] TECH-004 — Stale, deadline-specific compliance content live and indexed with no visible currency update
- **Confidence:** CONFIRMED
- **Affected Area:** `https://cashahnawaz.com/gst-amnesty-scheme-2023/`, `https://cashahnawaz.com/big-relief-for-taxpayers-whose-gst-number-got-canceled-due-to-non-filing-of-gst-returns/`
- **Evidence Summary:** The GST amnesty article's title, H1, and body are entirely anchored to a window its own text states closed 30 June 2023, with no visible revision — yet its sitemap `lastmod` (2026-05-06) is roughly 3 years newer than the deadline it describes as closed.
- **SEO Impact:** Organic Visibility and Qualified Traffic. Indexed pages describing expired deadlines without an "ended" notice risk misleading a searcher landing via a stale ranking.
- **Recommended Fix:** Add a clear "this scheme window has closed" notice at the top of both articles; route to a full content-currency review.
- **Manual Implementation Guide:** In the WordPress/Elementor editor, add a dated update notice block at the top of each article's content before any other page edits.
- **Validation:** Re-fetch both URLs and confirm the notice is visible in the rendered content.
- **Evidence Source:** `data/crawl/_batch-c-tier3-sample.md`.

#### [LOW] TECH-006 — Mixed `http://`/`https://` scheme in internal link hrefs
- **Confidence:** CONFIRMED
- **Affected Area:** Sitewide (footer links specifically confirmed; broader scope not independently verified)
- **Evidence Summary:** Multiple internal links (e.g., footer links to Contact Us, Accounting Services) use a literal `http://` scheme despite the site serving exclusively over HTTPS.
- **SEO Impact:** Crawlability. Each `http://` link forces an extra redirect hop (assuming HTTPS enforcement is in place, itself unconfirmed), diluting link equity slightly and adding avoidable crawl overhead.
- **Recommended Fix:** Bulk-update all internal hrefs to `https://`.
- **Manual Implementation Guide:** Use a database-safe search-and-replace tool (e.g., "Better Search Replace" plugin, safe for serialized Elementor JSON) to replace `http://cashahnawaz.com` with `https://cashahnawaz.com` across post/page content and Elementor templates; separately review Appearance → Menus for manually-entered `http://` URLs.
- **Validation:** Re-fetch the footer and main navigation and confirm all internal hrefs now read `https://`.
- **Evidence Source:** `data/crawl/site-inventory-notes.md`; `data/crawl/_batch-b-archives-footer.md`.

### B. Likely Risks

#### [MEDIUM] TECH-001 — `/trademark-registration/` page/taxonomy slug collision in the sitemap
- **Confidence:** LIKELY
- **Affected Area:** `https://cashahnawaz.com/trademark-registration/`
- **Evidence Summary:** The identical URL is listed in both `page-sitemap.xml` (lastmod 2026-07-22) and `category-sitemap.xml` (lastmod 2026-05-06), with conflicting freshness signals. Live content resolves as single-article-style, not a multi-item taxonomy listing.
- **SEO Impact:** Crawlability/Indexability. Conflicting sitemap signals for one URL can confuse how Google associates freshness/content-type with the page.
- **Recommended Fix:** Confirm the collision in WordPress Admin, then rename the taxonomy term's slug and redirect if it was ever independently indexed.
- **Manual Implementation Guide:** In WordPress Admin, check Pages/Posts and Categories/Taxonomies for a `trademark-registration` slug on both. If both exist, rename the taxonomy term's slug (e.g., `trademark-registration-articles`) via the standard category-edit screen; if the old slug was ever separately indexed, add a redirect via Rank Math → Redirections (module must be enabled first under Rank Math → Dashboard → Modules).
- **Validation:** Re-fetch `category-sitemap.xml` and confirm `/trademark-registration/` no longer appears there under the renamed term.
- **Evidence Source:** `data/crawl/sitemap-discovery.md`; `data/crawl/phase-1a-sitemap-audit.md` Section 4.

#### [MEDIUM] TECH-002 — Three footer-linked URLs point to outdated/mistyped slugs not present in the XML sitemap
- **Confidence:** LIKELY
- **Affected Area:** `http://cashahnawaz.com/project-business/trademark-registration/`, `http://cashahnawaz.com/income-tax-return-filling-in-mumbai/` (typo "filling"), `http://cashahnawaz.com/online-tds-return-filing/`
- **Evidence Summary:** All three load live content matching an existing, correctly-slugged sitemap page, but whether they are separate live duplicate pages or silently redirect could not be confirmed (no raw HTTP header tool available).
- **SEO Impact:** Crawlability/Indexability, and potentially Duplicate Content. A sitewide, high-frequency link position (the footer) is spending link equity on outdated URLs.
- **Recommended Fix:** Update footer hrefs to the current, correctly-slugged `https://` URLs; separately confirm via WordPress Admin whether the old slugs still resolve to live content (redirect/noindex if so).
- **Manual Implementation Guide:** In WordPress Admin → Appearance → Menus (or the Elementor footer template), locate the three footer links and update their hrefs to `https://cashahnawaz.com/trademark-registration/`, `https://cashahnawaz.com/income-tax-return-filing-in-mumbai/`, and `https://cashahnawaz.com/tds-return-filing-services/` respectively.
- **Validation:** Re-fetch the site footer and confirm all links use `https://` and current slugs; re-fetch the three old URLs and confirm they either 301 to the correct page or return a clean 404/410.
- **Evidence Source:** `data/crawl/site-inventory-notes.md`; `data/crawl/_batch-b-archives-footer.md` Part 2.

### C. Possible Risks

#### [LOW] TECH-005 — Possible keyword cannibalization: GST registration blog article vs. Tier 1 service page
- **Confidence:** POSSIBLE
- **Affected Area:** `https://cashahnawaz.com/how-to-file-gst-registration-process-benefits-penalty/` (blog, lastmod 2022-10-31) vs. `https://cashahnawaz.com/gst-registration-online/` (Tier 1, lastmod 2026-06-18)
- **Evidence Summary:** Both cover the same threshold/documents/process/penalty topics for the same core "how to register for GST" intent, with the older article offering no clearly distinct angle.
- **SEO Impact:** Organic Visibility. If both target similar intent, they may split ranking signals — a content-overlap observation, not a confirmed ranking-dilution finding (no GSC query data available).
- **Recommended Fix:** Route to a content-strategy decision: differentiate the blog article's intent explicitly, or merge/redirect it into the service page.
- **Validation:** Once GSC query-level data becomes available, check whether both URLs appear for overlapping queries.
- **Evidence Source:** `data/crawl/_batch-c-tier3-sample.md`.

#### [LOW] TECH-007 — `/tax-case-law/` index page may be under-populated relative to sitemap-listed case-law articles
- **Confidence:** POSSIBLE
- **Affected Area:** `https://cashahnawaz.com/tax-case-law/`
- **Evidence Summary:** The index page fetch surfaced only 1 case-law item, while the sitemap lists approximately 19 distinct case-law URLs. Could reflect a genuine content gap or a fetch/extraction limitation.
- **SEO Impact:** Crawlability (internal linking specifically) — if genuinely under-populated, ~18 case-law articles rely entirely on the sitemap and category archive for discovery.
- **Recommended Fix:** Manually re-check the page in a browser to confirm whether more items exist below the fold; if genuinely under-populated, add the missing articles to the index.
- **Validation:** Direct browser or raw-HTML re-check of the page.
- **Evidence Source:** `data/crawl/_batch-a-tier1-tier2.md`.

### D. Technical Limitations (sitewide, `DATA NOT AVAILABLE` this session)

| Data source | Status |
|---|---|
| Raw HTTP response headers (status codes, `X-Robots-Tag`, redirects) | DATA NOT AVAILABLE |
| Browser automation / rendered screenshots | DATA NOT AVAILABLE |
| Meta robots tag content (sitewide) | NOT VISIBLE (tool limitation) |
| Canonical tag target (sitewide) | NOT VISIBLE (tool limitation) |
| JSON-LD / structured data presence (sitewide) | NOT VISIBLE (tool limitation) |
| JS-rendered / client-side-injected content | DATA NOT AVAILABLE |
| GSC / GA4 / GTM | DATA NOT AVAILABLE |
| WordPress Admin / hosting access | DATA NOT AVAILABLE |
| Lighthouse / PageSpeed / Core Web Vitals | DATA NOT AVAILABLE |

`robots.txt` (confirmed, for contrast — this one item IS fully verified):
```
User-agent: *
Disallow: /wp-admin/
Disallow: /wp-admin/admin-ajax.php

Sitemap: https://cashahnawaz.com/sitemap_index.xml
```
No accidental blocking of content/service paths was found.

---

## 6. WordPress SEO Findings

**Access mode: fingerprint-only.** No WordPress Admin login was attempted or available in any session — every fact below is inferred from public live-site evidence (the `/wp-json/` REST discovery document, sitemap XML comments, and rendered page content), never from confirmed admin access.

### Rank Math (SEO Plugin)

**Identity: CONFIRMED.** No second SEO plugin's namespace (Yoast, AIOSEO) was found among 48 REST namespaces — LIKELY NOT a plugin-conflict situation, though not admin-confirmed.

| Item | Status | Confidence |
|---|---|---|
| Sitemap config (page/post/taxonomy correctly separated) | Page/post/taxonomy sitemaps cleanly split | CONFIRMED |
| Taxonomy sitemap inclusion | Present, but includes 2 thin single-item archives (see TECH-003) | CONFIRMED |
| Schema output (JSON-LD) | Not surfaced on any of 53+ fetches despite Rank Math injecting schema by default | NOT VISIBLE — tool limitation, not confirmed absence |
| Canonical output | Not surfaced on any fetch | NOT VISIBLE — tool limitation |
| Robots meta output | Not surfaced on any fetch | NOT VISIBLE — tool limitation |
| Breadcrumb signals | No breadcrumb trail reported in any fetch | NOT DETERMINED |
| Duplicate schema risk (theme vs. plugin) | Cannot be assessed without visible schema output | NOT DETERMINED |

**Modular-plugin note:** Rank Math ships modularly — its Redirections and Schema Generator modules must be individually enabled under Rank Math → Dashboard → Modules before the corresponding menu items exist. This should be confirmed before executing any Implementation Step above that references Redirections.

### Elementor (Page Builder)

**Identity: CONFIRMED** (`elementor/v1`, `elementor-pro/v1`, `elementor-ai/v1` namespaces; popup CTAs use Elementor Pro popup-action URL parameters). Likely add-ons: ElementsKit, JetKit — **LIKELY**, not admin-confirmed.

#### [LOW] WP-001 — Inconsistent content template across ITR industry-specific pages
- **Confidence:** CONFIRMED
- **Affected URLs:** `https://cashahnawaz.com/itr-filing-for-event-management-and-entertainment-professionals/`, `https://cashahnawaz.com/itr-filing-for-content-creators-influencers/`
- **Evidence Summary:** 2 of the 9 industry-specific ITR filing pages use an older, shorter Elementor template ("Introduction / Who Should File / 5 Important Case Laws / Practical Checklist") than the other 7, which share a newer, more comprehensive template referencing "Income Tax Act 2025," presumptive taxation, MSME compliance, and compliance calendars.
- **SEO Impact:** Organic Visibility and Engagement. The 2 outlier pages likely offer thinner topical coverage than their 7 siblings.
- **Recommended Fix:** Rebuild the 2 outlier pages using the 7-page family's template/section structure.
- **Manual Implementation Guide:** In Elementor, open one of the 7 up-to-date pages, use "Save as Template" (Elementor Pro), then apply that template to the 2 outlier pages, replacing content section-by-section with industry-specific detail.
- **Validation:** Re-fetch both outlier URLs and confirm the H2 structure matches the 7-page family's pattern.
- **Evidence Source:** `data/crawl/_batch-a-tier1-tier2.md`.

### Theme, Caching, and Forms

| Component | Status | Confidence |
|---|---|---|
| Theme (OceanWP) | REST namespace only, not admin-confirmed | LIKELY |
| Caching (LiteSpeed Cache) | REST namespace only; plugin presence alone cannot confirm actual performance impact | LIKELY |
| Form plugin (Contact Form 7 vs. Forminator vs. native Elementor Forms) | Both CF7 and Forminator namespaces present in `/wp-json/`; no distinguishing CSS class surfaced on any of 53+ fetches; namespace presence proves installation, not which plugin (if either) actually renders the live form | **POSSIBLE, ambiguous** |
| Permalink structure | Clean "post name"-style permalinks sitewide, no `?p=123` seen | LIKELY (not admin-confirmed) |
| Live chat (Chatway) | Namespace present; no widget visually confirmed | POSSIBLE |
| Notification bar | Namespace present; no bar observed | POSSIBLE |
| GTM container (`GTM-N2LHGRCX` per CLAUDE.md) | Not detected in any fetch | NOT DETERMINED — not a confirmed absence |

**Why this matters for implementation:** The form-plugin ambiguity must be resolved via WordPress Admin (Plugins list + inspecting a live form's rendered HTML class names) before any form-specific step (e.g., a GTM form-submission trigger keyed to a specific plugin's event) is attempted — this is an explicit blocker for the future GTM Conversion Audit phase.

### Items requiring WordPress Admin verification

- Theme identity (OceanWP → CONFIRMED)
- Form plugin identity (CF7 vs. Forminator vs. native Elementor Forms)
- The TECH-001 trademark-registration slug collision
- The OP-002 "LLP Registration" nav-link label/target
- Whether Rank Math's Redirections and Schema Generator modules are enabled
- Actual Rank Math schema/canonical/robots-meta output (requires raw-HTML or admin view)

---

## 7. On-Page SEO Findings

**Coverage:** All 13 Tier 1 pages received a full content-quality deep review this phase, on top of Phase 1A's title/H1-level check — the highest-confidence tier in this audit. Tier 2 remains at title-level only (1 of 15 pages received a content-quality pass). Tier 3 remains a 35% sample.

**No keyword volume, ranking, or GSC/GA4 data was available or used anywhere in this section.** Every search-intent statement is labeled `LIKELY USER SEARCH INTENT`; `SEARCH DEMAND DATA NOT AVAILABLE` applies wherever keyword-volume evidence would otherwise be needed.

### Strengths observed across Tier 1

- Logical, scannable H2/H3 structure on nearly every page; FAQ sections present on 12 of 13 pages.
- Strong internal linking from the 9 industry ITR pages, NRI Taxation, and TDS pages into the main ITR Mumbai hub.
- Two pages (Audit Services, LLP Annual Filing) show genuinely good practice not replicated elsewhere: Audit Services carries an explicit disclaimer; LLP Annual Filing has the only "Why us" trust section in the batch.

### Common weaknesses across Tier 1

- **Pricing disclosure is inconsistent with no discernible logic** — only 2 of 13 pages state an actual price (OP-003).
- **Trust signals are thin and uneven** — no individually named, checkable credential anywhere; testimonials are duplicated near-verbatim across 4 pages while 8 of 13 pages have none at all (OP-005).
- **The enquiry form is never pre-contextualized per page** — the same generic Name/Email/Mobile/City/Service-dropdown form appears everywhere, never defaulting to the page's own service.
- **Title/meta/canonical/JSON-LD content is `NOT VISIBLE`** on every fetch this session (tool limitation) — no on-page finding in this report asserts a specific title tag, meta description, or canonical target beyond what was directly captured for a small number of pages (noted per-page below where available).

### Tier 1 Page-by-Page Summary

| URL | Primary Service | Current Status | Main Issue / Opportunity | Recommended Action |
|---|---|---|---|---|
| `/` (Homepage) | Brand/navigational hub | ADEQUATE | Empty "TESTIMONIALS" section (OP-004); top CTA strip omits GST Registration, GST Return Filing, Audit Services (OP-006) | KEEP AND OPTIMIZE |
| `/gst-registration-online/` | GST Registration | STRONG | Misplaced return-filing sentence (OP-008); rupee figures lack a currency date-stamp (CONT-012) | KEEP AND OPTIMIZE |
| `/gst-return-filing/` | GST Return Filing | ADEQUATE | "Get a Free Quote" CTA with zero pricing content anywhere on the page; unverified anchor target (CONT-023) | EXPAND EXISTING PAGE |
| `/income-tax-return-filing-in-mumbai/` | Income Tax Return Filing | NEEDS IMPROVEMENT | Stale "Assessment Year 2020-21" FAQ reference (CONT-002, CRITICAL) | PROFESSIONAL ACCURACY REVIEW REQUIRED |
| `/itr-filing-for-nri-guide-for-non-resident-taxation/` | NRI Taxation | NEEDS IMPROVEMENT | No FAQ, no pricing, zero testimonials for the most trust-barrier-sensitive audience on the site; Act-2025 citations need review (CONT-011) | EXPAND EXISTING PAGE / PROFESSIONAL ACCURACY REVIEW REQUIRED |
| `/accounting-services/` | Accounting | NEEDS IMPROVEMENT | Wrong firm name "TAXZONA Consultancy" in live FAQ (CONT-001, CRITICAL) | KEEP AND OPTIMIZE — fix firm name immediately |
| `/audit-services/` | Tax Audit / Statutory Audit | ADEQUATE | Internal Audit reduced to a one-row table mention (CONT-017); zero testimonials; unattributed "UDIN-verified" credential; Act-2025 citations need review (CONT-011) | PROFESSIONAL ACCURACY REVIEW REQUIRED |
| `/startup-registration-india/` | Startup Registration | ADEQUATE | No trust signals at all; unqualified ₹100 crore / 10-year eligibility figures | KEEP AND OPTIMIZE; verify figures |
| `/section-8-company-registration/` | NGO Registration (formation) | STRONG | No trust signals; unqualified penalty figures; no reciprocal link to 12A/80G | KEEP AND OPTIMIZE; verify figures |
| `/public-limited-company/` | Company Registration | NEEDS IMPROVEMENT | Self-contradicting minimum paid-up-capital figures (OP-001, HIGH); also evidences the CRITICAL Private Ltd Co coverage gap (CONT-014) | PROFESSIONAL ACCURACY REVIEW REQUIRED |
| `/llp-annual-filing/` | ROC/Annual Compliance (LLP) | NEEDS IMPROVEMENT | "Final Year 2021-22" table presented as current (CONT-003, CRITICAL); possible mislabeled nav link (OP-002, HIGH) | PROFESSIONAL ACCURACY REVIEW REQUIRED |
| `/tds-return-filing-services/` | TDS Return Filing | ADEQUATE | Claims rates vary but never shows a rate table (one exists unlinked on a separate blog article); no trust signals | KEEP AND OPTIMIZE |
| `/12a-or-12aa-or-80g-registration-new-scheme/` | NGO Registration (tax exemption) | NEEDS IMPROVEMENT | Passed 2021–2022 transitional deadlines shown without historical framing (CONT-004, CRITICAL); H1 narrower than actual page scope (OP-007) | PROFESSIONAL ACCURACY REVIEW REQUIRED |

### On-Page Findings Index (OP-001–OP-008)

| ID | Severity | Confidence | Finding | Recommended Fix |
|---|---|---|---|---|
| OP-001 | HIGH | CONFIRMED | Public Limited Company page states two contradictory minimum paid-up capital figures ("Rs 5 lakhs" vs. "no minimum") | Verify current rule with a qualified professional; reconcile both sections to one figure |
| OP-002 | HIGH | LIKELY | Possible mislabeled nav link "Limited Liability Partnership Registration" resolves to the compliance-only LLP Annual Filing page | Verify the nav link's actual label/target in WP Admin; relabel or retarget |
| OP-003 | MEDIUM | CONFIRMED | Inconsistent pricing disclosure across Tier 1 pages — only 2 of 13 show a price, no discernible logic | Make one deliberate sitewide pricing-disclosure decision and apply it consistently |
| OP-004 | HIGH | LIKELY | Homepage's own "TESTIMONIALS" section renders with no populated content | Confirm via live browser check; populate with existing real testimonials if genuinely empty |
| OP-005 | MEDIUM | CONFIRMED | Same 6 testimonials reused near-verbatim across 4 pages; NRI Taxation and Audit Services have zero | Add genuine testimonials to NRI/Audit pages; vary selection across pages |
| OP-006 | MEDIUM | CONFIRMED | Homepage top CTA strip omits GST Registration, GST Return Filing, and Audit Services | Expand the CTA strip to represent all 5 CLAUDE.md priority groups at parity |
| OP-007 | MEDIUM | CONFIRMED | 12A/80G page's H1 ("12A Registration Online") is narrower than its actual scope (also covers 80G/12AA) | Update H1 to reflect the full scope |
| OP-008 | LOW | CONFIRMED | Misplaced sentence on GST Registration page describing GST Return Filing turnaround | Remove or correct the misplaced sentence |

Full evidence, SEO Impact, and step-by-step Manual Implementation Guide for each finding above is preserved in `reports/03-on-page-seo.md` and `implementation/MASTER-ISSUE-TRACKER.md`.

---

## 8. Content Audit

**Coverage discipline:** This section owns content depth, freshness/accuracy, coverage gaps, cannibalization/overlap, and trust/E-E-A-T substance. Title/meta/heading mechanics belong to Section 7. No specific tax rate, due date, threshold, or legal figure is asserted as currently correct or incorrect anywhere in this report — every staleness finding quotes the exact on-page evidence and routes to professional verification.

### Strong content areas (named specifically)

- **GST Registration:** a documents-required table, a 5-question FAQ, and the site's clearest published fee (Rs 1,500) — the only page besides ITR Mumbai this transparent on pricing.
- **NRI Taxation:** 15 H2 sections including Residential Status Determination, NRO/NRE/FCNR matrix, DTAA Treaties, NRI TDS Matrix, FEMA & Banking Regulations, and case law — genuinely NRI-specific, not a generic ITR reskin.
- **Section 8 Company Registration:** the deepest ongoing-compliance content in the batch, going beyond formation into post-registration obligations.
- **The Section 8 ↔ 12A/80G pair:** accurately represents the real two-step NGO lifecycle (form the company, then obtain tax exemption) — genuinely complementary coverage, not artificial splitting.
- **Accounting Services:** cleanly differentiated from Audit (zero cross-mentions confirmed), with dedicated sections for Bookkeeping, Financial Reporting, and Outsourced Accounting that fully satisfy those three CLAUDE.md priority services without a separate page.

### Content freshness — 15 items requiring professional verification

**`LIKELY OUTDATED` (8 items) — passed deadlines/years presented without historical framing:**

| # | URL | Issue |
|---|---|---|
| 1 | `/gst-amnesty-scheme-2023/` | Deadline closed 30 June 2023, lastmod ~3 years newer, no revision visible (TECH-004) |
| 2 | `/big-relief-for-taxpayers-whose-gst-number-got-canceled.../` | Deadline closed 30 June 2023 (TECH-004) |
| 3 | `/gst-new-update-due-dates-for-october-2021/` | October 2021 dates, ~5 years stale, no disclaimer (CONT-005) |
| 4 | `/due-date-calendar-for-the-month-of-november-2022/` | November 2022 dates, no disclaimer (CONT-006) |
| 5 | `/waiver-of-late-fees-for-gst-annual-return/` | Article's own text confirms the waiver window closed 31 March 2025 (CONT-007) |
| 6 | `/income-tax-return-filing-in-mumbai/` (FAQ) | Cites "Assessment Year 2020-21" inside FY2025-26/2026-27-framed content (CONT-002) |
| 7 | `/llp-annual-filing/` | H2 titled "LLP Compliance (The Final Year 2021-22)"; AY2021-22 threshold framing (CONT-003) |
| 8 | `/12a-or-12aa-or-80g-registration-new-scheme/` | Passed 2021–2022 transitional deadlines shown without historical framing (CONT-004) |

**`TIME-SENSITIVE — REVIEW REQUIRED` (9 items) — a figure/date present but currency not confirmable from the page alone:** `/key-recommendations-of-45th-gst-council-meeting/` (CONT-008), `/june-2026-important-due-dates/` (CONT-009), `/old-vs-new-tax-regime-.../` slab table with no FY/AY label (CONT-010), plus unqualified monetary thresholds/penalties on GST Registration, GST Return Filing, Startup Registration, Section 8 Company, TDS Return Filing, and Public Limited Company (consolidated as CONT-012).

**`PROFESSIONAL / CURRENT REGULATORY VERIFICATION REQUIRED` (1 consolidated item):** ITR Mumbai, NRI Taxation, and Audit Services all cite the "New Income Tax Act 2025" alongside old Income Tax Act 1961 section numbers in direct cross-mappings — the highest-density regulatory-risk pattern in the audit, formalized as one consolidated review item (CONT-011) rather than three separate checks.

**`CURRENTLY APPEARS EVERGREEN` (2 items — positive controls):** `/tds-chart-for-fy-2026-27/` and `/accounting-services/` are both internally date-consistent — included as contrast, not as confirmation that their underlying figures are currently correct.

### Pages needing improvement

Accounting Services (firm-name fix, CONT-001), ITR Mumbai / LLP Annual Filing / 12A-80G (stale-reference fixes), Public Limited Company (contradiction fix), Homepage (testimonials/CTA strip), GST Return Filing (pricing/anchor verification). No Tier 1 page warrants replacement — all 13 are recommended for optimization in place.

### Commercial content gaps (Section 6A)

Every `NO DEDICATED PAGE FOUND` gap is detailed in full in Section 9 below. In content terms, the most consequential gaps are: **Private Limited Company Registration** (CONT-014, CRITICAL — the single most severe gap in the entire audit, given this is the dominant Indian SME entity type with zero coverage while less-common types are fully built out), **LLP Registration formation** (CONT-015), **Proprietorship Registration** (CONT-016), **Internal Audit depth** (CONT-017, present only as a one-row table mention), and **company-side ROC/Annual Compliance** (CONT-018, directly evidenced by enquiry-dropdown options with zero matching landing page).

### Informational content gaps (Section 6B)

- The 12A/80G page's FAQ heading "Due Dates to Apply in Form 10AB" has no populated answer beneath it.
- NRI Taxation is the only Tier 1 page with no FAQ at all, despite arguably generating the most repeat practical questions.
- Section 8 Company and Startup Registration never state the firm's own typical incorporation turnaround (contrast: Public Limited Company states "seven working days").
- GST Return Filing explains what a return *is* but not what a client must *hand over* — no documents checklist, unlike GST Registration.
- A TDS rate table already exists on a separate blog article (`/tds-chart-for-fy-2026-27/`) but is not linked from the TDS service page.
- The 12A/80G page links to Section 8; the reverse link was not observed.

### Cannibalization and overlap

**9 pairs investigated: 1 `LIKELY CANNIBALIZATION RISK`, 5 `POSSIBLE OVERLAP`, 3 `NO MEANINGFUL OVERLAP FOUND`, 0 `CONFIRMED CONTENT DUPLICATION`.** No claim of actual SERP-level cannibalization is made anywhere — that requires GSC query-level data, which is `DATA NOT AVAILABLE`.

- **LIKELY:** GST Registration Online vs. the 2022 "How to File GST Registration" blog article (extends TECH-005).
- **POSSIBLE (5):** GST cancellation/revocation sub-topic spread across 3 URLs; the 8-article accounting blog cluster vs. Accounting Services; Section 8 vs. the Section 8/Trust comparative blog; TDS Chart vs. TDS service page; Accounting package bundling vs. GST/TDS service pages.
- **No meaningful overlap:** The 9 industry ITR pages vs. the main ITR Mumbai page (genuinely differentiated); `/trademark-registration/` (no competing page exists); Accounting vs. Audit (cleanly separated).
- **New unverified item (CONT-023, MEDIUM/POSSIBLE):** An in-body anchor on the GST Return Filing page resolves to `https://cashahnawaz.com/gst-registration-services-india-a-guide-to-gst/`, a URL absent from the 111-row site inventory — its live status could not be confirmed this session.

### Trust, expertise, and credibility (E-E-A-T)

**`CONFIRMED TRUST GAP` items:** No individually-named, checkable CA/CS credential anywhere sitewide (CONT-013) — every trust statement is firm-level only. No testimonials on 8 of 13 Tier 1 pages (OP-005). Homepage's "TESTIMONIALS" heading renders empty (OP-004). Wrong firm name in a live FAQ (CONT-001) — the most severe single trust defect found this phase. A minor NAP address-format inconsistency on the 12A/80G page (flagged for a future Local SEO pass, not scored as its own formal finding here).

**`TRUST OPPORTUNITY` items (not defects, concrete low-effort additions):** Attaching the existing "ICAI Practising CA UDIN-verified" claim on Audit Services to one named person is identified as the single highest-leverage trust addition in the entire batch, since the positioning work is already done.

### Content-Audit Findings Index (CONT-001–CONT-023)

| ID | Severity | Confidence | Finding | Recommended Fix |
|---|---|---|---|---|
| CONT-001 | CRITICAL | CONFIRMED | Wrong firm name ("TAXZONA Consultancy") in Accounting Services FAQ | Correct the firm name; audit rest of page for other un-customized template content |
| CONT-002 | CRITICAL | CONFIRMED | ITR Mumbai FAQ cites stale "Assessment Year 2020-21" | Route to qualified professional for verification and current framing |
| CONT-003 | CRITICAL | CONFIRMED | LLP Annual Filing presents "Final Year 2021-22" table/threshold as current | Route to qualified professional; relabel to current or explicitly historical |
| CONT-004 | CRITICAL | CONFIRMED | 12A/80G page presents passed 2021–2022 transitional deadlines without historical framing | Route to qualified professional; relabel; complete missing 10AB FAQ answer |
| CONT-005 | CRITICAL | CONFIRMED | `/gst-new-update-due-dates-for-october-2021/` — no disclaimer, ~5 years stale | Add historical-reference notice |
| CONT-006 | CRITICAL | CONFIRMED | `/due-date-calendar-for-the-month-of-november-2022/` — no disclaimer | Add historical-reference notice |
| CONT-007 | CRITICAL | CONFIRMED | `/waiver-of-late-fees-for-gst-annual-return/` — window closed March 2025 | Add closed-window notice |
| CONT-008 | HIGH | CONFIRMED | `/key-recommendations-of-45th-gst-council-meeting/` lacks historical-record framing | Add "historical record" framing note or archive |
| CONT-009 | MEDIUM | CONFIRMED | `/june-2026-important-due-dates/` still featured ~2 months past relevance | Rotate featured-post selection; establish monthly rotation process |
| CONT-010 | HIGH | CONFIRMED | Tax-regime comparison table has no FY/AY label anywhere | Verify applicable year with professional; add explicit label |
| CONT-011 | HIGH | LIKELY | Consolidated: "Income Tax Act 2025" section cross-references need professional verification across 3 pages | One consolidated professional review session |
| CONT-012 | HIGH | CONFIRMED | 5 Tier 1 pages state monetary thresholds/penalties with no currency date-stamp | Verify figures; add "current as of [date]" notes |
| CONT-013 | MEDIUM | CONFIRMED | Sitewide E-E-A-T gap — no individually-named CA credential | Add named practitioner bio with ICAI membership number |
| CONT-014 | CRITICAL | CONFIRMED | No Private Limited Company Registration page despite dominant entity type | Content brief + build page; add dropdown option |
| CONT-015 | HIGH | CONFIRMED | No LLP Registration (formation) page, distinct from LLP Annual Filing | Content brief + build page; cross-link with LLP Annual Filing |
| CONT-016 | HIGH | CONFIRMED | No Proprietorship Registration page or lead-capture category | Content brief + build page; add dropdown option |
| CONT-017 | HIGH | CONFIRMED | Internal Audit present only as a one-row table mention | Build a dedicated Internal Audit section on the existing Audit Services page |
| CONT-018 | HIGH | CONFIRMED | No company-side ROC/Company/Annual Compliance page despite confirmed demand | Consolidated pillar page + entity-specific subpages |
| CONT-019 | HIGH | CONFIRMED | No dedicated Tax Consultancy page or lead category | Content brief + build page distinguishing from ITR Filing |
| CONT-020 | MEDIUM | CONFIRMED | Partnership Registration has only an informational article, no service page | Build dedicated service page; link existing article to it |
| CONT-021 | MEDIUM | CONFIRMED | No dedicated page for GST Consultancy / GST Compliance | Content brief for consolidated GST Consultancy & Compliance page |
| CONT-022 | MEDIUM | CONFIRMED | No page distinguishing Income Tax Compliance from ITR Filing | Content brief, cross-linked with ITR Mumbai |
| CONT-023 | MEDIUM | POSSIBLE | Unverified possible third GST-registration-related URL via in-body anchor | Verify target URL live status first, then act |

Full evidence, SEO Impact, and step-by-step Manual Implementation Guide for each finding above is preserved in `reports/04-content-audit.md` and `implementation/MASTER-ISSUE-TRACKER.md`.

---

## 9. Priority Service Coverage

**Basis:** `data/crawl/service-coverage-map.md` / `.csv`, built against CLAUDE.md's priority-service list. CLAUDE.md names 25 distinct service line items across 5 groups (some working files round this to "23" in prose; this table presents every named service from the coverage map without omission). No new page is recommended anywhere a genuinely adequate existing page already covers the service — the coverage map's own determinations are followed throughout.

### Classification summary

| Classification | Count |
|---|---|
| `DEDICATED AND ADEQUATE` | 9 |
| `EXISTS UNDER DIFFERENT SERVICE/URL` | 5 (one — Annual Compliance — split across two rows below for its LLP vs. non-LLP portions) |
| `NO DEDICATED PAGE FOUND` | 12 |

### INCOME TAX

| Service | Dedicated Page Status | Existing URL | Quality | Recommended Action | Priority |
|---|---|---|---|---|---|
| Income Tax Return Filing | DEDICATED AND ADEQUATE | `/income-tax-return-filing-in-mumbai/` | Deep | No new page needed; maintain | LOW |
| Tax Consultancy | NO DEDICATED PAGE FOUND | — (only generic boilerplate on ITR page) | N/A | Content brief for dedicated Tax Consultancy page; add dropdown option (CONT-019) | HIGH |
| Income Tax Services | EXISTS UNDER DIFFERENT SERVICE/URL | `/income-tax-return-filing-in-mumbai/` (de facto hub) | Adequate as hub | Consider a distinct pillar page linking to ITR Filing, Tax Consultancy, NRI, Income Tax Compliance | MEDIUM |
| NRI Taxation | DEDICATED AND ADEQUATE | `/itr-filing-for-nri-guide-for-non-resident-taxation/` | Deep — 15 H2 sections | No action needed | LOW |
| Income Tax Compliance | NO DEDICATED PAGE FOUND | — | N/A | Content brief distinguishing ongoing compliance from annual filing (CONT-022) | MEDIUM |

### GST

| Service | Dedicated Page Status | Existing URL | Quality | Recommended Action | Priority |
|---|---|---|---|---|---|
| GST Registration | DEDICATED AND ADEQUATE | `/gst-registration-online/` | Adequate-to-deep | No new page needed | LOW |
| GST Return Filing | DEDICATED AND ADEQUATE | `/gst-return-filing/` | Adequate-to-deep | No new page needed | LOW |
| GST Consultancy | NO DEDICATED PAGE FOUND | — (thin H2 mention on GST Return Filing) | N/A | Content brief for dedicated GST Consultancy/Advisory page (CONT-021) | MEDIUM |
| GST Compliance | NO DEDICATED PAGE FOUND | — | N/A | Content brief; consider merging with GST Consultancy (CONT-021) | MEDIUM |

### ACCOUNTING

| Service | Dedicated Page Status | Existing URL | Quality | Recommended Action | Priority |
|---|---|---|---|---|---|
| Accounting | DEDICATED AND ADEQUATE | `/accounting-services/` | Adequate-to-deep | No new page needed | LOW |
| Bookkeeping | EXISTS UNDER DIFFERENT SERVICE/URL | `/accounting-services/` (dedicated H2) | Adequate | Optional standalone page as expansion opportunity, not a fix | OPPORTUNITY |
| Financial Reporting | EXISTS UNDER DIFFERENT SERVICE/URL | `/accounting-services/` | Adequate | Optional expansion only | OPPORTUNITY |
| Outsourced Accounting | EXISTS UNDER DIFFERENT SERVICE/URL | `/accounting-services/` (dedicated H2, best-covered) | Adequate-to-deep | No action needed | OPPORTUNITY |

### AUDIT

| Service | Dedicated Page Status | Existing URL | Quality | Recommended Action | Priority |
|---|---|---|---|---|---|
| Tax Audit | DEDICATED AND ADEQUATE | `/audit-services/` | Deep | No new page needed | LOW |
| Statutory Audit | DEDICATED AND ADEQUATE | `/audit-services/` (shares URL/title with Tax Audit) | Deep | No content gap; note shared-URL title-tag consideration for a future on-page-seo pass | LOW |
| Internal Audit | NO DEDICATED PAGE FOUND | — (thin, one-row mention on `/audit-services/`) | Thin | Build a dedicated Internal Audit section on the existing Audit Services page (CONT-017) | HIGH |

### REGISTRATION & COMPLIANCE

| Service | Dedicated Page Status | Existing URL | Quality | Recommended Action | Priority |
|---|---|---|---|---|---|
| Company Registration (Private Limited) | NO DEDICATED PAGE FOUND | — (`/public-limited-company/` and `/startup-registration-india/` both confirmed inadequate substitutes) | N/A | Content brief for a dedicated Private Limited Company Registration page; add dropdown option (CONT-014) | **CRITICAL** |
| LLP Registration | NO DEDICATED PAGE FOUND | — (`/llp-annual-filing/` is compliance-only) | N/A | Content brief for a dedicated LLP Registration/formation page, cross-linked with LLP Annual Filing (CONT-015) | HIGH |
| Partnership Registration | NO DEDICATED PAGE FOUND | `/tax-guides/partnership-firm-registration-maharashtra/` (informational only) | N/A for a service page | Convert/supplement with a dedicated service page (CONT-020) | MEDIUM |
| Proprietorship Registration | NO DEDICATED PAGE FOUND | — | N/A | Content brief for a dedicated page; add dropdown option (CONT-016) | HIGH |
| Startup Registration | DEDICATED AND ADEQUATE | `/startup-registration-india/` | Adequate | No gap | LOW |
| NGO Registration | DEDICATED AND ADEQUATE | `/section-8-company-registration/` and `/12a-or-12aa-or-80g-registration-new-scheme/` | Deep on both | No gap | LOW |
| ROC Compliance | NO DEDICATED PAGE FOUND (company-side) | `/llp-annual-filing/` (LLP-side only) | Adequate for LLP only | Content brief for Company ROC Compliance, cross-linked with LLP Annual Filing (CONT-018) | HIGH |
| Company Compliance | NO DEDICATED PAGE FOUND | — (dropdown-only demand evidence) | N/A | Content brief for a pillar page + Pvt Ltd/OPC/Section-8 subpages (CONT-018) | HIGH |
| Annual Compliance | EXISTS UNDER DIFFERENT SERVICE/URL (LLP) / NO DEDICATED PAGE FOUND (other entities) | `/llp-annual-filing/` (LLP portion only) | Adequate for LLP only | Consolidate with the Company Compliance content brief; cross-link with LLP Annual Filing (CONT-018) | MEDIUM |

**Overlap risks flagged in the coverage map:** Income Tax Services vs. Income Tax Return Filing (title/keyword dilution); GST Consultancy vs. GST Return Filing's "Top Reasons to Hire a GST Consultant" H2; Tax Audit/Statutory Audit sharing one URL/title; ROC Compliance, Company Compliance, and Annual Compliance are recommended for **consolidated planning as one content initiative**, not three separate thin pages, to avoid creating a new cannibalization risk.

---

## 10. Top SEO Issues & Opportunities

The table below ranks the audit's most consequential findings by business impact, combining all phases. CONFIRMED and LIKELY/POSSIBLE items are explicitly labeled — never blended.

| Priority | Finding | Type | Severity | Confidence | Business Impact | Recommended Action |
|---|---|---|---|---|---|---|
| 1 | CONT-001 | Content accuracy | CRITICAL | CONFIRMED | Wrong firm name in a live Tier 1 FAQ — direct, present-tense credibility failure | Fix immediately; single-sentence edit |
| 2 | CONT-014 | Service coverage | CRITICAL | CONFIRMED | Zero coverage for the dominant Indian SME entity type | Content brief + build dedicated page |
| 3 | CONT-002 | Content freshness | CRITICAL | CONFIRMED | Stale AY reference on the flagship Income Tax page | Route to professional review |
| 4 | CONT-003 | Content freshness | CRITICAL | CONFIRMED | "Final Year 2021-22" table shown as current on LLP Annual Filing | Route to professional review |
| 5 | CONT-004 | Content freshness | CRITICAL | CONFIRMED | Passed transitional deadlines shown as current on the site's only NGO tax-exemption page | Route to professional review |
| 6 | CONT-005/006/007 | Content freshness | CRITICAL | CONFIRMED | Three indexed articles present long-expired deadlines with no disclaimer | Add historical/closed-window notices |
| 7 | OP-001 | On-page accuracy | HIGH | CONFIRMED | Public Limited Company page self-contradicts on a concrete capital figure | Reconcile after professional verification |
| 8 | OP-002 | On-page/navigation | HIGH | LIKELY | Possible nav-link mislabel silently misroutes LLP formation searchers | Verify label/target in WP Admin |
| 9 | OP-004 | Trust/E-E-A-T | HIGH | LIKELY | Homepage's own trust section renders empty | Confirm via browser check; populate |
| 10 | CONT-011 | Content accuracy | HIGH | LIKELY | High-density old/new Act citations across 3 priority pages unverified | One consolidated professional review |
| 11 | CONT-012 | Content freshness | HIGH | CONFIRMED | 5 pages state monetary figures with no currency date-stamp | Verify and date-stamp |
| 12 | CONT-015/016/018/019 | Service coverage | HIGH | CONFIRMED | LLP Registration, Proprietorship, company-side Annual Compliance, and Tax Consultancy all have confirmed demand and zero content | Content-production batch |
| 13 | CONT-017 | Service coverage | HIGH | CONFIRMED | Internal Audit reduced to a one-row table mention | Build a dedicated section |
| 14 | CONT-008/010 | Content freshness | HIGH | CONFIRMED | Missing historical framing / missing FY label on 2 articles | Add framing/labels |
| 15 | TECH-001/002 | Technical | MEDIUM | LIKELY | Slug collision + 3 outdated footer links | Confirm in Admin; update hrefs |
| 16 | TECH-003/004 | Technical | MEDIUM | CONFIRMED | 2 thin archives; stale GST amnesty content | Sitemap toggle; add notices |
| 17 | OP-003/005/006/007 | On-page/trust | MEDIUM | CONFIRMED | Pricing inconsistency; testimonial duplication/absence; CTA-strip gap; H1 scope mismatch | Standardize per-item guidance |
| 18 | CONT-013 | Trust/E-E-A-T | MEDIUM | CONFIRMED | No individually-named, checkable CA credential sitewide | Add named practitioner bio |
| 19 | CONT-020/021/022 | Service coverage | MEDIUM | CONFIRMED | Partnership Registration, GST Consultancy/Compliance, Income Tax Compliance gaps | Content briefs, lower urgency |
| 20 | TECH-005/006/007, WP-001, OP-008, CONT-009/023 | Technical/On-page | LOW/MEDIUM | Mixed | Minor hygiene and possible-confidence items | Address opportunistically |

### Complete Finding Index (all 39 tracked findings)

| ID | Severity | Confidence | Issue | Recommended Action |
|---|---|---|---|---|
| TECH-001 | MEDIUM | LIKELY | `/trademark-registration/` page/taxonomy slug collision | Confirm in WP Admin; rename taxonomy slug |
| TECH-002 | MEDIUM | LIKELY | 3 footer links use outdated/mistyped slugs, `http://` scheme | Update footer hrefs; confirm old slugs' status |
| TECH-003 | MEDIUM | CONFIRMED | 2 thin single-item category archives indexed | Exclude from sitemap or build out content |
| TECH-004 | MEDIUM | CONFIRMED | Stale, deadline-specific compliance content live with no update | Add "scheme closed" notice |
| TECH-005 | LOW | POSSIBLE | Possible cannibalization: GST blog article vs. Tier 1 page | Route to content-strategy decision |
| TECH-006 | LOW | CONFIRMED | Mixed http/https scheme in internal links | Bulk search-and-replace to https |
| TECH-007 | LOW | POSSIBLE | `/tax-case-law/` index may be under-populated | Manual re-check; add missing articles |
| WP-001 | LOW | CONFIRMED | 2 of 9 ITR industry pages use an older Elementor template | Rebuild using the 7-page family's template |
| OP-001 | HIGH | CONFIRMED | Public Ltd Co self-contradicts on paid-up capital | Reconcile after professional verification |
| OP-002 | HIGH | LIKELY | Possible mislabeled "LLP Registration" nav link | Verify label/target in WP Admin |
| OP-003 | MEDIUM | CONFIRMED | Inconsistent pricing disclosure across Tier 1 | Standardize sitewide policy |
| OP-004 | HIGH | LIKELY | Homepage testimonials section renders empty | Confirm and populate |
| OP-005 | MEDIUM | CONFIRMED | Testimonials duplicated on 4 pages; absent on 2 | Add/vary testimonials |
| OP-006 | MEDIUM | CONFIRMED | Homepage CTA strip omits 3 of 5 priority groups | Expand CTA strip |
| OP-007 | MEDIUM | CONFIRMED | 12A/80G H1 narrower than page scope | Update H1 |
| OP-008 | LOW | CONFIRMED | Misplaced GST return-filing sentence on Registration page | Correct or remove sentence |
| CONT-001 | CRITICAL | CONFIRMED | Wrong firm name in Accounting FAQ | Correct firm name |
| CONT-002 | CRITICAL | CONFIRMED | Stale AY2020-21 in ITR Mumbai FAQ | Professional review |
| CONT-003 | CRITICAL | CONFIRMED | "Final Year 2021-22" table on LLP Annual Filing | Professional review |
| CONT-004 | CRITICAL | CONFIRMED | Passed 2021-22 deadlines on 12A/80G page | Professional review |
| CONT-005 | CRITICAL | CONFIRMED | Oct 2021 due dates, no disclaimer | Add historical notice |
| CONT-006 | CRITICAL | CONFIRMED | Nov 2022 due dates, no disclaimer | Add historical notice |
| CONT-007 | CRITICAL | CONFIRMED | Waiver window closed March 2025, no notice | Add closed-window notice |
| CONT-008 | HIGH | CONFIRMED | 2021 GST Council meeting recap lacks framing | Add historical-record note |
| CONT-009 | MEDIUM | CONFIRMED | June 2026 due-dates article still featured | Rotate featured post |
| CONT-010 | HIGH | CONFIRMED | Tax-regime table has no FY/AY label | Add year label after verification |
| CONT-011 | HIGH | LIKELY | Act-2025 section mappings unverified across 3 pages | Consolidated professional review |
| CONT-012 | HIGH | CONFIRMED | 5 pages' monetary figures lack date-stamp | Verify and date-stamp |
| CONT-013 | MEDIUM | CONFIRMED | No named, checkable CA credential sitewide | Add named practitioner bio |
| CONT-014 | CRITICAL | CONFIRMED | No Private Limited Company Registration page | Build dedicated page |
| CONT-015 | HIGH | CONFIRMED | No LLP Registration (formation) page | Build dedicated page |
| CONT-016 | HIGH | CONFIRMED | No Proprietorship Registration page | Build dedicated page |
| CONT-017 | HIGH | CONFIRMED | Internal Audit is a one-row table mention only | Build dedicated section |
| CONT-018 | HIGH | CONFIRMED | No company-side ROC/Annual Compliance page | Build pillar + subpages |
| CONT-019 | HIGH | CONFIRMED | No Tax Consultancy page | Build dedicated page |
| CONT-020 | MEDIUM | CONFIRMED | Partnership Registration lacks a service page | Build service page |
| CONT-021 | MEDIUM | CONFIRMED | No GST Consultancy/Compliance page | Build consolidated page |
| CONT-022 | MEDIUM | CONFIRMED | No Income Tax Compliance page | Build dedicated page |
| CONT-023 | MEDIUM | POSSIBLE | Unverified third GST-related URL via anchor | Verify live status first |

---

## 11. Quick Wins — Manual Implementation

These are the genuinely low-effort, high-value items identified across both phases. Every step below is written for **the user** to perform — Claude does not implement any of these.

### Quick Win 1 — Correct the wrong firm name on Accounting Services (CONT-001)
- **Why it matters:** A live, Tier 1 commercial page tells a prospective client the wrong firm's name at the exact FAQ moment designed to build confidence before they enquire.
- **Where to implement:** `/accounting-services/`, FAQ answer to "What are the Accounting services in Mumbai you provide?"
- **Step-by-step:** (1) In WordPress Admin, open the Accounting Services page in Elementor. (2) Locate the FAQ widget/accordion for that question. (3) Replace "TAXZONA Consultancy" with "Shahnawaz and Associates" (or the firm's preferred exact name). (4) Read the rest of that FAQ answer and the page's other FAQs for any other un-customized third-party references. (5) Save and republish.
- **Validation:** Re-fetch the live page and confirm the FAQ names the correct firm; search the rendered page for any remaining instance of "TAXZONA."

### Quick Win 2 — Reconcile the Public Limited Company capital contradiction (OP-001)
- **Why it matters:** The page states two different minimum paid-up capital figures in its own body copy — a material trust/decision-quality issue for figures a prospect would use to plan a real financial commitment.
- **Where to implement:** `/public-limited-company/`, "Requirements" section and FAQ Q1.
- **Step-by-step:** (1) Confirm the currently correct rule with a qualified CA/company-law professional. (2) In Elementor, edit both the "Requirements" section and the FAQ answer to state the same, verified figure (or explicitly frame one as historical if the rule changed at a known date). (3) Save and republish.
- **Validation:** Re-fetch the live page and confirm both sections agree.

### Quick Win 3 — Add historical/closed-window notices to 3 stale due-date articles (CONT-005/006/007)
- **Why it matters:** These articles present long-expired or self-confirmed-closed deadlines with no disclaimer, on live, indexed pages.
- **Where to implement:** `/gst-new-update-due-dates-for-october-2021/`, `/due-date-calendar-for-the-month-of-november-2022/`, `/waiver-of-late-fees-for-gst-annual-return/`.
- **Step-by-step:** (1) Open each article in the WordPress editor. (2) Add a short, prominent notice block at the top (e.g., "This article describes [month/year] deadlines and is retained for historical reference" or, for the waiver article, "This waiver window closed 31 March 2025"). (3) Save and republish each.
- **Validation:** Re-fetch each URL and confirm the notice is visible in the rendered content.

### Quick Win 4 — Populate or remove the homepage's empty "TESTIMONIALS" section (OP-004)
- **Why it matters:** The homepage is the site's highest-traffic entry point and primary trust surface; a labeled but empty proof section undercuts exactly the message it's meant to send.
- **Where to implement:** Homepage `/`, "TESTIMONIALS" H2 / "What People Are Saying About Us."
- **Step-by-step:** (1) Open the live homepage in a standard browser and scroll to the testimonials section to confirm whether it's genuinely empty (this could not be confirmed via this session's tools). (2) If empty, open the homepage in Elementor, locate the Testimonials widget, and either link it to the same data source as the service-page testimonial widget or manually add 2–3 of the real testimonials already displayed elsewhere on the site.
- **Validation:** Re-view the homepage and confirm testimonial content now displays.

### Quick Win 5 — Fix the sitewide mixed http/https internal-link scheme (TECH-006)
- **Why it matters:** Every `http://` internal link forces an unnecessary redirect hop and dilutes link equity slightly, at scale, across a sitewide, high-frequency link position (footer).
- **Where to implement:** Footer menu/widget and Elementor templates sitewide.
- **Step-by-step:** (1) Install/use a database-safe search-and-replace plugin (e.g., "Better Search Replace," which safely handles serialized Elementor JSON). (2) Run a search-and-replace of `http://cashahnawaz.com` → `https://cashahnawaz.com` across post/page content and Elementor template data. (3) Separately check Appearance → Menus for any manually-entered `http://` URLs.
- **Validation:** Re-fetch the footer and main navigation and confirm all internal hrefs read `https://`.

### Quick Win 6 — Update the 3 outdated footer links (TECH-002)
- **Where to implement:** Site footer (Appearance → Menus, or the Elementor footer template).
- **Step-by-step:** (1) Locate the three footer links pointing to `http://cashahnawaz.com/project-business/trademark-registration/`, `http://cashahnawaz.com/income-tax-return-filling-in-mumbai/`, and `http://cashahnawaz.com/online-tds-return-filing/`. (2) Update each href to its current correct URL (`https://cashahnawaz.com/trademark-registration/`, `https://cashahnawaz.com/income-tax-return-filing-in-mumbai/`, `https://cashahnawaz.com/tds-return-filing-services/`). (3) Separately confirm in WordPress Admin whether the old slugs still resolve to live content.
- **Validation:** Re-fetch the footer and confirm updated hrefs; re-fetch the old URLs and confirm a clean redirect or 404.

### Quick Win 7 — Exclude or noindex the 2 thin category archives (TECH-003)
- **Where to implement:** Rank Math → Sitemap Settings / Titles & Meta → Taxonomies.
- **Step-by-step:** (1) In Rank Math's Taxonomies settings, locate the `mca` and `donation` terms. (2) Toggle off sitemap inclusion, or set a noindex directive while keeping the archive reachable to visitors.
- **Validation:** Re-fetch `category-sitemap.xml` and confirm the toggled term(s) no longer appear.

### Quick Win 8 — Add dropdown-only lead categories ahead of new pages
- **Why it matters:** Adding "Private Limited Company Registration" and "Proprietorship Registration" as enquiry-dropdown options — even before their landing pages exist — starts capturing trackable lead demand immediately, at near-zero cost.
- **Where to implement:** The enquiry form's "Select Service" dropdown (coordinate with whichever plugin renders it — see Section 6's form-plugin ambiguity note).
- **Step-by-step:** (1) Identify the form-builder plugin actually controlling the live dropdown (verify via WordPress Admin, since this remains ambiguous per this audit's tools). (2) Add "Private Limited Company Registration" and "Proprietorship Registration" as new dropdown options, matching the existing option format. (3) Save.
- **Validation:** Re-fetch the live form and confirm the new options appear in the dropdown.

---

## 12. Manual Implementation Roadmap

Every item below is performed manually by the user. Expected Benefit is stated as High/Medium/Low only — this report makes no ranking or traffic guarantee.

### PHASE 1 — Immediate Priority

| Action | Priority | Expected Benefit | Manual Implementation Area |
|---|---|---|---|
| Fix wrong firm name (CONT-001) | CRITICAL | High | WordPress/Elementor FAQ edit |
| Route ITR Mumbai, LLP Annual Filing, 12A/80G stale content to professional review (CONT-002/003/004) | CRITICAL | High | Professional review + WordPress/Elementor content edit |
| Add historical/closed-window notices to 3 stale articles (CONT-005/006/007) | CRITICAL | Medium | WordPress editor |
| Reconcile Public Ltd Co capital contradiction (OP-001) | HIGH | High | Professional review + Elementor edit |
| Begin Private Limited Company Registration content brief (CONT-014) | CRITICAL | High | Content commissioning (longest lead time in this tier) |

### PHASE 2 — High Value Improvements

| Action | Priority | Expected Benefit | Manual Implementation Area |
|---|---|---|---|
| Verify/relabel possible LLP nav-link mislabel (OP-002) | HIGH | Medium | WordPress Admin → Menus |
| Confirm and populate homepage testimonials (OP-004) | HIGH | Medium | Browser check + Elementor edit |
| Consolidated professional review of Act-2025 section mappings across 3 pages (CONT-011) | HIGH | Medium | Professional review |
| Date-stamp monetary figures on 5 Tier 1 pages (CONT-012) | HIGH | Medium | Professional review + content edit |
| Build LLP Registration, Proprietorship Registration, Tax Consultancy pages (CONT-015/016/019) | HIGH | High | Content commissioning + WordPress/Elementor build |
| Build company-side ROC/Annual Compliance pillar + subpages (CONT-018) | HIGH | High | Content commissioning + WordPress/Elementor build |
| Expand Internal Audit into a dedicated section (CONT-017) | HIGH | Medium | Content commissioning + Elementor edit |
| Add historical-record framing / FY label (CONT-008/010) | HIGH | Low | WordPress editor |

### PHASE 3 — Content & Service Expansion

| Action | Priority | Expected Benefit | Manual Implementation Area |
|---|---|---|---|
| Standardize pricing-disclosure policy across Tier 1 (OP-003) | MEDIUM | Medium | Business decision + content edit |
| Vary/add testimonials sitewide (OP-005) | MEDIUM | Medium | Client outreach + Elementor edit |
| Expand homepage CTA strip to all 5 priority groups (OP-006) | MEDIUM | Medium | Elementor edit |
| Widen 12A/80G H1 to full scope (OP-007) | MEDIUM | Low | Elementor edit |
| Add named practitioner bio and ICAI credential (CONT-013) | MEDIUM | Medium | Content + About Us page edit |
| Build Partnership Registration, GST Consultancy/Compliance, Income Tax Compliance pages (CONT-020/021/022) | MEDIUM | Medium | Content commissioning + WordPress/Elementor build |
| Verify CONT-023's unverified URL and correct anchor if needed | MEDIUM | Low | Browser check + content edit |
| Resolve TECH-001 slug collision and TECH-002 footer links | MEDIUM | Low | WordPress Admin + footer edit |

### PHASE 4 — Further SEO Development

| Action | Priority | Expected Benefit | Manual Implementation Area |
|---|---|---|---|
| Fix TECH-005/006/007, WP-001, OP-008 (LOW items) | LOW | Low | Various — opportunistic during other edits |
| Commission Internal Linking Audit | — | Medium | Future audit phase |
| Commission Schema Audit (once raw-HTML access resolves JSON-LD visibility) | — | Medium | Future audit phase |
| Commission Performance / Core Web Vitals testing | — | Medium | Future audit phase |
| Commission Local SEO Audit (NAP consistency, map embed, WhatsApp) | — | Medium | Future audit phase |
| Commission Competitor Analysis | — | Medium | Future audit phase |
| Establish GSC/GA4/GTM connectivity for future analysis | — | High (unlocks data-driven prioritization) | Analytics/tooling setup |

---

## 13. 30/60/90 Day Roadmap

### First 30 Days

- Fix CONT-001 (wrong firm name) — same day, single-sentence edit.
- Route CONT-002, CONT-003, CONT-004 (Tier 1 stale content) to a qualified CA/tax professional as one batch review.
- Add historical/closed-window notices to CONT-005, CONT-006, CONT-007 — mechanical, no professional review needed for the notice text itself.
- Fix OP-001 (Public Ltd Co contradiction) after professional verification.
- Confirm and address OP-004 (homepage testimonials).
- Complete Quick Wins 5–7 (http/https cleanup, footer link update, thin-archive sitemap toggle — TECH-002/003/006).
- Confirm the TECH-001 slug collision in WordPress Admin.
- Begin the Private Limited Company Registration content brief (CONT-014) — longest lead-time item, start now so it lands in the 31–60 day window.
- Add "Private Limited Company Registration" and "Proprietorship Registration" as enquiry-dropdown options (Quick Win 8).

### Days 31–60

- Complete the consolidated professional review of CONT-011 (Act-2025 section mappings) and CONT-012 (date-stamping monetary figures).
- Resolve OP-002 (nav-link verification) via WordPress Admin.
- Build out CONT-017 (Internal Audit section expansion) — fastest of the coverage-gap items since it extends an existing page.
- Begin content production for CONT-015 (LLP Registration), CONT-016 (Proprietorship Registration), CONT-019 (Tax Consultancy), and CONT-018 (company-side Annual Compliance pillar + subpages) as one coordinated content batch alongside CONT-014.
- Standardize pricing disclosure (OP-003) and expand the homepage CTA strip (OP-006).
- Add named practitioner credential to About Us and Audit Services (CONT-013).
- Verify CONT-023's unverified URL.
- **Begin the Internal Linking Audit** (next phase — see Section 15) to formalize the many specific cross-link gaps already surfaced in this report (Section 8 ↔ 12A/80G reciprocity, Accounting ↔ Audit distinction links, TDS chart ↔ TDS service page).

### Days 61–90

- Publish the new Registration & Compliance pages built in Days 31–60; cross-link them bidirectionally with existing pages per each finding's guidance.
- Build out lower-priority coverage gaps: CONT-020 (Partnership Registration), CONT-021 (GST Consultancy & Compliance), CONT-022 (Income Tax Compliance).
- Add/vary testimonials sitewide (OP-005) and finalize any remaining LOW-severity items (TECH-005/006/007, WP-001, OP-008).
- **Schema Audit** — *scheduled, dependent on resolving the JSON-LD visibility gap with raw-HTML or browser access; not yet performed.*
- **Local SEO Audit** — *scheduled; will address the NAP address-format inconsistency noted on the 12A/80G page and the confirmed-absent WhatsApp entry point.*
- **Competitor Analysis** — *scheduled; not yet performed.*
- **Performance / Core Web Vitals testing** — *scheduled once a Lighthouse/PageSpeed-capable tool is available; not yet performed.*

All items marked *scheduled* above are explicitly future-audit-dependent — they are not confirmed fixes ready today, and no result from them is presented in this report.

---

## 14. Data Limitations

The following are `DATA NOT AVAILABLE` across every phase of this audit to date:

- Google Search Console (Coverage, Sitemaps, URL Inspection, Core Web Vitals report)
- Google Analytics 4
- Google Tag Manager (container `GTM-N2LHGRCX` per CLAUDE.md could neither be confirmed nor denied on the live site)
- Core Web Vitals / Lighthouse / PageSpeed Insights
- Raw HTTP response headers (status codes, `X-Robots-Tag`, `Cache-Control`, `Location`/redirect targets)
- Browser automation or rendered screenshots (no visual, above-the-fold, or sticky-CTA claim can be made anywhere in this report)
- WordPress Admin access (no plugin list, theme confirmation, or settings screen was verified directly)
- Hosting access (PHP version, server configuration, `.htaccess`)
- Meta robots tag content — `NOT VISIBLE` on effectively every fetch this session (tool limitation, not confirmed absence)
- Canonical tag targets — `NOT VISIBLE` sitewide (tool limitation)
- JSON-LD / structured data presence — `NOT VISIBLE` sitewide despite Rank Math being confirmed active (tool limitation)
- JS-rendered / client-side-injected content
- Keyword search volume, ranking position, organic traffic, conversion rate, and backlink data — none of this exists anywhere in this project and none is claimed anywhere in this report

**DATA NOT AVAILABLE does not mean the website has a problem. It means the issue could not be verified within the available audit environment.**

---

## 15. Next Audit Phases

The following remain outside the scope of this interim report:

- **Internal Linking Audit** — NOT YET INCLUDED IN THIS INTERIM REPORT.
- **Schema Audit** — NOT YET INCLUDED IN THIS INTERIM REPORT.
- **Performance Audit** — NOT YET INCLUDED IN THIS INTERIM REPORT.
- **Competitor Analysis** — NOT YET INCLUDED IN THIS INTERIM REPORT.
- **Local SEO Analysis** — NOT YET INCLUDED IN THIS INTERIM REPORT.
- **Conversion and Lead Generation (CRO) Audit** — NOT YET INCLUDED IN THIS INTERIM REPORT (only content-alignment was checked in Phase 1B; design/UX-level CRO was explicitly out of scope).
- **GSC Analysis** — NOT YET INCLUDED IN THIS INTERIM REPORT.
- **GA4 Analysis** — NOT YET INCLUDED IN THIS INTERIM REPORT.
- **GTM and Conversion Tracking Audit** — NOT YET INCLUDED IN THIS INTERIM REPORT.

---

## 16. Final Conclusion

Cashahnawaz.com stands on a genuinely clean technical and WordPress foundation. Phase 1A found zero CRITICAL and zero HIGH severity issues across crawlability, indexation, sitemap structure, and plugin/theme configuration — Rank Math is confirmed as the sole active SEO plugin, the sitemap is well-formed and correctly segmented, and `robots.txt` blocks nothing it shouldn't. This is not a site fighting a structural technical deficit.

The real, addressable priorities uncovered by this audit sit in **content accuracy and service coverage**, both of which Phase 1B examined in depth. Fifteen items across the site need a qualified professional's eyes on dates, deadlines, and figures — several of them one-sentence or one-paragraph fixes once verified. One live FAQ names the wrong firm. One page contradicts itself on a concrete number. And a dozen of the firm's named priority services — most consequentially Private Limited Company Registration, the entity type most Indian small businesses actually choose — have no dedicated page to meet a searcher looking for exactly that service, even while enquiry-form dropdown data confirms the firm already handles several of these engagements without any organic entry point to capture them.

None of this reflects a site in crisis. It reflects a well-built, content-rich CA firm website where a handful of pages have drifted out of date and a handful of common services were never given their own landing page — both are ordinary, fixable content-maintenance gaps, not structural failures. The strongest pages on the site (GST Registration, NRI Taxation, Section 8/12A-80G) demonstrate the firm already knows how to build genuinely deep, well-organized service content; the work ahead is applying that same standard consistently and keeping it current.

Completing the remaining audit phases — Internal Linking, Schema, Performance, Competitor, Local SEO, CRO, and the GSC/GA4/GTM analyses once connectivity is established — will sharpen prioritization further, particularly by replacing this report's inspection-based `LIKELY USER SEARCH INTENT` judgments with actual query-level demand data. Until then, the recommendation is straightforward: implement the findings in this report manually, in the priority order given, verify every regulated figure with a qualified professional before publishing it, and use each finding's Validation step to confirm the change actually took effect on the live site before considering it closed.
