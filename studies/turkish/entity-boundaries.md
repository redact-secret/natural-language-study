# Turkish entity boundaries: what sits inside or beside the PERSON span

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis from summaries and abstracts; independent review pending. NER proposals remain untested.

## Research answer and basis

Three boundaries recur: suffix after apostrophe ([TUR-001](findings/TUR-001.md)), honorific words ([TUR-005](findings/TUR-005.md)), and unmarked suffixes or plurals ([TUR-002](findings/TUR-002.md)). Orthographic sources describe spelling, not annotation; no Turkish NER corpus guideline was read ([TUR-S008](sources.md#tur-s008), [TUR-S009](sources.md#tur-s009) are abstracts only). Gold policy belongs downstream.

## Contrasts that challenge the shortcut

Examples are **synthetic** (invented, non-referential people, author-written, no native review) unless marked adapted from a cited source. They are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Zeynep Hanım'dan` (adapted form, TUR-S001 lists `Ayşe Hanım'dan`) | from Ms Zeynep | Name, honorific, suffix: three layers. |
| `Selim'in` versus `Selim Bey'in` | Selim's; Mr Selim's | Same name, different span-neighbours. |
| `Ahmetler` | the Ahmets | Plural: mention of one person? |

## NER decision and falsifiable handoff

Record the policy version with every fixture and compare candidate generators under each view. Disposition: proposal; [decision brief](decision-brief.md).

## Limits and next evidence

External corpus conventions for suffix inclusion remain unverified; obtain the Tür et al. and Şeker and Eryiğit annotation descriptions.

