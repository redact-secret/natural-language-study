# Spanish: Given-name homographs and surname-like words need context

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

Forms such as `Pilar`, `Rosa`, `Dolores`, `Mercedes`, `Jesús`, `Cruz`, `Guerra` and `Mármol` coincide with common nouns, product names or places; see [SPA-006](findings/SPA-006.md). The dictionary pages needed to verify these were not accessible (HTTP 403), so the lexical claims are leads, not sources. Contextual disambiguation matters because CoNLL-2002-style annotation marks only top-level entities ([SPA-S013](sources.md#spa-s013)); an embedded person inside a place or organization name is a separate boundary decision. Spanish capitalization marks proper nouns (author's general knowledge, unsourced here), so sentence-initial position is the main case where case is uninformative.

## Contrasts that challenge the shortcut

Examples are **synthetic** (authored for this study, fictional people, repository MIT terms) unless marked otherwise. Translations and proposed readings have author self-check only. They are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Pilar llamó.` | Pilar called. | Person reading. |
| `El pilar cedió.` | The pillar gave way. | Common noun. |
| `Calle Mármol` | Mármol Street | Surname-like word in a street name. |

## NER decision and falsifiable handoff

Keep unresolved contexts as unresolved; do not count one reading as gold. Compare lexicon-only against context features on matched pairs. Destination: `ner-evidence`, `ner-eval`. Untested.

## Limits and next evidence

Verify lexical entries in the RAE dictionary and a corpus. Frequency of each reading is unknown. Eponymous common nouns and metaphorical uses are not covered.
