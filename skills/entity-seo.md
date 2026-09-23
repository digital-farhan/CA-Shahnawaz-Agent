# Skill: Brand Entity SEO

## Purpose

Build and audit the firm's entity footprint across the web so search engines can answer, consistently and from multiple corroborating sources: **who this firm is → what it does → where it operates → what it specialises in → why it is authoritative.**

For a professional-services firm in a YMYL category, entity clarity is foundational. Search engines and AI answer engines both need to resolve "Shahnawaz and Associates" to a single, well-described, credentialed Mumbai CA practice — and a footprint that contradicts itself across sources prevents that resolution regardless of how good the website is.

## Scope

**This skill owns:** the entity footprint beyond NAP — brand and organisation mentions, founder/CA mentions, company and professional profiles, social profiles, knowledge-source presence, press, podcasts, interviews, videos, conference appearances — and consistency of the entity's *description*: brand name, business description, services, location, founder information, contact information.

**This skill does NOT own:**
- NAP values and directory listing consistency — [local-citation-authority](local-citation-authority.md), which owns the canonical record this skill consumes.
- On-site local signals — [local-seo](local-seo.md).
- Schema syntax and validity — [schema-audit](schema-audit.md), though this skill specifies the entity *values* the schema should express and the `sameAs` set.
- Author credentials and content trust signals on published pages — [eeat-ymyl-authority](eeat-ymyl-authority.md).
- Converting unlinked mentions into links — [backlink-reclamation](backlink-reclamation.md); this skill catalogues mentions as entity signals whether or not they link.
- Whether the firm appears in AI answers — [ai-search-visibility](ai-search-visibility.md), which consumes this skill's entity work.
- Creating or editing any profile — the user does that manually.

## When to use it

- Early, alongside [local-citation-authority](local-citation-authority.md), because most other authority work assumes a coherent entity.
- When the firm is not surfacing for its own brand name, or is being confused with a namesake.
- Before [ai-search-visibility](ai-search-visibility.md) work — answer engines resolve entities before they cite them.
- On a recurring cycle, as new mentions and profiles appear.

## Required Data

- The canonical entity record from [local-citation-authority](local-citation-authority.md).
- Official professional register details — for this firm, the ICAI public listing showing **Shahnawaz and Associates, FRN 151767W**, and **Shahnawaz Shaikh, membership 194241** (recorded in `data/crawl/nap-instances.md`).
- The live site's About, team, and contact pages.
- Existing on-site Organization / ProfessionalService schema.

## Data Sources & Limitations

### AVAILABLE WITH LIVE ACCESS
- The firm's own site: how it describes itself, its services, its people, its credentials.
- On-site Organization/LocalBusiness schema and any `sameAs` references.
- Public professional registers (ICAI), which are unusually strong entity evidence because they are official and independently verifiable.
- Third-party profiles, mentions, articles, listings and social profiles, found by search and verified by fetch.
- Whether each profile is current, complete, and consistent with the canonical record.

### DATA NOT AVAILABLE (mark explicitly — never estimate)
- **Google Knowledge Panel presence or contents.** No tool provides this. Whether a panel exists, what it says, and whether an entity is in Google's Knowledge Graph are all `DATA NOT AVAILABLE`. Recommend the user check by searching their own brand name; do not assert.
- Whether search engines have actually resolved the entity — unobservable. Every statement here is about *signals available to* search engines, never about what they concluded.
- Private or unpublished credentials, engagements, or affiliations — only what is publicly verifiable.
- A complete mention inventory — search-based discovery is always partial. Never claim completeness.
- Sentiment or reach of any mention.
- Any claim about the practitioner's history, qualifications, or experience that is not published on the site or an official register. **Never fill an entity profile with plausible-sounding biography.**

## Pre-Audit Checks

1. Load the canonical entity record; if fields remain `DISPUTED` (the address currently is), note that entity consistency work is blocked on the same owner decision.
2. Confirm the exact registered name, FRN and membership number from the official register — these are the entity's hardest identifiers and everything else should align to them.
3. Establish brand-name variants in actual use, so discovery covers all of them.
4. Confirm the namesake risk: check whether other individuals or firms share the name, since misattributed mentions corrupt an entity profile.

## Step-by-Step Audit Process

### Step 1 — Define the entity precisely

Write the entity definition once, and use it everywhere:

- **Organisation:** registered name, FRN, entity type (CA firm / professional service), founded, location, service scope, service area.
- **Person:** the practitioner's name as registered, ICAI membership number, designation, specialisations, and the relationship to the organisation (`founder` / `principal`).
- **Description:** one short and one long description, factually accurate, service-specific, location-specific — usable verbatim across every profile so descriptions stop drifting.

Every element must be sourced. Anything unverified is omitted, not approximated.

### Step 2 — Inventory the footprint

Search brand variants, the practitioner's name, the FRN, the membership number, the phone, and the domain. Catalogue each of the specification's monitored surfaces:

- Brand mentions; organisation mentions; founder/CA mentions
- Company profiles; professional profiles; social profiles
- Business directories (values owned by [local-citation-authority](local-citation-authority.md))
- Knowledge sources
- Press mentions; podcasts; interviews; videos; conference appearances

For each: URL, surface type, whether it links, whether it is claimed/controlled, the exact entity details published, and the date observed.

**Verify attribution before recording.** A mention is this entity only if corroborated by the address, phone, FRN, membership number, or unambiguous Mumbai-CA context. Unverifiable mentions are recorded as `ATTRIBUTION NOT DETERMINED` and excluded from consistency scoring — a wrongly attributed mention is worse than a missing one.

### Step 3 — Detect entity inconsistencies

Compare every surface against the entity definition, across the six specification dimensions:

| Dimension | Typical inconsistency |
|---|---|
| **Brand name** | `and` vs `&`; with/without `CA`; practitioner name used where the firm name belongs |
| **Business description** | Generic "accounting services" on one profile, specific CA/tax/compliance positioning on another |
| **Services** | Profiles listing services the firm does not offer, or omitting priority ones |
| **Location** | The open unit/floor conflict; some profiles listing only "Mumbai" |
| **Founder information** | Missing designation or membership number; inconsistent name spelling; unclear firm relationship |
| **Contact information** | Different phones or emails; non-canonical or HTTP website URLs |

Separate **contradiction** (two profiles state incompatible facts) from **incompleteness** (a profile omits something). Contradictions damage entity resolution; gaps merely fail to help.

### Step 4 — Assess entity signal strength on the site itself

The website is the entity's primary source, and weakness here caps everything else:

- Is there a substantive About page identifying the practitioner by name, with ICAI credentials, membership number and genuine professional background?
- Is authorship attributed to a named, credentialed person, or is content anonymous? Anonymous YMYL content is a significant entity and trust weakness — route to [eeat-ymyl-authority](eeat-ymyl-authority.md).
- Does Organization/ProfessionalService schema exist, with a `sameAs` array pointing to the firm's genuine external profiles? A missing or empty `sameAs` is the single most common technical entity gap, and it is the mechanism by which a site tells search engines which external profiles are actually the same entity. Specify the values; [schema-audit](schema-audit.md) validates the markup.
- Are services described in consistent, specific language matching the priority-service vocabulary?

### Step 5 — Identify footprint gaps

Where is the entity *absent* that a firm of this kind would normally be present — official professional listings, legitimate professional directories, relevant associations, a professional profile for the practitioner? Route genuine, eligible gaps to [backlink-opportunity-hunter](backlink-opportunity-hunter.md) (link value) and [local-citation-authority](local-citation-authority.md) (NAP values), and keep the entity value in view: the goal is corroboration from independent sources, not link count.

### Step 6 — Prepare corrections; do not make them

Produce exact values and manual steps. **Claude never edits a profile, creates an account, or publishes a bio.**

## What Checks to Perform

- [ ] Entity definition written, every element sourced, nothing approximated
- [ ] Official register details (FRN, membership number) confirmed and used as the anchor
- [ ] Discovery run on all name variants, practitioner name, FRN, phone and domain
- [ ] Every mention attribution-verified; namesakes excluded
- [ ] Footprint catalogued across all specification surfaces
- [ ] Inconsistencies classified across the six dimensions; contradiction vs. incompleteness separated
- [ ] On-site entity signals assessed: About page, named authorship, credentials, schema
- [ ] `sameAs` set specified from verified, controlled profiles only
- [ ] Footprint gaps identified and routed
- [ ] Knowledge Panel marked `DATA NOT AVAILABLE`
- [ ] Inventory stated as partial
- [ ] No biography, credential, or affiliation asserted without a source

## How to Identify Issues

An entity finding needs the entity definition value, the observed value, the source URL, and the date. Severity turns on whether a search engine or a client could be **misled or left unable to resolve the entity**. The strongest finding is a contradiction across independent authoritative sources — for this firm, the website, the ICAI register and multiple directories currently publishing different office units is exactly that, and it is an entity problem as much as a citation one. The second strongest is anonymous YMYL content: a tax site with no identifiable, credentialed author gives search engines nothing to attach expertise to.

## Evidence to Collect

Save to `data/backlinks/`:
- `entity-definition.md` — the canonical entity definition with sources.
- `entity-footprint.csv` — surface, URL, type, linked, claimed, published values, attribution confidence, date.
- `entity-inconsistencies.md` — dimension, definition value, observed value, source, classification.
- `entity-gaps.md` — surfaces where the entity should exist and does not, with routing.
- `sameas-set.md` — the verified profile URLs to include in schema, each confirmed as genuinely the firm's.
- Quote published descriptions verbatim rather than summarising them.

## How to Prioritize Issues

- **CRITICAL** — contradictory contact details that could misdirect a client.
- **HIGH** — the multi-source location contradiction; anonymous authorship across YMYL content; missing or empty `sameAs`; a missing or thin About page with no credentials.
- **HIGH** — a namesake being conflated with the firm in visible places, which actively corrupts entity resolution.
- **MEDIUM** — description drift; inconsistent service lists; absence from the official professional listing or a relevant association; unclaimed profiles.
- **LOW** — cosmetic name variants; incomplete but non-contradictory profiles.
- **OPPORTUNITY** — press, podcast, panel and interview surfaces where the practitioner could credibly appear, which build entity authority and links simultaneously.

## Implementation Recommendations

All manual, for the user.

- **On-site first.** The website is the entity's primary source; fix it before external profiles.
  - **About page:** name the practitioner, state ICAI membership number and FRN, describe genuine professional background and specialisations, and include a real photo. Supply the exact copy for the user to paste — factual only, no invented history.
  - **Author attribution:** a named, credentialed author on every substantive page, with a bio linked to the About page ([eeat-ymyl-authority](eeat-ymyl-authority.md)).
  - **Schema:** specify `Organization`/`ProfessionalService` with `name`, `legalName`, `address`, `telephone`, `url`, `founder` (`Person` with `name`, `jobTitle`, `hasCredential`), `areaServed`, and a `sameAs` array of verified profile URLs. In WordPress this is entered via Rank Math → Titles & Meta → Local SEO, or as a custom schema on the relevant page; [schema-audit](schema-audit.md) validates the result.
- **Then external profiles**, in the order: official professional listing → owned social/professional profiles → major directories → minor ones. Supply per profile: the URL, the current published values (recorded for rollback), the replacement values, and the edit route.
- **Never** publish a credential, qualification, membership, award, or affiliation that is not verifiable. In a regulated profession, an overstated credential is a professional-conduct exposure, not merely an SEO error.

## How to Validate Fixes

- **Per profile:** re-fetch and confirm the published values match the definition; re-check after a week where edits are moderated.
- **Schema:** validate the markup and confirm `sameAs` resolves to live, correct profiles ([schema-audit](schema-audit.md)).
- **Consistency trend:** re-run the footprint inventory next cycle; the meaningful metric is the proportion of surfaces matching the definition.
- **Brand resolution:** the user searches the brand name and the practitioner name and reports what appears, including any Knowledge Panel. Claude cannot observe this.
- **AI answer surfaces:** hand to [ai-search-visibility](ai-search-visibility.md) for its own testing method.

## Expected Output Format

1. **Entity definition** — organisation, person, descriptions, all sourced.
2. **Footprint inventory table:**

   | Surface | URL | Type | Links? | Claimed? | Matches definition? | Attribution confidence | Date |
   |---|---|---|---|---|---|---|---|

3. **Inconsistency report** across the six dimensions, contradictions first.
4. **On-site entity assessment** — About page, authorship, schema, `sameAs`.
5. **Specified `sameAs` set.**
6. **Gaps and opportunities**, routed.
7. **Limitations**, e.g.: *Knowledge Panel status is `DATA NOT AVAILABLE` (no tool). This footprint is search-derived and partial. N mentions were excluded as `ATTRIBUTION NOT DETERMINED`.*
8. Findings in the standard CLAUDE.md template with Confidence Level and Evidence Source.

## Common Mistakes to Avoid

- **Writing a plausible biography.** If the site and the register do not state it, it does not go in a profile. This is the most damaging failure available in this skill.
- **Asserting a credential, award, or affiliation** that cannot be verified — a professional-conduct risk in a regulated profession.
- **Attributing a namesake's mention to this firm**, which corrupts the entity rather than strengthening it.
- **Claiming Knowledge Graph or Knowledge Panel status** without any tool that can see it.
- **Fixing external profiles before the website**, leaving the primary source contradicting the corrections.
- **Putting unverified profiles in `sameAs`** — it should assert only profiles genuinely controlled by or belonging to the firm.
- **Treating entity work as link building.** A consistent, corroborated, unlinked profile still strengthens entity resolution.
- **Ignoring anonymous authorship** because it looks like a content issue. For a YMYL entity it is a first-order weakness.
- **Proceeding past the disputed address** and standardising profiles on an unconfirmed value.
- **Editing profiles.** Claude prepares values and steps; the user performs every change.
