# Industry basis and claim discipline

Reviewed 2026-08-28. Use these sources to support methodology; refresh them when current guidance is material to a client claim.

## Authoritative principles

1. [Google: Link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
   - Google generally extracts links from `<a>` elements with `href` values.
   - Anchor text should be descriptive, reasonably concise, and relevant to both source and destination.
   - Important pages should receive a link from at least one other site page.
   - Linked images use their `alt` attribute as anchor text.

2. [Google: Help Google understand site structure](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
   - Google analyzes relationships among pages through links and can infer relative importance from link paths and the number of links to a page.
   - Pages available only through an internal search box may not be found through normal crawling.
   - The documentation is ecommerce-focused, so apply its general architecture principles to other sites without importing ecommerce-specific requirements.

3. [Google Search Console: Links report](https://support.google.com/webmasters/answer/9049606)
   - The report groups by canonical URL, combines duplicates, may include historical links, limits tables, and is not comprehensive.
   - Use it to corroborate Google's observed linking, not as a complete current edge inventory.

4. [Google: Canonical URL guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
   - Consistently linking to the preferred canonical URL helps communicate the preferred version.

5. [Google: Breadcrumb structured data](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)
   - Breadcrumbs indicate a page's position in site hierarchy and can help users explore upward through that hierarchy.
   - Audit visible breadcrumb links here; route structured-data validity to schema review.

6. [W3C WCAG 2.2: Link Purpose in Context](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html)
   - Users should be able to determine link purpose from the text alone or its programmatically determinable context.
   - Use this as the accessibility basis for avoiding ambiguous link labels.

7. [WordPress: Site Editor navigation](https://wordpress.org/documentation/article/site-editor-navigation/) and [Appearance Menus](https://wordpress.org/documentation/article/appearance-menus-screen/)
   - Block themes and classic/hybrid themes can expose different menu-control paths.
   - Verify the site's active control system before writing click-by-click instructions.

## Useful vendor diagnostics

- [Screaming Frog: Internal linking audit](https://www.screamingfrog.co.uk/seo-spider/tutorials/internal-linking-audit-with-the-seo-spider/) describes crawl depth, unique inlinks, and a commonly used 1-3 depth heuristic for important pages.
- [Screaming Frog: Link Score](https://www.screamingfrog.co.uk/seo-spider/tutorials/link-score/) documents its proprietary PageRank-style 0-100 relative metric and eligibility rules.
- [Screaming Frog: Link position](https://www.screamingfrog.co.uk/seo-spider/tutorials/how-to-analyse-link-position/) explains its semantic-markup-based link-location classification and limitations.

Vendor metrics and thresholds are diagnostics, not Google requirements. Name the vendor and version when used.

## Claims to avoid

Do not claim any of the following without site-specific evidence and appropriately qualified language:

- an exact number of internal links is optimal;
- every important page must be within three clicks as a Google rule;
- contextual links pass a quantified amount more PageRank than navigation/footer links;
- repeating an exact-match anchor at a particular percentage improves rankings;
- changing internal links alone caused a ranking, traffic, or conversion change;
- a proprietary Link Score equals Google's internal PageRank;
- `nofollow` is a reliable method for sculpting internal PageRank;
- breadcrumbs, hubs, or silos guarantee indexing or ranking.

Prefer language such as “supports discovery,” “clarifies relationships,” “raises prominence within the observed architecture,” and “creates a more direct user path.”
