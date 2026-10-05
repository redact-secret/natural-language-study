# Turkish: decision brief and downstream proposal

**Decision: before any Turkish PERSON fixture work, separate three suffix situations (apostrophe-marked, unmarked by rule, unmarked by noise) and test apostrophe-aware boundaries, case folding and diacritic folding as independent slices.** Scope is the [dossier scope](overview.md). This is draft desk research and a proposal ready for owner review; every outcome is untested.

## Basis

[TUR-001](findings/TUR-001.md) (apostrophe boundary), [TUR-002](findings/TUR-002.md) (no cue), [TUR-003](findings/TUR-003.md) (dotted and dotless I), [TUR-004](findings/TUR-004.md) (diacritic loss), [TUR-005](findings/TUR-005.md) (honorifics) and [TUR-006](findings/TUR-006.md) (name/noun collisions). Sources were mostly read as summaries or abstracts, see [sources](sources.md).

## Evidence packet proposed to ner-evidence

Each row is a contrast family, not a fixture or a sample count; examples need qualified Turkish review before adoption.

| Family | Required contrast | Controlled comparison |
| --- | --- | --- |
| Apostrophe suffix | Person, place, title, abbreviation, foreign name | Whitespace-only versus apostrophe-aware candidates |
| No apostrophe | Matched present/absent pairs; institution and plural exceptions | Same model, cue deleted |
| Dotted I | Title case, ALL CAPS, NFC/NFD | Default versus Turkish-aware folding |
| ASCII fold | Name versus collision word | Original versus folded input |
| Honorifics | With and without `Bey/Hanım/Efendi`, titles before | Two declared span policies |
| Name/noun | Cue present versus absent | Per-cue recall and precision |

## Policy decisions before annotation

Whether suffixes, plurals such as `Ahmetler`, and post-name honorifics are inside the PERSON span is an owner policy question; sources describe spelling, not annotation. Store the policy version with each fixture. Keep undecidable name/noun contexts in an adjudication bucket.

## Experiment proposed to ner-eval and fastner

Hold snapshot, split, model, decoding and scoring fixed except the manipulated factor. Report exact-span precision and recall, false positives on hard negatives, boundary error types and denominators per family. Compare cost on the same workload. No threshold is defined. Candidate implementations (apostrophe split feature, tr-aware fold, fold-insensitive lexicon key, deasciification pre-pass) are options, with a no-change baseline.

## Rejected shortcut and reversal condition

Reject suffix-list stripping as a stand-in for boundary research (it may truncate names) and reject treating any apostrophe as a person-suffix boundary (titles, abbreviations, foreign names). Reverse if matched tests show an apostrophe rule performing equally on noisy inputs or no case-fold effect.

## Handoff disposition

- `ner-evidence`: **ready for owner review**, subject to language review; no issue exists.
- `ner-eval`: slice proposals only (`tr-apostrophe-suffix`, `tr-no-apostrophe`, `tr-dotted-i-casing`, `tr-ascii-fold`, `tr-honorific-span`, `tr-name-noun-collision`); deferred until reviewed evidence exists.
- `fastner`: deferred; no code was inspected.
- `fastner-benchmarks`: deferred; no evaluated artifact.

## Review and provenance

2026-10-04: author self-check only; no qualified Turkish review, no measured result, no issue or commit created.
