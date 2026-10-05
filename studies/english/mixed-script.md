# English: Treat script, normalization and corruption as different axes

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[ENG-005](findings/ENG-005.md) is the canonical study. UAX #24 ([ENG-S008](sources.md#eng-s008)) separates character properties from language; UTS #39 ([ENG-S009](sources.md#eng-s009)) addresses confusability. Their NER implication is a hypothesis: retain raw forms and test eligibility rather than assigning entity type from script.

Accented Latin is not a script switch. A Hangul quotation inside English is a cross-script carrier example. Replacing one Latin letter with Cyrillic is an artificial corruption test. Pooling these loses the cause of a failure.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Élodie arrived.` | A fictional person arrived. | Latin with a diacritic, not mixed-script text. |
| `김민수 arrived.` | A fictional Kim Minsu arrived. | Hangul name in a constructed English carrier; not evidence of prevalence. |
| `Nоra arrived.` | Intended Nora arrived robustness case. | U+043E Cyrillic о replaces U+006F Latin o; preserve original coordinates. |

## NER decision and falsifiable handoff

Compare raw recognition with optional features on distinct slices: accented Latin, quoted names and confusable substitutions. Keep a script-matched ordinary-word control. Do not use a confusable skeleton as the emitted name or assume it establishes identity.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

This is a bounded representation study, not coverage of multilingual English usage. Cyrillic appears only in deliberate robustness inputs; independent review and natural corpus examples remain necessary.
