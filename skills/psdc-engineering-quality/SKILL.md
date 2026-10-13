---
name: psdc-engineering-quality
description: Apply PSDC documentation and engineering standards when authoring or reviewing code, contracts, tests, infrastructure, runbooks, or architecture documents in a PSDC common or institution repository. Use for quality gates, implementation handoffs, and standard-conformance reviews; distinguish proposed rules from accepted authority.
---

# PSDC Engineering Quality

Use the owning repository's current contracts and its pinned architecture
baseline. Resolve the applicable standards in `psdc-architecture`:

- `docs/standards/Ecosystem-Documentation-Quality-Standard.md` for document
  type, scope, requirement quality, and evidence;
- `docs/standards/Ecosystem-Engineering-and-Code-Standard.md` for code,
  interfaces, comments, tests, security, review, and release evidence, **when
  present at the inspected architecture revision**;
- the repository's `AGENTS.md`, contribution guide, accepted ADRs, and
  language-specific checks for stricter local requirements.

Read each standard's status. Apply accepted rules as gates. Label a draft or
proposed standard as a recommendation under review, never a binding rule.
The skill itself cannot accept a standard, alter a consumer manifest, approve
a PR, or advance product readiness.

## Work through the change

1. Identify the changed artifacts, owning repository, inspected commits,
   consumer pin, document types, interfaces, trust boundaries, and relevant
   standard versions. Completion: every changed artifact has an owner and an
   applicable rule set or a reason that a rule is not applicable.
2. For documents, check concrete mechanics, stable requirements, source and
   decision traceability, failure behavior, binary acceptance evidence, and
   consistency with schemas. For code, inspect public contracts, state and
   concurrency invariants, validation, security boundaries, tests, and
   comments that explain *why* surprising behavior is necessary. Completion:
   every material behavior or claim can be traced to an authority and a test
   or is marked unverified.
3. Run the owning repository's documented validators and focused tests when
   available. Report commands, environment, pass/fail, and omissions. A
   formatting or schema pass is not proof of runtime safety. Completion: no
   check is presented as stronger evidence than it produced.
4. If the user requested implementation, make the bounded correction and
   repeat affected checks. If the user requested review, report findings
   without editing. Completion: list each finding by artifact and rule ID,
   severity, failure scenario, proposed fix, and evidence state; explicitly
   list applicable controls not yet evidenced.

Use `pass`, `fail`, `not applicable with reason`, or `not yet evidenced` for
each applicable control. Keep Common and institution findings separate. Do
not demand comments that paraphrase every line: require the maintained
reasoning, invariants, boundaries, and failure conditions the code cannot
communicate on its own.
