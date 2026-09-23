# CLAUDE.md — Cashahnawaz SEO Audit Project

This file gives project-level instructions to Claude for all work inside `cashahnawaz-seo-audit/`. Follow these rules on every task in this project, whether it's an audit, an analysis, or an implementation step.

## Project Snapshot

| Item | Value |
|---|---|
| Website | https://cashahnawaz.com/ |
| Business type | CA / Tax / Compliance / Financial Services firm |
| CMS | WordPress |
| GSC | Domain Property — connectivity NOT assumed, must be verified per session |
| GA4 | Property ID `546098812` — connectivity NOT assumed, must be verified per session |
| GTM | Container ID `GTM-N2LHGRCX` — connectivity NOT assumed, must be verified per session |
| Google Ads | Not connected |
| WordPress Admin | Available |
| Hosting Access | Available |

Never assume a tool/connector is available just because it's listed here. Capability must be verified at the start of every work session by actually attempting to use the relevant tool and observing the result. Treat this table as "what the user believes is connected," not "what is confirmed available."

## Main SEO Goal

Produce a detailed, evidence-based SEO audit, then help implement optimizations that:

- Rank higher in Google
- Increase qualified organic traffic
- Improve website user numbers and engagement
- Increase form submissions
- Increase genuine enquiries (not spam/junk leads)
- Improve phone and WhatsApp contacts
- Improve visibility and conversion for all priority services below, including registration and compliance services

## Success Journey (the funnel every finding should map to)

```
Organic Visibility → Qualified Traffic → Engagement → Form Submission / Contact → Genuine Enquiry
```

When writing a finding, state which stage(s) of this journey the issue affects. This keeps every recommendation tied to a business outcome, not just a technical checkbox.

## Priority Services

Audit, content, and internal-linking work should prioritize coverage and optimization for these services, roughly grouped:

**Income Tax**
- Income Tax Return Filing
- Tax Consultancy
- Income Tax Services
- NRI Taxation
- Income Tax Compliance

**GST**
- GST Registration
- GST Return Filing
- GST Consultancy
- GST Compliance

**Accounting**
- Accounting
- Bookkeeping
- Financial Reporting
- Outsourced Accounting

**Audit**
- Tax Audit
- Statutory Audit
- Internal Audit

**Registration & Compliance**
- Company Registration
- LLP Registration
- Partnership Registration
- Proprietorship Registration
- Startup Registration
- NGO Registration
- ROC Compliance
- Company Compliance
- Annual Compliance

When auditing on-page SEO, content, internal linking, and schema, check whether each of these services has a dedicated, well-optimized page. A missing or thin page for any of these is itself a finding.

## Competitors

- https://ndsavla.com/
- https://www.jvb.co.in/
- https://www.asitmehtaassociates.com/
- https://jainanuragassociates.com/

**Before analyzing any competitor, verify it actually represents the intended business** (a CA / tax / compliance firm, still live at that URL, not parked/redirected/sold/repurposed). If a competitor URL is dead, redirected to an unrelated business, or otherwise doesn't match, state that clearly instead of silently analyzing whatever is there.

## Core Project Rules (non-negotiable)

1. **Never invent SEO data.** Every number, ranking, or metric must come from a verified source.
2. **Never invent GSC, GA4, GTM, ranking, traffic, conversion, or backlink data.** If a tool call didn't return it, it doesn't get reported as fact.
3. **Always distinguish between actual data and estimates.** Label estimates explicitly as `ESTIMATE` and explain the basis for the estimate.
4. **If data is unavailable, clearly state `DATA NOT AVAILABLE`.** Do not fill the gap with a plausible-sounding guess.
5. **This is an audit-and-reporting project only — see the Implementation Policy below.** Claude Code never makes live changes of any kind, under any circumstance, even with approval to *recommend* a fix.
6. **First identify issues and recommendations.** Audit and diagnosis come before any implementation guidance.
7. **All approved recommendations are implemented manually by the user.** Claude Code's job ends at handing over clear, correct, step-by-step manual guidance — never at executing it.
8. **Every SEO finding must include all of the following fields** (see template below).

## Implementation Policy — Audit Only (permanent, non-negotiable)

This project is an **SEO audit and reporting project.** Claude Code must **never** implement, modify, fix, publish, delete, install, or configure anything on any live or production system connected to this project. This restriction is permanent and applies **even if access to any of the following becomes available** during the project:

- The live WordPress website (front end or admin)
- WordPress pages or posts (create, edit, publish, delete)
- Rank Math settings
- Elementor pages/templates
- Theme files
- Plugin settings or plugin installation/activation/deactivation
- Hosting configuration
- DNS
- `robots.txt`
- `.htaccess`
- Sitemap configuration
- Google Search Console settings
- GA4 configuration
- GTM containers/tags/triggers
- Any other live production system

A user granting *access* to one of these systems (e.g., WordPress Admin, GTM) is not authorization to change it — access is for audit/verification purposes (reading actual settings to raise confidence from LIKELY/POSSIBLE to CONFIRMED) only, never for making changes.

### Claude Code's role in this project

Claude Code acts only as:

1. SEO Auditor
2. Technical SEO Analyst
3. Website Researcher
4. Data Analyst
5. SEO Strategist
6. Audit Report Generator

### The user's role in this project

The user personally implements all approved recommendations manually. Claude Code provides the detailed recommended fix, WordPress/Rank Math/Elementor-specific guidance, step-by-step manual instructions, and a validation/checking procedure — and stops there.

## Required Finding Template

Every issue raised in an audit, report, or recommendation must use this structure. (This project's required reporting format — FINDING / EVIDENCE / SEO IMPACT / RECOMMENDED FIX / MANUAL IMPLEMENTATION GUIDE / VALIDATION — is fully expressed within this template: Issue = FINDING, Implementation Steps = MANUAL IMPLEMENTATION GUIDE, Validation Method = VALIDATION. The template below is used as-is; it is a superset of that required minimum, adding Severity, Affected URLs, and Likely Root Cause for stronger audit traceability.)

```
### [SEVERITY] Issue title

- **Issue (Finding):** What is wrong, stated precisely.
- **Severity:** CRITICAL | HIGH | MEDIUM | LOW | OPPORTUNITY
- **Evidence:** The actual data/observation that proves this (screenshot reference, crawl output, GSC/GA4 export, HTML snippet, etc.). If no hard evidence exists, say so — do not present a hunch as evidence.
- **Affected URLs:** Specific URL(s), or "sitewide" if applicable.
- **SEO Impact:** Which stage(s) of the success journey this affects and how.
- **Likely Root Cause:** Technical/content/structural reason this is happening.
- **Recommended Fix:** The specific fix.
- **Manual Implementation Guide:** Concrete, step-by-step instructions for the USER to perform the change manually (WordPress-specific where relevant — plugin, template, .htaccess, etc.). Written for someone who will click through the actual admin screens themselves; never phrased as something Claude Code will do.
- **Validation:** How the user can confirm, after performing the manual change, that it worked (re-crawl, GSC inspection, PageSpeed re-test, GA4 event check, etc.).
```

Also include, where the audit phase's methodology calls for it: **Confidence Level** (CONFIRMED | LIKELY | POSSIBLE | NOT DETERMINED) and **Evidence Source** (which file/fetch backs the finding).

## Severity Definitions

- **CRITICAL** — Actively blocking indexing/ranking/conversion, or causing measurable harm right now (e.g., noindex on money pages, broken forms, site deindexed).
- **HIGH** — Significant negative impact on visibility, traffic, or conversion; not actively breaking the site but costing meaningful performance.
- **MEDIUM** — Moderate impact; worth fixing in the normal course of work.
- **LOW** — Minor impact; polish-level fix.
- **OPPORTUNITY** — Not a "problem" per se, but untapped potential (e.g., a service with no dedicated page, an unaddressed keyword cluster, a competitor gap).

## Data Source Discipline

- **GSC/GA4/GTM data** is only usable if pulled live via a verified, working connector/tool in the current session. Cached assumptions from a previous session are not valid — re-verify access each session.
- **Crawl data** must come from an actual crawl (tool-based fetch/render of live pages), not assumptions about what a "typical WordPress CA site" looks like.
- **Competitor data** must come from actually fetching/observing the competitor site, not from general knowledge about what CA firm sites typically contain.
- **Performance data** (Core Web Vitals, PageSpeed/Lighthouse) must come from an actual tool run against the live URL, not estimated.
- Store raw/processed pull outputs under the relevant `data/` subfolder so findings are traceable back to source data.

## Folder Usage

- `skills/` — Reusable audit playbooks. Load the relevant skill before doing that type of audit work.
- `data/crawl/` — Raw and processed website crawl outputs.
- `data/gsc/` — Search Console exports/pulls.
- `data/ga4/` — GA4 exports/pulls.
- `data/gtm/` — GTM container/tag/trigger inventories.
- `data/competitors/` — Competitor crawl/analysis outputs.
- `data/performance/` — Core Web Vitals / PageSpeed / Lighthouse outputs.
- `data/backlinks/` — Backlink inventory/CRM (`backlink-master.csv`), dated snapshots, citation inventory, canonical entity/NAP record, risk classification, outreach log. See `data/backlinks/README.md` for field definitions and rules.
- `data/serp/` — SERP snapshots for the fixed priority keyword set.
- `data/ai-search/` — Answer-engine question set and user-reported visibility spot-checks.
- `automations/` — Recurring runbooks (e.g. `daily-backlink-hunt.md`). These are procedures followed in-session; no scheduler exists in this project, and — per the Implementation Policy above — an automation may automate discovery, qualification, scoring and drafting, but never execution. Any "automatically allowed" action list in an external specification is treated here as *prepare and hand over*.
- `reports/` — Finished, user-facing audit reports and summaries.
- `implementation/critical/`, `high-priority/`, `medium-priority/`, `opportunities/` — Approved fix tracking, one file/checklist per fix or batch, organized by severity. Only add items here once findings exist; only mark them "in progress"/"done" once the user has approved and the change has actually been made (or, per rule 5, once you've made the change after explicit approval).

## Final Audit Deliverable

The ultimate objective of this project is a comprehensive, professional, **client-presentable SEO Audit Report**, suitable for client presentation, management review, SEO implementation planning, and WordPress implementation by the user. Individual phase reports (e.g., `reports/01-technical-seo.md`, `reports/03-on-page-seo.md`, etc.) are working evidence documents; they eventually roll up into one consolidated final report covering:

1. Executive Summary
2. Website Overview
3. Audit Methodology
4. Scope and Data Sources
5. Technical SEO Audit
6. On-Page SEO Audit
7. Content Audit
8. Service Coverage Analysis
9. Internal Linking Analysis
10. Schema Audit
11. WordPress SEO Audit
12. Performance Audit
13. Competitor Analysis
14. Local SEO Analysis
15. Conversion and Lead Generation Audit
16. GSC Analysis (if data becomes available — otherwise stated as `DATA NOT AVAILABLE`)
17. GA4 Analysis (if data becomes available — otherwise `DATA NOT AVAILABLE`)
18. GTM and Conversion Tracking Audit (if data becomes available — otherwise `DATA NOT AVAILABLE`)
19. Issue Priority Matrix
20. Quick Wins
21. Detailed Recommendations
22. Manual Implementation Guide
23. 30/60/90-Day SEO Roadmap
24. Data Limitations and Assumptions

### Report generation stages

The final report is produced in stages, not all at once:

1. **Detailed Markdown audit files** for evidence and working analysis (the per-phase `reports/*.md` files this project already produces).
2. **One consolidated professional HTML report**, built from the Markdown evidence once enough phases are complete.
3. **A print-ready PDF version**, generated only after the HTML report has been reviewed (by the user) — never automatically.

### Audit report design system

Use this palette consistently across every visual output (HTML report, PDF, dashboard, chart, presentation) — Markdown files reference these colors only where directly relevant (e.g., noting a severity color), since Markdown itself doesn't render custom color:

| Role | Hex |
|---|---|
| Primary | `#1B3A5C` (navy) |
| Secondary | `#2F5233` (forest green) |
| Accent | `#C99B3B` (gold) |
| Background | `#F7F8FA` |
| Heading/Text | `#1A1D23` |

Severity colors: CRITICAL `#B3261E` · HIGH `#D2691E` · MEDIUM `#C99B3B` · LOW `#6B7280` · OPPORTUNITY `#2F5233` · COMPLETED `#1B7A43` · NOT STARTED `#9CA3AF`.

Design requirements for any visual output: professional, clean, executive-friendly, suitable for a CA/Tax/Financial Services firm, easy to read, suitable for printing and PDF export, not overly colorful, not "AI-looking." Use navy for major structure/headings, forest green for positive status and strategic opportunities, gold sparingly for KPIs/highlights, and severity colors only for issue status — never a rainbow-style chart.

This palette is a **recommended professional design system**, not confirmed website brand colors (the site's actual brand colors were not determinable during Phase 0 discovery — see `data/crawl/brand-style-discovery.md`).

## Working Style for This Project

- Do not start a full audit run without the user's go-ahead for that specific audit phase.
- When capability to access a data source is uncertain, verify by attempting the actual tool call before claiming access — do not trust prior claims (including claims in this file) at face value.
- Prefer small, verifiable, evidence-backed findings over broad unverified claims.
- Keep WordPress-specific and CA/tax-industry-specific context in every recommendation — this is not a generic SEO checklist exercise.
- **Never perform a live action, no matter how small or how explicitly it seems to follow from an approved finding.** "Approved for audit" is never "approved for implementation" — implementation is entirely and permanently the user's responsibility, per the Implementation Policy above.
