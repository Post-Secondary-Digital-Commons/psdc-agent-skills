---
name: psdc-evidence-audit
description: Audit PSDC readiness or status claims against artifacts, commits, checks, scope, producer, and expiry. Use when validating dashboard claims, evidence registries, release readiness, or statements such as implemented, deployed, or production ready.
---

# PSDC Evidence Audit

Read [`references/evidence-record.md`](references/evidence-record.md). For each
claim, resolve the cited artifact at the cited revision, reproduce the named
check where safe, and classify the strongest supported evidence state. Report a
claim as unsupported when its artifact is absent, mutable without a digest,
outside scope, expired, or evidence for a weaker state. Never upgrade a claim
based on prose confidence.

Completion requires a row for every input claim and an explicit list of evidence
that could not be reproduced.

