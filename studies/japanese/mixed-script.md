# Japanese: Use character properties without turning them into entity edges

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

UAX #24 [JPN-S008](sources.md#jpn-s008), section 3 table 7, assigns U+30FC a Common script value with Hiragana/Katakana Script_Extensions; U+3099 is Inherited with those extensions. A naive change-of-Script detector can therefore interrupt coherent kana text. This is a character-property observation, not a successful NER algorithm.

[JPN-003](findings/JPN-003.md) owns the broader script-boundary hypothesis. [JPN-005](findings/JPN-005.md) distinguishes rendering from identity. Canonical and compatibility transformations remain different operations under [JPN-S004](sources.md#jpn-s004).

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `メアリーさんが来た。` | Mary came. | U+30FC inside the synthetic katakana name must not mechanically terminate it. |
| `山田はるかさんが来た。` | Yamada Haruka came. | Han/hiragana transition inside the intended name. |
| `Johnさんが来た。` | John came. | Latin/hiragana transition at the proposed name edge in this constructed case. |

## NER decision and falsifiable handoff

Compare raw script-change features with contextual script-extension handling, holding reviewed spans fixed. Include long-vowel marks, voiced combining marks and ordinary kana words. Test width normalization in a separate slice and preserve an original-text mapping.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Japanese uses several scripts naturally; that is not equivalent to artificial homoglyph substitution. Character properties do not establish name readings, identity links or the prevalence of mixed-script names.
