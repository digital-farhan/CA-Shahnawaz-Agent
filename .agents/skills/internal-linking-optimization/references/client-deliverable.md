# Client deliverable standard

Use this reference when the result will be implemented by the user or shared with a client.

## Narrative structure

1. **Executive summary:** What the current architecture helps or hinders, why it matters commercially, and the three to five highest-leverage actions.
2. **Scope and evidence:** Crawl date/configuration, URLs and edges analyzed, data sources, exclusions, and known gaps.
3. **Priority-page scorecard:** Business role, indexability, depth, unique inlinks, contextual inlinks, main routes, issue, and action.
4. **Findings:** Use the complete project finding template, including confidence and evidence source where required.
5. **Implementation register:** Exact source, target, anchor draft, placement, owner, dependency, effort, priority, and validation.
6. **Cluster plan:** Current and proposed hub/child/sibling relationships for each priority service or topic group.
7. **Roadmap:** Sequence integrity fixes, discovery/architecture fixes, contextual opportunities, then measurement.
8. **Limitations and measurement:** What cannot be concluded and how outcomes will be checked.

Lead with business impact and user journeys, then provide technical detail. Keep “current state,” “recommendation,” and “expected mechanism” visually and verbally distinct.

## Core tables

### Priority-page architecture scorecard

| Priority page | Role/cluster | Status/indexability | Depth | Unique inlinks | Contextual inlinks | Main route(s) | Assessment | Priority |
|---|---|---|---:|---:|---:|---|---|---|

### Implementation register

| ID | Source URL | Current context | Proposed anchor | Target URL | Placement | User/SEO rationale | Owner | Dependency | Effort | Priority | Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|

### Integrity remediation

| Source URL | Current href | Problem | Final/canonical target | Recommended action | Scope | Severity | Validation |
|---|---|---|---|---|---|---|---|

### Cluster coverage

| Cluster | Hub | Child pages | Missing justified relationships | Cross-cluster journeys | Recommended module/context |
|---|---|---|---|---|---|

## Finding quality

Each finding must include the project's Issue, Severity, Evidence, Affected URLs, SEO Impact, Likely Root Cause, Recommended Fix, Manual Implementation Guide, and Validation fields. Include Confidence Level and Evidence Source when the methodology calls for them.

Evidence should quote exact URLs, counts, anchors, locations, statuses, or short page excerpts and name the dated file. Do not paste huge edge lists into the narrative; attach them as implementation/evidence tables.

Recommendations must specify:

- what changes;
- exactly where;
- the preferred destination;
- a draft anchor or editorial rule;
- who needs to approve/implement it;
- prerequisites and risks;
- how to confirm success.

## Client-safe language

Use measured claims:

- “The current crawl found…”
- “This page is reachable in four eligible link hops from the homepage…”
- “Most observed inlinks are repeated footer links; only two distinct source pages link contextually…”
- “Adding this link would create a direct, relevant route for users researching…”
- “Ranking impact cannot be isolated in advance; validate discovery and observe search/behavior trends after implementation.”

Avoid “link juice,” “guaranteed boost,” “Google requires three clicks,” “perfect anchor ratio,” and unsupported ROI forecasts.

## Visuals

Use a diagram only when it makes architecture clearer than a table. For clients, prefer a small current-versus-proposed cluster map or a priority-page flow. Large force-directed graphs are evidence aids, not automatically useful executive visuals; include one only when labeled, filtered, and interpretable.

Follow the workspace's navy/forest/gold report system for HTML/PDF outputs. Produce Markdown evidence first, then reviewed HTML, then PDF only after user review, per project rules.
