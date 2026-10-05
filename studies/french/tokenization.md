# French: A Latin token may need an internal PERSON start

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[FRA-002](findings/FRA-002.md) requires considering a name beginning after external d’. The pinned [runtime audit](../../research/runtime-boundary-audit.md) kept d’Élodie as one Latin token, as it also did name-internal d’Aubemont. An edge-only candidate path may therefore need another start mechanism; full inference was not tested.

[FRA-003](findings/FRA-003.md) preserves internal hyphens and accents. An English-compatible Latin tokenizer is not by itself a French capability guarantee.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Le dossier d’Élodie` | Élodie’s file. | Possible start after d’, internal to the observed token. |
| `Élodie d’Aubemont` | A fictional full name. | Keep internal surname particle and join across space. |
| `Anne-Claire Évrard` | A fictional full name. | Retain first-name hyphen and accented surname. |

## NER decision and falsifiable handoff

Compare connector-preserving tokenization plus alternative start candidates with indiscriminate apostrophe splitting. Measure candidate reachability, false internal splits and final exact spans separately. Keep the classifier fixed for the first capability comparison.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

The audit only probed tokenization. French profile/model support was not demonstrated. A reachable internal edge is necessary for some designs but does not show that the name is correctly selected.
