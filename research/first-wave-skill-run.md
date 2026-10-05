# First-wave skill application: 2026-10-04

Historical snapshot of the first skill application. The subsequent [dossier expansion](dossier-expansion.md) provides the current topic coverage and counts.
This record connects the new reusable skills to their actual outputs. Four existing dossier identities and all 12 original finding IDs were preserved; four new findings were appended. No downstream repository was modified or new GitHub message posted.

## Scope audit with dossier-initialize

Existing dossiers remain en-GB/en-US (ENG), ko-KR (KOR), ja-JP (JPN), fr-FR/fr-CA (FRA). Directory keys, unique prefixes, scope, issue URLs and review status were checked. Sources from another editorial context do not silently expand the study’s corpus scope.

The next question per language was narrowed to coordinated possessors (English), name suffix versus case and target-policy compatibility (Korean), within-kana unit boundaries (Japanese), and competing surname-particle casing rules (French). No empty dossiers/topic files were regenerated. Normalization coverage was not retained as a substitute for script-mixing research.

## Investigation with dossier-deep-research

Eight source records were added: English 2, Korean 3, Japanese 2, French 1. These are source records, not eight independent confirmations. Korean grammar and NER annotation reports share a commissioning institution; the pinned ner-evidence taxonomy is an engineering contract. The Japanese paper’s PERSON applicability was checked rather than assumed.

The Korean 2022 report required downloading the original PDF after web access failed. Relevant title pages and PDF p. 149 were inspected through text extraction; its source record retains document digest and exact locator. No full source text was added to this repository.

A separate [runtime audit](runtime-boundary-audit.md) records the inspected revisions, clean/dirty scope and 11 tokenizer probes. It exposes concrete candidate capability questions without producing gold annotations or F1 scores.

## Publication in dossier files with dossier-document

- [ENG-004](../studies/english/findings/ENG-004.md) and [English decision brief](../studies/english/decision-brief.md).
- [KOR-004](../studies/korean/findings/KOR-004.md) and [Korean decision brief](../studies/korean/decision-brief.md).
- [JPN-004](../studies/japanese/findings/JPN-004.md) and [Japanese decision brief](../studies/japanese/decision-brief.md).
- [FRA-004](../studies/french/findings/FRA-004.md) and [French decision brief](../studies/french/decision-brief.md).

Each brief identifies a decision, four contrast families, policy dependencies, baseline/comparison, reversal condition and handoff disposition. “Ready for owner review” means the proposal is concrete; it does not mean examples are independently reviewed or a downstream contract has adopted it.

## Synthesis with language-pattern-study

[Boundary roles and candidate capabilities](../comparative/boundary-roles-and-candidate-capabilities.md) distinguishes shared operations from linguistic causes and target policy. It rejects universal stripping, one-token names, unconditional case/script gates and conflated normalization operations. The earlier [boundary comparison](../comparative/person-boundaries.md) remains as the first-pass context and points to the newer study.

## Validation and completion state

Validation passed for 4 dossiers, 16 findings and 47 authored Markdown files, including skill reference links. All four skill-creator metadata/scaffold checks passed; `git diff --check` passed. The skills were exercised against the actual four-dossier task; no independent language review is claimed. The desk-research outputs and local handoff proposals are complete for the scoped questions. All 16 findings remain draft; all NER hypotheses remain untested. Existing epics remain open.
