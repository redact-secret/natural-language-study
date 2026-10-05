# English: Separate candidate reachability from statistical recognition

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Whitespace supplies useful candidate breaks, but a full name can cross several tokens and punctuation can remain inside it. See [ENG-001](findings/ENG-001.md) and [ENG-003](findings/ENG-003.md), grounded in [ENG-S001](sources.md#eng-s001) and [ENG-S003](sources.md#eng-s003), Middle initials and Other things.

The pinned [runtime audit](../../research/runtime-boundary-audit.md) already observed a split after O’Neil in a possessive input. Replacing the tokenizer before checking remaining candidate and model behavior is therefore not justified by that example alone.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Dr. Nora E. Vale arrived.` | A doctor named Nora E. Vale arrived. | Propose Nora E. Vale, retaining the initial period but excluding Dr. |
| `Nora O’Neil’s report` | A person’s report. | Existing apostrophe split is a baseline capability, not a measured successful recognition. |
| `Nora and Evan arrived.` | Two people arrived. | Joining all capitalized tokens across a conjunction would over-merge. |

## NER decision and falsifiable handoff

First enumerate whether a candidate can cover the desired original-text span; then score whether it is selected. Include initial periods, internal connectors and coordinated people. Keep candidate generation and classifier comparisons separate.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Sentence segmentation around initials and abbreviations needs explicit downstream probes. The existing 11-input audit is narrow and pinned, not a current full-pipeline guarantee.
