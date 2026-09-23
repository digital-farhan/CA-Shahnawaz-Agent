# Skill: GTM & Conversion Tracking Audit

## Purpose

Verify that Google Tag Manager (container `GTM-N2LHGRCX`) is actually, correctly capturing the enquiry actions that matter for this business: form submissions, phone clicks, and WhatsApp clicks. This skill audits the measurement plumbing itself — it's the prerequisite for trusting any conversion number reported by [ga4-analysis](ga4-analysis.md).

## When to use it

- Before trusting any GA4 conversion figure.
- When GA4 shows zero or implausibly low conversions for a service that clearly gets traffic.
- After any WordPress form plugin change, theme change, or GTM container edit.
- As part of the initial audit, since a broken conversion measurement setup undermines every downstream "increase form submissions / enquiries" goal in CLAUDE.md.

## Scope

This skill owns tag, trigger, variable, and container-level correctness within Google Tag Manager (`GTM-N2LHGRCX`), plus live-fire verification that tags actually execute on real user actions (form submit, phone click, WhatsApp click). It answers one question: **is the measurement plumbing itself actually working?**

It does NOT own:
- Conversion **rate** optimization — why a visitor doesn't submit the form, form UX/friction, button placement/copy, trust signals. That's [cro-audit](cro-audit.md).
- Interpreting GA4 reports, funnels, channel attribution, or traffic/engagement trends once events are confirmed flowing correctly. This skill only goes as far as confirming an event reaches GA4 and looks plausible in volume; deeper GA4 report analysis belongs to [ga4-analysis](ga4-analysis.md).
- Search Console query/impression/click data or Core Web Vitals field data — [gsc-analysis](gsc-analysis.md).
- Page speed / Core Web Vitals measurement and root-cause diagnosis of slowness — [performance-audit](performance-audit.md). (A laggy form hurting INP is a performance-audit finding; a form whose submit never fires a GTM tag is a gtm-conversion-audit finding.)
- The underlying HTML/page inventory of what forms and pages exist — that inventory comes from [website-crawl](website-crawl.md); this skill consumes it rather than producing it.
- General technical SEO — indexability, robots, sitemaps, canonicals: [technical-seo](technical-seo.md).
- On-page content/keyword optimization — [on-page-seo](on-page-seo.md), [content-audit](content-audit.md).
- Internal linking structure — [internal-linking](internal-linking.md).
- Structured data/schema markup — [schema-audit](schema-audit.md).
- Full WordPress plugin/theme inventory and general WP health, beyond identifying the specific form plugin in use (needed to choose the right trigger approach) — [wordpress-seo](wordpress-seo.md) is the reference for the complete plugin inventory.
- Competitor tracking setups — [competitor-analysis](competitor-analysis.md).
- Local SEO / Google Business Profile signals — [local-seo](local-seo.md).

## Data Sources & Limitations

### AVAILABLE WITH LIVE CONNECTOR / TOOL (GTM container access confirmed working this session)
- Full list of tags, triggers, and variables, and whether the currently published version matches the latest workspace edits.
- Trigger firing logic/conditions exactly as configured (selectors, event names, "Wait for Tags"/"Check Validation" settings).
- GTM Preview/Debug mode showing real-time tag firing during a live test interaction (if a real browser interaction is also possible).
- Version history, enabling a true before/after comparison once a fix is published.
- Confirmation of exactly which GA4 Measurement ID a GA4 Configuration tag points to, and whether it matches property `546098812`.

### AVAILABLE VIA LIVE-SITE INSPECTION ONLY (no container access, but fetching the live site's HTML works)
- Presence and correct placement of the GTM snippet — `<head>` script and the noscript `<body>` fallback — and whether the container ID matches `GTM-N2LHGRCX`.
- Presence of `tel:` and `wa.me` hrefs in the rendered HTML (proves the links exist — not that clicks on them are tracked).
- Any `dataLayer` push visible directly in raw HTML/inline `<script>` source (a hardcoded `dataLayer.push({...})`) — this only catches static pushes baked into the page, not ones triggered dynamically by user interaction.
- Which form plugin is in use, inferable from form markup/class names/enqueued asset URLs (e.g., `wpcf7`-prefixed classes for Contact Form 7, `wpforms-form` for WPForms, `gform_wrapper` for Gravity Forms).

### DATA NOT AVAILABLE (no connector/tool, or no real interaction capability)
Must be explicitly marked `DATA NOT AVAILABLE` / `NOT VERIFIABLE` rather than inferred:
- Whether a tag actually fires on a real form submission, phone click, or WhatsApp click. The presence of a `tel:`/`wa.me` link or a GTM snippet is **not** proof the click is tracked.
- Actual trigger logic/conditions inside GTM, if container access isn't available — never guess what trigger type "probably" exists from external symptoms alone.
- Whether events reach GA4 with plausible volume — this requires either container access plus a live test, or a working GA4 connector (see [ga4-analysis](ga4-analysis.md)).
- Whether a consent banner/consent mode is blocking tag firing pre-consent — this requires container inspection or a live interaction test in an unconsented browser state.
- Historical firing reliability (was it ever working, when did it break) — this needs GTM version history or GA4 historical data; never assume "it's probably always been broken" or "probably fine since it's published."

Claude must never: declare a tag "working" solely because it appears configured in GTM; estimate conversion volume from general traffic assumptions; assume a WordPress form "probably" pushes to `dataLayer` because "most plugins do this now"; or treat the mere existence of a phone/WhatsApp link as evidence it is being tracked. Every firing claim needs container Preview-mode evidence, a live test result, or corroborating GA4 event data — absent all three, mark it `DATA NOT AVAILABLE`.

## Pre-Audit Checks

Before starting the workflow below, confirm:

1. **Which access mode is actually available this session.** Attempt a real GTM container API call (e.g., list containers/workspaces) rather than assuming access just because CLAUDE.md lists a container ID. If that fails, attempt a live HTML fetch of the homepage to confirm at least snippet-level inspection is possible. Choose audit depth accordingly and state which mode is in effect at the top of the findings.
2. **Confirm you are looking at the PUBLISHED container version, not a draft workspace.** GTM workspaces can hold unpublished changes that look correct but aren't live — always evaluate the live/published container, and separately flag if a workspace has unpublished changes pending (a known fix sitting unpublished is itself a finding).
3. **Identify the actual form plugin(s) in use before assuming which trigger type/approach applies.** Contact Form 7, WPForms, and Gravity Forms behave differently (see Implementation Recommendations below). Determine this via live markup inspection (class names, script handles), not by guessing "most WordPress CA sites use X."
4. **Check for more than one form plugin or form instance type** — a site can run a main Contact Form 7 page form plus a separate WPForms popup, each needing its own trigger logic.
5. **Note whether a cookie consent banner is present before testing** — its state (consented vs. not) affects whether tags fire during your test; test both states if consent mode is in use.

## Step-by-Step Audit Process

1. **Verify GTM snippet is live.** Fetch the site's HTML and confirm the GTM container snippet (`GTM-N2LHGRCX`) is present in both the `<head>` and `<body>` (noscript) as Google's install pattern requires. A missing noscript tag or wrong container ID is itself a finding.

2. **Inventory what should be tracked**, based on the success journey in CLAUDE.md:
   - Contact/enquiry form submissions (every form on the site — Contact page, service pages, any popup/modal form, WordPress plugin forms like Contact Form 7 / WPForms / Gravity Forms — identify which plugin is actually in use).
   - Phone number clicks (`tel:` links).
   - WhatsApp clicks (`wa.me` links or WhatsApp widget/chat button).
   - Any newsletter/lead-magnet signups if present.

3. **Container-level audit** (if GTM access available):
   - List all tags, triggers, and variables in the container.
   - For each expected conversion type (form submit, phone click, WhatsApp click), confirm a tag + trigger pair exists and is **published** (not just saved in a draft workspace).
   - Check trigger conditions match actual site markup (e.g., a trigger listening for a specific CSS class or form ID — confirm that selector still exists on the live site; forms plugins sometimes change markup on update and silently break click/submit triggers).
   - Check the GA4 Configuration tag is present, firing on All Pages, with the correct Measurement ID matching property 546098812.
   - Check for duplicate or conflicting tags (e.g., two GA4 config tags, double-firing event tags that would inflate conversion counts).

4. **Live-site verification** (do this regardless of container access, as ground truth):
   - Identify every form on the site (from the [website-crawl](website-crawl.md) inventory).
   - For each form, phone link, and WhatsApp link, verify (via test interaction and dataLayer/network inspection, or via container trigger logic if direct interaction isn't feasible) whether a tag actually fires on the intended action.
   - Note especially: multi-step forms, AJAX-submitted forms (no page reload) commonly break simple "form submit" triggers that rely on page-load-based Google Tag Manager events — these need a proper Form Submission trigger or a plugin-specific dataLayer push.

5. **GA4 event correlation.** Cross-check against [ga4-analysis](ga4-analysis.md): does GA4 actually receive `form_submit`/`generate_lead`/`phone_click`/`whatsapp_click` events with plausible volume matching what container logic implies should fire? A container that looks correctly configured but produces zero GA4 events indicates a downstream break (wrong GA4 tag config, blocked by consent mode, ad blockers only explaining part of the gap, etc.).

6. **Consent/privacy layer check.** If a cookie consent banner is present, confirm it isn't blocking tag firing entirely for users who haven't yet interacted with it (common misconfiguration that silently zeroes out tracking for a portion of traffic).

7. **Attribution sanity check.** Confirm conversion events, once firing, are attributable to the correct landing page/session so [ga4-analysis](ga4-analysis.md) can map conversions back to specific priority service pages.

## What Checks to Perform

- [ ] GTM snippet present and correct container ID, head + body
- [ ] All site forms inventoried
- [ ] Tag/trigger exists and is published for: form submit, phone click, WhatsApp click
- [ ] Trigger selectors verified against live site markup
- [ ] GA4 Configuration tag present, correct Measurement ID, firing sitewide
- [ ] No duplicate/conflicting tags inflating counts
- [ ] Live test interaction confirms actual firing (not just container logic)
- [ ] GA4 event volume cross-checked against expected firing behavior
- [ ] Consent banner (if present) doesn't block tags pre-consent inappropriately
- [ ] Conversions attributable to correct landing page

## How to Identify Issues

- No tag/trigger exists for a critical conversion type = CRITICAL measurement gap.
- Tag/trigger exists but selector no longer matches live markup (e.g., form plugin updated) = CRITICAL (silently broken — looks fine in GTM, produces nothing).
- Tag published but GA4 shows no corresponding events = HIGH, investigate GA4 config tag or consent blocking.
- Duplicate tags inflating counts = MEDIUM/HIGH depending on how much it distorts reported conversion numbers used for decisions.
- AJAX form not using proper trigger type = CRITICAL if that form is a primary enquiry channel.

## Evidence to Collect

Save to `data/gtm/`:
- `data/gtm/container-inventory-YYYY-MM-DD.md` (tags/triggers/variables list, if container access available)
- `data/gtm/live-site-tag-verification-YYYY-MM-DD.md` (results of live interaction tests: which forms/links actually fired a tag, dataLayer push captured where possible)
- Screenshots or captured network/dataLayer evidence where feasible

## How to Prioritize Issues

Broken tracking on any primary enquiry channel (main contact form, click-to-call, WhatsApp) is CRITICAL — it directly undermines the "increase form submissions / genuine enquiries / phone and WhatsApp contacts" goals in CLAUDE.md by making them unmeasurable. Secondary forms (e.g., a newsletter signup) with broken tracking is MEDIUM.

## Implementation Recommendations

- Specify exact GTM changes needed: trigger type (Form Submission vs. Click vs. Custom Event), selector to use, and whether it requires the built-in GTM Form trigger (with "Wait for Tags"/"Check Validation" settings) or a dataLayer push added via the WordPress form plugin's settings/hooks.
- If the form plugin supports native GTM/dataLayer integration (many do, e.g. via a settings toggle or a small snippet), prefer that over fragile CSS-selector-based triggers.
- Always specify: this requires GTM publish (not just save) to go live, and container versioning means a rollback is possible if something breaks.

### Form plugin differences relevant to trigger design

The three form plugins commonly seen on WordPress CA/tax sites wire up to GTM differently. Verify actual behavior on the live site rather than assuming — the notes below are typical patterns, not guarantees for this specific install:

- **Contact Form 7 (CF7):** Typically fires a `wpcf7mailsent` DOM/JS event (and related events like `wpcf7invalid`) on successful submission, which a GTM Custom Event trigger can listen for directly. CF7 submits via AJAX by default, so the standard GTM "Form Submission" trigger (which listens for a native form submit that leads to page navigation) commonly does **not** fire reliably — a Custom Event trigger keyed to the plugin's own success event is usually the correct approach.
- **WPForms:** Commonly exposes its own JS hooks/events on submission and, depending on plan/addons, may support pushing directly to `dataLayer` (natively or via a small custom-JS snippet). Confirm which mechanism is actually wired up rather than assuming a GTM-native integration exists by default.
- **Gravity Forms:** Also fires its own JS hooks (e.g., form-confirmation-related events) and can be connected to `dataLayer` via an add-on or custom JS. Multi-page Gravity Forms setups add another wrinkle — confirm the trigger fires on final confirmation, not on intermediate page navigation within the form.
- **Cross-plugin pitfall:** Regardless of plugin, a naive GTM "Form Submission" trigger relying on page-navigation-based submission commonly fails silently on any AJAX-submitted form (which is the default behavior for all three plugins above). If a trigger of this type is found in the container, treat it as a strong candidate for silent breakage and verify with a live test rather than trusting that it "looks right."
- Where the actual hook/event name can't be confirmed with certainty, phrase the finding as "typically fires a `wpcf7mailsent`-style event" or "commonly exposes a dataLayer hook via addon" rather than stating it as a fact about this specific site's current plugin version — then verify directly (container Preview mode or live network/dataLayer inspection) before finalizing the recommendation.

## How to Validate Fixes

- After publishing a GTM fix, perform a live test submission/click and confirm via GTM Preview mode (or dataLayer/network inspection) that the tag fires exactly once, correctly.
- Confirm the corresponding event appears in GA4 Realtime.
- Over the following days, confirm event volume in GA4 standard reports is plausible relative to known traffic/visible form activity (not zero, not implausibly inflated from double-firing).

## Expected Output Format

A finished GTM & Conversion Tracking Audit produces findings using CLAUDE.md's required finding template, with this skill primarily feeding the **Evidence**, **Likely Root Cause**, and **Implementation Steps** fields (root cause here is almost always a specific trigger/tag/publish-state problem, not a vague "tracking seems off").

Produce a summary table alongside the findings:

| Conversion Action | Form/Link Plugin or Type | Tag Exists? | Trigger Type | Published? | Live Test Result | GA4 Event Seen? | Status |
|---|---|---|---|---|---|---|---|
| e.g. Main Contact Form | Contact Form 7 | Yes/No | Custom Event / Form Submission / — | Yes/No | Fired / Did not fire / DATA NOT AVAILABLE | Yes/No/DATA NOT AVAILABLE | WORKING / BROKEN / PARTIAL / UNVERIFIABLE |
| Phone Click (`tel:`) | — | ... | ... | ... | ... | ... | ... |
| WhatsApp Click (`wa.me`) | — | ... | ... | ... | ... | ... | ... |

Every row's "Live Test Result" and "GA4 Event Seen?" columns must be filled from real evidence or explicitly marked `DATA NOT AVAILABLE` — never left blank or inferred.

## Common Mistakes to Avoid

- Declaring a tag "working" because it exists and is published in GTM, without ever performing a live test interaction to confirm it actually fires.
- Double-counting conversions from both a form plugin's native GA4/Google Ads integration (some plugins have their own built-in analytics push) **and** a separate GTM tag firing on the same submission event — always check for this overlap before reporting conversion volume as reliable.
- Treating a `wa.me` link click as tracked by default. WhatsApp links typically open a new tab or hand off to the WhatsApp app itself, so the click event on the page may never register with a page-based trigger unless it's specifically bound to a click listener that fires *before* navigation — verify this explicitly rather than assuming.
- Assuming the standard GTM "Form Submission" trigger works for an AJAX-submitted form (the default for CF7, WPForms, and Gravity Forms) — this is one of the most common silent-failure patterns on WordPress sites.
- Confusing "tag is published in GTM" with "tag is published in GTM **and** the container change was actually published" — a workspace can have unpublished edits sitting indefinitely.
- Not checking for duplicate GA4 Configuration tags (one from a plugin's native integration, one from GTM) that inflate pageview/session counts and distort downstream GA4 conversion-rate analysis.
- Reporting a conversion "gap" as a GTM problem without first ruling out a GA4-side issue (wrong Measurement ID, filtered view, data retention/threshold suppression) or a GSC/traffic issue — cross-check with [ga4-analysis](ga4-analysis.md) before concluding the tracking layer itself is at fault.
- Testing tag firing only on desktop when the majority of phone/WhatsApp click actions for this audience likely happen on mobile — mobile tap behavior (and mobile browser dataLayer support) can differ from desktop click behavior.
