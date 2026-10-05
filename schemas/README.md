# Research schema

Canonical content stays in Markdown. JSON Schema validates **YAML front matter**, matching [dossier conventions](../conventions/dossier-files.md), rather than introducing a duplicate findings database.

- [Overview schema](overview.schema.json): identity, scope, scripts and dossier state.
- [Finding schema](finding.schema.json): stable IDs, controlled topics, source IDs, separate observation confidence/hypothesis outcome, review and downstream links.
- [Finding template](../templates/finding.md): required narrative sections and example provenance.
- [Taxonomy](../taxonomy.md): dimension meanings and limits.

Run from the repository root:

```sh
uv run --with 'PyYAML>=6,<7' --with 'jsonschema>=4,<5' python scripts/validate_research.py
```

Alternatively install [requirements](../requirements-validation.txt) in a virtual environment and run `python scripts/validate_research.py`. Validation checks metadata, duplicate IDs/prefixes, source resolution, body sections, review/outcome prerequisites, source dates, and local Markdown file/anchor links. It excludes the pre-existing generated `graft/` directory and `.git/`.

Validation does **not** verify linguistic truth, BCP 47 registry membership, reviewer competence, remote-link availability or downstream approval. Human review remains required. Dates are calendar dates; unknown publication dates remain null. Source records retain their richer Markdown/YAML form specified in conventions.
