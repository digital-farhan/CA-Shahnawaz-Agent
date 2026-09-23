# Skill: Linkable Content Planner

## Purpose

Decide what content actually gets built, by scoring every proposed page on two independent dimensions — can it rank, and can it earn references — and prioritising only what scores well on both. The governing rule is the specification's: **do not create content merely because a keyword exists.** For a firm with already-broad service coverage, the next stage is authority consolidation, not indiscriminate page creation.

## Scope

**This skill owns:** the dual SEO × Linkability scoring model, the resulting content priority order, and the decision of build / improve existing / do not build.

**This skill does NOT own:**
- Generating and specifying linkable asset concepts — [digital-pr-link-assets](digital-pr-link-assets.md) supplies candidates; this skill scores and sequences them.
- Discovering keyword and query opportunities — [seo-opportunity-mining](seo-opportunity-mining.md).
- Auditing existing content quality, depth, or cannibalization — [content-audit](content-audit.md).
- Refreshing decayed pages — [content-decay-refresh](content-decay-refresh.md).
- Writing the content, or publishing it — the user does both.
- On-page optimization of a built page — [on-page-seo](on-page-seo.md).
- Finding who will link to it — [backlink-opportunity-hunter](backlink-opportunity-hunter.md).

## When to use it

- Before any new page, guide, tool, or article is commissioned — this skill is the gate.
- When [digital-pr-link-assets](digital-pr-link-assets.md) has produced more candidate assets than can be built at once.
- When [seo-opportunity-mining](seo-opportunity-mining.md) surfaces query gaps and someone is about to translate them straight into a content brief.
- On a recurring planning cycle, to re-sequence the backlog against what has changed.

## Required Data

- Candidate assets from [digital-pr-link-assets](digital-pr-link-assets.md).
- Query/keyword opportunities from [seo-opportunity-mining](seo-opportunity-mining.md) — which depend on GSC, and are `DATA NOT AVAILABLE` without it.
- `data/crawl/service-coverage-map.md` and existing content inventory — to catch duplication and cannibalization risk before, not after, building.
- SERP observations from [serp-intelligence](serp-intelligence.md) where available.
- Current authority picture from [off-page-seo](off-page-seo.md).

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- The existing site inventory and coverage map — reliable, already in `data/crawl/`.
- Direct SERP observation for a target query, if a search tool is verified live: what formats rank, what the intent appears to be, whether the results are dominated by government sites or established publishers.
- Competitor content observation via fetch.
- GSC query data, if GSC access is verified live — the only real source of search demand and current position for this site.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Search volume.** No keyword tool exists in this project. Never write a monthly-volume number. Where demand must be characterised, use a labelled, reasoned `ESTIMATE` band (e.g., "`ESTIMATE`: likely meaningful seasonal demand — basis: ITR filing is a statutory annual obligation with a fixed due date; no volume data available") and never a figure.
- **Keyword difficulty scores.** Not available. Assess difficulty by observing who actually ranks — government portals and large aggregators ranking a query is direct evidence of difficulty, and it is better evidence than a vendor's difficulty score.
- **Traffic or link projections** for an unbuilt page.
- **Ranking probability.** Not knowable; do not present a score as a forecast.

## Pre-Audit Checks

1. Confirm the candidate does not duplicate or cannibalize existing content — check the coverage map and [content-audit](content-audit.md)'s cannibalization findings first. If an existing page already targets the intent, the correct output is almost always *improve that page*, not build a new one.
2. Verify which data sources are actually live this session, and mark every score's inputs accordingly.
3. Confirm the firm can genuinely deliver the service or expertise the content implies — content that attracts enquiries the firm does not serve produces unqualified leads, which CLAUDE.md explicitly counts as a failure, not a win.
4. Load [eeat-ymyl-authority](eeat-ymyl-authority.md); every candidate here is YMYL and must be buildable to that standard.

## Step-by-Step Audit Process

### Step 1 — Frame the real question

For each candidate, the question is not "is there a keyword?" but **"can this simultaneously rank *and* earn references, and does it move a priority service?"** Content that can do only one of these still sometimes deserves to exist — but it should be built knowingly, in the right lane, not mistaken for a growth asset.

### Step 2 — Score SEO potential (0–30)

Six dimensions, 0–5 each. Record the evidence and confidence for every one.

| Dimension | Scored on |
|---|---|
| **Search demand** | Evidence that people search this — GSC impressions if available; otherwise the statutory/seasonal nature of the topic, labelled `ESTIMATE` |
| **Search intent** | How clearly the intent is served by a page this firm would build; commercial and "how do I comply" intent score higher than idle informational |
| **Ranking difficulty** | Inverted: who currently ranks. Government portals + national aggregators = low score. A gap where only thin content ranks = high score |
| **Existing authority** | Whether this site already has topical footing in the cluster — existing rankings, existing pages, existing links |
| **SERP opportunity** | Whether there is room: weak incumbents, missing formats, unclaimed features (PAA, snippet, local pack) |
| **Business relevance** | Proximity to a CLAUDE.md priority service and to an actual enquiry |

### Step 3 — Score linkability (0–40)

Eight dimensions, 0–5 each.

| Dimension | Scored on |
|---|---|
| **Original data** | Does it contain data nobody else has? |
| **Unique insight** | A genuine practitioner perspective, not a restatement of the statute |
| **Useful tool** | Is it *used* rather than read? |
| **Expert contribution** | Named CA authorship and credentials attached |
| **Research value** | Would someone cite it as evidence? |
| **Reference value** | Is it the kind of page people link to when they need to point at something? |
| **Newsworthiness** | Tied to a change, a deadline, a budget, a notification |
| **Citation potential** | Are there **named, real** prospects already discovered who would link to it? |

Citation potential is scored from the actual prospect list in `data/backlinks/`, not from imagination. Zero named prospects means a low score, and that is a legitimate result.

### Step 4 — Plot both scores and decide

Total: SEO /30, Linkability /40. Judge them **as a pair**, never summed — a combined total hides exactly the distinction the skill exists to make.

| Quadrant | Meaning | Decision |
|---|---|---|
| **High SEO + High Link** | Ranks and earns references | **BUILD FIRST.** The only true growth assets |
| **High SEO + Low Link** | Ranks, nobody cites it — most service and money pages | **BUILD**, but as a commercial page; do not resource it as PR, and plan to build its authority via internal links and separate assets |
| **Low SEO + High Link** | Few searches, but highly citable — many tools, calendars, data assets | **BUILD** as an authority asset; judge it on referring domains earned, never on its own traffic |
| **Low SEO + Low Link** | Neither | **DO NOT BUILD.** Say so plainly |

Mark thin-margin cases honestly. A candidate scoring mid-range on both is usually a *do not build yet*, and recommending restraint is a valid, valuable output.

### Step 5 — Check for the cheaper alternative

Before any BUILD is confirmed, ask whether an existing page could be improved to the same effect. Improving a page that already has some authority and history almost always beats a new URL, and it avoids adding cannibalization. Where the answer is yes, route to [content-decay-refresh](content-decay-refresh.md) or [content-audit](content-audit.md) and close the candidate.

### Step 6 — Sequence and specify

Order the BUILD set by: unblocking value (does an asset already have prospects waiting?), then priority-service proximity, then seasonality (a compliance calendar published after the deadline is worthless), then effort. For each, record the target URL, the primary intent, the internal-link plan into the relevant service silo, the schema type, the authorship requirement, and the maintenance trigger.

## What Checks to Perform

- [ ] Duplication/cannibalization checked against the existing inventory before scoring
- [ ] "Improve existing instead" explicitly considered and answered for every candidate
- [ ] SEO score recorded per dimension with evidence and confidence
- [ ] Linkability score recorded per dimension with evidence and confidence
- [ ] Citation potential scored from named, real, already-discovered prospects
- [ ] Scores kept as a pair, never summed into one number
- [ ] Quadrant decision recorded with a one-line rationale
- [ ] No search-volume figures or difficulty scores invented
- [ ] Every BUILD has a target URL, internal-link plan, schema, author, and maintenance trigger
- [ ] Seasonality checked against the compliance calendar
- [ ] DO NOT BUILD candidates recorded with reasons, so they are not re-proposed

## How to Identify Issues

Two findings recur and both matter. First: **a content backlog dominated by Low-Link candidates** — the firm can rank but will never accumulate authority, which is the structural reason a well-optimised CA site plateaus. Second: **a proposed page that duplicates existing coverage**, where building it would split relevance across two URLs and worsen the very rankings it was meant to improve. Both are worth writing up as findings in their own right, not just as a scoring output.

## Evidence to Collect

Save to `reports/` and `data/`:
- `content-plan-YYYY-MM-DD.md` — the scored matrix, quadrant decisions, and sequenced build order.
- `content-plan-scores.csv` — one row per candidate with all fourteen dimension scores, totals, quadrant, decision, and confidence.
- `do-not-build-log.md` — rejected candidates with reasons, so the same idea is not re-proposed each cycle.
- Per BUILD candidate: a brief with target URL, intent, sources, internal links, schema, author, maintenance trigger.
- The named-prospect list backing each Citation Potential score.

## How to Prioritize Issues

- **HIGH** — a High/High candidate that unblocks already-discovered link opportunities and serves a priority service.
- **HIGH** — a duplication/cannibalization risk in a candidate that was about to be built.
- **MEDIUM** — Low SEO + High Link authority assets with named prospects; seasonal assets approaching their window.
- **MEDIUM** — High SEO + Low Link commercial pages for priority services with genuine coverage gaps.
- **LOW** — candidates dependent on data the firm has not yet supplied.
- **OPPORTUNITY** — a cluster where the firm has authority footing and competitors are thin.
- **Not a finding** — Low/Low candidates; record and close.

## Implementation Recommendations

For the user to execute manually.

- **Each BUILD** gets a brief specifying: target URL and where it sits in the WordPress structure; Page vs. Post (evergreen tools and calendars as Pages, for stable citable URLs); Rank Math title, meta description and canonical; schema type to add via Rank Math; the internal links to add *from* the relevant parent service page and *to* the target service page ([internal-linking](internal-linking.md)); named CA author with credentials and a bio ([eeat-ymyl-authority](eeat-ymyl-authority.md)); every factual claim with its primary source; a visible last-updated date; and the maintenance trigger.
- **Where "improve existing" wins,** the deliverable is a change list against the existing URL, not a new brief.
- **Where a candidate is blocked** on firm-supplied data, state exactly what the firm must provide before it can proceed.
- Claude never drafts content into WordPress, never publishes, and never schedules — it produces the brief and the manual steps.

## How to Validate Fixes

- **Plan-level:** after a cycle, check that what was built matches what was prioritised, and that nothing was built from the DO NOT BUILD log.
- **Ranking outcome** for High-SEO candidates, via [gsc-analysis](gsc-analysis.md) if available — measured over months, and reported as correlation.
- **Link outcome** for High-Linkability candidates, via referring domains to that URL in `data/backlinks/`, each verified by fetching the linking page. Judge an authority asset on links earned, never on its own traffic.
- **Cannibalization check** after publication: confirm the new URL has not started competing with an existing page for the same query ([content-audit](content-audit.md)).
- **Scoring calibration:** revisit past predictions against actual outcomes and adjust how dimensions are scored. If High-Linkability predictions never earn links, the Citation Potential dimension is being scored optimistically.

## Expected Output Format

1. **Scoring matrix:**

   | Candidate | SEO /30 | Link /40 | Quadrant | Decision | Confidence | Rationale |
   |---|---|---|---|---|---|---|

2. **Sequenced build order** with the reason each item sits where it does, and seasonal deadlines called out.
3. **Improve-instead list** routed to the owning skill.
4. **DO NOT BUILD list** with reasons.
5. **Blocked list** — what the firm must supply.
6. Findings in the standard CLAUDE.md template, with Confidence Level and Evidence Source.

Open with a limitations note where relevant, e.g.:

> No keyword tool or GSC access was available this session (verified). All Search Demand scores are reasoned `ESTIMATE`s based on the statutory and seasonal nature of each topic, with the basis stated per candidate. No search-volume figures appear in this plan because none could be sourced.

## Common Mistakes to Avoid

- **Building because a keyword exists.** The rule this skill exists to enforce.
- **Writing search-volume numbers** with no tool behind them. A labelled `ESTIMATE` band with a stated basis is honest; "2,400/mo" is fabricated.
- **Summing the two scores.** A 25/5 and a 5/35 are completely different propositions and must never collapse into "30."
- **Scoring Citation Potential on imagination** rather than on named prospects already in `data/backlinks/`.
- **Skipping the cannibalization check** and building a page that competes with an existing one.
- **Skipping "improve existing"** — the cheaper option is frequently the better one, especially where the existing page already has history.
- **Treating a Low SEO + High Link asset as a failure** because its traffic is small. It is doing a different job; judge it on referring domains.
- **Ignoring seasonality** on compliance content, where a late publish has near-zero value.
- **Planning content for services the firm does not actually deliver**, which generates exactly the unqualified enquiries the project is trying to reduce.
- **Producing a large backlog and calling it a plan.** A prioritised five with clear reasoning beats a scored fifty.
