# Phase 1A — Technical SEO Audit — cashahnawaz.com

**Session date:** 2026-08-27
**Site:** https://cashahnawaz.com/
**Phase type:** Evidence-based technical SEO audit. No live-site changes were made. No implementation was performed — findings and recommendations only, per CLAUDE.md rule 6/7.

---

## 1. URL Verification Strategy and Results Summary

Full per-URL evidence is in `data/crawl/phase-1a-url-verification.csv` (111 rows, one per URL in the site inventory, in inventory order). Summary:

| Metric | Count |
|---|---|
| Total discovered URLs (full inventory) | 111 |
| URLs individually fetched this session (Phase 0 + Phase 1A combined) | **53** |
| — of which VERIFIED (title/H1 captured, content unambiguous) | 27 |
| — of which PARTIALLY VERIFIED (thin/ambiguous evidence, or a field missing) | 26 |
| URLs NOT individually fetched this session (sitemap metadata only) | 58 |

**Method:** WebFetch (AI-summarized HTML→markdown extraction) against live URLs. No raw HTTP header inspection, no browser automation, no JS-rendering guarantee (see Section 8, Data Limitations). Phase 0 fetched the homepage + 11 interior pages (12 URLs — see note below on a count discrepancy in the Phase 0 narrative files). Phase 1A added three fresh batches this session: Batch A (16 URLs — remaining Tier 1 + all Tier 2), Batch B (10 URLs — 7 category archives + 3 footer-linked non-sitemap URLs), Batch C (15 of 66 Tier 3 blog/article URLs, an explicit sample, not exhaustive).

**Note on the Phase 0 count:** `site-inventory-notes.md`, `00-pre-audit-baseline.md`, and `00-capability-check.md` all state "11" URLs were individually fetched in Phase 0, but each of those same files' own named lists (Homepage + GST Registration Online + GST Return Filing + Income Tax Return Filing Mumbai + Accounting Services + Audit Services + Startup Registration India + Section 8 Company Registration + Public Limited Company + LLP Annual Filing + About Us + Contact Us) contains **12** distinct URLs, matching the 12 rows in `site-inventory.csv` explicitly marked "individually fetched." This synthesis uses **12** as the accurate Phase 0 count (the CSV's raw per-row data, not the narrative summary sentence) — flagged here transparently since it changes the Phase 0+1A combined total from an approximate "51" to the exact **53**.

**Coverage verdict: PARTIAL.** 53 of 111 URLs (48%) were individually fetched this session; the remaining 52% rely on XML sitemap metadata only (URL, lastmod) and have not had their live content, status, or on-page elements independently confirmed. All 13 Tier 1 and all 15 Tier 2 URLs were individually fetched (100% of both tiers); Tier 3 (66 blog/article URLs) was sampled at 15/66 (23%), explicitly stated as a sample per website-crawl.md's disclosure requirement, not a silent substitution.

---

## 2. Crawlability & Indexability Audit

Organized into the four evidence-confidence buckets, per instruction.

### CONFIRMED ISSUE
- **Two thin category/taxonomy archives indexed via the sitemap** (`/mca/`, `/donation/`) — each resolved to exactly one post with no pagination. See TECH-003 below.
- **Content-freshness signal on compliance-deadline content** (`/gst-amnesty-scheme-2023/` and related) — live, sitemap-indexed content describing a compliance window that closed years ago, with no visible revision. See TECH-004 below.
- **Mixed `http://`/`https://` scheme in internal link hrefs** — confirmed present in footer links and noted sitewide in Phase 0. See TECH-006 below.

### LIKELY ISSUE
- **`/trademark-registration/` page/taxonomy slug collision** across `page-sitemap.xml` and `category-sitemap.xml`. See TECH-001 below. Full reasoning: `data/crawl/phase-1a-sitemap-audit.md` Section 4.
- **3 footer-linked URLs pointing to non-sitemap, outdated/mistyped slugs**, live-loading content matching an existing correctly-slugged sitemap page. See TECH-002 below.

### POSSIBLE RISK
- **Keyword cannibalization risk**: `/how-to-file-gst-registration-process-benefits-penalty/` (blog, lastmod 2022-10-31 — oldest in the inventory) topically overlaps with the Tier 1 service page `/gst-registration-online/` (lastmod 2026-06-18). See TECH-005 below.
- **`/tax-case-law/` index possibly under-populated**: only 1 of ~19 sitemap-listed case-law articles was surfaced on the index page fetch; cannot confirm whether this is a genuine content/internal-linking gap or an extraction limitation. See TECH-007 below.
- **`/accounting-services-blog/` archive's newest visible post (Feb 2023) is older than a related sitemap entry's lastmod (2026-07-22)** — not resolved this session; noted for content-audit.md, not scored as a standalone finding here (insufficient evidence to state a specific technical cause).

### NOT VERIFIABLE WITH CURRENT ACCESS
- **Meta robots tags (`<meta name="robots">`) — sitewide.** NOT VISIBLE on every single one of 53 fetches this session (Phase 0 + Batch A/B/C), including on priority Tier 1 pages. **This is overwhelmingly a tool limitation, not evidence of a missing tag** — WebFetch's HTML→markdown conversion does not reliably surface `<head>`-level elements (confirmed independently in `00-capability-check.md`, `wordpress-fingerprint.md`, and every batch file's own stated caveat). No finding is made that meta robots tags are absent; this is a data limitation only.
- **`X-Robots-Tag` HTTP header — sitewide.** No raw header tool was available this session. `DATA NOT AVAILABLE`.
- **Canonical tags (`<link rel="canonical">`) — sitewide.** NOT VISIBLE on every fetch this session, with one partial exception: the `/trademark-registration/` page's fetch specifically noted canonical was NOT VISIBLE despite several sibling pages in the same batch returning other head-adjacent signals — this pattern is itself worth a second, independent/raw-HTML fetch attempt but does not amount to evidence the tag is missing. `DATA NOT AVAILABLE` sitewide.
- **Internal links pointing to noindexed pages.** Cannot be assessed — noindex status itself is unverifiable (see above), so whether any internal link targets a noindexed page cannot be determined.
- **Non-indexable sitemap URLs (URLs in the sitemap that are actually noindexed or non-200).** Cannot be confirmed — status codes and meta robots are both unverifiable this session (see Section 3 and Section 8).
- **WordPress default archive risks not directly observed this session: search results (`?s=`), attachment pages (`/?attachment_id=`), author archives (`/author/...`), date archives, and pagination URLs (`/page/2/`).** None of these were found in the sitemap XML or in any navigation/footer link extraction this session. **Absence from what was surfaced is not proof of absence** — WebFetch's markdown conversion may not expose every URL pattern, and no dedicated crawl of these WordPress-default paths (e.g., manually requesting `/?attachment_id=1`) was performed. Marked `NOT VERIFIABLE`, not "confirmed absent."
- **Parameter-based URL risks** (`?replytocom=`, UTM-tagged internal links, session IDs). Not observed in any fetch this session, but not specifically tested for either. `NOT VERIFIABLE`.
- **robots.txt Disallow scope beyond what was read.** `robots.txt` content itself was fetched fresh and is fully visible (see Section 8 for the raw text) — no accidental blocking of content paths found in what it names. This one item IS confirmed (see Section 8), included here only to distinguish it from the unverifiable items above.

---

## 3. Canonical & Duplication Audit

Per instruction, HTML canonical evidence (what was actually seen in page content) and HTTP redirect evidence (raw headers) are kept explicitly separate — they are not the same kind of evidence and must not be blurred.

### HTML CANONICAL EVIDENCE (what was actually observed in fetched page content)
- **Canonical `<link>` tag: NOT VISIBLE on all 53 fetches this session**, with zero exceptions recorded in any batch file. This includes 16/16 in Batch A (explicitly logged: "Canonical surfaced: 0 of 16"). This is a tool-extraction limitation (see Section 8), not a confirmed absence.
- **No evidence was found of two competing canonical signals** (e.g., a theme-level canonical conflicting with an SEO-plugin canonical) — but this absence-of-evidence claim is weak given canonical tags weren't visible at all; it should not be read as a clean pass.

### HTTP REDIRECT EVIDENCE (raw headers / status-code-based redirect confirmation)
- **`DATA NOT AVAILABLE` — uniformly, for every URL, every domain/protocol variant, and every footer-linked URL tested this session.** No raw HTTP header or status-code tool was available (`00-capability-check.md`). Specifically:
  - WWW vs. non-WWW and HTTP vs. HTTPS enforcement: all tested variants (`https://cashahnawaz.com/`, `https://www.cashahnawaz.com/`, `http://cashahnawaz.com/robots.txt`, `https://www.cashahnawaz.com/robots.txt`) returned matching content, but whether this reflects a real 301/302 redirect, multiple live origins, or WebFetch silently normalizing the request **cannot be determined**. `RAW HEADER / REDIRECT VERIFICATION NOT AVAILABLE`.
  - The `sitemap.xml` / `wp-sitemap.xml` / `sitemap_index.xml` alias mechanism: same limitation. `RAW HEADER / REDIRECT VERIFICATION NOT AVAILABLE`.
  - The 3 footer-linked non-sitemap URLs (Section 4 below): same limitation — cannot distinguish "genuinely separate live page" from "silently 301/302-redirects to the correct page" for any of the three. `RAW HEADER / REDIRECT VERIFICATION NOT AVAILABLE`.

**Implication:** No technical SEO finding in this report claims a confirmed redirect status, redirect chain length, or HTTP status code anywhere. Every such claim is explicitly marked `DATA NOT AVAILABLE` rather than inferred from qualitative "page loaded" observations.

---

## 4. Internal Technical Link Checks — the 3 Footer URLs

Stated plainly, using only the evidence from `data/crawl/_batch-b-archives-footer.md` (no further inference):

| Footer URL | Live-check result |
|---|---|
| `http://cashahnawaz.com/project-business/trademark-registration/` | **Live** — content loaded (H1 "Trademark Registration Process"), does not resemble a 404. Redirect-vs-duplicate status: **unknown** (not confirmable with WebFetch). |
| `http://cashahnawaz.com/income-tax-return-filling-in-mumbai/` (typo: "filling") | **Live** — content loaded (title/H1 "Income Tax Return Filing In Mumbai \| ITR Filing Services", matching the correctly-spelled sitemap page). Redirect-vs-duplicate status: **unknown**. |
| `http://cashahnawaz.com/online-tds-return-filing/` | **Live** — content loaded (title "TDS Return Filing Services In Mumbai \| Expert CA Support", matching the sitemap's `/tds-return-filing-services/` page). Redirect-vs-duplicate status: **unknown**. |

None of the three returned anything resembling a broken/404 page. None can be confirmed as either a genuinely separate live duplicate URL or a silent same-host redirect. This ambiguity is the evidence basis for TECH-002.

---

## 5. Technical SEO Findings

Each finding uses the full CLAUDE.md Required Finding Template plus **Confidence Level** and **Evidence Source**.

### [MEDIUM] `/trademark-registration/` page/taxonomy slug collision in the sitemap

- **Issue:** The identical URL `https://cashahnawaz.com/trademark-registration/` is listed in both `page-sitemap.xml` (lastmod 2026-07-22) and `category-sitemap.xml` (lastmod 2026-05-06), with conflicting freshness signals for what should be one resolvable resource.
- **Severity:** MEDIUM
- **Evidence:** `data/crawl/sitemap-discovery.md` anomaly note (both sitemap entries quoted with their exact lastmods); live fetch in `data/crawl/_batch-a-tier1-tier2.md` shows single-article-style content (H1 "Trademark Registration Process," visible `18/02/2022` publish date, "0 Comments") rather than a multi-item taxonomy listing.
- **Affected URLs:** `https://cashahnawaz.com/trademark-registration/`
- **SEO Impact:** Crawlability/Indexability stage of the success journey. Conflicting sitemap signals for one URL can confuse how Google associates freshness/content-type with the page, and blocks any future plan to build a genuine multi-item Trademark taxonomy archive at that slug.
- **Likely Root Cause:** LIKELY a WordPress slug collision between a Page/Post and a taxonomy term both using slug `trademark-registration`, with Rank Math's sitemap generator emitting both source-table entries without deduplicating (see `data/crawl/phase-1a-sitemap-audit.md` Section 4 for full reasoning and the ruled-out alternative explanations).
- **Recommended Fix:** Confirm the collision in WordPress Admin, then rename one of the two conflicting objects' slug (most likely the taxonomy term, since the Page/Post is the one serving real content) and 301-redirect the old slug if it was ever independently indexed.
- **Implementation Steps:** (1) In WordPress Admin, check Pages/Posts for a `trademark-registration` slug and Categories/Taxonomies for the same slug. (2) If both exist, rename the taxonomy term's slug (e.g., to `trademark-registration-articles`) via the standard WordPress category-edit screen. (3) In Rank Math → Titles & Meta → Taxonomies, confirm the renamed term's sitemap/indexing settings. (4) If the old slug was ever separately indexed, add a redirect via Rank Math → Redirections (module must be enabled under Rank Math → Dashboard → Modules first).
- **Validation Method:** Re-fetch `sitemap_index.xml` → `category-sitemap.xml` and confirm `/trademark-registration/` no longer appears there under the renamed term; re-fetch the page URL and confirm content is unchanged.
- **Confidence Level:** LIKELY
- **Evidence Source:** `data/crawl/sitemap-discovery.md`; `data/crawl/_batch-a-tier1-tier2.md`; full reasoning in `data/crawl/phase-1a-sitemap-audit.md` Section 4.

### [MEDIUM] Three footer-linked URLs point to outdated/mistyped slugs not present in the XML sitemap

- **Issue:** The site footer links to three URLs using an `http://` (not `https://`) scheme and slugs that don't match any current sitemap entry: `/project-business/trademark-registration/`, `/income-tax-return-filling-in-mumbai/` (misspelled "filling"), and `/online-tds-return-filing/`. All three load live content matching an existing, correctly-slugged sitemap page, but whether they are separate live duplicate pages or silently redirect to the correct page cannot be confirmed.
- **Severity:** MEDIUM
- **Evidence:** `data/crawl/site-inventory-notes.md` (footer cross-check); `data/crawl/_batch-b-archives-footer.md` Part 2 (all three live-fetch results quoted, including the tool's own inconsistent redirect-assessment language on the `/online-tds-return-filing/` fetch).
- **Affected URLs:** `http://cashahnawaz.com/project-business/trademark-registration/`, `http://cashahnawaz.com/income-tax-return-filling-in-mumbai/`, `http://cashahnawaz.com/online-tds-return-filing/`
- **SEO Impact:** Crawlability/Indexability and, if these are genuinely separate live pages, Duplicate Content stages of the success journey. Internal link equity from the footer (a sitewide, high-frequency link position) is being spent on outdated URLs instead of the current canonical pages, and if these are truly live duplicates rather than redirects, they compete with the correct pages for the same query intent.
- **Likely Root Cause:** LIKELY leftover footer widget/menu links from a prior URL structure or a content edit that renamed/corrected the canonical slug without updating the footer menu item, compounded by the footer's use of `http://` rather than `https://` in its stored hrefs (a common artifact of an unforced/incomplete HTTP→HTTPS migration in WordPress menu or Elementor-stored data).
- **Recommended Fix:** Update the footer menu/widget to link directly to the current, correctly-slugged `https://` URLs. Independently, confirm via WordPress Admin whether the old slugs still resolve to live posts/pages (in which case they should be 301-redirected to the correct URL and/or set to noindex) or are already redirecting (in which case only the footer link text/href needs updating to remove the unnecessary redirect hop).
- **Implementation Steps:** (1) In WordPress Admin → Appearance → Menus (or the Elementor footer template, given Elementor is confirmed active), locate the three footer links and update their hrefs to `https://cashahnawaz.com/trademark-registration/`, `https://cashahnawaz.com/income-tax-return-filing-in-mumbai/`, and `https://cashahnawaz.com/tds-return-filing-services/` respectively. (2) Separately check Pages/Posts for any content still living at the three old slugs; if found, either delete/merge into the current page or set up a redirect via Rank Math → Redirections. (3) Audit other footer/menu links sitewide for the same `http://` scheme pattern noted in `site-inventory-notes.md` and correct in the same pass.
- **Validation Method:** Re-fetch the site footer HTML and confirm all links now use `https://` and the current slugs; re-fetch the three old URLs and confirm they either 301 to the correct page or return a clean 404/410 (not a live duplicate).
- **Confidence Level:** LIKELY
- **Evidence Source:** `data/crawl/site-inventory-notes.md`; `data/crawl/_batch-b-archives-footer.md`.

### [MEDIUM] Two thin, single-item category archives indexed via the sitemap

- **Issue:** `/mca/` and `/donation/` are both listed in `category-sitemap.xml` but each resolves to exactly one post ("MCA Relaxation for Filling E-Forms for FY 2020-21," dated 14/02/2022; "Reporting of Statement of Donation Form 10BD," dated 17/05/2022 respectively), with no pagination or further content, versus 8-10 items for the other 5 independently-checked archives.
- **Severity:** MEDIUM
- **Evidence:** `data/crawl/_batch-b-archives-footer.md` Part 1 — `/mca/` fetch explicitly recorded "only 1 item listed... followed by 'End of content' / 'No more pages to load'"; `/donation/` fetch explicitly recorded "only 1 item listed... Page presents as effectively a single static article... No pagination or 'more posts' content observed."
- **Affected URLs:** `https://cashahnawaz.com/mca/`, `https://cashahnawaz.com/donation/`
- **SEO Impact:** Crawlability/Indexability stage. Thin, single-item archive pages are classic low-value indexed content that can dilute overall site quality signals and rarely earn independent rankings; "MCA" maps to the Registration & Compliance priority-service group in CLAUDE.md, so leaving it as a thin single-article archive is also an under-built opportunity.
- **Likely Root Cause:** These are WordPress category/taxonomy terms with only one post ever assigned to them, left in the Rank Math-generated sitemap by default rather than deliberately excluded or built out.
- **Recommended Fix:** Either (a) exclude both taxonomies from the XML sitemap via Rank Math's per-taxonomy sitemap toggle until more content exists, (b) merge each single article into the `/others/` catch-all category and 301-redirect the thin archive URL, or (c) commission additional MCA- and donation-related content to make the archives substantive (preferred for `/mca/` given its priority-service relevance).
- **Implementation Steps:** In Rank Math → Sitemap Settings, locate the Taxonomies module and toggle off sitemap inclusion for the `mca` and `donation` terms if choosing option (a); alternatively use Rank Math → Titles & Meta → Taxonomies to set a noindex directive on these two terms specifically while keeping the archive itself reachable for site visitors.
- **Validation Method:** Re-fetch `category-sitemap.xml` and confirm the toggled term(s) no longer appear (if excluded), or re-fetch the archive URL and confirm the meta-robots/indexing state changed as intended (requires a raw-HTML or GSC URL Inspection check, since meta robots is currently unverifiable with this session's tools).
- **Confidence Level:** CONFIRMED
- **Evidence Source:** `data/crawl/_batch-b-archives-footer.md`.

### [MEDIUM] Stale, deadline-specific compliance content live and indexed with no visible currency update

- **Issue:** `/gst-amnesty-scheme-2023/` presents its title, H1, and full body content entirely anchored to a GST amnesty scheme window that its own text states closed 30 June 2023, with no visible indication of revision for current relevance — yet its sitemap `lastmod` (2026-05-06) is roughly 3 years newer than the deadline the content describes as closed. A related article, `/big-relief-for-taxpayers-whose-gst-number-got-canceled-due-to-non-filing-of-gst-returns/`, similarly describes a now-closed relief window (also expiring 30 June 2023) and explicitly states "no further extension... shall be available," though in that case the lastmod (2023-04-08) is internally consistent with the content's own vintage.
- **Severity:** MEDIUM
- **Evidence:** `data/crawl/_batch-c-tier3-sample.md` — `/gst-amnesty-scheme-2023/` entry: "STALE-CONTENT SIGNAL... Title, H1, and full body content all reference a scheme window that closed 30 June 2023, yet the sitemap lastmod (2026-05-06) is far more recent — the lastmod date does not appear to reflect a substantive content update." This finding is scoped strictly to the staleness *signal itself* (the presence of unrevised deadline-specific content and a lastmod/content mismatch) — no claim is made here about what the correct current GST rule or deadline is; that determination is out of scope for this technical audit.
- **Affected URLs:** `https://cashahnawaz.com/gst-amnesty-scheme-2023/`; `https://cashahnawaz.com/big-relief-for-taxpayers-whose-gst-number-got-canceled-due-to-non-filing-of-gst-returns/`
- **SEO Impact:** Organic Visibility and Qualified Traffic stages. For a CA/compliance firm, indexed pages describing expired deadlines without a visible "this scheme has ended" notice or update risk misleading a searcher who lands on them via a stale ranking, and can flag the page as outdated to users even where Google itself still indexes it.
- **Likely Root Cause:** Content was published to cover a time-bound scheme and never revisited after the deadline passed; the `lastmod` on `/gst-amnesty-scheme-2023/` suggests a template-level or unrelated technical touch (e.g., a sitewide theme/plugin update triggering a `lastmod` bump) rather than an actual content edit.
- **Recommended Fix:** Add a clear "this scheme window has closed" notice at the top of both articles, and route a full content-audit.md pass to determine whether either page should be updated with current-scheme information, redirected to a more current resource, or explicitly retained as historical/archival content with dated framing.
- **Implementation Steps:** In the WordPress block/Elementor editor, add a dated update notice at the top of each article's content; if Rank Math's "Last Modified" display is enabled, ensure any future edit actually changes substantive content so the lastmod signal remains meaningful (Rank Math → General Settings → the sitemap/schema "show last modified" toggle can be checked here).
- **Validation Method:** Re-fetch both URLs after the edit and confirm the notice is visible in the rendered content.
- **Confidence Level:** CONFIRMED
- **Evidence Source:** `data/crawl/_batch-c-tier3-sample.md`.

### [LOW] Mixed `http://`/`https://` scheme in internal link hrefs

- **Issue:** Multiple internal links (footer links and others noted in Phase 0) use a literal `http://` scheme in their `href` attribute even though the site serves exclusively over HTTPS.
- **Severity:** LOW
- **Evidence:** `data/crawl/site-inventory-notes.md`: "Several footer links use a literal `http://` scheme in their `href` even though the site serves over HTTPS (e.g., `http://cashahnawaz.com/contact-us/`, `http://cashahnawaz.com/accounting-services/`)"; independently confirmed in `data/crawl/_batch-b-archives-footer.md`, where all 3 footer-unmatched URLs were themselves linked with `http://`.
- **Affected URLs:** Sitewide (footer links specifically confirmed; scope beyond the footer not independently verified)
- **SEO Impact:** Crawlability stage. Each `http://` internal link forces an extra redirect hop (assuming HTTP→HTTPS redirection is in place, which is itself unconfirmed — see Section 3) before Google or a user reaches the HTTPS page, diluting link equity slightly and adding avoidable crawl overhead at scale.
- **Likely Root Cause:** LIKELY leftover absolute `http://` URLs stored in WordPress menu items or Elementor page/template JSON from before or during an HTTP→HTTPS migration, never bulk-updated afterward.
- **Recommended Fix:** Bulk-update all internal link hrefs sitewide to use `https://`.
- **Implementation Steps:** Use a database-safe search-and-replace tool (e.g., the "Better Search Replace" plugin, safe for serialized Elementor JSON data) to replace `http://cashahnawaz.com` with `https://cashahnawaz.com` across post/page content and Elementor template data; separately review Appearance → Menus for any manually-entered `http://` URLs.
- **Validation Method:** Re-fetch the footer and main navigation and confirm all internal hrefs now read `https://`.
- **Confidence Level:** CONFIRMED
- **Evidence Source:** `data/crawl/site-inventory-notes.md`; `data/crawl/_batch-b-archives-footer.md`.

### [LOW] Possible keyword cannibalization: GST registration blog article vs. Tier 1 service page

- **Issue:** `/how-to-file-gst-registration-process-benefits-penalty/` (blog article, lastmod 2022-10-31 — the oldest lastmod of any URL in the full 111-URL inventory) covers GST registration process, thresholds, benefits, and penalties — substantially the same subject matter as the Tier 1 priority service page `/gst-registration-online/` (lastmod 2026-06-18).
- **Severity:** LOW
- **Evidence:** `data/crawl/_batch-c-tier3-sample.md`: "TOPIC OVERLAP WITH TIER 1 SERVICE PAGE. This article's subject matter... directly overlaps with the Tier 1 service page https://cashahnawaz.com/gst-registration-online/... a candidate for content cannibalization / topical overlap." No ranking or search-query data was available this session to confirm actual cannibalization is occurring in the SERPs — this is a content-overlap observation, not a confirmed ranking-dilution finding.
- **Affected URLs:** `https://cashahnawaz.com/how-to-file-gst-registration-process-benefits-penalty/`, `https://cashahnawaz.com/gst-registration-online/`
- **SEO Impact:** Organic Visibility stage. If both pages target similar GST-registration search intent, they may split ranking signals and internal link equity rather than reinforcing a single authoritative page.
- **Likely Root Cause:** The blog article predates the current, more comprehensive service page (by roughly 4 years per lastmod) and appears to have not been consolidated, redirected, or differentiated in scope since the service page was built out.
- **Recommended Fix:** Route to content-audit.md/internal-linking.md for a full review: either differentiate the two pages' target intent explicitly (e.g., reposition the blog article as a more general explainer that internally links to the service page as the transactional destination) or merge/redirect the older article into the service page.
- **Implementation Steps:** Not prescribed here — this finding is a discovery-stage flag for a content-strategy decision, not a mechanical technical fix.
- **Validation Method:** Once GSC query-level data is available (currently `DATA NOT AVAILABLE`), check whether both URLs appear for overlapping GST-registration queries and whether impressions/clicks are split between them.
- **Confidence Level:** POSSIBLE
- **Evidence Source:** `data/crawl/_batch-c-tier3-sample.md`.

### [LOW] `/tax-case-law/` index page may be under-populated relative to sitemap-listed case-law articles

- **Issue:** The `/tax-case-law/` index page fetch surfaced only 1 case-law item (the Sachin Tendulkar ITAT case study), while `site-inventory.csv` lists approximately 19 distinct "Blog/Article (Case Law)" URLs.
- **Severity:** LOW
- **Evidence:** `data/crawl/_batch-a-tier1-tier2.md`: "only ONE case-study item... was surfaced by the extraction — this could mean the page currently has only one item, or that the extraction truncated additional items; not confirmable via this tool alone."
- **Affected URLs:** `https://cashahnawaz.com/tax-case-law/`
- **SEO Impact:** Crawlability stage (internal linking specifically) — if genuinely under-populated, the ~18 other case-law articles would rely entirely on the sitemap and the `/gst-case-law/` category archive for discovery rather than also being linked from this dedicated index, reducing internal link equity to those pages.
- **Likely Root Cause:** NOT DETERMINED — could be a genuine content/index-page gap (case-law articles added to the taxonomy but never manually linked from the `/tax-case-law/` index template) or simply a WebFetch extraction/pagination limitation.
- **Recommended Fix:** Manually re-check `/tax-case-law/` in a browser (or with a raw-HTML tool) to confirm whether more items exist below the fold or on a paginated view; if genuinely under-populated, add the missing case-law articles to the index.
- **Implementation Steps:** Not prescribed — pending confirmation of root cause.
- **Validation Method:** Direct browser or raw-HTML re-check of the page.
- **Confidence Level:** POSSIBLE
- **Evidence Source:** `data/crawl/_batch-a-tier1-tier2.md`.

---

## 6. Data Limitations (Section 8)

All items below are explicitly `DATA NOT AVAILABLE` this session. No finding in this report relies on any of these as confirmed fact.

| Data source | Status | Note |
|---|---|---|
| Raw HTTP response headers (status codes, `X-Robots-Tag`, `Cache-Control`, `Location`) | `DATA NOT AVAILABLE` | No header-capable tool this session. |
| Browser automation / rendered screenshots | `DATA NOT AVAILABLE` | No browser automation tool present; no visual/above-the-fold or sticky-CTA claim can be made. |
| Google Search Console (Coverage, Sitemaps, URL Inspection, Core Web Vitals) | `DATA NOT AVAILABLE` | No GSC connector present this session (confirmed via tool search, per CLAUDE.md's never-assume rule). |
| Google Analytics 4 | `DATA NOT AVAILABLE` | No GA4 connector present this session. |
| Google Tag Manager | `DATA NOT AVAILABLE` | No GTM connector present this session; GTM container `GTM-N2LHGRCX` (per CLAUDE.md) could neither be confirmed nor denied on the live site. |
| WordPress Admin | `DATA NOT AVAILABLE` | No admin/login tool present; every WordPress-related fact in this audit is fingerprint-inferred from public live-site signals, not admin-confirmed. |
| Hosting access (PHP version, server config, `.htaccess`) | `DATA NOT AVAILABLE` | No hosting connector present. |
| Lighthouse / PageSpeed / Core Web Vitals | `DATA NOT AVAILABLE` | No performance-testing tool present or found via tool search. |
| Meta robots tag content (sitewide) | `NOT VISIBLE (tool limitation)` | WebFetch does not reliably surface `<head>`-level elements; confirmed across all 53 fetches this session. |
| Canonical tag target (sitewide) | `NOT VISIBLE (tool limitation)` | Same limitation as above. |
| JSON-LD / structured data presence (sitewide) | `NOT VISIBLE (tool limitation)` | No `<script type="application/ld+json">` block was surfaced anywhere this session despite Rank Math (which by default injects schema) being confirmed active; this is a tool-extraction gap, not confirmed absence — route to a dedicated schema-audit.md pass with raw-HTML access. |
| JS-rendered / client-side-injected content | `DATA NOT AVAILABLE` | No guarantee WebFetch executes client-side JavaScript; any JS-injected links or content are invisible to this audit. |

**robots.txt** (for contrast — this one item IS confirmed, not a limitation): fetched fresh this session, full content:
```
User-agent: *
Disallow: /wp-admin/
Disallow: /wp-admin/admin-ajax.php

Sitemap: https://cashahnawaz.com/sitemap_index.xml
```
No accidental blocking of content/service paths found.

---

## 7. Cross-references

- Full per-URL evidence: `data/crawl/phase-1a-url-verification.csv`
- Sitemap structure detail and full trademark-registration collision reasoning: `data/crawl/phase-1a-sitemap-audit.md`
- WordPress plugin/theme system findings: `reports/02-wordpress-seo.md`
- Executive summary: `reports/01a-phase-1a-executive-summary.md`
- All findings tracked centrally in: `implementation/MASTER-ISSUE-TRACKER.md` (IDs TECH-001 through TECH-007)
