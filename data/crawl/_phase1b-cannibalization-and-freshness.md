# Phase 1B — Section 7: Cannibalization, Content Overlap & Financial Content Freshness

**Session date:** 2026-08-27
**Site:** https://cashahnawaz.com/
**Method:** WebFetch (AI-summarized HTML→markdown extraction) against live URLs, plus reuse of prior-session fetch evidence in `_batch-a-tier1-tier2.md`, `_batch-c-tier3-sample.md`, and `phase-1a-url-verification.csv` where already sufficiently detailed. No live-site changes were made. **No GSC/GA4/ranking/query data was available this session** — every classification below is a content/topic-level judgment only. See the explicit note on every finding distinguishing this from actual SERP cannibalization.

---

# Part 1 — Cannibalization & Content Overlap Findings

## Overlap #1 — GST Registration: confirming scope beyond TECH-005 (Phase 1A)

- **Classification:** LIKELY CANNIBALIZATION RISK
- **Pages involved:** `https://cashahnawaz.com/gst-registration-online/` (Tier 1, lastmod 2026-06-18) vs. `https://cashahnawaz.com/how-to-file-gst-registration-process-benefits-penalty/` (Tier 3 blog, lastmod 2022-10-31)
- **Evidence:** This extends Phase 1A's TECH-005 (filed as POSSIBLE/LOW) with a fresh fetch of both pages' full structure. `/gst-registration-online/` H2s include: "Who is Liable for GST Registration Online?", "Documents Required for GST Registration Online", "What happens if you do not list for Online GST Registration Online?", with figures "Annual turnover threshold: Rs 40 lakhs for normal category states (Rs 20 lakhs for special category states)" and "Registration penalty: Rs 10,000 or the sum of tax unpaid, whichever is higher." The blog article's own quoted figures (from `_batch-c-tier3-sample.md`): "yearly gross sales revenue of more than Rs. 40 lakhs" (goods threshold), "Rs.20 lakh (for regular category states) or Rs.10 lakh (for special category states)" for services, plus a late-fee/penalty breakdown. Both pages cover the same four buckets — threshold, documents, process, penalty — for the same core query intent ("how to register for GST"), and the blog article offers no clearly distinct angle (it is not framed as a general explainer, comparison, or FAQ-style piece distinct from the service page's own content).
- **Content/Topic overlap vs. Search performance cannibalization:** This is a content/topic-level overlap observation only. No GSC or query-level data was available this session to confirm the two URLs are actually splitting rankings/clicks in the SERPs — that would require `ACTUAL SEARCH PERFORMANCE CANNIBALIZATION` evidence, which is `DATA NOT AVAILABLE` this session.
- **Notes:** No other live page targets "GST Registration" as its core topic. The `/gst/` category archive is a general GST-topic aggregator (10 posts spanning ~4.5 years per `phase-1a-url-verification.csv`), not itself a registration-focused competing page. This confirms the overlap set is exactly the two URLs already flagged in TECH-005 — no additional pages need to be added to that finding's scope.

## Overlap #2 — GST registration-cancellation/revocation sub-topic spread across 3 pages

- **Classification:** POSSIBLE OVERLAP
- **Pages involved:** `https://cashahnawaz.com/gst-registration-online/` ("Cancellation of GST Registration" H2), `https://cashahnawaz.com/gst-return-filing/` ("How to Activate Cancelled GST registration for Performing GST Return Filing", "Following Steps are to be Followed in Case of Revocation of Cancelled GST Registration", "GST REG-23: Cancellation of Application for Revocation"), and `https://cashahnawaz.com/big-relief-for-taxpayers-whose-gst-number-got-canceled-due-to-non-filing-of-gst-returns/` (Tier 3 blog, lastmod 2023-04-08)
- **Evidence:** All three pages independently explain GST registration cancellation/revocation. The two service pages cover it as a subordinate section within their broader registration/return-filing scope; the blog article is entirely devoted to a specific historical amnesty window for reactivating cancelled registrations ("Time frame for the scheme: From 01/04/2023 to 30/06/2023... no further extension of time period for filing application for revocation or cancellation of registration shall be available" — quoted in `_batch-c-tier3-sample.md`).
- **Content/Topic overlap vs. Search performance cannibalization:** Content/topic-level only; `DATA NOT AVAILABLE` for actual query-level competition between these three URLs.
- **Notes:** Differentiated by scope (general ongoing procedure on the two service pages vs. one specific, now-closed relief scheme on the blog) — this keeps it at POSSIBLE rather than LIKELY. This blog article is separately flagged for staleness in Part 2 below (consistent with TECH-004).

## Overlap #3 — The 9 industry-specific ITR pages vs. the main ITR filing page

- **Classification:** NO MEANINGFUL OVERLAP FOUND
- **Pages involved:** `https://cashahnawaz.com/income-tax-return-filing-in-mumbai/` (Tier 1) vs. all 9 industry ITR pages (Healthcare, Beauty & Wellness, E-Commerce, Real Estate & Construction, Wholesale & Retail Trade, Crypto Trading, Food & Beverage, Event Management & Entertainment, Content Creators & Influencers)
- **Evidence:** Fresh fetch of the main page confirms its content is general ITR mechanics: H2s include "What's ITR filing?", "Are you liable to File ITR?", "Documents Required to File Income Tax Return File", "Know your residential status income", "Compute Total Income From All The Sources", "Comprehensive Income Tax Rates (FY 2025-26 & 2026-27)", "Penalty for Late Filing u/s 234F" — it targets taxpayer categories generically (individuals, businesses, partnerships, companies, trusts, cooperatives) and explicitly internally links out to all 9 industry pages as further reading. Per `_batch-a-tier1-tier2.md`, each industry page instead carries sector-specific machinery not present on the main page: e.g., Real Estate's "Capital Gains on Sale of Property (Sections 67–92)", "TDR & FSI Tax/GST Treatment", "Joint Development Agreements (JDA)"; Crypto's "Section 115BBH", "The 1% TDS Under Section 194S", worked crypto-tax example; Food & Beverage's "Swiggy/Zomato — TDS, ECO Classification & Compliance"; Healthcare's "Step-by-Step: Applying the Presumptive Scheme" for doctors/clinics. Each industry page also carries its own "Presumptive Taxation," sector-specific GST/TDS treatment, MSME payment compliance, and industry-specific "Common Scrutiny Triggers" — content genuinely absent from the general page.
- **Content/Topic overlap vs. Search performance cannibalization:** Content-level assessment only; whether the main page and any industry page are actually splitting impressions/clicks for a shared query is `DATA NOT AVAILABLE` (GSC).
- **Notes:** These read as genuinely differentiated — industry-specific nuance, not thin variations. Two of the nine (Event Management & Entertainment, Content Creators & Influencers) use a visibly different/older template ("Introduction / Who Should File / 5 Important Case Laws" pattern) than the other seven's numbered "Income Tax Act 2025 — Critical Section Changes" template — this is a template-consistency observation already covered under the WordPress/technical audit, not a cannibalization risk, since each industry page still targets a distinct, non-overlapping industry keyword.

## Overlap #4 — Accounting Services (Tier 1) vs. the accounting-topic blog cluster

- **Classification:** POSSIBLE OVERLAP
- **Pages involved:** `https://cashahnawaz.com/accounting-services/` (Tier 1) vs. an 8-article accounting-topic blog cluster in `site-inventory.csv`: `/avoid-these-common-mistakes-in-writing-books-of-accounts/`, `/common-accounting-errors-and-how-to-prevent-them/`, `/important-accounting-concepts-to-ensure-proper-accounting-of-financial-data/`, `/9-principles-of-accounting-while-writing-books/`, `/what-is-the-role-of-accounting-within-a-company/`, `/what-is-business-accounting-21-tips-for-business-owners/`, `/finalisation-of-accounts-9-things-you-must-never-miss-out/`, `/the-best-accounting-software-for-small-businesses-in-2023/` (2 of the 8 fetched fresh this session; remaining 6 assessed by title/topic only)
- **Evidence:** `/accounting-services/`'s H2s are commercial/service-tier-focused: "Choose Your Package" (Essential/Enhanced/Ultimate), "What is Bookkeeping in Accounting?", "5 Things your Accounting Consultant can do for your business". The two blog articles fetched fresh are educational listicles with embedded promotion: `/avoid-these-common-mistakes-in-writing-books-of-accounts/` (H2s: "Hiring Issues: Expert Accountants & Bookkeepers", "Periodic Review of Accounts", "Scaling Accounting Easily", "Learning from Old Mistakes") and `/finalisation-of-accounts-9-things-you-must-never-miss-out/` (H2s: "Recording Expenses Payable...", "Bank Reconciliation", "Debtors & Creditors Confirmation", "Stock in Trade") — both link back to the accounting-services page and other service pages as CTAs rather than restating the service page's own package/pricing content.
- **Content/Topic overlap vs. Search performance cannibalization:** Content-level only; `DATA NOT AVAILABLE` for whether these 8 articles and the service page actually compete for shared queries in Google.
- **Notes:** The two fetched articles are differentiated by intent (long-tail informational "how to avoid X mistake" vs. commercial "hire us for bookkeeping") and explicitly funnel to the service page — this is the intended blog-supports-money-page structure, not clear cannibalization. Flagged POSSIBLE rather than NO OVERLAP because of sheer volume: 8 separate articles clustered tightly around the single broad topic "accounting/bookkeeping basics" is a pattern worth the user's attention for potential topic-cluster consolidation or a pillar-page structure, even though the 2 sampled articles individually read as legitimate top-of-funnel content. The remaining 6 articles were not fetched fresh this session — this note is scoped to title/topic-based pattern-matching, not confirmed content inspection of all 8.

## Overlap #5 — Section 8 Company Registration (Tier 1) vs. Section 8-vs-Trust comparative blog

- **Classification:** POSSIBLE OVERLAP
- **Pages involved:** `https://cashahnawaz.com/section-8-company-registration/` (Tier 1) vs. `https://cashahnawaz.com/notes-section-8-company-and-trust/` (Tier 3 blog)
- **Evidence:** The service page (fetched fresh) is procedural/transactional: H2s "Procedure for Incorporation of Section 8 Company," "Application for name availability," "Obtaining DSCs of First Directors," "Filing of SPICe 32 Form," "Benefits of Section 8 Company Registration Online." The blog article (fetched fresh) is comparative/decision-support: H2s "Governing Legislation," "Exemptions and Reliefs Available to Section-8 Companies," "Exemptions and Reliefs Available to Trust," "Foreign Contribution Regulation Act, 2010," "Social Stock Exchange," "Comparative Analysis." Both independently describe Section 8 company tax exemptions/benefits (e.g., service page: "Tax concessions via 80G certificate or 12A registration"; blog: "Exemptions include reduced stamp duty, tax benefits under Section 80G, potential full tax exemption if registered under Section 12AA").
- **Content/Topic overlap vs. Search performance cannibalization:** Content-level only; `DATA NOT AVAILABLE` for actual SERP competition between these two URLs.
- **Notes:** Differentiated primarily by framing (how-to-register vs. Section-8-vs-Trust comparison) rather than by subject matter — the "benefits/exemptions" sub-topic genuinely repeats across both. No internal link from the blog article back to the service page was observed in this fetch, which is a missed internal-linking opportunity worth flagging to internal-linking.md rather than a standalone cannibalization severity.

## Overlap #6 — TDS Chart (blog) vs. TDS Return Filing Services (Tier 1)

- **Classification:** POSSIBLE OVERLAP
- **Pages involved:** `https://cashahnawaz.com/tds-chart-for-fy-2026-27/` (Tier 3 blog) vs. `https://cashahnawaz.com/tds-return-filing-services/` (Tier 1)
- **Evidence:** The blog article is a rate-reference resource (per `_batch-c-tier3-sample.md`: TCS/TDS rate table by category — "Insurance Commission: 2% (Ind) / 10% (Others)", "Contract Work (Individual/HUF): 1%", etc.). The Tier 1 service page's H2s (`_batch-a-tier1-tier2.md`) are process-focused: "What is TDS?", "When should TDS be deducted?", "Why is TDS filing necessary?", "How to do Online TDS return filing?" — no explicit rate table on the service page itself.
- **Content/Topic overlap vs. Search performance cannibalization:** Content-level only; `DATA NOT AVAILABLE` for query-level competition.
- **Notes:** Low overlap risk — differentiated by format (reference chart vs. process/service guide) and likely different query intent (rate lookup vs. "how do I file TDS returns").

## Overlap #7 — `/trademark-registration/` reconsidered from a content angle (extends TECH-001)

- **Classification:** NO MEANINGFUL OVERLAP FOUND
- **Pages involved:** `https://cashahnawaz.com/trademark-registration/` vs. rest of the site
- **Evidence:** A fresh, more thorough fetch confirms the earlier Batch A observation: this page is a short, incomplete blog-style article — "The piece is incomplete, ending with 'prevents entrepreneurs from using…'" — with a visible publish date (18/02/2022) and "0 Comments," not a comprehensive service page. Its only structural content beyond the truncated body is "What is Trademark?" and duplicated "Get in Touch with us now…!!!" contact forms. No FAQ, no documents-required list, no process/procedure breakdown, no pricing — unlike every comparable Tier 1/2 service page audited this session (12A/80G, TDS, Section 8, GST Registration, GST Return Filing all have Overview → Documents → Procedure/Benefits → FAQ structure).
- **Content/Topic overlap vs. Search performance cannibalization:** Content-level only. No other live page on the site was found covering trademark registration, so there is no second URL to compete with in the SERPs even in principle — `NO MEANINGFUL OVERLAP FOUND` is the correct label for the overlap question specifically.
- **Notes:** This is a content-depth finding, not a cannibalization finding — flagged here per the task's explicit instruction to reconsider TECH-001 from the content angle. It independently reinforces TECH-001 (the page/taxonomy slug collision): the content currently occupying this contested slug is also the thinnest, least complete "service page" on the site, which is relevant context for whoever resolves the slug collision (renaming the taxonomy term won't fix the page's own content gap). Route the content-depth gap itself to content-audit.md's coverage-map scoring, not to this cannibalization section.

## Overlap #8 — Accounting Services package bundling vs. dedicated GST/TDS Return Filing pages

- **Classification:** POSSIBLE OVERLAP
- **Pages involved:** `https://cashahnawaz.com/accounting-services/` vs. `https://cashahnawaz.com/gst-return-filing/` and `https://cashahnawaz.com/tds-return-filing-services/`
- **Evidence:** The Accounting Services page summary confirms its packages ("Choose Your Package" — Essential/Enhanced/Ultimate) explicitly include "GST and TDS return filing" as a bundled feature, per the WebFetch summary: "Core offerings include 'Accounting in Tally,' GST and TDS return filing, financial statement preparation, and MIS reporting." Both `/gst-return-filing/` and `/tds-return-filing-services/` are separately dedicated Tier 1 pages for exactly those services.
- **Content/Topic overlap vs. Search performance cannibalization:** Content-level only; `DATA NOT AVAILABLE` for whether Accounting Services and the two dedicated filing pages compete for the same search queries.
- **Notes:** This is normal, expected package-bundling for a CA firm (accounting retainers commonly bundle compliance filing) and is not treated as a risk on its own — flagged POSSIBLE only because a searcher/Google could see three pages all claiming to offer "GST/TDS filing," and it's worth the user confirming the Accounting Services package descriptions don't duplicate the dedicated pages' full process/FAQ content (this fetch only surfaced package-feature bullet points, not a full section reproducing the dedicated pages' content).

## Overlap #9 — Accounting Services vs. Audit Services (specifically checked per content-audit.md's conflation warning)

- **Classification:** NO MEANINGFUL OVERLAP FOUND
- **Pages involved:** `https://cashahnawaz.com/accounting-services/` vs. `https://cashahnawaz.com/audit-services/`
- **Evidence:** Fresh fetches confirm clear differentiation. Accounting Services: bookkeeping-centric ("What is Bookkeeping in Accounting?", tiered packages, "Accounting in Tally," payroll/AR/AP, MIS reporting). Audit Services: statutory/compliance-centric ("Tax audit — thresholds, presumptive scheme & due dates," "Statutory audit — companies & LLPs," Section 44AB thresholds "₹50L-₹1Cr," "companies and LLPs above ₹40L turnover," "Audit & compliance calendar — AY 2026-27," "What typically triggers scrutiny").
- **Content/Topic overlap vs. Search performance cannibalization:** Content-level only; `DATA NOT AVAILABLE` for GSC-confirmed query overlap.
- **Notes:** content-audit.md specifically flags Accounting/Audit conflation as a common thin-CA-site pattern — checked directly and cleared. These two pages are well-differentiated on this site.

---

# Part 2 — Financial/Tax Content Freshness Sweep (extends Phase 1A's TECH-004)

Applying the Financial/Regulated Content Accuracy Protocol from `skills/content-audit.md`: for every claim below, the exact figure/date is quoted, no "correct" replacement value is asserted, and anything reading as outdated is flagged for professional verification independent of SEO severity.

## Consolidated from Phase 1A (TECH-004) — already established

### `https://cashahnawaz.com/gst-amnesty-scheme-2023/`
- **Classification:** LIKELY OUTDATED
- **Evidence:** "01/04/2023 to 30/06/2023" (amnesty active period); "30th June 2023" emphasized repeatedly as deadline; sitemap lastmod 2026-05-06, ~3 years after the described deadline, with no visible revision.
- **Professional verification flag:** PROFESSIONAL / CURRENT REGULATORY VERIFICATION REQUIRED — recommend the user's team confirm whether this content should be updated, archived with historical framing, or redirected.

### `https://cashahnawaz.com/big-relief-for-taxpayers-whose-gst-number-got-canceled-due-to-non-filing-of-gst-returns/`
- **Classification:** LIKELY OUTDATED
- **Evidence:** "The application can be made upto 30th June 2023"; "no further extension of time period for filing application for revocation or cancellation of registration shall be available" — the article's own text confirms the window is closed with no extension.
- **Professional verification flag:** PROFESSIONAL / CURRENT REGULATORY VERIFICATION REQUIRED.

## New items checked this session (5 additional articles, plus 1 evergreen contrast example)

### `https://cashahnawaz.com/gst-new-update-due-dates-for-october-2021/`
- **Classification:** LIKELY OUTDATED
- **Evidence:** H1 "Important of GST And Other Due Date Calendar Month Of October 2021"; body dates run "7-10-2021" through "31-10-2021"; "GSTR 4 for the FY 2020-21"; "Form MSME... for the period April 2021 to September 2021." No disclaimer or historical-archive notice observed. Sitemap lastmod is 2026-05-14 — nearly 5 years after the deadlines described, with no substantive-update signal.
- **Professional verification flag:** PROFESSIONAL / CURRENT REGULATORY VERIFICATION REQUIRED.

### `https://cashahnawaz.com/due-date-calendar-for-the-month-of-november-2022/`
- **Classification:** LIKELY OUTDATED
- **Evidence:** H1 "Due Date Calendar for the Month of November, 2022"; "The following is the Chart of due date under various Acts for the month of November 2022"; dated entries "01-11-2022" through "13-11-2022" (e.g., "TDS / TCS Payment for the month of October 2022" due 07-11-2022). No disclaimer indicating the content is historical/archival.
- **Professional verification flag:** PROFESSIONAL / CURRENT REGULATORY VERIFICATION REQUIRED.

### `https://cashahnawaz.com/waiver-of-late-fees-for-gst-annual-return/`
- **Classification:** LIKELY OUTDATED
- **Evidence:** "notification (No. 08/2025 – Central Tax)" dated "January 23, 2025"; applicable to FYs "2017-18" through "2022-23"; explicit self-stated deadline: "the waiver is valid only for filings completed by March 31, 2025" — a date now well in the past relative to the current session date (2026-08-27).
- **Professional verification flag:** PROFESSIONAL / CURRENT REGULATORY VERIFICATION REQUIRED.

### `https://cashahnawaz.com/key-recommendations-of-45th-gst-council-meeting/`
- **Classification:** TIME-SENSITIVE — REVIEW REQUIRED
- **Evidence:** "The GST Council's 45th meeting was held today in Lucknow" on "17th September, 2021"; multiple effective dates quoted ("w.e.f 1.10.2021," "31st December, 2021," "01.01.2022," "1.4.2022"). The article does not carry an explicit "historical record" framing/disclaimer, even though — like case-law articles — its subject matter is inherently a dated record of a specific past event. Because GST Council rate/policy recommendations are routinely superseded by later meetings, a reader unfamiliar with the GST Council's meeting cadence could mistake this for current guidance.
- **Professional verification flag:** PROFESSIONAL / CURRENT REGULATORY VERIFICATION REQUIRED — recommend either an explicit "historical record, see current GST Council updates" framing note, or archiving.

### `https://cashahnawaz.com/june-2026-important-due-dates/`
- **Classification:** TIME-SENSITIVE — REVIEW REQUIRED
- **Evidence:** H1 "June 2026 Important Due dates | Income Tax | GST | MCA | Other Law"; deadlines dated June 7, 11, 15, 20, and 30, 2026 — all now past as of the current session date (2026-08-27). No disclaimer observed. Per `_batch-a-tier1-tier2.md`'s `/blogs/` fetch, this article was still showing as one of only four featured posts on the blog index's first page, meaning it is being surfaced prominently roughly two months past its own relevance window.
- **Professional verification flag:** PROFESSIONAL / CURRENT REGULATORY VERIFICATION REQUIRED — lower urgency than the multi-year-stale items above (monthly due-date-calendar content naturally ages out each month, which is a normal content-type lifecycle rather than a one-off oversight), but the featured-post placement past relevance is worth flagging for a content-refresh/rotation process.

### `https://cashahnawaz.com/old-vs-new-tax-regime-which-tax-system-is-better-for-salaried-employees/` (previously noted as a raw observation in `_batch-c-tier3-sample.md`, formally classified here)
- **Classification:** TIME-SENSITIVE — REVIEW REQUIRED
- **Evidence:** Slab table quoted verbatim: "up to ₹3,00,000 - Nil; ₹3,00,001- ₹6,00,000 - 5%; ₹6,00,001- ₹9,00,000 - 10%; ₹9,00,001- ₹12,00,000 - 15%; ₹12,00,001- ₹15,00,000 - 20%; ₹15,00,001 and above - 30%" with no FY/AY label visible anywhere adjacent to the table, despite the page's entire premise being a year-sensitive "old vs. new" regime comparison.
- **Professional verification flag:** PROFESSIONAL / CURRENT REGULATORY VERIFICATION REQUIRED — the absence of a year label is itself the risk signal here (freshness cannot be confirmed either way from visible content), which is precisely why this needs review rather than being asserted as either current or outdated.

### `https://cashahnawaz.com/tds-chart-for-fy-2026-27/` (evergreen contrast example, previously fetched in `_batch-c-tier3-sample.md`)
- **Classification:** CURRENTLY APPEARS EVERGREEN
- **Evidence:** Title and H1 both explicitly state "FY 2026-27"; content references "Income-tax Act, 2025 coming into full effect from April 1, 2026" and new Section 392-394 numbering; sitemap lastmod (2026-05-11) is internally consistent with the FY the article targets, with no expired-window language.
- **Professional verification flag:** Not applicable — included here as a positive-control comparison showing what a correctly year-labeled, currently-targeted piece looks like next to the outdated items above, not because it needs verification itself. (Note: "appears evergreen" reflects internal date-consistency only, not a confirmation that the cited rates/rules are themselves currently correct — that determination is out of scope per the Accuracy Protocol.)

---

# Summary

**Part 1:** 9 overlaps investigated — 1 LIKELY CANNIBALIZATION RISK, 5 POSSIBLE OVERLAP, 3 NO MEANINGFUL OVERLAP FOUND. Zero CONFIRMED CONTENT DUPLICATION found (no near-identical text/structure was identified between any two pages this session). No claim is made anywhere in this document about actual SERP-level cannibalization — GSC/query data is `DATA NOT AVAILABLE` this session throughout.

**Part 2:** 2 items consolidated from Phase 1A's TECH-004 (both LIKELY OUTDATED) + 6 new items checked this session (3 LIKELY OUTDATED, 2 TIME-SENSITIVE — REVIEW REQUIRED newly formalized from prior raw notes, 1 TIME-SENSITIVE — REVIEW REQUIRED newly checked, 1 CURRENTLY APPEARS EVERGREEN as contrast). 7 of the 8 total items in this sweep carry a PROFESSIONAL / CURRENT REGULATORY VERIFICATION REQUIRED flag. No specific "correct" current rate, threshold, or deadline is asserted anywhere in this document, per CLAUDE.md and the Accuracy Protocol.
