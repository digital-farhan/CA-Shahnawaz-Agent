# Skill: Website Crawl

## Purpose

Produce the raw, first-party evidence base that almost every other skill in this project depends on: an actual, current map of cashahnawaz.com's URLs, status codes, on-page elements, and internal link graph. This skill doesn't diagnose issues itself — it collects the ground truth that [technical-seo](technical-seo.md), [on-page-seo](on-page-seo.md), [content-audit](content-audit.md), [internal-linking](internal-linking.md), and [schema-audit](schema-audit.md) all read from.

## Scope

This skill is **pure evidence collection — it does not diagnose or prioritize issues.** Its only job is to produce an accurate, current, first-party URL inventory and link graph that other skills read from.

**In scope:**
- Discovering the full URL set (sitemap + on-site navigation cross-check)
- Fetching each URL and recording status code, redirect chain, title, meta description, canonical, robots meta, H1, approximate word count, structured data JSON, outbound internal links, image alt-attribute presence, form/contact-element presence
- Building the inbound-link-count graph
- Flagging (not diagnosing) surface-level anomalies: non-200s, missing title/meta/H1, zero-inbound-link orphans, duplicate titles, priority services with no matching URL at all
- Classifying each URL by type, including separating WordPress-native non-content URL patterns from genuine content pages

**Out of scope — hand off instead:**
- Interpreting *why* a status/indexability issue exists, or its severity → [technical-seo](technical-seo.md)
- Content quality/thinness judgment beyond raw word count → [content-audit](content-audit.md)
- Internal-linking strategy, anchor text quality, link equity flow → [internal-linking](internal-linking.md)
- Schema type correctness/completeness → [schema-audit](schema-audit.md) (this skill only captures the raw JSON-LD)
- On-page title/meta/heading quality judgment → [on-page-seo](on-page-seo.md)
- Which plugin/theme is generating any of this behavior → [wordpress-seo](wordpress-seo.md)
- Formal findings using the CLAUDE.md template — this skill supplies the Evidence and Affected URL data those findings cite; it does not itself write CRITICAL/HIGH/etc. findings (the one exception, noted below, is a completely missing priority-service URL, since that gap would otherwise never surface).

If a downstream skill needs a re-crawl of a narrower slice (e.g., technical-seo wants fresh header data for 5 flagged URLs), that targeted re-fetch is still this skill's responsibility to perform/support, not a fork of it.

## When to use it

- First step of any audit cycle, before technical/on-page/content/linking/schema work.
- After any site change (new pages, redesign, plugin change) to refresh the evidence base.
- Whenever a finding needs verification against current live state rather than a stale prior crawl.

## Required Data

- Working web-fetch or browsing capability (verify this actually works before relying on it — see capability inspection).
- The site's sitemap (`https://cashahnawaz.com/sitemap_index.xml` or equivalent — confirm actual path from robots.txt) as a starting URL list.
- Homepage HTML as a fallback/secondary crawl seed if sitemap is incomplete.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- WebFetch against any live, non-blocked URL — returns processed/AI-summarized markup from which title, meta description, H1, canonical target, visible robots meta, visible internal links, and visible JSON-LD blocks can generally be extracted via a targeted extraction prompt.
- robots.txt and XML sitemap(s) — plain text/XML, directly fetchable and reliable as the URL-list source of truth once confirmed to resolve.
- Approximate word count and internal link enumeration from rendered page content.

### DATA NOT AVAILABLE / REQUIRES VERIFICATION
- **Byte-exact HTML** — WebFetch summarizes/processes content; it is not a guaranteed byte-for-byte HTML dump. Any finding that depends on exact character counts (e.g., title tag length for SERP truncation) or exact tag casing/attribute order needs a second, more targeted fetch/verification pass before being stated as precise fact — don't treat the first summarized pull as exact.
- **Raw HTTP response headers** (`X-Robots-Tag`, `Cache-Control`, redirect-hop status codes at each intermediate step) — mark `DATA NOT AVAILABLE` unless a header-capable tool is confirmed working this session.
- **JS-rendered content** — no guarantee WebFetch executes client-side JavaScript; content injected client-side (some page-builder/lazy-loaded elements) may be invisible to the crawl and must be flagged as a limitation rather than reported as "missing."
- **Full-site exhaustive crawl for very large sites** — if the sitemap/site is large, a representative priority-page sample may be used instead of every URL; this must be stated explicitly in the output, not silently substituted.
- **Rate-limit or bot-block behavior** — if fetches start failing or returning degraded content partway through, note this as a crawl limitation immediately rather than treating partial data as complete.

## Pre-Audit Checks

1. **Confirm WebFetch actually works against the homepage AND one interior page before trusting the full crawl.** A homepage-only success can mask template-specific failures (e.g., a page-builder template that fetches differently than the homepage). Do not proceed to the full URL list build until both checks return usable markup.
2. **Confirm the sitemap URL named in robots.txt actually resolves (200, valid XML) before treating it as the URL source of truth.** If it 404s, redirects unexpectedly, or returns malformed XML, fall back to homepage/navigation-based discovery and state explicitly that the sitemap could not be used as primary source this session.
3. **Note the session date/timestamp before starting** — every output file and finding this crawl feeds should be traceable to this specific pull date so staleness can be judged later.

## Step-by-Step Audit Process

1. **Confirm crawl capability.** Attempt to fetch the homepage and one interior page. If fetching fails or only returns partial/rendered-without-JS content, note that limitation explicitly — it affects what later skills can claim as evidence (e.g., JS-rendered content may be invisible to a simple fetch).

2. **Build the URL list.**
   - Fetch `robots.txt`, note sitemap location(s).
   - Fetch the sitemap index and all child sitemaps; compile a full URL list with `lastmod` where present.
   - Cross-check against homepage/menu navigation links and footer links for any URL not in the sitemap (candidate orphan or candidate "shouldn't be indexed" page).

3. **Fetch each URL (or a representative priority sample if the site is large).** For each, capture:
   - HTTP status code
   - Final URL after redirects (and the redirect chain)
   - `<title>` tag
   - Meta description
   - Canonical tag target
   - `<meta name="robots">` / `X-Robots-Tag`
   - H1 (count and text)
   - Word count of visible body content (approximate)
   - Outbound internal links found on the page (target URL + anchor text)
   - Structured data blocks present (`<script type="application/ld+json">`) — capture raw JSON for [schema-audit](schema-audit.md)
   - Images without `alt` attributes (count)
   - Presence of forms and their action targets (for [gtm-conversion-audit](gtm-conversion-audit.md) cross-reference)
   - Presence of phone/WhatsApp click elements (`tel:`, `wa.me`, WhatsApp widget)

4. **Classify each URL** by type: priority service page, other service/product page, blog/article, category/tag archive, static page (About/Contact/Privacy), or non-content (search results, filtered/parameterized).

   **Explicitly separate WordPress-native URL patterns from genuine content pages during classification** — these follow different rules and must not be counted toward priority-service coverage or content-page inbound-link expectations:
   - `/category/...` and `/tag/...` — taxonomy archives, not content pages
   - `/author/...` — author archives
   - `/?attachment_id=` or `/attachment-slug/` patterns — media attachment pages (a classic WordPress default-indexing issue)
   - `/wp-json/...` — REST API endpoints; flag immediately if any appear in the sitemap or receive internal links as if they were content, since that indicates a misconfiguration worth handing to technical-seo
   - `/page/2/`, `/page/3/`, etc. — pagination of an archive, not a distinct content page
   - Search result URLs (`?s=`) and other query-parameterized non-canonical duplicates

   Tag each such URL with a `page_type` of `wp-system` (or a similarly distinct label) in the inventory rather than leaving it ambiguous, so downstream skills (especially technical-seo's priority-service coverage mapping) can filter it out rather than accidentally counting it as a content page.

5. **Build the internal link graph.** From the outbound link data, compute for each URL: inbound internal link count. Flag priority service pages with zero or very low (1-2) inbound internal links.

6. **Save outputs** to `data/crawl/`:
   - `data/crawl/url-inventory.csv` (or `.json`) — one row per URL with all captured fields
   - `data/crawl/robots.txt`
   - `data/crawl/sitemap-urls.txt`
   - `data/crawl/link-graph.json` (inbound/outbound counts)

## What Checks to Perform

- [ ] Every priority service page (per CLAUDE.md) successfully fetched and present in inventory
- [ ] Status code captured for every URL
- [ ] Redirect chains fully resolved and logged
- [ ] Title/meta description/H1/canonical captured for every URL
- [ ] Structured data raw JSON captured where present
- [ ] Internal link graph computed (inbound counts per URL)
- [ ] Crawl limitations (JS-rendering, blocked sections, rate limits hit) explicitly logged

## How to Identify Issues (at crawl stage)

The crawl stage itself should flag, not fully diagnose:
- URLs returning non-200
- URLs with missing title/meta description/H1
- URLs with zero inbound internal links (orphans)
- Multiple URLs with identical title tags (duplicate content signal)
- Priority services from CLAUDE.md with **no matching URL found at all** — this is itself a critical content gap finding, to be handed to [content-audit](content-audit.md).

## Evidence to Collect

The full `url-inventory` dataset itself is the evidence. Every downstream finding that cites "Affected URLs" and "Evidence" should be traceable back to a row in this inventory. Timestamp the crawl (date of pull) so staleness can be judged later.

## How to Prioritize Issues

Crawl-stage issues are inputs to other skills' prioritization, not scored here. The one exception: **a missing page for a priority service** should immediately be logged as an OPPORTUNITY (or HIGH if the service is high commercial value and completely absent) in the findings pipeline, since it affects nearly every other audit dimension.

## Implementation Recommendations

Not applicable at crawl stage — this skill produces evidence, not fixes. Route findings to the appropriate specialist skill.

## How to Validate

- Re-run the crawl after fixes are implemented elsewhere and diff the inventory against the previous pull to confirm expected changes (status code fixed, title updated, new inbound links present, etc.).
- If crawl capability itself is limited (e.g., no JS rendering), note that some validations (e.g., confirming a React-rendered element) may need manual browser confirmation instead.

## Expected Output Format

This skill's deliverable is evidence, not narrative findings — but its outputs must be structured consistently enough for every other skill to consume without re-parsing raw fetches. At minimum:

**`data/crawl/url-inventory.csv`** — one row per URL, header row exactly:

```
URL | Status | Redirect Chain | Title | Meta Description | Canonical | Robots Meta | H1 | Word Count | Schema Types | Inbound Links | Page Type
```

Where:
- `Redirect Chain` — the sequence of hops if any (e.g., `301: /old-url/ → /new-url/`), or blank if direct 200
- `Schema Types` — comma-separated `@type` values found in JSON-LD (e.g., `Organization, LocalBusiness`), or blank
- `Page Type` — one of: `priority-service`, `other-service`, `blog-article`, `static`, `category-archive`, `tag-archive`, `wp-system` (author/attachment/wp-json/pagination/search), `non-content`

**`data/crawl/robots.txt`** — raw fetched content, unmodified.

**`data/crawl/sitemap-urls.txt`** — flat list of every URL found across sitemap index + child sitemaps, with `lastmod` alongside where present.

**`data/crawl/link-graph.json`** — per-URL inbound and outbound internal link counts, plus the raw edge list (source URL → target URL, anchor text) so internal-linking.md doesn't need to re-derive it from raw HTML.

Every field this skill cannot actually confirm (e.g., a header-dependent field, or JS-rendered content) should be written as `DATA NOT AVAILABLE` in that cell rather than left blank or guessed — a blank cell is ambiguous between "not checked" and "confirmed empty," which the explicit label resolves.

This inventory primarily feeds the **Evidence** and **Affected URLs** fields of every downstream finding built on the CLAUDE.md Required Finding Template; it does not itself produce Severity/Root Cause/Fix content.

## Common Mistakes to Avoid

- **Treating WebFetch's AI-summarized extraction as exact when a claim needs byte-exact verification** — e.g., citing a title tag's precise character count for SERP-truncation analysis based on a summarized pull. Always flag when a finding needs a second, targeted fetch to confirm exact text rather than relying on a paraphrase.
- **Counting WordPress-native URLs (category/tag archives, attachment pages, author pages, wp-json endpoints) as content pages** in priority-service coverage or inbound-link statistics — tag them `wp-system`/archive types explicitly so downstream skills filter correctly.
- **Treating a sitemap-listed URL as automatically indexable** without confirming it actually returns 200 and isn't noindexed — the sitemap states intent, not confirmed status.
- **Silently substituting a partial/sample crawl for a full crawl** on a large site without stating that substitution explicitly in the output — every downstream skill needs to know if it's looking at 100% or a sample.
- **Missing a redirect chain's intermediate hops** by only recording the final destination URL — a 3-hop chain and a clean 1-hop redirect look identical if only the end state is captured, but they're very different findings for technical-seo.
- **Letting a stale sitemap silently stand in as the URL source of truth** without checking `lastmod` plausibility or cross-referencing against on-site navigation — a sitemap that hasn't updated in months on a site that clearly has newer content is itself worth flagging, not just trusting.
- **Reporting "no structured data found" without distinguishing "confirmed absent" from "couldn't be captured due to JS-rendering limits."** These have very different implications for schema-audit's next steps.
- **Re-running a diff-validation crawl and attributing every difference to the fix under test** without checking whether unrelated content changes (a new blog post, a plugin update) also landed in between, which would confound the comparison.
