# Italian: person versus common noun, place and demonym

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested. Examples are **synthetic** (fictional people, repository MIT terms, author self-check only) unless marked attested.

## Research answer and basis

Question: which collisions need context beyond a name list?

Surnames derive from personal names, nicknames, place and ethnic terms and occupations, and many are ambiguous between categories [ITA-S006](sources.md#ita-s006). Ethnic adjectives are normally lowercase [ITA-S003](sources.md#ita-s003); capitals are required for proper names [ITA-S007](sources.md#ita-s007). Mid-sentence case is therefore a strong cue, but not at sentence start, in headlines, in all-caps, or with capitalized offices. See [ITA-005](findings/ITA-005.md).

## Contrasts that challenge the shortcut

| Original | Provenance | Question |
| --- | --- | --- |
| `Rosa ha comprato una rosa.` | synthetic | name then flower in one sentence |
| `Il Conte parlò.` | synthetic | capitalized title or surname, unclear without context |
| `un cittadino romano` / `Luigi Romano` | synthetic | demonym versus surname |
| `Pace` as a given name versus `la pace` | synthetic | abstract noun |
| `Sono a Marino.` | synthetic | possible place or a surname; the author asserts ambiguity, not that a place named Marino matches the sentence reading |

## NER implication and handoff

Hypothesis: article, title and sentence-position features separate readings better than a lexicon. Keep common-noun and demonym readings as hard negatives; do not remove names from lexicons for being common words. Disposition: ready-for-owner-review; no result.

## Limits and next evidence

No homograph list or frequencies are sourced. Antonomasia and brand-name uses (for example a fashion house named after a person) were not studied. Native-speaker adjudication of every reading is needed.
