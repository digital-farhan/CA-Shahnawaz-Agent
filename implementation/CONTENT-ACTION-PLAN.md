# Content Action Plan — cashahnawaz.com

**Source:** Every OP-xxx finding in `reports/03-on-page-seo.md` and every CONT-xxx finding in `reports/04-content-audit.md`, generated Phase 1B, session date 2026-08-27. TECH-xxx/WP-xxx findings from Phase 1A are tracked in `implementation/MASTER-ISSUE-TRACKER.md` and not re-grouped here (that phase's own report already prioritized them; see `reports/01a-phase-1a-executive-summary.md` Section 11 for its quick-wins list).

**Prioritization basis:** Every item below is grouped by commercial importance, missing coverage, existing weakness, user-demand relevance (informational judgment only, `SEARCH DEMAND DATA NOT AVAILABLE`), conversion relevance, internal-linking value, and freshness/regulatory risk — **explicitly NOT by word count or page length.** A short, accurate fix (e.g., correcting one wrong sentence) can rank CRITICAL; a long, well-written page with no defects can rank LOW or OPPORTUNITY.

No fix has been implemented for any item below, per CLAUDE.md's Implementation Policy — Audit Only. All items are pending user action. Every "Manual Implementation Guide" referenced is in the source finding in `reports/03-on-page-seo.md` or `reports/04-content-audit.md` — this plan does not restate full implementation steps, only the priority grouping and a one-line action summary.

---

## CRITICAL (8 items) — regulatory/trust risk or dominant-service coverage gap; act first

| ID | Issue | Why CRITICAL |
|---|---|---|
| CONT-001 | Wrong firm name ("TAXZONA Consultancy") in Accounting Services FAQ | Active, present-tense credibility failure on a Tier 1 commercial page; single-sentence fix |
| CONT-014 | No dedicated Private Limited Company Registration page | Dominant entity type, zero coverage, confirmed by two independent fetches |
| CONT-002 | ITR Mumbai FAQ cites stale "Assessment Year 2020-21" | Flagship Income Tax page; internally-inconsistent stale compliance rule |
| CONT-003 | LLP Annual Filing "Final Year 2021-22" table/threshold framing | Live compliance page presenting a 5-cycle-old year as current |
| CONT-004 | 12A/80G page presents passed 2021-2022 transitional deadlines as current | Site's only NGO tax-exemption page; misleading deadline framing |
| CONT-005 | `/gst-new-update-due-dates-for-october-2021/` — no disclaimer, ~5 years stale | Confirmed-stale, indexed, no archival notice |
| CONT-006 | `/due-date-calendar-for-the-month-of-november-2022/` — no disclaimer | Confirmed-stale, indexed, no archival notice |
| CONT-007 | `/waiver-of-late-fees-for-gst-annual-return/` — waiver window closed March 2025 | Article's own text confirms the described benefit no longer available |

**Action sequence recommended:** Fix CONT-001 first (lowest effort, highest immediate trust impact) same day. Route CONT-002/003/004 to a qualified CA/tax professional for verification and relabeling as one batch (all three need the same kind of review). Add historical-reference notices to CONT-005/006/007 (mechanical, no professional review needed for the notice itself). Begin the CONT-014 content brief in parallel — it is the longest-lead-time item in this tier.

---

## HIGH PRIORITY (12 items) — significant visibility/trust/conversion cost, not yet actively misleading

| ID | Issue |
|---|---|
| OP-001 | Public Limited Company page self-contradicts on minimum paid-up capital |
| OP-002 | Possible mislabeled "LLP Registration" nav link resolving to compliance-only page |
| OP-004 | Homepage's "TESTIMONIALS" section renders empty |
| CONT-008 | `/key-recommendations-of-45th-gst-council-meeting/` needs historical-record framing |
| CONT-010 | `/old-vs-new-tax-regime-.../` tax-slab table has no FY/AY label anywhere |
| CONT-011 | Consolidated "Income Tax Act 2025" section-mapping review across 3 pages |
| CONT-012 | 5 Tier 1 pages state monetary thresholds/penalties with no currency date-stamp |
| CONT-015 | No dedicated LLP Registration (formation) page |
| CONT-016 | No dedicated Proprietorship Registration page |
| CONT-017 | Internal Audit — thin one-row mention only on Audit Services |
| CONT-018 | No company-side ROC/Company/Annual Compliance landing page(s), despite confirmed demand |
| CONT-019 | No dedicated Tax Consultancy page or lead category |

**Action sequence recommended:** OP-001, OP-002, and OP-004 first (fast, on-page fixes, no content-brief lead time). CONT-011 and CONT-012 next as one consolidated professional-review engagement (both are "verify figures/citations" tasks that can share the same review session). The five coverage-gap items (CONT-015/016/017/018/019) should be sequenced by lead time: CONT-017 (expand an existing page) is fastest; CONT-015/016/018/019 (new pages) should be planned as one content-production batch alongside CONT-014 from the CRITICAL tier, since they share the same Registration & Compliance / Tax Consultancy content-planning work.

---

## MEDIUM PRIORITY (10 items) — moderate impact, address in normal work cadence

| ID | Issue |
|---|---|
| OP-003 | Inconsistent pricing disclosure across Tier 1 pages |
| OP-005 | Templated testimonial reuse; NRI and Audit Services have zero testimonials |
| OP-006 | Homepage CTA strip omits 3 of 5 priority-service groups |
| OP-007 | 12A/80G page H1 narrower than actual page scope |
| CONT-009 | `/june-2026-important-due-dates/` still featured past relevance window |
| CONT-013 | Sitewide E-E-A-T gap — no individually-named CA credential |
| CONT-020 | Partnership Registration — informational content only, no service page |
| CONT-021 | GST Consultancy & GST Compliance — consolidated content gap |
| CONT-022 | Income Tax Compliance — no page distinguishing it from ITR Filing |
| CONT-023 | Unverified possible third GST-registration-related URL (verify first, then act) |

**Action sequence recommended:** CONT-023 first — it's a 5-minute browser check that determines whether this item escalates (if the URL is live and substantive) or resolves itself (if broken/redirecting). OP-003/005/006/007 are all page-content edits achievable within normal content-maintenance cadence. CONT-020/021/022 should be sequenced after the HIGH-tier Registration & Compliance content batch, since they're lower commercial volume but benefit from the same content-planning effort already underway.

---

## LOW PRIORITY (1 item)

| ID | Issue |
|---|---|
| OP-008 | Misplaced "GST return filing takes six-seven days" sentence on the GST Registration page |

**Action sequence recommended:** Fix opportunistically the next time the GST Registration page is edited for any other reason; does not warrant a dedicated maintenance pass on its own.

---

## OPPORTUNITY (enhancement-only items — no defect, no confirmed gap; documented for completeness, not formal findings)

These are drawn directly from `data/crawl/service-coverage-map.md`'s own `OPPORTUNITY`-rated rows and the batch-review files' explicitly-labeled opportunity notes. None represent a confirmed problem — they are optional expansions the user may choose to pursue for incremental gain.

- **Standalone Bookkeeping landing page** — currently well-covered as a subsection of Accounting Services; a dedicated page is a possible long-tail SEO expansion, not a fix (`service-coverage-map.md`, Bookkeeping entry).
- **Standalone Financial Reporting landing page** — same basis as above (`service-coverage-map.md`, Financial Reporting entry).
- **Income Tax Services pillar-page architecture** — consider whether a dedicated pillar page linking to ITR Filing, Tax Consultancy, NRI Taxation, and Income Tax Compliance would better serve broad "income tax services" queries than relying on the ITR Filing page to do double duty; this is a future content-architecture decision, not a current defect (`service-coverage-map.md`, Income Tax Services entry).
- **Tax Audit / Statutory Audit title-tag consideration** — both share one URL/page; on-page-seo.md should evaluate in a later phase whether a title/keyword-targeting split is warranted, since the content itself is already well-differentiated (`service-coverage-map.md`, Statutory Audit entry).
- **Homepage FAQ section** — not expected on every homepage, but could serve brand/trust-level queries (`_phase1b-batch1-tier1-review.md`, Homepage entry).
- **Named team/founder bios and quantified experience statistics** — only if verified true figures exist; currently the site makes no quantified trust claims beyond "110+ companies" on the Accounting page (`_phase1b-batch1-tier1-review.md`, Homepage entry).
- **Worked examples/illustrative calculations** (e.g., a GST registration threshold scenario, a TDS deduction walkthrough) — flagged as opportunities only across multiple pages; per `content-audit.md`, do not author these with invented figures — any worked example must use professionally-verified numbers.
- **Accounting blog cluster consolidation** — 8 articles cluster tightly around "accounting/bookkeeping basics"; consider a pillar-page/topic-cluster restructuring for long-term topical authority, even though the individual articles are not currently duplicative (`_phase1b-cannibalization-and-freshness.md`, Overlap #4).

---

## Summary counts

| Tier | Count |
|---|---|
| CRITICAL | 8 |
| HIGH PRIORITY | 12 |
| MEDIUM PRIORITY | 10 |
| LOW PRIORITY | 1 |
| OPPORTUNITY (formal findings) | 0 (8 informal enhancement items documented above) |
| **Total formal findings (OP + CONT)** | **31** |

## Cross-references

- `reports/03-on-page-seo.md` — full OP-xxx finding detail
- `reports/04-content-audit.md` — full CONT-xxx finding detail
- `reports/03a-phase-1b-executive-summary.md` — phase summary
- `implementation/MASTER-ISSUE-TRACKER.md` — consolidated tracker, all phases
