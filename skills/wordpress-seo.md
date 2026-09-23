# Skill: WordPress-Specific SEO Audit

## Purpose

Identify SEO issues and risks that are specific to cashahnawaz.com's WordPress implementation — plugin configuration, theme behavior, and admin-level settings — and establish which plugin/system actually controls each SEO-relevant setting so other skills' implementation recommendations are accurate rather than generic.

## Scope

This skill is the **shared system-profile reference** for cashahnawaz.com: it establishes, once, which SEO plugin, theme/page-builder, caching plugin, security plugin, form plugin, and redirect-management system are actually active — and documents exactly where each SEO-relevant setting lives inside that specific plugin's admin UI. Every other skill's "Implementation Steps" should cite this skill's output (`data/crawl/wordpress-system-profile.md`) rather than re-discovering plugin identity or guessing at menu paths.

**In scope:**
- Identifying the active SEO plugin, theme, page builder, caching/security/form/redirect plugins
- Documenting exact (or "typically found under...", confirmed live) admin menu paths for SEO-relevant settings, per plugin
- Permalink structure
- Sitewide default noindex toggles (media attachments, archives) at the plugin-config level
- Plugin-conflict detection (two SEO plugins/schema sources active)
- Staging/backup/rollback safety posture before any change

**Out of scope — hand off instead:**
- Diagnosing whether a specific URL is actually noindexed/miscanonicalized in practice → [technical-seo](technical-seo.md) (this skill supplies *which plugin controls that toggle*; technical-seo confirms *the resulting state on specific URLs*)
- Crawling and building the URL inventory itself → [website-crawl](website-crawl.md)
- Schema markup correctness/type selection → [schema-audit](schema-audit.md) (this skill only flags when theme and plugin schema sources conflict)
- On-page copy, title/meta wording quality → [on-page-seo](on-page-seo.md)
- Core Web Vitals diagnosis (this skill only identifies the caching/optimization plugin in use) → [performance-audit](performance-audit.md)
- Conversion tracking setup detail (this skill only identifies which form plugin is in use) → [gtm-conversion-audit](gtm-conversion-audit.md)
- Local SEO plugin/schema specifics (e.g., local business plugins) → [local-seo](local-seo.md)

If a finding is "setting X is misconfigured, causing effect Y on the live site," document the plugin/setting location here and let the consuming skill (usually technical-seo or schema-audit) own the live-effect diagnosis and the formal finding.

## When to use it

- Early in the audit, as a foundational pass — its findings (which SEO plugin is active, how permalinks are structured, which caching/security plugins exist) inform how every other skill writes its "Implementation Steps."
- Whenever another skill needs to know "which plugin controls X" before recommending a fix.
- After any WordPress core, theme, or plugin update, since these can silently change SEO-relevant behavior.

## Required Data

- WordPress Admin access (confirmed available per CLAUDE.md) — actual login/inspection, not assumption.
- Hosting access (confirmed available per CLAUDE.md) — for server-level checks (caching, .htaccess, PHP version) if needed.
- Live site HTML (for detecting plugin fingerprints even without admin access, as a cross-check).

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- **If WordPress Admin access is confirmed reachable this session:** direct inspection of the Plugins list (name + version), Settings → Permalinks, the active SEO plugin's settings screens, theme identification (Appearance → Themes), and any plugin-config toggle — this is ground truth and should be preferred whenever actually available.
- **If admin access is not being used this session (or fails):** live-site fingerprinting via WebFetch — meta generator tags, sitemap URL pattern (e.g. `/sitemap_index.xml`), schema.org JSON-LD signatures, HTML comments some plugins leave, asset/script handle names in page source. This is inference from external signals, not a confirmed admin-side fact, and must be labeled as such (e.g., "Inferred from live-site fingerprint: likely Yoast SEO, not confirmed via Admin").
- Live page HTML for confirming rendered title/meta/schema output, regardless of which mode is used.

### DATA NOT AVAILABLE / REQUIRES VERIFICATION
- **Any admin-only setting when admin access is not actually being used this session** — plugin config toggles, sitewide noindex defaults, exact version numbers, staging environment existence — these must be marked `DATA NOT AVAILABLE` or explicitly labeled as fingerprint-inferred rather than confirmed, even though CLAUDE.md lists WordPress Admin as "Available." Availability per CLAUDE.md is not the same as verified reachable this session — attempt the actual login/navigation before treating any admin-screen fact as confirmed.
- Exact current menu labels/paths for plugin settings if not confirmed live this session — plugin UIs change between versions; a path that was correct in a prior session or in general plugin knowledge should be phrased as "typically found under..." and verified live, not stated as current fact.
- Hosting-level configuration (PHP version, server-level caching, .htaccess contents) unless hosting access is actually used this session, not merely assumed available.
- Plugin version numbers precisely enough to know whether a specific known bug/behavior applies, unless read directly from the admin Plugins screen or a version string exposed in page source.

## Pre-Audit Checks

1. **Determine and state which access mode is active for this session's findings before doing anything else: Admin-confirmed or fingerprint-only.** Attempt an actual WordPress Admin action (e.g., load the Plugins list) rather than assuming access works because CLAUDE.md lists it as available. If admin access fails or isn't attempted, every fact this session produces must be labeled as fingerprint-inferred, not confirmed.
2. **If admin access works, confirm the login level (Administrator vs. Editor/other)** — this determines which settings screens are even visible/changeable and should be stated once at the top of this pass's output so downstream implementation steps don't assume Administrator-level changes are executable.
3. **If falling back to fingerprint-only mode, fetch at least two different page types (homepage + one interior page)** before concluding on plugin identity — a single page's signals can be ambiguous or leftover from a prior plugin.

## Step-by-Step Audit Process

1. **Identify the active SEO plugin.** Check WordPress Admin → Plugins for Yoast SEO, Rank Math, All in One SEO, or others. Confirm via live-site fingerprints too (meta generator tags, specific schema patterns, sitemap URL pattern — e.g., `/sitemap_index.xml` for Yoast/RankMath vs. other patterns). Document exactly which plugin and version is active — this determines the "where to click" instructions in every other skill's Implementation Steps. Once identified, use the "Plugin-Specific Settings Reference" section below for the exact settings locations — never mix instructions from more than one plugin's column.

2. **Permalink structure.** Check Settings → Permalinks. Confirm a clean, SEO-friendly structure (e.g., Post name) is in use, not the default `?p=123` query-string structure.

3. **Theme identification and audit.**
   - Identify the active theme (and whether it's a page-builder-based theme — Elementor, Divi, WPBakery, etc. are common for CA/service sites and each has its own SEO quirks: bloated markup, render-blocking assets, heading misuse for styling rather than semantics).
   - Check for theme-level SEO interference: default titles not overridden, theme-generated schema conflicting with the SEO plugin's schema (cross-ref [schema-audit](schema-audit.md)).

4. **Plugin inventory relevant to SEO/performance/security**:
   - Caching plugin (if any) — relevant to [performance-audit](performance-audit.md) and to confirming that changes will actually go live (cache purge needed after edits).
   - Image optimization plugin (if any).
   - Security plugin (firewall/login protection) — check it isn't blocking legitimate crawler access (misconfigured security plugins occasionally block Googlebot).
   - Form plugin (Contact Form 7 / WPForms / Gravity Forms / other) — critical for [gtm-conversion-audit](gtm-conversion-audit.md), since trigger setup depends on which plugin and its markup/dataLayer support.
   - Backup plugin (relevant only insofar as it confirms a safe-rollback path exists before implementing changes).

5. **Redirect management.** Check whether redirects (from [technical-seo](technical-seo.md) findings) are managed via a dedicated plugin (Redirection, RankMath/Yoast redirect manager) or hand-edited `.htaccess`/server config — this determines implementation steps for any redirect fix.

6. **XML sitemap generation.** Confirm which system generates the live sitemap (should match the identified SEO plugin) and that its settings (included post types, excluded categories) are correctly configured — e.g., confirm all priority service pages' post type is included in the sitemap generation settings.

7. **Robots meta controls.** Check plugin-level default noindex settings (e.g., Yoast/RankMath have sitewide toggles for "noindex media attachments," "noindex category archives," etc.) — confirm none of these defaults are accidentally affecting priority content, and that media attachment pages (a common WordPress default-indexing issue) are handled correctly.

8. **User roles and change-safety.** Confirm what access level is actually available (Administrator vs. Editor) since this affects what implementation steps are actually executable, and note that plugin/theme updates should be tested on staging if a staging environment exists — check whether one does.

9. **Page builder / block editor content check.** If using Elementor/Divi/Gutenberg, check whether SEO-relevant content (headings, text) is actually present in a crawlable form or generated in a way that could hide it from crawlers (rare with modern builders, but verify at least one priority page renders correctly in a plain fetch, not just in-browser).

10. **WooCommerce or booking plugin check** (if the site has any transactional functionality beyond forms — e.g., a payment/booking system for consultations) — note if present, since it changes conversion tracking and schema considerations.

## Plugin-Specific Settings Reference

**Use this only after Step 1 has confirmed which single plugin is actually active.** Never apply instructions from more than one column below to the same site — if fingerprinting or admin inspection is ambiguous, that ambiguity is itself a finding (possible plugin conflict — see "How to Identify Issues" below) and must be resolved before writing fix instructions. Menu labels below reflect long-stable UI patterns for each plugin; plugin UIs are updated periodically, so treat every path as "typically found under..." and confirm the exact current label/location live in the admin before publishing it as fact in a report.

| Setting | Yoast SEO | Rank Math | All in One SEO (AIOSEO) |
|---|---|---|---|
| **Title & meta templates per post type** | SEO → Search Appearance → Content Types tab, one sub-tab per post type (Posts, Pages, custom types) | Rank Math → Titles & Meta → Posts / Pages / other post-type tabs | All in One SEO → Search Appearance → Content Types tab |
| **Category/tag archive noindex toggle** | SEO → Search Appearance → Taxonomies tab (per taxonomy: Categories, Tags) — "Show X in search results" toggle | Rank Math → Titles & Meta → Taxonomies tab, per-taxonomy noindex toggle | All in One SEO → Search Appearance → Taxonomies tab |
| **Media/attachment-page handling** | SEO → Search Appearance → Content Types → Media — "Redirect attachment URLs to the attachment itself" toggle | Rank Math → Titles & Meta → Media, "Attachment Redirect" setting | All in One SEO → Search Appearance → Content Types → Media, attachment redirect setting |
| **XML sitemap inclusion/exclusion by post type/taxonomy** | SEO → General → Site Features (sitemap toggle) + SEO → Search Appearance → Content Types/Taxonomies (per-type "Show in search results" also drives sitemap inclusion) | Rank Math → Sitemap Settings module, per post-type and per-taxonomy toggles | All in One SEO → Sitemaps → General Sitemap, post type/taxonomy inclusion checkboxes |
| **Canonical URL override field** | Per-post/page: SEO plugin metabox → Advanced tab → Canonical URL field, in the block/classic editor sidebar | Per-post/page: Rank Math metabox → Advanced tab → Canonical URL field | Per-post/page: AIOSEO metabox → Advanced → Canonical URL field |
| **Redirect manager** | Not included in free Yoast SEO; Yoast Premium adds a Redirects module (SEO → Redirects). Free Yoast typically needs a separate plugin (commonly "Redirection") | Built in: Rank Math → Redirections module (must be enabled under Rank Math → Dashboard → Modules if not already active) | Built in: All in One SEO → Redirects module |
| **Schema/structured-data settings** | SEO → Search Appearance → Content Types (per-type schema type default) + per-post metabox Schema tab | Rank Math → Titles & Meta (per-type default schema) + per-post metabox Schema tab (Schema Generator) | All in One SEO → Search Appearance (per-type default) + per-post metabox Schema Generator |

**Before prescribing any step from this table:** confirm the plugin's version-appropriate wording live (the menu labels above are well-known, stable patterns but are not guaranteed current), and confirm the module/feature referenced is actually enabled (e.g., Rank Math ships as a modular plugin — its Redirections and Schema modules must be individually enabled under Rank Math → Dashboard → Modules or they won't appear in the menu at all).

## What Checks to Perform

- [ ] Active SEO plugin identified and documented (name + version)
- [ ] Permalink structure confirmed SEO-friendly
- [ ] Active theme identified; page-builder-related quirks checked
- [ ] Form plugin identified (critical dependency for gtm-conversion-audit)
- [ ] Caching plugin identified (affects change-validation process)
- [ ] Security plugin checked for crawler-blocking misconfiguration
- [ ] Redirect management system identified
- [ ] Sitemap generation settings confirmed to include all priority content
- [ ] Sitewide noindex defaults checked against priority content
- [ ] Staging environment availability checked

## How to Identify Issues

Most findings here are configuration facts feeding other skills rather than "issues" in isolation — but flag directly as issues: crawler-blocking security rules, sitewide noindex defaults wrongly affecting priority content, non-SEO-friendly permalinks, and any plugin conflict (e.g., two SEO plugins active simultaneously, which causes duplicate meta tags/schema and is a known WordPress anti-pattern).

## Evidence to Collect

- Plugin name/version list (from Admin → Plugins, or live-site fingerprinting if admin access isn't used for this pass).
- Screenshots or direct quotes of relevant settings screens (permalink structure, SEO plugin global settings).
- Save a system profile to `data/crawl/wordpress-system-profile.md`: SEO plugin, theme, form plugin, caching plugin, security plugin, redirect system, staging availability — this becomes a shared reference other skills' implementation steps point to.

## How to Prioritize Issues

- **CRITICAL:** Security plugin blocking Googlebot; sitewide noindex default wrongly applied to priority content; two conflicting SEO plugins both active.
- **HIGH:** Non-SEO-friendly permalink structure; sitemap excluding priority post types.
- **MEDIUM:** Suboptimal but functional plugin configuration; missing staging environment (process risk, not a live SEO issue).
- **LOW:** Outdated plugin/theme versions with no observed functional SEO impact (still worth flagging for general maintenance).

## Implementation Recommendations

- Every recommendation from this skill should be phrased as "in [Plugin Name] → [exact menu path], change [setting] to [value]" — specificity is the entire value of this skill.
- Recommend testing any structural change (permalink, redirect system) on staging first if available; if no staging exists, recommend taking a backup immediately before the change and note this explicitly as a prerequisite step.
- If two SEO plugins are found active, recommend deactivating one — but flag this as needing careful sequencing (export settings/redirects first) since deactivation can drop existing meta/redirect data; this is a higher-risk change requiring explicit user approval per CLAUDE.md rule 5/7.

## How to Validate Fixes

- After any plugin/settings change, clear cache (if a caching plugin is active) and re-fetch the live page to confirm the change actually rendered, not just saved in admin.
- Re-run the relevant dependent skill's crawl/check (e.g., re-check sitemap after a sitemap setting change) to confirm the fix propagated correctly.
- Confirm no regression: spot-check a few unrelated pages still render/function correctly after the change.

## Expected Output Format

This skill's primary deliverable is the system profile file `data/crawl/wordpress-system-profile.md`, plus any direct findings using the CLAUDE.md template. The system profile should contain, at minimum:

```
# WordPress System Profile — cashahnawaz.com
Session date: [date]
Access mode: Admin-confirmed | Fingerprint-only (state which)

| Component | Value | Confidence/Source |
|---|---|---|
| SEO plugin (name + version) | | |
| Theme (name + version, page builder if any) | | |
| Permalink structure | | |
| Caching plugin | | |
| Security plugin | | |
| Form plugin | | |
| Redirect management system | | |
| Staging environment available? | | |
| Login level used this session | | |
```

Direct findings (e.g., plugin conflict, crawler blocked by security plugin, sitewide noindex default misapplied) use the full CLAUDE.md Required Finding Template, with **Implementation Steps** phrased as "In [confirmed Plugin Name] → [menu path from the Plugin-Specific Settings Reference, confirmed live], change [setting] to [value]."

## Common Mistakes to Avoid

- **Recommending a fix location for a setting that moved in a recent plugin version without confirming current placement live.** The paths in the Plugin-Specific Settings Reference above are stable historical patterns, not a guarantee of the current UI — always confirm live before publishing a path in a finding.
- **Recommending deactivating a "duplicate" SEO plugin without first exporting its settings/redirects.** Deactivation can silently drop custom meta, redirects, and schema configuration entered through that plugin — always recommend export/backup as an explicit prerequisite step, and flag this as a higher-risk change needing explicit approval per CLAUDE.md rule 5/7.
- **Treating live-site fingerprinting as equivalent to confirmed admin access.** State the access mode explicitly every session; don't let a fingerprint-based "likely Yoast" silently become "confirmed Yoast" in a later finding.
- **Applying instructions from the wrong plugin column** because two plugins showed conflicting fingerprints and the ambiguity wasn't resolved before writing implementation steps.
- **Assuming a module is enabled just because the plugin is installed** — notably Rank Math, which is modular: Redirections and Schema Generator must be individually switched on under Modules or the referenced menu simply won't exist.
- **Confusing "plugin setting saved" with "change is live."** A caching plugin can serve a stale response after a settings change — always note cache-clear as part of validation, not just as a courtesy.
- **Reporting theme/plugin version numbers from memory or general knowledge of "current" versions** instead of what's actually installed on this site — versions must come from actual inspection (admin Plugins screen or a version string in page source), not assumption.
- **Skipping the staging/backup check because "it's just a settings toggle."** Even simple toggles (attachment redirect, permalink structure) can have site-wide URL-structure consequences; always confirm the rollback path before recommending a live change.
