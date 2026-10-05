# English: Make inclusion decisions by role

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

The target contract summarized in the [runtime audit](../../research/runtime-boundary-audit.md) excludes English titles and possessives, retains initial periods and generational suffixes, and excludes postnominal degrees. This is target annotation policy, not a linguistic theorem. [ENG-001](findings/ENG-001.md), [ENG-003](findings/ENG-003.md) and [ENG-004](findings/ENG-004.md) supply its linguistic stress cases.

Apostrophe, period and whitespace each occur in both boundary and internal roles. A global punctuation strip would erase distinctions before they can be decided.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Nora E. Vale, PhD, spoke.` | A named person with a degree spoke. | Candidate Nora E. Vale; degree and separating comma stay outside. |
| `Nora O’Neil’s report` | The report of a named person. | Internal versus external apostrophe roles within one phrase. |
| `Nora and Evan’s report` | Report jointly associated with two people. | Do not turn a possessive constituent into one PERSON span. |

## NER decision and falsifiable handoff

Give ner-evidence a role-by-punctuation contrast set, then ask ner-eval to distinguish left-edge leakage, right-edge leakage, truncation and merging. Hold the entity referent fixed when comparing typography variants.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Collective surnames, institutions named after people and figurative references require policy decisions. Exact offsets remain downstream; do not copy raw-normalization examples into NFC fixtures without mapping.
