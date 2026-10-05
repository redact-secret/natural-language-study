# French: Name-origin words can describe a category instead of naming a person

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[FRA-005](findings/FRA-005.md) adds antonomasia using [FRA-S006](sources.md#fra-s006), Definition and Notes. The relevant question is referential: is this a direct individual mention, a fictional-character mention or a category-like comparison?

Particle ambiguity is independent: deciding whether d’ is outside or inside a name changes its edge, while figurative use can change the entity label itself. Mixing both failures into a single boundary slice hides the remedy.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Julien Morel est arrivé.` | Julien Morel arrived. | Constructed direct reference to a fictional ordinary person. |
| `C’est un vrai don Juan.` | He is a real seducer. | Adapted source illustration; figurative/category-like reading requires policy. |
| `Le personnage Don Juan entre en scène.` | The character Don Juan enters the scene. | Constructed explicit fictional-character reference; taxonomy decides inclusion. |

## NER decision and falsifiable handoff

Ask evidence owners to record direct, fictional, figurative and lexicalized readings. Compare lexical-name matching with contextual classification only after policy is fixed. Avoid assigning all figurative forms to non-PERSON merely because they are figurative.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

This is one sourced semantic family. General person/place/company metonymy and lexical collision frequencies remain unmeasured. Source rhetoric terminology is not a gold-label scheme.
