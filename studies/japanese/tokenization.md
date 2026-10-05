# Japanese: Verify internal edges before choosing an analyzer or model

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Japanese ordinary prose does not delimit all words with spaces, and corpus resources adopt different word units ([JPN-S001](sources.md#jpn-s001), Word Units). [JPN-001](findings/JPN-001.md) and [JPN-004](findings/JPN-004.md) separate that fact from the choice of NER architecture.

The pinned [runtime audit](../../research/runtime-boundary-audit.md) produced one OtherWord unit for アリスさんが. A candidate system restricted to those unit edges cannot isolate アリス without another boundary mechanism. This is a conditional capability result, not measured PERSON recall.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `アリスさんが来た。` | Alice came. | Need a possible edge before さん inside the observed run. |
| `田中さんが来た。` | Tanaka came. | Han segmentation exposes a different unit pattern; do not extrapolate kana behavior from it. |
| `お客さんが来た。` | A customer came. | An internal edge can be reachable without yielding a valid PERSON. |

## NER decision and falsifiable handoff

Compare current unit edges with subtoken candidates or an analyzer bridge on the same reviewed spans. Measure candidate reachability before model accuracy, then latency and candidate volume downstream. Character models are options, not a conclusion from no-space writing.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

The cited 2017 architecture experiment does not evaluate PERSON; it cannot substantiate PERSON superiority. Profile eligibility and all downstream candidate paths still need end-to-end verification.
