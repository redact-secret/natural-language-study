# Japanese: The name edge can be inside a run or across a separator

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[JPN-001](findings/JPN-001.md) and [JPN-004](findings/JPN-004.md) identify segmentation/candidate risks. [JPN-002](findings/JPN-002.md) motivates exclusion of address/grammatical material as a proposed Japanese target policy, still requiring evidence-owner agreement.

[JPN-003](findings/JPN-003.md) gives the reverse challenge: the middle dot can occur inside a constructed name. A punctuation boundary rule and an address-suffix boundary rule need different evidence.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `アリスさんが来た。` | Alice came. | Propose アリス; candidate edge may be internal to a tokenizer unit. |
| `ジョン・ミラーが来た。` | John Miller came. | Propose connected name with middle dot retained, subject particle outside. |
| `山田はるかが来た。` | Yamada Haruka came. | Propose name across Han/hiragana transition; need context to find the later particle edge. |

## NER decision and falsifiable handoff

Ask ner-evidence to adjudicate suffix, connector and script-transition roles independently. Evaluate unreachable spans, truncation and suffix leakage separately; measure candidate coverage before using classification scores to compare architectures.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

No existing English/Korean title policy is silently extended to Japanese. Lists, rubric text, ruby and nested parentheticals need their own interpretation before offset fixtures are created.
