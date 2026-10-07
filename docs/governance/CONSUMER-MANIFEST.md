# Repository Skill Adoption Contract

**Status:** Specification and structural validator  
**Authority:** The Decision Register, accepted ADRs, and contracts take precedence

Each product or institution repository uses one small
`.psdc/agent-skills.yaml` manifest to pin the common skill pack at an immutable
commit and name the review methods relevant to its own context. Its root
`AGENTS.md` is a short pointer to that manifest. `CLAUDE.md` points to
`AGENTS.md` so both coding clients receive the same repository rules.

The manifest identifies the repository, context, entrypoint documents, change
scope, common decision and contract authority, and institution policy authority
when applicable. This keeps one common skill implementation while allowing
each institution to own its policy bindings.

## Validation

From the skill-pack repository:

```powershell
python scripts/Validate-Consumer.py C:\path\to\repository\.psdc\agent-skills.yaml
```

The validator checks the schema, enabled-skill registry, repository identity,
and local entrypoint paths. A pass proves manifest structure and referenced
files; it does not prove that an agent obeyed the skills or that any product
service runs.

An assessment still records exact source revisions and applies the
`psdc-project-assessment` rubric. An evidence audit still resolves each
claim against its artifact. The manifest is routing data, not a new authority
or a readiness certificate.
