# Japanese: Preserve written order and allow names across script changes

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[JPN-005](findings/JPN-005.md) records a historical family-first institutional recommendation and ambiguity between written forms and readings. It does not claim one order across all modern writing. Recognition can preserve a full observed name without recovering its pronunciation or parsing surname fields.

[JPN-002](findings/JPN-002.md) supplies address suffix questions. [JPN-003](findings/JPN-003.md) covers connectors and script context. These combine into a surface-span task; script transitions and titles should be evidence, not fixed schema validation.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `山田はるかさんが来た。` | Yamada Haruka came. | Synthetic Han/hiragana name; proposed internal transition is not the name end. |
| `ジョン・ミラーさんが来た。` | John Miller came. | Synthetic katakana name retaining middle dot U+30FB. |
| `Yamada Harukaさんが来た。` | Yamada Haruka came. | Latin name with following Japanese address form. |

## NER decision and falsifiable handoff

Evaluate name-order, written-script and address-form axes independently. Compare full-span coverage before introducing surname/given-name parsing. Review single-component references in context rather than demanding a full legal name.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

No exhaustive Japanese name readings or historical-character coverage is established. Parenthetical kana and ruby need source-specific extraction rules and an agreed annotation policy.
