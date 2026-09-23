# Skill: SEO Opportunity Mining

## Purpose

Systematically mine GSC, GA4, crawl and competitor data for the specific, actionable opportunities that already exist in the site's own performance data — near-miss rankings, queries with impressions but no clicks, queries with no dedicated page, cannibalization, emerging terms, local and NRI opportunities, and long-tail commercial queries — and assign each an Impact / Confidence / Effort / Priority rating so effort goes where the return is.

This is the highest-yield analysis available to any established site, because it works from demonstrated demand rather than speculation: a query already showing impressions is proof that Google considers the site relevant for it.

## Scope

**This skill owns:** the systematic mining of existing performance and crawl data into a prioritised opportunity register, with Impact / Confidence / Effort / Priority assigned to each item.

**This skill does NOT own:**
- Pulling and interpreting GSC data generally — [gsc-analysis](gsc-analysis.md), whose exports this skill consumes. That skill answers "what is the data"; this one answers "what should we do about it."
- GA4 behavioural analysis — [ga4-analysis](ga4-analysis.md).
- Deciding what content to build from an opportunity — [linkable-content-planner](linkable-content-planner.md), which applies the dual SEO × Linkability gate.
- Fixing decayed pages — [content-decay-refresh](content-decay-refresh.md), which looks backward at decline; this skill looks forward at unrealised potential.
- SERP composition analysis — [serp-intelligence](serp-intelligence.md).
- Title/meta rewrites — [on-page-seo](on-page-seo.md); this skill identifies the CTR opportunity, that skill owns the rewrite.
- Cannibalization diagnosis and resolution — [content-audit](content-audit.md); this skill flags the pattern in query data.
- Implementing anything — the user does that.

## When to use it

- Whenever GSC access is available — this is the first thing to do with it.
- Quarterly, and after major content or technical work, to see what moved.
- When planning a content or optimisation cycle, so the plan starts from evidence.
- Before commissioning new content, to check whether an existing page could capture the demand instead.

## Required Data

- **GSC Performance data** — queries, pages, clicks, impressions, CTR, average position, with query×page detail and a comparable prior period. This is the core input.
- GA4 engagement and conversion data by landing page, if available.
- `data/crawl/` inventory, `service-coverage-map.md`, `priority-urls.md`.
- Competitor coverage from [competitor-analysis](competitor-analysis.md).

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- GSC Performance exports — the only source for query-level impressions, CTR and position for this site.
- GA4 landing-page engagement and conversions.
- Crawl inventory and coverage map — available now, and enough on their own to support the service-gap and coverage strands.
- Competitor coverage observations.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Everything query-level, without GSC.** Per `reports/00-capability-check.md`, no GSC connector was available at the last verified check. Without it, these are all `DATA NOT AVAILABLE`: keywords ranking 4–20, high-impression/low-CTR queries, declining or rising rankings, impression trends, query-level cannibalization evidence, and emerging search terms. **Most of this skill cannot run without GSC** — say so plainly rather than substituting assumption.
- Search volume for queries the site does not already rank for — no keyword tool exists here.
- Competitor query data.
- Conversion data without GA4.
- Predicted traffic gain from an optimisation. Any projection is an `ESTIMATE` with its basis stated, never a figure presented as a forecast.

**What remains possible without GSC:** service-coverage gap analysis, priority-service page-existence checks, and competitor-coverage comparison — all from crawl data already in the project. That is a genuine subset worth running, and it should be labelled as the partial analysis it is.

## Pre-Audit Checks

1. Verify GSC and GA4 availability, and **declare which strands can run**. Do not present a coverage-gap analysis as opportunity mining if the query strands were impossible.
2. Confirm the comparison period is genuinely comparable — for tax content, year-on-year almost always beats period-on-period, because filing seasons dominate everything else.
3. Load the coverage map and priority URLs.
4. Confirm which services the firm actually delivers, so opportunities are not mined for work it cannot take on.

## Step-by-Step Audit Process

### Strand 1 — Keywords ranking positions 4–20

Filter GSC for queries where average position sits between roughly 4 and 20. These are the highest-confidence opportunities available: Google already ranks the site, so the work is improvement rather than establishment.

Split them:
- **Positions 4–10** — small gains produce disproportionate click increases. Usually on-page and intent-match work.
- **Positions 11–20** — page two. Typically needs content depth, intent realignment, internal links, or authority.

For each, record the query, the ranking page, impressions, position, and whether the ranking page is the *right* page for the query. A mismatch is itself the finding, and often the cheapest fix available.

### Strand 2 — High-impression / low-CTR queries

Find queries with meaningful impressions and a CTR well below what the position would normally deliver. Diagnose before prescribing:

- **Title/meta mismatch** → [on-page-seo](on-page-seo.md).
- **Intent mismatch** — the page ranks but does not answer the query; a rewrite of the title will not fix it.
- **SERP features** absorbing clicks → [serp-intelligence](serp-intelligence.md), [ai-search-visibility](ai-search-visibility.md).
- **Brand-dominated SERP** where a low CTR is normal.

Do not treat every low CTR as a title problem. Position-normalised expectations vary enormously by query type, and there is no CTR benchmark available in this project — so compare against the site's own comparable queries rather than an invented industry curve.

### Strand 3 — Pages with declining or increasing impressions

- **Declining** → route to [content-decay-refresh](content-decay-refresh.md) after excluding seasonality.
- **Increasing impressions without clicks** → a page gaining relevance but not converting the impression; often the best short-term opportunity in the whole register, because Google is already moving in the site's favour.

### Strand 4 — Queries without dedicated pages

Find queries generating impressions where the ranking page is a generic or tangential page rather than a dedicated one. Cross-check against `service-coverage-map.md`. Where a priority service has demonstrated demand and no dedicated page, that is a strong, evidence-backed content opportunity — route to [linkable-content-planner](linkable-content-planner.md) for the build/no-build decision.

### Strand 5 — Cannibalization

Find queries where multiple URLs alternate or compete. Record every URL, its impressions and position for that query. Route the diagnosis and resolution to [content-audit](content-audit.md) — resolving cannibalization is frequently a faster win than any new content, because the demand and the pages already exist.

### Strand 6 — Emerging search terms

Identify queries appearing recently with no prior history — new regulations, new schemes, new deadlines, newly-relevant terms. In tax, these often follow a Budget or a notification, and being early is genuinely valuable because competition has not formed. Verify the underlying change against primary sources ([eeat-ymyl-authority](eeat-ymyl-authority.md)) before recommending content on it.

### Strand 7 — Local, service-gap, industry, NRI and long-tail commercial

- **Local** — queries with Mumbai and locality modifiers; route to [local-seo](local-seo.md).
- **Service gaps** — priority services with no page or a thin one, from the coverage map. **Runs without GSC.**
- **Industry-specific** — sector-specific compliance queries.
- **NRI** — a named priority service and a distinct, high-value audience with its own query language; worth a dedicated strand.
- **Long-tail commercial** — specific, high-intent, low-competition queries ("company registration cost in Mumbai", "GST registration documents for proprietorship"). Individually small, collectively significant, and usually the fastest route to qualified enquiries.

### Strand 8 — Rate every opportunity

Assign the specification's four ratings, each with its basis recorded:

| Rating | Scale | Based on |
|---|---|---|
| **Impact** | High / Medium / Low | Demonstrated impressions × commercial value of the query |
| **Confidence** | High / Medium / Low | Strength of the evidence and clarity of the diagnosis |
| **Effort** | High / Medium / Low | Realistic work: a title rewrite vs. a new researched page |
| **Priority** | P1 / P2 / P3 | Derived from the three above |

Priority is not a formula: a Medium-impact, High-confidence, Low-effort item is usually P1, while a High-impact, Low-confidence, High-effort item is usually P2 or P3. Record the reasoning so the register can be challenged.

## What Checks to Perform

- [ ] Data availability verified; runnable strands declared
- [ ] Comparison period genuinely comparable (year-on-year for seasonal content)
- [ ] Positions 4–20 mined, with ranking-page correctness assessed per query
- [ ] Low-CTR queries diagnosed, not assumed to be title problems
- [ ] Declining vs. rising impressions separated and routed
- [ ] Queries without dedicated pages cross-checked against the coverage map
- [ ] Cannibalization patterns captured with all competing URLs
- [ ] Emerging terms verified against primary sources before being acted on
- [ ] Local, service-gap, industry, NRI and long-tail strands run
- [ ] Impact / Confidence / Effort / Priority assigned with recorded reasoning
- [ ] Opportunities checked against services the firm actually delivers
- [ ] No query-level claim made without GSC data behind it

## How to Identify Issues

An opportunity here is a **gap between demonstrated demand and captured value**, evidenced by the site's own data: impressions without clicks, positions just outside the click range, queries landing on the wrong page, demand with no dedicated page, or two pages splitting one query. The best findings combine high commercial value with low effort and high confidence — typically an intent or title mismatch on a priority service query already ranking at position 5–8.

## Evidence to Collect

Save to `data/gsc/` and `reports/`:
- `opportunity-register-YYYY-MM-DD.csv` — one row per opportunity: strand, query, page, impressions, clicks, CTR, position, diagnosis, action, owning skill, Impact, Confidence, Effort, Priority.
- `opportunity-mining-YYYY-MM-DD.md` — method, periods compared, strands run, strands unavailable, and the reasoning behind the top items.
- Raw GSC exports for the periods used, so every figure is traceable.
- `service-gap-analysis.md` — the GSC-independent strand.

## How to Prioritize Issues

- **P1** — high commercial value, strong evidence, low effort: intent/title mismatches on priority service queries at positions 4–10; cannibalization on a commercial query; a priority service with demonstrated demand and no dedicated page.
- **P1** — rising impressions with no clicks on a priority page.
- **P2** — position 11–20 opportunities needing content work; long-tail clusters worth a consolidated page; local-modifier gaps.
- **P3** — low-volume long-tail; speculative emerging terms; high-effort/low-confidence items.
- **Not an opportunity** — queries for services the firm does not deliver, which would generate exactly the unqualified enquiries CLAUDE.md counts as a failure.

Weight by proximity to an enquiry throughout. An opportunity that produces traffic but no qualified contact does not advance the success journey.

## Implementation Recommendations

Manual, for the user, and routed to the owning skill rather than prescribed here.

- **Title/meta rewrites** → [on-page-seo](on-page-seo.md) supplies the exact strings; the user enters them in Rank Math.
- **Intent mismatch** → content restructure spec via [content-audit](content-audit.md) / [ai-search-visibility](ai-search-visibility.md).
- **Cannibalization** → consolidation plan with canonical/redirect decisions via [content-audit](content-audit.md).
- **New dedicated page** → [linkable-content-planner](linkable-content-planner.md) for the build decision, then a brief.
- **Internal linking** → [internal-linking](internal-linking.md).
- **Authority-limited opportunities** → [off-page-seo](off-page-seo.md), [backlink-opportunity-hunter](backlink-opportunity-hunter.md).
- Every item carries the page, the change, and the expected effect stated as a labelled `ESTIMATE` with its basis — never a predicted traffic number.

## How to Validate Fixes

- **Per opportunity:** compare the same query×page in GSC across comparable windows after the change, allowing several weeks. Record the actual outcome against what was expected.
- **Calibration:** review closed opportunities to see whether the ratings were accurate. Persistently over-rated Impact means the register is being scored optimistically, and that is worth correcting.
- **Cannibalization:** confirm one URL now holds the query consistently.
- **Business outcome:** enquiries and conversions via GA4 if available; otherwise `DATA NOT AVAILABLE`.
- Never claim a causal win from a single week, and never claim one at all where several changes shipped together — say what changed and what moved.

## Expected Output Format

1. **Availability header**, e.g.:

   > No GSC access this session (verified). Strands 1–6 are `DATA NOT AVAILABLE`. This report contains only the service-coverage and competitor-coverage strands, derived from crawl data already in the project. It is a partial analysis and should not be read as an opportunity mining run.

2. **Opportunity register table:**

   | # | Strand | Query | Page | Impr | CTR | Pos | Diagnosis | Action | Owner skill | I / C / E | Priority |
   |---|---|---|---|---|---|---|---|---|---|---|---|

3. **Top 10 by priority**, each with its reasoning.
4. **Routing summary** by owning skill.
5. **Excluded** — opportunities for services the firm does not deliver, and why.
6. Findings in the standard CLAUDE.md template with Confidence Level and Evidence Source.

## Common Mistakes to Avoid

- **Running this without GSC and calling it opportunity mining.** Without query data most strands are impossible; the honest output is the partial coverage analysis, clearly labelled.
- **Comparing period-on-period on seasonal tax content** and reading the filing-season cliff as decay or growth.
- **Treating every low CTR as a title problem** rather than diagnosing intent, SERP features, or brand dominance.
- **Inventing a CTR benchmark.** No such data exists here; compare against the site's own queries.
- **Predicting traffic gains** as figures rather than labelled estimates.
- **Mining opportunities for services the firm does not offer**, which generates unqualified leads.
- **Refreshing or building for a cannibalized query** instead of resolving the cannibalization first.
- **Acting on an emerging term without verifying the underlying regulatory change** against a primary source.
- **Producing a register nobody can act on.** Fifteen well-reasoned P1s beat three hundred rows.
- **Ignoring the "is this the right page?" question**, which is frequently the real finding behind a stuck ranking.
