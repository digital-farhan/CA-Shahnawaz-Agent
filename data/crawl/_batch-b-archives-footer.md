# Batch B — Category/Taxonomy Archives + Footer-Unmatched Links (Raw Evidence)

Fetched via WebFetch (HTML→markdown AI extraction). Per the known tool limitation, `<head>`-level
fields (title, meta robots, canonical) are inconsistently surfaced by this tool and were NOT VISIBLE
in every fetch below despite repeated, explicit prompting for them. Body-level content (H1, nav,
post listings, forms) was reliably surfaced. No HTTP status codes are stated anywhere below because
WebFetch does not expose raw status codes to this agent — all outcomes are described qualitatively
based on what content was actually rendered/summarized.

**General caveat on redirects (applies to all 3 Part 2 URLs):** WebFetch's own tool description states
it silently follows same-host redirects and only explicitly flags a redirect when the destination is a
*different host*. None of the 3 footer-link fetches below reported a cross-host redirect notice from the
WebFetch tool layer itself. However, the AI summarization step for each fetch separately asserted "no
redirect detected" — that claim is based only on the markdown content handed to the summarizer, not on
inspecting the actual HTTP redirect chain, so it is NOT a reliable confirmation that the browser-level
request stayed on the literal requested path. In other words: we cannot fully distinguish "this exact
URL genuinely serves this content natively" from "this URL silently 301/302-redirected to another
same-host URL that serves this content, and the tool simply didn't surface that it happened." This
ambiguity is flagged per-URL below rather than resolved, per instructions not to guess/invent status
codes or redirect mechanics.

---

## Part 1 — Category/Taxonomy Archives

### URL: https://cashahnawaz.com/income-tax/
- Category: Archive
- Fetch Result: SUCCESS
- Title Evidence: NOT VISIBLE
- Meta Robots Evidence: NOT VISIBLE
- Canonical Evidence: NOT VISIBLE
- H1 Evidence: NOT VISIBLE
- Content type observed: archive listing — 9 distinct posts observed, reverse-chronological, with pagination controls and nav/footer elements typical of a WordPress category archive. Posts observed: "When Can I Expect My ITR Refund?" (04/07/2026), "June 2026 Important Due dates | Income Tax | GST | MCA | Other Law" (01/06/2026), "Dos and Don'ts for Salaried person's ITR" (01/06/2026), "Allotment letter and bank payment saves from addition under Section 56(2)(x)" (26/05/2026), "Best Time to file ITR FY 2025-26" (15/05/2026), "The Ultimate Real Estate Tax Guide for Buyers in India" (11/05/2026), "TDS chart for FY 2026-27" (07/05/2026), "Bank Transaction Limits Explained | Income Tax & GST Rules" (06/05/2026), "The Ultimate Guide to Form 10BD: NGO Compliance" (02/05/2026).
- Notes: Genuine multi-post taxonomy archive; no thin-content indication. All posts topically match "Income Tax."

### URL: https://cashahnawaz.com/gst/
- Category: Archive
- Fetch Result: SUCCESS
- Title Evidence: NOT VISIBLE
- Meta Robots Evidence: NOT VISIBLE
- Canonical Evidence: NOT VISIBLE
- H1 Evidence: "GST Related Blogs - Shahnawaz and Associates Consultancy Services"
- Content type observed: archive listing — 10 distinct posts observed, reverse-chronological (01/06/2026 down to 28/09/2021), with "Older Posts →" pagination link. Posts observed: "June 2026 Important Due dates | Income Tax | GST | MCA | Other Law", "Waiver of Late Fees for GST Annual Return", "Big Relief for Taxpayers whose GST Number got canceled due to non Filing of GST returns", "GST AMNESTY SCHEME 2023", "How to file GST Registration – Process, Benefits and Penalty", "Recommendations of GST Council are only recommendatory and not binding on Union and State", "GST Registration Services India: A Guide To GST", "GSTR-2B – GST ITC can be claimed or available only when reflected in GSTR 2A/2B", "Important of GST And Other Due Date Calendar Month Of October 2021", "Things to keep in mind while filing GSTR 1 and GSTR 3B".
- Notes: Genuine multi-post archive spanning ~4.5 years of content; no thin-content indication. All posts topically match "GST."

### URL: https://cashahnawaz.com/mca/
- Category: Archive
- Fetch Result: SUCCESS
- Title Evidence: NOT VISIBLE
- Meta Robots Evidence: NOT VISIBLE
- Canonical Evidence: NOT VISIBLE
- H1 Evidence: "MCA Relaxation for Filling E-Forms for FY 2020-21"
- Content type observed: only 1 item listed ("MCA Relaxation for Filling E-Forms for FY 2020-21", dated 14/02/2022), followed by "End of content" / "No more pages to load" text. Rest of page is repeated nav menus and footer.
- Notes: THIN — this archive resolves to only a single post despite being a top-level footer/nav taxonomy ("MCA" is a named service category — Registration & Compliance is a priority service group per project scope). Does not read as a genuine multi-post archive; effectively presents as a single-item category with no further content behind it.

### URL: https://cashahnawaz.com/accounting-services-blog/
- Category: Archive
- Fetch Result: SUCCESS
- Title Evidence: NOT VISIBLE
- Meta Robots Evidence: NOT VISIBLE
- Canonical Evidence: NOT VISIBLE
- H1 Evidence: NOT VISIBLE (page displays text "Accounting Services Blog: Expert Advice, Tips, And Tricks" but the fetch could not confirm this is an actual `<h1>` tag vs. site branding/header text — recorded as NOT VISIBLE per instructions not to guess)
- Content type observed: archive listing — 8 distinct posts observed, reverse-chronological, spanning August 2022 to February 2023. Posts observed: "What is the Role of Accounting Within A Company?", "What Is An MIS Report? Definition, Types, Importance And Benefits", "Important Accounting Principles to know while writing Books of Accounts", "Important Accounting Concepts to Ensure Proper Accounting of Financial data", "Common Accounting Errors and How to Prevent Them – An Ultimate Guide", "What Is Business Accounting? 21 Tips For Business Owners", "The Best Accounting Software for Small Businesses in 2023", "Finalisation of Accounts – 9 Things You Must Never Miss Out".
- Notes: Genuine multi-post archive; no thin-content indication. Note: newest post dated Feb 2023 — no accounting-topic posts newer than that appear in this archive, despite the sitemap inventory showing an accounting-tagged item ("what-is-an-mis-report...") with a much later lastmod (2026-07-22); not resolved here, flagged for the synthesis pass.

### URL: https://cashahnawaz.com/others/
- Category: Archive
- Fetch Result: SUCCESS
- Title Evidence: NOT VISIBLE
- Meta Robots Evidence: NOT VISIBLE
- Canonical Evidence: NOT VISIBLE
- H1 Evidence: NOT VISIBLE
- Content type observed: archive listing — 10 distinct posts observed, reverse-chronological (04/02/2026 down to 05/11/2022). Posts observed: "Structural Overhaul and Legislative Calibration: An In-Depth Analysis of the Finance Bill 2026", "Charitable Trusts Alert: Its Time to Reapply for Tax Exemption Before 30th Sep", "SEBI Interim Order Against Gensol Engineering Ltd: A Deep Dive into Corporate Governance Failures", "Notes Section 8 Company and Trust", "Dematerialization of Shares", "Guidance Note on provisions of Direct Tax Vivad se Vishwas Scheme, 2024", "Old vs New Tax Regime: Which Tax System is Better for Salaried Employees", "Memorandum Explaining the Provisions in the Finance Bill 2023", "Taxation of Corporations and Businesses", "Due Date Calendar for the Month of November, 2022".
- Notes: Genuine multi-post archive; topically it's a miscellany/catch-all bucket ("Others") spanning corporate governance, trusts, tax regimes, due dates — consistent with an "uncategorized/other" taxonomy rather than thin content. No thin-content indication by volume, but topical coherence is low (expected for a catch-all category).

### URL: https://cashahnawaz.com/donation/
- Category: Archive
- Fetch Result: SUCCESS
- Title Evidence: NOT VISIBLE
- Meta Robots Evidence: NOT VISIBLE
- Canonical Evidence: NOT VISIBLE
- H1 Evidence: "Reporting of Statement of Donation Form 10BD"
- Content type observed: only 1 item listed ("Reporting of Statement of Donation Form 10BD", dated 17/05/2022). Page presents as effectively a single static article with surrounding nav/footer/contact-form chrome rather than a multi-item listing.
- Notes: THIN — single-post archive, same pattern as /mca/. No pagination or "more posts" content observed beyond the one article.

### URL: https://cashahnawaz.com/gst-case-law/
- Category: Archive
- Fetch Result: SUCCESS
- Title Evidence: NOT VISIBLE
- Meta Robots Evidence: NOT VISIBLE
- Canonical Evidence: NOT VISIBLE
- H1 Evidence: "GST Case Law"
- Content type observed: archive listing — 10 distinct posts observed, reverse-chronological (dated around September 2025 per the fetch), with "Older Posts →" pagination link indicating further pages exist. Posts observed: "Supreme Court Clarifies GST Summons vs Proceedings", "Allahabad HC Quashes GST Confiscation for Excess Stock", "Kerala HC: No GST Penalty for ITC Reporting Errors", "Allahabad HC: GST Demand Beyond Show-Cause Notice Quashed", "Gujarat HC: Refund of Compensation Cess ITC Allowed on Coal Used for Exports", "Patna HC on Section 77 Refunds: Wrong Head GST Payment Refund Allowed", "Bombay HC GST Ruling 2025 | GST Cash Credit Account Relief", "Sikkim HC Allows Refund of ITC on Business Closure", "Madras HC Quashes Composite GST Show Cause Notices", "Gujarat HC Quashes GST Demand Against Dissolved Company".
- Notes: Genuine multi-post archive with confirmed pagination beyond page 1; no thin-content indication. All posts topically match "GST Case Law."

---

## Part 2 — Footer-Linked URLs Not Found in Sitemap (Live-Check)

### URL: http://cashahnawaz.com/project-business/trademark-registration/
- Category: Footer-Unmatched-Link
- Fetch Result: SUCCESS (content returned; redirect status genuinely uncertain — see general caveat above)
- Title Evidence: NOT VISIBLE
- Meta Robots Evidence: NOT VISIBLE
- Canonical Evidence: NOT VISIBLE
- H1 Evidence: "Trademark Registration Process"
- Content type observed: appears to be a live single service page about trademark registration for "Shahnawaz and Associates" — nav menus, contact info, a lead-capture contact form (name/email/phone/service selection), footer with social links and copyright. Does not resemble a 404/not-found page.
- Notes: The AI summarizer explicitly stated "No redirect detected — the URL structure remains consistent throughout the provided content," but per the general caveat this claim is not a reliable confirmation of the literal request path (WebFetch only explicitly flags cross-host redirects; same-host redirects to e.g. the sitemap's `/trademark-registration/` would not necessarily be surfaced). Content topic (trademark registration) is consistent with both this footer URL's slug and the sitemap's `/trademark-registration/` page, so this fetch cannot distinguish "this exact `/project-business/trademark-registration/` path is a live, separate, valid page" from "this path silently redirects to the sitemap's `/trademark-registration/` page." Recorded as live/reachable content; redirect mechanics UNKNOWN/NOT CONFIRMABLE with this tool.

### URL: http://cashahnawaz.com/income-tax-return-filling-in-mumbai/
- Category: Footer-Unmatched-Link
- Fetch Result: SUCCESS (content returned; redirect status genuinely uncertain — see general caveat above)
- Title Evidence: "Income Tax Return Filing In Mumbai | ITR Filing Services"
- Meta Robots Evidence: NOT VISIBLE
- Canonical Evidence: NOT VISIBLE
- H1 Evidence: "Income Tax Return Filing In Mumbai | ITR Filing Services"
- Content type observed: appears to be a live, fully-built service page — tax rate tables for FY 2025-26 and FY 2026-27, residential status explanation, income-head breakdowns, pricing tiers (₹499–₹2,499), testimonials, contact forms. Does not resemble a 404/not-found page.
- Notes: The title/H1 text returned here ("Income Tax Return Filing In Mumbai | ITR Filing Services") is consistent with what the correctly-spelled sitemap URL `/income-tax-return-filing-in-mumbai/` would be expected to show. The AI summarizer stated "No automatic redirect to the corrected URL path was observed" and "the URL maintains its original form with the 'filling' typo" — but per the general caveat this is not a confirmed HTTP-level determination. It is equally consistent with this misspelled URL silently redirecting (same-host) to the correctly-spelled canonical page and the tool not surfacing that. Cannot confirm whether this typo URL is a genuinely separate live/duplicate page or a silent redirect target resolving to the correct page. Redirect mechanics UNKNOWN/NOT CONFIRMABLE with this tool.

### URL: http://cashahnawaz.com/online-tds-return-filing/
- Category: Footer-Unmatched-Link
- Fetch Result: SUCCESS (content returned; redirect status genuinely uncertain — see general caveat above)
- Title Evidence: "TDS Return Filing Services In Mumbai | Expert CA Support"
- Meta Robots Evidence: NOT VISIBLE
- Canonical Evidence: NOT VISIBLE
- H1 Evidence: "TDS Return Filing Services"
- Content type observed: appears to be a live, fully-built service page — "What is TDS?", "When should TDS be deducted?", step-by-step online filing guidance, quarterly due dates, penalty info, FAQ section, contact forms. Does not resemble a 404/not-found page.
- Notes: The AI summarizer's own wording was internally inconsistent: it stated "The content structure aligns with the `/tds-return-filing-services/` path found in sitemaps" while simultaneously stating "No redirect was detected — this appears to be the native page location." Those two statements are in tension (content matching the sitemap's different-slug page is itself circumstantial evidence of a redirect to that page, not evidence against one). Per the general caveat, the summarizer's redirect assessment is based only on markdown content, not an inspected HTTP chain. Cannot confirm whether `/online-tds-return-filing/` is a separate live page or silently redirects (same-host) to the sitemap's `/tds-return-filing-services/`. Redirect mechanics UNKNOWN/NOT CONFIRMABLE with this tool.
