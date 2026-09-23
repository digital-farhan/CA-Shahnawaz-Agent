# Phase 1B — On-Page SEO Audit — cashahnawaz.com

**Session date:** 2026-08-27
**Site:** https://cashahnawaz.com/
**Phase type:** Evidence-based on-page SEO audit (Sections 1, 3, 4, 9, 10 of the Phase 1B brief). No live-site changes were made. This report extends, and does not duplicate, Phase 1A's technical findings (TECH-001 through TECH-007, WP-001) in `reports/01-technical-seo.md` / `reports/02-wordpress-seo.md`.

**Scope discipline:** Per `skills/on-page-seo.md`, this report owns title/meta/heading/URL mechanics, CTA-copy/label relevance, and content-to-intent match at the page level. Content depth, freshness, trust/E-E-A-T substance, and content gaps belong to `reports/04-content-audit.md`; this report only points to those items briefly where they intersect with on-page mechanics.

**No keyword volume, ranking, or GSC/GA4 data was available or used anywhere in this report.** Every search-intent statement is explicitly labeled `LIKELY USER SEARCH INTENT`, and `SEARCH DEMAND DATA NOT AVAILABLE` is stated wherever keyword-volume evidence would otherwise be needed.

---

## Section 1 — Audit Coverage

| Metric | Value |
|---|---|
| Total URLs in site inventory | **111** (`data/crawl/site-inventory.csv`) |
| URLs available for detailed content review (sitemap-confirmed, live-loading content) | 111, minus 3 non-content/WP-system duplicates and query-only URLs; effectively ~108 content-bearing URLs |
| Tier 1 (Critical Commercial) URLs | 13 |
| Tier 2 (Supporting) URLs | 15 |
| Tier 3 (Blog/Article) URLs | 66 |
| Not Prioritized (legal/tools/archives/footer-only) | 18 |

### URLs actually reviewed this phase (Phase 1B)

- **13 Tier 1 pages** — full deep content-quality review, fresh WebFetch this session, per `data/crawl/_phase1b-batch1-tier1-review.md` (7 pages) and `_phase1b-batch2-tier1-review.md` (6 pages). This is a distinct, content-quality-focused re-fetch of every Tier 1 URL, independent of Phase 1A's title/H1-focused fetch of the same URLs.
- **9 additional pages** fetched fresh this session by the coverage-map and cannibalization/freshness work:
  - 1 Tier 2 page re-fetched for a deeper content-angle pass: `/trademark-registration/` (`_phase1b-cannibalization-and-freshness.md`, Overlap #7).
  - 8 Tier 3 pages fetched fresh for the first time this session (not part of Phase 1A's 15-URL Tier 3 sample): `/avoid-these-common-mistakes-in-writing-books-of-accounts/`, `/finalisation-of-accounts-9-things-you-must-never-miss-out/`, `/notes-section-8-company-and-trust/`, `/gst-new-update-due-dates-for-october-2021/`, `/due-date-calendar-for-the-month-of-november-2022/`, `/waiver-of-late-fees-for-gst-annual-return/`, `/key-recommendations-of-45th-gst-council-meeting/`, `/june-2026-important-due-dates/`.
  - (The coverage-map agent's own "9 candidate pages" fetch — `accounting-services`, `audit-services`, `startup-registration-india`, `public-limited-company`, `llp-annual-filing`, `gst-registration-online`, `gst-return-filing`, `income-tax-return-filing-in-mumbai`, `section-8-company-registration` — are all within the 13 Tier 1 set above and are not counted twice.)

**Total URLs individually reviewed this phase: 22** (13 Tier 1 + 9 additional). Combined with Phase 1A's 53 individually-fetched URLs (some overlapping, since Tier 1/Tier 2 pages were fetched in both phases for different purposes), the cumulative count of distinct URLs that have received at least one individual fetch across Phase 1A + Phase 1B is **62 of 111 (56%)**: the 53 from Phase 1A plus the 8 genuinely new Tier 3 URLs and 1 re-verified Tier 2 URL from this phase (the 13 Tier 1 pages were already inside Phase 1A's 53).

### Coverage verdict by tier

- **Tier 1: COMPLETE COVERAGE.** 13/13 (100%) received a full content-quality deep review this phase, on top of Phase 1A's title/H1/meta-level check. This is the highest-confidence tier in the audit.
- **Tier 2: PARTIAL COVERAGE.** 15/15 (100%) received title/URL-level verification in Phase 1A; only 1/15 (`/trademark-registration/`) received a genuine content-quality pass this phase. The 9 industry-specific ITR pages received a partial content-structure comparison (via `_phase1b-cannibalization-and-freshness.md` Overlap #3, reusing Phase 1A's H2-level evidence) but not a full per-page deep-dive equivalent to the Tier 1 batches. About Us, Contact Us, Blogs index, Tax Guides index, and Tax Case Law index received title/URL-level checking only, no content-quality pass this phase.
- **Tier 3: PARTIAL COVERAGE.** 15/66 sampled in Phase 1A + 8 new in Phase 1B = 23/66 (35%) have now received an individual fetch across both phases, explicitly disclosed as a sample, not a full crawl. The remaining 43 Tier 3 URLs (65%) rely on sitemap metadata only.
- **Site-wide: PARTIAL COVERAGE.** Tier 1 is complete; Tier 2 and Tier 3 remain samples. This is consistent with `website-crawl.md`'s disclosure requirement for a representative-sample approach on a site this size.

---

## Section 3 — On-Page SEO Audit (13 Tier 1 Pages)

Method: cross-references Phase 1A's title/H1 capture (`data/crawl/phase-1a-url-verification.csv`, `_batch-a-tier1-tier2.md`) with this phase's content-quality fetches (`_phase1b-batch1-tier1-review.md`, `_phase1b-batch2-tier1-review.md`). Where Phase 1A did not surface a field (meta description, canonical — sitewide tool limitation, see `reports/01-technical-seo.md` Section 6), it is marked `NOT VISIBLE (tool limitation)` rather than assumed absent.

| # | URL | Topic Clarity / URL Relevance | Title/H1 (per Phase 1A capture) | H2–H3 Structure | `LIKELY USER SEARCH INTENT` | CTA Relevance | FAQ Present? | Freshness Pointer | Cannibalization Pointer |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Homepage `/` | Clear — brand/navigational hub | H1: "Flawless Compliance. Strategic Advice. Total Peace of Mind." | Logical; "TESTIMONIALS" H2 renders empty (OP-004) | Branded search + generic "CA firm Mumbai" discovery. `SEARCH DEMAND DATA NOT AVAILABLE` | 6+ CTAs; top strip omits GST Registration, GST Return Filing, Audit Services (OP-006) | No | Due-dates widget appears current; no dated tax claims on-page | None |
| 2 | `/gst-registration-online/` | Clear, service term in slug | Title confirmed: "GST Registration Online In Mumbai \| Expert CA Consultant" | Logical; documents table well-structured | Transactional — register for GST now | Generic dropdown, not pre-selected; stated Rs 1,500 fee is a genuine differentiator | Yes (5 Q&A) | See report C — TIME-SENSITIVE figures | See report C CONT-023 (unverified 3rd URL via anchor text) |
| 3 | `/gst-return-filing/` | Clear | Title confirmed: "GST Filing Services In Mumbai \| Professional CA Support" | Logical; 11 return-type taxonomy is a genuine strength | Transactional/recurring | "Get a Free Quote" language misleading — no price shown anywhere on page | Yes (7 Q&A) | See report C — TIME-SENSITIVE figures | Extends TECH-005 (see report C) |
| 4 | `/income-tax-return-filing-in-mumbai/` | Local-intent title but content is nationally generic (Mumbai differentiator is keyword-only, not substantive local content) | Title confirmed | Logical; hub for 9 industry pages | Transactional, seasonal | "Checkout" buttons under priced packages — strongest CTA-to-price pairing on the site | Yes (6 Q&A) | **CRITICAL** — see report C CONT-002 | See report C CONT-011 |
| 5 | `/itr-filing-for-nri-guide-for-non-resident-taxation/` | Clear, genuinely NRI-specific (not generic ITR reskin) | Not individually captured Phase 1A; confirmed live in Batch A | Logical; DTAA/repatriation/case-law sections | Transactional/research hybrid, overseas audience | No FAQ, no pricing, no NRI due date, no international contact channel — see Section 9 | **No** | TIME-SENSITIVE — see report C CONT-011 | None |
| 6 | `/accounting-services/` | Clear | Title confirmed | Logical; "Charges" header over-promises (no numbers shown) | Package-comparison intent | "For Pricing, Check Out" routes to generic form, not disclosure | Yes (3 Q&A) | Evergreen (no dated claims) | See report C Overlap #4/#8/#9 |
| 7 | `/audit-services/` | Clear | Title confirmed: H1 itself states "FY 2025-26 (AY 2026-27)" | Logical; explicit disclaimer present (rare, good practice) | Transactional, deadline-driven | Phone/email-first CTA framing (distinct from form-first pattern elsewhere) | Yes (5 Q&A) | TIME-SENSITIVE — see report C CONT-011 | None |
| 8 | `/startup-registration-india/` | Clear | Title confirmed | Logical but prose-heavy in places | Transactional, founder audience | Generic dropdown | Yes (5 Q&A) | TIME-SENSITIVE — see report C CONT-012 | None |
| 9 | `/section-8-company-registration/` | Clear | Title confirmed | Logical; genuinely covers ongoing compliance, not just formation | Transactional, NGO founders | Generic dropdown | Yes | TIME-SENSITIVE — see report C CONT-012 | See report C Overlap #5 |
| 10 | `/public-limited-company/` | Clear, but is the site's only company-registration entity page | Title confirmed | Logical | Transactional / comparison-shopping (only entity-comparison content on-site) | Generic dropdown | Yes (4 Q&A) | **Self-contradiction — see OP-001 below** | Evidence that Private Ltd Co page is a real gap — see report C CONT-014 |
| 11 | `/llp-annual-filing/` | Scoped to compliance only; possible nav-link mislabeling — see OP-002 | Title confirmed | Logical; only page in batch with a "Why us" H2 | Recurring compliance, deadline-anxious | Generic dropdown | Yes (5 Q&A) | **CRITICAL** — see report C CONT-003 | LLP formation gap — see report C CONT-015 |
| 12 | `/tds-return-filing-services/` | Clear | Not individually captured Phase 1A; confirmed live in Batch A | Logical; comparatively shorter than sibling R&C pages | Recurring compliance | "Contact Now" placed directly after FAQ — good placement | Yes (3 Q&A) | TIME-SENSITIVE — see report C CONT-012 | See report C Overlap #6 |
| 13 | `/12a-or-12aa-or-80g-registration-new-scheme/` | H1 narrower than actual scope — see OP-007 | Not individually captured Phase 1A; confirmed live in Batch A | Logical but heavily repetitive (nav/CTA repeated 3-4x) | Transactional, NGO/trust administrators | Generic dropdown | Yes | **CRITICAL** — see report C CONT-004 | None |

---

## Section 4 — Page-by-Page Content Quality Ratings (13 Tier 1 Pages)

Ratings use `STRONG | ADEQUATE | NEEDS IMPROVEMENT | WEAK | NOT REVIEWED` across the phase brief's 14 dimensions, backed directly by the batch-file evidence above. No numeric score is used, per phase brief instruction.

| # | Page | Depth/Coverage | Accuracy/Freshness | E-E-A-T/Trust | Structure/Scannability | FAQ Quality | Pricing Transparency | CTA Alignment | Internal Linking | Overall |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Homepage | ADEQUATE | ADEQUATE | NEEDS IMPROVEMENT (empty testimonials, no named team) | STRONG | N/A | N/A | NEEDS IMPROVEMENT | STRONG | **ADEQUATE** |
| 2 | GST Registration | STRONG | NEEDS IMPROVEMENT (unqualified figures) | ADEQUATE | STRONG | STRONG | STRONG (only page with clear fee) | ADEQUATE | ADEQUATE | **STRONG** |
| 3 | GST Return Filing | STRONG | NEEDS IMPROVEMENT (unqualified figures) | NEEDS IMPROVEMENT (no confidentiality statement observed) | STRONG | STRONG | WEAK (no pricing at all) | NEEDS IMPROVEMENT | ADEQUATE | **ADEQUATE** |
| 4 | ITR Mumbai | STRONG | **WEAK** (confirmed stale AY2020-21 reference) | NEEDS IMPROVEMENT (no named byline) | NEEDS IMPROVEMENT (keyword-stuffed) | STRONG | STRONG | ADEQUATE | STRONG | **NEEDS IMPROVEMENT** |
| 5 | NRI Taxation | STRONG | NEEDS IMPROVEMENT (dense new/old Act mapping unverified) | ADEQUATE (strongest case-law depth) but WEAK on social proof | STRONG | **WEAK** (none) | WEAK (none) | **WEAK** (no international contact option) | STRONG | **NEEDS IMPROVEMENT** |
| 6 | Accounting Services | ADEQUATE (no Accounting-vs-Audit distinction) | ADEQUATE | **WEAK** (wrong firm name) | STRONG | ADEQUATE | WEAK (header promises, no numbers) | NEEDS IMPROVEMENT | ADEQUATE | **NEEDS IMPROVEMENT** |
| 7 | Audit Services | ADEQUATE (Internal Audit thin) | NEEDS IMPROVEMENT (dense citations, unverified) | ADEQUATE (best disclaimer practice) but WEAK (zero testimonials) | STRONG | STRONG | WEAK (none) | ADEQUATE | ADEQUATE | **ADEQUATE** |
| 8 | Startup Registration | STRONG | NEEDS IMPROVEMENT (unqualified figures) | WEAK (no trust signals at all) | ADEQUATE | STRONG | WEAK (none, may be intentional) | ADEQUATE | NEEDS IMPROVEMENT (Pvt Ltd/LLP gap) | **ADEQUATE** |
| 9 | Section 8 Company | STRONG (genuine ongoing-compliance depth) | NEEDS IMPROVEMENT (unqualified penalty figures) | WEAK (no trust signals) | STRONG | STRONG | WEAK (none) | ADEQUATE | NEEDS IMPROVEMENT (no reciprocal 12A link) | **STRONG** |
| 10 | Public Limited Company | ADEQUATE | **WEAK** (self-contradiction) | WEAK (no trust signals) | ADEQUATE | ADEQUATE | WEAK (none) | ADEQUATE | ADEQUATE | **NEEDS IMPROVEMENT** |
| 11 | LLP Annual Filing | ADEQUATE (no formation content, correctly scoped) | **WEAK** (confirmed stale "Final Year 2021-22") | ADEQUATE (only page with "Why us" section) | STRONG | STRONG | WEAK (none) | ADEQUATE | NEEDS IMPROVEMENT | **NEEDS IMPROVEMENT** |
| 12 | TDS Return Filing | ADEQUATE (thinner than siblings) | NEEDS IMPROVEMENT (unqualified figures) | WEAK (no trust signals) | ADEQUATE | ADEQUATE | WEAK (none) | STRONG (FAQ→CTA placement) | NEEDS IMPROVEMENT | **ADEQUATE** |
| 13 | 12A/80G Registration | STRONG (deepest page in batch) | **WEAK** (confirmed passed deadlines, no historical framing) | WEAK (no trust signals; minor NAP inconsistency) | NEEDS IMPROVEMENT (repetitive) | ADEQUATE (one FAQ answer incomplete) | WEAK (none) | ADEQUATE | STRONG | **NEEDS IMPROVEMENT** |

All 13/13 Tier 1 pages rated; 0 marked `NOT REVIEWED`. No Tier 2 or Tier 3 page is rated in this table — this table is scoped to Tier 1 only, per the phase brief's Section 4 instruction.

---

## Section 9 — Conversion Content Alignment (Content/Intent Only — Not a CRO Audit)

Per phase brief instruction, this is explicitly **not** a design/UX/CRO audit (that is `cro-audit.md`'s job in a later phase). This section judges only whether each page's CTA copy and form logic align with the content and intent already established on that page.

| Page | Classification | Basis |
|---|---|---|
| Homepage | `LIKELY CONVERSION OPPORTUNITY` | Multiple CTAs and forms present; empty testimonials section and thin top-level CTA strip are content-alignment issues, not design ones (OP-004, OP-006) |
| GST Registration | `LIKELY CONVERSION OPPORTUNITY` | Best-in-batch: publishes actual pricing (Rs 1,500), but CTA copy ("Get Quote in a moment") doesn't reference that price |
| GST Return Filing | `CONFIRMED CONTENT-TO-CONVERSION GAP` | CTA reads "Get a Free Quote" with zero pricing content anywhere on the page to set expectations before submission |
| ITR Mumbai | `LIKELY CONVERSION OPPORTUNITY` | "Checkout" CTAs sit directly under 3 named price tiers — the strongest content-to-CTA pairing site-wide, but unclear (content alone) whether "Checkout" leads to a package-specific flow or the same generic form |
| NRI Taxation | `CONFIRMED CONTENT-TO-CONVERSION GAP` | Page explicitly targets an overseas, non-resident audience; CTA/form offers no non-Indian contact channel, no time-zone accommodation copy, and no NRI-specific form fields — a direct mismatch between stated audience and conversion mechanics |
| Accounting Services | `CONFIRMED CONTENT-TO-CONVERSION GAP` | Section literally headed "Charges for Accounting Services" delivers no charges; CTA "For Pricing, Check Out" routes to the same generic form as every other CTA on the site |
| Audit Services | `LIKELY CONVERSION OPPORTUNITY` | Phone/email-first CTA framing suits the deadline-urgency content well; no pricing anywhere, but content-audit.md notes this may be an intentional choice for a variable-scope service |
| Startup Registration | `LIKELY CONVERSION OPPORTUNITY` | Generic dropdown; content doesn't reference the CTA's "quote" framing against any stated cost expectation |
| Section 8 Company | `LIKELY CONVERSION OPPORTUNITY` | Strong compliance-depth content not matched by any registration-timeline or cost expectation in the CTA copy |
| Public Limited Company | `LIKELY CONVERSION OPPORTUNITY` | Generic dropdown; the page's own self-contradiction (OP-001) undermines confidence in the surrounding CTA's implicit promise of accurate guidance |
| LLP Annual Filing | `LIKELY CONVERSION OPPORTUNITY` | "Why Shahnawaz and Associates?" section supports conversion well; undermined by the stale "Final Year 2021-22" content sitting nearby, which could reduce trust at the point of decision |
| TDS Return Filing | `LIKELY CONVERSION OPPORTUNITY` | "Contact Now" placed directly after the FAQ is a genuinely well-aligned content-to-CTA sequencing choice |
| 12A/80G Registration | `NOT VERIFIABLE` | CTA/form repetition (3-4x) makes it difficult to assess content-to-CTA sequencing from the fetch alone; requires a rendered/visual check outside this audit's tool access |

**Sitewide pattern (not scored per-page again):** Every Tier 1 page uses the same generic, non-pre-contextualized Name/Email/Mobile/City/Select-Service dropdown form, and the "GET IT NOW" popup pattern is sitewide. This is a content/intent-alignment observation (the dropdown never defaults to the page's own service) — the design/placement judgment on whether this constitutes a UX problem belongs to `cro-audit.md`.

---

## Section 10 — Full Per-Page Recommendation Blocks (13 Tier 1 Pages)

The structured per-page blocks below are drawn directly from `data/crawl/_phase1b-batch1-tier1-review.md` and `_phase1b-batch2-tier1-review.md`, which were already written to the phase brief's Section 10 spec. Vocabulary has been checked against the phase brief's required labels; `Recommended Next Action` values are normalized to the controlled set: `KEEP AND OPTIMIZE`, `EXPAND EXISTING PAGE`, `PROFESSIONAL ACCURACY REVIEW REQUIRED`, `CONSOLIDATE / REVIEW OVERLAP`, `NEW PAGE RECOMMENDED` (none of the 13 Tier 1 pages required this last label — they all already exist).

### 1. Homepage — `/`
- **Recommended Priority:** HIGH PRIORITY
- **Recommended Next Action:** KEEP AND OPTIMIZE
- **Key actions:** Populate or remove the empty "TESTIMONIALS" section (OP-004); promote GST Registration, GST Return Filing, and Audit Services into the top CTA strip (OP-006); add a quantified trust statistic only if a verified true figure exists; fix "Resonable Cost" typo.

### 2. GST Registration Online — `/gst-registration-online/`
- **Recommended Priority:** MEDIUM PRIORITY
- **Recommended Next Action:** KEEP AND OPTIMIZE
- **Key actions:** Enumerate the actual 11 registration steps (currently only a step count is given); add an in-body contextual link to GST Return Filing; remove/correct the misplaced "GST return filing takes six-seven days" sentence (OP-008); route rupee figures for professional currency verification (see report C).

### 3. GST Return Filing — `/gst-return-filing/`
- **Recommended Priority:** HIGH PRIORITY
- **Recommended Next Action:** EXPAND EXISTING PAGE
- **Key actions:** Add pricing (or an explicit statement that pricing is quote-based) to close the gap with its sibling GST Registration page; add a general (non-nil) return-filing walkthrough; add a documents/data checklist; verify the `/gst-registration-services-india-a-guide-to-gst/` anchor target (report C CONT-023).

### 4. Income Tax Return Filing in Mumbai — `/income-tax-return-filing-in-mumbai/`
- **Recommended Priority:** CRITICAL
- **Recommended Next Action:** PROFESSIONAL ACCURACY REVIEW REQUIRED
- **Key actions:** Resolve the AY2020-21 stale FAQ reference (CONT-002) before any other optimization; reduce "income tax return filing in mumbai" keyword repetition; add a genuinely Mumbai-specific content element or reconsider the local-intent framing; add a named CA byline.

### 5. ITR Filing for NRI — `/itr-filing-for-nri-guide-for-non-resident-taxation/`
- **Recommended Priority:** CRITICAL
- **Recommended Next Action:** PROFESSIONAL ACCURACY REVIEW REQUIRED
- **Key actions:** Line-by-line review of the old/new Income Tax Act section cross-mappings (CONT-011, consolidated with ITR Mumbai and Audit Services); add an FAQ; add pricing/timeline guidance; add an NRI-specific due date; add a non-Indian contact channel (WhatsApp or equivalent) and testimonial.

### 6. Accounting Services — `/accounting-services/`
- **Recommended Priority:** HIGH PRIORITY
- **Recommended Next Action:** KEEP AND OPTIMIZE
- **Key actions:** Correct "TAXZONA Consultancy" to the firm's actual name immediately (CONT-001) — this takes priority over all other work on this page; add an explicit Accounting-vs-Audit distinction with a link to Audit Services; either publish real pricing or remove the "Charges" section header.

### 7. Audit Services — `/audit-services/`
- **Recommended Priority:** HIGH PRIORITY
- **Recommended Next Action:** PROFESSIONAL ACCURACY REVIEW REQUIRED
- **Key actions:** Build out Internal Audit to the same depth as Tax Audit/Statutory Audit (report C CONT-017); attach the "ICAI Practising CA UDIN-verified" claim to a named, checkable individual; add testimonials/case studies; verify old/new Act section citations (CONT-011).

### 8. Startup Registration India — `/startup-registration-india/`
- **Recommended Priority:** MEDIUM PRIORITY
- **Recommended Next Action:** KEEP AND OPTIMIZE; PROFESSIONAL ACCURACY REVIEW REQUIRED for the ₹100 crore/10-year eligibility figures
- **Key actions:** Add a trust block naming team expertise; add ongoing-compliance-after-recognition content; add links to Accounting/Audit Services for post-incorporation needs.

### 9. Section 8 Company Registration — `/section-8-company-registration/`
- **Recommended Priority:** HIGH PRIORITY
- **Recommended Next Action:** KEEP AND OPTIMIZE; PROFESSIONAL ACCURACY REVIEW REQUIRED for stated penalty figures
- **Key actions:** Add a reciprocal link to the 12A/80G page; add a stated registration timeline; add a trust signal/named credential.

### 10. Public Limited Company — `/public-limited-company/`
- **Recommended Priority:** HIGH PRIORITY
- **Recommended Next Action:** PROFESSIONAL ACCURACY REVIEW REQUIRED (resolve the paid-up-capital contradiction, OP-001)
- **Key actions:** Resolve the internal contradiction; add testimonials; note (not act on) the comparison table as a seed for a possible future Private Limited Company page, contingent on the coverage-map's own CRITICAL-priority gap recommendation in report C.

### 11. LLP Annual Filing — `/llp-annual-filing/`
- **Recommended Priority:** CRITICAL
- **Recommended Next Action:** PROFESSIONAL ACCURACY REVIEW REQUIRED (the "Final Year 2021-22" table, CONT-003, as top priority)
- **Key actions:** Independently verify the "LLP Registration" nav-link anomaly (OP-002); add a step-by-step filing walkthrough; replicate the page's own "Why us" section pattern once strengthened, sitewide.

### 12. TDS Return Filing Services — `/tds-return-filing-services/`
- **Recommended Priority:** MEDIUM PRIORITY
- **Recommended Next Action:** KEEP AND OPTIMIZE; PROFESSIONAL ACCURACY REVIEW REQUIRED for stated rupee thresholds/penalties
- **Key actions:** Add a TDS rate table by payment category (the page claims rates vary but never shows them); add trust signals; add links to ITR Mumbai and GST Registration.

### 13. 12A/12AA/80G Registration — `/12a-or-12aa-or-80g-registration-new-scheme/`
- **Recommended Priority:** CRITICAL
- **Recommended Next Action:** PROFESSIONAL ACCURACY REVIEW REQUIRED (the March 2022/April 2021/June 2021 dated deadlines, CONT-004, as top priority)
- **Key actions:** Confirm reciprocal Section 8 → 12A/80G link exists; complete the missing Form 10AB due-date FAQ answer; broaden H1 to reflect 80G/12AA scope (OP-007); resolve the minor address-format inconsistency (NAP note for a future local-seo pass).

---

## On-Page Findings (OP-xxx)

Each finding uses the full CLAUDE.md Required Finding Template.

### [HIGH] OP-001 — Public Limited Company page states two contradictory minimum paid-up capital figures

- **Issue (Finding):** The page's "Requirements" section states minimum paid-up capital as "Rs 5 lakhs," while its own FAQ Q1 states "There is no minimum paid-up capital as of now for company incorporation" — a direct, in-page factual contradiction on a concrete capital-planning figure.
- **Severity:** HIGH. This is not CRITICAL because it does not block indexing, ranking, or the enquiry form itself, and the page still converts; it is not MEDIUM because it directly misinforms a prospective client on a specific number they would use to plan a real financial commitment, which is a material trust/decision-quality issue for a CA firm's own published copy.
- **Evidence:** `data/crawl/_phase1b-batch2-tier1-review.md`, Public Limited Company entry, "Issues Identified" and "Financial/Tax Content Freshness": "the eligibility section states 'minimum paid-up capital: Rs 5 lakhs,' but FAQ Q1 states 'There is no minimum paid-up capital as of now for company incorporation.'"
- **Affected URLs:** `https://cashahnawaz.com/public-limited-company/`
- **SEO Impact:** Engagement and Form Submission / Genuine Enquiry stages. A visitor who notices the contradiction loses confidence in the page's accuracy at the exact moment they would otherwise convert; it may also affect how the page is perceived by Google's content-quality signals if crawled verbatim.
- **Likely Root Cause:** LIKELY a partial content update (e.g., the FAQ was refreshed to reflect a rule change but the earlier "Requirements" section was not updated in the same edit), a common WordPress/Elementor content-maintenance gap when a page has multiple independently-edited sections.
- **Recommended Fix:** Reconcile the two statements into one consistent, correctly-sourced figure (or explicitly note that the requirement varies/has changed, with a date), after professional verification of which statement is actually current (see report C's Financial/Regulated Content Accuracy Protocol — this audit does not assert which of the two figures is correct).
- **Manual Implementation Guide:** (1) In WordPress Admin, open the Public Limited Company page in Elementor. (2) Locate both the "Requirements" section text and the FAQ Q1 answer. (3) Confirm the currently correct rule with a qualified CA/company-law professional. (4) Edit both sections to state the same, verified figure (or explicitly frame one as historical if the rule changed at a specific date). (5) Save and republish.
- **Validation:** Re-fetch the live page and confirm both sections now state the same figure; have a second reviewer read the page end-to-end checking specifically for this contradiction before considering it resolved.
- **Confidence Level:** CONFIRMED (both conflicting sentences are directly quoted in the source evidence).
- **Evidence Source:** `data/crawl/_phase1b-batch2-tier1-review.md`.

### [HIGH] OP-002 — Possible mislabeled navigation link: "Limited Liability Partnership Registration" resolves to the compliance-only LLP Annual Filing page

- **Issue (Finding):** This session's fetch of `/llp-annual-filing/` reported a navigation-menu entry labeled "Limited Liability Partnership Registration" whose href resolved to that same URL — i.e., a nav link that reads like an LLP formation/registration link may actually route to a page scoped entirely to LLP annual compliance (Form 8/Form 11 filing), with no formation content anywhere on the destination page.
- **Severity:** HIGH. If confirmed, a visitor clicking a "Registration" nav link with the explicit intent to form an LLP lands on a page that cannot serve that intent at all — a direct, navigation-level intent mismatch on a priority service. Not CRITICAL because indexing/ranking are unaffected and the page itself is not broken; not MEDIUM because, if true, it silently fails every visitor with this specific, common intent.
- **Evidence:** `data/crawl/_phase1b-batch2-tier1-review.md`, LLP Annual Filing entry, "Internal Linking Opportunities": "this fetch's extraction reported a navigation-menu entry labeled 'Limited Liability Partnership Registration' whose href resolved to this same URL... This could not be independently re-verified within this session and may reflect an extraction artifact rather than the live site's actual markup." Cross-confirmed in `data/crawl/service-coverage-map.md` (LLP Registration entry): "A nav item reportedly reads 'Limited Liability Partnership Registration,' but no corresponding URL was found in the crawl inventory."
- **Affected URLs:** `https://cashahnawaz.com/llp-annual-filing/` (destination); the site's primary navigation (source, exact menu location not independently verified).
- **SEO Impact:** Organic Visibility and Qualified Traffic stages. If true, the site has no reachable LLP formation page at all, and its own navigation actively misroutes searchers with formation intent — compounding the confirmed content gap in report C (CONT-015).
- **Likely Root Cause:** NOT DETERMINED with current tool access — either a WordPress menu item was never updated after the page's scope was defined as compliance-only, or this is a WebFetch extraction artifact (a markdown-conversion mislabeling of the link text). Genuinely ambiguous without raw-HTML or admin verification.
- **Recommended Fix:** Verify the nav link's actual label and target directly in WordPress Admin (Appearance → Menus) or via browser view-source. If confirmed mislabeled, either retitle the nav item to "LLP Annual Filing / Compliance" (if no formation page will be built) or point it to a genuine LLP Registration page once one exists (see report C CONT-015).
- **Manual Implementation Guide:** (1) In WordPress Admin, go to Appearance → Menus (or the active theme/page-builder's mega-menu editor, per `internal-linking.md`'s guidance to confirm which system controls live navigation). (2) Locate the menu item currently labeled "Limited Liability Partnership Registration" (or similar). (3) Confirm its target URL. (4) If it points to `/llp-annual-filing/`, either relabel it accurately or retarget it once a dedicated LLP Registration page exists.
- **Validation:** Re-fetch the live site navigation (or view-source) and confirm the nav item's label now matches its destination page's actual scope.
- **Confidence Level:** LIKELY (not CONFIRMED — the source evidence explicitly flags this as unverified/possibly an extraction artifact, and this report does not upgrade that confidence without new evidence).
- **Evidence Source:** `data/crawl/_phase1b-batch2-tier1-review.md`; `data/crawl/service-coverage-map.md`.

### [MEDIUM] OP-003 — Inconsistent pricing disclosure across Tier 1 pages with no evident logic

- **Issue (Finding):** Only 2 of 13 Tier 1 pages (GST Registration: "Rs 1,500"; ITR Mumbai: "₹499 / ₹1,499 / ₹2,499" tiers) state an actual price. The other 11, including sibling pages to the two that do (GST Return Filing, all Registration & Compliance pages, NRI Taxation, Audit Services), withhold pricing behind a generic enquiry form — with no visible pattern (e.g., transaction complexity, service type) explaining which pages disclose and which don't.
- **Severity:** MEDIUM. Pricing transparency is a conversion-relevant content choice, not a mechanical defect; it does not block any success-journey stage outright, but the inconsistency itself (rather than the absence of pricing, which `content-audit.md` notes can be a deliberate, reasonable choice) is the issue — it reads as unplanned rather than intentional.
- **Evidence:** `data/crawl/_phase1b-batch1-tier1-review.md` Cross-Page Patterns: "Only 2 of 7 pages (GST Registration: Rs 1,500; ITR Mumbai: ₹499/₹1,499/₹2,499 tiers) state an actual price. GST Return Filing, NRI, Audit Services, and Accounting Services (despite a 'Charges' section header) all withhold pricing behind a generic enquiry form." Corroborated across all 6 pages in `_phase1b-batch2-tier1-review.md`: "no pricing disclosed on any of the 6 pages."
- **Affected URLs:** `/gst-return-filing/`, `/itr-filing-for-nri-guide-for-non-resident-taxation/`, `/accounting-services/`, `/audit-services/`, `/startup-registration-india/`, `/section-8-company-registration/`, `/public-limited-company/`, `/llp-annual-filing/`, `/tds-return-filing-services/`, `/12a-or-12aa-or-80g-registration-new-scheme/` (11 of 13 Tier 1 pages).
- **SEO Impact:** Engagement and Form Submission / Genuine Enquiry stages. Inconsistent pricing transparency creates unpredictable friction: a visitor who found pricing on one page and expects to find it on a related page (e.g., moving from GST Registration to GST Return Filing) is met with a "Get a Free Quote" wall instead.
- **Likely Root Cause:** LIKELY organic, page-by-page authorship over time without a sitewide content-standards decision on whether/where to publish pricing — consistent with the varying template families already noted in WP-001.
- **Recommended Fix:** Make one deliberate, sitewide decision — either (a) publish at least indicative pricing/fee ranges on all Tier 1 pages where feasible, or (b) standardize on quote-based pricing everywhere with consistent "why we quote individually" framing — rather than the current unexplained mix.
- **Manual Implementation Guide:** (1) Decide the firm's pricing-disclosure policy per service (a business decision, not an SEO one). (2) For pages that will publish pricing, add a pricing/package section matching the ITR Mumbai or GST Registration page's existing format. (3) For pages that will remain quote-based, add one sentence explaining why (e.g., "pricing varies by turnover/complexity — request a free quote") so the absence reads as intentional rather than incomplete.
- **Validation:** Re-fetch all 13 Tier 1 pages and confirm the pricing-disclosure pattern now matches the chosen policy consistently.
- **Confidence Level:** CONFIRMED (pricing presence/absence directly observed on all 13 pages across both batch files).
- **Evidence Source:** `data/crawl/_phase1b-batch1-tier1-review.md`; `data/crawl/_phase1b-batch2-tier1-review.md`.

### [HIGH] OP-004 — Homepage's own "TESTIMONIALS" section renders with no populated content

- **Issue (Finding):** The homepage carries a "TESTIMONIALS" H2 (also styled "What People Are Saying About Us"), but this session's fetch surfaced no actual testimonial text beneath it — in direct contrast to 4 other Tier 1 pages (GST Registration, GST Return Filing, ITR Mumbai, Accounting Services), which each display 4-6 named testimonials with quotes.
- **Severity:** HIGH. The homepage is the site's single highest-traffic entry point and primary trust surface per `data/crawl/priority-urls.md`; a visibly empty trust section on the first page most visitors see is a meaningful, high-visibility credibility gap, even though it does not block any technical function.
- **Evidence:** `data/crawl/_phase1b-batch1-tier1-review.md`, Homepage entry, "Issues Identified": "A 'TESTIMONIALS' H2 section... is present on the page, but the fetch surfaced no actual testimonial text under it... This is either a rendering issue in this fetch or a genuinely empty section on the homepage; either way it's the site's single highest-visibility page showing an apparently broken/empty trust section."
- **Affected URLs:** `https://cashahnawaz.com/`
- **SEO Impact:** Engagement and Form Submission / Genuine Enquiry stages — a first-time visitor evaluating whether to trust the firm sees a labeled but empty proof section at the point in the page journey designed specifically to build that trust.
- **Likely Root Cause:** NOT DETERMINED with current tool access — could be a genuinely empty Elementor testimonial widget (e.g., not configured to pull from the same source as the service-page widget), or a WebFetch rendering/extraction limitation specific to this widget type. Both are plausible; the audit cannot distinguish them without a rendered browser check.
- **Recommended Fix:** Confirm via a live browser view whether the section is genuinely empty. If empty, populate it with 2-3 of the same real testimonials already displayed elsewhere on the site (they already exist and are already approved for public display).
- **Manual Implementation Guide:** (1) Open the live homepage in a standard browser (not just admin preview) and scroll to the "TESTIMONIALS" section to confirm whether content is actually missing or just not rendering to WebFetch. (2) If missing, open the homepage in Elementor, locate the Testimonials widget, and either link it to the same data source as the service-page testimonial widget or manually add 2-3 existing testimonials. (3) Save and republish.
- **Validation:** Re-fetch/re-view the homepage and confirm testimonial content now displays under the "TESTIMONIALS" heading.
- **Confidence Level:** LIKELY (the section's emptiness is confirmed in this fetch, but whether that reflects the live rendered page or a tool limitation is not fully resolved — hence LIKELY, not CONFIRMED, per the source file's own framing).
- **Evidence Source:** `data/crawl/_phase1b-batch1-tier1-review.md`.

### [MEDIUM] OP-005 — Templated testimonial reuse across pages, with two Tier 1 pages carrying zero testimonials

- **Issue (Finding):** The same 6 named testimonials (Fazal Ali, Rohit Ukrande, Ayesha Sayyed, Homi Daruwalla, Raj Pandey, Qasim Farooqi) recur near-verbatim across GST Registration, GST Return Filing, ITR Mumbai, and Accounting Services, consistent with one shared sitewide widget rather than page-specific proof. Meanwhile, NRI Taxation and Audit Services — two Tier 1 pages — carry zero testimonials of any kind.
- **Severity:** MEDIUM. This is a genuine E-E-A-T/authenticity-perception issue (a repeated generic testimonial set reads as less credible than page-specific proof) and an uneven-coverage issue, but it does not misinform or block conversion outright.
- **Evidence:** `data/crawl/_phase1b-batch1-tier1-review.md`, Cross-Page Patterns: "The same 6 named testimonials... recur near-verbatim across GST Registration, GST Return Filing, ITR Mumbai, and Accounting Services... The NRI and Audit Services pages have none at all." Individually confirmed per-page: NRI entry states "**CONFIRMED TRUST GAP:** No testimonials of any kind on this page"; Audit Services entry states "No testimonials or case studies anywhere on this page, in contrast to Accounting/GST/ITR Mumbai pages."
- **Affected URLs:** `/gst-registration-online/`, `/gst-return-filing/`, `/income-tax-return-filing-in-mumbai/`, `/accounting-services/` (duplication); `/itr-filing-for-nri-guide-for-non-resident-taxation/`, `/audit-services/` (zero testimonials).
- **SEO Impact:** Engagement stage. Per `content-audit.md`, this is specifically noted as a concern precisely because NRI Taxation targets a higher-trust-barrier, remote audience least able to visit the firm in person — the page most in need of social proof has none.
- **Likely Root Cause:** LIKELY a shared Elementor testimonial widget applied uniformly to some page templates but not others, rather than a deliberate curation decision.
- **Recommended Fix:** Add page-relevant testimonials to NRI Taxation and Audit Services (only genuine, verifiable client testimonials — never authored/invented ones); where feasible, vary which testimonials appear on which service page rather than repeating the identical 6 everywhere.
- **Manual Implementation Guide:** (1) Identify any existing real testimonials from NRI or audit-engagement clients (if none exist yet, this becomes a client-outreach task outside SEO scope, not something to fabricate). (2) In Elementor, add a testimonial widget/section to the NRI Taxation and Audit Services pages. (3) For the 4 pages already sharing the identical 6 testimonials, consider curating a different subset per page if enough genuine testimonials exist.
- **Validation:** Re-fetch the two currently-zero pages and confirm testimonial content is now present; spot-check that testimonials shown are genuine and not duplicated verbatim on every page.
- **Confidence Level:** CONFIRMED (testimonial presence/absence directly observed per page across both batch files).
- **Evidence Source:** `data/crawl/_phase1b-batch1-tier1-review.md`.

### [MEDIUM] OP-006 — Homepage top-level CTA strip omits 3 of 5 CLAUDE.md priority-service groups

- **Issue (Finding):** The homepage's main mid-page CTA strip surfaces only 3 clickable nav-style CTAs — "Register A Company," "Income Tax Return Filing," "Accounting Services" — leaving GST Registration, GST Return Filing, and Audit Services (all explicit CLAUDE.md priority services) absent from top-level homepage prominence, reachable only via a fuller link list further down the page.
- **Severity:** MEDIUM. This is a within-page prominence/hierarchy issue, not an absence — every service is still reachable from the homepage — but it under-represents GST and Audit (2 of 5 priority groups) at the highest-visibility position on the highest-traffic page.
- **Evidence:** `data/crawl/_phase1b-batch1-tier1-review.md`, Homepage entry, "Issues Identified": "The homepage's main mid-page CTA strip only surfaces 3 services as clickable nav-style CTAs... GST Registration, GST Return Filing, and Audit Services (all explicit CLAUDE.md priority services) are not represented as top-level homepage CTAs, only inside the fuller 'One Stop Solution' link list further down."
- **Affected URLs:** `https://cashahnawaz.com/`
- **SEO Impact:** Organic Visibility (internal link-equity distribution) and Qualified Traffic stages — the homepage typically carries the most authority on a small-business site, and CTA-strip placement is a strong equity/attention signal that 2 of 5 priority groups currently don't receive.
- **Likely Root Cause:** LIKELY an original page-design decision (3 CTAs fits the visual layout) made before the full priority-service list was finalized or expanded.
- **Recommended Fix:** Expand the top CTA strip to represent all 5 CLAUDE.md priority groups (Income Tax, GST, Accounting, Audit, Registration & Compliance) at parity, or restructure it as a 5-item grid instead of 3.
- **Manual Implementation Guide:** (1) In Elementor, open the homepage and locate the CTA-strip widget/section currently showing "Register A Company," "Income Tax Return Filing," "Accounting Services." (2) Add "GST Registration" and "Audit Services" (or a suitable GST/Audit-group representative link) as additional items in the same visual pattern. (3) Save and republish.
- **Validation:** Re-fetch the homepage and confirm all 5 priority groups are represented in the top-level CTA strip.
- **Confidence Level:** CONFIRMED.
- **Evidence Source:** `data/crawl/_phase1b-batch1-tier1-review.md`.

### [MEDIUM] OP-007 — 12A/80G page's H1 is narrower than its actual page scope

- **Issue (Finding):** The page's H1 reads "12A Registration Online," but the page's own body content substantively covers 80G registration and 12AA/12AB re-registration as well — the H1 does not reflect the full breadth of what the page addresses.
- **Severity:** MEDIUM. This is a heading-hierarchy/on-page targeting issue, not a content-accuracy problem — the content itself is comprehensive; only the H1's framing under-represents it.
- **Evidence:** `data/crawl/_phase1b-batch2-tier1-review.md`, 12A/80G entry, "Issues Identified": "H1 ('12A Registration Online') is narrower than the page's own actual scope, which explicitly also covers 80G and 12AA/12AB — a heading-hierarchy/on-page-seo concern."
- **Affected URLs:** `https://cashahnawaz.com/12a-or-12aa-or-80g-registration-new-scheme/`
- **SEO Impact:** Organic Visibility stage — a searcher specifically querying "80G registration" may weight the H1 mismatch as a weaker relevance signal for that term than the page's actual content would justify.
- **Likely Root Cause:** LIKELY the H1 was written when the page's initial scope was narrower (12A only) and not revised as 80G/12AA content was added over time.
- **Recommended Fix:** Update the H1 to reflect the page's full scope (e.g., "12A, 12AA/12AB and 80G Registration Online" or similar, matching actual on-page terminology), consistent with the URL slug which already references all three.
- **Manual Implementation Guide:** (1) In WordPress/Elementor, open the page editor for the 12A/80G page. (2) Locate the H1 element (likely in the hero/header widget). (3) Update the text to include 80G and 12AA/12AB alongside 12A. (4) If using Rank Math, also review the page's SEO title field for the same narrowness (confirm current Rank Math title text live before editing, since it was not visible to this session's tools).
- **Validation:** Re-fetch the page and confirm the H1 now reflects the full scope; confirm no duplicate/conflicting H1 was introduced.
- **Confidence Level:** CONFIRMED.
- **Evidence Source:** `data/crawl/_phase1b-batch2-tier1-review.md`.

### [LOW] OP-008 — Misplaced sentence on the GST Registration page describing GST Return Filing timelines

- **Issue (Finding):** The GST Registration page contains the sentence "GST return filing takes around six to seven working days," describing what should logically be a *registration* turnaround, not *return filing* — reading as a copy/paste artifact likely carried over from the GST Return Filing page.
- **Severity:** LOW. This is a single-sentence content-clarity defect, not a structural or trust-level problem, but it is confusing for a reader specifically trying to learn how long registration itself takes.
- **Evidence:** `data/crawl/_phase1b-batch1-tier1-review.md`, GST Registration entry, "Issues Identified": "A body sentence reads: 'GST return filing takes around six to seven working days' — this appears on a GST Registration page describing what should logically be the registration turnaround, not 'return filing.' This reads as a copy/paste or template artifact."
- **Affected URLs:** `https://cashahnawaz.com/gst-registration-online/`
- **SEO Impact:** Engagement stage — minor, but a reader specifically evaluating "how long will this take" gets an answer for the wrong service, which can create confusion at the point of decision.
- **Likely Root Cause:** LIKELY a copy/paste artifact from the sibling GST Return Filing page during initial content authoring, never corrected.
- **Recommended Fix:** Either remove the sentence, correct it to state the registration-specific turnaround (only if a verified, accurate figure exists), or clarify the sentence's context if it was intentionally referencing a post-registration filing obligation.
- **Manual Implementation Guide:** (1) In Elementor, open the GST Registration page and locate this sentence via a page search for "six to seven working days." (2) Confirm with the firm what the actual GST registration turnaround is. (3) Replace the sentence with an accurate, correctly-labeled statement.
- **Validation:** Re-fetch the page and confirm the sentence now correctly describes registration turnaround (or has been removed).
- **Confidence Level:** CONFIRMED.
- **Evidence Source:** `data/crawl/_phase1b-batch1-tier1-review.md`.

---

## Cross-references

- Full content-quality evidence: `data/crawl/_phase1b-batch1-tier1-review.md`, `_phase1b-batch2-tier1-review.md`
- Service coverage detail: `data/crawl/service-coverage-map.md` / `.csv`
- Cannibalization/freshness detail: `data/crawl/_phase1b-cannibalization-and-freshness.md`
- Content-depth, freshness, gap, trust, and cannibalization findings (CONT-xxx): `reports/04-content-audit.md`
- Executive summary: `reports/03a-phase-1b-executive-summary.md`
- All findings tracked centrally in: `implementation/MASTER-ISSUE-TRACKER.md` (this report's IDs: OP-001 through OP-008)
