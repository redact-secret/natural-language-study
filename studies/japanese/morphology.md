# Japanese: Suffix and particle context must remain visible after segmentation

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[JPN-002](findings/JPN-002.md) separates address suffix さん from following particles. The Japan Foundation lesson ([JPN-S002](sources.md#jpn-s002), lesson 3 audio script) supports a narrow pedagogical use; it is not a complete title inventory. UD [JPN-S001](sources.md#jpn-s001), Word Units, describes alternative morphological unit choices.

The NER proposal is to retain these units as context while deciding the name edge. It does not follow that every sequence before さん is an individual's name or that one analyzer's token labels supply gold boundaries.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `田中さんが来た。` | Tanaka came. | Propose 田中, treating さん and が separately from the name. |
| `田中さんも来た。` | Tanaka also came. | Change following particle while holding the intended name fixed. |
| `お客さんが来た。` | A customer came. | Constructed ordinary-role expression with さん; negative for a personal-name detector. |

## NER decision and falsifiable handoff

Compare suffix/context features on personal names and ordinary role nouns with the same ending. Evaluate boundary leakage and non-name false positives separately, after Japanese evidence owners decide title policy.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Honorific inventories, humble/polite expressions and verbal morphology are not comprehensively covered. Source-backed lesson examples do not establish model gains or universal suffix stripping.
