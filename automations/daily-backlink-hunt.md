# Automation: Daily Backlink Opportunity Hunt

## What this is

The recurring discovery and qualification cycle that feeds the backlink CRM. It runs the fifteen-step process from the source specification, under this project's guardrails.

**Frequency:** once per day, or at whatever cadence the user actually runs sessions. A cycle that runs when there is nothing new to find should report "no qualified opportunities this cycle" rather than manufacture output.

## What "automation" means in this project

**It means automated discovery, qualification, scoring and preparation — never automated action.**

CLAUDE.md's Implementation Policy is permanent and non-negotiable: Claude Code never submits, publishes, contacts, claims, registers, edits or configures anything on any live system. The source specification's "Automatically allowed" list (updating owned profiles, submitting to directories, requesting link corrections) is treated here as **prepare, package and hand over**. See [off-page-governance](../skills/off-page-governance.md) Rule 0.

So this cycle ends at a reviewed queue plus a hand-over package. Step 15 reports; a human acts.

There is also no scheduler in this project. This file is a **runbook** the user or Claude follows in a session — not a job that fires on its own. Do not describe it as running unattended.

## Prerequisites

Verify at the start of every cycle, by attempting the call:

| Requirement | If unavailable |
|---|---|
| Web search | Discovery strands cannot run — say so and stop, rather than guessing prospects |
| Web fetch | Qualification cannot run — no candidate may be scored from a search snippet alone |
| `data/backlinks/backlink-master.csv` | Create from the header in `data/backlinks/README.md` |
| `data/backlinks/rejected-opportunities.md` | Create empty; without it, duplicate protection fails |

Also load [off-page-governance](../skills/off-page-governance.md) — the REJECT list, scoring rubric, rate limits and approval gates govern every step.

## The daily process

The specification's fifteen steps, each delegated to its owning skill.

| # | Step | Owning skill | Notes |
|---|---|---|---|
| 1 | Discover new relevant websites | [backlink-opportunity-hunter](../skills/backlink-opportunity-hunter.md) | Categories A–D |
| 2 | Discover new competitor backlinks | [competitor-backlink-gap](../skills/competitor-backlink-gap.md) | Lower frequency — competitor profiles change slowly |
| 3 | Discover new brand mentions | [backlink-opportunity-hunter](../skills/backlink-opportunity-hunter.md) (E), [entity-seo](../skills/entity-seo.md) | Namesake check mandatory |
| 4 | Discover broken-link opportunities | [broken-link-building](../skills/broken-link-building.md) | Only if a genuine replacement resource exists |
| 5 | Discover relevant resource pages | [backlink-opportunity-hunter](../skills/backlink-opportunity-hunter.md) (D) | Apply the "do we deserve inclusion?" gate |
| 6 | Discover new local opportunities | [backlink-opportunity-hunter](../skills/backlink-opportunity-hunter.md) (A), [local-citation-authority](../skills/local-citation-authority.md) | **Blocked** while the address is disputed — see below |
| 7 | Discover new PR opportunities | [digital-pr-link-assets](../skills/digital-pr-link-assets.md), [backlink-opportunity-hunter](../skills/backlink-opportunity-hunter.md) (C) | |
| 8 | Check previously contacted prospects | [digital-pr-outreach](../skills/digital-pr-outreach.md) | Follow-ups due; declines are final |
| 9 | Check previously discovered prospects | [backlink-opportunity-hunter](../skills/backlink-opportunity-hunter.md) | Still live? still qualified? |
| 10 | Remove duplicates | This runbook | Deduplicate on registrable domain against CRM **and** rejection log |
| 11 | Score every opportunity | [off-page-governance](../skills/off-page-governance.md) | 100-point rubric, with confidence and proxy flags |
| 12 | Reject spam / low-quality | [off-page-governance](../skills/off-page-governance.md), [backlink-risk-monitor](../skills/backlink-risk-monitor.md) | Log every rejection with its reason |
| 13 | Add qualified prospects to the CRM | This runbook | `status = prospect` |
| 14 | Prepare recommended outreach | [digital-pr-outreach](../skills/digital-pr-outreach.md) | `DRAFT — FOR USER TO SEND` |
| 15 | Report results | `reports/daily-backlink-report.md` | |

Run steps 10–12 **before** deep qualification wherever possible — deduplicating and rejecting early avoids spending the cycle's effort on candidates that were never viable.

## Guardrails enforced every cycle

All eight automation failure protections from [off-page-governance](../skills/off-page-governance.md) apply. A cycle that cannot satisfy them does not run.

1. **Duplicate protection** — never re-surface or re-contact a known prospect.
2. **Domain protection** — no multiple low-value links from one domain without stated justification.
3. **Spam protection** — REJECT list applied before any further analysis.
4. **Anchor protection** — never propose anchors that push exact-match share past threshold.
5. **Rate limiting** — cap prospects promoted to "ready for approval" at what the user can genuinely review. A backlog of unreviewed drafts is a failed cycle, not a productive one.
6. **Approval gate** — everything external is user-executed.
7. **Audit trail** — log the cycle to `data/backlinks/opportunity-hunt-YYYY-MM-DD.md`: queries run, candidates found, rejections and reasons, prospects promoted.
8. **Rollback** — record the current state before recommending any change to an owned listing.

**No volume target.** Never "find N opportunities per day." The objective is qualified referring domains and authority gained per unit of effort. Zero qualified opportunities in a cycle is a legitimate, honest result.

## Currently blocking

`data/crawl/nap-instances.md` documents an unresolved conflict in the firm's office unit and floor across the website, the ICAI register, and third-party listings.

**Until the user confirms the authoritative address, this cycle must not prepare any directory submission or listing correction** — doing so would propagate an unconfirmed address across the web and be far harder to undo than to prevent. Discovery and scoring of local opportunities may continue; preparation of listing payloads is held. Flag this in every cycle report while it remains open.

## Cycle output

Each run produces:

1. `data/backlinks/opportunity-hunt-YYYY-MM-DD.md` — the audit trail.
2. Updated `data/backlinks/backlink-master.csv`.
3. Updated `data/backlinks/rejected-opportunities.md`.
4. Draft packages in `data/backlinks/outreach/`, marked `DRAFT — FOR USER TO SEND`.
5. `reports/daily-backlink-report.md` — refreshed per the template in that file.

## Common failure modes

- **Manufacturing output on a quiet cycle.** Report the quiet cycle.
- **Scoring from search snippets** instead of fetching the candidate.
- **Skipping deduplication** and re-surfacing rejected domains every run.
- **Accumulating unreviewed drafts** until the queue is unusable.
- **Preparing directory submissions** while the address is disputed.
- **Treating the cycle as an executor.** It discovers, qualifies, scores and prepares. The user acts.
