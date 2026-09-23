# Skill: Broken Link Building

## Purpose

Find authoritative pages carrying broken outbound links on topics this firm covers — Income Tax, GST, accounting, ITR, business registration, startup compliance, NRI taxation, audit, TDS, finance — determine whether cashahnawaz.com already has a genuinely appropriate replacement, and prepare a helpful correction the user can send. Where no suitable replacement exists, the honest output is a recommendation to build the resource first, not a link request for something inadequate.

This tactic works because the ask is a favour, not a request: a broken link is a defect on their page, and pointing it out is useful whether or not they use the replacement.

## Scope

**This skill owns:** discovery of broken outbound links on third-party pages, replacement-resource matching, and preparation of the notification.

**This skill does NOT own:**
- Broken links pointing *at this site* — [backlink-reclamation](backlink-reclamation.md).
- Broken *internal* links on cashahnawaz.com — [technical-seo](technical-seo.md) / [website-crawl](website-crawl.md).
- General prospect discovery — [backlink-opportunity-hunter](backlink-opportunity-hunter.md).
- Building the replacement resource — [digital-pr-link-assets](digital-pr-link-assets.md) specifies it, [linkable-content-planner](linkable-content-planner.md) sequences it, the user builds it.
- Sending anything — [digital-pr-outreach](digital-pr-outreach.md) drafts; the user sends.
- Scoring — [off-page-governance](off-page-governance.md).

## When to use it

- When the firm has a genuinely strong, current resource that could legitimately replace commonly-dead references (a maintained compliance calendar or a well-sourced guide are the usual candidates).
- After a major regulatory change, when a wave of links to superseded government pages, withdrawn circulars, and retired portal URLs breaks at once — the highest-yield window for this tactic in the Indian tax context.
- On the recurring cycle, at lower frequency than general opportunity hunting.

## Required Data

- Web search and fetch capability. **Both are essential** — this skill cannot run without the ability to check whether a linked URL is dead.
- The firm's live resource inventory, to judge replacement suitability honestly.
- `data/backlinks/backlink-master.csv` and the rejection log, for deduplication.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- Fetching candidate resource pages and reading their outbound links.
- **Verifying each outbound link individually** by fetching it — this is the core evidence of the skill and it is directly obtainable.
- Fetching the firm's own candidate replacement page, to judge whether it genuinely fits.
- Published contact routes on the prospect's site.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Bulk broken-link discovery.** Tools like Ahrefs' broken-link reports are not available here (per `reports/00-capability-check.md`). Discovery is manual, page by page, which makes it slow and makes prioritisation essential. Never present a hand-checked set as an exhaustive scan.
- Authority or traffic of the host page — `PROXY-SCORED` per [off-page-governance](off-page-governance.md).
- Whether the page is actively maintained — infer only from observable signals (recent updates, a dated changelog, other recent edits), and label the inference.
- What the dead URL originally contained, unless it can be established from the anchor text, surrounding context, or the URL itself. **Never assume**; a replacement matched to a guess is the main way this tactic goes wrong.

## Pre-Audit Checks

1. **Confirm the firm has at least one genuinely strong, current, relevant resource** before hunting. Without one, this skill produces nothing usable, and running it first wastes a cycle. If nothing qualifies, stop and route to [digital-pr-link-assets](digital-pr-link-assets.md).
2. Verify search and fetch capability this session.
3. Load the CRM and rejection log for deduplication on registrable domain.
4. Load [off-page-governance](off-page-governance.md) and [digital-pr-outreach](digital-pr-outreach.md).

## Step-by-Step Audit Process

### Step 1 — Find candidate host pages

Target pages that curate outbound links on the specification's topic list: Income Tax, GST, accounting, ITR, business registration, startup compliance, NRI taxation, audit, TDS, finance.

Search patterns:
- `"tax resources" India links` / `"useful links" GST India`
- `startup India compliance resources page`
- `"helpful resources" small business India tax`
- `NRI taxation resources links`
- University, incubator, chamber, association and library resource pages, which are frequently old, well-linked, and rarely maintained — the classic profile for this tactic.

Prioritise pages that are relevant, appear genuinely maintained by someone reachable, and sit on legitimate domains. Apply the REJECT list before spending time.

### Step 2 — Check the outbound links

Fetch each candidate page, extract its outbound links on-topic, and **test each one**. Record for every dead link: the URL, its anchor text, the surrounding sentence, and the observed failure (404, domain gone, server error, or redirect to something unrelated — a redirect to a generic homepage is functionally a dead reference and counts).

In the Indian tax context, the recurring pattern is links to superseded income-tax portal URLs, withdrawn or replaced circulars and notifications, retired GST portal paths, and defunct advisory blogs. These break in waves after portal migrations and regulatory changes.

### Step 3 — Determine what the dead resource was

Establish, from the anchor text, the surrounding sentence, and the URL structure, what the page was pointing readers to. If this cannot be determined with reasonable confidence, mark it `NOT DETERMINED` and do not propose a replacement — an unmatched suggestion makes the firm look careless and wastes the one favour the broken link earned.

### Step 4 — The honesty gate: does the firm actually have a replacement?

For each determinable dead link, ask whether cashahnawaz.com has a resource that genuinely serves the same purpose at comparable or better quality. Judge it as the curator would:

- Does it cover the same subject at the same depth, or is it a service page with a form on it? A commercial service page is **not** a replacement for an informational resource, and proposing one as such is the fastest way to be ignored.
- Is it current, accurate, and sourced?
- Is it ungated and accessible?
- Would a neutral curator agree it belongs there?

Three outcomes:

1. **Genuine replacement exists** → prepare the notification.
2. **A near-fit exists that needs improvement first** → route the improvement to [content-decay-refresh](content-decay-refresh.md) or [digital-pr-link-assets](digital-pr-link-assets.md), and hold the prospect.
3. **No replacement exists** → **recommend creating the resource first**, routed to [linkable-content-planner](linkable-content-planner.md) for scoring. Do not send a link request without one.

**Never create a weak article merely to obtain a link.** A thin page built to fill a broken-link slot fails the curator's judgement, adds a low-quality page to the site, and dilutes topical authority — it loses on every dimension.

### Step 5 — Score and prepare

Score per [off-page-governance](off-page-governance.md). Then prepare a notification that leads with the broken link and its exact location, mentions the replacement briefly and secondarily, and makes clear the report is useful either way. The correct tone is a colleague pointing out a defect, not a link request wearing a disguise.

Where **several** links on the same page are dead, report all of them — it is more helpful, and it makes the message obviously genuine.

Mark every draft `DRAFT — FOR USER TO SEND`. Claude does not contact the site.

## What Checks to Perform

- [ ] Firm confirmed to hold at least one genuine replacement resource before hunting began
- [ ] Candidate host pages verified relevant and legitimate; REJECT list applied
- [ ] Every outbound link tested individually, with the observed failure recorded
- [ ] Redirects to unrelated/generic pages counted as dead references
- [ ] Original resource purpose determined, or marked `NOT DETERMINED` and dropped
- [ ] Replacement suitability judged as a neutral curator would, not as an advocate
- [ ] Service pages never proposed as replacements for informational resources
- [ ] "Create the resource first" recommended where no genuine replacement exists
- [ ] No thin page proposed purely to enable a link request
- [ ] Multiple dead links on one page reported together
- [ ] Scored, deduplicated, CRM updated, draft marked user-to-send

## How to Identify Issues

A valid opportunity requires four verified facts: the host page is relevant and legitimate; a specific outbound link is genuinely dead; what it pointed to is determinable; and the firm has a resource a neutral curator would accept as a replacement. Three out of four is not an opportunity — it is either a content recommendation or a discard. The most common honest outcome of a cycle is a short list of genuine prospects plus a longer list of "we would need to build X first," and reporting that accurately is the point.

## Evidence to Collect

Save to `data/backlinks/`:
- `broken-link-building-YYYY-MM-DD.md` — pages checked, links tested, results, decisions.
- `broken-link-queue.csv` — host URL, dead URL, anchor, inferred purpose, proposed replacement, suitability verdict, score, status.
- Per prospect: the quoted sentence containing the dead link, plus the observed failure and the date tested.
- `resource-gaps.md` — dead links the firm could serve if a resource existed, routed to [linkable-content-planner](linkable-content-planner.md). Over time this becomes a genuinely demand-driven content backlog, which is one of the more valuable by-products of this skill.

## How to Prioritize Issues

- **HIGH** — a relevant, authoritative, maintained page with a dead link the firm can replace *today* with an existing strong resource, ideally one that supports a priority service.
- **HIGH** — a page with several dead links, where the report is unambiguously helpful.
- **MEDIUM** — a good prospect needing a modest improvement to an existing page first.
- **MEDIUM** — a repeated pattern of dead links across many pages pointing at the same retired resource; that is a content opportunity with proven demand.
- **LOW** — low-relevance pages, or pages with no reachable maintainer.
- **Not a finding** — no determinable purpose, no genuine replacement, or a REJECT-list host.

## Implementation Recommendations

For the user to execute manually.

- **Notification:** supply the host page URL, the exact dead link and its anchor, where on the page it sits, the observed failure, the proposed replacement URL, the published contact route, and the draft message. The user reviews and sends.
- **Re-test immediately before sending.** A dead link fixed in the interim makes the message wrong and the sender look careless. Add this as an explicit step in the handover.
- **Where a resource must be built first:** supply the specification, not the outreach. Note the evidenced demand (how many pages were found linking to a now-dead resource of that type) as justification, since that is unusually concrete evidence for a content decision.
- **Never** recommend publishing a thin page to service a link request.

## How to Validate Fixes

- **Placement:** fetch the host page after the user reports a response and confirm the link exists, its anchor, `rel`, and placement. Update the CRM with `first_seen`.
- **Partial success is normal and still valuable:** curators often fix the broken link without adding the replacement. Record that outcome honestly rather than as a failure — it costs nothing and preserves the relationship.
- **Pipeline health:** track the ratio of prospects found to replacements available. Persistently low availability is a content finding, not an outreach finding.
- **Never** count a prepared draft as an outcome.

## Expected Output Format

1. **Method and limits header**, e.g.:

   > No bulk broken-link tooling is available in this project (verified). The pages below were checked manually; every outbound link listed was individually fetched and its failure observed on the date shown. This is a sample, not an exhaustive scan.

2. **Opportunity table:**

   | # | Host page | Dead URL | Anchor | Inferred purpose | Replacement | Suitability | Score | Status |
   |---|---|---|---|---|---|---|---|---|

3. **Draft notifications**, marked `DRAFT — FOR USER TO SEND`, each with the re-test-before-sending reminder.
4. **Resource gaps** — routed to [linkable-content-planner](linkable-content-planner.md), with the demand evidence.
5. **Discards** with reasons.
6. Findings in the standard CLAUDE.md template with Confidence Level and Evidence Source.

## Common Mistakes to Avoid

- **Proposing a service page as a replacement for an informational resource.** Curators see through it immediately, and it converts a helpful message into a sales pitch.
- **Building a thin page to service a broken link.** Explicitly prohibited: never create a weak article merely to obtain a link.
- **Guessing what the dead resource was**, then proposing an unrelated replacement.
- **Reporting one dead link while ignoring three others on the same page** — less helpful and less credible.
- **Failing to re-test before the user sends.**
- **Treating a redirect to a homepage as a working link.** For the reader it is a dead reference.
- **Leading with the ask** instead of the defect.
- **Presenting manual sampling as a comprehensive audit.**
- **Chasing dead links on irrelevant pages** because they are easy to find.
- **Sending anything.** Claude prepares; the user sends.
