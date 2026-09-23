# Backlink Database

The running inventory and CRM for all off-page work in this project. Maintained by [off-page-seo](../../skills/off-page-seo.md), [backlink-opportunity-hunter](../../skills/backlink-opportunity-hunter.md), [competitor-backlink-gap](../../skills/competitor-backlink-gap.md), [backlink-reclamation](../../skills/backlink-reclamation.md), [broken-link-building](../../skills/broken-link-building.md), [digital-pr-outreach](../../skills/digital-pr-outreach.md) and [backlink-risk-monitor](../../skills/backlink-risk-monitor.md).

Its purpose is to answer, over time, the one question raw link counts cannot:

> **Did SEO activity actually increase authority?**

## Current data status

**No backlink-data tool and no GSC connector were available at the last verified capability check** (`reports/00-capability-check.md`). Consequences for everything in this folder:

- `backlink-master.csv` is **not** a complete backlink profile and must never be presented as one. It is a record of links and opportunities established by direct observation.
- Counting its rows does **not** give a backlink or referring-domain total. Those remain `DATA NOT AVAILABLE`.
- `domain_quality` and `traffic_estimate` are proxy judgements, not metrics — see the field notes below.
- New/lost link analysis becomes possible only once `snapshots/` holds two or more dated snapshots.

## Files

| File | Purpose | Owning skill |
|---|---|---|
| `backlink-master.csv` | The master inventory and CRM | all off-page skills |
| `snapshots/backlink-master-YYYY-MM-DD.csv` | Dated snapshot per cycle — enables new/lost analysis | [off-page-seo](../../skills/off-page-seo.md) |
| `rejected-opportunities.md` | Rejected domains + reasons, so they are never re-analysed | [backlink-opportunity-hunter](../../skills/backlink-opportunity-hunter.md) |
| `unlinked-brand-mentions.md` | Confirmed mentions without links | [backlink-reclamation](../../skills/backlink-reclamation.md) |
| `entity-record.md` | Canonical NAP/entity record | [local-citation-authority](../../skills/local-citation-authority.md) |
| `entity-definition.md` / `entity-footprint.csv` | Entity footprint | [entity-seo](../../skills/entity-seo.md) |
| `citation-inventory.csv` | Third-party listings, values verbatim | [local-citation-authority](../../skills/local-citation-authority.md) |
| `risk-classification.csv` | SAFE / WATCH / RISK per link | [backlink-risk-monitor](../../skills/backlink-risk-monitor.md) |
| `outreach/` | One file per prospect: record, evidence, draft | [digital-pr-outreach](../../skills/digital-pr-outreach.md) |
| `outreach-log.md` | Chronological audit trail | [digital-pr-outreach](../../skills/digital-pr-outreach.md) |
| `opportunity-hunt-YYYY-MM-DD.md` | Per-cycle discovery log | [backlink-opportunity-hunter](../../skills/backlink-opportunity-hunter.md) |
| `competitor-gap-matrix.csv` | Gap analysis | [competitor-backlink-gap](../../skills/competitor-backlink-gap.md) |
| `velocity-log.md` | New links/domains per period, with explanations | [backlink-risk-monitor](../../skills/backlink-risk-monitor.md) |

## `backlink-master.csv` fields

| Field | Meaning | Rules |
|---|---|---|
| `discovered_date` | When this project first recorded it | `YYYY-MM-DD` |
| `first_seen` | When the link was first **verified live** | Blank until observed live — never guessed |
| `last_seen` | Most recent live verification | Update on each re-check |
| `source_domain` | Registrable domain — the deduplication key | Lowercase, no scheme, no `www.` |
| `source_url` | Exact page carrying the link or opportunity | Full URL; never just the homepage for an opportunity |
| `target_url` | Page on cashahnawaz.com linked to or proposed | Full URL |
| `anchor_text` | Anchor, verbatim | Exact text; blank if not yet placed |
| `link_type` | `editorial` / `directory` / `profile` / `listing` / `footer` / `sitewide` / `comment` / `image` / `mention-only` | |
| `domain_quality` | Authority judgement | `PROXY-SCORED` unless a verified tool produced it. **Never a DA/DR figure** |
| `topical_relevance` | `high` / `medium` / `low` | Accounting, tax, finance, business, professional services |
| `local_relevance` | `high` / `medium` / `low` / `none` | Mumbai / India |
| `traffic_estimate` | Genuine-audience judgement | `PROXY-SCORED` or `DATA NOT AVAILABLE`. **Never a traffic number without a tool** |
| `competitor_link` | `yes` / `no` | Which competitors, in `notes` |
| `acquisition_method` | `existing` / `eligibility` / `directory` / `editorial` / `resource-page` / `broken-link` / `reclamation` / `mention-conversion` / `unknown` | |
| `status` | `prospect` / `prepared` / `awaiting-user` / `live` / `lost` / `recovered` / `rejected` | |
| `opportunity_score` | 0–100 per [off-page-governance](../../skills/off-page-governance.md) | Record the confidence level in `notes` |
| `outreach_status` | `none` / `draft_ready` / `sent` / `replied` / `declined` / `no-response` | `sent` **only** after the user confirms they sent it |
| `contact` | Publicly published contact route | **Never guessed or pattern-constructed.** Blank = `DATA NOT AVAILABLE` |
| `response` | What the prospect replied | Verbatim summary |
| `placement_status` | `none` / `promised` / `verified-live` / `removed` | `verified-live` only after fetching the page |
| `notes` | Confidence level, proxy-scored dimensions, competitors, rollback values, rationale | |

## Rules for this folder

1. **No invented metrics.** No backlink totals, DA/DR values, or traffic figures without a tool that produced them this session.
2. **A row is not a link.** A row may be a prospect, a rejected candidate, or a verified live link — `status` is what distinguishes them.
3. **Verify before you claim.** `first_seen` and `placement_status = verified-live` require fetching the page and reading the anchor.
4. **Deduplicate on `source_domain`.**
5. **Snapshot every cycle** into `snapshots/` before modifying the master, so history survives.
6. **Log rejections**, so rejected domains are not re-evaluated each cycle.
7. **Record the "before" state** in `notes` before recommending any change to an owned listing, so the user can revert.
8. **No personal contact data** beyond the published professional route.
9. **Claude never sends, submits, claims, or edits anything.** This CRM tracks prepared work and user-executed outcomes only — see CLAUDE.md's Implementation Policy and [off-page-governance](../../skills/off-page-governance.md) Rule 0.
