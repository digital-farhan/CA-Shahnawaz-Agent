# Skill: SERP & Competitor Intelligence

## Purpose

Monitor what the search results actually look like for the firm's important commercial keywords, and explain *why* the ranking order is what it is. The standard this skill is held to is the specification's: answer **"why did the competitor move above us?"** — not merely "the competitor ranks higher."

A ranking position is an outcome. This skill exists to find the cause, so the response is a specific, evidenced change rather than a guess.

## Scope

**This skill owns:** SERP composition monitoring for priority commercial keywords (top 10 results, SERP features, AI Overviews where visible, local pack, People Also Ask, featured snippets), competitor page-level analysis for those SERPs, change detection over time, and causal diagnosis.

**This skill does NOT own:**
- The firm's own query performance data — [gsc-analysis](gsc-analysis.md), [seo-opportunity-mining](seo-opportunity-mining.md).
- Competitor positioning, service coverage and business verification generally — [competitor-analysis](competitor-analysis.md), whose verification requirements this skill inherits.
- Competitor referring-domain gaps — [competitor-backlink-gap](competitor-backlink-gap.md).
- Whether the firm is cited by answer engines — [ai-search-visibility](ai-search-visibility.md), though AI Overview *presence* on a SERP is recorded here.
- Local pack ranking factors and GBP — [local-seo](local-seo.md); this skill records that a local pack appeared and who is in it.
- Fixing anything — the owning skills specify fixes; the user implements.

## When to use it

- When a priority commercial keyword loses position and the cause is not obvious.
- Before optimising a page, to establish what actually ranks and what the SERP rewards.
- On a recurring cycle for a fixed keyword set, so change is detectable rather than anecdotal.
- When [seo-opportunity-mining](seo-opportunity-mining.md) surfaces a position 4–20 opportunity and the question is what stands between the page and the top.

## Required Data

- A defined, stable set of priority commercial keywords — the same set each cycle, or nothing is comparable.
- Search capability to observe the SERP.
- Fetch capability to analyse the pages that rank.
- The firm's own ranking data ([gsc-analysis](gsc-analysis.md)) where available.
- Prior cycle observations, for change detection.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- **Direct SERP observation** for a keyword, if a search tool is verified live: which pages rank, in what order, and which features are present.
- **Direct analysis of the ranking pages themselves** by fetching them — content format and depth, structure, freshness signals, author expertise, schema, internal linking. This is fully obtainable and is where most of the causal insight comes from.
- Competitor page comparison against the firm's own page on the same dimensions.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Rank tracking.** No rank-tracking tool exists in this project (`reports/00-capability-check.md`). Positions are point-in-time observations, not tracked rankings, and they must be labelled with the date and method.
- **A neutral, canonical SERP.** Results are personalised, localised, device-dependent and continuously tested. An observation is a sample of one context, not "the ranking." This caveat belongs in every output.
- **Competitor backlink profiles** for the ranking pages — no tool. `DATA NOT AVAILABLE`; the specification lists backlink profiles as a monitored dimension, and the honest position here is that it can be discussed only qualitatively via [competitor-backlink-gap](competitor-backlink-gap.md)'s observation-based method.
- Search volume, traffic, or click share for any SERP.
- **AI Overview presence** unless actually observed — it varies by query, user and time, so absence in one observation is not absence.
- Why Google ranked something, definitively. Every causal statement here is an evidenced hypothesis and must be labelled as such.

## Pre-Audit Checks

1. Verify search capability this session; without it, only page-level analysis of known competitors is possible.
2. **Fix the keyword set** and keep it stable across cycles. A changing set makes change detection meaningless.
3. Record observation conditions — date, approximate location context, device assumption — since they materially affect results.
4. Re-verify competitors per [competitor-analysis](competitor-analysis.md) before analysing their pages.

## Step-by-Step Audit Process

### Step 1 — Define the keyword set

Anchor it to priority commercial services and real client language: `CA in Mumbai`, `GST registration Mumbai`, `income tax return filing Mumbai`, `company registration Mumbai`, `NRI taxation consultant`, and comparable terms across the priority services. Keep it small enough to observe properly each cycle — 15–25 well-chosen keywords beat 200 skimmed.

### Step 2 — Record SERP composition

For each keyword, record:

- **Top 10 organic results** — URL, domain, page type (service page, blog, directory, government portal, aggregator).
- **SERP features present** — AI Overview, featured snippet, local pack, People Also Ask, images, videos, sitelinks, ads.
- **Local pack** — which businesses appear, if any.
- **People Also Ask** — the actual questions, which are direct evidence of related intent and feed [ai-search-visibility](ai-search-visibility.md).
- **Featured snippet** — whether one exists, which page holds it, and its format.
- **The firm's own position**, if present.

A critical observation for this market: many CA-services SERPs are dominated by large aggregators and government portals rather than individual firms. Where that is true, the realistic objective changes — competing for the local pack and long-tail commercial queries may be far more valuable than pursuing a head term the site cannot win. Say so when the evidence shows it.

### Step 3 — Analyse the pages that rank

For the top results plus the firm's own page, fetch and compare on the specification's dimensions:

| Dimension | What to record |
|---|---|
| **Content format** | Service page, guide, listicle, tool, directory listing |
| **Content depth** | Structure, subtopics covered, specificity, worked detail |
| **Page depth** | How many clicks from the site's homepage; is it a top-level page? |
| **Freshness** | Visible publication/updated dates, current AY/FY, current rates |
| **Author expertise** | Named author, credentials, bio ([eeat-ymyl-authority](eeat-ymyl-authority.md)) |
| **Schema** | Types present |
| **Internal links** | How the site supports the page |
| **Backlink profile** | `DATA NOT AVAILABLE` — qualitative only |

Compare like with like: judge the firm's page against what actually ranks, not against an abstract standard.

### Step 4 — Identify what changed

Compare against the prior cycle's record:

- Position changes for the firm and for competitors.
- New entrants and departures.
- SERP feature changes — an AI Overview or new local pack can reduce clicks without any position change, which is a critical distinction when diagnosing a click decline.
- Content changes on competitor pages — did they update, expand, restructure, add author credentials, or add schema?
- Intent shift — is Google now serving a different kind of page for the query? This is common after tax changes, and it means the firm's page type may simply no longer match.

### Step 5 — Answer "why", with evidence

For each meaningful change, construct an evidenced hypothesis rather than an assertion. State: what was observed, what changed, the most plausible explanation, the evidence for it, alternatives not excluded, and confidence.

For example — *"Competitor page moved from 6 to 3. Observed: they added a 2026-27 rates table, a named CA author with membership number, and an FAQ block, and their updated date changed. Our page carries no visible date and no author. Hypothesis: freshness and expertise signals on a YMYL query. Confidence: LIKELY. Not excluded: authority changes we cannot measure, or an unrelated algorithm update."*

That is a usable finding. "They rank higher because they have better SEO" is not.

Never assert causation Google has not disclosed and no tool can isolate. Confidence levels are mandatory here.

### Step 6 — Route

Content depth → [content-audit](content-audit.md). Freshness → [content-decay-refresh](content-decay-refresh.md). Authorship → [eeat-ymyl-authority](eeat-ymyl-authority.md). Schema → [schema-audit](schema-audit.md). Internal links → [internal-linking](internal-linking.md). Authority → [competitor-backlink-gap](competitor-backlink-gap.md). Titles/intent → [on-page-seo](on-page-seo.md). Local pack → [local-seo](local-seo.md). Answer formatting → [ai-search-visibility](ai-search-visibility.md).

## What Checks to Perform

- [ ] Keyword set fixed and unchanged from the prior cycle
- [ ] Observation date and conditions recorded
- [ ] Top 10 recorded per keyword, with page types
- [ ] All SERP features recorded, including AI Overview presence
- [ ] PAA questions captured verbatim
- [ ] Local pack composition recorded where present
- [ ] Ranking pages fetched and compared on all available dimensions
- [ ] SERP dominance by aggregators/government portals noted where present
- [ ] Changes since prior cycle identified
- [ ] Every causal statement framed as a hypothesis with evidence, alternatives and confidence
- [ ] Competitor backlink profiles marked `DATA NOT AVAILABLE`
- [ ] Personalisation/localisation caveat stated
- [ ] Findings routed to owning skills

## How to Identify Issues

The finding is a **specific, observable difference between the firm's page and the pages outranking it, on a dimension the firm can change.** Freshness, author credentials, answer structure, content depth, schema and internal support are all actionable; authority differences usually are not, in the short term, and should be reported honestly as such rather than dressed up as a quick fix. The most valuable finding of all is often structural: *this SERP is not winnable for an individual firm, and effort should move to the local pack and long-tail queries where it is.*

## Evidence to Collect

Save to `data/competitors/` and `data/serp/`:
- `serp-snapshot-YYYY-MM-DD.md` — per keyword: full top 10, features, PAA questions, local pack, the firm's position, observation conditions.
- `serp-tracking.csv` — keyword, date, position per domain, so change is comparable across cycles.
- `page-comparison-<keyword>.md` — the dimension-by-dimension comparison of the ranking pages against the firm's page.
- `serp-change-log.md` — what changed and the evidenced hypothesis for each.
- Quote competitor page elements directly (their heading, their answer opening, their date line) rather than characterising them.

## How to Prioritize Issues

- **HIGH** — a priority commercial keyword where the firm has dropped out of the top 10, with an identified, fixable cause.
- **HIGH** — a fixable gap present across most top-ranking pages and absent on the firm's page (dates and author credentials are the recurring ones in this category).
- **MEDIUM** — a new SERP feature absorbing clicks; a competitor gaining through a change the firm could match; positions 4–10 with a clear gap.
- **LOW** — small movements within a stable SERP; low-value keywords.
- **OPPORTUNITY** — an unclaimed featured snippet or PAA answer; a local pack the firm is absent from.
- **Strategic finding** — a SERP structurally dominated by aggregators and portals, warranting a change of target rather than more effort.

## Implementation Recommendations

Routed to owning skills; all executed manually by the user.

- Supply the **specific difference**, quoted from the competitor page, alongside the firm's current state, so the recommendation is concrete: "top three results all show a visible updated date and a named CA author; the firm's page shows neither."
- For **featured snippet opportunities**, specify the format the current snippet uses (paragraph, list, table) and the exact restructure needed ([ai-search-visibility](ai-search-visibility.md)).
- For **intent mismatch**, specify the page type that actually ranks and whether the firm's page should be restructured or a different page targeted.
- For **unwinnable head terms**, recommend the reallocation explicitly — that is a legitimate, valuable recommendation, and pursuing an unwinnable term is a real cost.
- Never recommend copying a competitor tactic without evidence it is plausibly connected to the outcome.

## How to Validate Fixes

- **Re-observe the same keyword set** next cycle under the same recorded conditions, and compare. A single re-check the day after a change is not validation.
- **Corroborate with GSC** where available — impressions and average position across a comparable window are more reliable than a point-in-time observation, since they aggregate across contexts.
- **Feature capture:** confirm whether the firm now holds the snippet or appears in the local pack.
- Report movement as correlation, and state what else changed in the period. Where multiple changes shipped together, do not attribute the result to one of them.

## Expected Output Format

1. **Method and caveats header**, e.g.:

   > SERP observations recorded on [date] via direct search. No rank-tracking tool exists in this project (verified), so these are point-in-time observations, not tracked rankings. Results are personalised and localised; a single observation is a sample of one context. Competitor backlink profiles are `DATA NOT AVAILABLE`.

2. **Per-keyword SERP snapshot** — top 10, features, PAA, local pack, the firm's position.
3. **Page comparison matrix** for the priority keywords.
4. **Change log** — what moved, with evidenced hypotheses and confidence levels.
5. **Findings** in the standard CLAUDE.md template, routed to owning skills.
6. **Strategic observations** — SERPs worth pursuing and SERPs worth abandoning.

## Common Mistakes to Avoid

- **Reporting a position as a tracked ranking.** It is one observation in one context on one date.
- **Answering "they rank higher" instead of "why".** The whole point of the skill.
- **Asserting causation.** Every explanation is a hypothesis with evidence, alternatives and confidence.
- **Quoting competitor backlink metrics** that no tool produced.
- **Changing the keyword set between cycles**, destroying comparability.
- **Ignoring SERP feature changes** when diagnosing a click decline — an AI Overview can cut clicks with position unchanged.
- **Recommending "make it longer"** as a response to a depth gap without checking what the ranking pages actually do.
- **Missing an intent shift** and optimising a page type Google no longer serves for the query.
- **Chasing a SERP owned by government portals and aggregators** instead of reporting it as unwinnable and redirecting effort.
- **Treating PAA questions as noise.** They are free, direct evidence of related intent and should feed content and answer structure.
