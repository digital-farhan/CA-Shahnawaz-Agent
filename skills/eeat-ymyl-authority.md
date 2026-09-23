# Skill: E-E-A-T / YMYL Authority

## Purpose

Treat expertise, experience, authoritativeness and trust as first-class SEO signals, because taxation, accounting and financial compliance are squarely **Your Money or Your Life** topics. Google holds YMYL content to a higher bar, and — more importantly — a Mumbai CA firm publishing tax guidance carries a professional obligation for that guidance to be correct.

This skill has two jobs that are equally important: auditing the *signals* of expertise (authorship, credentials, review, sourcing, dates), and enforcing the *accuracy* of every high-stakes tax and legal statement the site publishes.

## Scope

**This skill owns:** author identity and credentials, reviewer information, bios, professional experience signals, sourcing and citation of tax/legal claims, government references, publication and updated dates, editorial review process, contact information, the About page as a trust artefact, professional credentials, disclosure, and factual accuracy of YMYL claims.

**This skill does NOT own:**
- Content depth, topical coverage, and cannibalization — [content-audit](content-audit.md).
- Which content to build — [linkable-content-planner](linkable-content-planner.md).
- Detecting outdated content by performance decay — [content-decay-refresh](content-decay-refresh.md), which triggers refreshes; this skill defines the accuracy standard a refresh must meet.
- Entity footprint across the web — [entity-seo](entity-seo.md).
- Schema syntax — [schema-audit](schema-audit.md), though this skill specifies the `author`, `reviewedBy`, and `hasCredential` values.
- Conversion elements and trust-signal placement for CRO — [cro-audit](cro-audit.md).
- Publishing or editing anything — the user does that.

## When to use it

- Before publishing any new tax, compliance, or advisory content — the accuracy gate is pre-publication, not post-hoc.
- When auditing existing content in a YMYL category, which is all substantive content on this site.
- After any regulatory change (Union Budget, Finance Act, GST Council decision, CBDT/CBIC notification, MCA amendment), which can make previously correct content wrong.
- When [entity-seo](entity-seo.md) flags anonymous authorship.
- When rankings decline across informational content without a technical cause.

## Required Data

- The live site's content pages, About page, contact information, and any author/bio pages.
- The practitioner's verifiable credentials — for this firm, ICAI membership 194241 and firm registration FRN 151767W as recorded in `data/crawl/nap-instances.md`.
- **Authoritative primary sources** for every factual claim audited: Income Tax Department / CBDT, GST Council / CBIC, MCA, ICAI, RBI, and the relevant Acts, sections, rules and notifications.
- `data/crawl/` content inventory.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- Direct inspection of every page for author byline, credentials, dates, sources, and disclosure.
- Direct fetching of **primary sources** to verify a rate, threshold, section, deadline or rule, with its effective date.
- The ICAI public register, to verify the practitioner's credentials independently.
- Observation of what competitors do on authorship and sourcing ([competitor-analysis](competitor-analysis.md)).

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Any E-E-A-T "score."** Google publishes no such metric. E-E-A-T is a set of quality concepts, not a measurable value, and any numeric E-E-A-T rating is fabricated. Assess signals present or absent; never score the site "72/100 on E-E-A-T."
- Whether a ranking change was caused by E-E-A-T — not isolable.
- The practitioner's professional history beyond what is published or officially registered. Claude cannot know years of experience, client sectors, or specialisations that are not stated. **These must be supplied by the user, never drafted speculatively.**
- Any internal editorial process the firm may or may not have — ask, do not assume.
- **The current state of any tax rule not verified against its primary source this session.** Model knowledge of Indian tax law has a cutoff and tax law changes constantly; treat every remembered rate, threshold, deadline or section as unverified until fetched from source. This is the most important limitation in this file.

## Pre-Audit Checks

1. Confirm which credentials are publicly verifiable, and use only those.
2. Confirm access to primary sources this session — without it, factual verification cannot be performed and the accuracy audit must be deferred rather than done from memory.
3. Identify the highest-stakes pages first: anything stating a rate, threshold, due date, penalty, eligibility rule, or procedure. These carry real client risk.
4. Load [entity-seo](entity-seo.md)'s entity definition so author identity is consistent with the entity.

## Step-by-Step Audit Process

### Step 1 — Audit author identity and credentials

Per page and sitewide:

- Is there a **named** author? Anonymous or "Admin"-attributed YMYL content is a significant weakness.
- Are **CA credentials** stated where appropriate — designation, ICAI membership number, firm registration number?
- Is there an **author bio** establishing genuine professional standing, linked from the byline?
- Is **professional experience** conveyed specifically — practice areas, years, client types — rather than generically?
- Is there **reviewer information** where the author is not the credentialed practitioner? For content written by a non-CA, a named CA reviewer with a review date is the appropriate pattern, and it is common practice in this category.

### Step 2 — Audit sourcing and citations

For each substantive tax/compliance page:

- Are claims **sourced**? Statements of law, rates, thresholds and deadlines should cite the provision or notification they come from.
- Are there **government references** — links to the Income Tax Department, GST portal, CBIC, MCA — where the reader would need the official source or the actual filing portal?
- Are **legal/tax citations** specific (section, rule, notification number, assessment year) rather than vague ("as per current rules")? Vagueness is both weaker for readers and a signal that the claim may not have been verified.
- Are cited sources **current**, or do they point to superseded circulars and retired portal URLs?

### Step 3 — Audit dates and freshness signals

- Is a **publication date** visible?
- Is an **updated date** visible, and is it honest? A "last updated" stamp refreshed by a plugin without any content change is a trust problem, not a freshness win.
- Does dated content state the **assessment year or financial year** it applies to? This is essential in Indian tax content and its absence makes otherwise-correct content misleading.
- Is any content visibly stale in a way that makes it **wrong** rather than merely old? Route to [content-decay-refresh](content-decay-refresh.md).

### Step 4 — The accuracy gate

**This is the most consequential step in the skill.** Every high-stakes tax or legal statement is checked against an authoritative primary source *before publication*, and re-checked on regulatory change.

The rule, stated plainly: **do not allow invented tax rules, sections, thresholds, deadlines or legal interpretations — including from the model's own memory.** Indian tax law changes at least annually and often mid-year. A rate that was correct in a training corpus may be wrong today, and a confidently-stated wrong deadline can cause a reader to miss a filing and incur a penalty.

Procedure for each factual claim:

1. Identify the claim and its type — rate, threshold, due date, section reference, procedure, eligibility, penalty.
2. Fetch the primary source and locate the provision.
3. Record the source URL, the provision, and the **effective date / applicable assessment year**.
4. Mark the claim `VERIFIED` with its source, `SUPERSEDED` (with the current position), or `UNVERIFIED`.
5. **An `UNVERIFIED` high-stakes claim is a finding**, regardless of whether it looks right. Recommend removal or correction; never leave it standing on the basis that it is probably fine.

Where a claim genuinely depends on individual circumstances, the correct fix is usually to state the general position, cite the provision, and direct the reader to professional advice — not to publish a definitive-sounding simplification.

### Step 5 — Audit trust artefacts

- **About page:** does it identify real people with real credentials, or is it generic filler?
- **Contact information:** complete, consistent with [local-citation-authority](local-citation-authority.md)'s canonical record, and genuinely reachable.
- **Professional credentials:** displayed and accurate — never overstated.
- **Disclosure:** is it clear the content is general information and not individualised professional advice? For a regulated profession this is both a trust signal and a professional-conduct matter.
- **Accuracy signals:** does the site show any evidence of review, correction, or maintenance?

### Step 6 — Route and hand over

Signal gaps route to on-site fixes; accuracy failures route to urgent correction. Claude never edits the site.

## What Checks to Perform

- [ ] Named author on every substantive page; anonymous content identified
- [ ] CA credentials (membership number, FRN) stated where appropriate and verified against the official register
- [ ] Author bio present, specific, and linked
- [ ] Reviewer named with review date where the author is not the credentialed practitioner
- [ ] Claims sourced; government references present where the reader needs them
- [ ] Citations specific — section / rule / notification / assessment year
- [ ] Cited sources current, not superseded or dead
- [ ] Publication and updated dates visible and honest
- [ ] Applicable AY/FY stated on all dated tax content
- [ ] **Every high-stakes claim verified against a primary source this session, with effective date recorded**
- [ ] `UNVERIFIED` high-stakes claims raised as findings
- [ ] About page, contact details, credentials and disclosure audited
- [ ] No E-E-A-T "score" invented
- [ ] No professional history asserted that the user did not supply

## How to Identify Issues

Two categories, and they are not equally urgent. **Accuracy failures** — a wrong rate, a superseded threshold, a missed deadline change, an incorrect section — are findings that carry client harm and are urgent regardless of SEO impact. **Signal failures** — anonymous authorship, missing credentials, unsourced claims, absent dates — weaken the site's standing in a category where Google explicitly expects expertise. An accuracy failure on a high-traffic page is the most serious finding this skill can produce, and it outranks every other consideration in the audit.

## Evidence to Collect

Save to `data/crawl/` and `reports/`:
- `eeat-audit-YYYY-MM-DD.md` — per-page signal audit.
- `eeat-signals.csv` — URL, author named, credentials shown, bio linked, reviewer, sources cited, government refs, publication date, updated date, AY/FY stated, disclosure.
- `accuracy-register.md` — **the important one**: every high-stakes claim audited, with page URL, the claim quoted verbatim, claim type, primary source URL, provision, effective date, and verdict (`VERIFIED` / `SUPERSEDED` / `UNVERIFIED`).
- `source-register.md` — shared with [digital-pr-link-assets](digital-pr-link-assets.md); every primary source with fetch date, so claims stay re-verifiable.
- Quote the claim exactly as published; paraphrase destroys the evidence.

## How to Prioritize Issues

- **CRITICAL** — a published statement of a rate, threshold, deadline, penalty or eligibility rule that is **wrong or superseded**. Client-harm risk; fix immediately, ahead of all other audit work.
- **HIGH** — high-stakes claims that are `UNVERIFIED`; anonymous authorship across YMYL content; no credentials anywhere on a site giving tax guidance; dated tax content with no AY/FY stated; a missing or generic About page.
- **MEDIUM** — unsourced but currently-correct claims; missing government references; missing updated dates; no reviewer on non-CA-authored content; missing disclosure.
- **LOW** — bio thinness; formatting of citations.
- **OPPORTUNITY** — adding `author`/`reviewedBy` schema; adding a visible editorial and review policy, which competitors in this category rarely have.

## Implementation Recommendations

All manual, for the user.

- **Accuracy corrections first.** Supply the page URL, the incorrect text quoted exactly, the corrected text, the primary source, and the effective date. Recommend correcting or unpublishing immediately; an incorrect deadline left live for another week is a real risk to a real reader.
- **Author identity:** in WordPress, set a real user account for the practitioner (Users → Profile) with display name, credentials in the Biographical Info field, and a photo; ensure the theme displays the byline and bio. Where the theme does not show them, that is the finding and the fix is theme-level — describe it for the user's developer rather than performing it.
- **Credentials:** state designation, ICAI membership number and FRN on the About page and in the author bio, exactly as officially registered.
- **Reviewer pattern:** for content not written by the CA, add a visible "Reviewed by [name], [credentials], on [date]" line, and keep it accurate — a review line for a review that did not happen is worse than none.
- **Sourcing:** add specific citations with links to the primary source, including section/notification and assessment year.
- **Dates:** display genuine publication and updated dates; update the date only when content actually changes.
- **Disclosure:** add a clear general-information / not-individual-advice notice, placed where readers will see it.
- **Schema:** specify `author` (`Person`, with `hasCredential`), `reviewedBy`, `datePublished`, `dateModified`; [schema-audit](schema-audit.md) validates.
- **Never** draft a biography, years of experience, specialisation, or credential the user has not supplied and that is not officially registered.

## How to Validate Fixes

- **Accuracy:** re-fetch the corrected page and confirm the text now matches the primary source; re-verify at every regulatory trigger. Record the re-verification date in the accuracy register — this register is the artefact that makes accuracy maintainable rather than a one-off.
- **Signals:** re-fetch and confirm byline, credentials, bio, dates, citations and disclosure render on the live page — not merely that a field was filled in the admin.
- **Schema:** validate `author`/`reviewedBy` markup.
- **Register maintenance:** on each Budget, Finance Act, GST Council decision or major notification, re-run the accuracy register against affected pages. This is the recurring obligation the skill creates.
- **SEO outcome:** track informational-content performance via [gsc-analysis](gsc-analysis.md) if available, reported as correlation. Never attribute a ranking change to E-E-A-T as if it were measurable.

## Expected Output Format

1. **Accuracy register** — first, because it is the most consequential section:

   | Page | Claim (verbatim) | Type | Primary source | Provision | Effective date | Verdict |
   |---|---|---|---|---|---|---|

2. **Signal audit table** per page.
3. **Sitewide signal summary** — how many pages have named authors, credentials, sources, dates.
4. **Findings** in the standard CLAUDE.md template with Confidence Level and Evidence Source, accuracy failures first.
5. **Regulatory-trigger watchlist** — which pages need re-checking on which events.
6. **Limitations**, e.g.: *No E-E-A-T score is given; no such metric exists. Claims marked `VERIFIED` were checked against the primary sources listed on the dates shown. Professional-history details were not drafted; the user must supply them.*

## Common Mistakes to Avoid

- **Verifying a tax fact from memory.** The single most dangerous mistake available in this project. Model knowledge has a cutoff; Indian tax law changes constantly. Fetch the source or mark it `UNVERIFIED`.
- **Inventing a rate, section, threshold, deadline, or legal interpretation** because it sounds right.
- **Drafting professional experience or credentials** the user has not supplied.
- **Scoring E-E-A-T numerically.** No such metric exists.
- **Treating a plugin-refreshed "updated" date as freshness.** It is a trust problem when the content did not change.
- **Adding a reviewer line for a review that did not happen.**
- **Omitting the assessment year** on tax content, which makes correct information misleading.
- **Leaving an unverified high-stakes claim live** because it is probably fine.
- **Overstating credentials** — a professional-conduct exposure in a regulated profession, not just an SEO issue.
- **Treating this as an SEO checklist.** The accuracy work protects readers first; the ranking benefit is a by-product.
- **Editing the site.** Claude supplies exact corrected text and manual steps; the user publishes.
