# Skill: Google Search Console Analysis

## Purpose

Extract real, first-party search performance data (queries, clicks, impressions, CTR, average position, indexing status) for cashahnawaz.com to ground findings in actual Google-observed behavior rather than assumptions.

## Scope

This skill covers analysis of data sourced from Google Search Console for cashahnawaz.com: search queries, impressions, clicks, CTR, average position, indexing/coverage status, sitemap status, mobile usability, Core Web Vitals URL grouping, manual actions/security issues, and the Links report. It answers "how is Google observing and surfacing this site in search results, and what is Google telling us directly."

This skill does NOT cover:
- **Why** a page underperforms once a content or relevance problem is suspected (thin content, missing service coverage, poor topical depth) — that diagnosis belongs to [content-audit](content-audit.md).
- **How** a page is structured on-page (titles, meta descriptions, headings, internal anchor text) beyond flagging that a CTR/position symptom exists — the fix and on-page diagnosis belong to [on-page-seo](on-page-seo.md).
- Crawl-based technical diagnosis (broken links, redirect chains, robots.txt/canonical logic, render-blocking issues) — that's [technical-seo](technical-seo.md) and [website-crawl](website-crawl.md), even though GSC Coverage/Indexing data is used as one input to cross-check those findings.
- Post-click visitor behavior, engagement, or conversion — once a searcher lands on the site, that's [ga4-analysis](ga4-analysis.md) territory.
- Whether GTM/gtag tags actually fire correctly — that's [gtm-conversion-audit](gtm-conversion-audit.md).
- Internal link structure/architecture — [internal-linking](internal-linking.md).
- Structured data / rich result eligibility — [schema-audit](schema-audit.md), though GSC's Enhancement reports (if present) are a useful cross-check.
- WordPress-specific implementation details (plugin settings, theme templates) — [wordpress-seo](wordpress-seo.md).
- Site speed/CWV lab or field metrics in detail — [performance-audit](performance-audit.md); this skill only relays the Good/Needs Improvement/Poor URL counts GSC itself reports.
- Competitor visibility comparison — [competitor-analysis](competitor-analysis.md); this skill only reports on cashahnawaz.com's own GSC data.
- Location-based/local pack visibility — [local-seo](local-seo.md); standard GSC web search data does not include Local Pack/Maps performance.
- On-site conversion rate — [cro-audit](cro-audit.md).

In short: this skill produces the "what Google sees and how searchers interact with results before the click" evidence layer. Anything about the page itself, the click-through experience, or the underlying technical cause is handed off to the named skill, cited explicitly in the finding.

## When to use it

- To identify which priority services (Income Tax, GST, Accounting, Registration, etc.) are actually earning impressions/clicks vs. which are invisible in search.
- To diagnose traffic drops or plateaus.
- To find striking-distance keywords (position 5-20) worth optimizing.
- To check indexing status of priority pages (cross-reference with [technical-seo](technical-seo.md)).
- Before writing any claim in a report about rankings, impressions, clicks, or CTR — this is the only legitimate source for those numbers.

## Data Sources & Limitations

GSC access for the Domain Property covering cashahnawaz.com, via a working connector/tool in the current session, is the only legitimate source for query/impression/click/position/indexing data. See [Pre-Audit Checks](#pre-audit-checks) for the exact verification procedure to run before trusting any pull this session.

### AVAILABLE WITH LIVE CONNECTOR

If a working GSC connector is confirmed this session, the following becomes available:
- Search performance metrics (clicks, impressions, CTR, average position) at query level, page level, and query+page combined, filterable by date, device, search appearance, and country.
- Date range coverage typically up to 16 months of history (Domain Property, Performance report), at daily granularity.
- Coverage/Indexing report: per-URL indexing status and exclusion reason (e.g., "Discovered - currently not indexed," "Crawled - currently not indexed," "Excluded by noindex tag," "Duplicate without user-selected canonical," "Page with redirect").
- Sitemaps report: submitted sitemap(s), last read date, discovered URL counts, and reported errors.
- Mobile Usability report (where still surfaced) and Core Web Vitals URL grouping (Good/Needs Improvement/Poor counts by metric).
- Manual Actions and Security Issues reports (site-wide status).
- Links report: top linking sites, top linked pages, top linking text (GSC's own view, not a third-party backlink tool).
- URL Inspection for individual URLs: current index status, last crawl, canonical chosen by Google vs. declared, and the ability to request indexing after a fix.

### DATA NOT AVAILABLE (no connector)

If no GSC connector works this session (verification attempt fails, returns an error, or returns no property matching cashahnawaz.com), every one of the following must be marked `DATA NOT AVAILABLE` in any finding or report — Claude must never estimate, infer, or backfill these numbers from crawl data, competitor rankings, GA4 organic traffic volume, general knowledge of "what a CA firm site typically ranks for," or any prior session's cached numbers, no matter how plausible the substitute would look:
- Actual query text, impressions, clicks, CTR, or average position for any query or page.
- Actual indexing/exclusion status of any URL (a URL "looking indexable" in a crawl is not the same as GSC confirming it's indexed).
- Manual action or security issue status (never assume "none" without a checked, dated pull — an unverified manual action could be masking a CRITICAL issue).
- Sitemap submission/error status.
- Any branded vs. non-branded split, striking-distance query list, or CTR-benchmark comparison — all of these are derived from the raw performance data above and inherit its unavailability.

### Known limitations even when the connector works

- **Reporting lag**: GSC data is typically 2-3 days behind real time (sometimes more); never treat the most recent 2-3 days of data as complete, and never judge a just-shipped fix against data from inside that lag window.
- **Data sampling/rounding on small numbers**: GSC aggregates and anonymizes very-low-volume query rows (queries with very few impressions may be omitted entirely from the query report, not just rounded), so an "absent" query is not proof of zero impressions — it may be below GSC's reporting threshold.
- **Row caps**: the Performance report UI/API returns a capped number of rows per report pull (historically up to ~1,000 rows per API call without pagination); a service with a long tail of queries may have real query volume that never surfaces in a single unpaginated pull — page through results rather than assuming the first page is the whole picture.
- **"Average position" is an average, not a rank**: it blends every impression across every SERP feature and query variant for that page/query, and can be skewed by a handful of rare, high-position, irrelevant impressions (see Common Mistakes below).
- **Domain Property vs. URL-prefix Property differences**: a Domain Property aggregates http/https and subdomains; if the connector is actually scoped to a URL-prefix property instead, totals will differ from what's expected — confirm which property type is actually being queried.
- **Anonymized/(not set) values**: some query and country dimensions can return as anonymized in aggregate views: don't treat these as a data quality bug, just an inherent GSC privacy floor.

## Pre-Audit Checks

Run these before starting the substantive audit (Step 1 below formalizes the first one, but do all of these first):

- [ ] Attempt one real GSC data pull (e.g., a 7-day Performance query for a known priority-service query or the site's top page) and inspect the actual response object/property URL returned — not just "no error thrown." Confirm the property identifier in the response literally matches cashahnawaz.com (Domain Property `sc-domain:cashahnawaz.com`) before trusting any further pull this session.
- [ ] Confirm it is the Domain Property, not a URL-prefix property (e.g., `https://cashahnawaz.com/` only) or a different/sibling property the account may also have access to — these can return materially different totals.
- [ ] Confirm the date range actually applied to the query isn't silently empty or defaulting to a window with no data (e.g., a future date range, or a range before the property existed) — check that returned row counts and total clicks/impressions are non-zero for a window known to have activity, before concluding "no data" means "no visibility."
- [ ] Check whether the account/connector has Owner or at least Full user access to the property — Restricted access can silently omit reports (Links, some Enhancement reports).
- [ ] Note today's date (2026-08-27) relative to India's tax filing calendar (e.g., ITR season, GST return due dates) — GSC trend swings around these dates are seasonal, not necessarily SEO-driven; don't attribute a July dip to a fix regression without checking whether it lines up with a filing-deadline traffic pattern from a prior year.
- [ ] If pulling Coverage/Indexing data, confirm the report type is current ("Indexing > Pages," not a deprecated "Index Coverage" naming) so the exclusion-reason taxonomy referenced in this skill still matches what the tool returns.

## Step-by-Step Audit Process

1. **Verify access.** Confirm the connector works and confirm it's reporting on the correct property (cashahnawaz.com Domain Property, not a different site).

2. **Pull the Performance report** for a meaningful trailing window (start with last 3 months, then extend to 12-16 months if available for trend/seasonality context). Capture: total clicks, impressions, average CTR, average position, and the trend over time.

3. **Query-level analysis.**
   - Pull top queries by impressions and by clicks.
   - Map queries to the priority services list in CLAUDE.md. For each priority service, determine: is it generating impressions at all? What's the average position? What's the CTR relative to expected CTR at that position?
   - Identify **striking-distance queries**: position 5-20, decent impressions, low clicks — prime optimization targets.
   - Identify **branded vs. non-branded** query split (branded = "cashahnawaz" or close variants) — a business overly reliant on branded search has an organic visibility problem regardless of headline traffic numbers.
   - Identify queries with high impressions but very low CTR — potential title/meta description problems (hand off to [on-page-seo](on-page-seo.md)).

4. **Page-level analysis.**
   - Pull top pages by clicks and by impressions.
   - Cross-reference against the priority service page list: which priority pages get zero or near-zero impressions? That's a visibility gap.
   - Identify pages with impressions but poor CTR — title/meta issue.
   - Identify pages ranking but positioned 11-20 (page 2) — content/authority gap.

5. **Coverage / Indexing report.**
   - Pull the Indexing report. List URLs marked "Not indexed" and their exclusion reason (e.g., "Discovered - currently not indexed," "Crawled - currently not indexed," "Excluded by noindex tag," "Duplicate without user-selected canonical").
   - Cross-reference excluded priority pages against [technical-seo](technical-seo.md) crawl findings.

6. **Core Web Vitals report** (if available in this GSC view) — pull Good/Needs Improvement/Poor URL group counts; hand detail to [performance-audit](performance-audit.md).

7. **Mobile usability report** — pull any reported issues.

8. **Sitemaps report** — confirm submitted sitemap(s) match what [technical-seo](technical-seo.md) found live, and check for reported errors.

9. **Manual actions / Security issues report** — always check this; a manual action or security issue would explain otherwise-mysterious performance collapse and is CRITICAL by definition.

10. **Links report** (if available) — top linking sites and top linked pages, as a rough, GSC-native (not third-party) signal for [competitor-analysis](competitor-analysis.md)/authority context.

## What Checks to Perform

- [ ] Access verified with an actual successful pull, correct property confirmed
- [ ] 3-month (minimum) and longer-trend performance data pulled
- [ ] Every priority service mapped to its query/impression/position data (or marked DATA NOT AVAILABLE/no visibility)
- [ ] Branded vs non-branded split calculated
- [ ] Striking-distance queries identified
- [ ] High-impression/low-CTR queries and pages identified
- [ ] Indexing report pulled, exclusions categorized
- [ ] Manual actions/security issues checked
- [ ] Sitemap status cross-checked against live sitemap

## How to Identify Issues

- A priority service with zero/near-zero impressions across all related queries = visibility gap (OPPORTUNITY or HIGH depending on commercial value and whether a page exists at all).
- A page with high impressions but CTR well below the CTR benchmark for its average position = title/meta problem (HIGH/MEDIUM).
- A priority page listed as "Excluded" in Coverage = technical blocker (CRITICAL/HIGH, cross-file with technical-seo).
- Heavy branded-query dependence (e.g., >60-70% of clicks from brand terms) with weak non-branded presence = overall organic visibility issue (HIGH).
- Any manual action or security issue = CRITICAL, top of the list, address before anything else.

## Evidence to Collect

Export/save the following into `data/gsc/` with the pull date in the filename:
- `data/gsc/performance-summary-YYYY-MM-DD.csv`
- `data/gsc/queries-YYYY-MM-DD.csv`
- `data/gsc/pages-YYYY-MM-DD.csv`
- `data/gsc/coverage-YYYY-MM-DD.csv`
- Notes on manual actions/security issues status (even if "none found" — record that as a checked, clean result with date)

## How to Prioritize Issues

Use CLAUDE.md severity definitions. GSC-sourced findings tend to skew CRITICAL/HIGH when they involve indexing exclusion or manual actions, and OPPORTUNITY/MEDIUM when they involve CTR/position optimization on already-indexed, already-ranking pages.

## Implementation Recommendations

GSC data tells you *what* is wrong; the fix usually lives in another skill (title/meta → [on-page-seo](on-page-seo.md); indexing → [technical-seo](technical-seo.md); content depth → [content-audit](content-audit.md)). Always name which skill's fix applies rather than inventing a generic recommendation here.

## How to Validate Fixes

- After a fix (e.g., rewritten title tag, resolved noindex), use URL Inspection to request re-indexing.
- Track the specific query/page's impressions, CTR, and position over the following 2-6 weeks (GSC data has inherent lag — do not judge a fix within days).
- Always compare against the pre-fix baseline saved in `data/gsc/`, not against memory or estimate.

## Expected Output Format

This skill primarily feeds the **Evidence**, **Affected URLs**, and **SEO Impact** fields of the CLAUDE.md finding template; it also frequently supplies the factual basis cited in **Likely Root Cause** (e.g., "Excluded by noindex tag" from Coverage).

**Tables/CSVs produced**, with exact column headers:

- `queries-YYYY-MM-DD.csv`: `Query | Impressions | Clicks | CTR | Avg Position | Mapped Service | Page`
- `pages-YYYY-MM-DD.csv`: `Page URL | Impressions | Clicks | CTR | Avg Position | Mapped Priority Service | Indexing Status`
- `coverage-YYYY-MM-DD.csv`: `URL | Status | Exclusion Reason | Mapped Priority Service | Last Crawled`
- `performance-summary-YYYY-MM-DD.csv`: `Date | Clicks | Impressions | CTR | Avg Position` (one row per day/week of the pulled window)
- Service mapping rollup (can be a section of the report rather than a separate CSV): `Priority Service | Query Count | Total Impressions | Total Clicks | Avg Position | Has Dedicated Page (Y/N) | Visibility Verdict`

**In the audit report**, every finding sourced from GSC should cite the specific CSV and row(s)/date range it came from in the Evidence field (e.g., "Evidence: `data/gsc/pages-2026-08-27.csv`, row for `/gst-registration/`, 0 impressions over 90-day window").

**A `DATA NOT AVAILABLE` entry must still use the full finding template**, not be silently dropped. Example shape:

```
### [N/A — DATA NOT AVAILABLE] GSC connector unavailable this session

- **Issue:** GSC-sourced query/impression/click/position/indexing data could not be retrieved.
- **Severity:** Cannot be assessed — severity depends on the missing data.
- **Evidence:** DATA NOT AVAILABLE — connector attempt on [date] returned [error/no matching property]. No prior-session data substituted.
- **Affected URLs:** DATA NOT AVAILABLE — cannot determine which priority service pages are impacted without query/page-level data.
- **SEO Impact:** Cannot be quantified without GSC data; this gap blocks assessment of the "Organic Visibility" stage of the success journey for all priority services.
- **Likely Root Cause:** Connector/authentication issue, not a site issue — do not conflate with an actual visibility problem.
- **Recommended Fix:** Restore GSC connector access, then re-run this skill.
- **Implementation Steps:** N/A until access restored.
- **Validation Method:** Successful pull returning real property/query data confirms resolution.
```

## Common Mistakes to Avoid

- **Confusing branded-query dominance with genuine visibility strength.** High total clicks driven mostly by "cashahnawaz" / "CA Ahnawaz" variants can mask near-zero non-branded visibility for GST/Income Tax/Registration terms — always report the branded/non-branded split, not just totals.
- **Treating "average position" as a real SERP rank.** A page can show Avg Position 4 while never actually ranking top-5 for any commercially relevant query, if a handful of rare, irrelevant, high-position impressions (e.g., a long-tail navigational query) skew the average. Always sanity-check average position against the underlying query list, not the summary number alone.
- **Reading query/page rows in isolation from the priority services list.** A query like "company registration documents required" should be mapped to Registration & Compliance even if it doesn't contain the literal service name — missing this mapping undercounts real visibility for a priority service.
- **Judging a fix too soon.** GSC data lags 2-3 days and Google needs time to recrawl/reprocess after any on-page change; don't declare a title-tag fix "not working" from data inside the first 1-2 weeks.
- **Treating an "absent" query as proof of zero impressions.** GSC omits very-low-volume rows from the query report; absence from the exported list is not the same as a confirmed zero — say "not surfaced in the pull" rather than "zero impressions" unless the page-level total impression count is itself confirmed at/near zero.
- **Not distinguishing Domain Property scope from URL-prefix scope**, especially if the site has ever served content on `www.` vs. non-`www`, or http vs. https — mismatched scope produces numbers that look wrong but are actually just measuring a different set of URLs.
- **Attributing a seasonal dip or spike to an SEO cause.** A CA/tax firm's search demand is inherently cyclical around ITR and GST filing deadlines; check year-over-year or prior-cycle GSC trend before attributing a change to a technical or content fix.
- **Silently omitting a finding when GSC access fails**, instead of producing the explicit DATA NOT AVAILABLE finding shown above — an audit that just skips the GSC section without saying why looks incomplete rather than honest about a connector gap.
