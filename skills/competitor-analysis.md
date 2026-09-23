# Skill: Competitor Analysis

## Purpose

Understand how cashahnawaz.com compares to the named competitor CA/tax firms on content coverage, on-page optimization, technical health, and positioning — to find realistic, evidence-based opportunities rather than assuming what "good" looks like in the abstract.

## Scope

**This skill owns:** comparative positioning of cashahnawaz.com against the four named competitors — service coverage matrix, relative content depth, visible trust/conversion/local signals, and structural/UX patterns worth noting, always framed as a comparison rather than a standalone assessment.

**This skill does NOT own:**
- Scoring cashahnawaz.com's own pages in isolation — that's [on-page-seo](on-page-seo.md) and [content-audit](content-audit.md). Competitor-analysis only surfaces a gap *by comparison* (e.g., "3 of 4 competitors have X, cashahnawaz.com doesn't"); it does not independently judge whether cashahnawaz.com's page is good on its own terms.
- Prescribing the actual fix for a surfaced gap — findings route to the owning specialist skill ([content-audit](content-audit.md), [on-page-seo](on-page-seo.md), [cro-audit](cro-audit.md), [local-seo](local-seo.md), [schema-audit](schema-audit.md)), which scores severity and specifies implementation.
- Cashahnawaz.com's own technical health, crawlability, or performance metrics — [technical-seo](technical-seo.md)/[performance-audit](performance-audit.md); this skill only notes obvious, visible competitor technical red flags/strengths at a glance, not a full technical audit of competitors or of the site itself.
- GSC/GA4 traffic or ranking data for cashahnawaz.com — [gsc-analysis](gsc-analysis.md)/[ga4-analysis](ga4-analysis.md); this skill may note that GSC shows competing domains in the Links report, but never treats that as competitor performance data.
- Any competitor traffic, ranking, or backlink metric — no tool exists in this project for that; always `DATA NOT AVAILABLE` (see Data Sources & Limitations below).

## When to use it

- After the site's own audits ([on-page-seo](on-page-seo.md), [content-audit](content-audit.md), [technical-seo](technical-seo.md)) have established a baseline, so gaps are meaningful by comparison.
- When a priority service underperforms and it's unclear whether the cause is internal (content/technical) or competitive (competitors simply doing it better/more visibly).
- When looking for content gap opportunities ([content-audit](content-audit.md) coordinates with this skill).

## Required Data

- The four named competitor URLs from CLAUDE.md:
  - https://ndsavla.com/
  - https://www.jvb.co.in/
  - https://www.asitmehtaassociates.com/
  - https://jainanuragassociates.com/
- Working web-fetch/browsing capability to actually visit and inspect these sites.
- GSC data (if accessible) can show competing domains in the Links report, but GSC does not show competitor traffic/rankings directly — do not claim competitor GSC-sourced metrics, since GSC only reports on the property it's connected to (cashahnawaz.com), not competitors.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- Live inspection of competitor sites via WebFetch — homepage, service pages, About/team pages, visible schema, visible conversion mechanisms, all as actually fetched and quoted.
- GSC's Links report showing competing/linking domains, if [gsc-analysis](gsc-analysis.md) has pulled it live this session — this shows *linking* relationships, not competitor traffic or rankings.

### DATA NOT AVAILABLE (mark explicitly — never estimate from appearance)
- **Competitor traffic, keyword rankings, or backlink counts/profiles.** No tool exists in this project for this. This must always be reported as `DATA NOT AVAILABLE`, never estimated or inferred from how professional, large, or polished a competitor site *looks* — site appearance, apparent size, or perceived production quality is not a reliable proxy for actual search performance and must not be used as a substitute metric.
- Competitor Google Business Profile presence, review counts/ratings, or local-pack visibility — no tool to check this; note the concept if relevant to [local-seo](local-seo.md) but mark the data itself unavailable.
- Competitor conversion rates or lead volume — only visible conversion *mechanisms* (a WhatsApp button exists) can be reported, never inferred conversion *performance*.
- Competitor paid-search/ad spend or presence — not checked by this skill; do not speculate.

## Pre-Audit Checks

Before starting the step-by-step process below:

1. **Verify every competitor URL is reachable and represents the correct business — this is the mandatory first gate before any comparative analysis proceeds** (formalized in Step 1 below; do not skip straight to profiling on the assumption a URL is still valid from a prior session — re-verify each session).
2. Confirm [content-audit](content-audit.md) or [on-page-seo](on-page-seo.md) has established at least a baseline read of cashahnawaz.com's own relevant pages, so the comparison has something concrete to compare against rather than comparing competitors only to each other.

## Step-by-Step Audit Process

1. **Verify each competitor before analyzing.** For each URL, fetch the live site and confirm:
   - It resolves and is live (not parked, expired, or redirecting to an unrelated domain).
   - It genuinely represents a CA/tax/accounting/compliance services business (check About/Services/homepage copy).
   - If a competitor fails this check (dead, unrelated business, redirected elsewhere), **state this explicitly and exclude it from further analysis** rather than analyzing whatever is actually there. Do not silently substitute assumptions.

   ### Business Model Verification Checklist

   Beyond the basic "is it dead or alive" check, verify these CA/tax-firm-specific red flags before treating a URL as a valid, comparable competitor:

   - **Specialty pivot.** Confirm the firm still practices broadly across CA/tax/compliance services rather than having narrowed to a different specialty entirely (e.g., now purely a payroll-processing SaaS, or purely an immigration-consulting business that happens to retain an old CA-sounding domain name). If the current service list looks materially different from what the competitor list implies, note it and treat the comparison as partial/limited rather than excluding outright, unless the pivot is total.
   - **Directory/franchise-listing masquerade.** Check whether the URL is actually an individual firm's site versus a directory listing, marketplace profile, or franchise-network landing page that aggregates many practitioners under one domain — these have fundamentally different content/structure patterns and shouldn't be scored against single-firm content-depth criteria as if they were the same kind of site.
   - **Merger/rebrand under a different name.** If on-site evidence (an announcement, a "formerly known as" note, a name mismatch between the domain and the displayed firm name) suggests the firm has merged or rebranded, note the evidence found and flag it for the user rather than asserting a merger/rebrand occurred — do not search for or assert a successor entity without explicit on-site or user-confirmed evidence.
   - Any of these conditions found should be **stated explicitly in the verification log** with the specific evidence observed, not silently absorbed into a normal competitor profile.

2. **For each verified competitor, build a comparison profile**:
   - Which of the CLAUDE.md priority services does the competitor have a dedicated page for? (Build a coverage matrix: Service × Competitor × Cashahnawaz.)
   - Approximate content depth per service page (structure, topics covered — same depth criteria as [content-audit](content-audit.md), applied consistently across all sites for fair comparison).
   - Title/meta tag patterns used (what keyword patterns/local modifiers do they target?).
   - Trust/E-E-A-T signals present (credentials, testimonials, years in business, team bios) — note what's present, don't infer more than what's visible.
   - Site structure/navigation approach (how do they organize services?).
   - Presence of blog/resource content and its apparent focus.
   - Visible technical basics (mobile-friendliness at a glance, apparent page speed by feel, whether HTTPS is enforced) — full technical depth isn't required here, that's this site's own [technical-seo](technical-seo.md) scope, but obvious competitor red flags/strengths are worth noting.
   - Conversion mechanisms visible (contact forms, click-to-call, WhatsApp, chat widgets, calendly-style booking) — relevant to [cro-audit](cro-audit.md) comparison.
   - Any visible local SEO signals (address, service-area mentions, embedded map) — feeds [local-seo](local-seo.md).

3. **Build the service coverage matrix.** Rows = priority services from CLAUDE.md. Columns = cashahnawaz.com + each verified competitor. Cells = has dedicated page (Y/N) + rough depth rating. This directly surfaces content gaps and is the single most actionable output of this skill.

4. **Identify structural/UX patterns worth noting** — e.g., if 3 of 4 competitors have a prominent WhatsApp click button above the fold and cashahnawaz.com doesn't, that's a concrete, evidence-based CRO opportunity (route to [cro-audit](cro-audit.md)).

5. **Do not estimate competitor traffic, rankings, or backlink counts** without a legitimate tool/data source actually queried this session. If no such tool is available, state `DATA NOT AVAILABLE` for those dimensions rather than guessing based on site appearance — appearance is not a reliable proxy for actual search performance.

6. **Note what NOT to copy.** Not every competitor pattern is a best practice; flag only patterns that plausibly connect to a real SEO/UX/trust benefit, and say why.

## What Checks to Perform

- [ ] Every competitor URL verified live and representing the correct business type before analysis
- [ ] Service coverage matrix built (all CLAUDE.md priority services × all verified competitors × cashahnawaz.com)
- [ ] Content depth compared using consistent criteria across all sites
- [ ] Trust/E-E-A-T signals compared
- [ ] Conversion mechanisms compared
- [ ] Local SEO signals compared (feeds local-seo skill)
- [ ] No competitor traffic/ranking/backlink numbers asserted without an actual queried data source

## How to Identify Issues (i.e., competitive gaps)

A gap exists where multiple verified competitors consistently do something cashahnawaz.com doesn't (dedicated page for a service, visible credentials, prominent WhatsApp CTA, etc.) — consistency across competitors is a stronger signal than a single outlier. A single competitor doing something unusual is a weaker, opportunity-tier signal, not a confirmed gap.

## Evidence to Collect

Save to `data/competitors/`:
- `data/competitors/verification-log.md` — which URLs were checked, live status, business-match confirmation, date checked.
- `data/competitors/service-coverage-matrix.csv`
- `data/competitors/[competitor-domain]-profile.md` — one file per verified competitor with the findings from step 2, including direct quotes/screenshots of specific claims (e.g., "homepage headline reads: '...'") rather than paraphrased impressions.

## How to Prioritize Issues

Competitive gaps feed into the relevant specialist skill's severity scoring (a missing service page found here is scored using [content-audit](content-audit.md)'s criteria; a missing WhatsApp CTA is scored using [cro-audit](cro-audit.md)'s criteria). This skill's own output is generally OPPORTUNITY-tier unless the gap is severe and consistent across all competitors on a high-value priority service, in which case it can support a HIGH rating in the receiving skill.

## Implementation Recommendations

Route findings to the owning skill rather than prescribing fixes directly here:
- Content/page gaps → [content-audit](content-audit.md)
- On-page pattern gaps → [on-page-seo](on-page-seo.md)
- Conversion mechanism gaps → [cro-audit](cro-audit.md)
- Local signal gaps → [local-seo](local-seo.md)
- Schema pattern gaps (e.g., competitor has visible rich results) → [schema-audit](schema-audit.md)

## How to Validate Fixes

Not directly applicable — validation happens in the owning skill. Re-run this competitor analysis periodically (e.g., alongside quarterly technical-seo checks) to see if the competitive gap has closed and whether competitors have moved in the meantime.

## Expected Output Format

A finished competitor analysis primarily feeds the owning skills' **Evidence** and **SEO Impact** fields (competitive gaps are corroborating evidence, not standalone findings) — this skill's own direct output is the comparison artifact itself:

1. **Service coverage matrix** (also saved to `data/competitors/service-coverage-matrix.csv`):

   | Service | Cashahnawaz | Competitor 1 | Competitor 2 | Competitor 3 | Competitor 4 |
   |---|---|---|---|---|---|
   | e.g. NRI Taxation | Deep / Adequate / Thin / Missing | ... | ... | ... | ... |

   Depth-rating legend (kept consistent with [content-audit](content-audit.md)'s criteria for a fair comparison): **Missing** = no dedicated page; **Thin** = page exists but a few generic sentences, no process/eligibility/document detail; **Adequate** = covers core client questions but not differentiated; **Deep** = genuinely differentiated, service-appropriate depth.

2. **Verification log** (`data/competitors/verification-log.md`) — live status, business-match confirmation, Business Model Verification Checklist findings, date checked, per competitor.
3. **Per-competitor profile files** (`data/competitors/[competitor-domain]-profile.md`) with direct quotes/observations, not paraphrased impressions.
4. **A short "gaps routed to owning skills" list**, naming which skill each surfaced gap was handed to, so nothing found here gets lost without a home.

## Common Mistakes to Avoid

- **Over-indexing on a single unusual competitor pattern as an industry norm.** One competitor doing something unusual is an OPPORTUNITY-tier signal at most (per How to Identify Issues above) — don't write it up with the same confidence as a pattern consistent across most/all verified competitors.
- **Recommending copying a competitor tactic without checking whether it's actually likely to help.** A directory-style page that looks comprehensive (long list of sub-services, lots of internal links) may actually be thin/low-quality content bloat rather than a genuine strength — assess the *substance*, not just the *existence*, of a competitor pattern before recommending it be copied.
- **Estimating competitor size/success from site polish.** A well-designed site is not evidence of better rankings or more clients; a dated-looking site is not evidence of worse performance. Neither should be used as a stand-in for the traffic/ranking data this project cannot access.
- **Skipping the Business Model Verification Checklist and treating "the site loads" as sufficient verification** — a directory listing or a firm that's pivoted away from CA/tax work can pass a basic liveness check while still being a poor comparison basis.
- **Asserting a merger/rebrand/successor entity without on-site or user-confirmed evidence** — note what's observed, don't investigate and assert a corporate history that can't be confirmed from the site itself.
- **Re-using a stale verification from a prior session** — competitor sites change; re-verify liveness and business match each time this skill is run, not just the first time.
- **Letting the comparison drift into judging cashahnawaz.com's pages in isolation** — every observation here should be framed relative to what competitors do, not as an independent critique (that's [content-audit](content-audit.md)/[on-page-seo](on-page-seo.md)'s job).
