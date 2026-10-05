# Hindi: decision brief and downstream proposal

**Decision: Treat Hindi boundary policy, Unicode normalization and romanization as three separately declared variables before any Hindi PERSON evaluation; do not add a generic Hindi suffix stripper.** Scope is the [dossier scope](overview.md): Hindi only, PERSON, Devanagari with Latin contrasts. Nothing is claimed about other Indian languages. This is completed desk research and a proposal for owner review; examples remain draft and NER outcomes untested.

## Basis

- Postpositions follow names as separate words, but fuse to pronouns, so a suffix list targets the wrong unit ([HIN-001](findings/HIN-001.md)).
- Honorific tokens are separate unless name-internal, and three annotation designs treat them differently ([HIN-002](findings/HIN-002.md)).
- Nukta letters have two encodings that NFC unifies, but nukta dropping and bindu/chandrabindu are not normalization ([HIN-003](findings/HIN-003.md), [HIN-004](findings/HIN-004.md)).
- No casing cue exists in Devanagari, and names collide with ordinary words ([HIN-005](findings/HIN-005.md)).
- Romanization has no single mapping and code-mixed text keeps Hindi function words outside Latin names ([HIN-006](findings/HIN-006.md)).

## Evidence packet proposed to ner-evidence

Each row is a **contrast family**, not an executable fixture or sample count. Examples must be reviewed and sourced before use.

| Family | Source finding | Required contrasts | Controlled comparison |
| --- | --- | --- | --- |
| Postposition spacing | HIN-001 | Names plus each case marker; pronoun plus ने/को; ordinary noun plus marker; synthetic glued variants | Whitespace candidates versus suffix guard |
| Honorific policy | HIN-002 | Title plus name; name plus जी; name-internal श्री/जी | Same output scored under each declared policy |
| Unicode forms | HIN-003, HIN-004 | Precomposed and decomposed nukta; dropped nukta; bindu versus chandrabindu; joiners; danda; digits | Raw versus NFC versus key-folding, with offset map |
| Name/common-word | HIN-005 | Matched person and common readings; uncertain contexts kept | Contextual model with and without lexicon feature |
| Cross-script | HIN-006 | Devanagari, Roman cap, Roman lower, mixed script | Per-script recall and boundary errors |

## Policy decisions before gold annotation

Record per source whether titles, honorifics (श्री, जी) and postpositions are inside spans, and keep that version with every fixture. Keep original code points and the normalized view separate. Decide whether nukta dropping and bindu folding are matching aids only. These choices belong to the evidence owner; nothing here is a gold policy.

## Experiment proposed to ner-eval and fastner

Hold evidence snapshot, split, annotation policy, normalization contract and model fixed except for the manipulated factor. Separate template identities between splits. Report exact-span precision and recall, false positives on common-word and pronoun controls, and boundary error type, with denominators per family. No threshold is defined. For `fastner`: compare baseline, NFC at ingestion with offset map, a pronoun-aware suffix guard, and key folding; no code was inspected in this study, so no claim about the current implementation is made.

## Rejected shortcuts and reversal conditions

Reject: global suffix stripping; treating a title token as always outside or always inside; normalizing away nukta, bindu or joiners in stored text; deterministic romanization as identity. Reverse if matched slices show no difference from baseline, if a multilingual encoder already unifies the variants, or if reviewed data shows that the standard spacing norms are broken at a high rate (which would need a different test). A reversal on any one family does not affect the others.

## Handoff disposition

- `ner-evidence`: **ready for owner review** after Hindi language review and policy decisions; no issue opened.
- `ner-eval`: slices named in findings (hi-postposition-spacing, hi-honorific-policy, hi-nukta-forms, hi-diacritic-variants, hi-danda-final, hi-name-homograph, hi-cross-script-names) are proposals, not registered dimensions; deferred.
- `fastner`: options only; deferred.
- `fastner-benchmarks`: defer; no evaluated artifact.
- Comparative: no Hindi comparison was written; any comparison with Urdu, Marathi or Bengali needs those dossiers.

## Review and provenance

2026-10-04: produced by the dossier-initialize, dossier-deep-research and dossier-document procedures. Author checks of sources, Unicode computation and examples completed; independent Hindi language review is not recorded. The Hindi grammar, naming-practice source and primary romanization standards remain unobtained. [Source records](sources.md) hold locators and limitations.
