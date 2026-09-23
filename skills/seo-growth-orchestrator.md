# Skill: SEO Growth Orchestrator

## Purpose

Connect every SEO skill in this project into one system, so work is sequenced by impact rather than run as a set of isolated audits. This is the master skill: it decides what to do next, in what order, and how findings from one discipline should change the answer in another.

The question it exists to answer, continuously, is the specification's:

> **What is the highest-impact SEO action we can take next?**

and explicitly **not**:

> ~~What SEO task can we automate next?~~

## Scope

**This skill owns:** cross-skill sequencing, the daily/weekly/monthly cycle, cross-domain diagnosis (using one skill's findings to interpret another's), the consolidated priority queue, and the project's primary objective and guardrails at the strategic level.

**This skill does NOT own:** any individual audit. Every check belongs to a specialist skill; the orchestrator never re-derives a finding a specialist owns, and never duplicates their analysis.

## The primary business objective

The orchestrator optimises for one thing:

> **Increase qualified organic visibility and enquiries for the firm's highest-value services.**

It explicitly does **not** optimise for: maximum backlinks, maximum articles, maximum keywords, maximum indexed pages, or maximum domain metrics. Any recommendation that raises one of those without advancing the objective is noise, and the orchestrator's job includes saying so.

Priority commercial areas: Chartered Accountant services, Income Tax, ITR filing, GST, Accounting, Audit, Business registration, Startup services, NRI taxation, TDS, trademark/NGO-related services, and industry-specific taxation and compliance.

The site already has broad coverage across these areas. **The next stage is authority consolidation, not indiscriminate page creation** — a principle that should override most "we should write more content" impulses.

Every recommendation maps to a stage of CLAUDE.md's success journey:

```
Organic Visibility -> Qualified Traffic -> Engagement -> Form Submission / Contact -> Genuine Enquiry
```

A recommendation that cannot be placed on that journey does not belong in the queue.

## The system maximises and minimises

**Maximise:** Relevance × Authority × Trust × Search Visibility × Business Value

**Minimise:** Spam × Risk × Waste × Cannibalization × Unnecessary Content × Unnatural Link Acquisition

Both are multiplicative for a reason: a zero on any factor zeroes the result. Authority built on irrelevant links is worth nothing; visibility for services the firm does not deliver produces unqualified enquiries, which CLAUDE.md counts as a failure rather than a win.

## Implementation Policy at the orchestration level

The orchestrator sequences and prepares; **it never executes.** CLAUDE.md's Implementation Policy is permanent and non-negotiable, and no cycle, automation, or approval in this system overrides it. Where the source specification describes automated execution, this project's behaviour is: prepare completely, hand over with manual steps and validation, and stop. See [off-page-governance](off-page-governance.md), Rule 0.

## When to use it

- At the start of any working session, to decide what to work on.
- When multiple skills have produced findings and the priority order is unclear.
- On the daily, weekly and monthly cycles below.
- Whenever someone proposes an action that is not obviously the highest-impact next step.

## The daily cycle

The specification's pipeline, with this project's constraint applied at the execution stage:

```
Crawl / Health Check
   |
GSC Opportunity Mining
   |
Competitor Intelligence
   |
Content Opportunity Detection
   |
Backlink Opportunity Hunt
   |
Brand Mention Detection
   |
Authority Analysis
   |
Prioritization
   |
Preparation / Approval        <- (spec: "Execution"; here: prepare + hand over)
   |
Measurement
   |
Learning
```

| Stage | Owning skill | Runs without GSC/GA4? |
|---|---|---|
| Crawl / health check | [website-crawl](website-crawl.md), [technical-seo](technical-seo.md) | Yes |
| GSC opportunity mining | [seo-opportunity-mining](seo-opportunity-mining.md) | Mostly no |
| Competitor intelligence | [serp-intelligence](serp-intelligence.md), [competitor-analysis](competitor-analysis.md) | Yes |
| Content opportunity detection | [content-decay-refresh](content-decay-refresh.md), [linkable-content-planner](linkable-content-planner.md) | Accuracy strand yes |
| Backlink opportunity hunt | [backlink-opportunity-hunter](backlink-opportunity-hunter.md), [competitor-backlink-gap](competitor-backlink-gap.md), [broken-link-building](broken-link-building.md) | Yes |
| Brand mention detection | [entity-seo](entity-seo.md), [backlink-reclamation](backlink-reclamation.md) | Yes |
| Authority analysis | [off-page-seo](off-page-seo.md), [backlink-risk-monitor](backlink-risk-monitor.md) | Partially |
| Prioritization | This skill | Yes |
| Preparation / approval | [digital-pr-outreach](digital-pr-outreach.md), [off-page-governance](off-page-governance.md) | Yes |
| Measurement | [gsc-analysis](gsc-analysis.md), [ga4-analysis](ga4-analysis.md) | No |
| Learning | This skill | Yes |

**Declare at the top of every cycle which stages could actually run.** A cycle that reports on stages it could not perform is worse than a shorter honest one.

## Weekly and monthly

- **Weekly** — authority growth, competitor gap movement, content authority, and the top 10 actions for the coming week: `reports/weekly-authority-report.md`.
- **Monthly** — integrated GSC + GA4 + backlink + rankings + content + competitor view, ending in the strategic conclusion: `reports/monthly-seo-growth-report.md`.

## Cross-domain diagnosis — the actual point of the skill

The system must not treat SEO tasks as isolated activities. The orchestrator's distinctive job is reading findings *across* skills to produce a diagnosis no single skill could reach.

**The specification's worked example — a service page with strong rankings but weak authority:**

```
identify competitor backlinks        -> competitor-backlink-gap
identify relevant linkable resources -> backlink-opportunity-hunter, broken-link-building
determine whether the page itself is link-worthy -> digital-pr-link-assets, linkable-content-planner
improve the page if necessary        -> content-audit, eeat-ymyl-authority
conduct outreach                     -> digital-pr-outreach  (drafted; user sends)
acquire relevant links               -> user action only
measure ranking change               -> gsc-analysis, serp-intelligence
```

Note the third step. A single-skill approach jumps from "needs links" straight to outreach; the orchestrated approach asks whether the page deserves links first, because asking people to link to a page that does not merit it fails and burns the prospect.

**Other standing diagnostic patterns:**

| Observation | Cross-domain reading | Sequence |
|---|---|---|
| Page ranks 4–10, low CTR | Title/intent problem, not authority | [seo-opportunity-mining](seo-opportunity-mining.md) → [on-page-seo](on-page-seo.md) → measure |
| Priority page has no inbound links and is thin | Content problem masquerading as a link problem | [linkable-content-planner](linkable-content-planner.md) → build → then hunt |
| Traffic flat, enquiries falling | Conversion problem, not visibility | [cro-audit](cro-audit.md), [ga4-analysis](ga4-analysis.md) — **not** more content |
| Rankings fell, no technical cause | Check SERP composition and freshness before authority | [serp-intelligence](serp-intelligence.md) → [content-decay-refresh](content-decay-refresh.md) → [backlink-risk-monitor](backlink-risk-monitor.md) |
| Links found, NAP inconsistent | New citations will entrench the inconsistency | [local-citation-authority](local-citation-authority.md) **first** |
| Content accurate but uncited by AI | Structure/attribution, not volume | [ai-search-visibility](ai-search-visibility.md) |
| Link spike | Risk before celebration | [backlink-risk-monitor](backlink-risk-monitor.md) |
| Two pages competing | Consolidate before refreshing or building | [content-audit](content-audit.md) |

## Sequencing rules

Ordered blocking rules — earlier rules override later ones:

1. **Accuracy before everything.** A published tax figure that is wrong is a client-harm risk and outranks all SEO work ([eeat-ymyl-authority](eeat-ymyl-authority.md)).
2. **Fix what is broken before building more.** Indexing blocks, broken forms, links to 404s, and NAP contradictions waste every downstream effort.
3. **Resolve blocking owner decisions.** The open office-address conflict blocks citation and entity work; do not work around it.
4. **Deserve it before asking for it.** No outreach for a page that would not merit the link.
5. **Consolidate before creating.** The site has broad coverage; authority consolidation beats new pages.
6. **Qualified over more.** Visibility for services the firm does not deliver is a negative outcome.
7. **Cheap and certain before expensive and speculative.** A title rewrite that recovers a position 6 ranking beats a six-month link campaign.
8. **Never trade guardrails for speed.** [off-page-governance](off-page-governance.md)'s REJECT list is not negotiable under time pressure.

## Step-by-Step Process

1. **Verify capability.** Test what actually works this session ([reports/00-capability-check.md](../reports/00-capability-check.md) as the record). Never assume; never carry forward.
2. **Check blocking items.** Open accuracy findings, open owner decisions, unresolved CRITICALs.
3. **Run the runnable stages**, delegating each to its owning skill.
4. **Read across findings**, applying the diagnostic patterns above.
5. **Build one consolidated queue** — all skills' findings in a single priority order, deduplicated, each mapped to a success-journey stage.
6. **Prepare the top items** to hand-over standard: manual steps plus validation.
7. **Measure** what previous cycles' completed items actually did.
8. **Learn** — record which predictions held and adjust future prioritisation.

## What Checks to Perform

- [ ] Capability verified this session, not assumed
- [ ] Runnable vs. unavailable stages declared
- [ ] Blocking items checked before new work is started
- [ ] Each stage delegated to its owning skill, not re-derived
- [ ] Cross-domain diagnosis applied before recommending action
- [ ] One consolidated, deduplicated priority queue produced
- [ ] Every item mapped to a success-journey stage
- [ ] Sequencing rules applied in order
- [ ] Top items prepared to hand-over standard
- [ ] Prior cycle outcomes measured and calibration recorded
- [ ] Nothing executed by Claude

## How to Identify Issues

The orchestrator's findings are about the *programme*, not the site: work being done in the wrong order; effort going to a symptom rather than a cause; a queue optimising volume metrics rather than qualified enquiries; a blocking item being worked around; or specialist findings that contradict each other and need reconciliation. The highest-value orchestrator finding is usually the one that stops work: *this is not the highest-impact next action, and here is what is.*

## Evidence to Collect

Save to `reports/`:
- `orchestrator-cycle-YYYY-MM-DD.md` — stages run, stages unavailable, findings ingested, diagnoses, queue produced.
- `priority-queue.md` — the live consolidated queue, one entry per action with owning skill, priority, journey stage, status.
- `learning-log.md` — predictions made, outcomes observed, calibration adjustments. This is what makes the system improve rather than merely repeat.
- Cross-references to each specialist skill's own evidence files, rather than copies.

## How to Prioritize Issues

The consolidated queue uses CLAUDE.md's severities, ordered by the sequencing rules and broken by proximity to a qualified enquiry:

- **CRITICAL** — published inaccuracy; indexing blocks on money pages; broken conversion paths; confirmed manual action.
- **HIGH** — blocking owner decisions; NAP contradictions; near-miss rankings on priority services; priority service pages with no authority and no link-worthiness.
- **MEDIUM** — content depth and freshness; internal linking; citation and entity consistency; qualified link opportunities.
- **LOW** — polish.
- **OPPORTUNITY** — linkable assets, unclaimed ecosystem placements, AI-answer surfaces.

When two items tie, prefer the one closer to an enquiry and the one with the lower effort.

## Implementation Recommendations

The orchestrator produces the **hand-over package**: a ranked list, each item with its owning skill's manual implementation guide and validation procedure, sequenced so the user can work top-down without hitting dependencies. Dependencies are stated explicitly ("do not submit directory listings until the address is confirmed"). Nothing in the package is performed by Claude.

## How to Validate Fixes

- **Per item:** the owning skill's validation procedure.
- **Per cycle:** were the prepared items actually actionable? An item the user could not execute from the guide is a defect in the guide.
- **Programme level:** monthly, against the primary objective — qualified organic visibility and enquiries for priority services. Rising links with flat enquiries means the queue is optimising the wrong thing.
- **Calibration:** compare predicted impact against observed outcomes in `learning-log.md`.
- Report correlation, not causation, and state what else changed in the period.

## Expected Output Format

1. **Cycle header** — date, capability verified, stages run and unavailable.
2. **Blocking items** — what must be resolved before other work proceeds.
3. **Cross-domain diagnoses** — the readings that span skills.
4. **Consolidated priority queue:**

   | # | Action | Owning skill | Severity | Journey stage | Effort | Status |
   |---|---|---|---|---|---|---|

5. **Prepared hand-over package** for the top items.
6. **Measurement** of prior-cycle items.
7. **Learning notes** and calibration.
8. **Explicit "what we are not doing, and why"** — the restraint list. This is a first-class output, not a footnote: declining to build unnecessary content or chase unwinnable SERPs is often the highest-value decision in the cycle.

## Common Mistakes to Avoid

- **Optimising for automation instead of impact.** The distinction the specification calls critical, and the failure this skill exists to prevent.
- **Running every skill every cycle** regardless of whether it can produce anything. Capability first.
- **Re-deriving a specialist's finding** instead of delegating to and citing them.
- **Producing parallel queues per skill** with no single order, leaving the user to arbitrate.
- **Skipping "does the page deserve links?"** and jumping to outreach.
- **Working around a blocking owner decision** rather than escalating it.
- **Reporting volume metrics as progress.** More links, more pages, more keywords are not the objective.
- **Chasing rankings for services the firm does not deliver.**
- **Treating a link spike as success** without a risk check.
- **Dropping the restraint list**, which is where much of the value sits.
- **Letting a cycle report on stages that could not run.**
- **Executing.** The orchestrator prepares and sequences; the user implements everything.
