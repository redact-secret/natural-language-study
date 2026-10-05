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

## Initial research candidates

The proposed first wave includes English, Korean, Japanese, Mandarin Chinese, Arabic, Spanish, Turkish, Russian, Hindi, and Vietnamese. These are research candidates, not supported languages or a complete representation of global language diversity.

Every study must declare the varieties, scripts, regions, registers, and entity types it actually covers. Broad labels such as “Chinese” or “Arabic” must not hide narrower evidence. Begin with PERSON; extend to other entity types only when the research question justifies it.

## Repository layout

| Path | Contents |
| --- | --- |
| `README.md` | Project purpose, ecosystem boundaries, and entry points. |
| `CONVENTIONS.md` | Research quality, review, and contribution rules. |
| `conventions/research-purpose.md` | Research purpose, scope, and handoff contracts. |
| `conventions/dossier-files.md` | Dossier layout, metadata, and finding templates. |
| `studies/<language-key>/` | Language dossiers created as research starts. |
| `comparative/` | Cross-language syntheses added when findings support comparison. |

The `studies/` and `comparative/` paths describe the planned structure; this starter contains the five governance documents only.

## Start a study

Read [the conventions](CONVENTIONS.md), [research purpose and scope](conventions/research-purpose.md), and [dossier file patterns](conventions/dossier-files.md). Then open a research issue and create the smallest dossier needed for its questions.

Contributions should favor a narrow, well-sourced finding with useful counterexamples over a broad survey without actionable evidence.

## License

Original repository contributions are licensed under the [MIT License](LICENSE.md), copyright Omiologic. Referenced works and third-party material retain their own licenses; citation does not grant redistribution rights.
