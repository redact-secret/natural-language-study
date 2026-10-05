# French: External elision and internal particles need separate analyses

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[FRA-002](findings/FRA-002.md) describes external elided de next to a name, based on [FRA-S002](sources.md#fra-s002). [FRA-001](findings/FRA-001.md) addresses name-internal particles. Their shared visible letters do not imply a shared inclusion rule.

UD [FRA-S004](sources.md#fra-s004), Tokenization and Nominal Features, treats some contractions as multiple syntactic words and expresses nominal predicate relations through prepositions. That syntactic segmentation is not a PERSON boundary contract; do not import its contraction split blindly into surname handling.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Le dossier d’Élodie est prêt.` | Élodie’s file is ready. | External d’ before proposed Élodie. |
| `Élodie d’Aubemont est arrivée.` | Élodie d’Aubemont arrived. | Constructed name-internal d’ retained in the surname. |
| `Le dossier d’archives est prêt.` | The archival file is ready. | Same elision pattern without a personal name. |

## NER decision and falsifiable handoff

Compare contextual prefix-role features with global apostrophe splitting. Hold typography fixed while changing the grammatical role. Include ordinary nouns to test whether suffix/prefix mechanics merely overgenerate person candidates.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

The overview of French UD contains a contraction typo noted in its source record; that example is not used. This study does not require a full French morphological analyzer.
