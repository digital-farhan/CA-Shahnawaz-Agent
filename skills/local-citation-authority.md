# Skill: Local Citation & Entity Authority

## Purpose

Maintain a single authoritative NAP/entity record for the firm, audit every discoverable third-party listing against it, and detect inconsistencies that undermine local ranking and client trust. For a Mumbai CA firm whose site publishes an office address and phone number, entity consistency is a direct local ranking factor and a direct trust factor — a prospective client who finds three different office units for the same firm has a reason to doubt it.

This project has already found exactly that problem, which makes this skill immediately actionable rather than theoretical.

## Scope

**This skill owns:** the canonical NAP/entity record, the citation inventory across third-party directories and professional listings, consistency auditing against that record, and the correction queue.

**This skill does NOT own:**
- On-site NAP consistency, GBP signals, service-area content, and click-to-call mechanics — [local-seo](local-seo.md), which owns the *website* side. This skill owns the *off-site* listing side and consumes local-seo's determination of the authoritative on-site values.
- Non-NAP brand mentions, professional profiles, press, and the wider entity footprint — [entity-seo](entity-seo.md).
- Directory listings evaluated purely as link opportunities — [backlink-opportunity-hunter](backlink-opportunity-hunter.md), which hands listing details here so NAP values stay consistent.
- Schema validity — [schema-audit](schema-audit.md).
- Creating, claiming, editing, or submitting any listing — **the user does all of this manually**.

## When to use it

- Before any directory submission or listing work, so a new listing does not add a fourth address variant.
- When [local-seo](local-seo.md) flags a NAP conflict.
- When [backlink-opportunity-hunter](backlink-opportunity-hunter.md) or [competitor-backlink-gap](competitor-backlink-gap.md) surfaces a directory opportunity.
- On a recurring cycle, since listings drift, get auto-created by aggregators, and get edited by third parties without notice.

## Required Data

- The **owner-confirmed** authoritative NAP. This is a hard dependency — see the open decision below.
- `data/crawl/nap-instances.md` — the existing evidence file, which already records the conflict.
- On-site NAP values from [local-seo](local-seo.md).
- Discoverable third-party listings.
- The firm's professional registration details (ICAI firm registration number, membership number) as published on official sources.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- On-site NAP via fetch — footer, Contact, About, schema.
- Public third-party listings via search and fetch — directories, professional listings, marketplace profiles — each read and quoted directly.
- Official professional registers (e.g., the ICAI public firm/member listing) where publicly searchable — the strongest available evidence of the registered name, firm registration number and registered address.
- Verification of whether each listing links to the site, and with what URL.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Google Business Profile contents.** No GBP connector exists in this project (confirmed in `reports/00-capability-check.md` and [local-seo](local-seo.md)). Category, reviews, rating, hours, photos, posts, Q&A, and GBP-side NAP are all `DATA NOT AVAILABLE`. Tell the user plainly to check GBP Manager themselves; never infer GBP contents from the website.
- **Which address is actually correct.** Claude can prove that listings disagree; it cannot determine which is the firm's current client-facing office. That is an owner decision and must be requested, not assumed.
- A complete citation inventory. Discovery is search-based and always partial; aggregator-generated listings frequently exist that no search surfaces. Never claim completeness.
- Listing ownership/claim status, unless publicly displayed.
- Any listing's traffic or referral value.

## Pre-Audit Checks

1. **Resolve or flag the canonical NAP before auditing anything against it.** Auditing consistency without an agreed reference produces a list of differences with no correct answer.
2. Confirm GBP is unavailable this session (attempt, then record) so GBP items are correctly marked.
3. Load `data/crawl/nap-instances.md` so prior evidence is extended, not re-gathered.
4. Load [off-page-governance](off-page-governance.md) — mass directory spam is a REJECT, and the Directory Legitimacy Test below is the gate for which listings are even worth holding.

## The canonical entity record

Maintain `data/backlinks/entity-record.md` as the single source of truth, tracking every field in the specification:

| Field | Value | Source | Confidence |
|---|---|---|---|
| Business name | | | |
| Legal / registered name | | ICAI register | |
| Firm registration number | | ICAI register | |
| Address (unit, floor, building, street, locality, city, PIN) | | **owner confirmation required** | |
| Phone | | | |
| Website | | | |
| Email | | | |
| Categories | | | |
| Opening hours | | | |
| Business description (short / long) | | | |
| Social profiles | | | |
| Professional profiles | | | |
| Directory profiles | | | |

Every field carries a source and a confidence level. A field that has not been owner-confirmed is marked `UNCONFIRMED` and must not be used to "correct" a live listing.

### Open decision blocking this skill

`data/crawl/nap-instances.md` already documents a genuine, unresolved address conflict for **Shahnawaz and Associates**: the website and its LocalBusiness markup publish a *C-18, Ground Floor, Grace Plaza* address; the ICAI public firm list shows *B38, Ground Floor, Grace Plaza*; and Justdial and Shuru both show *B/110, First Floor, Grace Plaza*. Same building, three different units across two floors.

**The user must confirm the current client-facing office unit and floor before any listing is corrected.** Until then:
- Do not bulk-edit or bulk-recommend edits to listings.
- Do not assume the website is right because it is the firm's own — the ICAI register is the official professional record and the discrepancy may run the other way.
- Do not assume the most frequent variant is correct; frequency reflects which aggregator copied which source, not which office the firm occupies.
- Do record every observed variant with its source, so the correction sweep can be done once, correctly, when the answer arrives.

## Step-by-Step Audit Process

### Step 1 — Establish the canonical record

Populate the entity record from the site, the official register, and owner confirmation. Where a field is disputed, record every variant with its source and mark the field `DISPUTED — OWNER DECISION REQUIRED` rather than picking one.

### Step 2 — Discover listings

Search for: the exact business name and its variants (`Shahnawaz and Associates`, `Shahnawaz & Associates`, `Shahnawaz Associates`, `CA Shahnawaz`); the phone number as a literal string; the address string; and the domain. Phone and address searches are the most effective way to surface aggregator-generated listings the firm never created.

Cover: general business directories; India-specific directories; CA/professional directories; the ICAI public listing; map and review platforms; marketplace and service-listing platforms; social and professional profiles; local chamber and association member pages.

### Step 3 — Record each listing exactly as published

For every listing found, fetch it and record verbatim: name, address, phone, website URL, email, categories, hours, description, whether the link is followed, and whether the listing appears claimed. Quote values exactly — normalising as you record destroys the evidence the audit depends on.

### Step 4 — Detect inconsistencies

Compare each listing to the canonical record and classify each difference:

| Type | Example | Severity |
|---|---|---|
| **Address conflict** | Different unit, floor, or building | Highest — the current live problem |
| **Phone conflict** | Different or outdated number | Highest — directly breaks enquiries |
| **Name variant** | `and` vs `&`, with/without `CA` | Medium — some variation is normal; contradiction is not |
| **Website conflict** | Wrong URL, HTTP, non-canonical, or a competitor's URL | Medium–High |
| **Category error** | Wrong profession or service category | Medium |
| **Hours conflict** | Contradicts published hours | Low–Medium |
| **Description drift** | Claims services the firm does not offer | Medium — can generate unqualified enquiries |
| **Duplicate listing** | Two listings for one firm on one platform | Medium — splits reviews and signals |
| **Defunct listing** | Old address or dead phone still live | High |

Distinguish **variation** from **contradiction**. `Shahnawaz and Associates` vs `Shahnawaz & Associates` is cosmetic and rarely worth an edit. Two different floors is a contradiction and matters.

### Step 5 — Apply the Directory Legitimacy Test

Before recommending any listing be created or maintained, confirm it is worth holding: does the directory have a real audience; is it moderated; is the firm's category genuinely represented; is inclusion free or reasonably priced and not a pure link sale; would a client plausibly use it? A directory failing this is `REJECT` under [off-page-governance](off-page-governance.md), and a NAP inconsistency on a spam directory is not worth correcting — it is worth ignoring.

### Step 6 — Build the correction queue

Rank corrections by impact: phone errors and address contradictions on high-visibility, legitimate listings first; duplicates next; cosmetic variants last (often not at all). For each, record the **current value before any change is recommended**, per [off-page-governance](off-page-governance.md)'s rollback requirement.

Then hand over. **Claude never creates, claims, edits, or removes a listing.**

## What Checks to Perform

- [ ] Canonical entity record exists, with source and confidence per field
- [ ] Disputed fields marked `DISPUTED — OWNER DECISION REQUIRED`, not silently resolved
- [ ] The open address conflict flagged and not worked around
- [ ] GBP availability tested this session and marked `DATA NOT AVAILABLE` if absent
- [ ] Discovery run on name variants, phone, address and domain — not name alone
- [ ] Every listing fetched and values recorded verbatim
- [ ] Inconsistencies classified; variation distinguished from contradiction
- [ ] Directory Legitimacy Test applied before recommending any listing
- [ ] Duplicate and defunct listings identified
- [ ] Current values recorded before any correction is recommended
- [ ] Inventory explicitly stated as partial, never complete
- [ ] Nothing created, claimed, or edited by Claude

## How to Identify Issues

A citation finding requires the canonical value, the listing's published value, the listing URL, and the date observed. The severity turns on whether the difference could **misdirect a client or contradict the entity**: a wrong phone number or a wrong floor is a real problem; `&` versus `and` generally is not. The compound finding worth leading with is a contradiction that spans the firm's *own* website, its *official professional register*, and *third-party listings* simultaneously — which is precisely the situation already documented here, and which no amount of link building will compensate for.

## Evidence to Collect

Save to `data/backlinks/` (keeping `data/crawl/nap-instances.md` as the on-site evidence file):
- `entity-record.md` — the canonical record.
- `citation-inventory.csv` — platform, listing URL, every field verbatim, claimed status, link status, date observed.
- `citation-inconsistencies.md` — every difference, classified, with canonical vs. observed side by side.
- `citation-correction-queue.md` — ranked corrections, each with the current value recorded for rollback, and the manual steps.
- `citation-rejected-directories.md` — directories failing the legitimacy test, so they are not re-evaluated.

## How to Prioritize Issues

- **CRITICAL** — a wrong phone number, or an address contradiction, on a high-visibility legitimate listing. This breaks enquiries and directly damages CLAUDE.md's success journey at the contact stage.
- **HIGH** — the unresolved multi-source address conflict itself (currently open); defunct listings with old contact details; duplicate listings on a major platform; a listing pointing at the wrong website.
- **MEDIUM** — category errors; description drift claiming services not offered; missing listings on legitimate professional directories competitors hold.
- **LOW** — cosmetic name and formatting variants; hours mismatches on minor platforms.
- **Not a finding** — inconsistencies on spam directories that fail the legitimacy test.

## Implementation Recommendations

All manual, for the user.

- **First, resolve the address.** The concrete ask: confirm the current client-facing unit and floor, and whether the ICAI-registered address should match it. Everything else waits, because correcting listings to an unconfirmed value would propagate an error across the web and be far harder to undo than to prevent.
- **Then correct in order:** the website and its LocalBusiness schema ([local-seo](local-seo.md) / [schema-audit](schema-audit.md)) → Google Business Profile → the official professional listing if it needs updating → major legitimate directories → minor ones. Fixing directories before the website leaves the authoritative source wrong.
- **Per listing:** supply the listing URL, the exact current value, the exact replacement value, the edit route as published on that platform, and whether claiming is required first. Note that some platforms require verification that takes days.
- **Duplicates:** supply the platform's merge/removal process; recommend keeping the claimed, more complete, better-reviewed listing.
- **New listings:** supply the complete field values verbatim from the canonical record so the new listing is consistent from creation.
- Claude performs none of these steps.

## How to Validate Fixes

- **Per correction:** re-fetch the listing after the user reports the edit and confirm the published value matches the canonical record. Many platforms queue edits for moderation — a submitted edit is not a live edit, so re-check after a week.
- **Consistency sweep:** re-run the inventory next cycle and count listings matching the canonical record. That count, trending upward, is the real measure of citation health.
- **Schema alignment:** confirm on-site LocalBusiness markup matches the corrected canonical values ([schema-audit](schema-audit.md)).
- **GBP:** the user checks in GBP Manager and reports back; Claude cannot verify it.
- **Business outcome:** call and enquiry volume, if GA4/call tracking ever becomes available; otherwise `DATA NOT AVAILABLE`.

## Expected Output Format

1. **Canonical entity record**, with disputed fields flagged.
2. **Citation inventory table:**

   | Platform | Listing URL | Name | Address | Phone | Website | Claimed? | Matches canonical? | Date observed |
   |---|---|---|---|---|---|---|---|---|

3. **Inconsistency report** — canonical vs. observed, classified by type and severity.
4. **Ranked correction queue** with current values recorded and manual steps.
5. **Blocking decision** stated prominently while the address remains unconfirmed.
6. **Limitations statement**, e.g.: *GBP is `DATA NOT AVAILABLE` (no connector, verified). This inventory is search-derived and partial; aggregator-generated listings may exist that were not surfaced.*
7. Findings in the standard CLAUDE.md template with Confidence Level and Evidence Source.

## Common Mistakes to Avoid

- **Picking a canonical address without owner confirmation** — including by assuming the website is right, or that the most common variant wins. Frequency reflects aggregator copying, not occupancy.
- **Bulk-correcting listings before the canonical value is settled**, which propagates an error and multiplies the cleanup.
- **Inferring GBP contents** from the website. No connector, no data.
- **Claiming a complete citation inventory.**
- **Normalising values while recording them**, which destroys the evidence of the inconsistency.
- **Treating cosmetic variants as errors** and burning the user's time on `&` versus `and`.
- **Correcting NAP on spam directories** instead of ignoring them.
- **Fixing directories before fixing the website and schema.**
- **Recommending a new listing without the legitimacy test** — a new inconsistent listing on a low-quality directory is a net negative.
- **Recording an edit as done because it was submitted.** Verify it live.
- **Creating, claiming, or editing anything.** Claude prepares the values and the steps; the user performs them.
