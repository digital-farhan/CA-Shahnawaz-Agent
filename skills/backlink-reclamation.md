# Skill: Backlink Reclamation

## Purpose

Recover authority the site has already earned but is not receiving — links pointing at 404s, old URLs, HTTP or non-canonical variants, deleted pages, and brand mentions that were never hyperlinked. Reclamation is the highest-return work in off-page SEO: the publisher has already made the editorial decision, so there is nothing to persuade, only something to fix.

## Scope

**This skill owns:** identifying recoverable links and mentions, diagnosing why each is not delivering value, and producing the recommended action (301 redirect, content restoration, publisher contact, URL replacement request, mention conversion, information correction).

**This skill does NOT own:**
- The overall backlink profile picture — [off-page-seo](off-page-seo.md), which *identifies* broken/lost links as a profile characteristic and hands them here for recovery.
- Finding new links — [backlink-opportunity-hunter](backlink-opportunity-hunter.md).
- Broken links on *other people's* sites pointing at *third parties* — [broken-link-building](broken-link-building.md). This skill is about links pointing at **this** site.
- Implementing the redirect or restoring the page — the user does that manually.
- The general redirect/canonical configuration — [technical-seo](technical-seo.md).
- Drafting standards for publisher messages — [digital-pr-outreach](digital-pr-outreach.md), whose rules this skill follows.
- NAP corrections in directories — [local-citation-authority](local-citation-authority.md), though incorrect business information found here routes there.

## When to use it

- Immediately after [off-page-seo](off-page-seo.md) surfaces links with broken, redirected, or non-canonical targets — this is the fastest available authority win and should precede new link building.
- After any site migration, URL restructure, redesign, or plugin/permalink change.
- When pages have been deleted or consolidated.
- On the recurring cycle, to catch newly broken targets and newly published unlinked mentions.

## Required Data

- Known inbound links from `data/backlinks/backlink-master.csv` and any GSC Links report data.
- The live site, to verify what each linked-to URL actually does now.
- Historical URL knowledge: old permalink structures, deleted pages, prior site versions. Where the project has no record, the user is the source.
- `data/crawl/` inventory and sitemaps, to identify the correct replacement target for each dead URL.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- **Direct verification of every link target** by fetching it: does it 200, 404, redirect, or resolve to a non-canonical variant? This works with no backlink tool and produces `CONFIRMED`-grade evidence.
- **Direct verification of the linking page**: does the link still exist, what is its anchor, is it in-content?
- GSC's Coverage/Pages and Links reports, if GSC access is verified live — the best available source for URLs that once existed and now 404.
- Brand-mention discovery via web search, verified by fetching each page.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **A complete list of lost backlinks.** Detecting a *lost* link requires knowing it once existed, which requires either a backlink tool with history or a prior snapshot from this project. Per `reports/00-capability-check.md`, no backlink tool was available at the last verified check. Without one, lost-link analysis begins only once `data/backlinks/snapshots/` holds at least two dated snapshots — state this rather than implying the recovery list is complete.
- The value of any recovered link — no metric available.
- Why a publisher removed a link — unknowable unless they say so; do not speculate in a finding.
- Archived copies of removed content, unless the user supplies them or they are genuinely retrievable — never reconstruct a "restored" page from imagination.
- Whether a 404ing URL ever existed, if there is no record of it. An inbound link to a URL is evidence someone once pointed there; it is not proof of what was on it.

## Pre-Audit Checks

1. Confirm the canonical host and protocol form from [technical-seo](technical-seo.md), since "non-canonical target" is undefined without it.
2. Load the known-link inventory and any prior snapshots; declare whether lost-link detection is possible this session.
3. Load [off-page-governance](off-page-governance.md) and [digital-pr-outreach](digital-pr-outreach.md) — any publisher contact follows their rules and is sent by the user, never by Claude.
4. Establish the replacement-target map: for each likely dead URL, which live page is the genuine equivalent.

## Step-by-Step Audit Process

### Step 1 — Classify every recoverable item

Work through the six categories from the specification, verifying each by direct fetch:

| Category | Test | Typical action |
|---|---|---|
| **Broken backlinks** | Linking page is gone or no longer contains the link | Usually unrecoverable; record and close |
| **Links to 404 pages** | Target returns a 404 / error page | **301 redirect** to the closest equivalent live page |
| **Links to old URLs** | Target is a superseded permalink | **301 redirect** |
| **Links to deleted pages** | Target existed, content removed | **Restore content** or **301** — see Step 3 |
| **Links to HTTP versions** | Target uses `http://` | Site-wide HTTPS enforcement ([technical-seo](technical-seo.md)); optionally a correction request for high-value links |
| **Links to redirected URLs** | Target 301s to the live page | Working already — correction request only if the link is genuinely valuable |
| **Links to non-canonical URLs** | Target is a `www`/non-`www`/parameterised variant | Canonicalization fix; correction request for high-value links |
| **Unlinked brand mentions** | Firm named in text, no hyperlink | **Mention conversion** request |
| **Incorrect business information** | Wrong address, phone, name, or credentials published | **Correction request**; route to [local-citation-authority](local-citation-authority.md) |
| **Incorrect anchor text** | Anchor is wrong or misleading, where correction is appropriate | Correction request — only where genuinely warranted |

### Step 2 — Verify both ends of every item

Never act on a report. For each item, fetch the **linking page** (does the link still exist, with what anchor and placement?) and the **target URL** (what does it actually return now?). Record both observations with the date. An item that fails verification at either end is not a reclamation opportunity.

### Step 3 — Choose the right action, not the easy one

- **301 redirect** — where a genuinely equivalent live page exists. The redirect must go to the *closest topical match*, not the homepage. A redirect to an unrelated page is treated as a soft 404 and recovers nothing, so a homepage catch-all is not a reclamation strategy.
- **Content restoration** — where the linked resource was genuinely useful and no equivalent exists. This is often the better recommendation for a page that earned links: the links exist because the content had value, and redirecting them to a thin service page throws that away. Route to [content-decay-refresh](content-decay-refresh.md) / [digital-pr-link-assets](digital-pr-link-assets.md) for the rebuild spec.
- **Publisher contact** — for high-value links only, where an on-site fix cannot solve it (e.g., they linked to a competitor's version, or the information about the firm is wrong).
- **URL replacement request** — ask the publisher to update the URL. Justified mainly where the link is valuable and a redirect is not possible.
- **Brand mention conversion** — ask that an existing mention be linked. The highest-acceptance request type available, because it asks for a small change to something they already chose to publish.
- **No action** — many broken backlinks are on dead sites, spam pages, or scrapers. Recovering a link from a spam site is not a win; record and close.

**Prefer the on-site fix over the outreach ask every time.** A 301 the user controls is faster, more reliable and imposes on nobody; contacting a publisher spends relationship capital that should be saved for cases where nothing else works.

### Step 4 — Prioritise by value recovered per unit of effort

Rank by: relevance and quality of the linking domain × whether the target is a priority commercial page × how cheap the fix is. A single 301 that reclaims several links from relevant domains to a priority service page is the best work available in this entire skill set.

### Step 5 — Prepare, hand over, and stop

For on-site actions, write the exact manual steps. For contact actions, prepare the draft per [digital-pr-outreach](digital-pr-outreach.md), marked `DRAFT — FOR USER TO SEND`. **Claude never implements a redirect, never restores a page, and never contacts a publisher** — including for "trivial" corrections.

## What Checks to Perform

- [ ] Lost-link detection capability declared (tool / snapshots / not possible this session)
- [ ] Every item verified at both ends by direct fetch, with dates recorded
- [ ] Each item classified into one of the categories above
- [ ] Replacement target identified per dead URL, and confirmed to be a genuine topical equivalent
- [ ] "Restore vs. redirect" decided deliberately for every deleted page that had earned links
- [ ] Homepage catch-all redirects explicitly rejected
- [ ] Spam/dead-source items recorded and closed, not pursued
- [ ] Publisher contact reserved for cases an on-site fix cannot solve
- [ ] Incorrect business information routed to [local-citation-authority](local-citation-authority.md)
- [ ] All drafts marked as user-to-send; nothing sent by Claude
- [ ] CRM updated with status per item

## How to Identify Issues

A reclamation finding requires proof at both ends: a verified inbound link, and a verified defect in what it reaches. The strongest version — and the one to lead with — is a relevant, quality domain linking to a 404 where a genuinely equivalent live page exists, because the fix is a single redirect the user fully controls. Unlinked mentions on relevant, reachable publishers are the strongest *outreach*-based finding, for the same reason: the editorial decision has already been made.

## Evidence to Collect

Save to `data/backlinks/`:
- `reclamation-YYYY-MM-DD.md` — full item list with both-end verification, classification, chosen action, and rationale.
- `reclamation-queue.csv` — source URL, anchor, target URL, observed target status, action, priority, status.
- `broken-and-noncanonical-targets.md` — kept in sync with [off-page-seo](off-page-seo.md).
- `unlinked-brand-mentions.md` — URL, quoted mention text, whether confirmed as this firm, date.
- Updated `backlink-master.csv` rows.
- For each item, the quoted sentence containing the link or mention, so placement and context are evidenced.

## How to Prioritize Issues

- **CRITICAL** — multiple links from relevant, quality domains pointing at 404s, especially where the intended target was a priority service page. Authority is being actively discarded and the fix is cheap.
- **HIGH** — a valuable link to a deleted page that genuinely warrants restoration; confirmed unlinked mentions on relevant publishers; incorrect business information published on a visible site (this harms entity consistency and trust, not just links).
- **MEDIUM** — links to redirected or non-canonical URLs where the on-site canonicalization fix is already recommended; HTTP-version links.
- **LOW** — cosmetic anchor corrections; low-value directory links.
- **Closed, not a finding** — broken links from dead, spam, or scraper sources.

## Implementation Recommendations

Manual steps for the user, per CLAUDE.md's Implementation Policy.

- **301 redirect (Rank Math):** WordPress Admin → Rank Math → Redirections → Add New. Source URL = the old path exactly as linked (check whether it includes a trailing slash or query string); Destination = the full live equivalent URL; Redirection Type = **301 Permanent**; Status = Active; Save. Repeat per dead URL. Note the Redirections module must be enabled under Rank Math → Dashboard → Modules.
- **Verify no conflict** with an existing redirect rule or a `.htaccess` rule before adding, so chains are not created. Where the site has server-level redirects, flag that the user should check both layers.
- **Content restoration:** supply the rebuild specification (topic, sources, author, schema, target URL — reusing the *original* URL wherever possible so existing links resolve without a redirect at all).
- **Publisher contact:** supply the draft, the published contact route, and the specific evidence, per [digital-pr-outreach](digital-pr-outreach.md).
- **Incorrect information:** supply the correct values verbatim from the canonical NAP record in [local-citation-authority](local-citation-authority.md), so the correction does not introduce a new inconsistency.
- Record the **current state before any change is requested** (governance requirement 8), so the user can revert.

## How to Validate Fixes

- **Redirects:** after the user implements, fetch the old URL and confirm it lands on the intended page; confirm there is exactly one hop, not a chain. Re-check a sample a week later — plugin and permalink changes silently break redirects.
- **Restored content:** confirm the URL returns the content, is indexable, and carries author, sources and last-updated date.
- **Mention conversion / corrections:** fetch the page and confirm the link or corrected detail is present, recording anchor and `rel`. Never mark it done on the strength of a reply promising it.
- **Profile-level:** confirm the item disappears from the broken-target list on the next cycle, and update `backlink-master.csv` (`status = recovered`, dated).
- **Business-level:** rankings and organic performance for the recovered target pages via [gsc-analysis](gsc-analysis.md) if available, reported as correlation over months.

## Expected Output Format

1. **Capability header**, e.g.:

   > Lost-link detection is not possible this session: no backlink tool was available (verified) and `data/backlinks/snapshots/` contains only one snapshot. The items below are links verified individually by direct fetch. This is a recovery list, not a complete lost-link inventory.

2. **Reclamation table:**

   | # | Linking page | Anchor | Target URL | Observed status | Category | Action | Priority | Status |
   |---|---|---|---|---|---|---|---|---|

3. **Redirect map** — old URL → new URL, ready for the user to enter, with the rationale for each destination choice.
4. **Restore-instead list** — pages worth rebuilding rather than redirecting, with reasons.
5. **Draft messages** for contact-based items, marked `DRAFT — FOR USER TO SEND`.
6. **Closed items** with reasons.
7. Findings in the standard CLAUDE.md template with Confidence Level and Evidence Source.

## Common Mistakes to Avoid

- **Redirecting everything to the homepage.** It is treated as a soft 404, recovers little, and hides the problem.
- **Redirecting a page that should be restored.** If the content earned links, the content had value; a redirect to a thin page discards it.
- **Reporting lost links without a baseline.** Without a tool or two snapshots, "links lost" is not measurable — say so.
- **Acting on a reported link without verifying both ends.** Links get removed, pages change, reports go stale.
- **Contacting a publisher when a redirect would have solved it.** Spend relationship capital only when nothing else works.
- **Pursuing broken links from spam or scraper sources** — recovering those is not a win.
- **Creating redirect chains** by not checking for an existing rule first.
- **Ignoring incorrect business information** because it is "not a link issue." Wrong NAP data on a visible third-party site harms local and entity authority directly.
- **Requesting an anchor change with a commercial exact-match anchor** — that converts a legitimate correction into anchor manipulation, which [off-page-governance](off-page-governance.md) prohibits.
- **Marking anything recovered on the basis of a promise.** Verify by fetching the page.
