# English: Possessive marking changes the edge, not the owner count

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Apostrophes can be name-internal or introduce grammatical material. [ENG-001](findings/ENG-001.md) separates those roles; [ENG-004](findings/ENG-004.md) adds joint possession. Cambridge [ENG-S001](sources.md#eng-s001), Apostrophe, and Purdue [ENG-S005](sources.md#eng-s005), possession rules, support the grammatical distinction. UD token units ([ENG-S004](sources.md#eng-s004), tokenization) are a separate annotation layer.

Do not interpret every final `s` as detachable morphology: a suffix decision requires a stem and a grammatical reading. Likewise, identifying a possessive phrase does not tell the system how many people occur inside it.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Nora O’Neil’s report` | Nora owns the report. | Propose Nora O’Neil; preserve internal apostrophe, exclude possessive material. |
| `Nora and Evan’s report` | Nora and Evan jointly own it. | Two proposed person mentions despite one possessive marker. |
| `The editor’s report` | An editor owns it. | Same possessive grammar without a personal name. |

## NER decision and falsifiable handoff

Compare role-aware edge handling with the current tokenizer/model on identical positive and common-noun controls. Measure suffix leakage and merged-person errors separately. A suffix splitter that improves edges but labels editor as PERSON has not solved recognition.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Plural family references and reduced is/has forms need separate evidence policies. No inference that all apostrophe-s strings are possessives.
