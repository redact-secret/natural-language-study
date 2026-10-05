# French: decision brief and downstream proposal

**Decision: Separate external elision, internal surname particles and normalization into distinct experiments.** Scope is the [dossier scope](overview.md). This is completed desk research and a proposal ready for owner review; examples remain draft and NER outcomes untested.

## Additional decisions from the broad dossier

[FRA-005](findings/FRA-005.md) adds direct versus figurative reference. First agree French title/particle boundaries and figurative/fictional-person policy, then test internal starts and normalization separately. A name lexicon alone cannot settle antonomasia. The [mixed-script synthesis](mixed-script.md) distinguishes accented Latin, canonical decomposition and constructed Hangul quotations; only the first two have normalization-specific motivation.

## What changed after deeper research

[FRA-004](findings/FRA-004.md) adds the source-backed distinction missing from the first pass. The [pinned runtime audit](../../research/runtime-boundary-audit.md) separates mechanisms already present from candidate capability questions. Its tokenizer traces are observations, not recognition scores.

## Evidence packet proposed to ner-evidence

Each row is a **contrast family**, not an executable fixture or a fixed sample count. Expand with independently reviewed names and registers; preserve original text, provenance and finding ID.

| Family | Required contrast / source finding | Controlled comparison |
| --- | --- | --- |
| Internal particles | [FRA-001](findings/FRA-001.md): Internal de/d’/du/des versus external prepositions | Contextual membership vs capitalization-run shortcut |
| External elision | [FRA-002](findings/FRA-002.md): d’Élodie versus internal d’Aubemont and d’assurance | Expose optional within-unit start candidates; retain punctuation in source |
| Compound/Unicode form | [FRA-003](findings/FRA-003.md): Hyphenated names/common nouns and NFC/NFD accented names | Canonical lookup with source mapping vs raw baseline; accent deletion separate |
| Casing disagreement | [FRA-004](findings/FRA-004.md): Documented du/Du variants and external du phrases | Case-robust contextual membership, without normalizing person identity |

## Policy decisions before gold annotation

Define internal-particle inclusion and title treatment. Preserve attested name spelling. Record editorial context; neither OQLF nor the federal guide provides a universal capitalization key for entity membership.

## Experiment proposed to ner-eval and fastner

Hold evidence snapshot, split, annotation policy, normalization contract, model artifact and decoding settings fixed where they are not the manipulated factor. Keep identities/templates separated across splits to avoid lexical leakage. When changing segmentation, first measure candidate endpoint coverage; then retrain comparable models under a stated training budget rather than feeding an old model incompatible units.

Report exact-span precision/recall, false-positive counts on hard negatives, boundary error type and denominators by family. List unresolved cases separately instead of silently counting one interpretation as gold. Compare runtime/memory on the same workload in `fastner`. No release threshold is defined by this study.

## Rejected shortcut and reversal condition

Reject removing every d’ and rejecting every lowercase particle. Reject assuming that retaining a combining mark inside a token makes its lexical hash canonical-equivalent.

Reopen the design if contextual membership does not reduce omissions without adding external function words. Any canonical normalization must preserve original coordinates and must not turn accent deletion into identity equivalence.

## Handoff disposition

- `ner-evidence`: **ready for owner review**, subject to language/example and policy adjudication; no adoption asserted.
- `ner-eval`: experiment question specified; execution pending reviewed evidence and compatible candidates.
- `fastner`: scoped experiment options specified; downstream code unchanged.
- `fastner-benchmarks`: defer until evaluated artifacts exist; no language-support claim.

## Review and provenance

2026-10-04: produced with dossier-initialize (existing-scope audit), dossier-deep-research and dossier-document. Author source checks and tokenizer probing completed; qualified independent language review not recorded. [Source records](sources.md) distinguish source restrictions, corpus conventions and unresolved disagreement. Research issue links are in [the overview](overview.md).
