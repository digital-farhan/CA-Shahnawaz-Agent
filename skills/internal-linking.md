# Skill: Internal Linking Audit

## Purpose

Ensure link equity and navigational paths flow toward the priority service pages, so both users and Google can easily find and understand the importance of the pages that matter most for enquiries (Income Tax, GST, Accounting, Audit, Registration & Compliance services).

## Scope

This skill owns: internal link equity flow, anchor text quality, click depth, navigation/menu placement, and contextual cross-linking between pages on cashahnawaz.com.

This skill does **not** own:

- Whether the *target* page itself is well-optimized once linked to (title/meta/heading/content-intent match) — that's [on-page-seo](on-page-seo.md). This skill concerns itself with whether a page is findable and well-linked, not whether the page is good once found.
- Whether new content/pages should exist at all, or whether existing content is deep/fresh enough to deserve more links — that's [content-audit](content-audit.md). This skill flags "this page needs more inbound links," not "this topic needs a new page" (though it may note the latter as an observation to hand off).
- Structured data / BreadcrumbList schema correctness — that's [schema-audit](schema-audit.md); this skill cares about breadcrumbs only as a navigational/click-depth signal, not their JSON-LD validity.
- The root cause of broken links (redirect chains, 404 sources, server config) — that's [technical-seo](technical-seo.md); this skill flags that an internal link points to a broken/redirected URL (using technical-seo's status-code data) but doesn't diagnose the underlying technical cause.
- Raw link-graph extraction itself — that's [website-crawl](website-crawl.md); this skill consumes that output, it doesn't produce it.
- Which theme/menu system or page builder controls the live site's navigation — identified via [wordpress-seo](wordpress-seo.md)'s theme identification; this skill uses that identification to give correct "where to make the change" instructions but doesn't do the identification itself.
- External backlinks/off-site link equity — out of scope entirely for this project's current skill set; do not conflate off-site link building with internal linking.
- CTA placement/button design within a page (conversion-path UX) — that's [cro-audit](cro-audit.md), even where "link to the priority page" overlaps with a conversion-path recommendation; this skill recommends that the link exists, cro-audit judges the surrounding conversion design.

**Boundary rule of thumb:** if the question is "can users/Google reach this page easily, and does the link structure signal its importance," it's this skill. If the question is "is the page itself good" or "should this page/content exist," route to on-page-seo or content-audit respectively.

## When to use it

- After [website-crawl](website-crawl.md) produces the link graph (inbound/outbound counts per URL).
- When a priority service page has weak organic visibility despite reasonable content ([gsc-analysis](gsc-analysis.md)) — check whether it's simply under-linked internally.
- When new content is published (blog posts, new service pages) and needs to be woven into the existing link structure.

## Required Data

- Link graph from [website-crawl](website-crawl.md): every internal link found, source URL, target URL, anchor text.
- URL inventory with page classification (priority service, other service, blog, static, archive).

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS

- From a working [website-crawl](website-crawl.md): the internal link graph (source URL, target URL, anchor text for every internal link found), URL inventory with page classification, and click-depth-from-homepage calculations derived from that graph — high confidence when the crawl is complete.
- From [technical-seo](technical-seo.md) status-code data, where supplied: which internal links point to broken/redirected URLs — high confidence, direct HTTP status observation.
- From a working GSC connection, where cited via [gsc-analysis](gsc-analysis.md): whether a page has strong impressions/rankings despite weak internal linking (a signal of under-served inherent demand) — Google's own reported data, usable when access is confirmed.

### DATA NOT AVAILABLE

- If the crawl is partial or failed (didn't complete, hit a crawl limit, or errored on sections of the site): **inbound-link counts are understated** for any page the crawl didn't fully traverse, and the link graph cannot be trusted as complete. Do not report inbound-link counts or click-depth figures from a partial crawl as if they were final/reliable — mark them `DATA NOT AVAILABLE`, or explicitly caveat them as a lower bound from a partial crawl, and prioritize re-running/completing the crawl before drawing firm conclusions.
- If GSC access is not verified working this session: the "strong demand despite poor linking" cross-reference is unavailable — mark it `DATA NOT AVAILABLE` rather than assuming a page has strong inherent demand.
- Do not estimate click depth or inbound-link count by browsing the site manually as a substitute for full crawl data — manual spot-checks can supplement but not replace a complete crawl-derived link graph, since manual browsing will miss links outside the pages actually visited.

## Pre-Audit Checks

Before starting the step-by-step process below:

1. **Confirm the crawl's link graph is complete, not partial.** Check the crawl output/log for completion status, crawl limits hit, or sections that errored out. A partial crawl systematically understates inbound-link counts (pages the crawler never reached can't be recorded as linking anywhere), which would make a page look more under-linked than it actually is. Do not trust inbound-link counts from a crawl you haven't confirmed completed successfully.
2. **Confirm the priority services list and groupings in CLAUDE.md** are current, so cluster-linking checks (e.g., "do all GST pages interlink") are evaluated against the right grouping.
3. **Confirm which theme/menu system is in control of primary navigation** (via [wordpress-seo](wordpress-seo.md)'s theme identification) before prescribing exact "where to edit navigation" implementation steps — see the theme/menu-system distinction in Implementation Recommendations below.
4. **Confirm orphan-page and broken-link findings from [website-crawl](website-crawl.md) / [technical-seo](technical-seo.md) are current** for this same crawl run, not carried over from a previous audit cycle, before cross-referencing them here.

## Step-by-Step Audit Process

1. **Inbound link count per priority page.** From the link graph, count internal inbound links to each priority service page. Compare against non-priority pages — ideally priority service pages should be among the most internally-linked pages on the site, not buried.

2. **Navigation/menu audit.** Confirm main navigation and footer include (directly or via a clear services dropdown/mega-menu) links to all priority services, or at minimum to a well-organized services hub page that itself links to all of them within one click. Flag any priority service absent from primary navigation.

3. **Homepage linking audit.** Check whether the homepage links to priority service pages (homepage typically carries the most link equity and internal/external authority on a small business site).

4. **Click depth audit.** For each priority page, determine click depth from homepage (homepage → category/hub → service page = depth 2; deeper paths reduce discoverability and equity flow). Flag any priority page at depth >3.

5. **Anchor text audit.** Review anchor text used in links pointing to priority pages — descriptive, service-specific anchor text ("GST Registration process" linking to the GST Registration page) is stronger than generic anchors ("click here," "read more," "learn more"). Flag heavy reliance on generic anchors.

6. **Contextual/body-content linking.** Check whether related pages link to each other contextually within body content, not just via navigation — e.g., does the "GST Registration" page link to "GST Return Filing" and "GST Compliance" where topically relevant? Does an Income Tax blog post link to the "Income Tax Return Filing" service page? This is often the weakest area on template-built WordPress sites where only nav/footer links exist.

7. **Cross-service linking clusters.** Verify related-service clusters (e.g., all GST services, all Registration services) interlink with each other logically, forming topical clusters that reinforce topical authority — check against the service groupings defined in CLAUDE.md (Income Tax, GST, Accounting, Audit, Registration & Compliance).

8. **Orphan page check.** Cross-reference against [website-crawl](website-crawl.md) orphan findings — any priority page with zero inbound internal links is a critical linking failure.

9. **Blog-to-service linking.** If a blog exists, check whether articles link back to relevant service pages (this is often a missed, low-effort SEO win, and also supports the CRO goal by guiding blog readers toward a conversion path).

10. **Broken internal links.** Cross-reference against [technical-seo](technical-seo.md) status-code data — any internal link pointing to a 404 or redirect chain wastes link equity and harms UX.

11. **Over-linking / link dilution check.** Pages with an excessive number of outbound links (especially generic/footer-repeated links) dilute the value passed to any single link — check if footer/sidebar link blocks are reasonable in size.

## What Checks to Perform

- [ ] Inbound internal link count computed per priority page
- [ ] All priority services present in main navigation (directly or via clear hub)
- [ ] Homepage links to priority services (directly or via hub)
- [ ] Click depth ≤3 for every priority page
- [ ] Anchor text reviewed for descriptiveness on links to priority pages
- [ ] Contextual body-content cross-links checked within and across service clusters
- [ ] Zero-inbound-link (orphan) priority pages identified
- [ ] Blog-to-service linking checked (if blog exists)
- [ ] Internal links to broken/redirected URLs identified

## How to Identify Issues

Compare each priority page's actual inbound link count and click depth against the ideal (high inbound count, depth ≤2-3, present in nav). Read actual body content of related-service pages to check for missing contextual links (don't assume based on structure alone — confirm by reading the fetched content). A service with strong GSC impressions/rankings despite poor internal linking suggests strong inherent demand being under-served by site structure — a clear, low-effort-to-fix opportunity.

## Evidence to Collect

- The link graph data itself (from `data/crawl/link-graph.json`), with a derived summary table: Priority Page → Inbound Links → Click Depth → In Nav? (Y/N).
- Specific examples of missed contextual linking opportunities (quote the source page/paragraph where a natural link should exist).
- List of broken internal links with source and target.

## How to Prioritize Issues

- **HIGH:** Priority service missing from main navigation entirely; priority page is an orphan (zero inbound links); priority page at click depth >3.
- **MEDIUM:** Weak/generic anchor text to priority pages; missing contextual cross-links within a service cluster; broken internal links to priority pages.
- **LOW/OPPORTUNITY:** Blog-to-service linking gaps; minor anchor text optimization; footer link block tidiness.

## Implementation Recommendations

- Specify exact proposed links: source page, anchor text suggestion, target page — as a concrete list, not a vague "add more internal links" instruction.
- For navigation changes, note this is typically a WordPress Appearance → Menus change (or theme-specific mega-menu builder) — confirm which via [wordpress-seo](wordpress-seo.md) before prescribing exact steps.
- Recommend building/strengthening a "Services" hub page if one doesn't exist or is thin, since it's an efficient way to raise link equity to all priority pages at once.

### Where Navigation Changes Are Made (theme/menu system, not SEO plugin)

Unlike on-page-seo.md and schema-audit.md — where the relevant "which tool controls this" question is which SEO plugin is active — navigation/menu changes on a WordPress site are governed by the active **theme** or **page-builder menu system**, not the SEO plugin. Before prescribing exact implementation steps, confirm via [wordpress-seo](wordpress-seo.md)'s theme identification which of the following applies:

- **Native WordPress menus:** typically edited under Appearance → Menus (or the Full Site Editor's Navigation block on block-based themes) — the default path on a theme without a custom mega-menu system.
- **Theme-specific or page-builder mega-menu module:** many premium themes and page builders (e.g., a theme's own "Mega Menu" panel, or a builder's dedicated menu widget/module) replace or extend the native menu editor — if one is active, native Appearance → Menus edits may not be sufficient or may not be where the visible mega-menu is actually configured. Confirm which system is actually rendering the live navigation (view-source / live inspection) before writing implementation steps, rather than assuming native WordPress menus are in control.
- Ask "which theme/menu system," not "which SEO plugin," here — this is the key distinction from on-page-seo.md's and schema-audit.md's plugin-first pattern, since the SEO plugin generally has no control over primary navigation structure.

## How to Validate Fixes

- Re-crawl and confirm inbound link counts and click depth improved for the targeted pages.
- Track [gsc-analysis](gsc-analysis.md) indexing/position and [ga4-analysis](ga4-analysis.md) organic landing traffic for previously under-linked priority pages over the following weeks.
- Confirm no new broken links were introduced by the changes.

## Expected Output Format

Every internal-linking finding produced by this skill should be written using the CLAUDE.md Required Finding Template, primarily feeding **Issue**, **Evidence** (link graph excerpt, anchor text quotes), **Affected URLs**, and **Recommended Fix** (specific source → target → anchor-text proposals, not a vague "add more links" instruction).

Maintain a summary table (as referenced in Evidence to Collect) in this format:

| Priority Page | Inbound Links | Click Depth | In Nav? | Anchor Text Quality | Severity |
|---|---|---|---|---|---|
| /gst-registration/ | 2 | 3 | No | Generic ("click here") | HIGH |

Pair this with a concrete link-recommendation list (Source Page | Proposed Anchor Text | Target Page) so implementation is a checklist, not a general directive.

## Common Mistakes to Avoid

- Recommending heavy new cross-linking to a priority page without checking it doesn't create excessive/unnatural link density that reads as manipulative to users or to Google — more links is not automatically better.
- Treating a footer "sitewide" link to a priority page as equivalent in value to a genuine contextual body-content link — they are not equivalent for user experience, and arguably not for link-equity concentration either; reporting "this page has 40 inbound links" is misleading if all 40 are the same repeated footer/sidebar block.
- Reporting inbound-link counts or click depth from a partial/incomplete crawl as if they were final, when the crawl actually failed to reach parts of the site.
- Recommending generic anchor text ("click here," "learn more") in proposed-fix examples instead of modeling the descriptive, service-specific anchor text this skill is meant to promote.
- Prescribing "go to Appearance → Menus" implementation steps before confirming whether a theme/page-builder mega-menu module is actually in control of the live navigation instead.
- Flagging a page as an "orphan" without cross-checking against the most current website-crawl/technical-seo orphan data, when the underlying crawl may be out of date.
- Recommending a new link from page A to page B without actually reading page A's content to confirm a natural, topically relevant place for that link exists — a forced/irrelevant link is itself a UX and topical-relevance problem.
- Confusing "should this page exist" (content-audit's job) with "this page needs more internal links" (this skill's job) — don't let an internal-linking finding smuggle in a content-creation recommendation without routing it explicitly to content-audit.md.
