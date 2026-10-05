# Research Purpose and Scope

## Purpose

Build a source-backed understanding of language behavior that informs multilingual entity recognition. Research should make hidden assumptions visible before those assumptions become tokenizer rules, model features, language profiles, or support claims.

The primary output is a linguistic finding with a bounded claim, reliable sources, useful contrasts, and a testable NER hypothesis. Documentation volume and the number of languages listed are not success measures by themselves.

## Questions this repository should answer

- Which observable forms distinguish names from non-names in a defined language variety and context?
- Where do linguistic word boundaries differ from desired entity boundaries?
- Which attached forms, titles, punctuation, and naming practices create ambiguity?
- Which assumptions fail across scripts, registers, domains, or varieties?
- What evidence and evaluation would determine whether a proposed feature helps?
- Which patterns justify a shared abstraction, and which need language-specific treatment?

## In scope

Research may cover writing systems, orthography, segmentation, morphology, name formation, name order, honorifics, casing, syntax, transliteration, code switching, and ambiguity when they affect a concrete recognition question.

Start with PERSON recognition and boundaries. Other entity types are allowed when they illuminate a PERSON contrast or have a separately stated research objective. Study noisy usage, OCR, informal text, and domain variation when these change the intended recognition behavior.

Foundational grammar surveys are useful when they identify relevant questions and link them to findings. Do not require every grammar topic to have an immediate implementation, but state why each investigated topic matters or why it remains exploratory.

Cross-language studies should compare the same defined phenomenon across explicitly scoped findings. Typological categories are descriptive starting points, not guarantees that languages can share code.

## Out of scope and owners

| Work | Owner |
| --- | --- |
| Executable positive/negative fixtures, annotation policy, gold spans, corpus splits | `ner-evidence` |
| Scoring, evaluation slices, reproducibility, evaluation artifacts | `ner-eval` |
| Tokenizers, features, trained models, runtime behavior, language-profile code | `fastner` |
| Benchmark reporting and readiness evidence | `fastner-benchmarks` |
| Release and language-support claims | Product release process, informed by benchmark evidence |

Research may propose contracts to these owners but cannot declare them adopted. Illustrative examples belong here; benchmark-ready copies and their gold annotations belong in `ner-evidence`.

This repository does not provide a comprehensive grammar encyclopedia, a replacement for linguistic expertise, a raw personal-data collection, or an automatic language-support certification system.

## Separate observation from engineering

Every actionable finding should distinguish four layers:

1. **Linguistic observation:** what a source establishes, within a named scope.
2. **NER hypothesis:** how that behavior may influence recognition or boundaries.
3. **Test proposal:** what contrasting cases and evaluation could falsify the hypothesis.
4. **Engineering options:** possible approaches with tradeoffs, pending experiments.

For example, a hypothetical study of attached name suffixes could motivate several options: character features, segmentation alternatives, contextual scoring, or explicit boundary handling. The observation alone does not select an algorithm. Mark such examples as hypothetical until reviewed sources establish the actual language behavior.

## Research selection

Prioritize a question when it addresses a current failure, challenges a cross-language assumption, enables a likely target language, or adds a meaningful contrast to existing research.

Use two complementary tracks:

- **Language dossiers:** understand a particular language variety across relevant dimensions.
- **Comparative studies:** compare a defined phenomenon across dossiers to identify reusable patterns and limits.

The first-wave language list in the README is a starting proposal. Revise priorities using source availability, target use cases, diversity of relevant phenomena, and downstream demand. Do not claim global representativeness from a small sample.

## Handoff contract

Each actionable finding records:

| Field | Required content |
| --- | --- |
| Finding reference | Stable ID, file link, and revision or commit reference when available. |
| Scope | Language tags, scripts, varieties, domains, registers, and entity types. |
| Claim and confidence | Observation, supporting sources, limitations, and confidence rationale. |
| Hypothesis | A prediction that evaluation could reject. |
| Evidence proposal | Positive cases, hard negatives, boundary contrasts, and variation axes. |
| Evaluation proposal | Suggested slice, measurement question, and comparisons; metrics follow `ner-eval` contracts. |
| Implementation options | Candidate experiments, relevant assumptions, and likely tradeoffs. |
| Destination | Linked issue or PR in the responsible repository, or an explicit deferred/no-action reason. |
| Outcome | Linked downstream artifacts and a scoped result, including negative outcomes. |

Research IDs should be retained in downstream issue descriptions or provenance fields supported by that repository. Do not invent a new mandatory fixture schema for another repository.

## Completion and success

A research task is complete when its question has a documented answer or a clearly documented unresolved state, sources and examples are checked, limitations are recorded, and handoffs are addressed. An unresolved finding can be valuable when it identifies precisely what evidence is missing.

Assess usefulness through traceable downstream experiments, improved case diversity, exposed assumptions, and decisions changed by evidence. A rejected hypothesis is a valid result. Never promote a linguistic finding into an accuracy, safety, or support claim without the responsible downstream evaluation and release process.
