# Conversion Entry Point Discovery — cashahnawaz.com

Session date: 2026-08-27
Scope: Homepage, footer, Contact Us page, and the 9 individually-fetched Tier 1 service pages (GST Registration, GST Return Filing, Income Tax Return Filing, Accounting Services, Audit Services, Startup Registration, Section 8 Company, Public Limited Company, LLP Annual Filing).

**Every item below is labeled VISIBLE ON PAGE (with the exact text/href observed) and carries a separate, explicit TRACKING STATUS: UNKNOWN note.** This phase does not check GTM/GA4 event tracking — that is gtm-conversion-audit.md's job in a later phase. No item here should be read as "confirmed tracked" or "confirmed converting."

## 1. Phone / Click-to-Call

- **VISIBLE ON PAGE:** `tel:+919819267015` and a secondary formatted variant `tel:098192%2067015` — both link to the same number, `+91 98192 67015`. Observed on: Homepage, Contact Us, GST Registration Online, GST Return Filing, Income Tax Return Filing, Accounting Services, Audit Services, Startup Registration, Section 8 Company Registration, Public Limited Company, LLP Annual Filing (i.e., present sitewide on every page individually checked).
- **TRACKING STATUS: UNKNOWN.**

## 2. Email

- **VISIBLE ON PAGE:** `mailto:ca.shahnawazshaikh@gmail.com`. Observed on: Homepage, Contact Us.
- **TRACKING STATUS: UNKNOWN.**

## 3. WhatsApp / wa.me

- **NOT FOUND.** No `wa.me` link or WhatsApp-branded button was surfaced on the homepage, footer, Contact Us page, or any of the 9 individually-fetched Tier 1 service pages. Given CLAUDE.md's explicit goal to "improve phone and WhatsApp contacts," this is a notable gap — recorded here factually; severity/diagnosis belongs to cro-audit.md or local-seo.md in a later phase.
- A `chatway/v1` REST namespace was found in `/wp-json/` (see wordpress-fingerprint.md), suggesting a live-chat widget plugin (Chatway) may be installed. **POSSIBLE** this could be presented as a chat entry point on-page, but no chat widget element was actually observed in any fetched page's visible content this session — script-injected widgets are a known WebFetch blind spot, so its absence from this extraction is not proof it isn't live on the actual rendered page.

## 4. Contact / Enquiry Form

- **VISIBLE ON PAGE:** A recurring enquiry form appears multiple times per page (homepage and every Tier 1 service page fetched), with fields: Name, Email, Mobile Number, City, and a "Select Service" dropdown (options include Company Incorporation, GST Registration, LLP Registration, Public Limited Company, One Person Company, Startup Registration, Trademark Registration, 12A/12AA/80G Registration, Business Registration, Accounting Services, GST Return Filing, Income Tax Return Filing, TDS Return Filing, Annual Compliance for OPC, LLP Annual Compliance, Private Limited Company Annual Compliances, Section-8 Annual Compliance), plus a Submit button. The form does not appear to be pre-contextualized per page (e.g., the GST Registration page's form still shows the full generic service dropdown rather than defaulting to "GST Registration") — recorded as an observation only, no CRO judgment made here.
- Exact underlying form plugin (Contact Form 7 vs. Forminator — both are installed per the fingerprint) could not be determined from the rendered markup this session (no distinguishing CSS class surfaced).
- **TRACKING STATUS: UNKNOWN.** Whether form submission fires a GA4/GTM conversion event was not checked this phase.

## 5. Header / Sticky CTAs

- **VISIBLE ON PAGE:** "GET IT NOW" button, appearing at or near the top of every page checked (popup trigger, linking to a modal enquiry form, referenced via Elementor popup action parameters, e.g. popup ID 1132).
- **TRACKING STATUS: UNKNOWN.**
- Whether this button is "sticky" (remains visible while scrolling, especially on mobile) could **NOT be determined** — this requires rendered/visual confirmation, which is unavailable this session (no browser automation/screenshot capability). Flagged as a limitation, not a finding.

## 6. Homepage-Specific CTAs

- **VISIBLE ON PAGE:** "Book a Free Enquiry" (popup trigger), "Register A Company", "Income Tax Return Filing", "Accounting Services", "Contact us", "Make An Appointment" (popup trigger), "View All →" (due-dates link), "View All Tax Guides".
- **TRACKING STATUS: UNKNOWN** for all.

## 7. Service-Page CTAs

- **VISIBLE ON PAGE (consistent pattern across all fetched Tier 1 pages):** "GET IT NOW" (repeated), "Submit" (form button), occasional "get a quote" hyperlink text (seen on GST Registration Online page).
- **TRACKING STATUS: UNKNOWN.**

## 8. Social Profile Links (footer)

- **VISIBLE ON PAGE (footer):** Instagram (`https://www.instagram.com/ca.shahnawaz/`), LinkedIn (`https://www.linkedin.com/in/cashahnawazshaikh/`), Facebook (`https://www.facebook.com/shahnawazandassociates`), YouTube (`https://www.youtube.com/@shahnawazandassociates`). These are brand/social presence links, not direct lead-generation conversion points, but recorded here for completeness since they appear alongside the footer's conversion-adjacent content.
- **TRACKING STATUS: UNKNOWN.**

## 9. Map Embed

- **NOT FOUND.** No map embed was detected on the Contact Us page in this session's fetch. A physical office address was found as plain text: "Ground Floor, Grace Plaza, C-18, Swami Vivekanand Rd, near Railway Station, Momin Nagar, Jogeshwari West, Mumbai, Maharashtra 400102."

## Summary table

| Conversion element | Found this session? | Where observed |
|---|---|---|
| Phone / tel: link | Yes | Sitewide (all 11 pages individually fetched) |
| Email / mailto: link | Yes | Homepage, Contact Us |
| WhatsApp / wa.me link | **No** | Not found anywhere checked |
| Contact/enquiry form | Yes | Sitewide (all 11 pages individually fetched) |
| Header/popup CTA ("GET IT NOW") | Yes | Sitewide |
| Sticky mobile CTA | Not determinable | Requires rendered/visual check (unavailable) |
| Live chat widget | Possible (plugin namespace only) | Not visibly confirmed on any fetched page |
| Map embed | No | Not found on Contact Us page |

Every row's tracking status is UNKNOWN — this file records visibility only.
