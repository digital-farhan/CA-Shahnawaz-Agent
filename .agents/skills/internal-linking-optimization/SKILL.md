---
name: internal-linking-optimization
description: Audit and plan internal linking for SEO, crawlability, topical relationships, user journeys, and priority-page visibility. Use for full internal-link audits, orphan/depth/anchor analysis, contextual-link opportunity mapping, implementation briefs, or post-change validation; do not use for external link building.
---

# Internal Linking Optimization

Produce evidence-led, client-ready internal-linking audits and precise implementation briefs. Optimize for users and search discovery together; do not reduce the work to adding keyword-rich links or chasing a universal link-count target.

## Governing rules

1. Read the workspace's governing instructions before analysis. In this project, `../../../CLAUDE.md` makes all live systems read-only and requires the user to implement every recommendation manually.
2. Do not claim a complete audit from a partial crawl. State `DATA NOT AVAILABLE` for metrics that cannot be supported.
3. Treat cutoffs such as depth 3, low inlink counts, anchor ratios, or Link Score as prioritization heuristics, never Google rules or ranking guarantees.
4. Separate observed facts, derived metrics, professional judgment, and proposed changes.
5. Recommend a link only after inspecting the source and target pages. The link must be useful in context, point to the preferred canonical 200 URL, and set an accurate expectation.
6. Never implement on the live website, Search Console, analytics, WordPress, Elementor, menus, templates, or plugins. Provide manual steps and validation only.

## Choose the operating mode

- **Readiness check:** Determine whether available crawl, sitemap, rendered-page, GSC, and business-priority inputs can support a defensible audit.
- **Full audit:** Diagnose crawlability, architecture, internal authority distribution, anchors, topical clusters, and user paths across the eligible URL set.
- **Opportunity plan:** Produce a source-to-target link plan for specified priority pages or content clusters.
- **Validation:** Compare pre/post crawls and confirm only the approved changes, regressions, and unresolved items.

For a full audit or opportunity plan, read [references/audit-methodology.md](references/audit-methodology.md). For workspace data fields and normalization, read [references/data-contract.md](references/data-contract.md). For a client-facing report or implementation brief, also read [references/client-deliverable.md](references/client-deliverable.md). When methodology claims or thresholds need support, use [references/industry-basis.md](references/industry-basis.md).

## Minimum evidence gate

A full sitewide audit normally needs:

- a completed, current crawl with source URL, target URL, anchor or image alt, link location, followability, status/final URL, canonical/indexability, and crawl depth;
- a URL inventory classified by page type and business priority;
- sitemap URLs to detect sitemap-only pages;
- rendered checks for links controlled by JavaScript, responsive navigation, accordions, or page builders;
- verified GSC/GA4 data only when using performance or journey evidence.

If these are incomplete, either run an authorized read-only collection step or narrow the output to a clearly labeled preliminary review. Search Console's Links report is corroborating evidence because it is sampled and may contain historical links; it is not a substitute for a current crawl edge list.

## Core workflow

1. **Define eligible targets.** Normalize URLs, resolve redirects, group canonical duplicates, and separate indexable HTML pages from non-indexable, utility, parameter, archive, and external URLs. Preserve excluded rows for traceability.
2. **Validate discovery.** Identify sitemap-only pages, true crawl orphans, non-crawlable links, broken targets, redirecting links, links to noncanonical URLs, and important pages reachable only through search/forms/scripts.
3. **Model architecture.** Calculate shortest crawl depth, unique inlinks, unique outlinks, link location, and repeated-template versus contextual links. Use a PageRank-style or vendor Link Score only as a relative diagnostic and name the tool/model.
4. **Compare structure with business priority.** Determine whether the pages intended to drive qualified traffic and enquiries receive appropriate prominence from navigation, hubs, the homepage, related services, and relevant editorial content.
5. **Assess meaning and journeys.** Review anchor clarity, source-target relevance, cluster connectivity, breadcrumbs, next-step links, conversion paths, and accessibility. Do not score anchors by exact-match percentage alone.
6. **Select opportunities.** For each proposed link, record source, exact target, proposed anchor or anchor range, placement/context, user benefit, SEO rationale, priority, effort, and conflicts or prerequisites. Avoid forced links and sitewide repetition.
7. **Report and validate.** Use the workspace finding template, attach implementation-ready tables, disclose limitations, and define a re-crawl plus analytics/search observation plan. Do not promise ranking gains or attribute later movement to links without controlling for other changes.

## Required audit dimensions

- crawlable `<a href>` implementation and rendered availability;
- target response, final URL, canonical consistency, indexability, and protocol/host consistency;
- orphan and sitemap-only discovery;
- shortest click/crawl depth from agreed entry points;
- unique inlinks, duplicate edges, self-links, and pages with no useful outlinks;
- template/navigation/footer/sidebar/breadcrumb versus main-content link placement;
- internal authority distribution relative to page priority;
- descriptive, concise, destination-accurate anchor text and linked-image alt text;
- hub-and-spoke and sibling relationships within topic/service clusters;
- blog/resource-to-service and service-to-supporting-resource journeys where genuinely useful;
- mobile/responsive navigation parity and keyboard/link-purpose accessibility;
- broken, redirected, chained, parameterized, noncanonical, nofollowed, or externally redirected internal targets;
- measurement limitations and pre/post validation.

## Output standard

Deliver the smallest set of artifacts that makes the recommendations auditable and implementable:

- executive summary and evidence/limitations statement;
- priority-page architecture scorecard;
- findings in the workspace's required template;
- source-to-target implementation register;
- orphan/broken/redirect/noncanonical remediation lists;
- topical-cluster coverage matrix;
- phased action plan and validation protocol.

Every recommendation must identify an exact source and target. When placement exists only as a conceptual opportunity, say so and require editorial review rather than inventing copy or implying the page was inspected.

## Handoffs

- Raw crawling and edge extraction: `../../../skills/website-crawl.md`
- HTTP, redirects, canonicalization, and indexability root causes: `../../../skills/technical-seo.md`
- Target-page quality and search intent: `../../../skills/on-page-seo.md` and `../../../skills/content-audit.md`
- Breadcrumb structured data: `../../../skills/schema-audit.md`
- WordPress/theme/page-builder control points: `../../../skills/wordpress-seo.md`
- Search and behavior evidence: `../../../skills/gsc-analysis.md` and `../../../skills/ga4-analysis.md`
- Conversion design beyond link-path diagnosis: `../../../skills/cro-audit.md`

Keep ownership clear, but include cross-discipline dependencies in the implementation register so the client receives one coherent plan.
