# Turkish person names: given name first, surname law, titles on both sides

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis from summaries and abstracts; independent review pending. NER proposals remain untested.

## Research answer and basis

The 1934 Surname Law fixed surnames and given-name-first order ([TUR-S013](sources.md#tur-s013), secondary reproduction). TDK capitalization guidance shows titles before (`Sayın`, `Dr.`, `Prof. Dr.`, `Bay`) and after (`Bey`, `Hanım`, `Efendi`) names ([TUR-S002](sources.md#tur-s002)). [TUR-005](findings/TUR-005.md) owns the claim; [TUR-006](findings/TUR-006.md) owns name/noun collisions. `-oğlu`, `-gil`, Arabic/Persian-origin names and Ottoman versus modern spelling were not sourced and are gaps, not findings.

## Contrasts that challenge the shortcut

Examples are **synthetic** (invented, non-referential people, author-written, no native review) unless marked adapted from a cited source. They are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Sayın Prof. Dr. Elif Akarsu geldi.` | Esteemed Prof. Dr. Elif Akarsu came. | Where does the name start? |
| `Ayşe Nur'a baktım.` | I looked at Ayşe Nur. | Compound given name as one span. |
| `Ayşe, Nur'a baktı.` | Ayşe looked at Nur. | Comma separates two people; contrast. |

## NER decision and falsifiable handoff

Score the same predictions under two declared span policies for honorifics and report which tokens flip. Disposition: proposal, see [decision brief](decision-brief.md).

## Limits and next evidence

No annotation guideline read; naming communities outside the 1934 convention, minority and historical names not studied; law amendments unread.

