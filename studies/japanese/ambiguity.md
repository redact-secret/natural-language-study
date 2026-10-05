# Japanese: Kana and address forms are compatible with non-names

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[JPN-003](findings/JPN-003.md) proposes the katakana-name versus ordinary-loanword contrast. [JPN-002](findings/JPN-002.md) adds address expressions. Shogakukan’s dictionary lists both mirror and Miller readings ([JPN-S010](sources.md#jpn-s010), Digital Daijisen entries), corroborating the lexical collision. The constructed sentences do not establish ambiguity frequencies.

Name-form recognition and reading resolution are different tasks. [JPN-005](findings/JPN-005.md) shows why selecting a reading does not guarantee a unique original name or referent.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `ミラーさんが来た。` | Miller came. | Intended fictional surname with address suffix. |
| `ミラーを買った。` | [Someone] bought a mirror. | Intended ordinary-loanword reading; dictionary-backed lexical sense; sentence interpretation still needs qualified review. |
| `お客さんが来た。` | A customer came. | Address-like ending with an ordinary role noun, challenging suffix-only classification. |

## NER decision and falsifiable handoff

Use script-matched and suffix-matched controls so an experiment cannot win by memorizing katakana or さん. Vary predicate and particle context separately. Retain difficult or ambiguous readings for adjudication instead of assigning confident labels by shape.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Person/place and person/organization homographs remain gaps. Additional collision families and corpus attestation are required for broad ambiguity coverage; these synthetic contrasts motivate evidence, not estimates.
