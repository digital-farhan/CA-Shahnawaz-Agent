# Skill: Digital PR & Linkable Asset Creation

## Purpose

Identify and specify content that can genuinely *earn* links and citations for a Mumbai CA firm — data-driven resources, practical tools, and original research — rather than more service pages and blog posts that nobody has a reason to reference. This is the supply side of authority: [backlink-opportunity-hunter](backlink-opportunity-hunter.md) keeps finding resource pages and publishers, and most of them will only link to something that is actually worth linking to.

## Scope

**This skill owns:** identifying which linkable assets this firm could credibly produce, specifying each one in enough detail to be built, and assessing the sourcing and accuracy requirements that a YMYL tax asset carries.

**This skill does NOT own:**
- Scoring and sequencing proposed content against search demand — [linkable-content-planner](linkable-content-planner.md) owns the dual SEO × Linkability scoring and the final priority order. This skill generates and specifies candidates; that skill decides what gets built first.
- Finding who would link to the finished asset — [backlink-opportunity-hunter](backlink-opportunity-hunter.md), [broken-link-building](broken-link-building.md).
- Pitching it — [digital-pr-outreach](digital-pr-outreach.md).
- Refreshing existing content — [content-decay-refresh](content-decay-refresh.md).
- Auditing existing content quality/depth — [content-audit](content-audit.md).
- E-E-A-T requirements for published pages — [eeat-ymyl-authority](eeat-ymyl-authority.md), which this skill defers to on authorship, sourcing and review.
- Writing or publishing anything to the live site — the user does that, always.

## When to use it

- When [off-page-seo](off-page-seo.md) shows priority pages with no inbound links and no realistic reason anyone would link to them.
- When [backlink-opportunity-hunter](backlink-opportunity-hunter.md) or [broken-link-building](broken-link-building.md) repeatedly finds opportunities blocked because the firm has no qualifying resource.
- When [competitor-backlink-gap](competitor-backlink-gap.md) shows competitors earning editorial links to a resource type this firm lacks.
- Ahead of a seasonal peak (ITR filing season, GST return cycles, year-end compliance) where a genuinely useful resource has natural pickup.

## Required Data

- `data/crawl/service-coverage-map.md` and the site inventory — what already exists, so a "new asset" is not a duplicate of a published page.
- `data/competitors/` — what competitors have published and earned links with.
- The firm's actual capabilities: which services it genuinely delivers, and what proprietary data it might hold.
- Access to **authoritative primary sources** for any statistic, rule, threshold, deadline, or rate proposed for inclusion.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- The live site and competitor sites, to establish what exists and what is missing.
- Authoritative primary sources for tax and compliance facts, fetched and cited directly: the Income Tax Department, the GST Council / CBIC, the MCA, ICAI, RBI, and official government statistical releases.
- Observation of which resource formats the discovered opportunity pages actually link to.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Any statistic the firm does not hold and no primary source publishes.** "Mumbai tax statistics" and "SME compliance statistics" are only viable assets if real numbers exist and can be cited. If they cannot be sourced, the asset is not viable as specified — say so and propose a variant that can be sourced.
- **The firm's own practice data** — filing volumes, client mix, common error rates. Claude cannot see it. Where an asset depends on it, the specification states what the firm would need to supply, and it stays unbuilt until they supply it.
- Search volume, traffic projections, or expected link counts for a proposed asset — no tool. Any expectation is an `ESTIMATE` with its basis stated, never a forecast presented as fact.
- Whether an asset "will go viral" or "will earn N links." Not knowable; do not claim it.

## Pre-Audit Checks

1. Confirm what already exists on the site, so the recommendation is "improve and make citable" rather than "create a duplicate." The site already publishes compliance calendars and current tax guides; an existing asset that is nearly citable is a faster win than a new build.
2. Confirm the sourcing route for every factual claim the asset would carry, **before** specifying it.
3. Load [eeat-ymyl-authority](eeat-ymyl-authority.md) — every asset here is YMYL and inherits its authorship, citation, and review requirements.
4. Check [content-audit](content-audit.md) findings so a proposed asset is not solving a problem better solved by fixing an existing page.

## Step-by-Step Audit Process

### Step 1 — Understand what actually earns links in this category

For a professional-services firm, links are earned by being *referenceable*, not by being long. The three asset families below are the ones with a genuine citation mechanism. Before specifying anything, confirm from the discovered opportunity pages what those curators actually link to — that is direct evidence of demand, and it beats assumption.

### Step 2 — Data-driven assets

Candidates from the specification, each viable **only** if the underlying data can be sourced and cited:

- Mumbai tax statistics; ITR filing trends; GST trends; SME compliance statistics; business registration statistics
- Tax deadline calendars
- NRI taxation resources
- Industry-specific tax guides
- Mumbai business compliance guides

For each candidate, record: the exact primary source, whether the data is actually published at the granularity claimed (national data is not "Mumbai data" — do not relabel it), the update cadence, and the citation format. **An asset built on unsourceable numbers is not an asset; it is a liability**, and in a YMYL category it is a serious one.

The strongest realistic plays here are usually the **deadline calendar** and the **compliance guide** families, because the source data is official, public, dated, and genuinely useful — and because other sites need something authoritative to point at.

### Step 3 — Tools

Candidates: ITR checklist; GST checklist; startup compliance checklist; tax deadline calculator; business registration checklist; TDS compliance calendar; NRI tax checklist; capital gains checklist.

Tools and checklists earn links because they are *used*, not read. For each, specify:
- The precise job it does and who for (a first-time founder registering a private limited company is a different user from an NRI with capital gains).
- Inputs, outputs, and logic — and for anything computational, the exact rule, section, threshold and rate applied, each cited to its primary source with an effective date.
- What makes it better than the government's own version and than competitors'.
- Its maintenance burden — a calculator carrying a superseded rate is worse than no calculator. Specify who updates it and on what trigger, or recommend the static checklist variant instead.
- Whether it works without a form fill. Gating a linkable asset behind a lead form destroys its linkability; if lead capture is required, recommend an ungated tool with an optional consultation CTA.

Note that a checklist is far cheaper to build and maintain than a calculator and earns links nearly as well. Recommend accordingly; do not default to the most complex build.

### Step 4 — Original research

Candidates: surveys; data studies; industry reports; annual tax reports; Mumbai SME reports.

This is the highest-ceiling and highest-effort family, and it is the only one that produces genuinely *unique* citable data. It is also entirely dependent on the firm: Claude cannot run a survey or supply practice data. Specify:
- The question the research answers and why a journalist or publisher would care.
- The data the firm would need to collect or contribute, and whether it can (sample size, client consent, anonymisation).
- Method, so the result is defensible.
- Confidentiality and professional-obligation constraints — client data cannot be published in any form that identifies or could re-identify a client. Flag this explicitly; it is a professional-conduct issue, not just a privacy nicety.
- The publication format and the citation hook (one memorable, quotable finding).

If the firm cannot supply the data, say so plainly and park the asset rather than proposing a "study" with no study behind it.

### Step 5 — Specify each viable asset

For every asset that survives, write a specification containing: working title; format; the specific audience; the citation hook; every factual claim and its primary source; authorship and review requirements per [eeat-ymyl-authority](eeat-ymyl-authority.md); the update trigger and cadence; the target URL and its place in the site structure; internal linking to the relevant priority service pages ([internal-linking](internal-linking.md)); schema type ([schema-audit](schema-audit.md)); and the named opportunity list of who would plausibly link to it, drawn from real discovered prospects rather than a hypothetical audience.

An asset with no named prospective linkers is not a linkable asset — it is just content. Do not specify it as PR.

### Step 6 — Hand off for scoring and sequencing

Pass every specification to [linkable-content-planner](linkable-content-planner.md) for dual SEO × Linkability scoring. This skill deliberately does not decide build order.

## What Checks to Perform

- [ ] Existing site content checked first — improve-and-make-citable considered before new-build
- [ ] Every proposed factual claim traced to a citable primary source, with effective date
- [ ] No statistic proposed that cannot be sourced or that the firm does not hold
- [ ] Geographic granularity honest (national data never presented as Mumbai data)
- [ ] Maintenance burden and update trigger specified for every dated/rate-bearing asset
- [ ] Ungated delivery confirmed for anything intended to earn links
- [ ] Client-confidentiality and professional-conduct constraints assessed for any research asset
- [ ] Named, real prospective linkers listed per asset
- [ ] Authorship, credentials, and review requirements specified per [eeat-ymyl-authority](eeat-ymyl-authority.md)
- [ ] Target URL, internal links, and schema specified
- [ ] Handed to [linkable-content-planner](linkable-content-planner.md) for scoring

## How to Identify Issues

The finding this skill produces is usually one of two shapes. First: *the firm has no asset that any discovered prospect would link to*, which reframes a link-building problem as a content problem and is often the single most important off-page insight available. Second: *an existing page is nearly citable but fails on a specific, fixable dimension* — no author credential, no source citations, no visible last-updated date, no stable URL, gated behind a form, or carrying superseded figures. The second is much cheaper to act on and should be surfaced first when it exists.

## Evidence to Collect

Save to `data/backlinks/` and `reports/`:
- `linkable-asset-specs/<asset-slug>.md` — one specification per viable asset.
- `linkable-asset-candidates-YYYY-MM-DD.md` — all candidates considered, including rejected ones and the reason (unsourceable, duplicate, unmaintainable, confidentiality-blocked).
- `source-register.md` — every primary source cited, with URL, publisher, and the date it was fetched, so claims remain traceable and re-verifiable.
- For each asset, the list of named prospective linkers with the specific URLs that evidence their interest.

## How to Prioritize Issues

Assets are ultimately sequenced by [linkable-content-planner](linkable-content-planner.md), but flag priority signals here:

- **HIGH** — an asset with named prospective linkers already blocked and waiting on it, sourceable data, and low maintenance burden (typically a compliance calendar or a well-sourced checklist).
- **MEDIUM** — a strong asset with a real maintenance requirement (calculators, rate-bearing guides), or one dependent on data the firm must supply.
- **LOW** — assets with no named linkers, or that duplicate something already published.
- **OPPORTUNITY** — original research: highest ceiling, entirely dependent on firm-supplied data, longest lead time.
- **Reject** — anything requiring invented or unsourceable statistics, however attractive the concept.

## Implementation Recommendations

Written for the user to build and publish manually; Claude never publishes.

- **New asset:** supply the full specification plus WordPress guidance — create as a Page (not a Post) for evergreen tools/calendars so it keeps a stable, citable URL; set the Rank Math title, description and canonical; place it in the relevant service silo with internal links from the parent service page; add the appropriate schema (`FAQPage`, `HowTo`, or `Dataset` as fits) via Rank Math's schema editor; add a visible "Last updated" date and a named CA author with credentials.
- **Make an existing page citable:** the usual fix list is add author byline and credentials, add primary-source citations with links, add a visible last-updated date, remove any form gate, stabilise the URL, and add the missing schema. Specify each as a discrete manual step.
- **Never** recommend publishing a figure, deadline, rate, threshold, or legal interpretation that has not been verified against its primary source. In a YMYL tax context an inaccurate published figure is a client-harm risk before it is an SEO risk.
- **Maintenance:** specify the review trigger (Union Budget, GST Council meeting, CBDT/CBIC notification, statutory due-date change) and record it in the content calendar so [content-decay-refresh](content-decay-refresh.md) picks it up.

## How to Validate Fixes

- **Accuracy:** re-verify every cited figure against its primary source before the user publishes, and again on each update trigger. This validation is non-negotiable and precedes any SEO validation.
- **Citability:** confirm the published URL is stable, ungated, indexable, and carries author, credentials, sources and last-updated date.
- **Earned links:** track referring domains to the asset URL in `data/backlinks/backlink-master.csv` over the following months, verifying each claimed link by fetching the page.
- **Usage:** GA4 engagement on the asset URL, if GA4 becomes available; otherwise `DATA NOT AVAILABLE`.
- **Outcome:** whether the asset unblocked previously blocked opportunities in the hunter's queue — the most direct measure of whether it did its job.

## Expected Output Format

1. **Candidate assessment table:**

   | Candidate asset | Family | Data sourceable? | Source | Maintenance | Named linkers | Verdict |
   |---|---|---|---|---|---|---|

2. **One specification file per viable asset**, in the structure from Step 5.
3. **Rejected candidates**, with reasons — particularly anything rejected for unsourceable data, which is a finding in itself.
4. **"Make citable" quick wins** on existing pages, in the standard CLAUDE.md finding template.
5. **Source register** entries for everything cited.

## Common Mistakes to Avoid

- **Inventing statistics.** "Mumbai SMEs miss 40% of GST deadlines" is a fabricated fact even when it sounds plausible, and publishing it in a YMYL category is a serious failure. No source, no claim.
- **Relabelling national data as Mumbai data** to make an asset sound locally unique.
- **Inventing or approximating a tax rule, section, threshold, rate, or deadline.** Every one is verified against its primary source with an effective date, or it is not written.
- **Specifying a calculator with no maintenance owner.** A superseded rate in a tool the firm's name is on is worse than having no tool.
- **Gating a linkable asset behind a lead form** and then wondering why nobody cites it.
- **Proposing "original research" with no data behind it.**
- **Publishing client data** in any identifiable or re-identifiable form.
- **Building content because a keyword exists** — that is the failure mode [linkable-content-planner](linkable-content-planner.md) exists to prevent.
- **Specifying an asset with no named prospective linkers** and calling it a PR asset.
- **Ignoring the cheaper fix:** an existing near-citable page usually beats a new build, and the audit should say so.
