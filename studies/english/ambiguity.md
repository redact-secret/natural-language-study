# English: Separate lexical collision, other entity types and incomplete context

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[ENG-S007](sources.md#eng-s007), rose verb and noun entries, confirms ordinary meanings for rose; [ENG-002](findings/ENG-002.md) shows why capitalization cannot independently establish PERSON. A sentence-initial noun can have the same visible case as a name.

Name/common-noun collision differs from a person/place collision or an organization bearing a name. The latter requires referential adjudication, not just a larger list of personal names. Short context may legitimately be insufficient.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Rose arrived.` | Intended reference to a fictional person named Rose. | Positive interpretation supplied for the constructed example. |
| `Rose petals fell.` | Petals of roses fell. | Identical capitalized prefix, common-noun modifier. |
| `The water rose.` | The water level increased. | Same letters with an independently sourced verb reading. |

## NER decision and falsifiable handoff

Use matched carrier contexts and casing transformations; prevent all negatives from being lowercase and all positives title-cased. Report false positives by collision type, not only aggregate F1. Include unresolved examples outside binary scoring until adjudicated.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

The dictionary supports the ordinary senses, not the synthetic PERSON annotation. Place/company metonymy and document-level disambiguation need dedicated evidence; no frequency estimate is available.
