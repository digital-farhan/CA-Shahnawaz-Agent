# Skill: Competitor Backlink Gap Analysis

## Purpose

Establish which domains link to the named competitor CA firms but not to cashahnawaz.com, determine which of those links are realistically obtainable, and score them — so link-building effort is aimed at gaps that are demonstrably winnable in this specific market rather than at a generic wish list.

The value of this skill is not "competitors have more links." It is the far more useful, evidence-backed statement: *here are the specific Mumbai associations, professional bodies, directories and publications that link to three of four competitors, that this firm genuinely qualifies for, and that it is currently absent from.*

## Scope

**This skill owns:** competitor referring-domain discovery, the gap set (links they have that this firm does not), obtainability assessment, and scoring of each gap opportunity.

**This skill does NOT own:**
- Non-competitor-derived opportunities — [backlink-opportunity-hunter](backlink-opportunity-hunter.md).
- Competitor content, service coverage, on-page patterns, or positioning — [competitor-analysis](competitor-analysis.md), which owns competitor comparison generally. This skill is strictly the link dimension and inherits that skill's competitor-verification requirement.
- Why a competitor outranks the firm on a given SERP — [serp-intelligence](serp-intelligence.md).
- This site's own backlink profile — [off-page-seo](off-page-seo.md).
- Outreach drafting — [digital-pr-outreach](digital-pr-outreach.md).
- Scoring rules — [off-page-governance](off-page-governance.md).

## When to use it

- After [off-page-seo](off-page-seo.md) has established this site's baseline, so a "gap" is measurable.
- When a competitor consistently outranks the firm on a priority commercial term despite comparable on-page and content quality.
- On the recurring cycle in `automations/daily-backlink-hunt.md`, at a lower frequency than general hunting (competitor profiles change slowly).

## Required Data

- The four competitor URLs from CLAUDE.md, **each re-verified live this session** per [competitor-analysis](competitor-analysis.md)'s verification requirement:
  - https://ndsavla.com/
  - https://www.jvb.co.in/
  - https://www.asitmehtaassociates.com/
  - https://jainanuragassociates.com/
- A backlink data source, if one exists. **This is the binding constraint** — see below.
- `data/backlinks/backlink-master.csv` — this site's known links, to compute the gap.
- `data/competitors/verification-log.md` — competitor validity status.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- **A third-party backlink tool**, if genuinely connected this session — the only source of a competitor's actual referring-domain list.
- **Observation-based gap discovery, which works without any backlink tool.** This is the practical mode for this project, and it is legitimate evidence when done properly:
  - Search for each competitor's brand name and domain to surface pages that mention or link to them.
  - Fetch candidate ecosystem pages directly (association member lists, chamber directories, ICAI-related listings, Mumbai business directories, professional directories, local publications) and read which firms are listed and which are linked.
  - Fetch the competitor site itself for declared affiliations, memberships, awards, press pages, and "as featured in" sections — firms advertise their own ecosystem placements, and each one names a page that can then be checked for whether this firm is also listed.
- Direct verification that cashahnawaz.com is absent from each such page.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Any competitor's total backlinks, referring domains, referring IPs, DA/DR, or traffic.** Per `reports/00-capability-check.md`, no backlink tool was available at the last verified check, and CLAUDE.md's competitor rules prohibit inferring these. This must be stated as `DATA NOT AVAILABLE`, not estimated from how established a competitor looks.
- A complete competitor referring-domain list without a tool. Observation-based discovery produces a **partial, directional sample**; it must always be labelled as such. "We found 11 ecosystem pages linking to competitors" is never "competitors have 11 referring domains."
- Which competitor links were paid, exchanged, or otherwise acquired — unknowable from outside, and irrelevant, since the firm will not pursue those routes anyway.
- Whether a competitor's link actually helps them rank — no tool isolates that.

## Pre-Audit Checks

1. **Re-verify every competitor URL this session** — live, and still a CA/tax/compliance firm — using [competitor-analysis](competitor-analysis.md)'s Business Model Verification Checklist. A dead, parked, pivoted, or redirected competitor is excluded and stated, never silently analysed.
2. Verify backlink-tool availability and **declare the mode**: Mode A (tool-backed, full referring-domain comparison) or Mode B (observation-based, partial ecosystem sample). Everything downstream is caveated by this.
3. Load this site's known-link set and the rejection log for deduplication.
4. Load [off-page-governance](off-page-governance.md).

## Step-by-Step Audit Process

Run steps 1–5 per the source specification: discover referring domains → identify what competitors have that this firm does not → categorize each opportunity → determine obtainability → score.

### Step 1 — Discover competitor referring domains

**Mode A:** export each verified competitor's referring domains, then intersect and union them. Domains linking to **multiple** competitors are the highest-signal targets: they indicate an ecosystem placement that CA firms in this market routinely hold, rather than a one-off.

**Mode B:** build the ecosystem map by hand:
- Fetch each competitor's site and record every declared affiliation, membership, association, award, press mention, directory badge, and "featured in" claim.
- Search each competitor's brand name and bare domain to surface third-party pages naming them.
- Fetch the resulting association/directory/publication pages and record which competitors appear and whether they are linked or only named.

Record each discovered page as a candidate with the specific URL that proves it.

### Step 2 — Compute the gap

For every discovered domain/page, check whether cashahnawaz.com is present. Verify by fetching the page and searching it — never assume absence. Classify:

| Class | Meaning |
|---|---|
| **Gap** | Links to ≥1 competitor, no link to this firm |
| **Shared** | Links to both — no action, but useful context |
| **Exclusive** | Links to this firm only — a strength worth protecting; note in [off-page-seo](off-page-seo.md) |
| **Mention-only gap** | Names competitors, links none — low value, deprioritize |

Prioritize gaps held by **multiple** competitors.

### Step 3 — Categorize each gap

Assign one category, because category predicts obtainability better than any metric:

- **Eligibility-based** — professional body, ICAI-related listing, association membership, chamber directory. Obtainable by *qualifying*, not by persuading. Highest priority.
- **Directory / listing** — business or professional directory with an open, legitimate listing process.
- **Editorial / publication** — a publication that wrote about or quoted a competitor.
- **Resource / curated list** — a page curating useful tax/business resources.
- **Client, partner or vendor** — a competitor's client or partner linking to them. Frequently *not* obtainable, and never worth manufacturing.
- **Event / speaking / webinar** — conference, panel, or webinar page.
- **Local / community** — Mumbai-specific community, news, or civic page.
- **Not pursuable** — anything failing the [off-page-governance](off-page-governance.md) REJECT list (paid networks, link farms, spam directories). Competitors having a spam link is not a reason to acquire one; log it and move on.

### Step 4 — Determine obtainability honestly

This is the step that makes the skill useful rather than aspirational. For each gap, answer from evidence:

1. **Is there a published route in?** A membership application, a listing submission, a contributor policy, a call for speakers.
2. **Does the firm actually qualify?** Membership criteria, locality, practice area, firm size, credentials. A qualified CA in Mumbai genuinely qualifies for a great many of these — that is the core insight of this skill.
3. **Why did the competitor get it?** If the answer is a personal relationship, a client engagement, a decade-old placement, a paid arrangement, or a merger legacy, obtainability is low and the honest output says so.
4. **Would inclusion be legitimate and useful to that site's audience?** If not, it is not an opportunity.
5. **Is the link editorial and in-content, or a footer/badge dump?** Placement quality affects the score.

Grade obtainability: `OBTAINABLE` (clear route + qualifies) / `PLAUSIBLE` (route exists, qualification or interest uncertain) / `UNLIKELY` (no route or dependent on a relationship) / `NOT PURSUABLE` (fails governance).

**Do not chase every competitor backlink.** A gap that is `UNLIKELY` or `NOT PURSUABLE` is documented and dropped, not converted into an outreach task.

### Step 5 — Score

Apply the 100-point rubric in [off-page-governance](off-page-governance.md), with `PROXY-SCORED` flags on Authority and Traffic in Mode B, and an overall confidence level. Competitor presence contributes to Editorial Likelihood — a site that has demonstrably linked to a comparable firm has proven it links to firms like this one.

Write results to `data/backlinks/backlink-master.csv` with `competitor_link = yes` and the competitor(s) named in `notes`.

## What Checks to Perform

- [ ] All four competitors re-verified live this session (or excluded, with reason stated)
- [ ] Mode (A tool-backed / B observation-based) declared in the output
- [ ] Every candidate page fetched and read — presence/absence of this firm verified, not assumed
- [ ] Gap set classified: gap / shared / exclusive / mention-only
- [ ] Multi-competitor gaps identified and prioritized
- [ ] Each gap categorized by type
- [ ] Obtainability graded with the reasoning recorded
- [ ] REJECT-list gaps logged and dropped, not pursued
- [ ] Every pursued gap scored with confidence and proxy flags
- [ ] Deduplicated against the CRM and the rejection log
- [ ] No competitor backlink totals, DA/DR, or traffic figures asserted anywhere

## How to Identify Issues

A genuine gap finding requires all of: at least one verified competitor is linked from the page; cashahnawaz.com is verifiably absent; the page is relevant and legitimate; and there is a published route in that the firm plausibly qualifies for. The strongest form of this finding — and the one to lead with — is a page where **most or all verified competitors** appear and this firm does not, in a category the firm qualifies for by right. Consistency across competitors is a far stronger signal than a single competitor's outlier link, exactly as in [competitor-analysis](competitor-analysis.md).

## Evidence to Collect

Save to `data/backlinks/`:
- `competitor-gap-YYYY-MM-DD.md` — the full analysis with mode, method, and per-gap reasoning.
- `competitor-gap-matrix.csv` — one row per discovered domain, columns for each competitor plus cashahnawaz.com (linked / mentioned / absent), category, obtainability, score.
- Updated `backlink-master.csv` rows for pursued gaps.
- Update `data/competitors/verification-log.md` with this session's re-verification.
- For every gap: the exact URL evidencing the competitor link, and a quoted line showing the competitor listed and this firm absent.

## How to Prioritize Issues

- **HIGH** — an eligibility-based placement (professional body, association, chamber, credible Mumbai business directory) held by multiple verified competitors, which the firm qualifies for and is absent from. This is a concrete, defensible, winnable authority gap.
- **MEDIUM** — a single competitor holds a relevant, obtainable placement with a published route in; or an editorial publication that has covered competitors and accepts contributions.
- **LOW** — mention-only pages; low-relevance directories; gaps graded `PLAUSIBLE` with weak audience overlap.
- **OPPORTUNITY** — categories where all competitors are equally absent (an unclaimed ecosystem the firm could lead).
- **Not a finding** — `UNLIKELY` (relationship-derived) and `NOT PURSUABLE` (governance REJECT) gaps. Document them so they are not rediscovered, then drop them.

Weight upward when the gap could point at a priority service page with no current inbound links.

## Implementation Recommendations

Prepared for manual execution by the user; Claude never submits, applies, joins, or contacts.

- **Eligibility-based placements:** supply the organisation, the page the firm should appear on, the published membership/listing route, the stated eligibility criteria, the fee if published, and the exact NAP-consistent field values to submit (values taken from [local-citation-authority](local-citation-authority.md)'s canonical record). Where a listing already exists but is incomplete, record the current values first so the user can revert.
- **Directory listings:** same, plus the [off-page-governance](off-page-governance.md) legitimacy assessment so the user can see why this directory is worth a listing when most are not.
- **Editorial gaps:** identify the specific journalist/editor/publication and the specific article that covered a competitor, then route to [digital-pr-outreach](digital-pr-outreach.md) for a personalised draft — which the user sends.
- **Gaps blocked on content:** if the firm would need a genuinely better resource to warrant inclusion, route to [linkable-content-planner](linkable-content-planner.md) instead of drafting an ask.

## How to Validate Fixes

- **Placement confirmed:** fetch the target page and verify the firm now appears, with the anchor, `rel`, and placement recorded. Update `backlink-master.csv` (`status = live`, `first_seen` dated).
- **Gap closure over time:** re-run the gap matrix on the next cycle and compare — the meaningful metric is *gaps closed in categories that matter*, never total links gained.
- **NAP consistency:** every new listing is re-checked by [local-citation-authority](local-citation-authority.md); a new link that introduces a conflicting address or phone is a net negative for local authority.
- **Ranking effect:** via [serp-intelligence](serp-intelligence.md) and [gsc-analysis](gsc-analysis.md) if available, over months, and stated as correlation.

## Expected Output Format

1. **Header** — mode, competitors verified/excluded, method, and an explicit limitations statement, e.g.:

   > **Mode B — observation-based.** No backlink tool was available this session (verified). Competitor referring-domain totals are `DATA NOT AVAILABLE`. The gaps below are a partial ecosystem sample built by fetching N pages directly; they are directional evidence of specific winnable placements, not a measurement of competitor link volume.

2. **Gap matrix:**

   | Domain / page | ND Savla | JVB | Asit Mehta | Jain Anurag | Cashahnawaz | Category | Obtainable? | Score | Band |
   |---|---|---|---|---|---|---|---|---|---|

3. **Top winnable gaps** — the eligibility-based, multi-competitor ones, each with its route in.
4. **Documented-and-dropped list** — `UNLIKELY` / `NOT PURSUABLE`, with reasons, so they are not rediscovered.
5. **Findings** in the standard CLAUDE.md template with Confidence Level and Evidence Source.
6. **Routing list** — which gaps went to which skill.

## Common Mistakes to Avoid

- **Reporting competitor backlink counts or DA/DR.** No tool, no number. This is a direct CLAUDE.md rule-2 violation and the easiest one to commit in this skill.
- **Presenting an observation-built sample as a competitor's link profile.**
- **Assuming absence without fetching the page.** "They're probably not listed" is not evidence.
- **Chasing every gap.** The specification is explicit: do not chase every competitor backlink. Most gaps are noise; the eligibility-based ones are the prize.
- **Copying a competitor's spam links** because they appear to be "working." Governance forbids it, and the assumption that the spam is what is working is unfounded.
- **Ignoring why the competitor has the link.** A link earned through a fifteen-year client relationship is not an opportunity, and listing it as one wastes the user's time.
- **Skipping competitor re-verification** and building a gap analysis on a firm that has since merged, pivoted, or gone offline.
- **Treating a shared link as a gap** — check whether the firm is already listed before writing it up as missing.
- **Forgetting the target page.** A gap link that would point at the homepage when the ITR filing page has no inbound links at all is a weaker win; state the intended target for every pursued gap.
