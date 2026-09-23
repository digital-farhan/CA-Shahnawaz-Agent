# Skill: On-Page SEO Audit

## Purpose

Audit the on-page elements (titles, meta descriptions, headings, URL structure, keyword targeting, content-to-intent match) of cashahnawaz.com's pages — especially the priority service pages — so each page is properly optimized to rank for and accurately represent the specific CA/tax/compliance service it covers.

## Scope

This skill owns: title tags, meta descriptions, heading structure (H1–H6), URL/slug structure, and content-to-search-intent match at the page level, for cashahnawaz.com's priority service pages and supporting pages.

This skill does **not** own:

- Content depth, freshness, factual accuracy, or word-count adequacy beyond intent-match triage — that's [content-audit](content-audit.md). This skill flags "content doesn't match intent"; it hands the actual content brief to content-audit.
- Internal link structure, anchor text, click depth, or navigation placement — that's [internal-linking](internal-linking.md). This skill only notes in-body linking opportunities observed while reading a page; it does not audit the link graph.
- Structured data / schema markup correctness — that's [schema-audit](schema-audit.md), even though schema fields are sometimes edited in the same plugin UI as title/meta.
- Crawlability, indexability, canonicalization conflicts, redirect chains, robots directives — that's [technical-seo](technical-seo.md). This skill assumes the crawl inventory it receives already reflects indexable pages.
- Raw URL inventory generation, status codes, and site structure mapping — that's [website-crawl](website-crawl.md); this skill consumes that output, it doesn't produce it.
- Identifying which WordPress SEO plugin is active, or plugin issues unrelated to title/meta fields — that's [wordpress-seo](wordpress-seo.md); this skill only asks it which plugin is active so it can give correct field-location instructions.
- Query-level ranking/CTR/impression data itself — that's [gsc-analysis](gsc-analysis.md); this skill cites that data when available but doesn't pull/process it.
- Page speed or image-compression impact — that's [performance-audit](performance-audit.md); this skill checks only that alt text exists, not load performance.
- Local NAP consistency / Google Business Profile — that's [local-seo](local-seo.md).
- Conversion element placement/CRO — that's [cro-audit](cro-audit.md).
- GA4 engagement metrics, GTM tag/conversion tracking, and competitor title/meta patterns — those belong to [ga4-analysis](ga4-analysis.md), [gtm-conversion-audit](gtm-conversion-audit.md), and [competitor-analysis](competitor-analysis.md) respectively; competitor patterns may be *cited* here only if supplied by competitor-analysis output, never independently gathered by this skill.

**Boundary rule of thumb:** if the question is "what does this page's `<title>`/`<meta>`/`<h1>`/URL say, and does it match what someone searching for this service would want," it's this skill. If the question is "should more content exist," "should other pages link here," or "is the underlying data structured correctly," route to content-audit, internal-linking, or schema-audit respectively.

## When to use it

- After [website-crawl](website-crawl.md) has produced the URL inventory.
- When [gsc-analysis](gsc-analysis.md) flags high-impression/low-CTR pages (title/meta issue) or pages ranking page 2 (content/on-page depth issue).
- When a priority service exists as a page but isn't performing — check whether it's actually optimized for that service before assuming it's a pure authority/content problem.

## Required Data

- URL inventory from [website-crawl](website-crawl.md) (title, meta description, H1, canonical, word count per page).
- GSC query data from [gsc-analysis](gsc-analysis.md), where available, to know which actual queries a page ranks/could rank for.
- The priority services list and the service groupings in CLAUDE.md.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS

- From a working [website-crawl](website-crawl.md): current title, meta description, H1/H2/H3 text, canonical tag, URL/slug, and image alt text per crawled page — high confidence, this is direct HTML inspection.
- From a working GSC connection ([gsc-analysis](gsc-analysis.md)): actual queries a page receives impressions/clicks for, CTR, and average position — high confidence, this is Google's own reported data, not inferred.
- Manual page-content reading (fetched/rendered page) to judge whether visible copy addresses the process/eligibility/documents/cost/timeline a searcher for that service would expect — this is professional judgment applied to real content, not a data pull. Present it as qualitative analysis, and say so explicitly.

### DATA NOT AVAILABLE

- If GSC access is not verified working this session: **the actual queries a page ranks for are unknown.** Do not guess which keywords a page "is probably ranking for" from its content alone — mark query-level findings `DATA NOT AVAILABLE` and note that any intent-match judgment made in that case rests on inspection only (what the page should logically cover for the transaction type), not on confirmed searcher behavior. State this distinction explicitly in the finding; never present an inspection-based judgment as if it were query-confirmed.
- If the crawl is stale or partial: title/meta/H1 data may not reflect the live page. Do not audit against cached/stale crawl data without flagging it as potentially outdated (see Pre-Audit Checks below).
- Pixel-width SERP truncation is approximate — character-count guidance is a heuristic, not a guarantee of display width in any given SERP. Don't state a title "will" or "won't" truncate as fact.
- Competitor title/meta patterns are only usable here if actually supplied by [competitor-analysis](competitor-analysis.md) output; never fabricate "what competitors typically do" from general knowledge.

## Pre-Audit Checks

Before starting the step-by-step process below:

1. **Confirm the crawl inventory is fresh, not stale.** Check the crawl's timestamp in `data/crawl/`. If the site has been edited since the crawl (verify with the user, or with a quick spot-fetch of a key page), re-run or re-verify the crawl before auditing titles/metas against it — auditing stale data risks recommending a "fix" to a title that's already changed, or missing one that changed for the worse.
2. **Confirm which WordPress SEO plugin is active** via the current session's [wordpress-seo](wordpress-seo.md) findings. Do not write plugin-specific "where to edit this" implementation instructions until the plugin is confirmed — different plugins put title/meta fields in different UI locations (see Implementation Recommendations below).
3. **Confirm GSC access status for this session** by attempting the actual tool call, not by assuming from a prior session. This determines whether intent-match findings can cite actual query data or must be marked inspection-only per Data Sources & Limitations above.
4. **Confirm the priority services list in CLAUDE.md hasn't changed** since the last audit, so the 1:1 page-mapping step in Step 1 starts from the correct target list.

## Step-by-Step Audit Process

1. **Map pages to intended target keyword/service.** For every priority service, identify the single page meant to rank for it. If more than one page targets the same service (keyword cannibalization risk) or no page targets it at all, flag immediately.

2. **Title tag audit**, per page:
   - Present and unique sitewide (no duplicates).
   - Includes the primary service term naturally (e.g., "GST Registration in [location] | Cashahnawaz" style — verify actual local modifier used, don't invent one not present).
   - Reasonable length (roughly 50-60 characters / won't truncate in SERP — note actual pixel truncation is approximate, treat as guidance not hard law).
   - Not keyword-stuffed, not identical to every other page's title (a common WordPress default-theme problem when titles aren't customized per page).

3. **Meta description audit**, per page:
   - Present and unique.
   - Includes the service + a reason to click (credibility signal, CTA) — CA-industry visitors are trust-sensitive, so check whether trust cues (experience, registration numbers, "free consultation," etc. — only if actually present on the page, don't invent) are reflected.
   - Reasonable length (~150-160 characters guidance).
   - If missing, note that WordPress/Yoast/RankMath will auto-generate one from content, which is usually suboptimal for conversion — flag as improvement opportunity.

4. **Heading structure audit**, per page:
   - Exactly one H1, matching page intent/service.
   - Logical H2/H3 hierarchy (no skipped levels, no H2s used just for visual styling of unrelated content).
   - Headings reflect subtopics a searcher for that service would expect (e.g., a GST Registration page might expect H2s like "Documents Required," "Process," "Fees," "Timeline" — check what's actually present, don't assume).

5. **URL structure audit**:
   - Clean, readable, includes the service term (e.g., `/gst-registration/` not `/services/?p=123`).
   - Consistent structure across similar page types (all services under a consistent path pattern).
   - No unnecessary parameters or excessive nesting depth.

6. **Keyword/intent match audit**:
   - Does the actual page content match search intent for the target service? (e.g., a page targeting "GST Registration" should address process, eligibility, documents, cost, timeline — not just a one-paragraph generic description.)
   - Cross-reference [gsc-analysis](gsc-analysis.md): what queries is this page actually getting impressions for? Does the page content genuinely serve those queries, or is Google showing it for loosely-related terms because nothing better exists (a sign of a content gap, not an on-page win)?

7. **Image optimization**:
   - Alt text present and descriptive (not filename dumps) on key images, especially any infographics/process diagrams.
   - Reasonably sized/compressed (cross-reference [performance-audit](performance-audit.md) for actual load impact).

8. **Internal contextual optimization** — hand off page-to-page linking depth to [internal-linking](internal-linking.md), but note here whether the page itself contains natural anchor-text opportunities to related services (e.g., a GST Registration page mentioning GST Return Filing without linking to it).

9. **NRI Taxation and other niche services**: confirm intent-specific content (e.g., NRI Taxation page should address NRI-specific concerns — DTAA, repatriation, residential status — not generic tax filing copy repurposed). If it reads generic, flag as a content depth issue and route to [content-audit](content-audit.md).

## What Checks to Perform

- [ ] Every priority service mapped 1:1 to a target page (no gaps, no cannibalization)
- [ ] Titles: present, unique, right length, includes service term
- [ ] Meta descriptions: present, unique, right length, includes CTA/trust cue
- [ ] Exactly one H1 per page, matches intent
- [ ] Logical heading hierarchy
- [ ] Clean, service-specific URL slugs
- [ ] Content genuinely matches search intent (not just keyword-present)
- [ ] Images have descriptive alt text
- [ ] Natural internal link opportunities identified within body content

## How to Identify Issues

Compare the crawl-captured title/meta/H1 data against the checklist above per priority page. Duplicate titles across pages are found by grouping the inventory by exact title string. Intent mismatch is found by reading actual page content against what the target query implies a searcher needs (cross-reference GSC queries where available) — do not guess intent, base it on the actual query strings and what a competent CA firm page should logically cover for that transaction type.

## Evidence to Collect

- Exact current title/meta/H1 text for each flagged page (quote it directly, don't paraphrase).
- Duplicate-title groupings.
- Specific GSC queries a page ranks for, when relevant to an intent-mismatch finding.
- Screenshot or quoted excerpt of content sections used to judge intent match.

## How to Prioritize Issues

- **CRITICAL/HIGH:** No page exists at all for a priority service; duplicate/cannibalizing pages for the same service; missing or generic-duplicate title on a priority page.
- **MEDIUM:** Suboptimal but present title/meta; missing meta description relying on auto-generation; heading hierarchy issues.
- **LOW/OPPORTUNITY:** Minor length optimization, alt text polish, additional heading refinement on already-functional pages.

## Implementation Recommendations

- Specify exact proposed title/meta text as a recommendation (clearly labeled as a *proposed draft*, not existing copy) sized to the priority service and, where evidenced, to the actual query language searchers use per GSC data.
- Note which plugin manages these fields (Yoast/RankMath/AIOSEO — confirm via [wordpress-seo](wordpress-seo.md)) and the exact admin location to edit them.
- For content/intent-depth gaps, hand off the specific content brief to [content-audit](content-audit.md) rather than trying to rewrite full page copy within this skill.

### Plugin-Specific Field Locations (confirm the plugin first)

Do not use these instructions until [wordpress-seo](wordpress-seo.md) has confirmed which SEO plugin is actually active on cashahnawaz.com. Once confirmed, title/meta/canonical fields are **typically** found as follows — phrase implementation steps with this same caution, since plugin UIs change between versions and themes, so confirm the exact current location live before publishing implementation steps as settled fact:

- **Yoast SEO:** typically the "Yoast SEO" meta box below the main content editor on each post/page edit screen, under its "Snippet Preview" / "Search appearance" tab — SEO title and Meta description fields are edited there. The Slug field lives in WordPress's native Permalink box, not the Yoast box.
- **Rank Math:** typically the "Rank Math" meta box (or its panel in the block editor sidebar), under the "General" tab — Title and Description fields are edited there, alongside the Focus Keyword field. Canonical URL overrides typically live under the same panel's "Advanced" tab.
- **All in One SEO (AIOSEO):** typically the "AIOSEO Settings" panel below the editor (or a sidebar panel in the block editor) — Title and Description fields appear on its "General" tab.

Treat these as standard/typical locations to verify live during implementation, not a guarantee for this specific site's plugin version or theme.

## How to Validate Fixes

- Re-crawl the page to confirm the new title/meta/H1 is live and correctly rendered (check both raw HTML and, if possible, how Google renders it via URL Inspection in GSC).
- Track the page's CTR and average position for its target queries in [gsc-analysis](gsc-analysis.md) over the following 2-4 weeks.
- Confirm no unintended duplicate was introduced elsewhere on the site.

## Expected Output Format

Every on-page finding produced by this skill should be written using the CLAUDE.md Required Finding Template. This skill primarily feeds the **Issue**, **Evidence**, **Affected URLs**, **Likely Root Cause**, and **Recommended Fix** fields, with **Implementation Steps** populated using the plugin-specific guidance above.

In addition to individual findings, produce a working table (attach to the report, or save under `data/crawl/`) in this format:

| URL | Target Service | Current Title | Proposed Title | Current Meta | Proposed Meta | Issue Severity |
|---|---|---|---|---|---|---|
| /gst-registration/ | GST Registration | (quoted exact current title) | (proposed draft) | (quoted exact current meta) | (proposed draft) | HIGH |

Pair this with a heading-hierarchy summary (URL, H1 present Y/N, heading issue notes) and a duplicate-title grouping list where relevant. Every "Proposed" column value must be clearly labeled as a draft recommendation pending approval, never presented as already implemented.

## Common Mistakes to Avoid

- Rewriting a title purely to hit a character-count target without checking the new version still matches actual searcher intent/query language from GSC — a title that looks more "optimized" but drifts from what people actually search for can lower CTR.
- Declaring a page "optimized" because the target keyword appears once in the copy, while the full intent behind that service query (process, eligibility, documents, cost, timeline) goes unaddressed — keyword presence is not intent coverage.
- Proposing plugin-specific implementation steps before confirming which plugin is actually active — Yoast, Rank Math, and AIOSEO field locations are similar but not identical, and wrong instructions waste implementation time.
- Flagging a missing meta description as a problem without checking whether the plugin's auto-generated fallback is actually reasonable in context — sometimes it's a genuine gap, sometimes it's a low-priority polish item.
- Treating pixel-width title-truncation guidance as a hard rule rather than a heuristic, and rejecting a good title solely because it's a few characters over 60.
- Auditing titles/metas against a stale crawl and recommending a "fix" for something already changed, or missing something newly broken.
- Assuming NRI Taxation, Startup Registration, or other niche service pages can reuse generic tax/registration copy patterns without checking whether niche-specific concerns (DTAA, repatriation, residential status for NRI; startup-specific compliance timelines for Startup Registration) are actually addressed.
- Recommending internal link additions or rewriting content depth within this skill instead of routing those findings to internal-linking.md / content-audit.md — scope creep here duplicates work and risks conflicting recommendations across skill files.
