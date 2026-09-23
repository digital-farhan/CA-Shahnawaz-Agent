# Skill: GA4 Analysis

## Purpose

Understand how real visitors actually behave on cashahnawaz.com after they arrive — engagement, on-site journeys, drop-off points, and (most importantly for this project) conversion behavior tied to form submissions and contact actions. This is the "Engagement → Form Submission / Contact" stage of the success journey in CLAUDE.md.

## Scope

This skill covers analysis of data sourced from Google Analytics 4 (property `546098812`) for cashahnawaz.com: sessions, users, engagement, channel grouping, landing pages, on-site behavior/drop-off, conversion events, and device/audience breakdowns for traffic that has already arrived on the site. It answers "once a visitor lands, what do they actually do, and does that lead to a genuine enquiry."

This skill does NOT cover:
- Pre-click search visibility (queries, impressions, CTR, average position, indexing) — that's [gsc-analysis](gsc-analysis.md); GA4 only sees traffic that already clicked through.
- **Whether** tags/triggers are configured correctly to fire the events this skill reports on — verifying GTM container setup, trigger logic, and tag firing is [gtm-conversion-audit](gtm-conversion-audit.md). This skill treats GA4's reported event volume as the input and flags implausible volume (e.g., zero `form_submit` events) as a signal to hand off to that skill, but does not itself inspect the GTM container.
- On-page content quality, structure, or keyword targeting — [on-page-seo](on-page-seo.md) and [content-audit](content-audit.md); this skill only reports the behavioral symptom (e.g., high traffic + low engagement time) and hands off the diagnosis.
- Technical crawlability/indexability — [technical-seo](technical-seo.md) / [website-crawl](website-crawl.md).
- Structured data — [schema-audit](schema-audit.md).
- WordPress plugin/theme implementation detail — [wordpress-seo](wordpress-seo.md).
- Site speed as a root cause — [performance-audit](performance-audit.md) owns Core Web Vitals measurement; this skill only notes correlated engagement gaps (e.g., mobile engagement lagging desktop) as a cross-reference.
- Competitor traffic/behavior — competitors have no GA4 access available; that gap is [competitor-analysis](competitor-analysis.md)'s to work around with public-signal methods, not this skill's.
- Local Pack/Maps visibility and NAP consistency — [local-seo](local-seo.md).
- The design/UX/persuasion fixes for a diagnosed conversion problem — [cro-audit](cro-audit.md) owns the fix once this skill has identified where in the funnel traffic is lost.

In short: this skill is the "Engagement → Form Submission / Contact" evidence layer in the CLAUDE.md success journey. It identifies symptoms in visitor behavior and conversion volume and routes the underlying cause (tracking, content, technical, CRO) to the named skill.

## When to use it

- To measure whether organic traffic is actually engaging (not just arriving and bouncing).
- To find which priority service pages convert visitors into enquiries and which don't.
- To diagnose where users drop off before submitting a form or clicking to call/WhatsApp.
- Before writing any claim about sessions, users, engagement rate, conversions, or channel performance — this is the only legitimate source for those numbers.

## Data Sources & Limitations

GA4 access to Property ID `546098812` via a working connector/tool in the current session is the only legitimate source for sessions/users/engagement/conversion data. See [Pre-Audit Checks](#pre-audit-checks) for the exact verification procedure to run before trusting any pull this session.

Also required: knowledge of what conversion events are actually configured in GA4 (from [gtm-conversion-audit](gtm-conversion-audit.md) findings) — GA4 analysis and GTM audit should be done together or in sequence, since GA4 can only report on events GTM/gtag is actually sending.

### AVAILABLE WITH LIVE CONNECTOR

If a working GA4 connector is confirmed this session, the following becomes available:
- Core metrics (Users, New Users, Sessions, Engaged Sessions, Engagement Rate, Average Engagement Time, Views) segmented by Default Channel Group, source/medium, landing page, device category, and date, typically at daily granularity.
- Standard historical lookback (commonly up to 14 months of retained event-level data, subject to the property's configured data retention setting — verify the actual retention setting rather than assuming 14 months).
- Event-level reports: any event GA4 is actually recording (e.g., `form_submit`, `generate_lead`, `phone_click`, `whatsapp_click`, `click`, `page_view`, `session_start`), with event count and, where marked as a conversion, conversion count and (if e-commerce/value is configured, which is unlikely for a service firm) event value.
- Landing page and full page path reports, combinable with channel/source filters (e.g., Organic Search only).
- Audience breakdowns: new vs. returning, device category, and (if configured) user properties.
- Realtime report, useful for confirming an event fires immediately after a tracking fix (see How to Validate Fixes).
- Explorations (funnel exploration, path exploration) if the connector supports pulling Exploration data — useful for real drop-off/funnel visualization rather than inferring it from separate reports.

### DATA NOT AVAILABLE (no connector)

If no GA4 connector works this session (verification attempt fails, returns an error, or returns data from a property other than `546098812`), every one of the following must be marked `DATA NOT AVAILABLE` — Claude must never estimate, infer, or backfill these numbers from GSC click volume, crawl data, competitor traffic assumptions, industry-typical conversion rates, or any prior session's cached numbers, no matter how plausible the substitute would look:
- Actual sessions, users, engagement rate/time, or channel split for any period.
- Actual conversion event names, volumes, or rates for any page or channel.
- Actual landing page performance or organic-specific behavior.
- Any service → traffic → conversion mapping table — this is entirely derived from the above and inherits its unavailability.
- Device/audience breakdowns.
- A "reasonable guess" that a page "probably converts well because it ranks well in GSC" is not a substitute — GSC and GA4 measure different things (search behavior vs. on-site behavior) and one cannot stand in for the other.

### Known limitations even when the connector works

- **Thresholding/data withholding on small segments**: GA4 automatically withholds or thresholds data for low-volume segments (common for a service-business site with modest traffic per individual priority-service page), especially in demographic/audience breakdowns. A "0" or missing row may mean thresholded, not truly zero — check for GA4's own thresholding indicator before reporting a hard zero.
- **Attribution model dependency**: conversion counts (especially in "Conversions" vs. raw "Event count") depend on the attribution model configured for the property (data-driven, last-click, etc.); a channel's conversion credit can shift materially if the model changes — always note which model/report type (Events vs. Conversions vs. Advertising attribution) the pulled numbers come from.
- **Default Channel Group misattribution risk**: traffic can be silently reclassified out of Organic Search into Direct/Referral/Unassigned due to UTM/GTM misconfiguration or referrer-stripping (see Common Mistakes) — treat channel-split numbers as provisional until cross-checked.
- **Processing lag**: GA4 standard reports typically have a processing delay of several hours up to about a day (Realtime is near-instant but only covers roughly the last 30-60 minutes and a limited metric set) — do not treat "missing from today's standard report" as "event isn't firing" without also checking Realtime.
- **Sampling on ad hoc/Exploration queries**: high-cardinality or long-date-range Exploration queries can be sampled; the standard predefined reports generally are not, so prefer standard reports for headline numbers and treat Exploration numbers as directional.
- **GDPR/consent-mode considerations**: cashahnawaz.com serves an India-based audience where India's DPDP framework doesn't mandate the EU-style consent-before-tracking pattern the way GDPR does, but if any consent banner/plugin is present (or if EU/UK visitors reach the site and a consent-mode signal is respected), Google's consent mode can suppress or model traffic for consent-pending users — check whether a consent-management plugin is active on the WordPress site before assuming full traffic capture.

## Pre-Audit Checks

Run these before starting the substantive audit (Step 1 below formalizes the first one, but do all of these first):

- [ ] Attempt one real GA4 data pull (e.g., a 7-day Users/Sessions report) and inspect the actual property ID in the response object — confirm it literally reads `546098812`, not a GA4 demo property, a different client's property the same account can access, or a Universal Analytics leftover. Do this before trusting any further pull this session.
- [ ] Confirm the date range default isn't silently empty (e.g., a report requested for "yesterday" on a property with a processing lag can return zero rows that look like "no traffic" rather than "not processed yet") — validate against a window with known historical activity first.
- [ ] Confirm which data stream(s) exist on the property (web stream for cashahnawaz.com; check there isn't an unrelated second stream diluting or splitting numbers) and that the audit is reading the correct stream's data, not an app stream or a staging/dev stream if one exists.
- [ ] Check for a WordPress consent-management/cookie-consent plugin (e.g., CookieYes, Complianz) that could be suppressing GA4 tag firing for some visitors via consent mode — this would undercount real traffic even though India doesn't legally require it; note whether it's present and configured to block-by-default before trusting raw totals as complete.
- [ ] Confirm the conversion events expected for this business (form submissions, phone clicks, WhatsApp clicks — tied to the CLAUDE.md "Form Submission / Contact" and "Genuine Enquiry" funnel stages) are marked as "key events"/conversions in GA4 admin, not just recorded as raw events — a real event that isn't marked as a conversion won't appear in Conversions-scoped reports even though it's firing.
- [ ] Note today's date (2026-08-27) relative to India's tax filing calendar (ITR/GST deadlines) — GA4 traffic and conversion swings around these dates are seasonal for a CA firm; don't attribute a post-deadline traffic drop to a site issue without checking prior-year seasonality first.
- [ ] Confirm whether Google Ads or any paid channel has ever run — if so, make sure Organic Search isolation in step 2 isn't accidentally including Paid Search or Paid Social sessions due to a channel-grouping misconfiguration.

## Step-by-Step Audit Process

1. **Verify access and property.** Confirm the pull is against property 546098812.

2. **Traffic overview.**
   - Pull Users, Sessions, Engaged Sessions, Engagement Rate, Average Engagement Time, by channel, for a trailing window (start 90 days, extend if useful for trend/seasonality — tax season timing matters for a CA firm, note any seasonal pattern e.g. around ITR filing deadlines).
   - Isolate the **Organic Search** channel specifically — this is what SEO work directly influences.

3. **Landing page analysis (Organic Search only).**
   - Pull top landing pages by organic sessions.
   - Cross-reference against the priority services list: which priority service pages receive meaningful organic landing traffic, and which get none?
   - For each priority landing page, pull: engagement rate, average engagement time, bounce/exit behavior, and conversion rate (once conversion events are confirmed — see step 5).

4. **Behavior flow / drop-off.**
   - Identify where users go after landing on a priority service page — do they navigate toward a contact/enquiry action, or exit?
   - Identify pages with high traffic but very low engagement time (possible content/relevance mismatch with the ranking query — cross-check against [gsc-analysis](gsc-analysis.md) query data for that page).

5. **Conversion events.**
   - List all conversion events actually configured in GA4 (e.g., `form_submit`, `generate_lead`, `phone_click`, `whatsapp_click`, `contact`). Do not assume standard event names — confirm what's actually firing by checking the Events report for real event volume.
   - For each, pull volume by channel (isolate organic), and by landing page/service where possible.
   - If expected conversion events (form submit, phone click, WhatsApp click) are **not present at all** in GA4, this is a critical measurement gap — flag it immediately and route to [gtm-conversion-audit](gtm-conversion-audit.md), since it means the business cannot currently measure enquiry volume from organic traffic at all.

6. **Service-level conversion mapping.**
   - For each priority service (CLAUDE.md list), determine: organic sessions to its page(s), engagement rate, and conversion count/rate. Build a simple table service → traffic → conversions so gaps are visible (e.g., "GST Registration gets traffic but zero conversions" vs. "NGO Registration gets neither traffic nor conversions").

7. **New vs. returning, device breakdown** for organic traffic — mobile is typically dominant for local/service search; confirm mobile engagement/conversion isn't lagging desktop significantly (cross-reference [performance-audit](performance-audit.md) mobile CWV if it is).

8. **Site search** (if GA4 site search tracking is enabled) — what are visitors searching for on-site? Gaps here can reveal missing content or navigation issues.

## What Checks to Perform

- [ ] Access verified against correct property ID 546098812
- [ ] Organic Search isolated as its own channel view
- [ ] Top organic landing pages pulled and mapped to priority services
- [ ] Conversion events inventoried (real event names, real volumes — not assumed)
- [ ] Conversion volume/rate pulled by channel and by priority service page
- [ ] Engagement rate/time compared across priority service pages
- [ ] Mobile vs desktop organic performance compared
- [ ] Any priority service with traffic but zero conversions flagged
- [ ] Any priority service with zero organic traffic flagged (cross-ref gsc-analysis)

## How to Identify Issues

- Configured conversion events missing or firing with implausibly low/zero volume = measurement/tracking issue (CRITICAL — you can't optimize what you can't measure).
- High organic traffic + low engagement rate/time on a priority page = relevance or on-page/content issue (cross-file to [on-page-seo](on-page-seo.md) or [content-audit](content-audit.md)).
- Traffic present but conversions absent on a priority service page = CRO issue (route to [cro-audit](cro-audit.md)).
- Large mobile/desktop engagement or conversion gap = mobile UX or performance issue (route to [performance-audit](performance-audit.md)).

## Evidence to Collect

Save to `data/ga4/` with pull date in filename:
- `data/ga4/traffic-overview-YYYY-MM-DD.csv`
- `data/ga4/organic-landing-pages-YYYY-MM-DD.csv`
- `data/ga4/conversion-events-YYYY-MM-DD.csv`
- `data/ga4/service-conversion-mapping-YYYY-MM-DD.csv` (the table built in step 6)

## How to Prioritize Issues

Missing/broken conversion tracking is CRITICAL by default (it blocks measurement of the entire success journey's final stage). Traffic-but-no-conversion on a high-value priority service (e.g., GST Registration, Company Registration) is HIGH. Engagement gaps on lower-commercial-intent pages (e.g., a blog post) are typically MEDIUM/LOW unless the page is a major traffic driver.

## Implementation Recommendations

GA4 findings about *tracking gaps* route to [gtm-conversion-audit](gtm-conversion-audit.md) for the fix. Findings about *conversion rate* on a page with working tracking route to [cro-audit](cro-audit.md). Findings about *engagement/relevance* route to [content-audit](content-audit.md) or [on-page-seo](on-page-seo.md).

## How to Validate Fixes

- After a tracking fix, confirm the event appears in GA4 Realtime report during a test action, then confirm it accumulates in standard reports over the following days.
- After a CRO/content fix, compare the affected page's engagement rate and conversion rate over a matched post-fix window against the pre-fix baseline saved in `data/ga4/`. Allow at least 2-4 weeks given typical traffic volume for a service-business site, and note seasonal factors (e.g., don't compare a post-fix April window against a pre-fix December baseline without noting tax-season seasonality).

## Expected Output Format

This skill primarily feeds the **Evidence**, **Affected URLs**, and **SEO Impact** fields of the CLAUDE.md finding template, and frequently supplies the factual basis for **Likely Root Cause** when a tracking or engagement gap is the cause.

**Tables/CSVs produced**, with exact column headers:

- `traffic-overview-YYYY-MM-DD.csv`: `Date | Channel | Users | Sessions | Engaged Sessions | Engagement Rate | Avg Engagement Time`
- `organic-landing-pages-YYYY-MM-DD.csv`: `Landing Page | Mapped Priority Service | Organic Sessions | Engagement Rate | Avg Engagement Time | Conversions | Conversion Rate`
- `conversion-events-YYYY-MM-DD.csv`: `Event Name | Marked as Key Event (Y/N) | Total Count (All Channels) | Organic Search Count | Trend Note`
- `service-conversion-mapping-YYYY-MM-DD.csv`: `Priority Service | Page URL | Organic Sessions | Engagement Rate | Conversions | Conversion Rate | Verdict (Traffic+Conversions / Traffic No Conversions / No Traffic)`

**In the audit report**, every finding sourced from GA4 should cite the specific CSV and row(s)/date range in the Evidence field (e.g., "Evidence: `data/ga4/service-conversion-mapping-2026-08-27.csv`, row for GST Registration — 143 organic sessions over 90 days, 0 conversions").

**A `DATA NOT AVAILABLE` entry must still use the full finding template**, not be silently dropped. Example shape:

```
### [N/A — DATA NOT AVAILABLE] GA4 connector unavailable this session

- **Issue:** GA4-sourced engagement/conversion data could not be retrieved for property 546098812.
- **Severity:** Cannot be assessed — severity depends on the missing data.
- **Evidence:** DATA NOT AVAILABLE — connector attempt on [date] returned [error/wrong property]. No prior-session data substituted.
- **Affected URLs:** DATA NOT AVAILABLE — cannot determine which priority service pages are converting without landing-page/conversion data.
- **SEO Impact:** Cannot be quantified; blocks assessment of the "Engagement → Form Submission / Contact → Genuine Enquiry" stages for all priority services.
- **Likely Root Cause:** Connector/authentication issue, not a site issue — do not conflate with an actual engagement/conversion problem.
- **Recommended Fix:** Restore GA4 connector access, then re-run this skill.
- **Implementation Steps:** N/A until access restored.
- **Validation Method:** Successful pull returning real property-546098812 data confirms resolution.
```

## Common Mistakes to Avoid

- **Pulling blended, all-channel numbers and drawing an SEO conclusion.** Always isolate Organic Search before saying anything about "traffic is engaging well" or "conversions are up" — a paid campaign, a WhatsApp broadcast, or a branded email blast can move blended numbers with zero SEO involvement.
- **Trusting Default Channel Group without checking for misattribution.** WhatsApp links opened in an in-app browser strip the referrer header on many Android devices, and clicks from the WhatsApp Business catalog or a shared link routinely land in GA4 as Direct or Unassigned rather than the true source — a very common leak for a CA firm that shares links via WhatsApp. Check landing page + source/medium combinations for suspicious concentration in Direct/Unassigned before accepting the channel split at face value.
- **Treating a real but unmarked event as "not converting."** If `form_submit` fires as a raw event but isn't marked as a GA4 key event/conversion, standard Conversions reports will show zero even though the form works — check the raw Events report, not only Conversions, before declaring a tracking gap.
- **Judging a fix's impact before the reporting lag and statistical noise settle.** GA4 processing lag plus normal day-to-day traffic variance on a moderate-traffic service site means a 2-3 day post-fix comparison is noise, not signal — hold to the 2-4 week window this skill specifies, and use a matched prior period, not an arbitrary one.
- **Ignoring ITR/GST seasonality when comparing periods.** Comparing a post-fix window against a pre-fix baseline from a different point in the tax calendar (e.g., post-July-31-ITR-deadline traffic vs. pre-deadline traffic) will misattribute a seasonal swing to the fix.
- **Asserting a precise conversion figure from small-sample, possibly-thresholded data.** If GA4 withholds or approximates a low-volume segment (e.g., WhatsApp clicks from organic on a single service page), report the number with its thresholding caveat rather than stating it as an exact fact in a client-facing report.
- **Confusing "Engaged Sessions"/"Engagement Rate" with actual lead quality.** A high engagement rate on a blog post about tax deadlines doesn't mean commercial intent — always weight engagement findings by the commercial value of the page (priority service pages vs. informational content) rather than treating all engagement equally.
- **Skipping the GTM cross-check before declaring a "measurement gap."** GA4 showing zero for an expected event could be a GA4 configuration issue (event not marked as key event, wrong event name filter) rather than a true tag-firing failure — confirm via [gtm-conversion-audit](gtm-conversion-audit.md) before asserting the tag itself is broken.
