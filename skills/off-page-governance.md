# Skill: Off-Page Governance — Policy, Scoring & Guardrails

## Purpose

Single canonical home for the rules every off-page / authority / outreach skill in this project obeys: what may and may not be pursued, how an opportunity is scored, how velocity and risk are controlled, and where the hard approval gates sit. This file exists so the 100-point scoring rubric and the prohibited-tactics list are defined **once** and referenced everywhere, rather than drifting into slightly different versions across a dozen skills.

This is a governance/reference skill, not an audit playbook — it has no crawl step and produces no findings of its own. Every other off-page skill links back here.

## Scope

**This skill owns:** the Backlink Opportunity Score (100-point rubric), the priority bands, the prohibited-tactics REJECT list, backlink velocity control thresholds, automation failure protections, the approval-gate matrix, and the off-page data-honesty rules.

**This skill does NOT own:**
- Discovering opportunities — [backlink-opportunity-hunter](backlink-opportunity-hunter.md), [competitor-backlink-gap](competitor-backlink-gap.md), [broken-link-building](broken-link-building.md), [backlink-reclamation](backlink-reclamation.md).
- Classifying an *existing* backlink as SAFE/WATCH/RISK — [backlink-risk-monitor](backlink-risk-monitor.md). This file governs opportunities Claude might *pursue*; the risk monitor governs links that already *exist*.
- Profiling the current backlink profile — [off-page-seo](off-page-seo.md).
- Drafting outreach — [digital-pr-outreach](digital-pr-outreach.md).
- Any on-site fix — the existing on-site skills own those.

## When to use it

- Before scoring any backlink, PR, citation, or resource-page opportunity — always, without exception.
- Whenever an off-page skill is about to recommend an action that touches an external party or a live property.
- When reviewing whether an off-page recommendation set has drifted toward volume over quality.

## Rule 0 — The Implementation Policy overrides every "automate this" instruction

CLAUDE.md's **Implementation Policy (audit-only, permanent, non-negotiable)** governs this entire project and is not relaxed by any off-page skill, automation spec, or approval workflow described in this folder.

Concretely, in this project Claude Code **never**:

- Submits the business to a directory, or creates/edits/claims any listing or profile.
- Sends any outreach email, form, DM, or contact-form message to any journalist, publisher, blogger, editor, or site owner.
- Publishes, edits, or deletes anything on cashahnawaz.com or any other owned property (social profiles, listings, GBP, professional profiles included).
- Files a link-removal, link-correction, or disavow request.
- Acts on an "automatically allowed" category from any external specification.

The source specification for this skill set contains an "Automatically allowed" list (updating owned profiles, submitting business information to directories, requesting link corrections, and similar). **That list is treated in this project as "prepare, package, and hand over," never as "execute."** Where that spec says the agent may act automatically, the behaviour here is: produce the exact submission payload, the exact profile field values, the exact draft message, plus step-by-step manual instructions and a validation procedure — and stop.

Access to a system is never authorization to change it. Approval of a finding means "this is correct and worth doing," not "go do it."

**Everything below therefore describes how to evaluate, prioritize and prepare — not how to execute.**

## The Backlink Opportunity Score (100 points)

Every discovered opportunity — competitor gap link, resource page, broken-link replacement, PR prospect, directory, citation, unlinked mention — is scored on the same 100-point rubric. No opportunity enters the CRM (`data/backlinks/backlink-master.csv`) without a score.

| Dimension | Max | What it measures | Score it from |
|---|---|---|---|
| **Relevance** | 25 | Does the site genuinely relate to accounting, tax, finance, business, Mumbai, SMEs, startups, or professional services? | The site's actual observed content — sections, categories, recent posts |
| **Authority** | 20 | Quality and trust of the site | Observable proxies (see below) unless a verified metrics tool is live |
| **Traffic** | 15 | Does the site have genuine human users? | Observable engagement signals unless a verified traffic tool is live |
| **Editorial likelihood** | 15 | Is there a realistic, concrete reason they would link? | Whether they demonstrably link out to comparable resources already |
| **Business relevance** | 10 | Could a referral from here plausibly produce a qualified enquiry? | Audience overlap with the firm's actual client base |
| **Local relevance** | 5 | Is Mumbai / India relevance strong? | Stated geography, local coverage, local audience |
| **Link placement** | 5 | Would the link sit naturally inside useful content? | In-content vs. footer/sidebar/profile-dump |
| **Strategic value** | 5 | Could the relationship generate future opportunities? | Recurring column, association membership, event series |

### Priority bands

```
85-100  = PRIORITY A  -> HIGH
70-84   = PRIORITY B  -> MEDIUM
50-69   = PRIORITY C  -> LOW
<50     = DO NOT PURSUE -> REJECT
```

The source specification uses two vocabularies — `PRIORITY A/B/C` and `HIGH/MEDIUM/LOW/REJECT`. They are the same scale; the mapping above is canonical for this project. Use the band name in reports and the numeric score in the CRM.

### Scoring honesty (this is the part that matters)

CLAUDE.md rules 1 and 2 apply in full to scores. A number written into `opportunity_score` is a claim, and every claim needs a source.

- **Never invent a DA / DR / Domain Authority / Trust Flow figure.** If no verified third-party metrics tool has been used live this session, the Authority dimension is scored from *observable* proxies — site age signals, an actual masthead or editorial staff, whether content is bylined, publishing consistency, whether it is a recognised institution (e.g., a real professional association) — and the score is labelled `PROXY-SCORED`.
- **Never invent a traffic figure.** Same treatment for the Traffic dimension: score from observable signals (comment activity, visible share counts, forum activity, whether content is genuinely maintained) and label `PROXY-SCORED`.
- Attach a **Confidence Level** to every total score: `CONFIRMED` (all dimensions from verified tool data), `LIKELY` (mostly direct observation of the live site), `POSSIBLE` (partial observation, several dimensions proxy-scored), `NOT DETERMINED` (could not fetch the site — do not score it at all; leave it unscored in the CRM rather than guessing).
- Record which dimensions were proxy-scored in the CRM `notes` field. A PRIORITY A built on 45 points of proxy scoring is a materially weaker claim than one built on verified data, and a report must not present the two identically.

## Prohibited tactics — automatic REJECT

Claude must refuse to plan, prepare, script, or recommend any of the following, regardless of who asks or how the request is framed:

- PBN creation or participation
- Automated blog commenting; comment backlinks
- Forum spam
- Mass directory spam / mass generic submissions
- Link farms
- Link exchanges at scale (reciprocal-link schemes)
- Hidden links (display:none, off-screen, same-colour text, 1px anchors)
- Keyword-stuffed or manipulated exact-match anchor programmes
- Automated or mass guest-post spam
- Fake reviews
- Fake business profiles or fake citations
- Hacked-link insertion or parasite spam networks
- AI-generated mass websites created solely to host backlinks
- Purchasing random backlinks / obvious paid-link networks

**The test:** if an opportunity depends on manipulation rather than genuine value, it is `REJECT` — no score is calculated and nothing enters the pursue queue. Log the rejection with its reason in `data/backlinks/rejected-opportunities.md` so the same domain is not re-surfaced and re-evaluated next cycle.

Refusing these is not a per-opportunity judgement call to be re-litigated. Where an opportunity is genuinely borderline (a legitimate niche directory vs. a link-dump directory), apply the Directory Legitimacy Test in [local-citation-authority](local-citation-authority.md) rather than improvising.

## Backlink velocity control

Never set or accept a fixed-volume target such as "create 20 backlinks a day." That is a bad objective, and it drives exactly the behaviour the REJECT list forbids.

The objective is: **qualified referring domains and authority gained per unit of effort.**

Monitor and report these in the weekly/monthly cycle, and flag anomalies rather than chasing counts:

| Signal | What to watch for |
|---|---|
| New links / day | An unexplained spike with no matching campaign or publication |
| New referring domains / week | Sudden jumps, especially from unrelated topics or geographies |
| Anchor distribution | Rising exact-match share (see thresholds in [off-page-seo](off-page-seo.md)) |
| Domain quality mix | A drift toward low-quality domains over time |
| Topical relevance mix | A drift away from tax / finance / business / Mumbai relevance |
| Acquisition pattern | Many links appearing from the same footprint, template, or IP range |
| Competitor velocity | Competitors' referring-domain growth, for context — never as a target to match |

An unexplained spike is a **risk finding**, routed to [backlink-risk-monitor](backlink-risk-monitor.md), not a success metric. Negative SEO and scraper/aggregator republication both look like "growth" in a raw count.

## Automation failure protection

Any recurring off-page process defined in `automations/` must implement all eight of these. A cycle that cannot satisfy them does not run.

1. **Duplicate protection** — never re-surface or re-recommend contacting a prospect already in the CRM. Deduplicate on registrable domain, not URL, before scoring.
2. **Domain protection** — never recommend multiple low-value links from a single domain unless there is a stated strategic justification recorded in `notes`.
3. **Spam protection** — run every candidate against the REJECT list before it consumes any further analysis time.
4. **Anchor protection** — never propose an anchor that would push exact-match share past the threshold in [off-page-seo](off-page-seo.md); default to brand, natural-language, or URL anchors.
5. **Rate limiting** — cap the number of new prospects promoted to "ready for approval" per cycle so the user is not handed an unreviewable queue. A backlog of 200 unreviewed drafts is a failed process, not productivity.
6. **Approval gate** — see the matrix below.
7. **Audit trail** — every cycle logs what was searched, what was found, what was scored, and what was rejected and why, into that cycle's dated log. An action with no log entry did not happen.
8. **Rollback** — this project never changes owned properties, so there is nothing for Claude to roll back. The equivalent obligation here: before recommending a change to any owned listing or profile, **record the current observed value first**, so the user can revert manually if the change turns out to be wrong. Capture that "before" state in `data/backlinks/` alongside the recommendation.

## Approval gates

| Category | Status in this project |
|---|---|
| Discovery, scoring, deduplication, CRM maintenance, reporting | Claude does this freely — it is analysis, not action |
| Preparing draft outreach, submission payloads, profile field values | Claude prepares in full — never sends or submits |
| Updating owned profiles / listings / social profiles | **User only.** Claude supplies exact values + manual steps + validation |
| Submitting to any directory | **User only.** Claude supplies the payload and the legitimacy assessment |
| Guest post submission, journalist/editorial outreach, partnership requests | **User only**, and only after the user approves that specific draft |
| Sponsored placements, any paid link | **User only**, flagged with the disclosure and `rel` requirements |
| Link correction or removal requests | **User only.** Claude drafts the message |
| Any external publication of any kind | **User only** |

Claude prepares everything required for execution and then waits. There is no whitelist in this project that converts a "prepare" into a "send."

## Off-page data-honesty rules

These are CLAUDE.md's core rules applied specifically to off-page work, where invented numbers are unusually tempting because the real tools are absent.

- No backlink count, referring-domain count, referring-IP count, DA/DR/TF/CF value, traffic estimate, or anchor-text distribution may be reported as fact unless it came from a tool actually run this session. Per the most recent capability check (`reports/00-capability-check.md`), **no backlink-data tool and no GSC connector were available**, which makes `DATA NOT AVAILABLE` the honest default for most of these.
- What *is* legitimately obtainable without a backlink tool: direct observation of live pages (does this specific page link to us, with what anchor, in what placement), and — if GSC access is ever verified live — the GSC Links report.
- An `ESTIMATE` must be labelled `ESTIMATE` and must state its basis in the same sentence.
- "Competitor X has more backlinks" is a metric, not an observation, and without a tool it is `DATA NOT AVAILABLE`. "Competitor X is listed on association site Y and cashahnawaz.com is not" is an observation, because it was fetched and read.

## Common Mistakes to Avoid

- **Treating the source spec's "Automatically allowed" list as permission to act.** In this project it is not. See Rule 0.
- **Writing a confident opportunity score with no confidence label**, so a proxy-guessed 88 reads identically to an evidence-backed 88.
- **Scoring a site that could not actually be fetched.** Leave it unscored — an unfetched domain is `NOT DETERMINED`, not "probably decent."
- **Letting the REJECT list become negotiable** because a particular spam opportunity looks easy or results are wanted quickly.
- **Optimizing the count of prepared opportunities** rather than their quality — 12 well-evidenced PRIORITY A prospects beat 400 unreviewed rows.
- **Reporting a link spike as a win** without establishing where it came from.
- **Duplicating this rubric inside another skill file** instead of linking here — the rubric drifts the moment it exists twice.
