# Skill: Content Audit

## Purpose

Assess whether cashahnawaz.com's content actually covers the priority services with the depth, accuracy, and trust signals a CA/tax/compliance searcher and Google both expect — and identify content gaps, thin pages, and outdated information (a particular risk in tax content, where rules, due dates, and thresholds change yearly).

## Scope

**This skill owns:** depth, accuracy, freshness, and trust-signal (E-E-A-T) assessment of content that already exists (or is conspicuously missing) on cashahnawaz.com's priority-service and blog pages — coverage gaps, thin content, stale tax/compliance references, duplicate/cannibalizing content, and content-format quality (structure, FAQs, worked-example opportunities).

**This skill does NOT own** (route to the owning skill instead):
- Title tags, meta descriptions, heading-tag optimization, or keyword targeting mechanics — [on-page-seo](on-page-seo.md). Content-audit judges whether the *substance* is deep and accurate; on-page-seo judges whether it's packaged/labeled correctly for search.
- Internal link structure and anchor text between pages — [internal-linking](internal-linking.md). Content-audit only notes *whether* an article should link back to a service page (feeding that skill), not link mechanics.
- Schema markup syntax/validity for FAQ, Article, or Service schema — [schema-audit](schema-audit.md). Content-audit identifies FAQ-worthy content; schema-audit verifies the markup is well-formed.
- Technical crawlability/indexability — [technical-seo](technical-seo.md)/[website-crawl](website-crawl.md).
- Conversion mechanics on a content page (CTA placement, form friction) — [cro-audit](cro-audit.md).
- Local/geo relevance and NAP — [local-seo](local-seo.md); content-audit only flags when a page reads generic/placeless (see Step 5).
- Independent competitor site profiling — [competitor-analysis](competitor-analysis.md); content-audit consumes its output for gap prioritization but doesn't re-run competitor fetches itself.
- Traffic/ranking performance diagnosis — [gsc-analysis](gsc-analysis.md)/[ga4-analysis](ga4-analysis.md); their data is prioritization input here, not this skill's subject.

When a finding straddles two of these (e.g., a thin page that also has a weak title tag), record the content-depth dimension here and cross-reference the owning skill for the rest.

## When to use it

- After [on-page-seo](on-page-seo.md) identifies intent-mismatch or thin-content issues.
- When a priority service has no dedicated page (gap identified by [website-crawl](website-crawl.md) or [gsc-analysis](gsc-analysis.md)).
- Periodically, to check tax-content freshness (rates, due dates, forms, thresholds change with each Finance Act / assessment year).
- When [competitor-analysis](competitor-analysis.md) shows competitors covering a subtopic this site doesn't.

## Required Data

- URL inventory and word counts from [website-crawl](website-crawl.md).
- Priority services list and groupings from CLAUDE.md.
- Actual page content (fetched, not assumed).
- Publicly known, verifiable facts only when checking factual freshness (e.g., current ITR filing due date, current GST thresholds) — and only state these if independently confirmable; if uncertain, flag for the user/a qualified professional to confirm rather than asserting a specific figure.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- Actual page content fetched via WebFetch/crawl — text, structure, headings, and dates/figures exactly as published (never paraphrased into an assumed "typical" version).
- URL inventory, word counts, and `lastmod`/on-page dates from [website-crawl](website-crawl.md) crawl data.
- Priority services list and groupings, defined in CLAUDE.md (a project fact, not something requiring a live tool).
- Competitor content excerpts, if [competitor-analysis](competitor-analysis.md) has actually fetched them this session.

### DATA NOT AVAILABLE (mark explicitly — never fill the gap with a plausible guess)
- GSC ranking/impression/query data for prioritizing which content gap matters most — usable only if [gsc-analysis](gsc-analysis.md) has actually pulled it live this session; otherwise mark `DATA NOT AVAILABLE` and prioritize gaps by CLAUDE.md priority-service weight and evident competitor coverage instead.
- GA4 engagement data for existing pages — same rule, via [ga4-analysis](ga4-analysis.md).
- **Current authoritative tax rates, due dates, thresholds, or form names.** This is a separate, stricter gate than tool access. Even when WebSearch/WebFetch is working, Claude must NOT assert a "correct" current tax figure — tax rules carry effective-date nuances (assessment year, taxpayer category, transitional provisions) that a search result alone cannot fully resolve or date-stamp with confidence. Treat "a tool is available" and "Claude is qualified to certify this figure as currently correct" as two different gates: the first can be open while the second stays closed. The second gate is always closed for this project — any specific current figure must be flagged for verification by the user or a qualified CA/tax professional, not asserted.

## Pre-Audit Checks

Before starting the step-by-step process below, confirm:

1. **Crawl inventory freshness.** Confirm the URL/word-count inventory from [website-crawl](website-crawl.md) being used was pulled this session, or is recent enough to be trusted. An audit built on a stale crawl can miss pages added/removed since, or misreport word counts from before an edit. If recency is unknown or old, say so and re-crawl (or explicitly flag the risk) before proceeding.
2. **Current-date context confirmed.** Establish today's actual date before making any "stale content" judgment — freshness/staleness of an assessment year, due date, or filing deadline is only meaningful relative to the real current date, never inferred from the content being reviewed or from Claude's own training-data sense of "recent."
3. **Priority services list reviewed** against CLAUDE.md immediately before coverage mapping, so no service or grouping is missed or misremembered.

## Step-by-Step Audit Process

1. **Coverage mapping.** Build a table: Priority Service → Page exists? (Y/N) → URL → Word count → Last updated (if determinable from sitemap `lastmod` or on-page date). Every gap (no page) is a finding on its own.

2. **Depth assessment**, per existing priority service page:
   - Does it answer the core questions a prospective client would have: what the service is, who needs it, eligibility/applicability, process/steps, documents required, timelines, cost/fee structure (if the firm publishes pricing — many CA firms don't; note whether absence of pricing is a conscious choice or a gap), and how to get started/contact.
   - Compare against what a thorough competent answer requires for that specific service (e.g., "NRI Taxation" content should differ meaningfully from generic "Income Tax Services" content, not be a reskin).
   - Flag pages that are mostly boilerplate/generic with minimal service-specific detail.
   - **What "genuinely deep" looks like per CLAUDE.md service group** — judge each page against its group's actual decision drivers, not a generic checklist:
     - **Income Tax** (ITR Filing, Tax Consultancy, Income Tax Services, NRI Taxation, Income Tax Compliance): who must file / is exempt, which ITR form category likely applies, residency-status nuances (especially for NRI Taxation — DTAA relevance, repatriation questions), documents typically needed, and what distinguishes "return filing" from "compliance"/"consultancy" as services (these should read as genuinely different offerings, not the same page relabeled).
     - **GST** (Registration, Return Filing, Consultancy, Compliance): who needs to register (turnover-threshold *concept*, not a stated figure — see Accuracy Protocol below), the registration process at a high level, return-filing cadence/types by taxpayer category, and common compliance pitfalls the firm helps avoid — content should distinguish one-time (Registration) from recurring (Return Filing/Compliance) engagement.
     - **Accounting** (Accounting, Bookkeeping, Financial Reporting, Outsourced Accounting): what's actually delivered (books maintained, reports produced, cadence), who this suits (a small business vs. a larger outsourcing need), and how it differs from the Audit group — these two are commonly confused/merged in thin CA-site copy and should be clearly distinguished.
     - **Audit** (Tax Audit, Statutory Audit, Internal Audit): applicability triggers (who is required/chooses to get audited), what distinguishes the three audit types from each other, process/timeline, and deliverables (audit report) — generic "we do audits" copy that doesn't differentiate the three types is a depth failure specific to this group.
     - **Registration & Compliance** (Company/LLP/Partnership/Proprietorship/Startup/NGO Registration, ROC Compliance, Company Compliance, Annual Compliance): entity-type comparison context (why a founder would pick one structure over another — at a conceptual level, not asserting current fee/threshold figures), the registration process/documents, and — critically — what *ongoing* compliance obligations follow registration, since a page that only covers "how to register" but not the recurring compliance burden is incomplete for this group specifically and likely to under-serve searchers comparing structures.

3. **Freshness/accuracy check** (high-stakes for tax content):
   - Look for explicit dates, deadlines, rates, thresholds, or form names mentioned in content (e.g., a specific assessment year, a specific due date, a specific GST rate/threshold).
   - Flag any content that appears to reference an outdated assessment year, due date, or rate — this is a **trust and compliance risk**, not just an SEO issue, and should be flagged prominently regardless of SEO severity scoring, with a note recommending the user have this verified by their own tax/compliance judgment (Claude should not assert what the *current* correct figure is unless it can verify it, and should recommend professional review given the regulated nature of this content).
   - Note: do not fabricate "current" tax rates/dates/thresholds to fill in what's missing. If a check requires knowing the current correct value, state that this must be verified against official sources (Income Tax Department, GST portal, MCA) by the user rather than asserting a number.

   ### Financial/Regulated Content Accuracy Protocol

   Apply this exact sequence to every content claim that references a tax rate, due date, threshold, or form name:

   1. **Identify the claim.** Quote the exact sentence/figure found on the page, with its URL.
   2. **Do not assert a "correct" replacement value** — even if WebSearch/WebFetch is used to sanity-check it. Tax rules have effective-date and category-specific nuances Claude cannot fully verify from a search result, so a search-derived figure is not a substitute for professional confirmation; do not present it as one.
   3. **Flag as CRITICAL**, with a note that a qualified CA/tax professional (the user or their team) must verify and supply the correct current value before publishing or before this content is otherwise relied upon.
   4. **Never let ordinary SEO severity scoring override this.** A page with low traffic and a wrong/stale tax figure is still flagged prominently at CRITICAL — regulatory/trust risk is evaluated independently of SEO impact, not blended into a lower composite score because the page is low-traffic.

4. **Trust and E-E-A-T signals** (especially relevant for YMYL-adjacent financial content):
   - Author/reviewer credentials shown (CA membership number, qualifications)?
   - Firm credentials/experience/certifications visible?
   - Client testimonials/case studies/reviews present and genuine-looking (not templated placeholder text)?
   - Physical address, registration details, contact info clearly present (also feeds [local-seo](local-seo.md))?
   - Disclaimers where appropriate (e.g., "this is general information, consult a professional for your specific case")?

5. **Content format and structure**:
   - Scannable structure (headings, lists, tables) vs. wall-of-text.
   - FAQs addressing common client questions per service (also feeds [schema-audit](schema-audit.md) FAQPage opportunities).
   - Presence of illustrative examples/calculations where helpful (e.g., a worked GST calculation) — only flag as opportunity, don't author tax-specific worked examples with invented numbers.

6. **Content gap analysis vs. competitors** — coordinate with [competitor-analysis](competitor-analysis.md): which subtopics/services do competitors cover that this site doesn't?

7. **Blog/article content review** (if a blog section exists):
   - Relevance to priority services (does it support the money pages, or is it disconnected/generic?).
   - Freshness (same date-sensitivity concern as service pages).
   - Internal linking from articles back to relevant service pages (feeds [internal-linking](internal-linking.md)).
   - Thin/low-value posts that may be diluting site quality signals (very short, outdated, or duplicate-topic posts).

8. **Duplicate/near-duplicate content check** across pages (common in WordPress CA sites where service pages get cloned from a template and lightly edited) — flag pages that are too similar to differentiate in search results.

## What Checks to Perform

- [ ] Every priority service mapped to page existence and word count
- [ ] Depth assessed against expected client questions per service
- [ ] Dates/rates/thresholds/deadlines checked for staleness signals
- [ ] E-E-A-T/trust signals inventoried
- [ ] FAQ presence checked
- [ ] Blog content relevance/freshness checked (if applicable)
- [ ] Near-duplicate content across service pages flagged
- [ ] Competitor content gaps cross-referenced

## How to Identify Issues

Thin content = page exists but covers the service in a few generic sentences with no depth on process/eligibility/documents. Stale content = specific dated references that are clearly old (e.g., referencing an assessment year or due date from a prior cycle). Missing E-E-A-T = no visible author credentials, no firm credentials, on financial advice content. Cannibalization = two+ pages effectively targeting the same service with overlapping content.

## Evidence to Collect

- Quoted excerpts showing thin/generic content, or stale date/rate references (quote exactly, with the URL).
- Word count and structural comparison per priority page.
- Screenshot/excerpt of any E-E-A-T elements present or notably absent.
- Save the coverage map to `data/crawl/content-coverage-map.csv` (this can live alongside crawl data since it's derived from crawl + manual review).

## How to Prioritize Issues

- **CRITICAL:** Stale/incorrect-looking tax compliance information live on the site (regulatory/trust risk, not just SEO) — flag prominently and recommend professional review regardless of traffic impact.
- **HIGH:** No page for a high-commercial-value priority service; severely thin content on a priority page that does exist.
- **MEDIUM:** Missing FAQs, weak E-E-A-T signals, moderate depth gaps.
- **OPPORTUNITY:** Blog content expansion, additional worked examples, competitor-inspired subtopic coverage.

## Implementation Recommendations

- For gaps: recommend a specific content brief (target service, questions to answer, suggested headings) rather than writing full finished copy inside an audit finding — full drafting is a separate, explicitly-approved implementation step per CLAUDE.md rule 6/7.
- For staleness: recommend the user (or their in-house CA team) verify and update specific figures; Claude should not draft replacement rates/dates without a verified source.
- For E-E-A-T: recommend specific, concrete additions (e.g., "add CA registration number and years of experience to About page and service page author bylines") rather than vague "build trust" advice.

## How to Validate Fixes

- Re-fetch the updated page and confirm depth/freshness/E-E-A-T additions are live.
- Track [gsc-analysis](gsc-analysis.md) position/impressions and [ga4-analysis](ga4-analysis.md) engagement time for the page over the following weeks.
- For compliance-sensitive updates, confirm with the user that the updated figures were verified against an authoritative source before publishing.

## Expected Output Format

A finished content audit primarily feeds the CLAUDE.md finding template's **Issue**, **Evidence**, **SEO Impact**, and **Recommended Fix** fields for every gap/thin-page/staleness finding it produces. Structure the core deliverable as:

1. **Coverage map table** (also saved to `data/crawl/content-coverage-map.csv`):

   | Service | Page Exists? | Word Count | Depth Rating | Freshness Flag | E-E-A-T Present? | Severity |
   |---|---|---|---|---|---|---|
   | e.g. NRI Taxation | Y/N | e.g. 420 | Thin / Adequate / Deep | OK / Stale-suspected / N/A | Y/N/Partial | CRITICAL/HIGH/MEDIUM/LOW/OPPORTUNITY |

   Depth Rating legend: **Thin** = a few generic sentences, no process/eligibility/document detail; **Adequate** = covers the core client questions but lacks differentiation or depth vs. what the service group needs (see Step 2 per-group guidance); **Deep** = genuinely differentiated, group-appropriate depth.

2. **One finding block per gap/issue**, in the CLAUDE.md required template format, for every row rated MEDIUM or above.
3. **A short freestanding list of Financial/Regulated Content Accuracy Protocol flags**, called out separately even though they also appear as CRITICAL findings above, since these carry a compliance dimension the user's team needs to triage distinctly from ordinary SEO fixes.

## Common Mistakes to Avoid

- **Treating "more content" as inherently better.** A concise, accurate, trust-building page (e.g., a tight NRI Taxation page that clearly nails eligibility, process, and a credible CTA) often outperforms a padded 2,000-word page for a considered financial decision. Do not recommend expansion as a default fix for a page that is already Adequate/Deep — target genuine gaps, not word count.
- **Asserting a tax figure is "outdated" from Claude's own training-data knowledge cutoff.** A figure that looks old to Claude may still be current, or may have changed again since Claude's knowledge cutoff in a direction Claude doesn't know. Only flag staleness by what's *evidenced on the page itself* (e.g., an explicit prior assessment year stated), never by comparing against Claude's memory of "what the rate/date should be."
- **Letting SEO traffic potential water down a CRITICAL compliance flag.** A low-traffic page with a wrong due date or rate is still CRITICAL — don't downgrade it to MEDIUM because "not many people see this page."
- **Authoring worked tax/GST examples with invented numbers** to make a page feel more helpful. Flag the *opportunity* for a worked example; do not draft one with numbers Claude cannot verify are currently correct.
- **Conflating Accounting and Audit group content** without checking whether the page actually differentiates them — a common thin-content pattern on cloned CA-site templates.
- **Scoring depth generically** instead of against the specific service-group expectations in Step 2 — e.g., praising a Registration & Compliance page for covering "how to register" while missing that it omits ongoing compliance obligations entirely.
- **Skipping the current-date check** and eyeballing "this looks recent enough" — always establish the actual current date first (see Pre-Audit Checks) before judging freshness.
- **Writing full replacement copy inside a finding** instead of a content brief — full drafting is a separate, explicitly-approved implementation step per CLAUDE.md rules 6/7 (see Implementation Recommendations above).
