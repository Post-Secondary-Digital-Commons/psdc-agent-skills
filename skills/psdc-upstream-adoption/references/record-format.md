# Adoption record format

Store one JSON record per component under the owning repository's governed
adoption-record location. The repository catalog should map each component ID
to exactly one record; implementation tickets and PRs cite that ID and the
record's immutable revision. Validate the record with
`python scripts/Validate-Adoption.py <record.json>` in the skill-pack
repository. Structural validation cannot accept the architecture decision.

Required fields capture the decision rather than an essay:

| Field | Meaning |
|---|---|
| `componentId`, `repository`, `scope` | Stable owner and Common/institution boundary |
| `status`, `decisionOwner` | Proposed, accepted, deferred, or rejected; no agent self-approval |
| `governingRefs` | Exact ADR/contract/decision versions relevant to the seam |
| `candidates` | Primary source URL, exact revision, SPDX evidence, fit and failure results for each meaningful option |
| `selection` | Adopt, adapter, upstream extension, bounded patch, fork, or build, with rationale |
| `upstreamProvides`, `psdcOwns`, `excluded` | Prevent semantic clones and authority transfer |
| `evidence` | Command/review, artifact revision, result, and limitation |
| `maintenance` | Patch queue, update owner, security response, and replacement trigger |
| `openGates` | Human, legal, compatibility, security, or institution approvals still needed |

For each implementation ticket/PR, record `componentId`, adoption-record
revision, changed upstream source/dependencies, integration-mode delta,
contracts and consumers affected, tests run/not run, and newly open gates.
This can live in a PR's structured review record or an implementation manifest;
it need not duplicate the component's full research. A new component or
unreviewed upstream change cannot use the short path.

Example status distinction:

```json
{
  "schemaVersion": 1,
  "componentId": "vs01.lab-worker",
  "repository": "psdc-compute",
  "scope": "common",
  "status": "proposed",
  "decisionOwner": "PSDC Compute Fabric Working Group",
  "governingRefs": ["ADR-0026", "compute.lease.v1"],
  "candidates": [],
  "selection": { "mode": "adapter", "rationale": "Candidate only; exact upstream source review pending" },
  "upstreamProvides": ["candidate machine/job matching"],
  "psdcOwns": ["institutional admission", "signed lease authority"],
  "excluded": ["public provider admission by default"],
  "evidence": [],
  "maintenance": { "owner": "unassigned", "updatePlan": "pending", "replacementTrigger": "pending" },
  "openGates": ["source revision", "license review", "failure spike", "owner acceptance"]
}
```

The example is intentionally **proposed** and empty of proof. Do not convert
it to `accepted` merely because it matches the schema. Acceptance requires
the named decision authority and reviewed evidence.
