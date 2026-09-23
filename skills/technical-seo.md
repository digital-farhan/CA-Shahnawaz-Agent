# Skill: Technical SEO Audit

## Purpose

Find and document technical issues that block Google from crawling, rendering, indexing, or correctly understanding pages on cashahnawaz.com. Technical SEO is the foundation — if this is broken, content and on-page work can't pay off.

## Scope

This skill diagnoses **indexability, crawlability, redirects, canonicalization, HTTPS/domain enforcement, and sitemap/robots.txt integrity** for cashahnawaz.com. It answers "can Google reach, crawl, and correctly index this URL, and is it pointing at the right canonical target?"

**In scope:**
- robots.txt and XML sitemap correctness
- HTTP status codes, redirect chains/loops
- Indexability signals: meta robots, X-Robots-Tag, canonical tags
- WWW/non-WWW and HTTP/HTTPS domain enforcement, trailing-slash consistency
- Crawl depth/orphan pages, crawl traps (parameters, faceted URLs, WordPress archives)
- SSL/mixed content
- Whether structured data exists at all sitewide (presence only)
- Whether Core Web Vitals data exists at all in GSC (presence/status only)

**Out of scope — hand off instead:**
- Structured data *correctness/depth* (schema types, required properties, rich-result eligibility) → [schema-audit](schema-audit.md)
- On-page content quality, title/meta *copywriting*, heading structure for relevance → [on-page-seo](on-page-seo.md)
- Content thinness/coverage gaps → [content-audit](content-audit.md)
- Internal link graph analysis, anchor text strategy → [internal-linking](internal-linking.md)
- Core Web Vitals *diagnosis and fix* (LCP/INP/CLS root causes) → [performance-audit](performance-audit.md); this skill only checks whether the report exists and its status buckets
- Which plugin/theme/caching system controls a given setting → [wordpress-seo](wordpress-seo.md) is the system-of-record; this skill cites its findings rather than re-discovering plugin identity
- GSC Coverage/Indexing report deep analysis (query-level, historical trend) → [gsc-analysis](gsc-analysis.md); this skill only cross-references Coverage status for specific flagged URLs
- Local SEO signals (NAP consistency, GBP, local schema) → [local-seo](local-seo.md)
- Conversion/CRO elements → [cro-audit](cro-audit.md), [gtm-conversion-audit](gtm-conversion-audit.md)
- Competitor technical comparison → [competitor-analysis](competitor-analysis.md)

When a finding straddles two skills (e.g., a noindexed page that is also thin content), record it here as the technical fact (noindex present) and note in "Likely Root Cause" that content-audit should assess whether thinness is the underlying driver.

## When to use it

- At the start of any full-site audit, before content/on-page work (technical issues can invalidate other findings).
- When organic traffic or impressions drop suddenly (check indexing/crawl issues first).
- After any WordPress core, theme, or plugin update.
- After a migration, redesign, or URL structure change.
- Periodically (quarterly) as a health check even with no reported problem.

## Required Data

- Live crawl of the site (via [website-crawl](website-crawl.md) skill) — status codes, redirect chains, robots directives, canonical tags, hreflang if applicable.
- `robots.txt` (fetch live).
- XML sitemap(s) (fetch live, usually `/sitemap_index.xml` on Yoast/RankMath).
- Google Search Console: Coverage/Indexing report, Sitemaps report, URL Inspection tool results, Core Web Vitals report — **only if GSC access is verified working this session**.
- Server response headers for key URLs (status, cache-control, HSTS).
- SSL certificate status.
- Mobile-friendliness / mobile rendering check.

If GSC is not accessible, technical SEO audit can still proceed using crawl data alone — clearly mark GSC-dependent findings as `DATA NOT AVAILABLE` rather than skipping them silently.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- WebFetch against live URLs — retrieves rendered/summarized HTML content, from which title tags, meta descriptions, H1s, visible canonical `<link>` tags, and visible `<meta name="robots">` content can usually be extracted via a targeted prompt (e.g., "return the exact title tag, meta robots tag, and canonical link tag from this page's HTML").
- robots.txt and XML sitemap content — plain text/XML, fetchable directly and reliably.
- HTTP status codes and redirect destinations — WebFetch generally surfaces the final resolved URL; whether it exposes the full intermediate hop chain depends on the fetch tool's behavior and should be spot-checked, not assumed.
- GSC Coverage/Sitemaps/URL Inspection/Core Web Vitals reports — **only if GSC connectivity is verified working this session** (per CLAUDE.md, GSC access is never assumed).

### DATA NOT AVAILABLE / REQUIRES VERIFICATION
- Raw HTTP response headers (`X-Robots-Tag`, `Cache-Control`, `HSTS`, exact `Content-Type`) — WebFetch returns processed/summarized content, not guaranteed raw byte-level headers. Any finding that depends specifically on a response header (not the HTML `<meta>` equivalent) must be marked `DATA NOT AVAILABLE` unless a tool capable of raw header inspection is confirmed working this session, or flagged as needing manual/hosting-side confirmation.
- JS-rendered content or client-side redirects — WebFetch does not guarantee full JavaScript execution; a page that relies on JS to inject its canonical tag, noindex meta, or redirect could read as clean when it isn't (or vice versa). Flag this explicitly wherever a page's markup looks JS-dependent.
- Google's actual rendering/indexing decision — only GSC URL Inspection ("Test Live URL" / indexed cache) can confirm how Google itself sees a page. Crawl-side evidence shows what *we* fetched, not what Googlebot fetched or how Google indexed it; do not conflate the two in a finding's Evidence field.
- SSL certificate chain detail, mixed-content resource-level enumeration, and exact redirect hop count for chains >1 hop — treat as needing a dedicated header/SSL-check tool if not confirmed working, otherwise mark `DATA NOT AVAILABLE`.
- Any WordPress Admin-side setting (plugin config, sitewide noindex toggles) — this skill does not have admin access itself; it consumes the system profile produced by [wordpress-seo](wordpress-seo.md), which does.

## Pre-Audit Checks

Run these before starting the full step-by-step process; do not skip them even if a prior session already established the answer — verify fresh each session.

1. **Pull robots.txt and the sitemap fresh this session.** Do not reuse a prior session's cached copy or assume the sitemap path from memory — fetch `https://cashahnawaz.com/robots.txt` live, read its `Sitemap:` directive(s), and fetch the sitemap URL it actually names. If it differs from what a previous audit assumed, that difference is itself worth noting.
2. **Confirm which WordPress SEO plugin is active before writing any plugin-specific fix instructions.** Check the [wordpress-seo](wordpress-seo.md) skill's system profile (`data/crawl/wordpress-system-profile.md`) if it exists this session; if it doesn't exist yet or is stale, run (or request) that skill's Step 1 first rather than guessing from sitemap URL pattern alone. Never write "in Yoast, go to..." without this confirmation.
3. **Verify WebFetch is actually returning usable content for this site right now** — fetch the homepage and confirm the response is markup, not an error page, login wall, or bot-block page (some security plugins block automated fetches; this would itself be a finding, but first it needs to be recognized rather than mistaken for "page returned no title").
4. **Confirm GSC connectivity status for this session** (working / not working) before deciding whether GSC-dependent checks in the process below run live or get marked `DATA NOT AVAILABLE`.

## Step-by-Step Audit Process

1. **Indexability baseline**
   - Fetch `robots.txt`. Check for accidental `Disallow` rules blocking important paths (especially `/wp-admin/` exceptions, service pages, or an entire site block left over from staging).
   - Fetch the sitemap index and each child sitemap. Confirm it lists priority service pages, is well-formed XML, and isn't returning 404/500.
   - For each priority service page (see CLAUDE.md priority services list), check: HTTP status, `<meta name="robots">` content, `X-Robots-Tag` header, canonical tag target.
   - Flag any priority page that is `noindex`, blocked in robots.txt, missing from the sitemap, or canonicalized to a different URL.

2. **Crawlability**
   - Confirm crawl (see website-crawl skill) reaches all priority service pages within reasonable depth (ideally ≤3 clicks from homepage).
   - Identify orphan pages (in sitemap but not linked internally, or vice versa).
   - Check for crawl traps: faceted/filtered URLs, session IDs, infinite pagination, WordPress default archive/tag/author pages generating thin duplicate content.

3. **Status codes & redirects**
   - From the crawl, list all non-200 responses: 3xx, 4xx, 5xx.
   - For every redirect, confirm it's a single-hop 301 (not a chain, not a 302 used permanently).
   - Check for redirect loops.
   - Spot-check that old/legacy URLs (if any prior URL structure existed) still redirect correctly rather than 404ing.

4. **Canonicalization & duplicate content**
   - Check WWW vs non-WWW and HTTP vs HTTPS: confirm exactly one canonical version is enforced site-wide via redirect, not just a canonical tag.
   - Check trailing-slash consistency.
   - Check for duplicate content from WordPress taxonomy pages (tags, categories) competing with service pages, and parameter-based duplicates (`?replytocom=`, UTM-tagged internal links, etc.).

5. **HTTPS & security**
   - Confirm valid SSL certificate, no mixed-content warnings (HTTP resources loaded on HTTPS pages), HSTS if applicable.

6. **Sitemap & structured navigation**
   - Confirm sitemap freshness (lastmod dates plausible, not stale for months if content has changed).
   - Confirm sitemap doesn't include noindexed, redirected, or 404 URLs.

7. **International/regional targeting** (if relevant — NRI Taxation service suggests some international audience)
   - Check for any hreflang implementation issues if multiple regional variants exist. If none exist and none are needed, note as not applicable.

8. **Core Web Vitals & mobile** — hand off to [performance-audit](performance-audit.md) skill for the detailed pass; here just confirm GSC's Core Web Vitals report status (Good/Needs Improvement/Poor URL groups) if GSC is accessible.

9. **Structured data presence** — hand off to [schema-audit](schema-audit.md) for depth; here just note whether structured data exists at all sitewide as a technical baseline.

## What Checks to Perform (checklist form)

- [ ] robots.txt accessible, correctly formatted, not blocking priority content
- [ ] XML sitemap valid, submitted, matches live indexable URLs
- [ ] All priority service pages return HTTP 200
- [ ] No priority page is noindexed or canonicalized away
- [ ] No redirect chains >1 hop on internal links
- [ ] No redirect loops
- [ ] Single enforced canonical domain (protocol + www)
- [ ] No mixed content
- [ ] Valid SSL, no cert warnings
- [ ] No orphan priority pages
- [ ] No thin/duplicate WordPress taxonomy pages indexed unintentionally
- [ ] GSC Coverage report reviewed for Excluded/Error URLs (if accessible)
- [ ] GSC Core Web Vitals report reviewed (if accessible)

## How to Identify Issues

Cross-reference crawl output against the priority services list in CLAUDE.md. Any priority service without a clean, indexable, 200-status, canonical-self page is an issue regardless of other findings. Cross-reference GSC Coverage "Excluded" reasons (if available) against what the crawl independently found — discrepancies (e.g., GSC shows "Crawled – currently not indexed" for a page the crawl shows healthy) are themselves findings worth flagging (possible content quality / quality-threshold issue).

## Evidence to Collect

- Raw robots.txt content (save to `data/crawl/robots.txt`)
- Sitemap URL list (save to `data/crawl/sitemap-urls.txt` or `.json`)
- Full crawl status-code table (save to `data/crawl/`)
- Screenshot or export of GSC Coverage/Core Web Vitals report if accessible (save to `data/gsc/`)
- Specific HTTP header dumps for flagged URLs

## How to Prioritize Issues

- **CRITICAL:** Priority service page noindexed/blocked/404; sitemap or robots.txt broken sitewide; site-wide indexing collapse visible in GSC.
- **HIGH:** Redirect chains/loops on priority pages, duplicate canonical domain not enforced, orphaned priority pages.
- **MEDIUM:** Thin taxonomy pages indexed, stale sitemap, minor redirect inefficiencies on non-priority pages.
- **LOW:** Cosmetic header inconsistencies, non-impactful parameter duplicates with correct canonical already in place.

## Implementation Recommendations

Always give WordPress-specific implementation steps: which plugin controls the setting (Yoast SEO / RankMath / All in One SEO — identify which is installed first), which admin screen, or which `.htaccess`/server config change is needed, and whether hosting-level access is required. Never assume a generic CMS fix — check what's actually installed (see [wordpress-seo](wordpress-seo.md) skill for how to detect the SEO plugin) before prescribing steps.

For the exact menu path/setting name once the plugin is known, route to [wordpress-seo](wordpress-seo.md)'s "Plugin-Specific Settings Reference" rather than re-deriving it here — that section is the single source of truth for Yoast/Rank Math/AIOSEO UI locations so instructions stay consistent across skills.

### WordPress-specific technical patterns to check explicitly

These are common, WordPress-default-behavior sources of technical issues on a CA/tax site and should each get their own checklist line, not be folded silently into general "duplicate content" notes:

- **Category/tag archive pages competing with priority service pages.** WordPress auto-generates `/category/x/` and `/tag/x/` archive URLs. On a CA/tax site these often thinly duplicate or dilute a dedicated priority service page (e.g., a "GST" tag archive competing with the actual GST Registration service page for the same query intent). Check whether these archives are indexed, and whether any outrank or cannibalize a priority page.
- **Attachment-page auto-indexing.** WordPress creates a standalone page for every uploaded media file by default (`/?attachment_id=` or `/attachment-slug/`) unless the SEO plugin's "redirect attachment URLs to file/parent" setting is enabled. This is a classic default-on issue that silently generates thin, near-duplicate indexable pages at scale. Check sitemap and crawl data for attachment URLs.
- **`?attachment_id=` parameter duplicates.** Related to the above — confirm these parameterized URLs aren't independently indexable/canonicalized to themselves rather than to the parent post/page.
- **Plugin-conflict detection (two SEO plugins simultaneously active).** This is a known, common WordPress failure mode: if a second SEO plugin (or a theme's built-in SEO module) is active alongside the primary one, it typically produces duplicate `<title>`/meta tags, duplicate or conflicting JSON-LD schema blocks, and/or duplicate/competing XML sitemaps. Explicitly check page source for more than one set of OG tags, more than one JSON-LD `Organization`/`WebSite` block, or more than one sitemap index. Treat any confirmed instance as its own CRITICAL finding regardless of what else is found, and cross-reference [wordpress-seo](wordpress-seo.md) for the plugin inventory that would explain it.
- **REST API / `wp-json/` endpoints accidentally indexed** — check whether any `/wp-json/` paths appear in the sitemap or crawl inventory as indexable content; these should never be treated as content pages.

## How to Validate Fixes

- Re-crawl the affected URL(s) and confirm status/canonical/robots directive changed as expected.
- Use GSC URL Inspection ("Test Live URL") to confirm Google's rendering matches expectation, then request indexing if appropriate.
- Re-check robots.txt/sitemap after any plugin or server change.
- Monitor GSC Coverage report over the following 1-2 weeks for the affected URLs to move to "Indexed."

## Expected Output Format

A finished technical-seo audit pass produces findings using the CLAUDE.md Required Finding Template exclusively — this skill mainly populates **Evidence** (status codes, header/meta values, robots.txt/sitemap excerpts), **Affected URLs**, **Likely Root Cause** (technical mechanism, e.g. "attachment pages auto-indexed because SEO plugin's redirect-attachment setting is off"), and **Implementation Steps** (plugin path from wordpress-seo.md, or server/.htaccess change).

Supporting evidence tables should accompany the findings, saved under `data/crawl/` or referenced from it:

- **Status code / redirect table** — columns: `URL | Status | Final URL | Redirect Chain (hops) | Redirect Type (301/302) | Notes`
- **Indexability table** — columns: `URL | Meta Robots | X-Robots-Tag (or DATA NOT AVAILABLE) | Canonical Target | In Sitemap? (Y/N) | Blocked by robots.txt? (Y/N)`
- **Domain/protocol enforcement table** — columns: `Variant Tested (http/https/www/non-www/trailing-slash) | Result | Redirects To | Single-Hop? (Y/N)`

Every finding in the final report should be traceable back to a specific row in these tables or to a specific fetched artifact (robots.txt content, sitemap excerpt).

## Common Mistakes to Avoid

- **Treating a 200-status page as "healthy" without checking its noindex meta tag.** A page can return HTTP 200 and still be excluded from the index via `<meta name="robots" content="noindex">` — this is a very common false-negative if the audit stops at status code.
- **Assuming HTTPS enforcement from one successful redirect.** Confirming `http://cashahnawaz.com/` redirects to `https://` is not the same as confirming *every* HTTP URL pattern does, or that a canonical/internal link doesn't still point at an HTTP version. Test both directions and a few different entry URLs, not just the homepage.
- **Confusing "we fetched it fine" with "Google indexes it fine."** Crawl-tool success is not GSC-confirmed indexing status — don't phrase a finding as "indexed" unless GSC URL Inspection actually confirmed it, or GSC wasn't accessible and the finding says so.
- **Writing plugin-specific fix instructions before confirming which plugin is actually active.** Never default to "in Yoast..." out of habit — always confirm via wordpress-seo.md's system profile first, even if a prior audit identified the plugin (it can change).
- **Miscounting WordPress-native non-content URLs as orphan or thin content pages.** Category/tag archives, author pages, and `wp-json/` endpoints follow different rules than genuine service/content pages — don't apply "priority service page must have X inbound links" logic to them.
- **Marking a redirect chain as "fixed" from a single re-fetch without checking cache.** If a caching plugin is active (see wordpress-seo.md), a stale cached response can still serve the old redirect/status even after the underlying setting changed — purge or note cache status before validating.
- **Reporting `X-Robots-Tag` or other raw header values as confirmed when they came from a WebFetch summary rather than a raw header inspection.** If the tool used doesn't guarantee raw header visibility, mark that field `DATA NOT AVAILABLE` rather than inferring it from page content.
- **Treating GSC Core Web Vitals report status as this skill's finding rather than performance-audit's.** This skill only notes whether the report exists/its bucket counts — the diagnosis and fix belong to performance-audit.md; don't duplicate that analysis here.
