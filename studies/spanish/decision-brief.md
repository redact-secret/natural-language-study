# Spanish: decision brief and downstream proposal

**Decision: Treat double-surname connectors, surname-particle case, del/al contractions, cue words and Unicode form as separate experiments, and do not use a fixed name shape or case gate.** Scope is the [dossier scope](overview.md). This is draft desk research and a proposal for owner review; examples are synthetic and NER outcomes untested.

## Basis and uncertainty

[SPA-001](findings/SPA-001.md) rests on two legal texts read as summaries. [SPA-002](findings/SPA-002.md) and [SPA-004](findings/SPA-004.md) rest on RAE search excerpts because the RAE site was inaccessible; re-verify first. [SPA-006](findings/SPA-006.md) has no verified lexical source. Uncertainty is highest for Mexico and other Latin American varieties, which are unresearched.

## Evidence packet proposed to ner-evidence

Each row is a contrast family, not a fixture or sample count. Preserve original text, provenance and finding ID.

| Family | Source finding | Controlled comparison |
| --- | --- | --- |
| Double surname with connector | [SPA-001](findings/SPA-001.md): `Marín y Soto` versus coordination | Contextual connector rule vs capitalized-run baseline |
| Particle case | [SPA-002](findings/SPA-002.md): `de la Rosa` / `De la Rosa` / sentence-initial `De la` | Case-agnostic contextual membership |
| Contractions | [SPA-003](findings/SPA-003.md): internal vs external `del`, nickname article | Whole-token vs UD-split handling |
| Cues | [SPA-004](findings/SPA-004.md): `Sr.`, personal `a`, `A Coruña` | With and without cue features |
| Unicode | [SPA-005](findings/SPA-005.md): NFC, NFD, accent loss | Normalize-for-lookup with offsets vs raw |
| Homographs | [SPA-006](findings/SPA-006.md): `Pilar`, `Mercedes` | Lexicon-only vs context |

## Policy decisions before gold annotation

Whether titles, nickname articles and connector `y` belong inside PERSON spans; how nested persons within organizations are handled (CoNLL-2002 marks top-level only, [SPA-S013](sources.md#spa-s013)); how unresolved homograph contexts are recorded.

## Experiment proposed to ner-eval and fastner

Hold evidence snapshot, split, annotation policy, normalization contract and model fixed except the manipulated factor; separate identities and templates across splits. Report exact-span precision and recall, false positives on hard negatives, boundary error type and denominators by family; list unresolved cases separately. Compare runtime in `fastner` on the same workload. No threshold is defined.

## Rejected shortcut and reversal condition

Reject assuming one given name plus one or two surnames, requiring uppercase for particles, stripping every `del`/`al`, and treating accent deletion as canonical equivalence. Reopen if contextual rules do not reduce omissions or add false positives on the matched negatives.

## Handoff disposition

- `ner-evidence`: ready for owner review after source re-verification and language review; no adoption asserted.
- `ner-eval`: experiment questions specified; execution pending reviewed evidence.
- `fastner`: options specified; no code changed.
- `fastner-benchmarks`: deferred until evaluated artifacts exist.

## Review and provenance

2026-10-04: author source checks only; no qualified independent language review. [Sources](sources.md) record access failures and summary-only reads. No GitHub issue was created.
