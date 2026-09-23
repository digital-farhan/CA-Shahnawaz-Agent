# Data contract and normalization

Use this reference when preparing or checking the datasets for an internal-linking audit.

## Workspace inputs

The current crawler writes:

- `data/crawl/internal-links-YYYY-MM-DD.csv`: `source,target,anchor,location,rel`
- `data/crawl/url-inventory-YYYY-MM-DD.csv`: URL-level status, final URL, redirects, indexability, canonical, inbound/contextual-inbound counts, click depth, and page type
- `data/crawl/crawl-summary-YYYY-MM-DD.json`: run scope, counts, anomalies, and sitemap coverage
- `data/crawl/sitemap-urls-YYYY-MM-DD.csv`: declared sitemap URLs

Join the edge list to the inventory twice: once on normalized `source`, once on normalized `target`. Do not infer target status, canonicality, or indexability from the edge row alone.

## Required edge fields

For a robust audit, retain or derive:

| Field | Meaning |
|---|---|
| `source` | Normalized page on which the link occurs |
| `target_raw` | Literal URL in the link before resolution |
| `target` | Normalized resolved internal target |
| `anchor` | Visible anchor text; linked-image alt when applicable |
| `location` | Main content, navigation, footer, sidebar, breadcrumb, or unknown |
| `rel` | `nofollow`, `ugc`, `sponsored`, or other values |
| `source_indexable` | Whether the source is eligible to contribute to the indexable architecture |
| `target_status` | Direct response status of the linked URL |
| `target_final_url` | Final URL after redirects |
| `target_canonical` | Declared preferred URL |
| `target_indexable` | Whether the destination is an eligible indexable target |

If `target_raw` is unavailable in the current export, disclose that normalization may conceal mixed protocol, parameter, or redirecting href problems and verify suspected cases against raw HTML or a crawl export that preserves the literal href.

## URL normalization

Keep raw values, then derive a comparison key. Apply only transformations justified by observed site behavior:

1. lowercase scheme and host;
2. remove the fragment for page-level graph analysis but retain it separately for jump-link checks;
3. normalize default ports;
4. resolve relative URLs against the source;
5. treat trailing slash, hostname variants, case, and selected query parameters according to actual redirects/canonicals, not by assumption;
6. do not collapse two live 200 URLs merely because their paths look similar;
7. resolve redirect chains but keep the original edge so remediation can target the source href;
8. group canonical variants for reporting only after confirming the canonical relationship.

## Eligible graph

Build at least two views:

- **Observed graph:** every discovered internal hyperlink, including broken, redirected, non-indexable, and duplicate edges.
- **Eligible architecture graph:** unique source-to-target edges between preferred, indexable HTML URLs that are followable and reachable through crawlable anchors.

Report which graph each metric uses. A sitemap URL with no edge in a complete observed graph is a sitemap-only orphan candidate. A URL discovered from an external source, GSC, analytics, or CMS export but absent from both crawl and sitemap is a broader orphan candidate. Never call a page a confirmed orphan without naming the discovery sources checked.

## Metric definitions

- **Unique inlinks:** number of distinct eligible source URLs linking to the target. Count repeated links from one source separately only in a raw-link diagnostic.
- **Contextual unique inlinks:** distinct eligible source URLs with at least one main-content link to the target.
- **Crawl depth:** shortest eligible link path from the declared start URL. State whether redirects count as a hop.
- **Template coverage:** distinct sources linking through repeated navigation/footer/sidebar modules.
- **Anchor diversity:** descriptive distribution for qualitative review; not an exact-match quota.
- **Cluster coverage:** eligible links observed versus editorially justified relationships in the approved topic map.
- **Relative authority:** named PageRank-style/Link Score model over the eligible graph. Use only for within-site comparison; do not present it as Google's PageRank.

## Completion checks

Before relying on totals, record crawl date, start URLs, rendering mode, authentication, robots behavior, crawl limits, excluded patterns, timeout/error counts, and whether mobile/responsive navigation was rendered. A crawl can reach every sitemap URL and still miss JavaScript or interaction-gated links.
