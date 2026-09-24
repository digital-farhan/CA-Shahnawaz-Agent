# Cashahnawaz SEO Audit Project

Evidence-based SEO audit and reporting workspace for **https://cashahnawaz.com/**, a WordPress-based CA / tax / compliance services website.

---

## Quick Start — how to run this project

This is a **Claude Code agent project**. Most of the work is done by asking Claude, not by running scripts. The scripts in `tools/` are optional helpers.

### Step 1 — Install what you need

| Need | Install |
|---|---|
| Python 3.10+ | [python.org/downloads](https://www.python.org/downloads/) |
| Claude Code | [claude.com/claude-code](https://claude.com/claude-code) |
| Git | [git-scm.com](https://git-scm.com/downloads) |

### Step 2 — Get the project

```bash
git clone https://github.com/digital-farhan/CA-Shahnawaz-Agent.git
cd CA-Shahnawaz-Agent
```

### Step 3 — Install Python packages

```bash
pip install -r requirements.txt
playwright install chromium
```

> `playwright install chromium` is only needed for speed tests and PDF export.

### Step 4 — Open with Claude Code

```bash
claude
```

Claude reads `CLAUDE.md` automatically — that file contains all the project rules.

### Step 5 — Ask for an audit

Just talk to it in plain English. Examples:

```
Audit the GST registration page in depth
Run a backlink opportunity hunt
Check which pages have outdated tax content
Create a client report as PPTX
```

Claude picks the right playbook from `skills/` on its own.

---

### Optional — connect Google Search Console / GA4

Only needed for real traffic data. Without it, Claude marks those figures `DATA NOT AVAILABLE` instead of guessing.

1. Create a **service account** in [Google Cloud Console](https://console.cloud.google.com/) and download the JSON key.
2. Grant that service-account email read access in Search Console and GA4.
3. Point the project at the key:

```bash
# Windows (PowerShell)
$env:GOOGLE_APPLICATION_CREDENTIALS = "C:\path\to\key.json"

# macOS / Linux
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"
```

4. Pull the data:

```bash
python tools/pull_google_data.py
```

---

### Optional — run the tools directly

```bash
python tools/crawl_site.py          # crawl the site      → data/crawl/
python tools/browser_audit.py       # speed + screenshots → data/performance/
python tools/validate_schema.py     # check schema markup
python tools/render_report.py       # Markdown report     → HTML
python tools/export_report_pdf.py   # HTML report         → PDF
```

---

### Where things go

| Folder | What's inside |
|---|---|
| `skills/` | The playbooks Claude follows |
| `data/` | Evidence — crawls, exports, backlinks |
| `reports/` | Finished reports you can send |
| `implementation/` | Fixes to make, tracked by severity |
| `automations/` | Recurring routines |

### One rule to know

**Claude never changes the live website.** It audits, finds issues and writes step-by-step instructions — you make the actual changes yourself. See the Implementation Policy in [CLAUDE.md](CLAUDE.md).

---

## What this project is — and is NOT

This is an **audit and reporting project only**. Claude's role here is SEO Auditor / Technical SEO Analyst / Website Researcher / Data Analyst / SEO Strategist / Audit Report Generator — never an implementer. Claude never makes live changes of any kind (WordPress pages/posts, Rank Math or Elementor settings, theme files, plugins, hosting, DNS, robots.txt, `.htaccess`, sitemap config, GSC/GA4/GTM configuration, or any other production system), **even if access to those systems becomes available.** The user implements every approved recommendation manually; Claude's job ends at handing over clear, correct, step-by-step manual guidance.

This is a working folder for Claude (and the user) to:

1. Audit the site across technical SEO, on-page, content, internal linking, schema, performance, WordPress-specific issues, local SEO, CRO, and competitor positioning.
2. Ground every finding in real evidence pulled from GSC, GA4, GTM, live crawls, and tool-based performance tests — never invented data.
3. Produce clear, evidence-backed findings with manual implementation guidance the user can execute themselves, tracked through to completion by severity.
4. Eventually roll everything up into one consolidated, client-presentable final SEO Audit Report (Markdown evidence → one HTML report → a print-ready PDF, in that order — see CLAUDE.md's "Final Audit Deliverable" section for the full 24-section structure).

See [CLAUDE.md](CLAUDE.md) for the full set of project rules, the **Implementation Policy (audit-only, permanent, non-negotiable)**, the required finding template, severity definitions, and business context (priority services, competitors, success funnel). Read that file first — it governs how all work in this project must be done.

## Folder Structure

```
cashahnawaz-seo-audit/
│
├── CLAUDE.md                  Project rules, business context, finding template
├── README.md                  This file
│
├── skills/                    Audit playbooks — one per audit discipline
│   │
│   │   ── On-site & analytics (the original foundation)
│   ├── technical-seo.md
│   ├── website-crawl.md
│   ├── gsc-analysis.md
│   ├── ga4-analysis.md
│   ├── gtm-conversion-audit.md
│   ├── on-page-seo.md
│   ├── content-audit.md
│   ├── internal-linking.md
│   ├── schema-audit.md
│   ├── wordpress-seo.md
│   ├── performance-audit.md
│   ├── competitor-analysis.md
│   ├── local-seo.md
│   ├── cro-audit.md
│   │
│   │   ── Orchestration & governance
│   ├── seo-growth-orchestrator.md   Master skill — sequences everything below
│   ├── off-page-governance.md       Scoring rubric, REJECT list, approval gates
│   │
│   │   ── Off-page authority & acquisition
│   ├── off-page-seo.md
│   ├── backlink-opportunity-hunter.md
│   ├── competitor-backlink-gap.md
│   ├── broken-link-building.md
│   ├── backlink-reclamation.md
│   ├── backlink-risk-monitor.md
│   ├── digital-pr-outreach.md
│   │
│   │   ── Content & linkable assets
│   ├── digital-pr-link-assets.md
│   ├── linkable-content-planner.md
│   ├── content-decay-refresh.md
│   │
│   │   ── Entity, trust & intelligence
│   ├── local-citation-authority.md
│   ├── entity-seo.md
│   ├── eeat-ymyl-authority.md
│   ├── ai-search-visibility.md
│   ├── seo-opportunity-mining.md
│   └── serp-intelligence.md
│
├── automations/               Recurring runbooks (run in-session — no scheduler exists)
│   └── daily-backlink-hunt.md
│
├── data/                      Raw/processed pulls — the evidence backing every finding
│   ├── crawl/                 Site crawl outputs
│   ├── gsc/                   Search Console exports
│   ├── ga4/                   GA4 exports
│   ├── gtm/                   GTM container/tag inventories
│   ├── competitors/           Competitor site analysis outputs
│   ├── backlinks/             Backlink CRM, citations, entity record, outreach log
│   │   └── snapshots/         Dated snapshots — enables new/lost link analysis
│   ├── serp/                  SERP snapshots for the fixed keyword set
│   ├── ai-search/             Answer-engine question set and spot-check results
│   └── performance/           Core Web Vitals / PageSpeed / Lighthouse outputs
│
├── reports/                    Finished, user-facing audit reports
│   ├── daily-backlink-report.md
│   ├── weekly-authority-report.md
│   └── monthly-seo-growth-report.md
│
└── implementation/             Approved fixes, tracked by severity
    ├── critical/
    ├── high-priority/
    ├── medium-priority/
    └── opportunities/
```

### The off-page / authority layer

The skills under *Orchestration*, *Off-page authority*, *Content & linkable assets*, and *Entity, trust & intelligence* extend this project from an on-site audit into a full **SEO Growth & Authority System**. Two things govern all of them:

- **[seo-growth-orchestrator.md](skills/seo-growth-orchestrator.md)** is the entry point. It sequences every other skill and answers *"what is the highest-impact SEO action we can take next?"* — never *"what can we automate next?"*
- **[off-page-governance.md](skills/off-page-governance.md)** holds the 100-point opportunity scoring rubric, the prohibited-tactics REJECT list (no PBNs, no spam, no bought links, no fake profiles or citations, no anchor manipulation), velocity control, and the approval gates. Every off-page skill defers to it, so the rules exist in exactly one place.

**These skills prepare; they never execute.** Discovery, qualification, scoring and drafting are automated aggressively. Every outward-facing action — sending outreach, submitting a directory listing, editing a profile, publishing a page, filing a disavow — is prepared in full and handed to the user, who performs it manually. This follows CLAUDE.md's Implementation Policy, which overrides any "automatically allowed" instruction from any specification.

Two constraints shape what these skills can honestly produce today: **no backlink-data tool and no GSC/GA4 connectors** were available at the last verified capability check (`reports/00-capability-check.md`). Backlink totals, referring-domain counts, DA/DR values, traffic estimates and query-level data are therefore `DATA NOT AVAILABLE` rather than estimated. What remains fully available — and is where these skills do their real work — is direct observation: fetching pages, verifying links and their targets, checking claims against primary sources, and comparing competitor ecosystem placements.

## How to use this project

1. **Start of any session:** verify actual tool/connector access (GSC, GA4, GTM, crawling, WordPress) before relying on it — see the "Capability Inspection" step in project setup. Connectivity claimed by the user is not the same as connectivity confirmed by a working tool call. Access to a system (e.g., WordPress Admin) is for verification/evidence only — never a green light to change anything.
2. **Pick the relevant skill(s)** from `skills/` before starting a given type of audit.
3. **Pull real data** into the matching `data/` subfolder as you go, so every finding is traceable to a source.
4. **Write findings** into `reports/` using the required template from CLAUDE.md (Issue/Finding, Severity, Evidence, Affected URLs, SEO Impact, Likely Root Cause, Recommended Fix, **Manual Implementation Guide**, Validation).
5. **Claude never implements anything live, ever** — not automatically, not after approval, not even for a trivial one-line change. Approval of a finding means "this is correct and worth acting on," not "go make the change." The user performs every implementation step manually.
6. **Once the user has manually implemented a fix,** update its status under the matching `implementation/<severity>/` folder (or `implementation/MASTER-ISSUE-TRACKER.md`), and use the finding's Validation steps to help the user confirm the change worked — validation is a check, not an implementation.
7. **Working toward the final deliverable:** as phases complete, their Markdown reports accumulate toward one consolidated, client-presentable final SEO Audit Report — first as an HTML report, then (only after the user reviews the HTML) a print-ready PDF. See CLAUDE.md's "Final Audit Deliverable" section for the full structure and the design palette to use consistently.

## Status

Audit in progress across multiple phases (Phase 0 discovery, Phase 1A technical/WordPress audit, Phase 1B on-page/content audit). See `reports/` for completed phase reports and `implementation/MASTER-ISSUE-TRACKER.md` for the consolidated, currently-tracked findings. No live-site changes have been made or ever will be made by Claude in this project — see CLAUDE.md's Implementation Policy.
