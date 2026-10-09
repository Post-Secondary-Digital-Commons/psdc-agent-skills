# Skill Adoption Architecture

**Status:** Explanatory architecture; `config/skill-registry.yaml` governs
pack-wide disposition and each consumer manifest governs repository opt-in.

**Runtime claim:** None.

## Method and authority

PSDC keeps reviewed Matt Pocock source files unchanged at a pinned upstream
revision. PSDC-native skills, the registry, and repository instructions add
authority, evidence, privacy, federation, and lifecycle boundaries. This
separation makes upstream changes auditable and keeps institution policy out of
common skill source. A true fork belongs under `skills/` with recorded source,
modifications, and maintenance ownership, as described in
[Upstream Maintenance](../governance/UPSTREAM-MAINTENANCE.md).

The [complete inventory](../governance/COMPLETE-SKILL-INVENTORY.md) describes
every pinned upstream and PSDC-native skill. The
[application-scope map](../governance/SKILL-APPLICATION-SCOPE.md) identifies
repository areas, useful task methods, declared consumer opt-ins, exact source
revisions, and evidence boundaries. It is a generated snapshot, not proof that
an agent ran a skill. Do not maintain a second skill-by-skill status table here.

## Current lifecycle boundary

`code-review`, `codebase-design`, `prototype`, and other permitted methods are
present in the pack. `diagnosing-bugs` and `tdd` are vendored but deferred;
`implement` and `implement-spec` are vendored but prohibited by the current
registry. Presence is provenance, not activation. An explicit implementation
request does not itself change the registry or waive a component's accepted
handoff and contract gates. The owner must accept a policy change before those
skills become enabled. A bounded prototype remains labeled a prototype and
does not satisfy a D2 handoff or production admission.

Each consuming repository pins an immutable pack revision in
`.psdc/agent-skills.yaml`. It enables only relevant skills at that revision.
Refreshing the pack does not update consumer pins; a consumer update is a
separate reviewed change. The validator proves manifest structure and routing,
not behavioral compliance, implementation, or deployment.

## Institution overlay

An institution may specialize contacts, approval routes, topology, deployment
commands, branding, and local policy bindings through its own repository or
overlay. It retains common provenance and cannot redefine a shared contract
or accepted common decision under a local name. An Algonquin skill-pack overlay
is planned, not presumed to exist or to be in use.

## Review completion criteria

A skill-pack change is ready for owner review when its source revision and
license are recorded, vendored-file hashes and registry coverage pass, the
application-scope projection is regenerated if policy changed, and the change
identifies which consumer manifests need separate updates. No readiness state
advances without evidence for that state.
