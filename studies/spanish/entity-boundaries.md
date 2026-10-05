# Spanish: Titles, the personal a and article-plus-name cases need explicit span policy

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

Treatment abbreviations (`Sr.`, `D.`) take an initial capital ([SPA-S003](sources.md#spa-s003), excerpt only; `Dña.` and `Lic.` unverified), and the preposition `a` marks specific animate direct objects ([SPA-S005](sources.md#spa-s005), excerpt only). Both are left-context cues that sit next to the name; see [SPA-004](findings/SPA-004.md). Internal `del` and external `del` are the boundary question in [SPA-003](findings/SPA-003.md). Names starting with `A` or `El` (`A Coruña`, `El Salvador`) show that the cue letters can also be name material ([SPA-S014](sources.md#spa-s014)). Whether titles and nickname articles belong inside a PERSON span is a gold-policy question that this study does not settle.

## Contrasts that challenge the shortcut

Examples are **synthetic** (authored for this study, fictional people, repository MIT terms) unless marked otherwise. Translations and proposed readings have author self-check only. They are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Vi a Lucía.` | I saw Lucía. | Personal `a` outside the span. |
| `Escribí a Lucía.` | I wrote to Lucía. | Dative `a`; same surface form, different role. |
| `A Coruña es bella.` | A Coruña is beautiful. | `A` belongs to the place name; not PERSON. |

## NER decision and falsifiable handoff

Agree title and nickname-article inclusion policy first; then test cue features against matched pairs. Destination: `ner-evidence`, `ner-eval`. Untested.

## Limits and next evidence

RAE pages were not read in full. Treatment forms by country, and the status of `doña`/`don` as lowercase words in running text, are not sourced.
