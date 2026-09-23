# Skill: Digital PR Outreach

## Purpose

Research individual prospects — journalists, editors, publishers, bloggers, association secretaries, site owners — and prepare personalised, genuinely useful outreach that the **user** then sends manually. The output is a small number of well-researched, specific, human-reviewable drafts, each tied to a real reason this firm is relevant to that person's audience.

## Scope

**This skill owns:** prospect research, the prospect record, personalisation evidence, draft messages, and the follow-up policy.

**This skill does NOT own:**
- Sending anything. **Claude never sends outreach in this project** — see the hard rule below.
- Finding the opportunity in the first place — [backlink-opportunity-hunter](backlink-opportunity-hunter.md), [competitor-backlink-gap](competitor-backlink-gap.md), [broken-link-building](broken-link-building.md), [backlink-reclamation](backlink-reclamation.md). Those skills produce opportunities; this one prepares the approach.
- Deciding whether the firm has something worth pitching — [digital-pr-link-assets](digital-pr-link-assets.md), [linkable-content-planner](linkable-content-planner.md).
- Scoring — [off-page-governance](off-page-governance.md).
- Reclamation-specific message types (link corrections, 301 requests, unlinked-mention conversions) — [backlink-reclamation](backlink-reclamation.md) owns those workflows, though it uses this skill's drafting standards.

## The hard rule

> **Claude Code does not contact anyone.** No email, contact form, DM, comment, or submission — not after approval of a finding, not for a "low-risk" reclamation note, not ever.

This follows from CLAUDE.md's Implementation Policy and the approval-gate matrix in [off-page-governance](off-page-governance.md). Claude researches the prospect, drafts the message, and hands over a ready-to-send package. The user reviews, edits, and sends it from their own account. Every draft is written in the user's voice, as a message *they* would send, and is marked `DRAFT — FOR USER TO SEND`.

The source specification's CRITICAL RULE applies in full and is not softened here. Do **not** prepare or plan any of: mass generic outreach, spamming large numbers of websites, automatic guest-post submission at scale, fake profiles, forum spam, comment backlinks, automated blog commenting, purchased backlinks, PBNs, doorway sites, fake citations, or anchor-text manipulation. Any of these is `REJECT` under [off-page-governance](off-page-governance.md).

Outreach here must be: **relevant + personalised + useful + human-reviewable.** If a draft fails any of the four, it does not leave this skill.

## When to use it

- When a qualified prospect reaches PRIORITY A or B and there is a genuine, specific thing to offer.
- When a confirmed unlinked brand mention needs a correction request drafted.
- When a broken-link-building opportunity has a verified replacement resource live.
- When a journalist has covered a topic the firm can add real expertise to.

## Required Data

- A scored prospect from the CRM (`data/backlinks/backlink-master.csv`), PRIORITY C or better.
- The **publicly published** contact route for that prospect.
- Personalisation evidence: a specific article, page, resource list, or call for contributions — fetched and read.
- The specific asset or contribution being offered, and its live URL if it exists.
- Contact history from the CRM, to enforce duplicate protection.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- The prospect's own site: published contact page, editorial or submissions email, contributor guidelines, staff/masthead listing, bylines, the specific article to reference.
- The publication's stated policies — what they accept, what they explicitly do not.
- Whether they link out editorially, and to what.
- CRM contact history.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Any contact detail not publicly published.** Never guess, infer, or pattern-construct an email address (`firstname.lastname@domain`), and never use a scraped or purchased list. If no published route exists, the prospect is `DATA NOT AVAILABLE — no contact route` and the draft is not prepared. This is the single most important limitation in the skill: guessed contacts are what turn outreach into spam.
- Personal contact details, private phone numbers, or home addresses — never collected, never recorded.
- Whether a prospect has been contacted outside this project — ask the user; do not assume the CRM is complete.
- Response-rate predictions, publication probability, or "expected placements."
- The prospect's editorial calendar, unless published.

## Pre-Audit Checks

1. **Duplicate protection** — check the CRM for prior contact with this domain or person. If contacted and unanswered, do not prepare another approach unless the follow-up policy below permits it.
2. **Domain protection** — do not prepare a second ask to a domain that already links to the site, unless there is a stated strategic reason.
3. **Legitimacy** — re-confirm the prospect passes [off-page-governance](off-page-governance.md)'s REJECT list.
4. **Substance check** — confirm there is something genuinely useful to offer. No offer, no draft.
5. **Contact route** — confirm it is published on the prospect's own site, and record where it was found.

## Step-by-Step Audit Process

### Step 1 — Build the prospect record

For every prospect, collect and record (per the source specification's field list):

| Field | Notes |
|---|---|
| Website | Domain |
| Publication | Name of the outlet or organisation |
| Topic | What they actually cover |
| Contact method | **Published route only**, with the URL where it was found |
| Relevant article | The specific piece being referenced — URL and date |
| Why this firm is relevant | The concrete, specific link to their audience |
| Proposed contribution | What is being offered |
| Potential target URL | The page on cashahnawaz.com it would point at |
| Link opportunity | The nature of the placement |
| Opportunity score | From [off-page-governance](off-page-governance.md), with confidence |

If "why this firm is relevant" cannot be answered in one specific sentence that could not be said about any other CA firm, the prospect is not ready and no draft is written.

### Step 2 — Establish the genuine offer

Outreach succeeds when it gives before it asks. Legitimate offers for this firm:

- **Expert commentary** on a tax or compliance change, from a named, qualified CA — the strongest and most repeatable offer a CA firm has.
- **A correction or update** to something outdated or incorrect in their existing content (deadlines, rates, superseded rules) — genuinely useful, and it costs them nothing to accept.
- **A resource** that belongs on their curated list, where it demonstrably belongs.
- **A replacement** for a broken link they are already carrying.
- **A contribution** where they publish an open call for contributors.
- **A correction of an existing mention** — they already named the firm.

Not legitimate: "we'd love a backlink"; a generic guest-post offer with no topic; anything requiring payment not disclosed; any exchange.

### Step 3 — Draft, personally

Every draft must:
- **Reference something specific and real** they published, showing it was read. Quote or name the exact piece.
- **State the offer plainly** in the first two lines. Editors decide fast.
- **Establish credibility briefly** — qualified CA, Mumbai, the relevant practice area, one line.
- **Be honest about the ask**, including any link, rather than concealing it. Concealment reads as manipulation and destroys the relationship.
- **Be short** — under ~150 words for a cold approach.
- **Include an easy no.**
- **Never** claim a relationship that does not exist, fabricate credentials, invent a shared contact, or imply prior correspondence.
- **Never** promise anything the firm has not agreed to deliver.
- **Never** contain a fabricated statistic or an unverified tax fact — YMYL accuracy applies to outreach, not just published pages. Anything factual in a pitch is sourced per [eeat-ymyl-authority](eeat-ymyl-authority.md).

Write one draft per prospect. Templates with a name merged in are mass outreach with extra steps, and the specification forbids them.

### Step 4 — Prepare the send package

For each approved-to-draft prospect, produce: the recipient and the published contact route (with its source URL); the subject line; the message body; the specific evidence URL that personalises it; what to do with a reply; and the follow-up policy. Mark it `DRAFT — FOR USER TO SEND`.

Update the CRM: `outreach_status = draft_ready`. It becomes `sent` **only** when the user confirms they sent it — Claude never marks a message sent on its own initiative.

### Step 5 — Follow-up policy

- At most **one** follow-up, no sooner than 7–10 days after the first message, and only where there was a substantive offer.
- No second follow-up. Silence is an answer.
- A decline is final; record it and never re-approach that prospect for the same ask.
- Never re-approach the same person for a different ask within the same cycle.
- Record every send, reply, decline and placement in the CRM, so duplicate protection actually works.

### Step 6 — Rate limit

Cap drafts per cycle to what the user can genuinely review and send personally. A queue of 60 drafts is not a pipeline; it is either unreviewed work or, if sent, exactly the mass outreach the specification prohibits. A handful of excellent drafts is the correct output.

## What Checks to Perform

- [ ] Every prospect deduplicated against CRM contact history
- [ ] Contact route publicly published and its source URL recorded — none guessed
- [ ] A specific, genuine offer identified before drafting
- [ ] "Why this firm specifically" answerable in one non-generic sentence
- [ ] Each draft references a specific piece the prospect actually published
- [ ] Each draft individually written, not templated
- [ ] The ask, including any link, stated honestly
- [ ] No fabricated credentials, relationships, statistics, or tax facts
- [ ] Every draft marked `DRAFT — FOR USER TO SEND`
- [ ] Rate limit respected; the queue is reviewable
- [ ] Follow-up policy attached; declines recorded as final
- [ ] Nothing sent by Claude — no exceptions

## How to Identify Issues

Findings here are usually about the *state of the pipeline*: prospects with no published contact route (a dead end to record and stop working); prospects where the firm has no genuine offer (route to [digital-pr-link-assets](digital-pr-link-assets.md) — the block is the missing asset, not the missing message); an outreach history with sends and no replies, indicating the offer or targeting is wrong rather than the volume being too low; and any pressure to increase volume, which should be answered with the governance rule rather than accommodated.

## Evidence to Collect

Save to `data/backlinks/`:
- `outreach/<domain>-<YYYY-MM-DD>.md` — one file per prospect: full record, evidence URLs, the draft, and the follow-up policy.
- Updated `backlink-master.csv` — `contact`, `outreach_status`, `response`, `placement_status`, `notes`.
- `outreach-log.md` — chronological audit trail of every draft prepared, every user-confirmed send, and every reply, satisfying [off-page-governance](off-page-governance.md)'s audit-trail requirement.
- `no-contact-route.md` — prospects dropped for lack of a published contact route, so they are not re-researched.

Never store personal contact data beyond the published professional route.

## How to Prioritize Issues

- **HIGH** — PRIORITY A prospects with a live asset ready, a published contact route, and a specific personalisation hook. These are ready to send today.
- **HIGH** — correction opportunities on prospects already mentioning the firm, or already carrying a broken link the firm can replace: low effort, high acceptance, no imposition.
- **MEDIUM** — PRIORITY B prospects with a real offer.
- **LOW** — PRIORITY C prospects, or A/B prospects whose offer is weak.
- **Blocked** — no contact route, or no genuine offer. Record the reason; these are not sent "anyway."

Expert-commentary offers tied to a current change (a Budget provision, a GST Council decision, a CBDT notification) are time-sensitive; prioritise them within their window.

## Implementation Recommendations

The deliverable is a package the user executes:

1. **What to send** — recipient, subject, body, ready to paste.
2. **Where to send it** — the published route, with the URL where it was found.
3. **When** — any timing consideration (a news hook, a filing deadline, a stated submission window).
4. **What to attach or link** — the live asset URL.
5. **How to handle replies** — what an acceptance requires the firm to deliver, and what to do with a request for payment (disclose, and treat as a sponsored placement requiring `rel="sponsored"` — route back to [off-page-governance](off-page-governance.md)).
6. **What to tell Claude afterwards** — so the CRM reflects reality.

The user sends from their own account, in their own name. Claude's involvement ends at the handover.

## How to Validate Fixes

- **Placement:** when the user reports a placement, verify by fetching the live page — confirm the link exists, its anchor, `rel`, and placement, then update the CRM with `first_seen`.
- **Quality of placement:** confirm it is in-content and on a page consistent with what was pitched, not relegated to a link dump.
- **NAP consistency:** if a listing was created, check it against the canonical record in [local-citation-authority](local-citation-authority.md).
- **Pipeline health:** review acceptance rate by offer type and prospect category. A category with sustained zero acceptance should be stopped, and saying so is the right recommendation.
- **Never** validate by assuming a sent message produced a link. Verify or record nothing.

## Expected Output Format

1. **Ready-to-send queue:**

   | # | Prospect | Publication | Offer | Target URL | Score / Band | Contact route (source) | Status |
   |---|---|---|---|---|---|---|---|

2. **One draft package per prospect**, each headed `DRAFT — FOR USER TO SEND`, with the personalisation evidence URL directly above the draft so the user can verify it before sending.
3. **Blocked list** — no contact route, or no genuine offer, with routing.
4. **Follow-up due list** — who is due, and the date the follow-up window opens.
5. A standing note in every output: *No message in this queue has been sent. Claude does not contact anyone in this project; each draft requires the user to review and send it manually.*

## Common Mistakes to Avoid

- **Sending anything.** Claude does not. The most important line in this file.
- **Guessing an email address.** No published route means no outreach.
- **Templating with a merge field** and calling it personalised.
- **Pitching with nothing to offer** — the fastest way to burn a genuinely valuable prospect permanently.
- **Hiding the ask** behind flattery. Editors recognise it instantly.
- **Fabricating a statistic or a tax fact** to make a pitch land. YMYL accuracy applies here too.
- **Over-following-up.** One follow-up, then stop.
- **Re-approaching a declined prospect.**
- **Optimising for drafts produced.** The metric is qualified placements, and a large unreviewed queue is a failure state.
- **Recording a message as sent** because a draft was prepared. Only a user confirmation moves it to `sent`.
- **Accepting a paid placement without disclosure** — undisclosed paid links violate Google's guidelines and are a REJECT in [off-page-governance](off-page-governance.md); if the firm wants it anyway, it needs `rel="sponsored"` and that is the user's decision, made with the risk stated.
