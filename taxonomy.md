# Research taxonomy

These stable topic keys classify research questions. They are not downstream fixture fields, universal language classes or an implementation API. A finding has one primary `topic`; overview coverage may link it under multiple dimensions.

| Key | Record only what affects a testable NER question |
| --- | --- |
| `writing-system` | Script repertoire, orthography and Unicode representation; separate script from language. |
| `segmentation` | Spaces, morphological units and entity spans; distinguish within-token from across-token boundaries. |
| `morphology` | Specific productive affixes/clitics and their context; “agglutinative” alone selects no algorithm. |
| `naming-practices` | Name components/order, initials, titles, surname variants and mononyms, scoped to a community. |
| `casing` | Name/non-name discrimination and losses under lowercase, uppercase or sentence-initial casing. |
| `entity-boundaries` | Name-internal versus external punctuation, particles, clitics and titles. Gold policy belongs downstream. |
| `script-mixing` | Script changes, transliteration and borrowed forms; transliteration does not establish identity. |
| `ambiguity` | Person/common noun, person/place, person/organization; preserve uncertain contexts. |
| `context-and-word-order` | Local/distant context only when it motivates a controlled feature experiment. |
| `domain-and-register` | Edited prose versus messages, OCR and noise; constructed perturbation versus attested use. |

## Comparison axes

Describe observations, not mutually exclusive language buckets: boundary visibility; attachment direction and role; name-internal separators; casing availability; representation changes; ambiguity context. Record scope, source and exceptions alongside each value. A language may occupy multiple values by register or name type.

Morphological types (isolating, agglutinative, fusional, polysynthetic) may be source-backed descriptors but are not assigned wholesale by this first wave. No common language profile is inferred merely because Korean and Japanese share some attachment behavior.

## Evidence and review vocabulary

- Example provenance: `synthetic`, `adapted`, `attested`.
- Finding status: `draft`, `reviewed`, `superseded`, `withdrawn`.
- Observation confidence: `low`, `medium`, `high`, with rationale; independent of outcome.
- Hypothesis outcome: `untested`, `inconclusive`, `supported`, `not-supported`.
- Topic coverage: `not-started`, `in-progress`, `reviewed`, `out-of-scope`.

Source IDs, finding IDs and original-input fidelity are required at handoff. Slice names in findings are proposals, not registered `ner-eval` dimensions. See [conventions](CONVENTIONS.md), [schema](schemas/README.md) and [comparison](comparative/person-boundaries.md).
