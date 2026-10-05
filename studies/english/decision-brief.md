# English: decision brief and downstream proposal

**Decision: Keep existing apostrophe segmentation; test mention joining and cue robustness.** Scope is the [dossier scope](overview.md). This is completed desk research and a proposal ready for owner review; examples remain draft and NER outcomes untested.

## Additional decisions from the broad dossier

[ENG-005](findings/ENG-005.md) adds script eligibility as a separate capability question. First retain the existing apostrophe baseline and test joining/context; then test quoted-script eligibility with script-matched ordinary words. Compare accented Latin, quoted Hangul and artificial Cyrillic substitutions separately. Do not confound natural name variants with adversarial corruption. The [ambiguity synthesis](ambiguity.md) adds a dictionary-backed ordinary-word control.

## What changed after deeper research

[ENG-004](findings/ENG-004.md) adds the source-backed distinction missing from the first pass. The [pinned runtime audit](../../research/runtime-boundary-audit.md) separates mechanisms already present from candidate capability questions. Its tokenizer traces are observations, not recognition scores.

## Evidence packet proposed to ner-evidence

Each row is a **contrast family**, not an executable fixture or a fixed sample count. Expand with independently reviewed names and registers; preserve original text, provenance and finding ID.

| Family | Required contrast / source finding | Controlled comparison |
| --- | --- | --- |
| Apostrophe roles | [ENG-001](findings/ENG-001.md): Internal O’Neil versus external ’s and common-noun possessives | Current tokenizer vs context-sensitive changes only if reviewed cases expose a gap |
| Casing ambiguity | [ENG-002](findings/ENG-002.md): Rose as name/common noun; same sentence position and case condition | Case-only shortcut vs lexical/context features with matched negatives |
| Name components | [ENG-003](findings/ENG-003.md): Initials, lowercase internal components, titles and non-name letter labels | Component-capable candidates vs restricted title-case chains |
| Coordinated possessors | [ENG-004](findings/ENG-004.md): Shared/separate possession and role-noun coordinations | Same units/candidates, change joining constraint; count person merges |

## Policy decisions before gold annotation

Use existing ner-evidence rules for excluded titles/possessive ’s and included name initials/periods and generational suffixes. Review separate versus collective mentions and uncertainty handling without silently changing that contract. A possessive phrase can mention multiple people. Do not let a grammar grouping silently become one entity.

## Experiment proposed to ner-eval and fastner

Hold evidence snapshot, split, annotation policy, normalization contract, model artifact and decoding settings fixed where they are not the manipulated factor. Keep identities/templates separated across splits to avoid lexical leakage. When changing segmentation, first measure candidate endpoint coverage; then retrain comparable models under a stated training budget rather than feeding an old model incompatible units.

Report exact-span precision/recall, false-positive counts on hard negatives, boundary error type and denominators by family. List unresolved cases separately instead of silently counting one interpretation as gold. Compare runtime/memory on the same workload in `fastner`. No release threshold is defined by this study.

## Rejected shortcut and reversal condition

Reject tokenizer replacement based solely on the presence of apostrophes; the inspected baseline already preserves O’Neil and separates possessive ’s. Reject a capitalization gate as the only name criterion.

A reviewed counterexample where the tokenizer lacks a necessary endpoint reopens segmentation work; otherwise prefer a narrower joining/context experiment.

## Handoff disposition

- `ner-evidence`: **ready for owner review**, subject to language/example and policy adjudication; no adoption asserted.
- `ner-eval`: experiment question specified; execution pending reviewed evidence and compatible candidates.
- `fastner`: scoped experiment options specified; downstream code unchanged.
- `fastner-benchmarks`: defer until evaluated artifacts exist; no language-support claim.

## Review and provenance

2026-10-04: produced with dossier-initialize (existing-scope audit), dossier-deep-research and dossier-document. Author source checks and tokenizer probing completed; qualified independent language review not recorded. [Source records](sources.md) distinguish source restrictions, corpus conventions and unresolved disagreement. Research issue links are in [the overview](overview.md).
