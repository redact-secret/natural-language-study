# Dossier File Patterns

A dossier is the canonical collection of scoped research for a language. Create files as research needs them; do not generate empty topic files for every language.

## Paths and language identity

Use a readable lowercase kebab-case key such as `korean`, `english`, or `mandarin-chinese` under `studies/`. Declare BCP 47 language tags and script identifiers in metadata; directory names are navigation labels, not language identifiers.

Scope regional or register variation inside the dossier first. Create a separate dossier only when independent scope and maintenance justify it. Define a stable uppercase three-letter `id_prefix` in `overview.md`; it is a repository identifier, not a promise of equivalence to an ISO code. Check uniqueness before creating it.

## File responsibilities

| Path inside a dossier | Purpose |
| --- | --- |
| `overview.md` | Required entry point: scope, metadata, questions, coverage, finding index, and gaps. |
| `sources.md` | Required when research sources are added: canonical source records. |
| `findings/<PREFIX>-001.md` | One canonical finding per file. |
| `writing-system.md` | Script and orthographic questions; links to canonical findings. |
| `tokenization.md` | Segmentation and word/entity boundary questions. |
| `morphology.md` | Affixes, inflection, particles, clitics, and related interactions. |
| `person-names.md` | Naming practices, order, titles, initials, and variation. |
| `entity-boundaries.md` | Boundary inclusion/exclusion questions and contrasts. |
| `ambiguity.md` | Person/non-person collisions and context-dependent readings. |
| `mixed-script.md` | Transliteration, script mixing, and code switching. |

A single-question dossier may use only overview, sources and canonical findings. A requested broad language dossier, including the initial four-language wave, also needs substantive `morphology.md`, `tokenization.md`, `person-names.md`, `entity-boundaries.md`, `ambiguity.md` and `mixed-script.md` syntheses. Index each in the overview. A topic must answer a scoped question with sourced observations, a challenging contrast, an NER implication and an explicit gap; a heading or finding-link list alone does not satisfy coverage.

Distinguish **breadth delivered** (the requested topic syntheses exist with substantive research) from **review completed** and **hypotheses evaluated**. Draft desk research can deliver breadth while every topic remains in-progress. Do not claim exhaustive language coverage. For an inapplicable dimension, explain the scoped exclusion instead of inventing content. Add other kebab-case topics only when useful.

Cross-language synthesis lives at `comparative/<topic>.md`. It cites finding IDs and scoped comparisons; it must not duplicate or silently strengthen the original claims.

## Overview template

```yaml
---
language_key: korean
display_name: Korean
language_tags: [ko]
scripts: [Hang]
id_prefix: KOR
status: draft
scope:
  varieties: []
  regions: []
  registers: []
  domains: []
  entity_types: [PERSON]
research_issues: []
updated: YYYY-MM-DD
---
```

The metadata above illustrates structure only. Tags and scripts must match the actual study; populate the empty scope lists or explicitly explain that scope is not yet established. A tag such as `ko` alone does not define regional, social, or domain coverage.

Use these overview sections:

1. Research questions and motivation.
2. Scope and exclusions.
3. Topic coverage: `not-started`, `in-progress`, `reviewed`, or `out-of-scope`, with links and reasons.
4. Finding index: ID, title, status, observation confidence, and downstream links.
5. Known gaps and source or reviewer needs.
6. Research issue links and revision notes.

Dossier `status` is `draft`, `active`, or `archived`. `active` means research is maintained, not that the language is supported. Topic `reviewed` means its declared scope was reviewed, not that every relevant phenomenon was covered.

## Finding IDs and metadata

Use `<PREFIX>-<three-or-more-digit-sequence>`, for example `KOR-001`. Allocate the next unused sequence in the dossier. IDs persist across renames and revisions; never reuse a withdrawn or superseded ID.

Each finding has YAML front matter:

```yaml
---
id: KOR-001
title: "Replace with a scoped research title"
language_tags: [ko]
topic: entity-boundaries
status: draft
observation_confidence: low
hypothesis_outcome: untested
source_ids: []
research_issues: []
downstream:
  ner_evidence: []
  ner_eval: []
  fastner: []
  fastner_benchmarks: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
review:
  reviewer: null
  date: null
  scope: null
supersedes: []
superseded_by: []
---
```

Allowed values and review rules are defined in [CONVENTIONS.md](../CONVENTIONS.md). Dates are ISO calendar dates. Store issue/PR URLs in link lists. Drafts may have empty source lists; reviewed factual observations require traceable sources. The `reviewer` field must not imply independent review when the check was performed only by the author.

## Finding body template

### Question and scope

State the research question, varieties, scripts, domains, registers, entity types, and exclusions. Explain why the question matters to recognition.

### Observation

State the linguistic claim and cite source IDs with section/page locators. Separate documented behavior from an author's interpretation. Describe disagreements and confidence rationale.

### Illustrative examples and contrasts

For each example, provide:

| Field | Content |
| --- | --- |
| ID | A local example key, such as `example-01`. |
| Original text | Exact original-script string; preserve meaningful Unicode and whitespace. |
| Provenance | `synthetic`, `adapted`, or `attested`. |
| Source | Source ID and locator for adapted/attested text; author attribution for synthetic text. |
| Meaning | Translation plus gloss/transliteration when useful. |
| Boundary question | Candidate reading or proposed inclusion/exclusion; not gold annotation. |
| Contrast | Related non-name, alternate reading, or boundary counterexample. |
| Validation | Who checked the example, what was checked, and remaining uncertainty. |
| Reuse | Licensing or privacy constraints where applicable. |

Do not assign executable offsets here. Downstream fixture authors must follow the evidence repository's offset, normalization, and annotation contract.

### NER hypothesis

State a falsifiable prediction and its limits. Distinguish expected boundary behavior from entity classification behavior. Explain what result would challenge the hypothesis.

### Evidence handoff

Propose positive cases, hard negatives, boundary contrasts, and variation axes. Link the `ner-evidence` issue or state why the handoff is deferred or unnecessary.

### Evaluation handoff

Propose a slice and comparison that test the hypothesis. Discuss relevant precision/recall or boundary errors as questions, without claiming measurements. Link the `ner-eval` issue or record disposition.

### Implementation options

List candidate experiments and tradeoffs, including the current approach or a no-change baseline where useful. Avoid prescribing an implementation solely from a linguistic category. Link applicable `fastner` work.

### Limitations and review

Record exceptions, coverage gaps, missing expertise, source limitations, reviewer scope, and unresolved disagreements.

### Downstream outcomes and revisions

Link results and benchmark artifacts when available. State which scoped hypothesis was supported, rejected, or left unresolved. Record dates and materially changed claims. For superseded or withdrawn findings, preserve the reason and replacement links.

## Source record template

Assign stable source IDs such as `KOR-S001` in `sources.md`.

```yaml
id: KOR-S001
title: "Verified source title"
authors_or_institution: []
publication_date: null
url_or_identifier: "Verified URL, DOI, ISBN, or catalog identifier"
accessed: YYYY-MM-DD
source_type: "grammar | paper | official-guidance | corpus | other"
language_scope: []
relevant_locators: []
reuse_terms: "Record verified terms or state unknown"
limitations: []
```

Source records may be written as Markdown entries containing these fields. Never fill templates with fabricated bibliography. Cite only a short excerpt when necessary; prefer original summaries and links. Source material retains its original rights.

## Machine-checkable contracts

The [metadata schemas and validation guide](../schemas/README.md) implement these patterns. Use the [finding template](../templates/finding.md), [research taxonomy](../taxonomy.md) and [research issues](../research/README.md) when extending the initial four-language wave. Automated validation checks structure, not linguistic correctness.

## Completion check

Before merging a dossier change, check unique IDs, metadata consistency, source-to-claim mapping, example provenance, valid local links, explicit limitations, review status, and handoff disposition. A reviewed finding needs at least one meaningful contrast or counterexample, or a documented reason why one cannot yet be provided; any resulting review limitation must remain visible.
