# Skill: Off-Page SEO Audit

## Purpose

Establish what cashahnawaz.com's off-site authority profile actually looks like — which domains link to it, with what anchors, to which pages, in what placement, and whether that profile is healthy, thin, or risky for a Mumbai CA/tax firm competing in a YMYL category. Off-page authority is the most common reason a technically sound, well-written service page still cannot outrank an established competitor, so this skill exists to replace "we probably need more backlinks" with an evidence-based picture.

## Scope

**This skill owns:** the *current state* of the backlink and brand-mention profile — inventory, composition, distribution, and the structural problems visible within it (links to 404s, links to non-canonical URLs, links to HTTP, anchor over-optimization, lost/broken links as a profile characteristic).

**This skill does NOT own:**
- Finding *new* link opportunities — [backlink-opportunity-hunter](backlink-opportunity-hunter.md).
- Competitor referring-domain comparison — [competitor-backlink-gap](competitor-backlink-gap.md).
- Recovering specific lost/broken links — [backlink-reclamation](backlink-reclamation.md) owns the recovery workflow; this skill only *identifies* that they exist as a profile issue.
- Classifying individual links SAFE/WATCH/RISK and monitoring for spam attacks — [backlink-risk-monitor](backlink-risk-monitor.md).
- NAP/citation consistency — [local-citation-authority](local-citation-authority.md).
- Brand entity footprint beyond links — [entity-seo](entity-seo.md).
- Scoring or pursuing anything — [off-page-governance](off-page-governance.md) owns scoring; pursuit is user-executed.
- Internal links — [internal-linking](internal-linking.md). This skill is external inbound links only.
- Fixing a 404 or canonical problem that inbound links expose — that is [technical-seo](technical-seo.md)'s fix; this skill supplies the "and external links are pointing at it" evidence that raises its severity.

## When to use it

- Before any link-building or digital-PR work begins — you cannot identify a gap without a baseline.
- When a priority service page has solid on-page and content scores ([on-page-seo](on-page-seo.md), [content-audit](content-audit.md)) but still does not rank.
- After a site migration, URL change, or redesign, where inbound equity is commonly lost silently.
- On a recurring cycle, to detect new/lost links and anchor drift.

## Required Data

- A verified backlink data source. **This is the binding constraint on this entire skill** — see limitations below.
- The live site, for confirming what inbound links actually resolve to (404, redirect, canonical target).
- `data/crawl/priority-urls.md` and `data/crawl/service-coverage-map.md` — to judge whether links point at commercially important pages or only the homepage.
- `data/backlinks/backlink-master.csv` — the running CRM/inventory this skill maintains.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- **A third-party backlink tool** (Ahrefs, Semrush, Majestic, Moz, or similar), *if* one is genuinely connected and run this session. This is the only source for totals, referring domains, referring IPs, historical new/lost links, and quality metrics.
- **GSC Links report**, *if* GSC access is verified live this session — gives top linking sites, top linked pages, and top anchor text for the property. It is first-party, free, and sample-limited, but it is real data.
- **Direct page verification via WebFetch** — for any candidate linking URL, fetch it and confirm the link exists, its anchor text, its `rel` attributes where visible, and its placement in the page. This works without any backlink tool and produces `CONFIRMED`-grade evidence, one URL at a time.
- **Live-site verification of link targets** — fetch each linked-to URL to determine whether it 200s, 404s, redirects, or is non-canonical.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- Per `reports/00-capability-check.md`, the last verified capability check found **no backlink-data tool and no GSC connector** available. Under those conditions the following are all `DATA NOT AVAILABLE` and must be reported as such:
  - Total backlinks; referring domains; referring IPs
  - Follow / nofollow / sponsored / UGC distribution across the profile
  - Domain authority or quality scores of any kind
  - New and lost backlinks over time
  - Full anchor text distribution
  - Historical trend of any of the above
- **Do not substitute a manual sample for a profile total.** If five linking pages were verified by hand, that is "5 links confirmed by direct observation," never "the site has 5 backlinks." The distinction is the difference between evidence and a fabricated metric.
- Competitor backlink profiles — same constraint; see [competitor-backlink-gap](competitor-backlink-gap.md).
- Any claim that a link "passes authority" or "is worth X" — not measurable with any tool available here.

## Pre-Audit Checks

1. **Verify the data source before writing anything.** Attempt the backlink tool and/or GSC pull. Record in `reports/00-capability-check.md` (or the session's capability note) what was actually available. Do not carry a prior session's answer forward.
2. **Decide and declare the audit mode** at the top of the output:
   - **Mode A — Tool-backed:** a backlink source was verified live. Full profile analysis is possible.
   - **Mode B — Observation-only:** no backlink source. The audit is limited to directly verified linking pages, GSC-free brand-mention discovery, and structural checks on link targets. Every quantitative profile statement is `DATA NOT AVAILABLE`.
3. Confirm the canonical domain form and redirect behaviour from [technical-seo](technical-seo.md) findings, since "links pointing to non-canonical URLs" is meaningless without knowing which form is canonical.
4. Load [off-page-governance](off-page-governance.md) — the prohibited-tactics list and data-honesty rules apply throughout.

## Step-by-Step Audit Process

1. **Establish the inventory.** In Mode A, export the full backlink list and load it into `data/backlinks/backlink-master.csv` using the standard field set. In Mode B, build the inventory incrementally from directly verified linking pages, unlinked mention discovery, and any links surfaced by [competitor-backlink-gap](competitor-backlink-gap.md) work — and mark the inventory explicitly as a partial, observation-built sample, not a profile.

2. **Profile composition.** Where data exists, characterise:
   - Total backlinks vs. referring domains (a high ratio of links to domains means a few sites linking many times — usually sitewide footer/template links, which are worth far less than the raw count suggests).
   - Referring IPs vs. referring domains (many domains on one IP is a footprint signal — route to [backlink-risk-monitor](backlink-risk-monitor.md)).
   - `rel` distribution: follow / nofollow / sponsored / UGC.
   - Link type: editorial in-content, directory listing, profile page, comment, footer/sitewide, image.

3. **Relevance and placement assessment.** For every linking domain that matters, judge two things that no tool scores well:
   - **Topical relevance** — is this an accounting/tax/finance/business/Mumbai/SME/startup/professional-services site, or an unrelated site that happens to link? Relevance is the single largest scoring dimension in [off-page-governance](off-page-governance.md) for a reason.
   - **Placement** — is the link inside body content a reader would actually encounter, or buried in a footer, sidebar, author box, or link dump? Record the observed placement, not an assumption.

4. **Target URL distribution.** Map links to the pages they point at, then compare against `data/crawl/priority-urls.md`. The typical pattern for a firm like this is heavy homepage concentration with priority service pages (ITR filing, GST registration, company registration, NRI taxation) holding zero external links. Quantify how many priority service pages have **no** inbound external links at all — this is usually the single most actionable output of the skill.

5. **Anchor text analysis.** Categorise every known anchor into exactly one bucket:

   | Category | Example |
   |---|---|
   | Brand | `Shahnawaz & Associates`, `CA Shahnawaz` |
   | Naked URL | `cashahnawaz.com`, `https://cashahnawaz.com/` |
   | Generic | `click here`, `read more`, `website`, `visit site` |
   | Partial match | `Mumbai CA firm for GST help` |
   | Exact match | `GST registration Mumbai` |
   | Service | `income tax return filing` |
   | Location | `Mumbai`, `Andheri` |
   | Long-tail | a full descriptive sentence fragment used as the anchor |
   | Other | image links with no alt-derived anchor, emoji, punctuation-only |

   Then check for **over-optimization**. A natural profile for a professional-services firm is dominated by brand and naked-URL anchors, because that is how people actually cite a firm. Treat a high commercial exact-match share as a risk signal warranting investigation — and state the observed percentage alongside the count it was derived from, since a percentage over a tiny sample is noise. **Never manufacture an exact-match anchor profile** ([off-page-governance](off-page-governance.md) prohibits it); the fix for over-optimization is diversification and, where warranted, correction requests, never more exact-match links.

6. **Structural problems in the inbound profile.** For each known linking URL, verify the *target* resolves correctly:
   - **Links to 404 pages** — inbound equity landing on nothing. Highest-value structural fix available in off-page work; route to [backlink-reclamation](backlink-reclamation.md).
   - **Links to redirected URLs** — working but with an extra hop; worth a correction request only when the link is genuinely valuable.
   - **Links to non-canonical URLs** — e.g., a `www`/non-`www` or `http`/`https` variant, or a URL with tracking parameters, where the canonical is a different URL.
   - **Links to HTTP versions** — same treatment.
   - **Broken backlinks** — the linking page itself is now gone.

7. **Brand mentions without links.** Identify places the firm is named in text but not linked. These are the highest-conversion reclamation opportunities because the publisher has already chosen to mention the firm. Hand the list to [backlink-reclamation](backlink-reclamation.md) for the outreach draft and to [entity-seo](entity-seo.md) for entity-consistency checking.

8. **New and lost links.** Only possible with a tool or with dated snapshots this project has built up over time. Where snapshots exist in `data/backlinks/`, diff the current inventory against the previous one and report additions and removals with dates. Where they do not, state that trend analysis begins once a second snapshot exists.

9. **Hand off, do not fix.** Every issue found here routes somewhere: reclamation to [backlink-reclamation](backlink-reclamation.md), risk to [backlink-risk-monitor](backlink-risk-monitor.md), gaps to [backlink-opportunity-hunter](backlink-opportunity-hunter.md), on-site causes (404s, canonical/redirect config) to [technical-seo](technical-seo.md). Claude never contacts a publisher and never changes the site.

## What Checks to Perform

- [ ] Data source verified live this session, and audit mode (A/B) declared in the output
- [ ] Inventory recorded in `data/backlinks/backlink-master.csv`, with sample-vs-complete status stated
- [ ] Links-to-domains ratio examined (sitewide/template link inflation identified)
- [ ] `rel` distribution recorded where available
- [ ] Topical relevance judged per referring domain
- [ ] Link placement recorded per verified link
- [ ] Target URL distribution mapped against priority service pages
- [ ] Count of priority service pages with zero external inbound links
- [ ] Anchors categorised into the nine buckets; exact-match share stated with its denominator
- [ ] Every known link target checked for 404 / redirect / non-canonical / HTTP
- [ ] Unlinked brand mentions listed
- [ ] New vs. lost links diffed against the prior snapshot, or trend explicitly deferred
- [ ] Nothing quantitative asserted that a tool did not actually return

## How to Identify Issues

An off-page issue exists where the profile's *composition* works against the business, not merely where the count is low. Concretely: commercially critical pages with no inbound links while the homepage holds most of them; inbound links landing on 404s or non-canonical URLs; anchor distribution skewed toward commercial exact-match; a referring-domain set with little topical or local relevance; or a profile whose growth comes from domains that fail the relevance test in [off-page-governance](off-page-governance.md). A thin profile with clean composition is an OPPORTUNITY; a profile with links being wasted on broken targets is a defect.

## Evidence to Collect

Save to `data/backlinks/`:
- `backlink-master.csv` — the running inventory (field definitions in `data/backlinks/README.md`).
- `snapshots/backlink-master-YYYY-MM-DD.csv` — dated snapshot each cycle, so new/lost analysis becomes possible.
- `anchor-distribution-YYYY-MM-DD.md` — anchor buckets with counts, percentages, and the denominator.
- `target-url-distribution-YYYY-MM-DD.md` — links per target URL, joined to priority-page status.
- `broken-and-noncanonical-targets.md` — every inbound link whose target 404s, redirects, or is non-canonical, with the verified live status of each target.
- `unlinked-brand-mentions.md` — URL, quoted mention text, date observed.
- For each directly verified link, quote the surrounding sentence so placement is evidenced rather than asserted.

## How to Prioritize Issues

- **CRITICAL** — inbound links from genuinely valuable, relevant domains pointing at 404s (equity actively being discarded), or evidence of an active spam/negative-SEO link attack (hand immediately to [backlink-risk-monitor](backlink-risk-monitor.md)).
- **HIGH** — priority commercial service pages with zero external inbound links while competitors demonstrably have them; anchor profile skewed toward commercial exact-match; significant links pointing to non-canonical or HTTP URLs.
- **MEDIUM** — valuable links landing on redirects; heavy homepage-only concentration; unlinked brand mentions on relevant, reachable publishers.
- **LOW** — cosmetic anchor issues; low-value directory duplication.
- **OPPORTUNITY** — a thin but clean profile in a category where competitors are also thin, i.e., authority is winnable.

Weight by the affected page's commercial value: a structural link problem on the GST registration page outranks the same problem on a blog post, because CLAUDE.md's success journey runs through the service pages.

## Implementation Recommendations

All recommendations are written for the user to perform manually, per CLAUDE.md's Implementation Policy.

- **Links to 404s:** recommend a 301 from the dead URL to the closest genuinely equivalent live page, implemented via Rank Math's Redirections module (WordPress → Rank Math → Redirections → Add New; source = old path, destination = live URL, type 301). Never redirect to the homepage as a default — an irrelevant redirect is treated as a soft 404. Where no equivalent page exists, the better recommendation is to restore or rebuild the resource ([content-decay-refresh](content-decay-refresh.md)).
- **Links to non-canonical/HTTP URLs:** the on-site fix (correct canonicalization, forced HTTPS, single canonical host) belongs to [technical-seo](technical-seo.md); this skill supplies the evidence that external links make the fix urgent. A correction request to the publisher is a *secondary* step, and only for high-value links.
- **Priority pages with no inbound links:** route to [linkable-content-planner](linkable-content-planner.md) and [backlink-opportunity-hunter](backlink-opportunity-hunter.md) — the honest answer is usually that the page is not currently link-worthy, and making it link-worthy precedes asking anyone to link to it.
- **Anchor over-optimization:** diversify future anchors toward brand and natural-language forms; where a specific manipulated anchor is identified on a controllable property, prepare a correction request for the user to send.

## How to Validate Fixes

- **Redirect fixes:** after the user implements, re-fetch the old URL and confirm it resolves to the intended live page; confirm in GSC's URL Inspection (if available) that the target is indexable.
- **Canonical/HTTPS fixes:** re-fetch the previously non-canonical inbound target and confirm it now resolves to the canonical form.
- **New links:** confirm by fetching the live linking page and reading the anchor and `rel` — not by trusting a report that it was placed.
- **Profile-level change:** compare the next dated snapshot in `data/backlinks/snapshots/` against the current one. Meaningful validation here is measured in months, not days; do not claim authority improvement from a single cycle.
- **Business-level validation:** rankings and organic enquiries for the specific target pages, via [gsc-analysis](gsc-analysis.md) and [ga4-analysis](ga4-analysis.md) if and when those become available.

## Expected Output Format

Findings use the standard CLAUDE.md template (Issue / Severity / Evidence / Affected URLs / SEO Impact / Likely Root Cause / Recommended Fix / Manual Implementation Guide / Validation), plus **Confidence Level** and **Evidence Source**.

Open the report with a mode-and-limits header, for example:

> **Audit mode:** B — Observation-only. No backlink-data tool and no GSC connector were available this session (verified, not assumed). All profile totals, referring-domain counts, `rel` distribution, and historical trend data are `DATA NOT AVAILABLE`. Findings below rest on N linking pages verified individually by direct fetch, and are a sample, not a profile.

Then:
1. Profile composition table (or the `DATA NOT AVAILABLE` statement per row).
2. Anchor distribution table with counts, percentage, and denominator.
3. Target URL distribution, flagging priority pages with zero external links.
4. Structural defects table: inbound link → target → observed status (404 / redirect / non-canonical / HTTP / OK).
5. Unlinked brand mentions list.
6. Findings in template form.
7. Routing list: which finding went to which skill.

## Common Mistakes to Avoid

- **Reporting a hand-verified sample as a profile total.** "We confirmed 6 links" is not "the site has 6 backlinks," and the second statement is a fabricated metric.
- **Quoting DA/DR or traffic numbers** for referring domains when no tool produced them. Score authority as `PROXY-SCORED` per [off-page-governance](off-page-governance.md) instead.
- **Computing an anchor percentage over a handful of links and presenting it as a distribution.** Always state the denominator; a 33% exact-match share over 3 links is not a finding.
- **Counting links instead of referring domains.** Fifty sitewide footer links from one directory is one domain's worth of signal, not fifty.
- **Treating every nofollow as worthless** — a relevant, trafficked, nofollowed mention on a real publication still drives qualified visitors and entity recognition, both of which sit on CLAUDE.md's success journey.
- **Recommending disavow.** It is rarely appropriate, it is irreversible in practice, and it is a live GSC action Claude cannot take here regardless. Route genuine attack evidence to [backlink-risk-monitor](backlink-risk-monitor.md) and let the user decide with full evidence in hand.
- **Blanket-redirecting dead linked URLs to the homepage** — Google treats an irrelevant redirect as a soft 404, so the equity is lost anyway and the audit trail is muddied.
- **Diagnosing "not enough backlinks" as the cause of a ranking problem** before [on-page-seo](on-page-seo.md), [content-audit](content-audit.md), and [technical-seo](technical-seo.md) have been cleared. Authority is the usual suspect, but it is not automatically the culprit, and link building is the most expensive remedy to get wrong.
