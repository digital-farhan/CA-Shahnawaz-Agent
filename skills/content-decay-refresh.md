# Skill: Content Decay & Refresh Engine

## Purpose

Continuously identify pages that are losing ground or have gone out of date, and prioritise refreshes by the value they would recover. For a CA firm this matters more than for most businesses: tax and compliance information has a built-in expiry date, and the site already publishes monthly compliance calendars and current tax guides that become wrong — not merely stale — the moment a due date, rate or rule changes.

Refreshing an existing page that already has history and links is usually a far better investment than publishing a new one, which makes this one of the highest-return skills in the set.

## Scope

**This skill owns:** decay detection (performance-based and accuracy-based), refresh prioritisation, and the refresh specification.

**This skill does NOT own:**
- Deciding what *new* content to build — [linkable-content-planner](linkable-content-planner.md).
- The accuracy standard a refresh must meet — [eeat-ymyl-authority](eeat-ymyl-authority.md), which owns verification against primary sources; this skill triggers and prioritises, that skill sets the bar.
- Baseline content quality, depth and cannibalization diagnosis — [content-audit](content-audit.md); this skill consumes its cannibalization findings rather than re-deriving them.
- Query-level opportunity discovery — [seo-opportunity-mining](seo-opportunity-mining.md), which shares GSC inputs but looks forward at opportunities rather than backward at decline.
- Backlink loss as a profile issue — [off-page-seo](off-page-seo.md) / [backlink-reclamation](backlink-reclamation.md).
- Internal link structure — [internal-linking](internal-linking.md).
- Editing or republishing anything — the user does that.

## When to use it

- On a recurring cycle — decay is gradual and invisible without deliberate checking.
- **Immediately after any regulatory trigger**: Union Budget, Finance Act, GST Council decision, CBDT/CBIC notification, MCA amendment, due-date extension. This is the highest-urgency entry point, because a single notification can make many pages wrong at once.
- At the start of each compliance season, before the traffic arrives.
- When [gsc-analysis](gsc-analysis.md) shows declining clicks or positions.

## Required Data

- **GSC performance data** for ranking, click and impression trends — the primary decay signal, and `DATA NOT AVAILABLE` without GSC access.
- GA4 engagement data, if available.
- The live content, for accuracy and freshness inspection.
- `data/crawl/` inventory, including the existing freshness notes in `data/crawl/_phase1b-cannibalization-and-freshness.md`.
- Primary sources, to determine whether content is outdated.
- Backlink data per page, if any exists.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- **Accuracy-based decay detection, which works entirely without GSC.** Fetch a page, identify its dated claims (rates, thresholds, due dates, AY/FY references, rule citations), and check them against primary sources. This is the more important half of the skill in a tax context and it is fully available.
- Visible freshness signals: publication and updated dates, stated assessment year, references to superseded rules or portals, outdated screenshots, dead outbound links.
- Internal links pointing at retired or redirected URLs.
- GSC click, impression and position trends — **only if** GSC access is verified live this session.
- GA4 engagement trends — only if verified live.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Performance-based decay without GSC.** Per `reports/00-capability-check.md`, no GSC connector was available at the last verified check. Without it: lost rankings, lost clicks, lost impressions, declining traffic, and traffic-based prioritisation are all `DATA NOT AVAILABLE`. Do not infer that a page "has probably lost traffic" from its age or its content — that is an invented metric.
- Declining backlinks per page, absent a backlink tool or prior snapshots.
- Competitor performance changes.
- Recovery probability as a computed value — it is a reasoned judgement, labelled as such, never a number presented as a calculation.
- Why a page declined, where multiple causes are plausible. State the candidates and the evidence; do not assert a single cause without support.

## Pre-Audit Checks

1. Verify GSC/GA4 availability and **declare the detection mode**: performance-based (GSC live), accuracy-based (no GSC), or both. This determines what the skill can honestly claim.
2. Check for regulatory triggers since the last cycle — these drive the urgent queue regardless of performance data.
3. Load prior freshness findings so work extends rather than repeats.
4. Load [eeat-ymyl-authority](eeat-ymyl-authority.md)'s accuracy register — pages already flagged there are automatic refresh candidates.

## Step-by-Step Audit Process

### Step 1 — Detect accuracy decay (always available, always first)

For each substantive page, identify time-bound content and verify it against primary sources:

- **Outdated tax information** — rates, thresholds, slabs, exemption limits, sections superseded by amendment.
- **Outdated deadlines** — due dates that have passed, been extended, or changed. Compliance calendars decay fastest and hardest here.
- **Outdated laws** — rules amended or replaced; references to repealed provisions.
- **Outdated screenshots** — portal interfaces change often; a procedural guide with stale screenshots actively misleads a reader trying to follow it.
- **Missing or wrong assessment year** — content correct for a prior AY presented as current.
- **Dead or superseded outbound links** — references to retired portal URLs or withdrawn circulars.
- **Outdated internal links** — links to pages since retired, merged, or redirected.

Anything wrong routes to [eeat-ymyl-authority](eeat-ymyl-authority.md) as an accuracy finding and is treated as urgent, independent of any performance signal.

### Step 2 — Detect performance decay (GSC-dependent)

Where GSC is live, compare a recent window against the equivalent earlier window and identify pages that lost rankings, clicks or impressions. Distinguish carefully:

- **Genuine decay** — sustained decline against a comparable baseline.
- **Seasonality** — an ITR guide falling after the filing deadline is behaving correctly, not decaying. Compare year-on-year for seasonal content; comparing July to October in tax content produces false alarms and wasted refreshes.
- **Query-mix change** — impressions moving to a different query rather than disappearing.
- **SERP change** — an AI Overview or new feature reducing clicks while impressions and position hold ([serp-intelligence](serp-intelligence.md), [ai-search-visibility](ai-search-visibility.md)).
- **Cannibalization** — two pages competing, from [content-audit](content-audit.md).

### Step 3 — Detect structural decay

- Pages whose internal links have degraded, leaving them orphaned or weakly linked ([internal-linking](internal-linking.md)).
- Pages that have lost backlinks, where snapshots allow the comparison.
- Pages superseded by newer content on the same topic — a consolidation candidate rather than a refresh candidate.

### Step 4 — Diagnose before prescribing

For each decayed page, establish *why* before recommending a fix. The correct action differs completely:

| Cause | Action |
|---|---|
| Content is factually outdated | Update facts, re-verify, update the date honestly |
| Content is thin versus current SERP | Deepen ([content-audit](content-audit.md)) |
| Cannibalized | Consolidate or differentiate — refreshing both pages makes it worse |
| Seasonal | No action; note the cycle |
| SERP feature absorbing clicks | Route to [ai-search-visibility](ai-search-visibility.md) / [serp-intelligence](serp-intelligence.md) |
| Lost links | [backlink-reclamation](backlink-reclamation.md) |
| Orphaned | [internal-linking](internal-linking.md) |
| Genuinely obsolete topic | Retire and redirect, rather than refresh |

### Step 5 — Prioritise

Rank by the specification's formula, stated as a reasoned judgement rather than a computed score:

```
Traffic potential  x  business value  x  recovery probability
```

- **Traffic potential** — GSC impressions where available; otherwise the page's commercial role, labelled `ESTIMATE` with its basis.
- **Business value** — proximity to a priority service and to an enquiry. A decayed GST registration page outranks a decayed general blog post regardless of traffic.
- **Recovery probability** — higher where the cause is clear and fixable (outdated facts, thin content), lower where it is structural (a dominant government portal now occupying the SERP).

Where GSC is unavailable, prioritise by **accuracy risk × business value** instead, and say so. A wrong deadline on a priority page is the top of the queue regardless of whether traffic can be measured.

### Step 6 — Specify the refresh

For each, specify exactly: what is wrong (quoted verbatim), the corrected content with primary sources and effective dates, whether the URL stays (it almost always should — a new URL discards the page's history and links), whether the date should be updated, internal links to add or fix, and the next review trigger.

### Step 7 — Hand over

Claude never edits or republishes. Supply the change list and the manual steps.

## What Checks to Perform

- [ ] Detection mode declared (performance / accuracy / both)
- [ ] Regulatory triggers since last cycle identified
- [ ] Every dated claim on in-scope pages verified against primary sources
- [ ] Compliance calendars and deadline content checked first
- [ ] Assessment year / financial year stated and correct
- [ ] Screenshots and procedural steps checked against current portal interfaces
- [ ] Outbound and internal links tested
- [ ] Seasonality distinguished from decay via year-on-year comparison
- [ ] Cannibalization excluded before recommending a refresh
- [ ] Cause diagnosed per page before a fix is prescribed
- [ ] Prioritised by the stated formula, with the basis for each factor
- [ ] URL retention decided deliberately
- [ ] Next review trigger recorded per page
- [ ] No traffic or ranking decline asserted without GSC data

## How to Identify Issues

Two distinct findings. **Accuracy decay:** the page publishes something that is now wrong — evidenced by the quoted claim plus the current primary-source position. This is urgent regardless of traffic, because it carries client risk. **Performance decay:** the page has lost measurable ground, evidenced by GSC figures across comparable windows, with seasonality and cannibalization excluded. In this project the first is fully available and the second usually is not, so an honest decay audit here leads with accuracy and states the performance limitation plainly.

## Evidence to Collect

Save to `data/crawl/` and `reports/`:
- `content-decay-YYYY-MM-DD.md` — full audit with mode, per-page diagnosis and priority.
- `decay-register.csv` — URL, decay type, evidence, cause, action, priority, next review trigger, status.
- `refresh-specs/<page-slug>.md` — per-page refresh specification.
- `review-triggers.md` — which pages need re-checking on which regulatory events. This is the artefact that turns decay management into a maintainable process rather than a periodic scramble.
- Quote outdated content verbatim alongside the current primary-source position.

## How to Prioritize Issues

- **CRITICAL** — a live page publishing a wrong rate, threshold, deadline or rule, especially on a priority service page or a compliance calendar. Client-harm risk; fix ahead of everything else.
- **HIGH** — content correct but for a superseded assessment year with no AY stated; procedural guides with obsolete screenshots on high-intent pages; measured sustained decline on a priority commercial page with a clear, fixable cause.
- **MEDIUM** — dead outbound references; outdated internal links; thin-versus-SERP content on secondary pages; moderate measured decline.
- **LOW** — cosmetic staleness; old examples that remain broadly accurate.
- **Not a refresh** — seasonal troughs; cannibalization (consolidate instead); obsolete topics (retire and redirect instead).

## Implementation Recommendations

Manual, for the user.

- **Keep the URL.** Refresh in place: editing the existing page preserves its history, links and any accumulated authority. Recommend a new URL only when the topic genuinely changed. Where content is AY-specific and the firm wants both years available, recommend a deliberate URL and canonical strategy rather than silently duplicating.
- **WordPress steps:** edit the existing page or post; update the body content; update Rank Math's title and description if the focus changed; update the visible last-updated date **only because the content actually changed**; re-check internal links; clear any cache so the change is live; and re-submit the URL in GSC's URL Inspection tool if GSC is available.
- **Compliance calendars** need a standing update process, not ad-hoc fixes. Recommend a fixed monthly review with a named owner and a checklist of source pages, since these decay on a predictable schedule.
- **Screenshots:** recommend recapturing from the current portal, with the capture date noted.
- **Retirement:** where a topic is genuinely obsolete, recommend a 301 to the closest relevant live page — never a homepage catch-all — and check first whether the page has inbound links ([off-page-seo](off-page-seo.md)) that make restoration the better option.
- **Never** update a "last updated" date without a substantive content change; that is a trust problem, not an optimisation.
- **Never** publish a corrected figure that has not been verified against its primary source this session.

## How to Validate Fixes

- **Accuracy:** re-fetch and confirm the corrected content matches the primary source; record the re-verification date in the accuracy register.
- **Structural:** confirm links resolve, screenshots are current, AY is stated, and the date reflects a real change.
- **Performance:** compare the same window year-on-year after the refresh, via GSC if available. Allow weeks, not days, and report as correlation.
- **Process:** confirm the next review trigger is recorded, so the same page does not silently decay again.
- **Never** claim recovery from a short post-refresh window, particularly on seasonal content where the natural cycle will dominate any refresh effect.

## Expected Output Format

1. **Mode and limits header**, e.g.:

   > **Accuracy-based detection only.** No GSC access this session (verified), so lost rankings, clicks and impressions are `DATA NOT AVAILABLE` and no traffic-based prioritisation is possible. The pages below were assessed by verifying their dated claims against primary sources, and prioritised by accuracy risk x business value.

2. **Decay register table:**

   | URL | Decay type | Evidence | Cause | Action | Priority | Next trigger |
   |---|---|---|---|---|---|---|

3. **Urgent accuracy corrections** — quoted claim, current position, source, effective date.
4. **Refresh specifications** for the prioritised set.
5. **Retire/consolidate list**, with routing.
6. **Review-trigger schedule.**
7. Findings in the standard CLAUDE.md template with Confidence Level and Evidence Source.

## Common Mistakes to Avoid

- **Claiming traffic or ranking decline without GSC data.** Age is not evidence of decay.
- **Mistaking seasonality for decay** and refreshing an ITR guide every autumn because filing-season traffic ended.
- **Refreshing both halves of a cannibalized pair**, which entrenches the competition instead of resolving it.
- **Changing the URL on refresh**, discarding the page's history and links.
- **Bumping the updated date without changing the content.**
- **Correcting a figure from memory** rather than from the primary source — the most consequential error available here.
- **Refreshing by adding words.** Decay is usually about accuracy and intent match, not length.
- **Ignoring compliance calendars** because they look like minor pages. They decay fastest, they carry deadline risk, and clients rely on them.
- **Refreshing a page that should be retired**, or retiring one that has inbound links and should be restored.
- **Treating decay work as one-off.** Without recorded review triggers the same pages decay again unnoticed.
- **Editing the site.** Claude specifies; the user publishes.
