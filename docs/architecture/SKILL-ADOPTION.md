# Skill Adoption Architecture

**Status:** Draft for owner review  
**Scope:** Common PSDC agent behavior  
**Runtime claim:** None

## Decision

PSDC vendors a reviewed subset of Matt Pocock's skills as upstream material and
wraps their methods with PSDC-native authority, evidence, privacy, federation,
and lifecycle rules. Upstream files stay unmodified so maintenance diffs remain
auditable. PSDC behavior is expressed by router skills, repository instructions,
the skill registry, and review rubrics.

## Fit by skill

| Skill | Direct value | PSDC adaptation | Current mode |
|---|---|---|---|
| setup-matt-pocock-skills | Consistent tracker and domain setup | Respect existing ADR/register authority and avoid unsolicited tracker writes | Adapted |
| grill-with-docs | Finds ambiguity early | Record proposals separately from accepted decisions | Adapted |
| domain-modeling | Sharpens vocabulary and ADRs | Preserve common versus institution bounded contexts | Adapted |
| to-spec | Converts conversation into a testable spec | Add evidence states, federation scope, security and privacy boundaries | Adapted |
| to-tickets | Produces tracer-bullet work | Require approved handoff, explicit blockers and verifiable vertical slices | Adapted |
| wayfinder | Maps uncertain decisions | Link decisions to register IDs and scope them to common or institution | Adapted |
| research | Encourages primary sources | Add license, provenance, version, and uncertainty capture | Adapted |
| writing-for-agents | Reduces prompt sprawl | Becomes the writing discipline for common and overlay agent repos | Enabled |

## Explicit non-adoption

Implementation-driving skills are not imported in this wave. The repository has
no authority to turn a specification into code or deployment. Code review,
diagnosis, and TDD can be added once executable components exist and a reviewed
implementation slice is authorized.

## Institution overlay

`algonquin-agent-skills` should be a thin fork/overlay of this repository. It may
add Algonquin contacts, approval routes, topology, deployment commands, branding,
and policy bindings. It must retain upstream provenance and must not redefine a
common contract under an institution-specific name.

## Acceptance gates

1. Every imported skill has repository, revision, path, and license provenance.
2. Every enabled skill has lifecycle scope and PSDC constraints.
3. Imported files are byte-comparable to the pinned upstream revision.
4. Custom skills pass the Codex skill validator.
5. Assessment output conforms to the assessment-result schema.
6. No skill can promote a readiness state without a new evidence record.

