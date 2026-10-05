# Natural Language Study

Language structure research for evidence-driven multilingual named entity recognition.

`natural-language-study` records how writing systems, grammar, naming practices, and real-world language use affect entity recognition. It supplies traceable research findings and testable hypotheses to the FastNER ecosystem.

The goal is to understand languages before committing to tokenizer, feature, or language-profile abstractions. Research must identify concrete boundary and ambiguity problems, including counterexamples and variation within a language.

This repository is a research layer. Publication here does not establish that FastNER supports a language or that a proposed technique improves detection.

## Ecosystem responsibilities

| Repository | Responsibility |
| --- | --- |
| **natural-language-study** | Linguistic findings, sources, hypotheses, and research handoffs. |
| [ner-evidence](https://github.com/redact-secret/ner-evidence) | Reviewed, executable evidence cases, annotations, and corpus taxonomy. |
| [ner-eval](https://github.com/redact-secret/ner-eval) | Evaluation contracts, slices, measurements, and reproducible evaluation artifacts. |
| [fastner](https://github.com/redact-secret/fastner) | Inference runtime, tokenization, features, models, and language-profile implementation. |
| [fastner-benchmarks](https://github.com/redact-secret/fastner-benchmarks) | Benchmark presentation and evidence for product readiness and support decisions. |

Research proposes changes to these repositories; it does not override their review, annotation, evaluation, or release contracts. Final support claims belong to the product's release process, informed by benchmark evidence.

## Research workflow

1. Open a scoped research issue with questions, language variety, source strategy, and expected handoffs.
2. Record sourced observations and limitations in a language dossier.
3. Separate each observation from the NER hypothesis it motivates.
4. Specify contrasting examples, counterexamples, and a falsifiable evaluation question.
5. Review the finding and link downstream issues where evidence, measurement, or implementation work is warranted.
6. Link downstream results back to the finding, including negative results.

Issues coordinate research. Merged dossier files are the durable research record. Comments and closed issues alone do not complete a research task.

## Research dimensions

| Dimension | Questions to investigate |
| --- | --- |
| Writing systems | Which scripts and orthographic conventions affect observable entity cues? |
| Segmentation | Where can word boundaries and entity boundaries differ? |
| Morphology | How do affixes, inflection, particles, and clitics interact with names? |
| Naming practices | How do name order, titles, initials, compound names, and mononyms vary? |
| Casing | When is capitalization informative, absent, or unreliable? |
| Entity boundaries | Which punctuation and attached forms should be included or excluded? |
| Ambiguity | When can the same surface form represent a person, ordinary noun, place, or organization? |
| Context and word order | Which local or distant context helps disambiguation? |
| Script mixing | How do transliteration, borrowed forms, and code switching change recognition? |
| Domain and register | How do formal writing, messages, OCR, and noisy text differ? |

These dimensions organize questions, not universal implementation rules. A shared typological label is insufficient evidence for a shared algorithm.

## Initial research wave

Four scoped PERSON dossiers now include **24 substantive topic syntheses and 21 draft findings** (English 5, Korean 6, Japanese 5, French 5). Each provides source/example contrasts and a decision brief. All hypotheses remain **untested**; qualified language/example review is pending.

| Dossier | First decision to investigate |
| --- | --- |
| [English](studies/english/overview.md) | Apostrophe roles, casing ambiguity, initials and multipart names. |
| [Korean](studies/korean/overview.md) | Attached particles, scoped spacing/title rules, Hangul normalization. |
| [Japanese](studies/japanese/overview.md) | No-space segmentation, address suffixes, script/context cues. |
| [French](studies/french/overview.md) | Internal name particles versus external elision, compound names and accents. |

Start with the [research decisions](comparative/boundary-roles-and-candidate-capabilities.md), [runtime boundary audit](research/runtime-boundary-audit.md), [taxonomy](taxonomy.md) and [research queue](research/README.md). Five GitHub epics track the comparison and four languages; the research queue links each issue. Other languages remain future candidates, not active studies or supported languages.

## Repository layout

| Path | Contents |
| --- | --- |
| `README.md` | Project purpose, ecosystem boundaries, and entry points. |
| `CONVENTIONS.md` | Research quality, review, and contribution rules. |
| `conventions/research-purpose.md` | Research purpose, scope, and handoff contracts. |
| `conventions/dossier-files.md` | Dossier layout, metadata, and finding templates. |
| `studies/<language-key>/` | Language dossiers created as research starts. |
| `comparative/` | Cross-language syntheses linked to findings. |
| `taxonomy.md` | Stable research dimensions and comparison axes. |
| `schemas/`, `templates/` | Metadata contracts, narrative template and validation guide. |
| `research/README.md` | GitHub research epics and review priorities. |
| `scripts/validate_research.py` | Metadata, source and local-link consistency checks. |
| `.github/ISSUE_TEMPLATE/` | Scoped research issue and language epic templates. |

Run the [research validation command](schemas/README.md) before submitting changes. Automated checks do not replace linguistic review.

## Repository skills

Four discoverable skills live in `.agents/skills/`; invoke them by name or let the matching workflow select them. For a combined task, scope the dossier, investigate, document, then compare the defined phenomenon across languages.

- [dossier-initialize](.agents/skills/dossier-initialize/SKILL.md): initialize or audit bounded dossier scope without resetting existing IDs.
- [dossier-deep-research](.agents/skills/dossier-deep-research/SKILL.md): verify sources, pursue counterexamples and retain competing evidence.
- [dossier-document](.agents/skills/dossier-document/SKILL.md): reconcile findings and owner-ready decision briefs.
- [language-pattern-study](.agents/skills/language-pattern-study/SKILL.md): derive testable common capabilities and language-specific limits.

See the [first-wave application record](research/first-wave-skill-run.md) for concrete outputs from these skills. These workflows do not imply permission to modify downstream repositories or publish issues.

## Start a study

Read [the conventions](CONVENTIONS.md), [research purpose and scope](conventions/research-purpose.md), and [dossier file patterns](conventions/dossier-files.md). Then open a research issue and create the smallest dossier needed for its questions.

Contributions should favor a narrow, well-sourced finding with useful counterexamples over a broad survey without actionable evidence.

## License

Original repository contributions are licensed under the [MIT License](LICENSE.md), copyright Omiologic. Referenced works and third-party material retain their own licenses; citation does not grant redistribution rights.

## Expanded dossier results

See the [delivery audit](research/dossier-expansion.md) for new sources and remaining review limits, and [capability and referent comparison](comparative/capability-and-referent-matrix.md) for the controlled downstream sequence. Broad desk-research coverage does not establish independent review, measured accuracy or language support.
