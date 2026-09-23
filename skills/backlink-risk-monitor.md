# Skill: Backlink Quality & Risk Monitor

## Purpose

Classify every discovered backlink as **SAFE/VALUABLE**, **WATCH**, or **RISK**, detect anomalous acquisition patterns, and give the user a clear, evidenced picture of whether the link profile carries genuine risk — without the reflexive panic that leads firms to disavow perfectly ordinary links.

Most links most sites acquire are harmless. Google's algorithms ignore the majority of spam links rather than penalising for them. This skill exists to identify the genuine exceptions and, equally importantly, to prevent overreaction to the rest.

## Scope

**This skill owns:** classification of *existing* backlinks, anomaly and velocity-spike detection, negative-SEO assessment, and the risk register.

**This skill does NOT own:**
- Evaluating opportunities the firm might *pursue* — [off-page-governance](off-page-governance.md) owns the REJECT list for prospective links. This skill judges links that already exist and were not chosen.
- Profile composition and anchor distribution generally — [off-page-seo](off-page-seo.md), which supplies the inventory this skill classifies.
- Recovering broken or lost links — [backlink-reclamation](backlink-reclamation.md).
- Finding new links — [backlink-opportunity-hunter](backlink-opportunity-hunter.md).
- Any live action, including disavow submission — the user decides and acts.

## When to use it

- On every backlink discovery cycle — classification is not optional, per the specification.
- When an unexplained spike in links or referring domains appears.
- When anchor text drifts toward commercial exact-match.
- If the site experiences an unexplained ranking drop and other causes ([technical-seo](technical-seo.md), [content-decay-refresh](content-decay-refresh.md), [serp-intelligence](serp-intelligence.md)) have been excluded.
- Before the user considers any disavow — this skill supplies the evidence for that decision.

## Required Data

- The backlink inventory from [off-page-seo](off-page-seo.md) / `data/backlinks/backlink-master.csv`.
- Dated snapshots in `data/backlinks/snapshots/`, for velocity and anomaly detection.
- Fetch capability, to inspect linking pages directly.
- GSC Links report and any manual-action notice, if GSC is ever available.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- **Direct inspection of any linking page** — the strongest evidence available for classification. Fetching a page and reading it tells you far more about whether it is a link farm than any metric would.
- Observable spam signals on the page: scraped or machine-generated text, unrelated multilingual link blocks, casino/pharma/adult adjacency, hidden or stuffed link lists, no discernible audience, template footprints repeated across domains.
- **GSC manual action notices**, if GSC access is verified live — the only authoritative statement that Google has actually penalised the site. Its absence is meaningful information.
- Velocity comparison across this project's own dated snapshots.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Spam scores, toxicity scores, or any vendor risk metric.** No such tool exists here, and these metrics are vendor heuristics rather than Google signals in any case. Never produce a "toxicity score."
- A complete backlink profile, without a backlink tool (`reports/00-capability-check.md` confirms none). Risk assessment is therefore over the *known* subset, and must be labelled as such.
- **Whether Google has devalued or penalised any link.** Unknowable without a manual action notice. Algorithmic devaluation is invisible by design.
- Whether a ranking change was caused by links — not isolable.
- Who created a spam link, or whether it was deliberate negative SEO.
- Velocity trends without at least two dated snapshots.

## Pre-Audit Checks

1. Establish coverage: how much of the profile is known, and by what means. A risk statement over a hand-verified sample is a statement about that sample.
2. Check whether GSC is available; if it is, **check for a manual action first** — its presence or absence changes everything that follows.
3. Load prior snapshots to determine whether velocity analysis is possible at all.
4. Load [off-page-governance](off-page-governance.md)'s velocity thresholds.

## Step-by-Step Audit Process

### Step 1 — Classify every known link

Fetch each linking page and assign exactly one class, recording the observed evidence.

**SAFE / VALUABLE** — all of: topically relevant; editorial rather than injected; a genuine website with real content; a plausible real audience; natural placement in useful content; contextually meaningful. These need no action beyond monitoring for loss.

**WATCH** — legitimate but weaker or ambiguous: low apparent traffic; weak topical relevance; directory listings; user-generated content; sponsored placements; anything with a manipulative *appearance* without clear evidence. WATCH is not a problem — it is a category that gets re-checked. Most directory and profile links belong here permanently and require nothing.

**RISK** — evidenced spam: link farms; PBN footprints; spam websites; automated or machine-generated pages; casino/porn/pharma spam; hacked pages; malware sites; obvious paid-link networks; mass-generated sites. Requires observed evidence on the page, not an impression from the domain name.

Record for each: URL, class, the specific observed signals, anchor, target, date. Classification without recorded evidence is an opinion, and it is exactly what leads to unnecessary disavows.

### Step 2 — Look for patterns, not just individual links

Individual spam links are normal for any site. Patterns are what matter:

- Many domains sharing a template, footer, or hosting footprint.
- A cluster appearing in a narrow window with no matching activity.
- Repeated commercial exact-match anchors across unrelated domains — the strongest signal of either a manipulative campaign or negative SEO.
- Links from a single unrelated topical cluster (e.g., a sudden set of gambling-adjacent domains).
- Sitewide links from one domain across thousands of pages.

### Step 3 — Velocity and anomaly detection

Where snapshots allow, monitor the [off-page-governance](off-page-governance.md) signals: new links/day, new referring domains/week, anchor distribution shift, domain quality drift, topical relevance drift, acquisition pattern, competitor velocity.

**An unexplained spike is a risk signal, not a win.** Before treating growth as success, establish its cause: a publication, a campaign, a viral page, a scraper republishing content, an aggregator, or an attack. Scraper and aggregator republication is the most common benign explanation and typically needs no action at all.

### Step 4 — Assess actual risk honestly

For each RISK item and each pattern, judge:

- **Scale** — a handful of spam links is background noise for every site on the web. A coordinated campaign of hundreds is different.
- **Anchors** — spam with brand or naked-URL anchors is far less concerning than spam with commercial exact-match anchors, which suggests intent.
- **Targets** — links aimed at priority commercial pages warrant closer attention than links to the homepage.
- **Correlation** — did the pattern coincide with a ranking change? Note it as correlation, and only after other causes are excluded.
- **Manual action** — present or absent, where GSC is available. This is the single most important input, because in its absence the practical risk is usually low.

Then state the conclusion plainly, including when it is "no meaningful risk identified." That is a valuable finding, and it saves the user from an unnecessary and irreversible-in-practice intervention.

### Step 5 — Recommend proportionately

The response ladder, in order:

1. **Monitor** — the correct response to most spam. Google's systems ignore the great majority of it.
2. **Document** — record the pattern so a future change has a baseline.
3. **Request removal** — only for genuinely harmful, evidenced links where a real contact exists. Low success rate; rarely worth the effort.
4. **Disavow** — **last resort only**, and only where there is a manual action, or overwhelming evidence of a large-scale attack, and other causes have been excluded.

On disavow, be explicit with the user: it is a live GSC action **Claude will never perform** under CLAUDE.md's Implementation Policy; it is easy to do damage with (disavowing legitimate links removes their value permanently in practice); and Google's own guidance is that most sites should never use it. If the user asks for a disavow file, prepare it with the evidence, state the risk clearly, and let them decide — do not refuse to prepare it, and do not prepare it casually.

## What Checks to Perform

- [ ] Profile coverage stated — what fraction is known, and how
- [ ] GSC manual action checked, or marked `DATA NOT AVAILABLE`
- [ ] Every known link classified SAFE / WATCH / RISK with recorded observed evidence
- [ ] Classification based on fetching the page, not on domain appearance
- [ ] Patterns examined across domains, not just individual links
- [ ] Velocity checked against snapshots, or trend analysis deferred
- [ ] Spikes investigated for cause before being called growth or attack
- [ ] Anchor patterns across unrelated domains examined
- [ ] Risk stated proportionately, including "no meaningful risk identified" where true
- [ ] Response matched to the ladder; disavow treated as last resort
- [ ] No toxicity or spam score invented
- [ ] Nothing submitted, requested, or disavowed by Claude

## How to Identify Issues

A genuine risk finding requires: observed spam characteristics on the linking pages (quoted or described from the actual page); a *pattern* rather than isolated instances; and ideally a plausible mechanism (commercial exact-match anchors at scale, a shared footprint, a narrow time window). A single spam link is not a finding. A coordinated set of 200 exact-match-anchor links from machine-generated pages appearing in one week is. The absence of risk, stated clearly, is equally a finding worth writing.

## Evidence to Collect

Save to `data/backlinks/`:
- `risk-classification.csv` — URL, domain, class, observed signals, anchor, target, date, action.
- `risk-register-YYYY-MM-DD.md` — patterns identified, scale, assessment, recommendation, confidence.
- `velocity-log.md` — new links and domains per period from snapshots, with explanations for any spike.
- `disavow-candidates.md` — only if genuinely warranted, with full evidence per entry and the risk warning attached.
- Describe the specific spam characteristics observed on each RISK page; "looks spammy" is not evidence.

## How to Prioritize Issues

- **CRITICAL** — a confirmed GSC manual action for unnatural links. Everything else stops.
- **HIGH** — a large-scale, evidenced pattern of commercial exact-match anchors from unrelated spam domains, correlating with an unexplained ranking decline after other causes are excluded.
- **MEDIUM** — a growing cluster of RISK links with a shared footprint; a velocity spike with no identified cause; sitewide links from an unrelated low-quality domain.
- **LOW** — isolated spam links; scraper and aggregator republication; ordinary directory and profile links classified WATCH.
- **Not a finding** — the background spam every site accumulates. Say so, and do not manufacture concern.

## Implementation Recommendations

Manual, for the user.

- **Monitor:** no action; re-check next cycle. State this clearly rather than leaving the user feeling something is unresolved.
- **Removal request:** supply the linking URL, the published contact route, the evidence, and a short factual draft ([digital-pr-outreach](digital-pr-outreach.md)), marked for the user to send. Set expectations honestly — most requests go unanswered.
- **Disavow, if the user decides to proceed:** supply the file in Google's format (one `domain:` entry per line, comments prefixed with `#`), the per-entry evidence, and a written statement of the risk. The user uploads it in Search Console. **Claude does not upload it, and does not recommend it in the absence of a manual action or overwhelming evidence.**
- **If a manual action exists:** the reconsideration process requires documented cleanup effort. Claude can help assemble the evidence and draft the request; the user submits it.
- **Preventive:** the durable protection is the [off-page-governance](off-page-governance.md) REJECT list — not acquiring risky links in the first place.

## How to Validate Fixes

- **Removal:** re-fetch the page and confirm the link is gone. A promise is not a removal.
- **Disavow:** it produces no visible confirmation and no measurable signal — set that expectation explicitly. Do not attribute subsequent ranking changes to it, in either direction.
- **Manual action:** the only genuine validation is Google lifting it, visible in GSC.
- **Ongoing:** re-classify each cycle and track the proportion of RISK links over time.
- **Never** claim a risk was "resolved" without observable evidence; algorithmic effects are invisible and unverifiable.

## Expected Output Format

1. **Coverage and limits header**, e.g.:

   > No backlink tool and no GSC access this session (verified). This assessment covers the N links known to this project through direct observation — it is not a complete profile audit. Manual action status is `DATA NOT AVAILABLE`. No toxicity or spam scores are given; no such metric exists here.

2. **Classification summary** — counts by class, with the coverage caveat.
3. **RISK detail table:**

   | URL | Domain | Observed signals | Anchor | Target | Pattern? | Recommendation |
   |---|---|---|---|---|---|---|

4. **Pattern analysis** — footprints, clusters, anchor patterns, velocity.
5. **Risk assessment and recommendation**, proportionate, with confidence — explicitly including "no meaningful risk identified" where that is the finding.
6. Findings in the standard CLAUDE.md template with Confidence Level and Evidence Source.

## Common Mistakes to Avoid

- **Recommending disavow reflexively.** It is the last resort, it is easy to do harm with, and most sites should never use it.
- **Inventing a toxicity or spam score.** No tool, no metric — and vendor scores are not Google signals regardless.
- **Classifying from the domain name** rather than from fetching the page.
- **Treating background spam as an emergency.** Every site accumulates it; Google ignores most of it.
- **Presenting a sample-based assessment as a full profile audit.**
- **Assuming a link spike is either an attack or a success** without establishing the cause. Scrapers and aggregators are the usual explanation.
- **Attributing a ranking drop to links** before excluding technical, content and SERP causes.
- **Claiming Google penalised the site** without a manual action notice. Algorithmic devaluation is invisible.
- **Disavowing legitimate links** by over-broad domain entries — practically irreversible value loss.
- **Failing to state "no meaningful risk identified"** when that is the honest conclusion, leaving the user anxious about a non-problem.
- **Acting.** Claude classifies and prepares; the user submits, requests and decides.
