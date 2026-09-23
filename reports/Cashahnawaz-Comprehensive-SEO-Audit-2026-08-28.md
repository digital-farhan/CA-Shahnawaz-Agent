# Comprehensive SEO, Analytics & Growth Audit

## Shahnawaz and Associates — cashahnawaz.com

**Audit date:** 28 August 2026  
**Data through:** 25 August 2026 for GSC and GA4  
**Prepared from:** live crawl, Google Search Console, GA4, published Google Tag Manager container, browser-rendered mobile/desktop tests, public local citations and competitor research  
**Status:** Confidential · diagnosis and implementation roadmap · no live-site changes made

---

## Executive decision summary

Organic visibility is growing quickly, but the site currently has three material constraints on turning that growth into qualified enquiries:

1. **A priority registration URL sends prospects and SEO signals to another CA firm.** `/private-limited-company-registration/` returns a permanent redirect to `anamca.com`, and Google confirms the external URL as canonical. Four other internal URLs also redirect there.
2. **Conversion reporting is not trustworthy.** The published GTM WhatsApp trigger fires on every link click, not only WhatsApp clicks. GA4 consequently reports 587 `whatsapp_click` events and 585 key events that cannot be treated as genuine WhatsApp enquiries. Successful form submissions are not tracked.
3. **The pages with the strongest search opportunity need trust, snippet and conversion work.** Accounting, NRI taxation, ITR filing, GST filing and 12A/80G pages already receive meaningful impressions, but their click-through rates and commercial journeys are weak relative to their visibility.

The site is not suffering a sitewide indexing failure. The homepage and sampled priority pages are indexed, the sitemap is valid, HTTPS/non-WWW enforcement works, and organic search is already the main acquisition channel. The best growth path is therefore to fix lead leakage and measurement first, then improve pages that Google is already showing—before publishing a large volume of new articles.

### Verified baseline

| Metric | Current verified value | Interpretation |
|---|---:|---|
| GSC clicks, last 90 days | **3,744** | A meaningful organic base already exists |
| GSC impressions, last 90 days | **402,561** | Google is testing the site across a broad query set |
| GSC CTR | **0.93%** | Large snippet and intent-alignment opportunity |
| GSC weighted average position | **7.84** | Many results sit on page one, but not yet in the strongest click positions |
| Last 30 days vs first 30 days — clicks | **+83.2%** | Strong positive momentum |
| Last 30 days vs first 30 days — impressions | **+49.7%** | Visibility is expanding rapidly |
| Last 30 days vs first 30 days — CTR | **+22.4% relative** | Snippet performance improved, but remains low overall |
| GA4 organic sessions | **2,533** | Covers only 19 July–25 August because the property was created on 19 July |
| Organic share of all GA4 sessions | **81.7%** | SEO is the dominant acquisition channel |
| Organic engagement rate | **56.8%** | Useful content engagement, with a mobile gap |
| Organic sessions from India | **2,463 / 2,533** | Audience is geographically relevant at country level |
| Organic sessions attributed to Mumbai | **420 / 2,533** | Only 16.6% is explicitly Mumbai; much traffic is national informational traffic |
| Published GTM container | **Version 5 · 4 tags · 2 triggers** | Connected and live, but conversion logic is incomplete |

**Historical limitation:** GSC data begins on 2 May 2026 and GA4 begins on 19 July 2026. A year-over-year conclusion is not possible yet.

---

## Audit status by workstream

| Workstream | Status | What it means |
|---|---|---|
| Search visibility | **Growing** | Strong recent gains and several page-one opportunities |
| Crawlability & core indexation | **Mostly healthy** | Priority pages inspected are indexed; no robots/sitemap failure |
| Lead ownership | **Critical issue** | Company-registration traffic is redirected to another firm |
| Analytics & conversion tracking | **Unreliable** | WhatsApp is overcounted; form success is not measured |
| Commercial page coverage | **Needs expansion** | Company, LLP formation, ROC/company compliance, GST consultancy/compliance and internal audit gaps |
| On-page CTR | **High opportunity** | Multiple high-impression pages have CTR below 1% |
| Trust / E-E-A-T | **Weak on core pages** | Practitioner identity and firm credentials are not clearly presented |
| Mobile performance | **Needs improvement** | Measured mobile LCP exceeded 2.5s on all nine sampled pages |
| Local SEO | **Blocked by address conflict** | Website/citations/ICAI sources show different unit/floor variants |
| Structured data | **Mixed** | Good Organization/LocalBusiness base, but two invalid FAQ JSON-LD blocks and inconsistent service markup |

---

## What is connected

| Platform | Connection result | Scope verified |
|---|---|---|
| Google Search Console | **Connected** | URL-prefix property `https://cashahnawaz.com/`; service account is a restricted user; performance, sitemaps and URL Inspection work |
| Google Analytics 4 | **Connected** | Property 546098812, stream `G-1SFXZJSYYY`, created 19 July 2026; reporting API works |
| Google Tag Manager | **Connected** | Account “Shahnawaz And Associates”; container `GTM-N2LHGRCX`; published version 5 inspected |
| Google Business Profile | **Not connected to this audit** | GBP categories, services, primary address, reviews, posts and performance remain unavailable |
| WordPress Admin / hosting panel | **Not logged into** | Plugin fingerprints were verified publicly; versions and admin-only settings were not confirmed |

No further action is needed to connect GSC, GA4 or GTM. To close the remaining access gaps, provide WordPress Administrator access and Google Business Profile Manager access when implementation begins. A Domain-property GSC permission would also be preferable to the current restricted URL-prefix access, but it is not required for the recommendations in this report.

---

## Priority action plan

### P0 — protect leads and restore trustworthy data (days 1–7)

| Action | Owner | Effort | Success check |
|---|---|---:|---|
| Restore an owned Private Limited Company Registration page and remove the redirect to `anamca.com` | WordPress/hosting | Medium | Cashahnawaz URL returns 200, self-canonical, own phone/form/GTM, included in sitemap |
| Audit and remove the four other unintended external redirects | WordPress/hosting | Low–Medium | No internal URL redirects to an unrelated business |
| Restrict the GTM WhatsApp trigger to actual WhatsApp URLs | Analytics | Low | GTM Preview fires only on `wa.me` / approved WhatsApp links |
| Track successful Elementor form submissions | Analytics + WordPress | Medium | A real successful test creates one GA4 lead event; failed/abandoned forms create none |
| Preserve the current phone-click trigger and validate it | Analytics | Low | One phone click produces one `phone_click` event |
| Annotate GA4 reporting from 19 July until the GTM fix as contaminated for WhatsApp/key-event analysis | Analytics | Low | Dashboards clearly exclude or label the invalid period |

### P1 — improve pages Google already shows (weeks 2–4)

1. Rework homepage positioning around “Chartered Accountant / Tax Consultant in Mumbai,” with verified practitioner credentials, service proof and a specific enquiry CTA.
2. Upgrade Accounting, NRI, ITR Mumbai, GST Return Filing and 12A/80G pages using the page plan below.
3. Add a visible, verified CA bio and firm identity to the homepage, About page and money-page author/reviewer blocks.
4. Confirm the authoritative office unit/floor and standardize website, schema, GBP and major citations.
5. Reduce mobile hero and page-builder load cost, starting with the homepage and highest-opportunity money pages.

### P2 — build topical and commercial depth (weeks 5–12)

1. Build owned pages only for services the firm genuinely provides: LLP Registration, ROC/Company Annual Compliance, GST Compliance/Consultancy, and Internal Audit.
2. Repair invalid schema, indexable AJAX variants and confirmed internal 404 links.
3. Build contextual internal links from high-traffic guides into matching service pages.
4. Introduce a regulated-content review workflow with a named CA reviewer and visible “reviewed on” date.
5. Improve Google Business Profile and citation consistency after the address is confirmed.

---

## Page-by-page implementation register

Use this register as the working queue. Complete **P0 before P1**, take a backup before changing templates or redirects, and test changes on staging where possible. Do not change a URL slug merely to insert a keyword. Any tax, legal, filing-year, threshold or deadline change must be approved by a practising CA before publication.

The companion spreadsheet, `Page-Implementation-Register-2026-08-28.csv`, contains the same work in a filterable format for assigning owners and recording completion.

### P0 — immediate ownership, lead and trust repairs

| URL / scope | Work to implement | Owner | Completion test |
|---|---|---|---|
| `/private-limited-company-registration/` | Remove the cross-domain redirect and publish an owned Cashahnawaz service page. Add a self-canonical, firm phone/WhatsApp/form, verified process, documents, realistic timelines, FAQs, `Service` schema and sitemap entry. Do not copy another firm's text. | Owner + CA + WordPress + SEO | Returns 200 on `cashahnawaz.com`; self-canonical; Cashahnawaz branding/tracking only; submitted in sitemap and inspected in GSC |
| `/annual-compliances-for-private-limited-company/` | Confirm this is a service offered. If yes, replace the Anam redirect with an owned ROC/annual-compliance page; if no, remove Cashahnawaz internal links and redirect only to the closest genuinely equivalent owned service. | Owner + CA + WordPress | No cross-domain redirect; destination matches the same user intent and business |
| `/difference-between-accounting-and-bookkeeping/` | Confirm content ownership. Restore and improve it as an original supporting guide, or redirect it to `/accounting-services/` only if that page satisfies the query. Remove every internal link if the URL is retired. | Owner + Content + SEO | No Anam destination; final URL is owned, relevant and one hop |
| `/gst-council-constitution-functions-and-decision-making/` | Confirm content ownership. Restore an original CA-reviewed explainer or consolidate into a genuinely relevant owned GST guide. Do not redirect informational visitors to an unrelated sales page. | Owner + CA + Content | No Anam destination; facts reviewed; relevant owned final page |
| `/instant-tips-on-income-tax-deductions-that-you-can-start-figuring-out-today/` | Confirm content ownership. Restore an original current guide or consolidate into a relevant income-tax guide after professional review. | Owner + CA + Content | No Anam destination; all tax claims dated/reviewed; owned canonical |
| **All pages / GTM container** | Add a filter to the WhatsApp click trigger so it fires only for approved `wa.me`, `api.whatsapp.com` or WhatsApp application links. Preserve and test the `tel:` trigger. | Analytics | GTM Preview: ordinary navigation produces no WhatsApp event; one real WhatsApp click produces exactly one event |
| **All Elementor forms** | Fire `generate_lead` or `form_submit_success` only after Elementor confirms a successful AJAX submission. Include `form_name`, `service` and `page_location`; mark only the success event as a GA4 key event. | Analytics + WordPress | One successful controlled form submission creates one GA4 event; errors, starts and button clicks do not |
| `/about-us/` | Replace the rendered `0`, `0%`, `0`, `0+` counters with verified values or remove the counters. Add the verified practitioner name, membership/FRN, experience, services and professional-review role. | Owner + CA + WordPress | No zero counters; credentials match owner-approved records; mobile and desktop render correctly |
| `/contact-us/`, homepage, footer and sitewide schema | Confirm the authoritative office address, then use exactly one NAP format everywhere. Do not make this change until the owner resolves C-18 vs B38 vs B-110. | Owner + WordPress + Local SEO | Visible NAP, schema, GBP and priority citations match exactly |

### P1 — pages already earning visibility

| URL | Work to implement | Do not do | Validation |
|---|---|---|---|
| `/` | Rewrite the first screen around “Chartered Accountant and Tax Consultant in Mumbai”; show a visible service-specific CTA, verified CA identity, clear phone/WhatsApp choices and links to the six priority service groups. Simplify the Elementor hero and optimize its LCP asset. | Do not remove the current local relevance or change the homepage URL | Re-test mobile LCP; inspect title/snippet; test every CTA; monitor `ca in mumbai` and `tax consultant mumbai` |
| `/when-can-i-expect-my-itr-refund/` | Add one descriptive H1; update the refund-status/process steps; rewrite title/meta for the actual refund query; add a current reviewed date and contextual CTA/link to `/income-tax-return-filing-in-mumbai/`. | Do not turn the guide into a thin sales page or change its slug | One H1; CA approval; self-canonical; CTR monitored against the 53,708-impression baseline |
| `/accounting-services/` | Rewrite title/meta, H1 and first screen around CA-supervised accounting, bookkeeping, MIS and reporting in Mumbai. Correct copy quality, explain deliverables/frequency/software/handoff, add proof, one main form and contextual links from accounting guides. | Do not create separate thin pages for every keyword variant | Valid `Service` schema; one form; CTA tracked; monitor `accounting services in mumbai` |
| `/itr-filing-for-nri-guide-for-non-resident-taxation/` | Separate guide content from engagement details; add named CA reviewer, remote-client workflow, document checklist, NRI-specific situations handled, response expectations and a page-specific enquiry CTA. | Do not claim international capability or outcomes that cannot be evidenced | CA review; one lead path; valid schema; monitor NRI query CTR and qualified enquiries |
| `/income-tax-return-filing-in-mumbai/` | Professionally correct the AY 2020–21 FAQ and review every year, threshold and penalty. Reduce repetitive exact-match copy, strengthen current-year/local proof, improve title/meta, fix FAQ JSON-LD and track the form success. | Do not update regulated figures without CA sign-off | Schema validates; stale AY reference removed/reframed; test lead; monitor page-one queries |
| `/12a-or-12aa-or-80g-registration-new-scheme/` | Review all transitional 2021–22 dates; broaden the page around current 12AB/80G registration intent; add eligibility, documents, process, renewal/revalidation distinction, named reviewer, CTA and links from NGO/ITR-7 content. | Do not present expired dates as current | CA approval; current review date; valid schema; improved internal links |
| `/gst-return-filing/` | Expand return types, reconciliation, records handoff, notice/error support, service cadence and boundaries. Replace generic CTA, reduce duplicate forms and repair malformed FAQ JSON-LD. | Do not create competing pages for `gst filing services` and `gst return filing services` | Schema validates; one main form; tracked CTA; monitor both query clusters |
| `/gst-registration-online/` | Make the page the canonical owner for GST registration. Add eligibility, documents, process, post-registration obligations, local proof and page-specific CTA. Resolve overlap with the old GST guide below. | Do not publish another near-duplicate GST registration sales page | Self-canonical; unique intent; relevant internal links; monitor local queries |
| `/llp-annual-filing/` | Update FY 2021–22 framing after CA review; clarify Forms 8/11 and the current annual-compliance process; add deadlines only with a review date; link to the future LLP Registration page without merging the two intents. | Do not combine LLP formation and annual filing into one page | CA-approved current copy; clearer title/H1; contextual links from compliance content |
| `/section-8-company-registration/` | Review regulatory accuracy; improve title/meta, process, documents, eligibility and after-registration compliance; add links from 12A/80G, ITR-7 and Section 8 vs Trust content. | Do not imply Section 8, trust and society are identical structures | CA approval; at least four relevant contextual links; lead event tested |
| `/audit-services/` | Split the visible service coverage into statutory audit, tax audit and internal audit sections with scope, ideal client, process and deliverables. If internal audit is active and substantial, build the dedicated page listed under P2. Stabilize the layout causing CLS. | Do not publish unverifiable client counts or audit outcomes | Mobile CLS at or below 0.1 in repeat lab tests; service scope approved |
| `/startup-registration-india/` | Clarify what “startup registration” means, distinguish incorporation from DPIIT recognition, explain deliverables/eligibility/documents, add owned-company/LLP pathways and a specific founder CTA. | Do not conflate Startup India recognition with company incorporation | CA/legal review; internal links to the correct formation pages; lead tracked |
| `/public-limited-company/` | Review current process and compliance claims, strengthen qualification criteria/documents/timeline boundaries, add trust proof and connect it to the future ROC compliance hub. | Do not use private-company keywords for this page | Current reviewed date; distinct title/H1; valid Service schema |
| `/tds-return-filing-services/` | Review current forms, due dates, penalties and correction process; add service cadence, documents, reconciliation and notice-support scope; track a page-specific CTA. | Do not leave undated compliance tables | CA approval and visible review date; successful test lead |
| `/trademark-registration/` | Clarify this is a supported service, improve process/search/opposition boundaries and proof, and correct footer links that still point through legacy paths. | Do not imply guaranteed registration | One canonical URL; no legacy-path hops; claims reviewed |
| `/contact-us/` | Reduce the mobile hero height, put phone/WhatsApp/form above the fold, show the confirmed address and hours, retain one concise form and add privacy/data-use text beside submit. | Do not publish an address until the owner confirms it | Mobile render checked; all contact actions work; one successful lead event |

### P1 — high-traffic industry and supporting pages

Apply a shared pattern to every industry page: retain the industry-specific tax intent, add a named CA reviewer and visible review date, remove generic filler, explain the exact records/risks/forms relevant to that industry, link to the main ITR service, and use one contextual CTA. The URL-specific exceptions are below.

| URL | Additional implementation required |
|---|---|
| `/itr-filing-for-healthcare-industry/` | Protect its strong visibility; review profession/business-income distinctions and healthcare-specific records before changing the snippet |
| `/itr-filing-for-crypto-trading-in-india/` | Professionally verify the current tax/TDS/loss-treatment content and date every regulated claim |
| `/itr-filing-for-food-and-beverage-industry/` | Keep as the only Food & Beverage URL; replace links pointing to obsolete food/beverage slugs |
| `/itr-filing-for-content-creators-influencers/` | Verify platform income, foreign receipts, GST and expense examples; improve the service handoff |
| `/itr-filing-for-beauty-wellness-industry/` | Repair obsolete Food & Beverage and Real Estate internal links |
| `/itr-filing-for-wholesale-retail-trade-industry/` | Replace the broken `/company-registration/` link with the restored private-company page or another contextually correct destination |
| `/itr-filing-for-event-management-and-entertainment-professionals/` | Verify TDS/GST/expense examples and add event-specific record requirements |
| `/itr-filing-for-e-commerce-industry/` | Replace the obsolete Food & Beverage URL and review marketplace/GST/TCS claims |
| `/itr-filing-for-real-estate-construction/` | Make this the only owned Real Estate/Construction URL and replace links to the obsolete `-industry` variant |

### P1/P2 — regulated and time-sensitive content refresh queue

| URL | Required decision and work | Priority |
|---|---|---:|
| `/mca-extension-due-date-of-annual-filling/` | Rewrite as an explicitly historical FY 2020–21 update or consolidate into a current ROC compliance resource; correct its title/meta and remove false freshness signals | P1 |
| `/charitable-trusts-alert-its-time-reapply-for-tax-exemption-before-30th-sep/` | The September 2025 deadline has passed. Update with CA-verified present treatment or label/archive it clearly and link to the current 12AB/80G service | P1 |
| `/gst-new-update-due-dates-for-october-2021/` | Mark as a historical October 2021 calendar or remove from current discovery surfaces; never change old dates to new dates without rebuilding the content | P1 |
| `/due-date-calendar-for-the-month-of-november-2022/` | Archive as November 2022, noindex if it has no continuing search value, and remove from current navigation/widgets | P2 |
| `/gst-amnesty-scheme-2023/` | Add an expired-scheme notice and historical context; review whether a newer scheme warrants a separate current article | P2 |
| `/memorandum-explaining-the-provisions-in-the-finance-bill-2023/` | Preserve as historical analysis; repair the broken `/msme-ssi-registration/` link and add publication/review context | P2 |
| `/the-best-accounting-software-for-small-businesses-in-2023/` | Refresh the comparison with current products and a transparent review date, or label it as a 2023 archive | P2 |
| `/june-2026-important-due-dates/` | Keep the original month/year immutable; after expiry add a historical notice and link to the current due-date hub | Recurring |
| `/due-date/july/` and `/due-date/august/` | Use a controlled annual update process with reviewed dates, accurate year in title/H1 and an archive policy; never silently reuse outdated monthly URLs | Recurring |
| `/tds-chart-for-fy-2026-27/` | Schedule a CA review before each financial year; retain the FY-specific URL/content as an archive when the next chart is published | Recurring |

### P2 — technical URL and internal-link repairs

| URL / source | Implementation | Validation |
|---|---|---|
| `/gst-registration-services-india-a-guide-to-gst/` | Decide whether unique informational value remains. If not, 301 to `/gst-registration-online/` and remove from internal links. If retained, use an HTTPS self-canonical, differentiate guide intent and include it in the sitemap. | One canonical owner; no HTTP canonical; GSC inspection agrees |
| `/?jkit-ajax-request=jkit_elements` and pagination variant | Prevent crawl/index generation using the responsible Elementor/JKit setting or server rule; return a non-indexable response and ensure no internal discovery. Do not block in robots.txt before Google can see removal signals. | Live response is not indexable; no canonical ambiguity; validate in GSC |
| `/mca/` and `/donation/` | These are thin one-item archives. Either build useful maintained hubs or noindex/remove them from the sitemap and link directly to the article. | Index directive and sitemap treatment match the chosen purpose |
| Useful paginated archives | Give each useful pagination page a self-canonical and crawlable next-page path. Noindex or consolidate archives that have no standalone value. | Crawl deeper posts; inspect canonical on page 2+ |
| `/itr-filing-for-beauty-wellness-industry/` | Replace obsolete Food & Beverage and Real Estate/Construction targets with the live canonical URLs. | Crawl reports no 404 targets |
| `/itr-filing-for-e-commerce-industry/` | Replace the obsolete Food & Beverage target with `/itr-filing-for-food-and-beverage-industry/`. | Link returns 200 directly |
| `/itr-filing-for-wholesale-retail-trade-industry/` | Replace `/company-registration/` after the owned company-registration destination is restored. | Link returns 200 directly |
| `/memorandum-explaining-the-provisions-in-the-finance-bill-2023/` | Replace/remove `/msme-ssi-registration/` depending on whether a genuine MSME service/resource exists. | No broken link; anchor matches destination |
| `/trademark-classes/` | Replace/remove `/online-trust-registration/`; it is not contextually suitable unless the surrounding copy genuinely discusses trust registration. | No broken or misleading link |
| `/bombay-hc-gst-bank-recovery-notice/` and `/madras-high-court-gst-notice-service-judgment/` | Restore the missing cited PDF only if it is the correct licensed/public document; otherwise replace it with the authoritative source or remove the link. | Asset/source returns 200 and matches the citation |
| **Service-page schema template** | Use stable Organization + Breadcrumbs sitewide and accurate `Service` markup on genuine service pages. Repair the two invalid FAQ blocks; use Article/BlogPosting only on editorial pages. | Rich Results Test/Schema Validator passes and visible content matches markup |
| **Elementor service template** | Keep one main embedded form plus the global popup, reduce hero height/DOM, load only the actual LCP asset early, defer non-critical scripts and replace generic “GET IT NOW” text. | Two-run mobile lab retest plus form/CTA test on every template family |

### P2 — new pages to create only for services actually offered

| Suggested URL | Page purpose | Minimum implementation |
|---|---|---|
| `/llp-registration/` | LLP formation—not annual filing | Eligibility, partners/designated partners, documents, process, deliverables, realistic timeline boundaries, FAQs, Service schema and links to `/llp-annual-filing/` |
| `/roc-annual-compliance/` | Company/OPC/Section 8 annual compliance hub | Entity-specific sections, AOC/MGT scope, records checklist, engagement cadence, CA-reviewed current treatment and links from company-registration pages |
| `/gst-compliance-services/` | Ongoing GST compliance/consultancy, only if distinct from return filing | Reconciliation, notices, registrations/amendments, advisory boundaries and clear differentiation from `/gst-return-filing/` |
| `/internal-audit-services/` | Dedicated internal-audit service, only if actively delivered | Scope, risk areas, process, deliverables, sectors served, confidentiality and team credentials |
| `/tax-consultancy-services/` | Ongoing tax advisory/compliance hub | Audience, recurring scope, advisory workflow, boundaries, proof and links to ITR/TDS pages; avoid duplicating the homepage |

### Implementation sequence and release checks

1. **Backup and baseline:** export WordPress/database and the current GTM version; save current title/meta, schema and GSC metrics for each page being changed.
2. **Fix P0:** external redirects, analytics, form success tracking, zero counters and confirmed NAP.
3. **Release P1 in small batches:** update two to four pages at a time. Preserve URLs and avoid simultaneous sitewide title changes.
4. **QA every batch:** mobile/desktop visual test, status/canonical/indexability, title/H1, schema, links, form/phone/WhatsApp events and sitemap inclusion.
5. **Request indexing selectively:** use GSC URL Inspection for materially improved P0/P1 pages; do not submit every unchanged URL.
6. **Measure after 28 days:** compare clicks, impressions, CTR, position and valid leads against the saved baseline. Keep changes that improve qualified outcomes; diagnose pages that decline before rewriting again.

Pages not named in this register have no verified urgent defect. Keep them published, monitor performance, and include them in the quarterly accuracy/link review rather than rewriting them without evidence.

---

## Search performance and audience analysis

### Growth trend

The latest 30 days produced **1,513 clicks from 147,877 impressions**, compared with **826 clicks from 98,800 impressions** in the first 30 days of the 90-day window. Weighted average position improved by **0.78 positions**. This is healthy momentum, not a reason to rebuild the site or change every URL.

The opportunity is concentrated in moving already-visible pages higher and earning more clicks at the same rank. The ten highest-click pages account for approximately **45.1%** of page-level clicks, so focused upgrades can materially influence the total.

### Audience fit

- Organic search supplies **81.7%** of all GA4 sessions.
- **97.2%** of organic sessions are from India.
- Mumbai is the largest city at **420 sessions**, but represents only **16.6%** of organic sessions. Bengaluru, Delhi, Chennai, Kolkata, Pune and Hyderabad are also significant.
- Desktop accounts for **69.4%** of organic GA4 sessions, while mobile accounts for **30.7%**.
- Mobile organic engagement is **47.4%**, materially below desktop at **61.1%**. Mobile layout and speed therefore need attention even though desktop currently leads traffic.
- Traffic is heavily driven by ITR industry guides, due-date resources, tax guides and case-law content. This is valuable reach, but it needs clear service pathways to become qualified enquiries.

### Priority page opportunities

| Page / role | Clicks | Impressions | CTR | Avg. position | Recommended focus |
|---|---:|---:|---:|---:|---|
| ITR refund guide | 113 | 53,708 | 0.21% | 6.8 | Add a real H1, align snippet to refund-status intent, update for current process, link to ITR service |
| Homepage | 432 | 25,813 | 1.67% | 10.5 | Improve local CA/tax-consultant positioning, visible hero message and practitioner proof |
| NRI taxation guide/service | 77 | 10,647 | 0.72% | 8.7 | Strengthen service intent, named reviewer, remote-client process, CTA and NRI proof |
| Accounting services | 32 | 10,377 | 0.31% | 19.1 | Reframe around CA-supervised bookkeeping/MIS, fix copy quality, improve local snippet and proof |
| 12A/80G registration | 68 | 11,102 | 0.61% | 9.8 | Professional regulatory review, broaden H1, improve service CTA and trust |
| ITR filing Mumbai | 91 | 8,619 | 1.06% | 6.4 | Protect page-one position; improve snippet, proof, valid schema and lead tracking |
| GST return filing | 15 | 2,413 | 0.62% | 10.0 | Expand deliverables/reconciliation/process, add document handoff, fix schema and CTA |
| LLP annual filing | 4 | 614 | 0.65% | 8.9 | Refresh old-year content and distinguish compliance from LLP formation |
| Section 8 registration | 0 | 594 | 0% | 9.3 | Add relevant internal links, precise snippet, current legal review and clear process |
| GST registration | 0 | 295 | 0% | 12.4 | Consolidate overlapping GST pages; improve local intent, proof and documents/process |
| Audit services | 0 | 25 | 0% | 6.6 | Build authority and dedicated internal-audit depth; visibility is currently too small for CTR diagnosis |

### Query-to-page map

| Query cluster | Current landing page | Evidence | Action |
|---|---|---|---|
| `ca in mumbai` | Homepage | 749 impressions, 14 clicks, avg. position 3.0 | Preserve relevance; improve snippet and visible firm credentials |
| `tax consultant mumbai` / `tax consultant in mumbai` | Homepage | 532 combined impressions; positions 6–7 range | Add a clearer tax-consultant proposition and service proof |
| `accounting services` | Accounting | 904 impressions, 5 clicks, position 7.6 | Rewrite title/meta and first screen around outcomes and CA supervision |
| `accounting services in mumbai` | Accounting | 247 impressions, 0 clicks, position 5.3 | High-priority CTR test; local proof and specific deliverables |
| `itr filing in mumbai` | ITR Mumbai | 249 impressions, 7 clicks, position 3.0 | Protect intent alignment; strengthen pricing/proof and conversion tracking |
| `income tax return filing mumbai` | ITR Mumbai | 233 impressions, 0 clicks, position 4.7 | Improve snippet differentiation and current-year clarity |
| `gst filing services` | GST Return Filing | 380 impressions, 3 clicks, position 13.7 | Move toward page one through content depth and links |
| `gst return filing services` | GST Return Filing | 270 impressions, 0 clicks, position 13.9 | Same page; no new competing page needed |
| `12a registration online` | 12A/80G page | 306 impressions, 3 clicks, position 7.9 | Refresh, broaden scope and improve CTA |
| `online tax consultant` | Homepage | 367 impressions, 1 click, position 10.6 | Explain remote/online process and response expectations |

**Content direction:** do not create separate pages for minor keyword variants that already map cleanly to one page. Improve the existing owner page and its supporting links.

---

## Measurement and conversion audit

### Confirmed published GTM setup

| Published tag | Trigger | Audit result |
|---|---|---|
| GA4 Integration (`G-1SFXZJSYYY`) | Initialization / all pages | Connected and live |
| Website Menu Phone Click | Link click where Click URL starts with `tel:` | Logic is appropriately restricted; validate in Preview and GA4 DebugView |
| GA4 — WhatsApp Click | Link click with **no filter** | **Defective: fires on every link click** |
| “Hotjar” tag | All pages | Loads a Contentsquare UX script; name and vendor should be normalized in documentation |

### GA4 evidence

- `whatsapp_click`: **587 events**, **204 users**, **585 key events**.
- `phone_click`: **7 events**, **6 users**, **5 key events**.
- `form_start`: **12 events**, but there is **no successful form-submission/lead event**.
- Organic reports show **360 key events**, but these are largely contaminated by the WhatsApp trigger.
- `(not set)` accounts for **230 organic landing sessions** with only **3.9% engagement**, which should be investigated after event/session tagging is corrected.

### Required measurement design

Use one clear lead taxonomy:

| User action | GA4 event | Key event? | Required parameters |
|---|---|---|---|
| Successful enquiry form | `generate_lead` or `form_submit_success` | Yes | `form_name`, `service`, `page_location` |
| WhatsApp click | `whatsapp_click` | Yes | `click_url`, `page_location`, optional `service` |
| Phone click | `phone_click` | Yes | `phone_number`, `page_location` |
| Email click | `email_click` | Optional | `email_address`, `page_location` |

For Elementor forms, fire the lead event only after the AJAX success response or on a unique success/thank-you state—not on button click or form start. Use GTM Preview, GA4 DebugView and one real controlled submission per form family before publishing.

---

## Technical SEO findings

### What is healthy

- `robots.txt` is accessible and points to the sitemap index.
- The sitemap index and its post/page/category sitemaps return 200 with no GSC warnings or errors; 108 web URLs are submitted.
- HTTP redirects to HTTPS in one hop; `www` redirects to non-`www` in one hop.
- The homepage and all sampled owned priority pages are mobile-crawled, allowed and indexed according to GSC URL Inspection.
- Sitemap priority pages return 200 and are indexable.
- Legacy URL redirects sampled earlier resolve in one hop.

### Concentrated technical issues

1. **Cross-domain permanent redirects:** five cashahnawaz.com URLs redirect to `anamca.com`, including the priority Private Limited Company Registration page.
2. **Indexable AJAX crawl variants:** `/?jkit-ajax-request=jkit_elements` and a pagination variant return indexable 200 pages without canonicals. GSC confirms the homepage parameter variant was crawled and is currently not indexed.
3. **Duplicate GST page outside the sitemap:** `/gst-registration-services-india-a-guide-to-gst/` is indexed, but its declared canonical uses HTTP. Google selects HTTPS. It overlaps the main GST Registration page and a registration guide.
4. **Broken internal links:** confirmed source pages link to obsolete company-registration, ITR-industry, MSME, trust-registration and PDF URLs.
5. **Pagination canonical inconsistency:** several paginated archive URLs canonicalize to page one. This can suppress discovery of deeper archive content; use self-canonicals for useful paginated pages or noindex/archive consolidation where appropriate.
6. **No HSTS header observed:** this is a security-hardening opportunity, not a primary ranking issue. Confirm compatibility before enabling at the CDN/hosting layer.

The GSC sitemap API returns an `indexed: 0` field, but this conflicts with URL Inspection and live search performance. It is therefore treated as an unpopulated API field, not as evidence of an indexing collapse.

---

## Content, on-page and E-E-A-T audit

### Strong assets to protect

- Industry-specific ITR pages are generating substantial visibility and traffic.
- The NRI guide, ITR Mumbai page and current due-date resources have strong content depth.
- Google already associates the homepage with valuable local queries such as “CA in Mumbai.”
- The current homepage, About, Contact and on-site schema use one consistent phone and C-18/Ground Floor address family.
- Current Organization/LocalBusiness markup exists on the homepage and Contact page.

### Trust and identity gap

The rendered About page shows:

- `COMPLETED PROJECTS 0`
- `SATISFACTION RATE 0%`
- `ONLINE CONSULTING 0`
- `BUSINESS REGISTRATIONS 0+`

After an eight-second rendered check, these values remained zero. Neither the homepage nor the About page visibly included “CA Shahnawaz,” “Shahnawaz Shaikh,” FRN, membership number or ICAI terms in body text.

The public ICAI firm list provides a strong trust asset—**Shahnawaz And Associates, FRN 151767W; Shahnawaz Shaikh, membership 194241**—but also displays a B38 office-unit variant. Confirm that these details are current, then add a professionally written practitioner profile, firm-registration detail and reviewed-by block. Do not publish credentials until the firm verifies them.

### Regulated-content governance

Several pages contain passed years/deadlines without strong historical framing, including:

- MCA annual-filing relief content for FY 2020–21: **5,939 impressions / 62 clicks**.
- Charitable-trust reapplication deadline of September 2025: **6,174 impressions / 36 clicks**.
- ITR Mumbai FAQ reference to AY 2020–21 on a current service page: **8,619 impressions / 91 clicks**.
- LLP content labelled FY 2021–22: **614 impressions / 4 clicks**.
- 12A/12AA/80G transitional dates from 2021–22: **11,102 impressions / 68 clicks**.

These are not replaced with new figures in this audit. A practising CA should verify the governing law, date, threshold and correct treatment. Then each page should be updated, clearly archived as historical, consolidated, or redirected according to continuing search intent.

### Commercial content gaps

Create or expand only where the service is genuinely offered:

| Gap | Recommended owned page / treatment | Priority |
|---|---|---|
| Private Limited Company Registration | Restore the existing Cashahnawaz URL as an owned page | Immediate |
| LLP Registration | Create formation page; keep LLP Annual Filing separate | High |
| ROC / Company Annual Compliance | Create one strong hub with AOC-4/MGT-7 and entity-specific sections | High |
| GST Compliance / Consultancy | Expand GST Return Filing or create one ongoing-compliance page if scope is distinct | High |
| Internal Audit | Create a dedicated page if this is an active service; current coverage is too thin | High |
| Tax Consultancy / Income Tax Compliance | Prefer one ongoing-advisory hub over several near-duplicate pages | Medium |
| Partnership / Proprietorship Registration | Build only if commercially important and genuinely serviced | Medium |

---

## Structured data audit

### Confirmed strengths

- Homepage: valid `Organization`, `LocalBusiness`, `WebSite`, `WebPage` and location objects.
- Contact page: valid `ContactPage`, `Organization`, `LocalBusiness` and address/location objects.
- Breadcrumb markup is widespread.

### Confirmed defects

- GST Return Filing FAQ JSON-LD is invalid because of an unescaped control character.
- ITR Mumbai FAQ JSON-LD is invalid for the same class of error.
- Service pages use inconsistent schema families: some have only Breadcrumbs, some are marked as Article, and GST Return Filing also uses Product/Brand/Organization blocks.
- FAQ markup is not a meaningful rich-result strategy for this business. Google states that FAQ rich results are generally limited to well-known authoritative government and health sites. Keep FAQ markup only when it matches visible content and is maintained correctly; do not treat it as a traffic feature. See [Google’s FAQ rich-result change](https://developers.google.com/search/blog/2023/08/howto-faq-changes).

### Recommended schema model

1. One stable sitewide `Organization` / appropriate `LocalBusiness` entity with verified name, URL, logo, telephone and authoritative address.
2. `WebSite` on the homepage and `BreadcrumbList` on eligible internal pages.
3. `Service` markup for owned commercial service pages where the visible page supports it.
4. `Article` / `BlogPosting` only for genuine editorial content, with accurate author, reviewer, publication and modification dates.
5. Valid FAQ markup only where every question and answer is visible on the page.
6. Validate in Google Rich Results Test and Schema Markup Validator, then inspect the live URL in GSC.

Google recommends accurate Organization/LocalBusiness name, address, telephone and URL properties; fewer accurate properties are better than extensive inaccurate markup. See [Google’s Organization guidance](https://developers.google.com/search/docs/appearance/structured-data/organization) and [LocalBusiness guidance](https://developers.google.com/search/docs/appearance/structured-data/local-business).

---

## Internal linking and architecture

All owned priority pages are reachable from the homepage at crawl depth one. The issue is contextual relevance, not basic reachability.

| Target page | Contextual inbound links found | Recommended new sources |
|---|---:|---|
| Section 8 Company Registration | **1** | 12A/80G page, Section 8 vs Trust guide, ITR-7 NGO guide, Form 10AB articles |
| LLP Annual Filing | **2** | July/August compliance pages already link; add Startup, future LLP Registration and ROC/annual-compliance hub |
| Audit Services | 41 | Add deeper anchors for internal/statutory/tax audit rather than repeated generic “Audit Services” |
| Accounting Services | 51 | Existing accounting cluster is useful; prioritize high-traffic MIS/finalisation/accounting guides |
| GST Return Filing | 51 | Add contextual conversion blocks from GST case-law and due-date articles where genuinely relevant |
| ITR Mumbai | 102 | Strong support; refine anchors and avoid making every industry page look templated |

### Confirmed broken source → target repairs

| Source | Broken target | Correct treatment |
|---|---|---|
| ITR for Wholesale/Retail | `/company-registration/` | Point to the restored owned company-registration page |
| Beauty/Wellness and E-commerce ITR pages | two obsolete Food & Beverage URLs | Point to `/itr-filing-for-food-and-beverage-industry/` |
| Beauty/Wellness ITR page | obsolete Real Estate/Construction URL | Point to `/itr-filing-for-real-estate-construction/` |
| Finance Bill article | `/msme-ssi-registration/` | Point to a real Udyam/MSME page if offered, otherwise remove/rewrite the link |
| Trademark Classes article | `/online-trust-registration/` | Point to the appropriate trust/NGO service only if intent matches |
| GST/case-law content | missing uploaded PDF | Restore the asset or remove/update the citation |

---

## Mobile performance and CRO

### Lab methodology

Two mobile runs were completed per page in headless Chromium with 4× CPU slowdown and approximately 1.6 Mbps / 150 ms network conditions. These are **LAB** results, not CrUX field results. INP was not inferred because it requires interaction/real-user data. Google’s “Good” thresholds are LCP ≤2.5s, INP ≤200ms and CLS ≤0.1; see [Google Search Central’s Core Web Vitals guidance](https://developers.google.com/search/docs/appearance/core-web-vitals).

| Page | Mobile LCP median | CLS median | Long-task time | Assessment |
|---|---:|---:|---:|---|
| Homepage | **6.45s** | 0.00 | 1.28s | Poor LCP |
| Private company registration external destination | **5.66s** | 0.06 | 5.54s | Poor; also wrong business destination |
| GST Return Filing | **3.92s** | 0.00 | 1.18s | Needs improvement |
| Contact | **3.74s** | 0.00 | 1.29s | Needs improvement |
| NRI guide | **3.66s** | 0.01 | 2.20s | Needs improvement |
| Accounting | **3.33s** | 0.00 | 2.05s | Needs improvement |
| GST Registration | **3.25s** | 0.00 | 2.82s | Needs improvement |
| ITR Mumbai | **2.87s** | 0.00 | 1.26s | Needs improvement |
| Audit | **2.64s** | **0.18** | 1.94s | LCP near threshold; poor CLS |

The LCP element is usually an Elementor hero section or background overlay. The likely optimization path is to replace CSS-background LCP artwork with a correctly sized responsive image where appropriate, preload only the real above-the-fold asset, simplify the hero DOM, reduce unused Elementor add-on assets, and defer non-critical scripts. LiteSpeed/Hostinger caching is present, so tune the existing system before adding another overlapping optimization plugin.

### Rendered conversion issues

- Mobile homepage headline contrast is weak and the text is partially obscured by the fixed CTA; desktop capture showed a large empty hero area before the main CTA/message fully appeared.
- “GET IT NOW” is generic and does not describe the next step.
- The WhatsApp button is visible above the fold, but phone links are generally below the fold.
- Contact mobile hero consumes most of the first screen before “Get in Touch With Us.”
- Accounting, GST and ITR templates render duplicate forms—two to four instances in a page/browser state.
- The common form asks for email, mobile, city and service, with several required fields. This may create unnecessary friction for high-intent mobile users.
- There is no reliable form-success analytics event, so no conversion-rate conclusion can be made.

### CRO redesign principles

1. Change generic CTA copy to page-specific actions: “Speak to a CA about GST filing,” “Get an accounting quote,” or “Check my ITR requirements.”
2. Keep one primary form per page plus the global popup; avoid repeating identical long forms.
3. Test a short first step: Name + Mobile/WhatsApp + Service, with email/city optional or collected next.
4. Add verified trust proof immediately beside the form: practising CA identity, response expectation, confidentiality statement and authentic service-relevant testimonial.
5. Add a visible privacy-policy link and short data-use statement near the submit button.
6. Prefill WhatsApp messages with the page/service context, then track only genuine WhatsApp URLs.

---

## Local SEO audit

### Current on-site NAP

**Shahnawaz and Associates**  
Ground Floor, Grace Plaza, C-18, S. V. Road, near Railway Station, Momin Nagar, Jogeshwari West, Mumbai 400102  
**Phone:** +91 98192 67015

This variant is internally consistent across the current homepage, About page, Contact page, footer and LocalBusiness markup.

### External inconsistency requiring owner confirmation

| Public source | Address variant |
|---|---|
| ICAI firm listing | **B38, Ground Floor**, Grace Plaza |
| Website / Magicpin / ServiceBazzar | **C-18, Ground Floor**, Grace Plaza |
| Justdial / Shuru | **B-110, First Floor**, Grace Plaza |

Do not choose a variant based only on frequency. Confirm the current legal and client-facing location, then update the website, schema, Google Business Profile and major citations. The [ICAI public firm list](https://lof.icai.org/LOFPDF/westprop.pdf) is also the source for the firm/practitioner identity that should be verified before publication.

### GBP work still required

Because Google Business Profile was not connected, the following are **DATA NOT AVAILABLE**: primary/secondary categories, GBP-side address, services, hours, review count/rating, photos, posts, Q&A and GBP performance. Once access is provided:

1. Confirm primary category and add only genuine service categories.
2. Use the authoritative NAP and service area.
3. Add each priority service with concise descriptions and correct landing pages.
4. Publish current office/team/service photos.
5. Create a compliant review-request process and respond to every review.
6. Add UTM-tagged website/appointment links so GBP leads can be measured separately.

---

## Competitor and search-landscape review

All four named competitors are live and relevant. The strongest recurring competitive advantage is not simply “more content”; it is **visible professional proof plus clearly packaged services**.

| Competitor | Visible strength relevant to Cashahnawaz |
|---|---|
| [N D Savla & Associates](https://www.ndsavla.com/) | Deep service structure, named operating history/scale, partner-led approach, multiple offices and explicit client segments |
| [JVB & Co.](https://www.jvb.co.in/) | Very deep audit, controls, risk, cyber and advisory taxonomy plus partner/location pages |
| [Asit Mehta & Associates](https://www.asitmehtaassociates.com/) | Long history, visible team/client scale, industries, audit, corporate tax and outsourced accounting |
| [Jain Anurag & Associates](https://jainanuragassociates.com/) | Broad registration, GST, income tax, NRI, audit, cross-border and accounting positioning |

Query-specific search results also surfaced pages from [SVT & Associates](https://svtandassociates.com/accounting-services/), [DMJC & Co.](https://www.dmjccharteredaccountants.com/services/gst-registrations-returns-and-audits) and [Taxpex](https://taxpex.com/services/gst-return-filing/mumbai). Their visible patterns include named CA credentials, concrete deliverables, process, response expectations, fee framing and prominent contact actions.

**What to adopt:** professional proof, precise deliverables, transparent process, service-specific FAQs and clear contact expectations.  
**What not to copy:** mass-produced locality pages, unverified ratings, unsupported “best” claims, or regulatory figures without professional review.

---

## 90-day SEO growth roadmap

### Days 1–7 — protect and measure

- Restore owned company-registration URL; remove external CA-firm redirects.
- Fix WhatsApp GTM trigger and implement successful form tracking.
- Confirm NAP, FRN/membership and approved practitioner bio.
- Repair invalid FAQ JSON-LD and the highest-value broken links.
- Noindex/control the AJAX parameter variants.
- Establish GA4 exploration by landing page, device, city and lead type.

### Days 8–30 — optimize existing demand

- Homepage: local CA/tax-consultant positioning, visible hero, credentials, service proof and specific CTA.
- Accounting: rewrite proposition, fix “TAXZONA” copy residue, specify monthly deliverables/software/process, improve local snippet.
- NRI: named CA reviewer, remote onboarding process, jurisdiction/service scope, relevant proof and conversion block.
- ITR Mumbai: current-year professional review, valid visible FAQ, snippet test, form success tracking.
- GST Return Filing: document checklist, reconciliation deliverables, filing cadence explanation, page-specific CTA, valid Service schema.
- 12A/80G: professional legal review, broaden H1, archive/update passed deadlines, add NGO-specific service proof.
- Improve homepage and money-page mobile LCP.

### Days 31–60 — close commercial gaps

- Publish owned LLP Registration and Company/ROC Compliance pages.
- Publish a dedicated Internal Audit page if actively offered.
- Decide whether GST Compliance/Consultancy is distinct enough for a page or should strengthen GST Return Filing.
- Add page-specific internal links from high-traffic articles and guides.
- Standardize money-page templates: practitioner proof, process, deliverables, documents, fee/quote rationale, FAQ, CTA.

### Days 61–90 — local authority and iteration

- Complete GBP categories/services/photos/review workflow and UTM tracking.
- Correct top citations after NAP confirmation.
- Review high-impression/low-CTR pages in GSC every two weeks.
- Compare mobile vs desktop engagement and valid lead rate.
- Refresh or archive outdated content based on a CA-approved content calendar.
- Re-run crawl, schema and mobile performance tests.

### Operational targets—not traffic guarantees

| Target | 90-day success condition |
|---|---|
| Lead ownership | Zero priority/internal URLs redirect to unrelated businesses |
| Measurement | One successful action = one valid GA4 key event; form, WhatsApp and phone separated |
| Technical hygiene | Zero invalid priority-page JSON-LD blocks; zero confirmed internal 404 links |
| Mobile experience | Priority-page lab LCP approaches or passes 2.5s; CLS below 0.1 |
| Search snippets | Improve CTR on selected pages by 15–25% relative while controlling for position |
| Commercial visibility | Accounting, GST filing, NRI, ITR and 12A/80G pages move upward for mapped queries |
| Local consistency | Website, GBP, schema and priority citations use one confirmed NAP |

---

## Detailed findings register

### F-01 — External redirect transfers a priority service and leads to another CA firm

**Severity:** CRITICAL · **Confidence:** Confirmed  
**Evidence:** `https://cashahnawaz.com/private-limited-company-registration/` returns a one-hop 301 to `https://anamca.com/services/registration/private-limited-company-registration/`. GSC reports “Page with redirect” and selects the external URL as Google/user canonical. The destination displays Anam Shaikh & Associates, another phone/email/WhatsApp, GTM `GTM-WV5SVHJK` and GA4 `G-WM2MWWHY3Y`. Four more Cashahnawaz URLs redirect to the same domain: annual private-company compliance, accounting-vs-bookkeeping, GST Council, and income-tax-deductions pages.  
**Affected URLs:** the five redirecting Cashahnawaz URLs and all internal links pointing to them.  
**SEO/Business impact:** Users, leads and canonical signals leave the site; Cashahnawaz has no owned private-company-registration landing page. Google treats a permanent redirect as a canonical-location signal; see [Google’s redirect documentation](https://developers.google.com/search/docs/crawling-indexing/301-redirects).  
**Likely root cause:** A legacy cross-domain migration/redirect rule or content transfer that was never removed. Ownership intent must be confirmed; this audit does not characterize it as malicious.  
**Recommended fix:** Restore an owned page on the existing URL if Cashahnawaz provides the service. Remove the external redirect, use Cashahnawaz branding/contact/tracking, self-canonicalize, add to sitemap and update internal links. If the service is intentionally referred out, remove it from the owned SEO strategy and clearly disclose the referral rather than using a silent permanent redirect.  
**Manual implementation:** Check Rank Math → Redirections, any redirect plugin, `.htaccess`, Hostinger redirect rules and CDN rules for the exact five source paths. Export/backup redirect settings first. Remove only confirmed unintended rules. Publish the owned page, clear LiteSpeed/hCDN cache, recrawl, and request indexing in GSC.  
**Validation:** Source returns 200 with no hop; page uses Cashahnawaz NAP/GTM/GA4; canonical equals source; URL Inspection shows indexable; controlled test lead reaches Cashahnawaz.

### F-02 — WhatsApp and form conversion measurement is invalid/incomplete

**Severity:** HIGH · **Confidence:** Confirmed  
**Evidence:** Published GTM version 5 has a “WhatsApp Click” link-click trigger with no filter. GA4 reports 587 WhatsApp events/585 key events, while no successful form event exists.  
**Affected assets:** GTM-N2LHGRCX, GA4 property 546098812, every link and form.  
**Impact:** The business cannot distinguish genuine leads from navigation clicks or calculate landing-page conversion rate.  
**Root cause:** Missing trigger condition and no Elementor success-state implementation.  
**Fix:** Restrict WhatsApp to approved `wa.me`/WhatsApp URL patterns; add a post-success Elementor lead event; validate phone tracking; mark the prior period as contaminated.  
**Manual implementation:** In a GTM workspace, duplicate/backup the trigger. Add a regex such as `^https?://(wa\.me|api\.whatsapp\.com)/` after confirming every live WhatsApp pattern. Configure an Elementor success event/dataLayer or unique success page and fire one GA4 lead tag. Preview every form family and link type before publishing.  
**Validation:** Navigation clicks do not fire WhatsApp; one WhatsApp click fires once; failed forms fire no lead; one successful form fires one lead in GTM Preview and GA4 DebugView.

### F-03 — High-impression pages underperform on CTR and commercial intent

**Severity:** HIGH · **Confidence:** Confirmed  
**Evidence:** ITR refund 53,708 impressions/0.21% CTR; Accounting 10,377/0.31%; NRI 10,647/0.72%; 12A/80G 11,102/0.61%; GST Return Filing 2,413/0.62%.  
**Impact:** Google visibility is not translating proportionally into qualified visits.  
**Root cause:** Mixed informational/service intent, generic or overlong snippets, weak visible authority and insufficient differentiation.  
**Fix:** Optimize one owner page per mapped query cluster; improve title/meta/intro, professional proof and service-specific conversion block.  
**Manual implementation:** Use the query map in this report. Change no URL unless consolidation is specifically approved. Record pre-change GSC metrics, publish one page group at a time, request recrawl and compare 28-day periods controlling for average position.  
**Validation:** Relative CTR improves without query cannibalization; valid lead rate becomes measurable.

### F-04 — Practitioner and firm trust proof is missing while About counters show zero

**Severity:** HIGH · **Confidence:** Confirmed rendered check  
**Evidence:** About counters remain at zero after rendering; homepage/About body contains no visible practitioner name, FRN, membership number or ICAI identity. Public ICAI data provides candidate details that require owner verification.  
**Impact:** Financial-service visitors cannot easily verify who is accountable for advice, weakening trust and differentiation.  
**Root cause:** Generic agency template and unconfigured counters; professional identity not integrated into the content model.  
**Fix:** Remove zero counters; publish a verified practitioner profile, firm identity, experience, review process and authentic proof.  
**Manual implementation:** In Elementor About template, remove or populate counters only with defensible numbers. Add a named bio with verified credentials, LinkedIn/professional profile, areas of practice and regulatory review role. Reuse a compact verified reviewer block on tax pages.  
**Validation:** Rendered home/About pages display accurate identity/proof; no zero or unverifiable claims remain.

### F-05 — Mobile LCP is above Google’s “Good” threshold on every sampled page

**Severity:** HIGH · **Confidence:** Confirmed lab, field data unavailable  
**Evidence:** Two-run mobile medians: homepage 6.45s; GST Return 3.92s; Contact 3.74s; NRI 3.66s; Accounting 3.33s; GST Registration 3.25s; ITR 2.87s; Audit 2.64s. Audit CLS is 0.18.  
**Impact:** Slower first impressions and lower mobile engagement; mobile engagement is already 13.7 percentage points below desktop.  
**Root cause:** Elementor background/overlay LCP elements, large DOMs, long main-thread tasks and redundant template assets.  
**Fix:** Optimize the existing LiteSpeed/Hostinger setup; simplify hero/templates; reduce unused add-ons; use responsive/preloaded LCP assets; reserve layout space.  
**Manual implementation:** Work on staging/backup. Use Chrome/Lighthouse element diagnostics plus this report’s LCP element. Change one template family at a time, purge cache, test twice on mobile and check visual regressions.  
**Validation:** Three comparable mobile lab runs; LCP ≤2.5s target, CLS <0.1; later confirm GSC/CrUX field data when available.

### F-06 — Current office address conflicts across public sources

**Severity:** HIGH · **Confidence:** Confirmed conflict; authoritative answer requires owner  
**Evidence:** Website C-18 Ground Floor; ICAI B38 Ground Floor; Justdial/Shuru B-110 First Floor.  
**Impact:** Potential clients and local-search systems receive conflicting location data.  
**Root cause:** Office move/unit-format changes not propagated consistently.  
**Fix:** Owner confirms one authoritative legal/client-facing address; standardize website, schema, GBP and priority citations.  
**Manual implementation:** Create a source-of-truth NAP sheet. Correct owned assets first, then GBP, ICAI if required, and major directories. Avoid creating a duplicate GBP.  
**Validation:** Search brand/address variants; all priority sources show the confirmed form and correct map pin.

### F-07 — Time-sensitive tax/compliance content lacks a controlled review lifecycle

**Severity:** HIGH · **Confidence:** Confirmed dates; replacement law requires CA review  
**Evidence:** Passed 2020–21, 2021–22 and 2025 references remain on pages still earning impressions/clicks.  
**Impact:** Trust, user decision quality and regulated-content accuracy risk.  
**Root cause:** Pages are updated irregularly without explicit archive/current status or named reviewer.  
**Fix:** Professional review; update, archive or consolidate; add “last reviewed,” reviewer and source notes.  
**Manual implementation:** Export the regulated-page list, assign a practising CA, preserve historical context where useful, avoid silently replacing figures, and maintain a quarterly calendar plus event-driven updates.  
**Validation:** Every priority regulated page has current/historical status, CA approval and accurate visible dates.

### F-08 — Commercial service coverage is incomplete

**Severity:** HIGH · **Confidence:** Confirmed crawl and competitor comparison  
**Evidence:** No owned Private Limited registration page; LLP formation absent; ROC/company compliance absent; Internal Audit thin; GST consultancy/compliance not distinctly served. Competitors package these areas more clearly.  
**Impact:** The site cannot rank or convert well for services without an owned intent-matched destination.  
**Root cause:** Content evolved around articles and a subset of services instead of a complete revenue-service architecture.  
**Fix:** Restore/build pages in priority order, only for genuine services, using one canonical owner per intent.  
**Manual implementation:** Confirm service, target client, process, documents, deliverables, pricing approach and responsible practitioner before drafting. Link from nav/hubs and relevant articles; add to sitemap.  
**Validation:** Each priority service has one owned indexable page, no overlap, appropriate internal links and GSC query coverage.

### F-09 — Elementor AJAX variants are crawlable and indexable

**Severity:** MEDIUM · **Confidence:** Confirmed crawl and GSC  
**Evidence:** `/?jkit-ajax-request=jkit_elements` returns 200, `index,follow`, no canonical; GSC: crawled—currently not indexed. A page-2 parameter variant also exists.  
**Impact:** Crawl waste and risk of low-quality parameter URLs entering the index.  
**Root cause:** JKit/Elementor endpoint produces full HTML without indexing controls.  
**Fix:** Prevent internal discovery where possible; return appropriate endpoint content/status; add `noindex`/canonical handling at plugin/server level without blocking Google before noindex is seen.  
**Manual implementation:** Identify the JKit component that creates links; update plugin/configuration first. If needed, add a narrowly scoped Rank Math/filter/server rule for the exact parameter. Test functionality before deployment.  
**Validation:** Endpoint functionality still works; URL is noindex or canonicalized appropriately; no new parameter variants appear in crawl/GSC.

### F-10 — An indexed duplicate GST page declares an HTTP canonical

**Severity:** MEDIUM · **Confidence:** Confirmed source and GSC  
**Evidence:** `/gst-registration-services-india-a-guide-to-gst/` is indexed; source canonical is the HTTP version; Google selects HTTPS; page is absent from sitemap and overlaps the main GST registration page/guide.  
**Impact:** Conflicting consolidation signals and diluted maintenance/linking.  
**Root cause:** Legacy manual canonical plus content duplication.  
**Fix:** Decide the owner page. Usually consolidate this low-performing legacy page to the main GST Registration page with a relevant 301; otherwise make it uniquely informational, HTTPS self-canonical and intentionally linked/sitemapped.  
**Manual implementation:** Compare content and backlinks first. If consolidating, map the closest section, add unique useful content to the destination, implement one-hop 301, remove internal links to source.  
**Validation:** GSC eventually shows the chosen canonical; only the owner page receives query impressions.

### F-11 — Confirmed internal links point to 404 URLs

**Severity:** MEDIUM · **Confidence:** Confirmed crawl  
**Evidence:** Company registration, two Food & Beverage variants, Real Estate/Construction variant, MSME registration, Trust registration and one PDF link return 404 from real source pages.  
**Impact:** Lost user journeys, wasted internal authority and reduced confidence.  
**Root cause:** Slug changes/content removals without source-link maintenance.  
**Fix:** Update source links to exact current destinations; use 301 only where a real equivalent exists.  
**Manual implementation:** Use the source→target table in this report; edit Elementor/article links, clear cache and crawl again. Do not redirect unrelated removed pages to the homepage.  
**Validation:** Zero internal 404 edges in a fresh crawl.

### F-12 — Priority-page structured data is invalid and inconsistent

**Severity:** MEDIUM · **Confidence:** Confirmed JSON parsing  
**Evidence:** Invalid FAQ JSON-LD on GST Return Filing and ITR Mumbai; inconsistent Article/Product/Breadcrumb-only models across services.  
**Impact:** Google cannot reliably parse the invalid blocks; entity/service meaning is inconsistent.  
**Root cause:** Manual custom-HTML schema plus plugin-generated schema without one source of truth.  
**Fix:** Choose Rank Math or one controlled schema source; use Organization/LocalBusiness + Service/Breadcrumb/Article as appropriate; remove invalid/redundant manual blocks.  
**Manual implementation:** Back up current schema. In Rank Math page schema settings and Elementor custom HTML widgets, identify which source outputs each block. Escape line breaks correctly or regenerate valid JSON-LD.  
**Validation:** JSON parser, Schema Validator, Rich Results Test and GSC URL Inspection pass with content matching the page.

### F-13 — Mobile conversion templates contain generic CTAs, excess hero space and duplicate forms

**Severity:** MEDIUM · **Confidence:** Confirmed browser render  
**Evidence:** Generic “GET IT NOW”; contact hero pushes the form below the first screen; 2–4 duplicate forms on sampled templates; common form requires email/mobile/city/service; phone generally below fold.  
**Impact:** Friction and unclear next step, especially on mobile.  
**Root cause:** Multiple Elementor template/popup/form instances and generic global components.  
**Fix:** One page-specific primary action, one main form, compact mobile hero, visible phone/WhatsApp and trust near the form.  
**Manual implementation:** Inventory global header/popup/footer templates and page forms; remove duplicates on staging; shorten and label form; add service-specific CTA copy and privacy link.  
**Validation:** Mobile browser test at 390px; no overlap, primary action visible, one successful submission tracked once.

### F-14 — Contextual internal linking is uneven for commercial pages

**Severity:** MEDIUM · **Confidence:** Confirmed link graph  
**Evidence:** Section 8 has one contextual inbound link; LLP Annual Filing has two, while ITR Mumbai has 102.  
**Impact:** Weaker discovery/relevance reinforcement for underperforming registration/compliance pages.  
**Root cause:** Template navigation is strong, but article-to-service links were added unevenly.  
**Fix:** Add source-relevant contextual links using descriptive, varied anchors and lifecycle relationships.  
**Manual implementation:** Start with 12A/80G → Section 8, ITR-7/Form 10AB → Section 8, Startup/future LLP Registration → LLP Annual Filing, and high-traffic GST guides → GST services.  
**Validation:** Link graph shows additional unique contextual sources; anchors accurately describe destination; no sitewide keyword-stuffed blocks.

---

## Data limitations and what is still needed

1. **Google Business Profile access:** required for a complete GBP/category/review/performance audit.
2. **Authoritative office address:** owner must confirm the correct unit/floor.
3. **Professional credentials:** confirm current FRN, membership, title and approved public wording.
4. **WordPress Administrator and hosting access:** required to confirm plugin versions, redirect rule source, staging/backup and exact implementation screens.
5. **GSC UI-only reports:** the API does not expose Manual Actions, Links or Core Web Vitals report groups. A full-permission user should manually confirm those screens.
6. **Field Core Web Vitals:** PageSpeed API quota was unavailable and the GSC API does not expose CWV groups; this report labels browser metrics as LAB.
7. **Regulatory facts:** all current legal/tax figures and replacement wording require practising-CA review.
8. **Competitor metrics:** competitor traffic, conversion rates and backlink counts were not available and were not estimated.

---

## Evidence index

- GSC exports and URL Inspection: `data/gsc/`
- GA4 exports: `data/ga4/`
- Published GTM inventory: `data/gtm/`
- Crawl, schema and link graph: `data/crawl/`
- Browser performance/CRO evidence: `data/performance/`
- Competitor verification/matrix: `data/competitors/`
- Consolidated analysis: `data/search-analytics-analysis-2026-08-28.json`

This audit is a prioritized diagnosis and implementation guide. It does not promise rankings or traffic. Results depend on implementation quality, professional accuracy review, competitor changes and Google’s systems. Measure progress using valid conversion events, GSC query/page data and a fresh technical validation after each implementation phase.
