# Skill: CRO (Conversion Rate Optimization) Audit

## Purpose

Close the final gap in the success journey from CLAUDE.md — turning engaged visitors into form submissions, genuine enquiries, and phone/WhatsApp contacts. SEO can bring the right traffic to the right page, but if the page doesn't convert, none of the earlier work pays off. This skill focuses specifically on conversion mechanics and friction, not rankings or traffic.

## Scope

**This skill owns:** conversion mechanics and friction on pages that are already being tracked — CTA presence/clarity/placement, form field friction, confirmation states, phone/WhatsApp prominence, and trust-signal proximity to the conversion point.

**This skill explicitly depends on** [gtm-conversion-audit](gtm-conversion-audit.md) having confirmed tracking actually works, and on [ga4-analysis](ga4-analysis.md) for real conversion-rate data. CRO findings are only as confident as that dependency — see Data Sources & Limitations and Pre-Audit Checks below.

**This skill does NOT own** (route to the owning skill instead):
- Traffic volume or ranking diagnosis for why a page isn't getting visitors in the first place — [gsc-analysis](gsc-analysis.md)/[ga4-analysis](ga4-analysis.md). CRO-audit assumes the visitor already arrived; it does not diagnose why more/fewer visitors arrive.
- Whether conversion events are firing correctly at all — [gtm-conversion-audit](gtm-conversion-audit.md). CRO-audit consumes that skill's "tracking confirmed working" status as a precondition; it does not itself debug tags/triggers.
- Content depth/accuracy of the page copy — [content-audit](content-audit.md). CRO-audit judges CTA/form/trust-signal *mechanics and placement*, not whether the surrounding service explanation is deep or accurate enough.
- Title/meta/heading optimization — [on-page-seo](on-page-seo.md).
- NAP correctness and tel:/wa.me `href` accuracy as a local-SEO/schema concern — [local-seo](local-seo.md); CRO-audit checks that these links are prominent and functional as a *conversion* mechanism, and cross-references local-seo rather than re-verifying NAP correctness itself.
- Site speed/Core Web Vitals as a technical concern — [performance-audit](performance-audit.md), even though slow load can itself be a conversion killer; CRO-audit may note the symptom but routes the diagnosis there.
- Independent competitor CTA/conversion profiling — [competitor-analysis](competitor-analysis.md); CRO-audit consumes that skill's output as a comparison input.

## When to use it

- After [ga4-analysis](ga4-analysis.md) identifies priority pages with traffic but low/no conversions.
- After [gtm-conversion-audit](gtm-conversion-audit.md) confirms tracking is actually working (don't run a CRO diagnosis on unreliable conversion data — fix measurement first).
- When [competitor-analysis](competitor-analysis.md) reveals competitors using stronger conversion mechanisms.
- As part of a full audit cycle, on every priority service page regardless of current performance, since CRO issues are often invisible in aggregate traffic/ranking data.

## Required Data

- Confirmed-working conversion tracking ([gtm-conversion-audit](gtm-conversion-audit.md)) and actual conversion rate data per page ([ga4-analysis](ga4-analysis.md)).
- Live rendering of priority pages (via crawl or, ideally, actual browser rendering if available, since CRO issues like above-the-fold layout, sticky elements, and form friction are often only visible in rendered view, not raw HTML).
- Knowledge of the form plugin in use ([wordpress-seo](wordpress-seo.md)) to assess form field friction accurately.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- Live/rendered page content via WebFetch/crawl — CTA copy, form field structure, visible trust signals, phone/WhatsApp link presence, all as literally rendered.
- Form plugin identification from [wordpress-seo](wordpress-seo.md) findings, if that audit has been run.
- tel:/wa.me `href` correctness, cross-referenced from [local-seo](local-seo.md)'s NAP findings.

### DATA NOT AVAILABLE (mark explicitly, downgrade findings accordingly — do not fill the gap)
- This skill's quantitative findings **depend entirely** on [gtm-conversion-audit](gtm-conversion-audit.md) having confirmed tracking is actually working, and on [ga4-analysis](ga4-analysis.md) having actually pulled live conversion-rate data this session. If either is unavailable or not yet run this cycle:
  - Any "high traffic + low conversion" style finding must be **downgraded to qualitative/inspection-only**, explicitly labeled **OPPORTUNITY tier, lower-confidence** rather than presented as data-confirmed. Do not phrase an inspection-only finding using data-sounding language (e.g., avoid "this page converts poorly" when no conversion data was actually pulled — say instead "this page has a CRO defect by inspection; conversion-rate impact is unverified because GA4/GTM data was not available this session").
  - State plainly in the finding's Evidence field which of the two dependencies (tracking confirmed, GA4 data pulled) was and wasn't available.
- A/B test result data — this project has no confirmed A/B testing tool; frame recommendations as "implement and monitor over N weeks" (see Step 8), never as if a formal test was run.
- Competitor conversion-rate data — never available; [competitor-analysis](competitor-analysis.md) can note visible competitor conversion *mechanisms* (a WhatsApp button exists), never competitor conversion *rates*.

## Pre-Audit Checks

Before starting the step-by-step process below, confirm:

1. **Check whether [gtm-conversion-audit](gtm-conversion-audit.md) has actually been run this cycle**, and if so, whether it confirmed tracking is working or found it broken/unverified. This single fact determines the confidence tier every downstream CRO finding on this page can carry.
2. **Check whether [ga4-analysis](ga4-analysis.md) has pulled live conversion/engagement data this cycle** for the pages being audited. If not, proceed with inspection-only CRO review but flag every quantitative-sounding finding per the Data Sources & Limitations rule above.
3. If both are unknown/unverified, say so explicitly at the start of the audit output rather than silently defaulting to inspection-only without telling the user why.

## Step-by-Step Audit Process

1. **Above-the-fold audit** on each priority service page:
   - Is it immediately clear what service the page is about and who it's for?
   - Is a clear call-to-action (enquiry form, phone, WhatsApp) visible without scrolling, or does the user have to hunt for it?
   - Is there a trust signal near the top (credentials, years of experience, client count) that reduces hesitation for a financial-services decision?

2. **Call-to-action inventory and clarity.**
   - List every CTA on the page (form, tel: link, WhatsApp link, email, chat widget).
   - Assess clarity of CTA copy (generic "Submit" vs. specific "Get a Free GST Registration Consultation") — specific, service-relevant CTA copy typically outperforms generic copy, especially for a considered financial/compliance decision.
   - Check CTA visual prominence (contrast, size, placement) at a basic level from rendered HTML/CSS if visible.

3. **Form friction audit.**
   - Number of required fields — every additional required field is a known point of drop-off; check if the form asks for more than necessary for an initial enquiry (e.g., does it really need to ask for a full financial history upfront, or would name/contact/brief need suffice to start a conversation?).
   - Field types and validation behavior (does validation block submission unclearly? Any evidence of the form being difficult to complete on mobile — small tap targets, no numeric keyboard for phone field, etc.?).
   - Presence of unnecessary CAPTCHA friction or multi-step complexity beyond what spam protection requires.
   - Confirm a clear success/confirmation state exists after submission (a form with no visible confirmation creates doubt about whether the enquiry was received — bad for trust and for measurement).

4. **Phone/WhatsApp prominence.**
   - On mobile specifically, is a sticky or persistent call/WhatsApp button present, or does the user have to scroll back up? Many local-intent CA searches on mobile favor an immediate call/WhatsApp over filling a form — check whether the page accommodates that preference.
   - Confirm tel:/wa.me links are correctly formatted and functional (cross-ref [local-seo](local-seo.md) NAP check).

5. **Trust and objection-handling near the CTA.**
   - Are trust signals (testimonials, certifications, "your data is confidential," response-time expectations like "we respond within 24 hours") present near the conversion point, not just buried elsewhere on the page? Financial/compliance services carry higher perceived risk, so proximity of trust signals to the CTA matters more than for a low-stakes purchase.

   ### Trust Signal Placement for Financial Services

   CA/tax clients are unusually risk-averse for a services purchase — they are trusting a stranger with tax filings, financial records, and compliance obligations that carry personal legal/financial consequences if mishandled. What reduces hesitation for this audience specifically, in rough priority order for proximity to the CTA:

   1. **ICAI/CA registration number and credentials** — a verifiable professional-body registration is the single strongest trust signal for this vertical; check whether it's visible near the enquiry point, not just buried on an About page.
   2. **Years in practice / firm tenure** — concrete ("15+ years serving clients") outperforms vague ("experienced team").
   3. **Data confidentiality assurance** — an explicit statement addressing that financial/tax data shared via the form will be handled confidentially; its absence is a real objection-handling gap for this audience, not a nice-to-have.
   4. **Response-time commitment** — "we respond within 24 hours" or similar sets a concrete expectation and reduces the anxiety of "did this actually go through and will anyone reply."
   5. **Clear "what happens after you submit" expectation-setting** — a brief note (near the form or on the confirmation state) on the next step (e.g., "a team member will call you within one business day to understand your requirement") measurably reduces perceived risk of submitting personal/financial information to an unfamiliar form.

   **What does NOT apply to this vertical** — do not recommend generic e-commerce CRO tactics here, and flag them if found in use, since they actively undermine trust for a considered financial/compliance decision:
   - Urgency countdown timers ("offer ends in 2 hours") — inappropriate for professional services and reads as manipulative for a tax/compliance context.
   - Fake scarcity ("only 3 slots left this month") — not credible for a professional-services firm and damages trust if noticed as implausible.
   - Aggressive exit-intent popups pushing a discount — discounting a CA/compliance engagement this way undercuts the professional positioning the firm needs for a high-trust sale.

6. **Page-specific conversion path check.**
   - For each priority service, does the page's CTA correctly match the service (a GST Registration page shouldn't funnel to a generic "Contact Us" with no context — ideally the enquiry form is pre-contextualized, e.g., a hidden field or subject line noting which service was of interest, which also makes leads easier for the firm to triage as "genuine enquiries" per the CLAUDE.md goal).

7. **Funnel drop-off analysis** (using [ga4-analysis](ga4-analysis.md) data): where in the page/session do users disengage before reaching a conversion action? If GA4 event-level or scroll-depth data is available, use it; otherwise rely on engagement time/exit data as a proxy and label it clearly as indirect evidence.

8. **A/B or before/after framing for recommendations** — this skill should propose testable changes, but note that actually running a formal A/B test requires tooling/traffic volume the project may not currently have; if not available, frame recommendations as "implement and monitor conversion rate over N weeks" rather than assuming true A/B testing capability exists.

## What Checks to Perform

- [ ] Above-the-fold clarity and CTA visibility checked per priority page
- [ ] All CTAs inventoried with copy/prominence assessed
- [ ] Form field count and friction assessed against genuine necessity
- [ ] Mobile form usability specifically checked
- [ ] Confirmation/success state after submission confirmed present
- [ ] Phone/WhatsApp prominence checked, especially mobile
- [ ] Trust signals checked for proximity to CTA, not just presence somewhere on page
- [ ] CTA context-matching to specific service checked
- [ ] GA4 funnel/engagement data reviewed for drop-off signal, where available

## How to Identify Issues

Compare each priority page against the checklist directly by reading its rendered content. A CRO issue is confirmed most strongly when it's paired with matching GA4 evidence (e.g., high traffic + low engagement time + low conversion rate on a page found to have a below-the-fold, generic-CTA form) — flag issues found by inspection alone as OPPORTUNITY/lower confidence if no corroborating GA4 data exists, and be explicit about that distinction in the finding.

## Evidence to Collect

- Rendered-page excerpts/screenshots showing CTA placement and form structure.
- Exact CTA copy quoted.
- Form field list (as actually present, from HTML inspection).
- Corroborating GA4 metrics for the specific page (engagement rate, conversion rate) pulled per [ga4-analysis](ga4-analysis.md), cited directly rather than paraphrased.
- Save findings to `data/ga4/` (metrics) and reference directly in `reports/` (qualitative CRO findings can live in the report itself, since they're primarily judgment calls anchored to evidence rather than raw exportable data).

## How to Prioritize Issues

- **CRITICAL/HIGH:** No functional CTA above the fold on a high-value priority page; broken/missing form confirmation state; excessive form friction on the primary enquiry form; confirmed (via GA4) high-traffic page with near-zero conversion correlating with a clear CRO defect.
- **MEDIUM:** Generic (non-service-specific) CTA copy; trust signals present but not proximate to CTA; suboptimal but functional mobile call/WhatsApp prominence.
- **OPPORTUNITY:** Untested copy/design improvements without corroborating drop-off data; incremental form UX polish.

## Implementation Recommendations

- Propose specific, concrete changes: exact revised CTA copy, specific fields to remove/keep, specific placement change (e.g., "add a sticky mobile call/WhatsApp bar" — note this is typically a small theme/plugin-level change, confirm feasibility via [wordpress-seo](wordpress-seo.md) findings on active plugins/theme).
- Any change to the live form (fields, plugin settings) must follow CLAUDE.md rule 5/7 — propose first, implement only after explicit approval, and note that form changes should be tested (submit a real test entry) before considering the change complete.

## How to Validate Fixes

- Confirm the change is live via a direct site check (rendered page, working confirmation state, working tel:/wa.me links).
- Track conversion rate for the specific page in [ga4-analysis](ga4-analysis.md) over a meaningful post-change window (at least 2-4 weeks, more for lower-traffic pages, to get a reliable sample), comparing against the documented pre-change baseline.
- Where feasible, track lead quality qualitatively with the user (e.g., "are the enquiries coming through more relevant/complete since the form was simplified?") since "genuine enquiries" per CLAUDE.md's goal is a quality measure GA4 alone can't fully capture.

## Expected Output Format

A finished CRO audit primarily feeds the CLAUDE.md finding template's **Evidence**, **SEO Impact** (mapped explicitly to the Engagement → Form Submission/Contact → Genuine Enquiry stages of the success journey), and **Validation Method** fields. Structure the core deliverable as:

1. **Per-page CRO table**:

   | Page | CTA Present Above Fold? | Form Field Count | Confirmation State? | Mobile Call/WhatsApp Prominence | Confidence (Data-backed/Inspection-only) |
   |---|---|---|---|---|---|
   | e.g. GST Registration | Y/N | e.g. 6 | Y/N | High/Medium/Low/Absent | Data-backed / Inspection-only |

   "Confidence" must be filled per the Data Sources & Limitations rule — never mark "Data-backed" unless GTM tracking and GA4 conversion data were both actually confirmed and pulled for that specific page this cycle.

2. **One finding block per confirmed defect**, in the CLAUDE.md required template format.
3. **A separate Trust Signal Placement checklist** per priority page (per the subsection above), since this is a recurring, vertical-specific check worth tracking consistently across pages rather than folding into ad hoc findings only.

## Common Mistakes to Avoid

- **Recommending a form so simplified it stops collecting what the firm needs to triage a genuine enquiry from spam/junk.** CLAUDE.md's goal is *genuine* enquiries, not just raw submission volume — cutting a "which service are you enquiring about" field to reduce friction can backfire by making every lead harder to triage, which works against the actual business goal.
- **Presenting an inspection-only finding as if it were GA4-confirmed** — always state the confidence tier explicitly (see Data Sources & Limitations); don't let a CRITICAL/HIGH severity implicitly borrow credibility from data that wasn't actually pulled.
- **Applying generic e-commerce CRO patterns** (urgency timers, fake scarcity, aggressive discount popups) to a CA/tax firm — these actively damage trust for this audience; see Trust Signal Placement for Financial Services above.
- **Recommending a design/CTA change without checking [gtm-conversion-audit](gtm-conversion-audit.md) status first** — a "low conversion" diagnosis built on broken tracking is not a real diagnosis; verify measurement before diagnosing the page.
- **Ignoring mobile-specific behavior** — a desktop-only rendered check will miss that a local CA searcher on mobile strongly prefers immediate call/WhatsApp over a form; always check mobile rendering and tap-target usability separately.
- **Proposing a live form/plugin change without explicit approval** or skipping the post-change test submission — both violate CLAUDE.md rules 5/7 and the validation step in this skill.
- **Treating "trust signal present somewhere on the page" as sufficient** — proximity to the CTA is the actual requirement for this risk-averse audience; a testimonial buried in a footer doesn't do the same job as one near the form.
