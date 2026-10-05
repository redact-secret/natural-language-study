# French: The apostrophe role matters more than its glyph

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[FRA-002](findings/FRA-002.md) supplies the external/internal d’ contrast; [FRA-001](findings/FRA-001.md) and [FRA-004](findings/FRA-004.md) prevent case from deciding particle membership. [FRA-003](findings/FRA-003.md) adds a separate normalization concern.

A proposed French annotation contract should state title exclusion, internal particle/hyphen inclusion and external preposition exclusion before fixtures are written. These are handoff proposals, not already-adopted target policy.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Le dossier d’Élodie` | Élodie’s file. | Propose Élodie, excluding external d’. |
| `Élodie d’Aubemont` | A fictional full name. | Propose full observed name including internal d’. |
| `Mme Anne-Claire Évrard` | Ms Anne-Claire Évrard. | Propose name without Mme; period variants need the same policy decision. |

## NER decision and falsifiable handoff

Cross external/internal apostrophe role with straight/curly typography; keep the semantic reading and name constant. Separate left-edge errors, lost internal components and coordinate errors. Review raw/NFC mapping before importing normalization contrasts into target fixtures.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

An apostrophe glyph substitution is not necessarily Unicode canonical equivalence. No automatic normalization of a person’s preferred spelling is authorized by the boundary proposal.
