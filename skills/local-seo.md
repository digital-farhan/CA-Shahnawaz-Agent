# Skill: Local SEO Audit

## Purpose

Ensure cashahnawaz.com and its associated business listings are optimized for local/geo-relevant search — critical for a CA/tax firm, since most clients search for a firm they can trust and realistically engage with in their region ("CA near me," "GST registration in [city]," etc.), and local pack/map visibility is a distinct ranking surface from organic web results.

## Scope

**This skill owns:** NAP (Name, Address, Phone) consistency across on-site instances, Google Business Profile signals (where accessible), local-intent content signals on service pages, service-area clarity, and click-to-call/WhatsApp functionality as a local-contact mechanism.

**This skill does NOT own** (route to the owning skill instead):
- Schema markup *syntax/validity* — [schema-audit](schema-audit.md). Local-seo establishes what the *correct* NAP/`areaServed` values are and flags whether schema matches on-site NAP; schema-audit verifies the JSON-LD itself is well-formed, correctly typed, and passes structured-data testing once local-seo has confirmed the values are right.
- General on-page title/meta/heading optimization — [on-page-seo](on-page-seo.md), even when a local modifier is involved (e.g., "GST Registration in [City]" as a title pattern is on-page-seo's concern; whether the page's *content* genuinely reflects the service area is local-seo's).
- Overall CTA design/form friction — [cro-audit](cro-audit.md). Local-seo checks that tel:/wa.me links exist and function; cro-audit assesses their placement, prominence, and surrounding trust signals as a conversion mechanism.
- Site-wide technical crawlability — [technical-seo](technical-seo.md)/[website-crawl](website-crawl.md).
- Competitor local-signal comparison in depth — [competitor-analysis](competitor-analysis.md); local-seo consumes that skill's output rather than independently profiling competitors.
- GSC query-level performance analysis — [gsc-analysis](gsc-analysis.md); local-seo uses location-modified query findings as input, not as its own output.

## When to use it

- As part of the initial audit, especially since services like GST Registration, Company Registration, and Statutory Audit often carry strong local-intent search behavior.
- When [gsc-analysis](gsc-analysis.md) shows queries with location modifiers underperforming.
- When [schema-audit](schema-audit.md) reviews LocalBusiness/ProfessionalService markup — coordinate NAP accuracy checks together.
- When [competitor-analysis](competitor-analysis.md) shows competitors with stronger local signals.

## Required Data

- Live site content (footer, contact page, About page) for NAP (Name, Address, Phone) data.
- Google Business Profile status — **only if a connector/tool provides actual access this session; do not assume GBP access exists.** If unavailable, note `DATA NOT AVAILABLE` for GBP-specific findings and clearly state that GBP audit requires the user to either grant access or check it directly themselves.
- Schema data from [website-crawl](website-crawl.md)/[schema-audit](schema-audit.md) for structured NAP.
- GSC query data ([gsc-analysis](gsc-analysis.md)) for location-modified query performance, if accessible.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- On-site NAP via WebFetch/crawl — footer, Contact page, About page text, and schema blocks, fetched and quoted exactly as published.
- Actual `tel:`/`wa.me` `href` values, confirmed by inspecting rendered/crawled HTML rather than assumed from visible text.
- Schema data already pulled by [website-crawl](website-crawl.md)/[schema-audit](schema-audit.md) for structured NAP comparison.
- GSC location-modified query performance, only if [gsc-analysis](gsc-analysis.md) has actually pulled it live this session.

### DATA NOT AVAILABLE (mark explicitly by default — do not fill the gap)
- **Google Business Profile access is, by default, NOT available in this project** — no GBP connector was found in this project's capability inspection. Treat every GBP-dependent line item (category, reviews/ratings, photos, posts, Q&A, GBP-side NAP) as `DATA NOT AVAILABLE` unless a session explicitly confirms working GBP access via an actual successful tool call. Never estimate or infer GBP contents (e.g., star rating, review count, category) from anything else observed on the website. When GBP is unavailable, tell the user directly and plainly to check Google Business Profile Manager themselves for these items — do not soften this into a vague "may want to review GBP" note.
- Third-party citation/directory listings (Justdial, Sulekha, CA-specific directories) — never claim these were checked unless a tool actually fetched them this session; note the *concept* matters, but state plainly that no citation audit was performed if none was.
- Competitor GBP/local-pack presence — [competitor-analysis](competitor-analysis.md) can note visible on-site local signals from competitor sites, but neither skill has a tool to check competitor GBP listings; mark `DATA NOT AVAILABLE` if referenced.

## Pre-Audit Checks

Before starting the step-by-step process below, confirm:

1. **Which NAP variant is authoritative, before treating any instance as "correct."** Scan on-site instances first (footer, Contact page, About page, schema) and note which value appears most often and/or in the most authoritative location (e.g., a dedicated Contact page vs. a legacy blog post byline). Do not silently pick one to standardize on — if more than one distinct variant exists, flag the conflict explicitly and route it to the user for confirmation of which is actually current and correct (frequency is a clue, not proof — see Common Mistakes below).
2. **GBP access status confirmed for this session** — attempt the actual tool call before writing any GBP-related finding; do not carry over an assumption from a previous session or from CLAUDE.md's project snapshot table.
3. **Service-area claims are not assumed** — confirm from the site or the user whether the firm is local/single-office, regional, or serves NRI/out-of-region clients (relevant given NRI Taxation is a priority service) before checking `areaServed`/local-content consistency against that.

## Step-by-Step Audit Process

1. **NAP consistency check (on-site).**
   - Locate every instance of the business name, address, and phone number across the site (footer, Contact page, About page, schema markup).
   - Confirm exact consistency — same formatting, same phone number, same address — across every instance. Inconsistent NAP (e.g., different phone number in footer vs. schema) is a known local ranking and trust issue.
   - **Identify where each NAP instance is actually stored/editable in WordPress before prescribing a fix** — this matters because "fix the NAP" means a very different implementation step depending on where it lives:
     - **Theme Customizer setting** (Appearance → Customize, e.g., a "Site Identity" or theme-specific contact-info field) — editable by the user directly in wp-admin, no developer needed.
     - **A widget** (e.g., a footer widget area with a Text/HTML or contact-info widget) — editable via Appearance → Widgets or the block-based widget editor, again user-editable.
     - **A dedicated Contact page built with a page builder** (Elementor, WPBakery, Divi, Gutenberg blocks, etc.) — editable via the page builder's editor; confirm which builder is active (cross-ref [wordpress-seo](wordpress-seo.md) plugin inventory) since instructions differ by builder.
     - **Hardcoded in a footer/header template file** (e.g., `footer.php`, a template part, or inline in a child theme) — this requires a developer/theme-file edit, not a wp-admin change, and should be flagged as such so the implementation step correctly scopes the effort (and correctly triggers CLAUDE.md rule 5's "no live file edits without explicit approval").
     - Note in the finding which of these applies for each inconsistent instance found, so the Implementation Steps field of the resulting finding is actually actionable rather than a generic "update the NAP."

2. **Contact page audit.**
   - Confirm a dedicated, easy-to-find Contact page exists with full address, phone, WhatsApp (if used), email, business hours, and ideally an embedded map.
   - Check click-to-call (`tel:`) and WhatsApp (`wa.me`) links are actually functional (not just displayed as plain text) — this directly supports the "Improve phone and WhatsApp contacts" goal in CLAUDE.md.

3. **Service-area clarity.**
   - Determine whether the firm serves a specific city/region, a state, or nationally/internationally (relevant given NRI Taxation is a listed priority service, implying some non-local/international audience alongside local clients).
   - Check whether service pages and schema (`areaServed`) reflect this accurately — don't invent a service area; use only what the site or user confirms.

4. **Google Business Profile check** (only if accessible this session):
   - Category selection appropriateness (e.g., "Tax Consultant," "Accountant," "Chartered Accountant" — check what's actually set).
   - NAP consistency between GBP and website.
   - Completeness (hours, services listed, photos, description).
   - Reviews — note count/rating only if actually retrievable via a real tool; never estimate or invent a rating.
   - Posts/Q&A activity if visible.
   - If GBP is not accessible via any connector, explicitly instruct the user this needs to be checked directly in Google Business Profile Manager, and mark all GBP-specific line items `DATA NOT AVAILABLE`.

5. **Local content signals.**
   - Check whether service pages naturally reference the service area/city where relevant (without keyword-stuffing) — a common gap when a site is written in a generic, placeless tone despite serving a specific region.
   - Check for any location-specific landing pages if the firm serves multiple distinct areas (only relevant if applicable — don't recommend multi-location pages for what may be a single-office firm without confirming this first).

6. **Local schema markup** — coordinate with [schema-audit](schema-audit.md): confirm `ProfessionalService`/`LocalBusiness` schema includes accurate `address`, `telephone`, `geo` (if used), and `areaServed`, matching on-site NAP exactly.

7. **Citations/directories** — this skill can note the *concept* (consistency of NAP across directories like Justdial, Sulekha, industry-specific CA directories, etc. matters for local SEO) but should not claim to have checked third-party directories unless a tool was actually used to verify them; if not checked, state so plainly rather than implying comprehensive citation audit was done.

8. **Mobile click-to-contact prominence** — cross-reference [cro-audit](cro-audit.md): on mobile, are phone/WhatsApp actions prominent (e.g., sticky call button) given local searchers on mobile often want immediate contact rather than form-filling?

## What Checks to Perform

- [ ] NAP consistency verified across all on-site locations
- [ ] Contact page complete and functional (tel:/wa.me links working)
- [ ] Service area claims checked against actual site/schema content (nothing invented)
- [ ] GBP checked if accessible; explicitly marked DATA NOT AVAILABLE if not
- [ ] Local content signals reviewed on priority service pages
- [ ] Local schema (address/telephone/areaServed) cross-checked against on-site NAP
- [ ] Mobile click-to-contact prominence assessed

## How to Identify Issues

NAP inconsistency is found by direct comparison of every instance found on-site (and in schema) — any discrepancy, however small (e.g., "+91 98XXXXXXXX" vs "098XXXXXXXX" formatting, or an old address vs current), is a finding. Non-functional tel:/wa.me links are found by inspecting the actual `href` attributes during crawl, not just visually.

## Evidence to Collect

- Direct quotes of every NAP instance found, with source (URL/schema block), saved to `data/crawl/nap-instances.md`.
- GBP screenshots/export if accessible, saved to `data/gsc/` or a dedicated local folder if the project later needs one (until then, note in reports).
- Confirmation (or failure) of tel:/wa.me link functionality, with the exact href values found.

## How to Prioritize Issues

- **CRITICAL:** Non-functional or missing click-to-call/WhatsApp links (directly blocks the "phone and WhatsApp contacts" goal); significantly inconsistent NAP that could confuse or lose potential clients.
- **HIGH:** Missing/incomplete GBP optimization (if accessible and found lacking); no local schema markup at all.
- **MEDIUM:** Minor NAP formatting inconsistencies; generic/placeless service page content when local relevance would help.
- **OPPORTUNITY:** Location-specific landing pages (only if genuinely warranted by a multi-area service model); citation-building (flagged conceptually, actual execution outside this project's direct tooling unless specified otherwise).

## Implementation Recommendations

- Specify the exact correct NAP to standardize on (confirm with the user which version is authoritative before prescribing — do not guess which of several found variants is "correct").
- For GBP changes, since this project only has "verify what's accessible" capability confirmed, most GBP recommendations will need to be executed by the user directly in GBP Manager unless a working connector is confirmed — say so explicitly.
- For tel:/WhatsApp link fixes, give the exact correct href format (`tel:+91XXXXXXXXXX`, `https://wa.me/91XXXXXXXXXX`) once the correct number is confirmed with the user.

## How to Validate Fixes

- Re-crawl to confirm NAP consistency across all instances after correction.
- Manually test tel:/WhatsApp links function correctly on both desktop and mobile rendering.
- Re-check schema validity after any NAP/schema update (cross-ref [schema-audit](schema-audit.md) validation steps).
- If GBP was updated, ask the user to confirm the change reflects correctly in Google Business Profile Manager, since this project cannot independently verify GBP without confirmed tool access.

## Expected Output Format

A finished local SEO audit primarily feeds the CLAUDE.md finding template's **Evidence**, **Affected URLs**, and **Implementation Steps** fields (the latter driven by which WordPress storage location applies per instance, per Step 1 above). Structure the core deliverable as:

1. **NAP instance table** (also saved to `data/crawl/nap-instances.md`):

   | NAP Field | Value Found | Source | Consistent Across Site? | Matches Schema? |
   |---|---|---|---|---|
   | e.g. Phone | e.g. +91 98XXXXXXXX | Footer / Contact page / schema block (URL) | Y/N | Y/N/N/A |

2. **WordPress storage-location note** per inconsistent instance (Customizer / widget / page-builder page / hardcoded template) so implementation steps are correctly scoped.
3. **GBP section explicitly marked either "reviewed" (with findings) or `DATA NOT AVAILABLE`** — never silently omitted.
4. **One finding block per inconsistency/gap**, in the CLAUDE.md required template format, for anything MEDIUM or above.

## Common Mistakes to Avoid

- **Standardizing NAP on whichever variant appears most frequently on-site, without confirming it's actually current.** Frequency is not correctness — an old address can appear on more legacy blog posts/pages than a newer, correct one that only exists on the current Contact page and schema. Always confirm with the user before prescribing which variant to standardize on.
- **Assuming GBP is accessible because CLAUDE.md's project snapshot lists it as "the user believes is connected."** CLAUDE.md is explicit that this table is not confirmation — attempt the actual tool call every session.
- **Prescribing "edit the footer NAP" as one generic instruction** when the actual fix requires either a two-minute wp-admin widget edit or a developer template-file change — always identify which applies first (Step 1).
- **Inferring service area from generic marketing copy** (e.g., "serving clients nationwide") without checking whether that's substantiated elsewhere on the site or confirmed by the user — don't invent or assume a service area.
- **Treating a visually present map embed as proof of correct address** — the embedded map's pinned location can drift from the current NAP address if the site was never updated after an office move; cross-check the actual embed coordinates/address string against the current NAP, don't just confirm a map exists.
- **Recommending multi-location landing pages by default** for a firm that may operate from a single office — only recommend this if a genuine multi-area service model is confirmed, per Step 5.
- **Reporting a GBP rating/review count from memory or from a general sense of "CA firms this size usually have X reviews"** — this is inventing data; if GBP isn't accessible, say so.
