# Local GPU evidence triage

`scripts/Triage-LocalEvidence.py` is a bounded reviewer assistant, not a skill
executor or an approval authority. It reads excerpts from named Git commits,
checks their hashes and repository identities, then submits only those excerpts
to a loopback Ollama endpoint using the exact `qwen3.5:4b-q4_K_M` model tag.
The model cannot browse, edit files, call tools, or change readiness states.

Run one triage process at a time. The current file cache is not a multi-writer
queue. Keep the input and cache on a private local volume; they may contain
sensitive documentation. The runner refuses remote Ollama URLs and redirects.
The operator must review every candidate against its cited source before using
it in an issue, specification, or implementation handoff. An empty findings
array does not prove that the source is sound.

Create an input JSON document with `items` containing `repository`, a full
40-character `commit`, POSIX-relative `path`, one-based inclusive `startLine`
and `endLine`, the exact newline-joined `text`, and its lowercase SHA-256.
The local Git checkout must have an `origin` remote whose repository slug
matches `repository`. First validate without inference:

```powershell
python scripts/Triage-LocalEvidence.py .\triage-input.json --repo psdc-cloud=C:\path\to\psdc-cloud --cache C:\private\triage-cache --validate-only
```

Remove `--validate-only` for one local model pass. Set `--context 4096`
(default) or `8192` after measuring available VRAM. The output status is
always `candidate_review_only`; the cache key binds source, model digest,
prompt, schema, and settings. Structural tests run through
`scripts/Test-AgentSkills.ps1`. Passing tests prove input/output boundaries,
not finding accuracy, operator independence, production behavior, or GPU
availability on another machine.
