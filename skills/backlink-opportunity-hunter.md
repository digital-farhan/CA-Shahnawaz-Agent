# Skill: Backlink Opportunity Hunter

## Purpose

Continuously find *legitimate, obtainable* backlink opportunities relevant to a Mumbai CA/tax/compliance firm — local, professional, industry, resource-page, and unlinked-mention opportunities — then qualify and score them so the user receives a small, high-conviction, ready-to-act queue instead of a long list of domains nobody will ever contact.

This is one of the highest-value additions to the project, because a CA firm's realistic authority ceiling is set less by content volume than by whether it is genuinely present in Mumbai's professional, business, and industry ecosystem.

## Scope

**This skill owns:** discovery and qualification of *new* link opportunities across the five categories below, deduplication against the existing CRM, scoring via [off-page-governance](off-page-governance.md), and preparation of the pursue queue.

**This skill does NOT own:**
- Opportunities derived specifically from a competitor's backlink profile — [competitor-backlink-gap](competitor-backlink-gap.md).
- Opportunities based on a broken outbound link on someone else's page — [broken-link-building](broken-link-building.md).
- Recovering links the site already had — [backlink-reclamation](backlink-reclamation.md).
- Writing or sending outreach — [digital-pr-outreach](digital-pr-outreach.md) drafts it; the user sends it.
- Deciding whether the firm has an asset worth linking to — [linkable-content-planner](linkable-content-planner.md) and [digital-pr-link-assets](digital-pr-link-assets.md).
- NAP-bearing citation listings as a *consistency* problem — [local-citation-authority](local-citation-authority.md) owns NAP accuracy; this skill treats a directory as a link opportunity and hands the listing details there.
- The current backlink profile — [off-page-seo](off-page-seo.md).
- Scoring rules themselves — [off-page-governance](off-page-governance.md).

## When to use it

- Once a baseline exists from [off-page-seo](off-page-seo.md), so discovery is targeted at real gaps rather than generic link chasing.
- When priority service pages are shown to have zero external inbound links.
- On the recurring cycle defined in `automations/daily-backlink-hunt.md`.
- When a new linkable asset is published and needs a distribution list.

## Required Data

- Working web search and/or web fetch capability. **Without at least one of these, this skill cannot run** — discovery is entirely dependent on reaching the live web.
- `data/backlinks/backlink-master.csv` — to deduplicate against everything already discovered, contacted, or rejected.
- `data/backlinks/rejected-opportunities.md` — so previously rejected domains are not re-evaluated every cycle.
- CLAUDE.md's priority services and the Mumbai/CA business context, to judge relevance honestly.
- `data/crawl/service-coverage-map.md` — to know what the firm can actually credibly offer a publisher.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- Web search for prospect discovery using the query patterns below (if a search tool is verified live this session).
- Direct fetching of each candidate site to verify what it is, who it serves, whether it links out editorially, and whether a submission/contribution route exists.
- Direct verification of whether a candidate already links to cashahnawaz.com, and whether it links to competitors.
- Publicly stated contact routes on the candidate's own site (contact page, editorial email, submission form, listed editor).

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- Domain authority, domain rating, traffic volume, or traffic value for any prospect — no tool for this. Authority and Traffic dimensions are `PROXY-SCORED` per [off-page-governance](off-page-governance.md).
- Whether a site accepts guest contributions, unless it says so on its own pages. Do not infer it.
- Editorial calendars, staff email addresses not publicly published, or any private contact detail. **Never guess or pattern-construct an email address** (`firstname@domain`) — an unverified contact is `DATA NOT AVAILABLE`, and guessed contacts are how legitimate outreach becomes spam.
- Whether a prospect has been contacted outside this project (by the user or a previous agency) — ask the user rather than assuming the CRM is complete.

## Pre-Audit Checks

1. Verify search/fetch capability actually works this session before planning a discovery run.
2. Load the CRM and the rejected list; build the exclusion set of registrable domains already known.
3. Load [off-page-governance](off-page-governance.md) — the REJECT list, rate limiting, and duplicate/domain protections govern every step here.
4. Confirm with [off-page-seo](off-page-seo.md) which target pages most need links, so discovery is aimed at a purpose rather than at "more links."

## Step-by-Step Audit Process

### Step 1 — Set the target, not a quota

Start from the gap, not from a number. Identify the two or three priority service pages or topics that most need authority (from [off-page-seo](off-page-seo.md) and [seo-opportunity-mining](seo-opportunity-mining.md)), and hunt for opportunities that could plausibly point at *those*. Per [off-page-governance](off-page-governance.md), never set a volume target.

### Step 2 — Discover across the five categories

**A. Local (Mumbai) opportunities**
Mumbai business directories; local business associations; Mumbai professional organizations; business communities; startup communities; local publications and news sites; local blogs; local event websites; chambers of commerce and trade bodies; professional networking organizations.

Search patterns to use and adapt:
- `Mumbai business directory` / `Mumbai chartered accountant directory`
- `Mumbai chamber of commerce members`
- `Mumbai startup community` / `Mumbai SME association`
- `Mumbai business news submit` / `Andheri business association`
- `"Mumbai" "business resources" list`

**B. Accounting / finance / business publications**
Accounting and tax publications; finance blogs; business publications; CA and financial communities; entrepreneurship, startup and SME publications; finance-education websites.

- `India tax publication contributors` / `write for us accounting India`
- `GST blog India guest contributor`
- `Indian SME business magazine`
- `finance education India resources`

**C. Professional authority**
ICAI-related opportunities (branches, study circles, committees, member listings); professional associations; business organizations; conferences; webinars; podcasts; interviews; expert roundups; industry panels; professional directories.

- `ICAI Mumbai branch study circle`
- `chartered accountant podcast India guest`
- `tax expert roundup India`
- `finance conference Mumbai speakers`

These are frequently the **highest-value and most obtainable** category for a genuine CA firm, because eligibility is real: a qualified CA is genuinely entitled to a member listing, a study-circle contribution, or a panel seat. Relevance and editorial likelihood both score high, and the link is unimpeachable.

**D. Resource links**
Find pages that curate: helpful resources, tax resources, finance resources, Mumbai business resources, startup resources, SME resources, ITR resources, GST resources, accounting resources.

- `"tax resources" India links`
- `"helpful resources" startup India compliance`
- `"useful links" GST India`
- `startup incubator India resources page`

For each, apply the gate in Step 4 before treating it as an opportunity.

**E. Unlinked brand mentions**
Search brand variants: `"CA Shahnawaz"`, `"Shahnawaz and Associates"`, `"Shahnawaz & Associates"`, `"Shahnawaz Associates"`, plus the firm's phone number and office address as literal strings (address/phone searches surface directory listings that name the firm without linking it).

Verify each hit by fetching the page and confirming the mention is (a) genuinely about this firm and not a namesake, and (b) not already hyperlinked. Namesake confusion is a real and common failure here — confirm via corroborating detail (Mumbai, the specific address, CA context), and if the mention cannot be confirmed as this firm, record it as `NOT DETERMINED` and do not pursue it.

Hand confirmed unlinked mentions to [backlink-reclamation](backlink-reclamation.md), which owns the reclamation workflow.

### Step 3 — Deduplicate before spending analysis on anything

Normalise each candidate to its registrable domain and drop anything already present in the CRM (as prospect, contacted, live link, or rejected). Duplicate protection is a governance requirement, and re-contacting a prospect is the fastest way to burn a relationship.

### Step 4 — Qualify each survivor

Fetch the candidate and answer, from what is actually on the page:

1. **Is it real?** A genuine site with an audience, not an auto-generated page, scraped aggregator, or expired-domain shell. Anything failing here is `REJECT` under [off-page-governance](off-page-governance.md).
2. **Is it relevant?** To accounting, tax, finance, business, Mumbai, SMEs, startups, or professional services.
3. **Does it link out editorially at all?** If nothing on the site ever links externally, editorial likelihood is near zero regardless of how attractive the domain looks.
4. **Is there a real, legitimate route in?** A published submission process, a members' listing the firm actually qualifies for, a resource page that accepts suggestions, a stated contributor policy, a call for speakers.
5. **Does the firm genuinely deserve inclusion?** This is the honesty gate, and it is the one most often skipped. For a resource page, ask: does cashahnawaz.com actually have a resource good enough to belong on that list? If the answer is no, the correct output is **not** an outreach draft — it is a recommendation routed to [linkable-content-planner](linkable-content-planner.md) to build the asset first. Asking for a link to a page that does not merit it wastes the relationship and produces nothing.
6. **Does it carry risk?** Paid-link language ("submit your link $50"), sponsored-post farms, unrelated multilingual link dumps, casino/pharma adjacency → `REJECT`.

### Step 5 — Score

Apply the 100-point rubric in [off-page-governance](off-page-governance.md) in full, with per-dimension confidence and `PROXY-SCORED` flags where authority/traffic could not be measured. Bands: A/HIGH ≥85, B/MEDIUM 70–84, C/LOW 50–69, REJECT <50.

### Step 6 — Record and prepare

Write every qualified prospect to `data/backlinks/backlink-master.csv` with `status = prospect`, its score, the evidence URL, the proposed target URL on cashahnawaz.com, and the publicly listed contact route (or `DATA NOT AVAILABLE`). Log rejections with reasons to `data/backlinks/rejected-opportunities.md`.

Then stop. Preparing the queue is where this skill ends — outreach drafting is [digital-pr-outreach](digital-pr-outreach.md), and **sending is the user's manual action only**, per CLAUDE.md's Implementation Policy and the approval-gate matrix in [off-page-governance](off-page-governance.md). This includes directory submissions and listing claims: Claude produces the exact field values to submit, never the submission itself.

## What Checks to Perform

- [ ] Discovery targeted at specific pages/topics that need authority, not at a link count
- [ ] All five categories (A–E) covered, or the skipped ones stated with a reason
- [ ] Every candidate deduplicated on registrable domain against the CRM and the rejected list
- [ ] Every surviving candidate fetched and verified live — never scored from a search snippet
- [ ] Namesake check performed on every brand mention before it is treated as this firm
- [ ] "Does the firm genuinely deserve inclusion?" answered explicitly per resource-page opportunity
- [ ] REJECT list from [off-page-governance](off-page-governance.md) applied before scoring
- [ ] Every qualified prospect scored with confidence and `PROXY-SCORED` flags
- [ ] Contact routes recorded only where publicly published — none guessed or constructed
- [ ] CRM and rejection log updated; rate limit on new prospects respected

## How to Identify Issues

The "issue" this skill surfaces is an authority gap with a named, evidenced, obtainable route to closing it. A valid opportunity has all four of: genuine topical or local relevance; a real editorial or eligibility route in; a page on cashahnawaz.com that plausibly deserves the link; and no manipulation requirement. Missing any one of these makes it an opportunity to *reject* or *defer*, and saying so is a legitimate output — an honest "no qualified opportunities found this cycle" beats a padded list.

## Evidence to Collect

Save to `data/backlinks/`:
- `backlink-master.csv` — the CRM, updated with new prospects.
- `opportunity-hunt-YYYY-MM-DD.md` — the cycle log: queries run, candidates found, candidates rejected and why, prospects promoted. This is the audit trail required by [off-page-governance](off-page-governance.md).
- `rejected-opportunities.md` — running list, so rejected domains are never re-analysed.
- `unlinked-brand-mentions.md` — confirmed mentions with quoted text and date.
- For every promoted prospect: the specific URL that proves the opportunity exists (the actual resource page, the actual members' page, the actual call for contributors) — never just the homepage.

## How to Prioritize Issues

Prioritize by the [off-page-governance](off-page-governance.md) band, then break ties by:

1. **Eligibility-based opportunities first** (professional bodies, ICAI-related listings, legitimate local associations) — the firm qualifies by right, so the acceptance probability is highest and the link is defensible.
2. **Unlinked mentions second** — the publisher already chose to name the firm.
3. **Resource pages where a genuinely deserving asset already exists** third.
4. **Opportunities requiring a new asset to be built** last — these are real, but they are a content project ([linkable-content-planner](linkable-content-planner.md)) before they are a link project.

Weight toward opportunities that can point at an under-linked priority service page rather than the homepage.

## Implementation Recommendations

Every item below is prepared for the user to execute manually.

- **Directory / association / professional listing:** supply the exact listing URL, the submission or membership route as published, and the precise field values to enter — business name, address, phone, website, category, description — taken verbatim from the canonical NAP record maintained by [local-citation-authority](local-citation-authority.md) so the new listing does not introduce an inconsistency. State the "before" state where a listing already exists (governance requirement 8).
- **Resource page inclusion:** supply the target page URL, the specific resource being proposed, one sentence on why it belongs on that list, and the published contact route. [digital-pr-outreach](digital-pr-outreach.md) drafts the message.
- **Professional/PR opportunity:** supply the opportunity URL, the deadline if published, what the firm would contribute, and which credential makes the firm eligible.
- **Where the firm does not yet deserve the link:** the deliverable is a content recommendation, not an outreach draft. Name the asset that would need to exist and route it.

## How to Validate Fixes

- **Prospect quality:** re-fetch a sample of promoted prospects and confirm each still meets the qualification gate — sites change, resource pages get retired.
- **Placement:** after the user has acted and a link is claimed, verify by fetching the live page and reading the anchor, `rel`, and placement. A reported link is not a link until it is observed.
- **Pipeline health:** track acceptance rate per category in the CRM. If a category consistently produces no placements, stop hunting it — that is a genuine finding about where this firm's authority is actually winnable.
- **Business impact:** rankings/traffic for the specific linked target pages via [gsc-analysis](gsc-analysis.md) / [ga4-analysis](ga4-analysis.md), if and when available. Attribution here is directional, never causal from a single link.

## Expected Output Format

A per-cycle opportunity report containing:

1. **Cycle header** — date, capability verified, categories hunted, exclusion-set size.
2. **Qualified prospect table:**

   | # | Domain | Opportunity type | Proposed target URL | Score | Band | Confidence | Route in | Evidence URL |
   |---|---|---|---|---|---|---|---|---|

3. **Rejections summary** — count by reason (spam, irrelevant, no route in, firm does not deserve inclusion, duplicate).
4. **"Asset needed first" list** — opportunities blocked on content, routed to [linkable-content-planner](linkable-content-planner.md).
5. **Awaiting-approval queue** — what is prepared and what the user would need to do manually, with the reminder that no contact has been or will be made by Claude.
6. Any finding worth escalating (e.g., "8 of 9 competitor-held association listings are ones this firm qualifies for") written in the standard CLAUDE.md finding template.

## Common Mistakes to Avoid

- **Producing volume instead of conviction.** Forty unqualified domains is worse than four verified ones, because it hides the good ones and burns the user's review time.
- **Scoring from search snippets.** If the page was not fetched, it was not qualified.
- **Guessing an email address.** Pattern-constructed contacts turn legitimate outreach into spam; unpublished contact detail is `DATA NOT AVAILABLE`.
- **Skipping the "do we deserve this link?" gate**, then producing an outreach draft asking a curator to link to a thin page. This is the single most common failure mode in link building and it damages the relationship permanently.
- **Treating a namesake mention as the firm's** without corroborating Mumbai/CA/address detail.
- **Confusing a directory link opportunity with a NAP citation.** Both matter, but the NAP values must come from [local-citation-authority](local-citation-authority.md)'s canonical record, or the "win" creates an entity inconsistency.
- **Re-surfacing previously rejected domains** each cycle because the rejection log was not consulted.
- **Chasing an attractive-looking domain with no editorial route in** — a site that never links out will not start for this firm.
- **Drifting toward "easy" opportunities** (open-submission link lists, low-moderation directories) that sit close to the REJECT line. Easy is usually a signal, not a bargain.
- **Acting.** Claude does not submit, register, claim, or contact. It prepares and hands over.
