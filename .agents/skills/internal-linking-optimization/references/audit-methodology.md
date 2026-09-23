# Audit methodology

Use this reference for a full audit or an opportunity plan.

## 1. Frame the decision

Confirm the site scope, business priorities, conversion goals, priority page set, content types, markets/languages, and whether the request is diagnostic, implementation planning, or validation. A page's ideal prominence depends on its role; do not rank every URL by inlinks and assume the most-linked should be a money page.

## 2. Establish evidence readiness

Check the crawl's date, completion, rendering mode, scope, exclusions, error rate, and sitemap coverage. Join edge and URL inventories using `data-contract.md`. Spot-check raw/rendered HTML on the homepage, a hub, a priority service page, an article, and any page-builder or mobile-navigation pattern.

Label each conclusion:

- **Observed:** directly present in fetched/crawl/rendered data.
- **Derived:** calculated from observed data; state the formula/input graph.
- **Corroborated:** supported by a second source such as GSC Links or manual rendering.
- **Judgment:** expert prioritization or editorial fit.
- **Proposed:** a future change, never current state.

## 3. Build the architecture views

Create:

1. an observed graph for remediation;
2. an eligible indexable graph for architecture metrics;
3. a contextual-only graph;
4. optional template-only views for header/nav/footer/sidebar/breadcrumb;
5. business-priority overlays for service groups, supporting resources, trust pages, and conversion pages.

Calculate shortest depth, unique inlinks/outlinks, contextual inlinks, repeated-source edges, self-links, components/disconnected sets, and relative centrality when useful. Compare pages within similar roles, not across unlike types without context.

## 4. Diagnose in this order

### A. Link integrity and canonical consistency

Find links that are non-crawlable, broken, redirected, chained, externally redirected, mixed-protocol/host, parameterized without purpose, nofollowed internally, or aimed at a noncanonical/non-indexable destination. Update recommendations at the source href; do not merely say the final URL resolves.

### B. Discovery gaps

Reconcile crawl, sitemap, CMS exports when available, GSC-known pages, and analytics landing pages. Distinguish:

- true orphan candidates;
- sitemap-only pages;
- pages reachable only from non-indexable sources;
- pages reachable only through JavaScript interaction/search/forms;
- intentionally isolated utility/legal/campaign pages.

Severity depends on page purpose and indexation intent, not zero inlinks alone.

### C. Depth and prominence

Compare important pages' shortest paths, unique inlinks, contextual inlinks, and relative authority with their business/search role. Depth over three can be a useful review trigger on many sites, but investigate the actual path, site size, navigation model, and page role before making it a finding.

### D. Link placement

Separate template links from contextual links. Sitewide counts can make a target look prominent while offering no topic-specific path. Inspect whether navigation, hub, breadcrumb, sibling, and body links each serve a real user need. Do not assume one placement type has a fixed SEO value.

### E. Anchor and accessible purpose

Review whether anchor text is understandable, concise, and accurate in its local context. Flag empty anchors, linked images with missing/empty alt text when the image is the only label, misleading anchors, long sentence anchors, ambiguous repeated labels such as “read more,” and identical labels leading to different purposes without context.

Use natural variation driven by sentence meaning. Do not prescribe exact-match quotas. Brand, partial-service, question, entity, and action-oriented anchors can all be appropriate when they accurately describe the destination.

### F. Topic and service relationships

Create an approved cluster map before judging “missing” links. For each cluster, review:

- hub to child coverage;
- child back to hub where useful;
- sibling links only where a user would reasonably need the adjacent service/topic;
- informational content to commercial service paths;
- service pages to supporting guides, evidence, FAQs, or compliance resources;
- cross-cluster links where the real-world journey overlaps.

Avoid rigid silos that block useful cross-topic navigation. Avoid forced reciprocal linking among every page in a cluster.

### G. Business and performance opportunities

When live access is verified, use GSC to prioritize pages with demonstrated impressions, page-two visibility, query mismatch, or cannibalization signals; use GA4 to understand landing-to-next-page journeys and conversions. Record date ranges, filters, property IDs, and limitations. These sources affect prioritization but do not prove that an added link will improve rankings or conversions.

## 5. Prioritize findings

Use the workspace severity definitions, tempered by evidence confidence and business role.

| Condition | Typical treatment |
|---|---|
| Priority indexable page has no crawlable route in a complete multi-source check | HIGH; CRITICAL only when active blocking or measurable harm meets project rules |
| Internal sitewide/navigation link resolves to 404 or unrelated external site | HIGH when it affects priority journeys; otherwise MEDIUM |
| Priority target is linked mainly through repeated templates with little relevant contextual support | MEDIUM or OPPORTUNITY depending on performance and role |
| Important page is materially deeper than comparable peers | MEDIUM after verifying actual route and intent |
| Ambiguous/misleading anchors impair navigation or destination understanding | MEDIUM; LOW for isolated polish |
| Editorially strong source-to-target opportunity | OPPORTUNITY unless it remedies an evidenced gap |

Never assign severity from a numeric cutoff alone.

## 6. Build the opportunity register

Every proposed edge needs:

| Field | Requirement |
|---|---|
| Source URL | Existing inspected page |
| Target URL | Preferred canonical 200 URL |
| Current context | Quoted short excerpt or section/heading reference |
| Proposed anchor | Draft text or bounded natural-language option |
| Placement | Exact paragraph/module or editorial instruction |
| User benefit | Why a visitor would follow it |
| SEO rationale | Discovery, hierarchy, relevance, or authority distribution |
| Priority/effort | Relative implementation order and complexity |
| Dependency | Content rewrite, target fix, legal/CA review, menu ownership, etc. |
| Validation | What should change in crawl/render/analytics evidence |

Reject candidates where the source does not genuinely discuss the target, the target is weak/non-indexable/duplicative, the anchor would be forced, or the recommendation mainly inflates link counts.

## 7. Manual implementation guidance

Confirm the actual WordPress control layer before naming menus: classic theme, block theme Site Editor, Elementor template, synced pattern, widget, theme options, or plugin/mega-menu. Give the user reversible steps, cache considerations, page-by-page QA, and a pre-publish preview. Never edit the live system from this audit workspace.

## 8. Validation

After the user implements approved changes:

1. capture the implementation date and exact approved edge set;
2. re-crawl with the same configuration;
3. confirm href, anchor/accessible name, location, 200 final target, canonical/indexability, followability, and mobile rendering;
4. compare only relevant depth/inlink/centrality metrics and note unrelated site changes;
5. check for new broken links, accidental duplicates, navigation regressions, or template-wide side effects;
6. observe GSC/GA4 over a suitable period without promising a fixed window or attributing causality from correlation alone.

## QA checklist

- [ ] Crawl scope and limitations disclosed
- [ ] Raw and normalized URLs preserved
- [ ] Observed and eligible graph definitions stated
- [ ] Orphans reconciled across available discovery sources
- [ ] Template and contextual links separated
- [ ] Important pages compared with business role peers
- [ ] Anchors reviewed in actual source context
- [ ] Every proposed target is canonical, indexable, and useful
- [ ] Exact source-to-target register supplied
- [ ] Findings follow the workspace template
- [ ] Manual implementation and validation steps included
- [ ] No ranking guarantees, invented metrics, or live changes
