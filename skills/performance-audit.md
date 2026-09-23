# Skill: Performance Audit (Core Web Vitals & Page Speed)

## Purpose

Measure actual page speed and Core Web Vitals for cashahnawaz.com, since slow load times directly hurt both rankings (Core Web Vitals is a confirmed ranking factor) and conversions (users abandon slow-loading forms/contact pages before ever reaching the "Form Submission / Contact" stage of the success journey).

## When to use it

- As part of the initial technical audit.
- When [gsc-analysis](gsc-analysis.md) Core Web Vitals report shows Needs Improvement/Poor URL groups.
- When [ga4-analysis](ga4-analysis.md) shows high bounce/low engagement on specific pages that might be speed-related.
- After any theme, plugin, or hosting change.

## Scope

This skill owns Core Web Vitals and page-speed measurement (LCP, INP, CLS, TTFB, and supporting lab diagnostics) plus root-cause diagnosis of poor scores down to the specific plugin/theme/hosting element responsible. It writes the recommendation and implementation steps for each root cause, but does NOT own:

- Actually carrying out image-optimization/caching-plugin configuration changes or theme code edits — that is implementation work under CLAUDE.md rule 7 (diagnosis and recommendation happen here; approved execution happens after sign-off). [wordpress-seo](wordpress-seo.md) is the reference for the full plugin/theme inventory — check it before recommending a new plugin so you don't recommend installing a caching plugin that's already active but misconfigured.
- Conversion-rate/UX friction analysis of a slow page beyond the direct speed-to-abandonment link — form field count, CTA clarity, trust signals are [cro-audit](cro-audit.md).
- Interpreting GA4 engagement/bounce data — this skill may use a GA4 signal as a trigger to investigate a page's speed, but [ga4-analysis](ga4-analysis.md) owns GA4 report interpretation itself.
- GSC coverage/indexing/query data beyond the Core Web Vitals field-data report specifically — [gsc-analysis](gsc-analysis.md) owns the rest of GSC.
- General technical SEO — robots, sitemaps, canonicals, redirects: [technical-seo](technical-seo.md); structured data: [schema-audit](schema-audit.md).
- Content quality/on-page keyword optimization — [on-page-seo](on-page-seo.md), [content-audit](content-audit.md).
- Internal linking structure — [internal-linking](internal-linking.md).
- Full WordPress plugin/theme/security inventory — [wordpress-seo](wordpress-seo.md) (this skill inspects only the subset of plugins/theme behavior that measurably affects speed).
- Systematic competitor site benchmarking — a speed spot-check for context is fine, but [competitor-analysis](competitor-analysis.md) owns structured competitor comparison.
- Local SEO / Google Business Profile — [local-seo](local-seo.md).
- Site crawl/URL inventory — this skill consumes the inventory from [website-crawl](website-crawl.md) rather than producing it.

## Data Sources & Limitations

### AVAILABLE WITH LIVE CONNECTOR / TOOL (PageSpeed/Lighthouse-style tool confirmed working this session)
- Lab-based LCP, INP (or a proxy like TBT/FID depending on the tool), CLS, TTFB, and Speed Index for a specific URL/device combination at the moment of the test.
- The opportunity/diagnostic breakdown (render-blocking resources, unoptimized images, unused CSS/JS, font-loading issues) tied to that specific lab run.
- A true before/after comparison of the same URL/device/tool once a fix is implemented, run under comparable (cache-cleared) conditions.

### AVAILABLE WITH GSC (Core Web Vitals field/CrUX report confirmed working this session)
- Real-user (field) LCP, INP, CLS aggregated by URL group over a rolling ~28-day window, reflecting actual visitor devices/networks rather than one lab environment.
- Good / Needs Improvement / Poor URL-group counts and trend direction over time.

### DATA NOT AVAILABLE (no connector/tool)
Must be marked `DATA NOT AVAILABLE` rather than estimated:
- Any specific LCP/INP/CLS/TTFB number for any page, if neither a lab tool nor GSC CrUX access is confirmed working this session.
- Claims like "this is probably slow because it's WordPress" or "Elementor sites are usually bloated" — never acceptable substitutes for a real measurement, even where often directionally true in general industry experience.
- Any performance claim inferred purely from visual inspection ("the hero image looks large so LCP is probably bad") without an actual measured value backing it — visual inspection may point to a hypothesis worth testing, but the finding itself needs a real number.
- Competitor site speed, unless actually tested with the same tool — never assume a competitor is faster or slower "because their site looks more modern."

### Lab vs. field data — label this distinction explicitly wherever it applies
Lab data (a single tool run, one simulated device/network condition) and field data (GSC CrUX, real visitors over time) frequently disagree, and each carries different evidentiary weight:
- Tag every metric cited as `LAB` or `FIELD` — never present one as if it were the other.
- Field data is what Google actually uses for the Core Web Vitals ranking signal; when the two disagree, treat field data as the stronger claim and say so explicitly (e.g., "Lab LCP 2.1s [Good], but GSC field data shows this URL group as Poor — real visitors on slower networks/devices are experiencing worse conditions than the lab run captured").
- A single lab run can vary noticeably between runs due to network/CPU throttling variance in the testing infrastructure itself — never treat one run as definitive; note in the evidence whether multiple runs were averaged or a single run is being reported as indicative only.
- If only lab data is available (no GSC CrUX access, or a URL/device combination falls below CrUX's minimum-traffic threshold to report), say so explicitly rather than implying field-level confidence.

## Pre-Audit Checks

Before starting the workflow below, confirm:

1. **Run one real test first and inspect the raw output** before trusting further runs — confirm the tool returns genuine metric values (not a timeout, error page, or a stubbed/zeroed response) against the live homepage.
2. **Decide mobile vs. desktop testing priority.** This audience (local-intent tax/CA searches) is predominantly mobile; treat mobile as the primary test condition and desktop as secondary/supporting, and say so explicitly when presenting results rather than weighting the two equally.
3. **Check whether a caching plugin is active and needs cache-clearing before each fresh test.** A stale cached page (pre-fix HTML/assets still being served) produces a misleading "before"/"after" comparison that doesn't actually reflect the change under test — clear/purge cache immediately before every test run meant to represent current state.
4. **Watch for testing-infrastructure noise.** If back-to-back runs of the same URL produce wildly different scores, note the variance rather than cherry-picking whichever run supports the desired conclusion.
5. **Source test URLs from the [website-crawl](website-crawl.md) inventory**, and, where available, prioritize by traffic from [gsc-analysis](gsc-analysis.md)/[ga4-analysis](ga4-analysis.md) rather than guessing which pages matter most.

## Step-by-Step Audit Process

1. **Verify testing capability.** Run one real test against the homepage. Confirm it returns real metrics (not a stub/error) before treating results as evidence.

2. **Test priority pages.** Run tests (mobile and desktop separately — mobile is typically the primary ranking/traffic surface) for: homepage, and a representative sample of priority service pages (at minimum, the highest-traffic ones per [ga4-analysis](ga4-analysis.md)/[gsc-analysis](gsc-analysis.md) if available, else a cross-section covering each service group).

3. **Capture Core Web Vitals** per tested page/device:
   - LCP (Largest Contentful Paint) — target <2.5s
   - INP (Interaction to Next Paint) — target <200ms (replaced FID as the responsiveness metric)
   - CLS (Cumulative Layout Shift) — target <0.1
   - Also capture: TTFB, Speed Index, Total Blocking Time as supporting diagnostics.

4. **Identify root causes** from the lab test's diagnostics/opportunities section, e.g.:
   - Unoptimized/unresized images (very common on WordPress CA sites using large stock/hero images).
   - Render-blocking CSS/JS (common with page builders like Elementor/Divi — cross-ref [wordpress-seo](wordpress-seo.md) theme findings).
   - No/poor caching or CDN.
   - Excessive third-party scripts (chat widgets, tracking pixels, font loaders) — note GTM itself and any WhatsApp widget as candidates to check aren't misconfigured to load synchronously/blocking.
   - Large unused CSS/JS bundles from an unoptimized theme or too many active plugins.
   - Web font loading strategy causing layout shift or delayed text render.
   - Server response time (TTFB) issues pointing to hosting/PHP performance rather than front-end.

5. **Field data cross-check (GSC/CrUX)**, if accessible: compare real-user field data against lab results — field data reflects actual visitor devices/networks (often slower than a lab test environment) and is what Google actually uses for the ranking signal. Note discrepancies (e.g., good lab score but poor field score suggests real-world conditions, like slow mobile networks among the target audience, aren't reflected in the lab test).

6. **Mobile-specific check.** Given financial/tax searches often happen on mobile, specifically verify mobile LCP/INP/CLS meet targets, and check for mobile-specific issues: tap target sizing (relevant for phone/WhatsApp click buttons — also a CRO concern), viewport configuration, unoptimized mobile images.

7. **Form-page-specific check.** Specifically test any page with the primary contact/enquiry form for interactivity responsiveness (INP) — a laggy form directly undermines the "increase form submissions" goal.

8. **Third-party script audit.** List all third-party scripts loading (analytics, GTM, chat widgets, fonts, ad scripts if any) and their measured impact on load time — flag any clearly unnecessary or redundant script (e.g., duplicate analytics loading from both a plugin and a manual snippet).

## What Checks to Perform

- [ ] Testing capability verified with a real run before relying on results
- [ ] Homepage + representative priority pages tested, mobile and desktop
- [ ] LCP, INP, CLS captured per test
- [ ] Root-cause diagnostics captured per test (not just scores)
- [ ] GSC field data (CrUX) cross-checked against lab data, if accessible
- [ ] Mobile specifically checked (tap targets, mobile LCP/INP/CLS)
- [ ] Primary contact form page specifically tested for interactivity
- [ ] Third-party scripts inventoried with impact noted

## How to Identify Issues

Any Core Web Vital metric outside the "Good" threshold on a priority page is a finding. Prioritize by (a) how far outside threshold, (b) whether it's field data (real users affected now) vs. lab-only, and (c) whether the affected page is high-commercial-value (a slow GST Registration page matters more than a slow old blog post).

## Evidence to Collect

Save to `data/performance/`:
- `data/performance/lighthouse-[page-slug]-[mobile|desktop]-YYYY-MM-DD.json` (or summary table if raw JSON isn't practical to store)
- `data/performance/cwv-field-data-YYYY-MM-DD.csv` (from GSC, if accessible)
- A summary table: Page → Device → LCP → INP → CLS → Top Opportunity

## How to Prioritize Issues

- **CRITICAL/HIGH:** Poor (not just Needs Improvement) Core Web Vitals on high-traffic priority pages or the primary contact form page, confirmed by field data.
- **MEDIUM:** Needs Improvement scores on priority pages; Poor scores on low-traffic pages.
- **OPPORTUNITY:** Lab-only findings not yet confirmed by field data at scale; general optimization headroom on already-passing pages.

## Implementation Recommendations

- Tie each recommendation to the specific diagnosed cause (e.g., "compress and resize hero image on GST Registration page, currently Xkb, no responsive sizes" rather than a generic "improve image optimization").
- Note whether the fix is content-level (something an editor can do — resize an image, remove an unnecessary embed), plugin-level (install/configure a caching or image-optimization plugin — cross-ref [wordpress-seo](wordpress-seo.md) for what's already active), or hosting-level (requires the hosting access noted in CLAUDE.md, e.g., enabling server-level caching, upgrading PHP version).
- Flag any recommendation that would require a plugin/theme change as needing a backup/staging test first, consistent with CLAUDE.md rule 5.

### Owner/access level for each fix type

Route every recommendation to the correct owner so the "Implementation Steps" field in the finding template is actually actionable, using the access levels CLAUDE.md confirms are available (WordPress Admin, Hosting Access):

- **Plugin-configuration fixable (WordPress Admin access):** Enabling/tuning a caching plugin (page cache, browser cache headers, minification), configuring an image-optimization plugin (lazy-loading, WebP/AVIF conversion, responsive `srcset` generation), or a CDN plugin toggle. Also covers turning off/deferring a genuinely unnecessary third-party script loaded via a plugin. Before recommending a new plugin install, check [wordpress-seo](wordpress-seo.md)'s plugin inventory — a misconfigured existing caching plugin is a more common root cause than "no caching plugin at all."
- **Theme/page-builder fixable (WordPress Admin access, but higher risk — needs staging/backup first):** Bloat from Elementor/Divi widget stacks, excessive custom CSS/JS injected per-page by the builder, render-blocking web-font loading strategy baked into the theme, layout patterns causing CLS (ads/embeds/widgets injected above the fold without reserved space). These are structural to the theme/template rather than a simple settings toggle, and carry more regression risk — flag for a staging test per CLAUDE.md rule 5 rather than a direct live edit.
- **Hosting-level fixable (Hosting Access):** Slow TTFB/server response time, outdated PHP version, absent or misconfigured server-level caching (as distinct from a WordPress caching plugin), missing HTTP/2 or compression at the server/CDN layer, and shared-hosting resource contention. These require hosting-panel/server access rather than WordPress Admin — say so explicitly rather than routing a TTFB fix to "install a plugin," which won't fix a genuinely slow server.
- If a root cause spans more than one owner (e.g., a hosting-level TTFB issue compounding a theme-level render-blocking issue), say so and list both, rather than collapsing them into a single vague recommendation.

## How to Validate Fixes

- Re-run the same lab test (same tool, same page, same device setting) after implementation and compare directly against the pre-fix baseline saved in `data/performance/`.
- Confirm the change didn't regress a different metric (e.g., an image lazy-load fix improving LCP but introducing CLS).
- Track GSC Core Web Vitals field data over the following weeks (field data takes time — typically a 28-day rolling window — to reflect a fix; don't judge success from lab data alone).

## Expected Output Format

A finished Performance Audit produces findings using CLAUDE.md's required finding template, with this skill primarily feeding the **Evidence** (lab/field metrics, explicitly labeled), **Likely Root Cause** (the specific diagnostic, not a generic "page is slow"), and **Implementation Steps** (routed to the correct owner) fields.

Produce a summary table alongside the findings:

| Page | Device | LCP | INP | CLS | Field or Lab | Top Opportunity | Owner (Plugin/Theme/Hosting) |
|---|---|---|---|---|---|---|---|
| e.g. GST Registration | Mobile | 3.8s | — | 0.05 | LAB | Unoptimized hero image, no responsive sizes | Plugin (image optimization) |
| e.g. Homepage | Mobile | Poor (URL group) | Needs Improvement | Good | FIELD (GSC CrUX) | High TTFB dragging LCP | Hosting |
| ... | Desktop | ... | ... | ... | ... | ... | ... |

Every metric cell must be a real measured/reported value or `DATA NOT AVAILABLE` — never left blank or inferred from visual inspection. Where lab and field data disagree for the same page, include both rows and note the discrepancy explicitly in the finding's Evidence field.

## Common Mistakes to Avoid

- Judging Core Web Vitals success or failure from a single lab run without accounting for run-to-run variance — always note whether a result is a single run or an average, and re-test before declaring a metric fixed.
- Recommending a caching or image-optimization plugin install without first checking (via [wordpress-seo](wordpress-seo.md)'s inventory) whether one is already active but misconfigured — installing a second overlapping plugin can create conflicts rather than fix anything.
- Not clearing cache before a "before/after" comparison — a stale cached page served during the "after" test invalidates the comparison entirely and can make a real fix look like it did nothing (or vice versa).
- Presenting a lab score as if it were field data (or the reverse) without labeling which is which — the two can disagree, and CLAUDE.md's evidence discipline requires the distinction to be explicit.
- Treating "Needs Improvement" and "Poor" as interchangeable severity — CLAUDE.md's severity guidance and this skill's prioritization both depend on how far outside threshold a metric falls, plus whether it's field-confirmed and on a high-commercial-value page.
- Testing only desktop, or only the homepage, and generalizing to "the site is fast/slow" — this audience is mobile-heavy and commercial intent lives on service pages (GST Registration, ROC Compliance, etc.), not just the homepage.
- Attributing a slow TTFB to "the theme" or "too many plugins" without isolating server response time specifically — TTFB is a hosting-level signal and needs a hosting-level fix, not a front-end optimization plugin.
- Recommending a theme/page-builder change (e.g., stripping Elementor widgets) as a quick fix without flagging it for staging/backup first per CLAUDE.md rule 5 — these changes carry real regression risk on a live business site.
