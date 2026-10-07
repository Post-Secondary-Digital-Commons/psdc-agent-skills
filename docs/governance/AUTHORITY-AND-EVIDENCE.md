# Authority and Evidence Rules

## Authority order

```text
Decision Register
  -> accepted defaults, human decisions, supersession records
ADRs
  -> architecture decisions and consequences
Contracts
  -> schemas, APIs, events, state machines, registries
Repository documents
  -> subsystem elaboration
Institution overlays
  -> local policy, branding, topology, deployment choices
Generated views and Obsidian notes
  -> navigation and explanation only
```

When two sources conflict, do not average them. Report the conflict and apply the
higher authority unless a formal supersession exists.

## Evidence states

| State | Minimum evidence | Does not prove |
|---|---|---|
| proposed | Identified proposal and owner | Acceptance |
| documented | Scoped document at a revision | Contract validity or code |
| contracted | Machine-readable interface plus fixtures | Runtime behavior |
| structurally_validated | Reproducible parser/schema/link checks | Semantic correctness or execution |
| implemented | Source plus relevant executable tests | Deployment |
| deployed | Identified environment and deployment evidence | Reliability at production load |
| production_proven | Time-bounded operational evidence and SLO results | Future correctness |

## Required separation

Each finding labels its basis as `observed`, `documented_claim`, `inference`,
`assumption`, or `recommendation`. An assessment must name inspected revisions,
checks run, checks omitted, and evidence expiry where applicable.

