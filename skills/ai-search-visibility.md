# Skill: AI Search Visibility (AEO / GEO)

## Purpose

Assess and improve whether the firm's content is surfaced and cited by answer engines — Google AI Overviews, ChatGPT-style search, Perplexity, Gemini and others — for the questions Mumbai taxpayers and business owners actually ask. Answer engines increasingly sit between a search and a click, and for a CA firm the practical stake is being the cited source for "what is the ITR filing deadline" or "how do I register a company in Mumbai" rather than being invisible behind an answer someone else supplied.

The governing constraint: **the content must remain useful for humans first.** Content shaped for machines at the expense of readers fails both audiences.

## Scope

**This skill owns:** the structural and evidential characteristics that make content citable by answer engines — direct answers, definitions, tables, FAQs, entity clarity, source citations, expert attribution, structured information, concise answer blocks, original data, supporting evidence — plus the method for testing whether the firm is being surfaced.

**This skill does NOT own:**
- Classic SERP features (featured snippets, PAA, local pack) — [serp-intelligence](serp-intelligence.md), though the two overlap and should be run together.
- Schema syntax/validity — [schema-audit](schema-audit.md); this skill specifies which structured data helps machine comprehension.
- Content depth and coverage — [content-audit](content-audit.md).
- Author credentials and factual accuracy — [eeat-ymyl-authority](eeat-ymyl-authority.md), whose standards this skill depends on entirely: answer engines in YMYL categories favour attributable, sourced content, and an inaccurate answer is worse when a machine repeats it.
- Entity resolution — [entity-seo](entity-seo.md).
- Crawlability and rendering — [technical-seo](technical-seo.md).
- Publishing anything — the user does that.

## When to use it

- After [eeat-ymyl-authority](eeat-ymyl-authority.md) and [entity-seo](entity-seo.md) have established authorship and entity clarity — those are prerequisites, not optional extras.
- When informational content holds impressions but loses clicks, a pattern consistent with answers being consumed in the SERP ([seo-opportunity-mining](seo-opportunity-mining.md)).
- When planning content for question-shaped queries.
- On a recurring cycle, since answer-engine behaviour changes quickly.

## Required Data

- The live content pages, especially question-answering and definitional content.
- The priority question set — the questions clients actually ask, drawn from services, PAA observations, and the user's own knowledge of enquiry patterns.
- Verified authorship and accuracy status from [eeat-ymyl-authority](eeat-ymyl-authority.md).
- `robots.txt` and any AI-crawler directives from [technical-seo](technical-seo.md).

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- **Direct inspection of the site's content structure** — whether a page answers its question early, whether definitions are clean, whether tables and FAQs exist, whether claims carry sources and attribution. This is fully obtainable and is the bulk of the skill.
- `robots.txt` inspection for AI-crawler directives, which determines whether the site is even eligible to be cited by some engines.
- Competitor content structure, for comparison.
- **Manual spot-checks by the user**, who can run a question in an answer engine and report what appeared and who was cited.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Whether the firm appears in AI Overviews or any answer engine.** No tool in this project queries answer engines or measures AI citation. This is the central limitation: the *optimisation* work is verifiable, the *outcome* is not, other than through user-reported spot-checks.
- AI-referred traffic. GA4 can sometimes show referrals from some AI products, but GA4 is unavailable here (`reports/00-capability-check.md`); until it exists this is `DATA NOT AVAILABLE`.
- Any "AI visibility score," share-of-voice, or citation-rate metric. No such measurement exists in this project — do not produce one.
- How any specific engine selects sources. The mechanisms are undisclosed and change; treat all guidance here as *well-founded practice*, not as a documented ranking system, and label it that way.
- Whether a competitor is being cited — same limitation, unless the user checks.

## Pre-Audit Checks

1. Confirm [eeat-ymyl-authority](eeat-ymyl-authority.md) has verified accuracy on the pages in scope. **Optimising an inaccurate page for machine citation actively amplifies harm** — a wrong deadline repeated by an answer engine reaches more people, with more apparent authority, than the page alone.
2. Confirm crawlability and rendering ([technical-seo](technical-seo.md)) — content that depends on client-side rendering may not be readable by all crawlers.
3. Check `robots.txt` for AI-crawler directives, and confirm with the user whether any blocking is intentional. Some firms deliberately block AI crawlers; that is a legitimate business decision, and this skill should surface it rather than override it.
4. Establish the priority question set before auditing, so the audit is anchored to real demand.

## Step-by-Step Audit Process

### Step 1 — Build the priority question set

List the questions the firm should be the answer to, grouped by priority service: deadlines and due dates; eligibility and applicability; procedures and document requirements; definitions; penalties and consequences; cost and process questions; NRI-specific and Mumbai-specific variants. Draw them from PAA observations ([serp-intelligence](serp-intelligence.md)), GSC queries if available, and the user's knowledge of what clients actually ask.

### Step 2 — Audit answerability per question

For each priority question, find the page that should answer it and assess:

- **Direct answer** — is the question answered plainly within the first paragraph or two, or buried after several hundred words of preamble? Answer engines extract concise, self-contained answers; so do human readers in a hurry. This is the single highest-leverage structural change available.
- **Concise answer block** — is there a short, quotable, standalone passage that answers the question without requiring surrounding context?
- **Definition** — where the question is definitional, is there a clean, one-or-two-sentence definition?
- **Table** — is comparative, threshold-based, or rate-based information in a real HTML table rather than prose or an image? Tables are highly extractable and much easier for readers to scan.
- **FAQ** — are related sub-questions grouped and answered explicitly, in plain question form?
- **Structured information** — headings that state questions, lists for sequential procedures, clear hierarchy.

### Step 3 — Audit evidential quality

Answer engines in YMYL categories favour content that is attributable and verifiable, and so do readers:

- **Entity clarity** — is it obvious which organisation published this, where it operates, and what it does? ([entity-seo](entity-seo.md))
- **Source citations** — are claims linked to primary sources? ([eeat-ymyl-authority](eeat-ymyl-authority.md))
- **Expert attribution** — is the answer attributable to a named, credentialed CA?
- **Original data** — is there anything here that exists nowhere else? Unique data is the most reliable reason to be cited rather than paraphrased. ([digital-pr-link-assets](digital-pr-link-assets.md))
- **Strong supporting evidence** — worked examples, specific figures with sources, cited provisions.
- **Currency** — a visible, accurate updated date and stated assessment year. For tax answers, currency is decisive: an engine has good reason to prefer a clearly-dated current answer over an undated one.

### Step 4 — Audit machine comprehension

- Is the content in the HTML, or injected client-side?
- Is `FAQPage` / `HowTo` / `Article` schema present and accurate where genuinely applicable? Specify; [schema-audit](schema-audit.md) validates. Do not recommend marking up an FAQ that is not visibly on the page.
- Are headings semantically meaningful rather than styling artefacts?
- Do tables use proper `<table>` markup with headers, rather than layout divs or images?
- Does `robots.txt` permit the crawlers the firm wants?

### Step 5 — Testing method (user-performed)

Since Claude cannot query answer engines here, define a repeatable manual test for the user:

1. Take 10–15 priority questions.
2. Run each in the target engines, recording: whether an AI answer appeared; which sources were cited; whether this firm appeared; and which competitors did.
3. Record results in `data/ai-search/ai-visibility-YYYY-MM-DD.md`.
4. Repeat on the same question set each cycle, so change is measurable.

Note the caveats honestly in the record: answer-engine results are personalised, location-dependent and non-deterministic, so a single observation is an anecdote and a consistent pattern across a fixed question set is the only usable signal.

### Step 6 — Prioritise and hand over

Rank by commercial value of the question × how far the current page is from being citable. Claude never edits the site.

## What Checks to Perform

- [ ] Accuracy verified before any citability optimisation
- [ ] `robots.txt` AI-crawler directives checked and intent confirmed with the user
- [ ] Priority question set built from real demand
- [ ] Direct-answer placement assessed per question
- [ ] Concise, standalone answer blocks identified or flagged as missing
- [ ] Definitions, tables and FAQs assessed; prose-buried data identified
- [ ] Rate/threshold data confirmed to be in real HTML tables, not images
- [ ] Entity clarity, citations, expert attribution and currency assessed
- [ ] Original data identified or flagged as absent
- [ ] Server-rendered content confirmed
- [ ] Schema specified only where the content genuinely exists on the page
- [ ] Manual testing method defined and results recorded on a fixed question set
- [ ] No AI visibility metric invented

## How to Identify Issues

The finding is: *for a priority question this firm should own, the page that should answer it does not answer it in a citable way* — the answer is buried, hedged, undated, unattributed, unsourced, or locked in an image. Severity rises with the commercial value of the question and with how close the page already is. A high-value question where the page has the right content but buries the answer under 600 words of preamble is the best kind of finding here: cheap to fix, and the fix helps human readers just as much.

## Evidence to Collect

Save to `data/ai-search/`:
- `question-set.md` — the priority questions, grouped by service, with the page that should own each.
- `answerability-audit-YYYY-MM-DD.md` — per question: page, direct-answer presence, structure, evidence, currency, verdict.
- `ai-visibility-YYYY-MM-DD.md` — user-reported spot-check results on the fixed question set, with the caveat noted.
- `ai-crawler-directives.md` — `robots.txt` findings and confirmed intent.
- Quote the page's current opening answer verbatim, so the "buried answer" finding is evidenced rather than asserted.

## How to Prioritize Issues

- **CRITICAL** — an inaccurate answer on a high-visibility page. Fix accuracy first ([eeat-ymyl-authority](eeat-ymyl-authority.md)); never optimise it for citation while it is wrong.
- **HIGH** — a high-commercial-value question where the page has the answer but buries it, or presents rates/deadlines as an image; unintentional AI-crawler blocking; undated tax content answering a time-sensitive question.
- **MEDIUM** — missing FAQ structure on question-heavy pages; unattributed answers; missing citations; prose where a table belongs.
- **LOW** — heading-hierarchy cleanups; schema additions on low-value pages.
- **OPPORTUNITY** — original data that would make the firm the primary citable source for a question nobody else answers well, especially Mumbai-specific or NRI-specific.

## Implementation Recommendations

Manual, for the user.

- **Lead with the answer.** Restructure the page so the question is answered in the first paragraph, then expand. Supply the exact rewritten opening. This helps readers first — which is the standard the whole skill is held to.
- **Add a concise answer block** — a short, self-contained paragraph directly under the heading that answers the question completely.
- **Convert prose data to tables** — rates, thresholds, due dates, comparisons — as real HTML tables. In Elementor, use a table widget or a properly marked-up text block, not an image. Any rate or deadline currently published as an image is invisible to extraction and inaccessible to screen readers; that is a double failure worth flagging.
- **Add genuine FAQ sections** with real questions clients ask, answered plainly; then add `FAQPage` schema via Rank Math reflecting the visible content.
- **Add attribution and currency** — named credentialed author, visible updated date, stated assessment year.
- **Cite primary sources** inline.
- **Never** create content designed to game answer engines — question-stuffed pages, fake FAQ blocks marked up but hidden, or padded "AI-friendly" filler. The specification is explicit: do not create fake AI-friendly content. It is also self-defeating, since schema for hidden content is a guidelines violation.

## How to Validate Fixes

- **Structural:** re-fetch and confirm the answer now appears early, the table is real markup, the FAQ is visible, and the date and author render.
- **Schema:** validate and confirm it reflects visible content ([schema-audit](schema-audit.md)).
- **Visibility:** the user re-runs the fixed question set next cycle and records results. Compare across cycles, never on a single observation.
- **Human outcome:** engagement and conversions on the affected pages if GA4 becomes available; otherwise `DATA NOT AVAILABLE`.
- **Never** claim an AI-visibility improvement without the fixed-question-set comparison, and always state its limitations.

## Expected Output Format

1. **Limitations header**, e.g.:

   > Claude cannot query answer engines in this project. No AI-citation measurement exists here, and no AI visibility score is given because none can be measured. The audit below assesses citability characteristics that are directly observable on the site; outcome measurement depends on the user running the manual question-set test.

2. **Answerability matrix:**

   | Priority question | Owning page | Direct answer? | Structure | Attribution | Currency | Verdict |
   |---|---|---|---|---|---|---|

3. **User test results** on the fixed question set, where available.
4. **Findings** in the standard CLAUDE.md template with Confidence Level and Evidence Source.
5. **Rewrite specifications** for the highest-value pages, with exact suggested opening answers.

## Common Mistakes to Avoid

- **Optimising an inaccurate page for citation.** Amplifying a wrong tax deadline is worse than leaving it unfound.
- **Inventing an AI visibility metric.** No tool measures it here.
- **Claiming the firm does or does not appear in AI Overviews** without a user-reported observation.
- **Marking up an FAQ that is not visible on the page** — a structured-data guidelines violation.
- **Writing padded "AI-friendly" content** that serves no reader.
- **Leaving rates and deadlines in images**, which are unextractable and inaccessible.
- **Treating a single spot-check as measurement.** Results are personalised and non-deterministic; only a fixed question set tracked over cycles is meaningful.
- **Presenting practice as documented ranking mechanics.** Engines do not publish their selection criteria; say so.
- **Overriding a deliberate AI-crawler block** without confirming intent with the user.
- **Neglecting the human reader.** If a change makes the page worse to read, it is the wrong change.
