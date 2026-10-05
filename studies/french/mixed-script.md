# French: Distinguish accented Latin from quoted names in another script

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[FRA-003](findings/FRA-003.md) covers canonical accents; [FRA-S007](sources.md#fra-s007), UAX #24 sections 2–3, supplies character-script properties. An accent alone does not turn a Latin name into a second writing system. A Hangul quotation in French is a different input class.

The engineering inference is to test quoted-name eligibility without forcing ASCII spelling. This is a bounded synthetic stress study; no source here establishes how often French prose uses those quotations or how they should be transliterated.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Élodie est arrivée.` | Élodie arrived. | Accented Latin baseline. |
| `Élodie est arrivée.` | Élodie arrived. | U+0045 plus U+0301 replaces U+00C9; canonical representation contrast, not transliteration. |
| `김민수 est arrivé.` | A fictional Kim Minsu arrived. | Constructed Hangul quotation in a French carrier sentence; distinct script-eligibility question. |

## NER decision and falsifiable handoff

Keep three slices: accented Latin, canonical decomposition and non-Latin quoted names. Compare candidate eligibility and exact original-text spans with appropriate ordinary-word controls. Do not pool a missing script capability with a normalization hash mismatch.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

French transliteration conventions and natural code-switching distributions remain unresearched. No identity equivalence between different scripts is asserted; metadata marks Hangul only as a constructed stress envelope.
