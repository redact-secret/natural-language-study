# Japanese: decision brief and downstream proposal

**Decision: Establish kana endpoint capability and profile eligibility before PERSON model selection.** Scope is the [dossier scope](overview.md). This is completed desk research and a proposal ready for owner review; examples remain draft and NER outcomes untested.

## Additional decisions from the broad dossier

[JPN-005](findings/JPN-005.md) adds written-order and reading limitations. The [mixed-script synthesis](mixed-script.md) adds U+30FC/U+3099 Script_Extensions, preventing a naive property change from becoming an unconditional boundary. Retain kana candidate reachability as the first experiment; then test script- and suffix-matched ordinary-word controls. Do not make name-part parsing or reading recovery prerequisites for recognition.

## What changed after deeper research

[JPN-004](findings/JPN-004.md) adds the source-backed distinction missing from the first pass. The [pinned runtime audit](../../research/runtime-boundary-audit.md) separates mechanisms already present from candidate capability questions. Its tokenizer traces are observations, not recognition scores.

## Evidence packet proposed to ner-evidence

Each row is a **contrast family**, not an executable fixture or a fixed sample count. Expand with independently reviewed names and registers; preserve original text, provenance and finding ID.

| Family | Required contrast / source finding | Controlled comparison |
| --- | --- | --- |
| Word versus entity unit | [JPN-001](findings/JPN-001.md): Identical raw text under multiple analyzer segmentations | Measure endpoint coverage with a fixed reviewed PERSON set |
| Address and particle roles | [JPN-002](findings/JPN-002.md): Bare name, name+さん+particle and みなさん control | Keep suffix and particle over-inclusion separate |
| Script cues | [JPN-003](findings/JPN-003.md): Kana names, ordinary loanwords, middle dots and Latin+suffix | Script features with context versus script-run shortcut |
| Within-unit endpoints | [JPN-004](findings/JPN-004.md): アリスさんが versus Han-name controls and bare kana+particle | Character candidates vs analyzer or hybrid candidates, then same-data NER comparison |

## Policy decisions before gold annotation

Resolve address-suffix inclusion, partial names and middle-dot membership. Do not inherit UD word annotations as PERSON gold. A PERSON-specific held-out set is needed; the inspected 2017 paper does not provide PERSON performance evidence.

## Experiment proposed to ner-eval and fastner

Hold evidence snapshot, split, annotation policy, normalization contract, model artifact and decoding settings fixed where they are not the manipulated factor. Keep identities/templates separated across splits to avoid lexical leakage. When changing segmentation, first measure candidate endpoint coverage; then retrain comparable models under a stated training budget rather than feeding an old model incompatible units.

Report exact-span precision/recall, false-positive counts on hard negatives, boundary error type and denominators by family. List unresolved cases separately instead of silently counting one interpretation as gold. Compare runtime/memory on the same workload in `fastner`. No release threshold is defined by this study.

## Rejected shortcut and reversal condition

Reject script transitions as the sole boundary rule and copying Korean profile activation as a complete Japanese solution. Reject importing non-PERSON paper scores as a PERSON benchmark.

If reviewed PERSON spans already have adequate endpoints under a chosen analyzer, prefer that narrower candidate strategy unless controlled quality/cost evidence favors character candidates.

## Handoff disposition

- `ner-evidence`: **ready for owner review**, subject to language/example and policy adjudication; no adoption asserted.
- `ner-eval`: experiment question specified; execution pending reviewed evidence and compatible candidates.
- `fastner`: scoped experiment options specified; downstream code unchanged.
- `fastner-benchmarks`: defer until evaluated artifacts exist; no language-support claim.

## Review and provenance

2026-10-04: produced with dossier-initialize (existing-scope audit), dossier-deep-research and dossier-document. Author source checks and tokenizer probing completed; qualified independent language review not recorded. [Source records](sources.md) distinguish source restrictions, corpus conventions and unresolved disagreement. Research issue links are in [the overview](overview.md).
