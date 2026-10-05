# Korean: Freeze annotation policy before testing linguistic features

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

The target taxonomy 0.2.0 excludes josa, titles and specified informal suffix 이. Its external-corpus mismatch is documented in [KOR-004](findings/KOR-004.md), with [KOR-S005](sources.md#kor-s005) as the target source. A linguistically plausible analysis does not automatically authorize a different gold span.

[KOR-003](findings/KOR-003.md) adds a separate coordinate requirement: raw and normalized text are not interchangeable offset spaces. The target fixture contract uses NFC; any raw-input experiment needs an explicit projection or adapter.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `김민수는` | Kim Minsu, as topic. | Proposed target 김민수; particle outside. |
| `영철이가` | Yeongcheol, as subject. | Target excludes informal suffix 이 as well as subject 가; external annotation may differ. |
| `김 씨가` | Mr/Ms Kim, as subject. | Individual candidate 김; 씨 and 가 outside, provided the referent is an individual. |

## NER decision and falsifiable handoff

Prepare a policy crosswalk before importing NIKL cases. Report boundary errors under one pinned target policy, and record annotation disagreements separately. Include normalized/raw coordinate checks without storing invalid fixtures here.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Parenthesized alternate scripts are distinct spans under the inspected target rule, not one merged name. Collective clan readings remain a taxonomy question; this repository does not settle them by stripping 씨.
