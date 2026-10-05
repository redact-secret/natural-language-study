# Korean: decision brief and downstream proposal

**Decision: Preserve ner-evidence 0.2.0 and explicitly map external suffix annotations; exploit existing syllable boundaries.** Scope is the [dossier scope](overview.md). This is completed desk research and a proposal ready for owner review; examples remain draft and NER outcomes untested.

## Additional decisions from the broad dossier

[KOR-005](findings/KOR-005.md) adds romanized name variation; [KOR-006](findings/KOR-006.md) adds individual versus surname-category/collective reference. After freezing the source-to-target suffix mapping, test Latin-name-plus-particle candidate eligibility and 씨 contexts independently. Review collective references before assigning gold; longest-suffix removal cannot resolve entity class. See [mixed script](mixed-script.md) and [ambiguity](ambiguity.md).

## What changed after deeper research

[KOR-004](findings/KOR-004.md) adds the source-backed distinction missing from the first pass. The [pinned runtime audit](../../research/runtime-boundary-audit.md) separates mechanisms already present from candidate capability questions. Its tokenizer traces are observations, not recognition scores.

## Evidence packet proposed to ner-evidence

Each row is a **contrast family**, not an executable fixture or a fixed sample count. Expand with independently reviewed names and registers; preserve original text, provenance and finding ID.

| Family | Required contrast / source finding | Controlled comparison |
| --- | --- | --- |
| Particle attachment | [KOR-001](findings/KOR-001.md): Single/stacked particles on names and ordinary nouns | Fixed syllable tokenizer; boundary context features vs baseline |
| Name/title spacing | [KOR-002](findings/KOR-002.md): Joined/clarified names, titles and deliberately nonstandard glued forms | Keep normative and noisy slices distinct; identify statistical vs sequence backend |
| Hangul representation | [KOR-003](findings/KOR-003.md): NFC/NFD forms and non-name controls | Existing jamo composition path vs raw source-coordinate checks |
| Suffix versus case 이 | [KOR-004](findings/KOR-004.md): Given-name suffix+particle, full-name+case and non-name nouns | Compare source/target policy explicitly before measuring boundary errors |

## Policy decisions before gold annotation

[KOR-004](findings/KOR-004.md) verifies an actual mismatch: NIKL includes name-attached 이, while ner-evidence 0.2.0 excludes it. Keep the target contract unless its owner versions a change. Imports must record the source rule and justified transformation; ambiguous suffix analyses need adjudication. Both policies exclude grammatical particles. Apply existing title exclusions and person-referring surname-only acceptance; review genuinely ambiguous contexts. Store policy version with evidence so apparent recall changes do not merely reflect changed gold boundaries.

## Experiment proposed to ner-eval and fastner

Hold evidence snapshot, split, annotation policy, normalization contract, model artifact and decoding settings fixed where they are not the manipulated factor. Keep identities/templates separated across splits to avoid lexical leakage. When changing segmentation, first measure candidate endpoint coverage; then retrain comparable models under a stated training budget rather than feeding an old model incompatible units.

Report exact-span precision/recall, false-positive counts on hard negatives, boundary error type and denominators by family. List unresolved cases separately instead of silently counting one interpretation as gold. Compare runtime/memory on the same workload in `fastner`. No release threshold is defined by this study.

## Rejected shortcut and reversal condition

Reject global suffix deletion and the claim that every 이 is a case marker. Reject reimplementing Hangul NFC/NFD segmentation before checking the existing composition path.

The verified source/target policy disagreement requires an explicit import mapping or separate evaluation views; a reviewed boundary absent from current units would justify a tokenizer experiment.

## Handoff disposition

- `ner-evidence`: **ready for owner review**, subject to language/example and policy adjudication; no adoption asserted.
- `ner-eval`: experiment question specified; execution pending reviewed evidence and compatible candidates.
- `fastner`: scoped experiment options specified; downstream code unchanged.
- `fastner-benchmarks`: defer until evaluated artifacts exist; no language-support claim.

## Review and provenance

2026-10-04: produced with dossier-initialize (existing-scope audit), dossier-deep-research and dossier-document. Author source checks and tokenizer probing completed; qualified independent language review not recorded. [Source records](sources.md) distinguish source restrictions, corpus conventions and unresolved disagreement. Research issue links are in [the overview](overview.md).
