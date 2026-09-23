# Skill: Schema (Structured Data) Audit

## Purpose

Verify cashahnawaz.com uses structured data correctly to help Google understand the business type, services, location, and content — improving eligibility for rich results (FAQ snippets, breadcrumbs, local business panels) that increase visibility and CTR for a local professional-services firm.

## Scope

This skill owns: presence, correctness, validity, and completeness of structured data (JSON-LD, or microdata/RDFa if found) on cashahnawaz.com — i.e., whether the right schema `@type`s exist, are properly formed, and accurately reflect what's genuinely present on the page.

This skill does **not** own:

- Whether the underlying content claims referenced by schema (FAQ answers, service descriptions, article content) are accurate, current, or well-written — that's [content-audit](content-audit.md). This skill only checks that schema content *matches* what's visibly on the page, not whether that visible content is itself good.
- The source-of-truth business Name/Address/Phone (NAP) — that's [local-seo](local-seo.md), which verifies NAP correctness against Google Business Profile and other citations. This skill only checks that schema NAP fields *match* whatever local-seo.md has established as the correct source-of-truth NAP; it does not independently determine what the "correct" NAP is.
- Title/meta/heading optimization — that's [on-page-seo](on-page-seo.md), even though the same plugin UI sometimes exposes schema and meta fields together.
- The navigational/UX value of breadcrumbs — that's [internal-linking](internal-linking.md); this skill only checks that BreadcrumbList schema, where present, is structurally valid and matches the actual URL path, not its click-depth or nav-placement value.
- Page-load performance impact of large/inline schema blocks — that's [performance-audit](performance-audit.md).
- Crawlability/indexability of the pages carrying the schema — that's [technical-seo](technical-seo.md) / [website-crawl](website-crawl.md); this skill consumes the raw JSON-LD the crawl captured, it doesn't determine which pages exist.
- Identifying which WordPress SEO plugin/theme is active — that's [wordpress-seo](wordpress-seo.md); this skill asks it which plugin/theme is active so it can correctly attribute auto-generated schema.
- Competitor schema patterns — usable here only if supplied by [competitor-analysis](competitor-analysis.md); this skill does not independently crawl competitor sites.
- Pulling GSC/GA4/GTM data itself — this skill cites GSC Enhancements data when [gsc-analysis](gsc-analysis.md) supplies it, but doesn't pull it directly.

**Boundary rule of thumb:** if the question is "does the markup on this page correctly and validly describe what's actually there," it's this skill. If the question is "is what's there actually true/accurate/complete" (NAP, content, service claims), route to local-seo or content-audit respectively.

## When to use it

- After [website-crawl](website-crawl.md) captures raw JSON-LD blocks per page.
- When [gsc-analysis](gsc-analysis.md) Enhancements reports (if available) show structured data errors/warnings.
- When [local-seo](local-seo.md) audit needs to confirm LocalBusiness/ProfessionalService markup backs up NAP (Name/Address/Phone) claims.
- When adding a new service page or FAQ content, to check whether schema should be added alongside it.

## Required Data

- Raw JSON-LD (or microdata/RDFa, though JSON-LD is standard for modern WordPress SEO plugins) captured per page during crawl.
- GSC Enhancements reports (FAQ, Breadcrumbs, etc.) if GSC access is verified working — these show Google's actual parsing/eligibility status, which is stronger evidence than static validation alone.
- Knowledge of which WordPress SEO plugin is active (Yoast/RankMath/AIOSEO commonly auto-generate some schema — confirm via [wordpress-seo](wordpress-seo.md) before assuming schema is missing vs. plugin-generated but incomplete).

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS

- From a working [website-crawl](website-crawl.md): raw JSON-LD blocks captured per page — high confidence, this is direct extraction from rendered/raw HTML.
- Static validity checks performed on that raw JSON-LD (well-formed JSON, required properties present for the declared `@type` per schema.org) — deterministic inspection, doable with high confidence regardless of GSC access.
- From a working GSC connection: Enhancements reports (FAQ, Breadcrumbs, etc.) showing Google's actual parsing/eligibility status per schema type — the strongest available evidence of what Google itself sees, stronger than static validation alone, when accessible.

### DATA NOT AVAILABLE

- If GSC access is not verified working this session: **the GSC Enhancements cross-check step (Step 8 below) is impossible.** Do not guess whether Google considers a schema block "Valid," "Invalid," or eligible for a specific rich result — mark this `DATA NOT AVAILABLE` and state that findings rest on static/manual JSON inspection only, which is necessary-but-not-sufficient evidence of Google's actual parsing behavior. Never present inspection-only validity as equivalent to confirmed Google-side validity.
- Rich-result *eligibility* (e.g., "this will show a FAQ snippet") is never something to assert from static inspection alone — technically valid schema does not guarantee a rich result will display; Google narrows and changes eligibility rules over time. Say "eligible for consideration," not "will show."
- If the active plugin/theme is not yet confirmed via [wordpress-seo](wordpress-seo.md): do not assert whether missing schema is a genuine gap versus an unconfigured plugin feature — mark plugin-attribution findings as pending confirmation rather than guessing.

## Pre-Audit Checks

Before starting the step-by-step process below:

1. **Confirm whether GSC Enhancements access exists this session** (attempt the actual tool call). This materially changes audit depth: with it, findings can be anchored to Google's own parsing verdict; without it, every validity finding must be caveated as inspection-only per Data Sources & Limitations above. Decide and state which mode this audit run is operating in before starting.
2. **Confirm which WordPress SEO plugin is active** via [wordpress-seo](wordpress-seo.md), and whether a schema-capable theme or page builder is also in use. Yoast, Rank Math, and AIOSEO each auto-generate different baseline schema by default (see Implementation Recommendations below) — a "missing schema" finding is only valid once you know what the active plugin should already be producing versus what a human still needs to configure or add.
3. **Confirm the crawl captured rendered/final HTML, not just server-delivered source**, if the site uses any JS-injected schema — some page builders inject JSON-LD client-side, which a source-only crawl would miss and could produce a false "missing schema" finding.
4. **Confirm the [local-seo](local-seo.md) source-of-truth NAP is established** (or explicitly not yet available) before evaluating whether schema NAP fields are "correct" — without it, NAP-schema comparisons can only check internal consistency, not accuracy against ground truth.

## Step-by-Step Audit Process

1. **Inventory existing schema.** For each crawled page, list every `@type` present in JSON-LD blocks (e.g., `Organization`, `LocalBusiness`, `ProfessionalService`, `WebSite`, `BreadcrumbList`, `FAQPage`, `Service`, `Article`, `Person`). Note which pages have none at all.

2. **Organization/LocalBusiness schema** (should typically appear sitewide, often via header/footer template):
   - Confirm presence of business name, logo, URL, address, phone, matching what's actually shown on the site (no invented or mismatched NAP data — cross-reference against [local-seo](local-seo.md)).
   - Check `@type` appropriateness — a CA firm is well-suited to `ProfessionalService` or `AccountingService` (a valid schema.org type) rather than a generic `LocalBusiness`, if accurately descriptive of the actual services offered; note current type and whether it's the most descriptive available.
   - Check for `sameAs` links to verified social/business profiles if present.

3. **Service schema** on priority service pages:
   - Check whether each priority service page has `Service` markup (or is nested under a `ProfessionalService`'s `hasOfferCatalog`/`makesOffer`) naming the specific service (e.g., "GST Registration") — not just generic sitewide Organization markup repeated with no service-specific detail.
   - Confirm `areaServed` and `provider` fields are accurate if present.

4. **FAQPage schema**:
   - Cross-reference [content-audit](content-audit.md) FAQ findings — any page with genuine on-page FAQ content should have matching `FAQPage` schema to be eligible for FAQ rich results (note: Google has narrowed FAQ rich result eligibility over time to certain site types — treat as an opportunity, not a guarantee, and don't overstate expected impact).
   - Verify the schema's questions/answers actually match the visible on-page FAQ content exactly (mismatched/hidden schema content violates guidelines and risks a manual action).

5. **BreadcrumbList schema**:
   - Check presence and accuracy on interior pages (helps SERP display a clean URL path breadcrumb).

6. **Article schema** (for blog posts, if applicable):
   - Presence of `datePublished`/`dateModified`, author, headline — relevant for freshness signals in tax content especially (cross-reference [content-audit](content-audit.md) staleness findings — an outdated `dateModified` next to genuinely stale content compounds the trust problem).

7. **Validity check.** For each schema block found, check for structural validity: valid JSON syntax, required properties present for the declared type, no obviously placeholder/template values left in (e.g., a demo phone number or "Your Company Name" leftover from a theme's default schema template — this happens often with WordPress theme-bundled schema).

8. **GSC Enhancements cross-check** (if accessible): compare GSC's reported valid/invalid/warning counts for each schema type against your own findings — GSC's parser is the actual authority on what Google sees, so discrepancies with manual JSON inspection should defer to GSC's report where available.

9. **Duplicate/conflicting schema check**: WordPress sites sometimes have both a theme-level and plugin-level schema generator both firing, producing duplicate or conflicting `Organization`/`WebSite` blocks — flag if found.

## What Checks to Perform

- [ ] Every page's JSON-LD blocks inventoried by `@type`
- [ ] Organization/ProfessionalService schema present sitewide with accurate NAP
- [ ] Priority service pages have service-specific schema (not just generic sitewide markup)
- [ ] On-page FAQ content matched by FAQPage schema where present
- [ ] Breadcrumb schema present on interior pages
- [ ] Article schema present on blog posts with accurate dates
- [ ] No placeholder/template leftover values in schema
- [ ] No duplicate/conflicting schema blocks
- [ ] GSC Enhancements report cross-checked (if accessible)

## How to Identify Issues

Compare the JSON-LD inventory against the checklist per page type. Placeholder values are identified by literally reading the JSON for template-looking content (demo phone numbers, "Lorem ipsum," a different business name, wrong address). Mismatches between visible FAQ content and FAQPage schema content are found by direct text comparison.

## Evidence to Collect

- Raw JSON-LD snippets quoted per finding (exact, not paraphrased), with the source URL.
- GSC Enhancements report screenshots/export if accessible (`data/gsc/`).
- Save a schema inventory table to `data/crawl/schema-inventory.csv`: URL, schema types present, valid/invalid/notes.

## How to Prioritize Issues

- **CRITICAL:** Placeholder/incorrect NAP or business info live in schema (misleads Google about the actual business); FAQ schema content that doesn't match visible page content (guideline violation risk).
- **HIGH:** Missing Organization/ProfessionalService schema sitewide; missing service-specific schema on high-value priority pages.
- **MEDIUM:** Missing Breadcrumb/Article schema; duplicate/conflicting schema blocks.
- **OPPORTUNITY:** Adding FAQPage schema to pages with genuine FAQ content that currently lack it.

## Implementation Recommendations

- Identify whether the active WordPress SEO plugin (Yoast/RankMath/AIOSEO) already provides a schema builder UI — if so, recommend configuring through the plugin rather than hand-coding JSON-LD (safer, less error-prone, auto-updates with plugin best practices). Confirm which plugin via [wordpress-seo](wordpress-seo.md).
- Only recommend a custom JSON-LD snippet (via a plugin like "Insert Headers and Footers" or theme's custom code area) when the plugin's built-in schema genuinely can't express what's needed (e.g., a specific `Service` sub-type the plugin doesn't support).
- Always give the exact proposed schema properties/values based on real site information — never fabricate NAP, review counts, or ratings data in a schema recommendation.

### What Each Plugin Typically Auto-Generates (confirm live before relying on this)

Confirm the active plugin via [wordpress-seo](wordpress-seo.md) before using this as a baseline — plugin behavior varies by version and configuration, so treat the following as typical/common defaults to verify live, not settled fact for this specific install:

- **Organization/WebSite/BreadcrumbList schema** is commonly auto-generated sitewide by all three major plugins (Yoast SEO, Rank Math, AIOSEO) once basic setup is completed, without requiring per-page manual entry.
- **Yoast SEO:** typically generates Organization, WebSite, and BreadcrumbList schema automatically; FAQ and HowTo schema are generally driven by adding Yoast's dedicated FAQ/HowTo Gutenberg blocks to a post/page — if those blocks aren't used, FAQ-looking content elsewhere on the page will **not** automatically get `FAQPage` schema even though it visually reads as an FAQ.
- **Rank Math:** typically ships a more extensive built-in schema type picker per post/page (its "Schema" tab in the Rank Math panel), commonly including types such as Service, Product, FAQ, HowTo, and Article, selectable per page — a "missing Service schema" finding on a Rank Math site should first check whether this picker was simply left unset for that page, since the capability likely already exists.
- **All in One SEO (AIOSEO):** typically provides its own dedicated Schema Generator UI (a "Schema" tab in the page/post settings) allowing selection and configuration of schema types per page, separate from its general Organization/WebSite sitewide defaults.

Because auto-generation varies this much by plugin, a "missing schema" finding must state explicitly whether it means (a) the plugin doesn't offer this schema type at all, (b) the plugin offers it but it's unconfigured/unset on this page, or (c) something is actively overriding/suppressing it — these have different fixes and different severities.

### Detecting Plugin-vs-Theme Schema Conflicts

WordPress themes (especially page-builder themes and some premium professional-services themes) sometimes bundle their own schema generation independent of the SEO plugin. Check specifically for:

- **Duplicate competing Organization/WebSite blocks** — more than one JSON-LD block declaring `@type: Organization` or `@type: WebSite` on the same page, potentially with different/conflicting name, logo, or URL values between the theme's version and the plugin's version. This is a genuine conflict, not just redundancy, when the values disagree.
- **Duplicate BreadcrumbList blocks** — a theme-generated breadcrumb schema alongside a plugin-generated one, which can confuse which breadcrumb path Google actually uses.
- **Source attribution** — when a duplicate/conflicting block is found, identify (via view-source inspection, and if needed by consulting plugin/theme documentation or asking the user) which system emitted which block, so the recommended fix is "disable the theme's schema module and rely on the plugin" (or vice versa) rather than a vague "remove duplicate schema."
- **Severity:** conflicting NAP/business-identity values between duplicate blocks should be treated as CRITICAL or HIGH per the severity table above (misleads Google about the actual business); non-conflicting but merely redundant duplicate blocks are MEDIUM.

## How to Validate Fixes

- Validate updated JSON-LD structurally (well-formed JSON, required properties present) after implementation.
- Use GSC URL Inspection / Rich Results eligibility check to confirm Google parses it without errors.
- Monitor GSC Enhancements report over following weeks for the affected schema type moving from Invalid/Warning to Valid, and note if this correlates with any rich-result appearance change.

## Expected Output Format

Every schema finding produced by this skill should be written using the CLAUDE.md Required Finding Template, primarily feeding **Issue**, **Evidence** (quoted raw JSON-LD), **Affected URLs**, **Likely Root Cause** (plugin default vs. unconfigured feature vs. theme conflict vs. genuine hand-coding gap), and **Recommended Fix**.

Maintain the schema inventory table (already specified in Evidence to Collect, `data/crawl/schema-inventory.csv`) using this column format:

| URL | Schema @type Found | Plugin-Generated? | Valid? | Missing/Recommended Type | Severity |
|---|---|---|---|---|---|
| /gst-registration/ | Organization, BreadcrumbList | Yes (Rank Math) | Yes | Service (unconfigured in Rank Math schema picker) | HIGH |

"Plugin-Generated?" should specify which plugin/theme where known, or "Unknown — plugin not yet confirmed" rather than left blank. "Valid?" reflects static inspection unless a GSC Enhancements cross-check confirms Google-side validity, in which case note that source explicitly (e.g., "Yes — confirmed via GSC Enhancements").

## Common Mistakes to Avoid

- Flagging schema as "missing" when it's actually generated dynamically by the plugin and simply wasn't visible in the specific crawl snapshot (e.g., JS-injected schema missed by a source-only crawl) — recommend a live re-check (view rendered source, or a fresh JS-rendered crawl) before finalizing a "missing" finding.
- Copying a competitor's schema pattern (via competitor-analysis findings) without confirming it actually fits this business's real offerings — copying a `Service` list, `areaServed`, or NAP structure that doesn't match cashahnawaz.com's actual services or address creates a new, self-inflicted schema error.
- Treating an unconfigured plugin feature (e.g., Rank Math's Service schema picker left blank) the same as a genuine capability gap requiring custom code — the fix and effort level differ, and the finding's Root Cause field should say which one it is.
- Asserting rich-result eligibility ("this will get a FAQ snippet") from static validity alone, without caveating that Google controls actual display and has narrowed FAQ/HowTo eligibility over time.
- Missing a plugin-vs-theme duplicate/conflicting Organization or WebSite block because only one schema block on the page was checked instead of scanning every JSON-LD `<script>` tag present.
- Recommending hand-coded JSON-LD via a custom-code plugin when the active SEO plugin already offers a built-in, safer way to produce the same schema — hand-coding should be a last resort, not a default recommendation.
- Confirming FAQPage schema "exists" without actually text-comparing its questions/answers against the visible on-page FAQ content — a mismatch here is a guideline-violation risk, not just a technical nicety.
- Presenting an inspection-only validity judgment as if it were GSC-confirmed when GSC access wasn't actually available that session — always state which evidentiary basis (static inspection vs. GSC Enhancements) backs each validity claim.
