---
name: psdc-project-assessment
description: Assess PSDC architecture, contracts, documentation, workspace catalogs, or implementation readiness against authority and evidence. Use for project status, gap analysis, cross-repository consistency, documentation maturity, or implementation handoff review.
---

# PSDC Project Assessment

Produce a bounded, revision-specific assessment. Read
[`references/rubric.md`](references/rubric.md) before scoring.

## Procedure

1. **Bind the snapshot.** Record repositories, branches or commits, included
   paths, exclusions, and the time of inspection. Completion: every conclusion
   is traceable to a named snapshot.
2. **Load authority.** Locate the Decision Register, accepted ADRs, contracts,
   repository instructions, and applicable institution overlay. Completion:
   conflicts are ranked by authority rather than silently reconciled.
3. **Inventory evidence.** Separate observed artifacts, tool results,
   documentation claims, inferences, assumptions, and recommendations.
   Completion: no inference appears in an observed field.
4. **Apply the rubric.** Score every applicable dimension and mark non-applicable
   dimensions with a reason. Completion: every score cites evidence and names
   the next evidence needed for a higher score.
5. **Run proportionate checks.** Prefer existing repository validators. Record
   command, exit code, revision, and limitations. Completion: passing structural
   checks are described as structural evidence only.
6. **Adversarial review.** Search for authority drift, stale links, semantic
   clones, unsafe defaults, missing failure paths, and readiness inflation.
   Completion: the ten highest-risk failure scenarios are either findings or
   explicitly reported as checked and not found.
7. **Publish the result.** Validate against
   `schemas/assessment-result.schema.json`. Completion: the assessment contains
   findings, sound areas, unresolved questions, and the next bounded slice.

Use vendored `domain-modeling`, `research`, `grill-with-docs`, and `wayfinder`
only where their branch applies. They do not override PSDC authority rules.

