# Spanish: Contractions and enclitics touch names differently from surname particles

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

Two attachment mechanisms matter. First, the contractions `del` (de + el) and `al` (a + el) fuse a preposition with an article; UD splits them into two syntactic words ([SPA-S008](sources.md#spa-s008)), and RAE orthography reportedly keeps them uncontracted before a capitalized article that belongs to a name (`de El País`) but contracts before a lowercase nickname article (`al Greco`) ([SPA-S014](sources.md#spa-s014), excerpt only). See [SPA-003](findings/SPA-003.md). Second, enclitic pronouns attach to verbs (`hacerlo`, UD multiword token, [SPA-S008](sources.md#spa-s008)); the pronoun attaches to the verb, not to a following name, so a clitic does not directly join a PERSON token. This is the author's reading of the UD description and was not tested against data.

## Contrasts that challenge the shortcut

Examples are **synthetic** (authored for this study, fictional people, repository MIT terms) unless marked otherwise. Translations and proposed readings have author self-check only. They are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Dímelo, Lucía.` | Tell me it, Lucía. | Enclitics on the verb, comma before the name; the name is not attached to the clitic form. |
| `Pedro del Amo llegó.` | Pedro del Amo arrived. | `del` inside a surname; do not split it off. |
| `El libro del Amo llegó.` | The owner's book arrived. | External `del`; `Amo` is not a name here. |

## NER decision and falsifiable handoff

Treat UD splits as an annotation convention. Test whether a tokenizer that splits `del` loses name-internal `del` and whether keeping it whole adds false positives on the external case. Destination: `ner-evidence` review, then `ner-eval`; `fastner` only if warranted. No downstream result exists.

## Limits and next evidence

No data was inspected for enclitic-plus-name sequences; verb forms with a written accent shift (`dímelo`) were not sourced. Derivational and diminutive name forms (`Lucita`) are not covered.
