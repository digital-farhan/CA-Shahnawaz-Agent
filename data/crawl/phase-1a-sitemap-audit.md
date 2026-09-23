# Phase 1A — Sitemap Audit — cashahnawaz.com

Session date: 2026-08-27
Basis: `data/crawl/sitemap-discovery.md` (Phase 0), `data/crawl/_batch-a-tier1-tier2.md`, `data/crawl/_batch-b-archives-footer.md` (Phase 1A fresh fetches), `data/crawl/priority-urls.md`.

## 1. Sitemap structure and URL counts

Primary sitemap (matches `robots.txt`'s `Sitemap:` directive): `https://cashahnawaz.com/sitemap_index.xml`. Generator: **Rank Math SEO Plugin — CONFIRMED** (named explicitly in an XML comment inside the sitemap; corroborated by the `rankmath/v1` REST namespace).

| Child sitemap | URL count | Lastmod range |
|---|---|---|
| `page-sitemap.xml` | 42 | 2024-01-09 to 2026-08-21 |
| `post-sitemap.xml` | 58 | 2022-08-26 to 2026-07-22 |
| `category-sitemap.xml` | 8 | 2026-05-06 to 2026-07-22 |
| **Total sitemap-listed URLs** | **108** (107 unique paths — see collision below) | |

Plus **3 footer-linked URLs found on the live site but absent from all three child sitemaps** (see Section 6). **Total inventory: 111 rows.**

## 2. `sitemap.xml` / `sitemap_index.xml` / `wp-sitemap.xml` alias question

All three URLs returned 200 with valid XML listing the same 3 child sitemaps in the Rank Math naming pattern (not WordPress's native `wp-sitemap-posts-post-1.xml` pattern). This strongly suggests Rank Math has overridden WordPress's native `wp-sitemap.xml` output and that `sitemap.xml` is either an alias or a redirect to `sitemap_index.xml`.

**RAW HEADER / REDIRECT VERIFICATION NOT AVAILABLE** — WebFetch does not expose HTTP status codes or `Location` headers, so whether `sitemap.xml` and `wp-sitemap.xml` are (a) server-side 301/302 redirects to `sitemap_index.xml`, (b) separately generated files with identical content, or (c) WebFetch silently normalizing the request cannot be determined this session. A `curl -I` or browser dev-tools check against all three URLs is needed to confirm the exact mechanism before this can be stated as fact in any implementation step.

## 3. Unexpected URL types in the sitemap

- No `/?attachment_id=`, `/wp-json/`, `/tag/`, `/author/`, or `/page/2/`-style URLs were found in any child sitemap. Their absence is a positive signal but **not confirmed absent sitewide** — only what was enumerated in the fetched sitemap XML was checked; this is not proof no such URL could exist unlisted.
- `category-sitemap.xml` contains 8 taxonomy archive URLs (`/income-tax/`, `/gst/`, `/mca/`, `/accounting-services-blog/`, `/trademark-registration/` [duplicate — see Section 4], `/others/`, `/donation/`, `/gst-case-law/`). These are `wp-system`/taxonomy-archive type URLs, not content pages, and are correctly segregated into their own child sitemap rather than mixed into `page-sitemap.xml` or `post-sitemap.xml`.
- The site does **not** use WordPress's default `/category/x/` path structure — taxonomy archives sit at flat top-level slugs (e.g., `/gst/`, `/income-tax/`) instead. This is **NOT DETERMINED** as either a deliberate custom permalink/rewrite setup or an indication these are actually Pages rather than true category archives — WordPress Admin access (Settings → Permalinks, or the Pages/Categories list) would be needed to confirm. Flagged as an open question, not scored as an issue, since a flat taxonomy slug is not inherently a problem.

## 4. Duplicate URL appearance: `/trademark-registration/` — page/category collision

`https://cashahnawaz.com/trademark-registration/` appears as the **identical URL string** in both `page-sitemap.xml` (lastmod `2026-07-22T12:34:02+00:00`) and `category-sitemap.xml` (lastmod `2026-05-06T08:26:09+00:00`).

**Conclusion: LIKELY a WordPress permalink/slug collision between a Page (or Post) and a taxonomy term sharing the same slug, where Rank Math's sitemap generator has listed the same resolved URL from two different content-source tables (post/page table and taxonomy table) without deduplicating.**

**Confidence label: LIKELY** (not CONFIRMED — full confirmation requires WordPress Admin access to see both the Pages list and the Categories/Taxonomy list and check for a shared slug, which was not available this session).

Reasoning, weighing the candidate explanations:
- **Actual duplicate URLs (two separately reachable pages at the same path)** — ruled out as implausible; WordPress cannot serve two different pieces of content at one exact URL path simultaneously under normal rewrite rules. Not the likely explanation.
- **Taxonomy slug collision (a Page/Post and a category term share the slug `trademark-registration`)** — **best-evidenced explanation.** The one live fetch of this URL (`data/crawl/_batch-a-tier1-tier2.md`) returned a single coherent article — H1 "Trademark Registration Process," a visible `18/02/2022` publish date, and "0 Comments" directly under the H1 — which are WordPress single-post/page template markers, not a multi-item archive listing (no grid of teaser excerpts, no "Read More" links to distinct posts, no pagination controls). This is consistent with the live URL resolving to the Page/Post, while the category-sitemap.xml entry is Rank Math independently emitting the *taxonomy term's* canonical URL (which happens to share the same resolved path) into its own child sitemap — a scenario WordPress permalink structures allow when a category slug is not distinguished by a `/category/` prefix (see Section 3) and happens to match an existing page slug.
- **Sitemap generator behavior (Rank Math bug/quirk)** — plausible as a contributing factor (Rank Math not deduplicating across its post-type and taxonomy sitemap modules) but does not on its own explain *why* the same URL string exists in both source tables in the first place; more likely a downstream symptom of the slug collision above than an independent cause.
- **WordPress rewrite conflict** — related to, not distinct from, the slug-collision explanation above.
- **Incorrect categorization** — no evidence found that an editor manually mis-assigned a page to be listed as a category; the more parsimonious explanation is a genuine slug match.
- **Tool parsing limitation (WebFetch misreading the sitemap)** — ruled out: the `<loc>` and `<lastmod>` values were extracted cleanly and consistently from valid, well-formed XML in both child sitemaps; this is not an artifact of the fetch tool.

**What would be needed to move this from LIKELY to CONFIRMED:** WordPress Admin access to (a) open Pages/Posts and search for a page or post with the exact slug `trademark-registration`, and (b) open the taxonomy/category list and check whether a category term also uses slug `trademark-registration`. If both exist, the collision is CONFIRMED and the fix is a straightforward slug rename on one of the two objects (with a 301 redirect from the old URL if the renamed object was ever indexed under its old slug).

**SEO impact if left unresolved:** Google may treat the two sitemap entries as pointing to the same URL with conflicting `lastmod` signals, is very unlikely to index "two pages" (since only one is reachable), but the ambiguity muddies which content type Google associates with this URL and could affect how it's categorized/understood, and complicates any future attempt to build out a genuine multi-item Trademark category archive (since the slug is already claimed by the page). See the full CLAUDE.md-template finding in `reports/01-technical-seo.md` (TECH-001).

## 5. Missing priority-service URLs (cross-referenced from `priority-urls.md`)

The sitemap does not contain a dedicated URL for several CLAUDE.md priority services. This is a discovery-stage observation carried forward from `data/crawl/priority-urls.md`; scoring/prioritizing these gaps as findings is content-audit.md's job in a later phase, not this technical/sitemap audit's:

- **Private Limited Company Registration** — only a Public Limited Company page exists.
- **LLP Registration (formation)** — only "LLP Annual Filing" (a compliance page) exists.
- **Partnership Registration** — only a Tax Guides blog article ("Partnership Firm Registration in Maharashtra") exists; no dedicated service page.
- **Proprietorship Registration** — no page found.
- **Tax Consultancy / Income Tax Compliance / GST Consultancy / GST Compliance / Internal Audit** — no separately dedicated pages found (may be implicitly covered by broader service pages).
- **Company Compliance / Annual Compliance (Private Limited / OPC)** — captured as contact-form dropdown options but no dedicated landing pages found.

## 6. URLs in inappropriate sitemap types / non-sitemap footer URLs

Three footer-linked URLs do not appear in any child sitemap and were live-checked this session (`data/crawl/_batch-b-archives-footer.md`, Part 2):

| Footer URL (as linked, using `http://`) | Nearest sitemap equivalent | Live-check result |
|---|---|---|
| `http://cashahnawaz.com/project-business/trademark-registration/` | `/trademark-registration/` | Loads live content (H1 "Trademark Registration Process"); does not resemble a 404 |
| `http://cashahnawaz.com/income-tax-return-filling-in-mumbai/` (typo: "filling") | `/income-tax-return-filing-in-mumbai/` | Loads live content matching the correctly-spelled page's title/H1; does not resemble a 404 |
| `http://cashahnawaz.com/online-tds-return-filing/` | `/tds-return-filing-services/` | Loads live content matching that page's structure; does not resemble a 404 |

**RAW HEADER / REDIRECT VERIFICATION NOT AVAILABLE for all 3** — WebFetch only reliably surfaces a notice for cross-host redirects, never confirmed one on any of these three fetches, but this is inconclusive rather than proof of "no redirect": a same-host 301/302 to the correct sitemap URL would not necessarily be flagged by the tool. It cannot be determined this session whether these are (a) separately live, indexable duplicate-content URLs still reachable from the footer, or (b) silently redirecting to their correct sitemap counterparts. Either way, the footer continues to link to an outdated URL structure (including a literal typo in one case and an `http://`, not `https://`, scheme in all three), which is itself worth fixing regardless of the underlying redirect mechanism. Full finding: `reports/01-technical-seo.md` (TECH-002).

## 7. Whether categories should be included in the sitemap — assessment

Of the 8 category/taxonomy archive URLs in `category-sitemap.xml`, live-checks (`data/crawl/_batch-b-archives-footer.md`, Part 1) found:

| Archive | Items observed | Assessment |
|---|---|---|
| `/income-tax/` | 9 posts, reverse-chronological | Genuine multi-post archive — reasonable sitemap inclusion |
| `/gst/` | 10 posts, ~4.5 years of content, pagination | Genuine multi-post archive — reasonable sitemap inclusion |
| `/mca/` | **1 post only**, "End of content" | **THIN — questionable sitemap inclusion** |
| `/accounting-services-blog/` | 8 posts | Genuine multi-post archive — reasonable sitemap inclusion (though newest post is Feb 2023 despite a much later lastmod on a related sitemap entry — unresolved, noted for content-audit) |
| `/trademark-registration/` (category entry) | Not separately fetched — see Section 4 collision | Cannot assess independently of the collision question |
| `/others/` | 10 posts (catch-all, low topical coherence but not thin) | Reasonable sitemap inclusion by volume |
| `/donation/` | **1 post only**, no pagination | **THIN — questionable sitemap inclusion** |
| `/gst-case-law/` | 10 posts, confirmed pagination beyond page 1 | Genuine multi-post archive — reasonable sitemap inclusion |

**Assessment: category/taxonomy archives should generally remain in the sitemap on this site** — 5 of the 7 independently-checked archives are genuine, substantive multi-post listings that provide real crawl paths to content. However, **`/mca/` and `/donation/` are single-item archives that read as thin/low-value indexed pages** and are candidates for either (a) being left out of the sitemap via Rank Math's per-taxonomy sitemap toggle, (b) merging their one article into the `/others/` catch-all category, or (c) building out more MCA/donation-related content given "MCA" maps to the Registration & Compliance priority-service group in CLAUDE.md. Full finding: `reports/01-technical-seo.md` (TECH-003).

## 8. Lastmod date patterns

- `page-sitemap.xml` lastmods range from 2024-01-09 to 2026-08-21 — broadly plausible and recent, consistent with an actively maintained site.
- `post-sitemap.xml` lastmods range from 2022-08-26 (oldest in the entire inventory: `/how-to-file-gst-registration-process-benefits-penalty/`) to 2026-07-22 — a wide spread, expected for a 58-article blog archive built up over ~4 years.
- Several older-lastmod blog posts carry content that is explicitly time-bound and describes a now-closed compliance window (`/gst-amnesty-scheme-2023/`, lastmod 2026-05-06, describing a scheme window that closed 30 June 2023; `/big-relief-for-taxpayers-whose-gst-number-got-canceled.../`, lastmod 2023-04-08, consistent with its own stated closed window) — see `reports/01-technical-seo.md` (TECH-004) for the scored finding on this content-freshness signal. Note the `/gst-amnesty-scheme-2023/` case specifically: its lastmod (2026-05-06) is roughly 3 years newer than the deadline its own body content describes as closed, suggesting the lastmod reflects a template/technical touch rather than a substantive content refresh — this mismatch pattern is itself worth noting for content-audit.md.
- `category-sitemap.xml` lastmods (2026-05-06 to 2026-07-22) are all recent regardless of how thin or substantive the underlying archive is — lastmod recency does not correlate with archive substance on this site (both the 1-item `/donation/` archive and the 10-item `/gst-case-law/` archive carry comparably recent lastmods).

## 9. Summary for `reports/01-technical-seo.md`

This file is the evidence base for: TECH-001 (trademark-registration collision, LIKELY), TECH-002 (3 footer-linked non-sitemap URLs, LIKELY), TECH-003 (thin `/mca/` and `/donation/` archives, CONFIRMED), TECH-004 (stale compliance-deadline content signal, CONFIRMED), and the sitemap.xml/wp-sitemap.xml alias mechanism (Data Limitations — RAW HEADER / REDIRECT VERIFICATION NOT AVAILABLE).
