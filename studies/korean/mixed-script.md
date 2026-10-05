# Korean: Romanization is a recognition variant, not reversible identity normalization

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[KOR-005](findings/KOR-005.md) gives the sourced romanization result. NIKL permits multiple presentation forms and retained established names; it does not make one converter output an exhaustive whitelist. [KOR-003](findings/KOR-003.md) concerns canonical Hangul normalization, which must stay distinct from romanization.

For Han/Hangul or Latin parenthetical alternates, the pinned target policy in the [runtime audit](../../research/runtime-boundary-audit.md) proposes separate surface spans. That is an annotation rule; it does not independently establish transliteration identity.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Min Yong-ha는 왔다.` | Min Yong-ha came. | Constructed Latin-to-Hangul boundary before topic particle. |
| `민용하(Min Yongha)가 왔다.` | Min Yongha came, with a Latin rendering in parentheses. | Constructed alternate presentation; review two spans under target policy. |
| `김민수(金民秀)가 왔다.` | A fictional Kim Minsu came, with an intended Han rendering. | Synthetic proposed rendering requires competent name-reading review; not an attested identity mapping. |

## NER decision and falsifiable handoff

Test Latin-name-plus-particle eligibility separately from cross-script alternate mentions and NFC/NFD fidelity. Ordinary Latin abbreviations with particles are necessary negatives. Keep original name spelling and coordinates when trying normalized matching.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Han readings and established individual romanizations require additional attestation. No cross-script identity resolver or measured mixed-script coverage is delivered.
