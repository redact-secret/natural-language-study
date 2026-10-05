# Italian: elision, articulated prepositions and enclitics around names

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested. Examples are **synthetic** (fictional people, repository MIT terms, author self-check only) unless marked attested.

## Research answer and basis

Question: which Italian function-word and clitic attachments can touch a name without belonging to it?

- Elision: singular definite articles and matching articulated prepositions lose a final vowel before a vowel and take an apostrophe (l'ombrello, nell'epica); plural gli does not elide [ITA-S004](sources.md#ita-s004). Role in names is handled in [ITA-001](findings/ITA-001.md).
- Articulated prepositions (del, dello, della, nel, sul, al) are single orthographic words; UD Italian splits them into multiword tokens for syntax [ITA-S012](sources.md#ita-s012). That split is not a PERSON boundary.
- Enclitic pronouns attach to imperatives and apocopated infinitives and form one graphic unit (dammelo, farlo) [ITA-S005](sources.md#ita-s005); UD treats them as multiword tokens as well [ITA-S012].

## Contrasts that challenge the shortcut

| Original | Provenance | Meaning | Question |
| --- | --- | --- | --- |
| `la casa di Maria` | synthetic | Maria's house | external `di`; Maria only |
| `Maria Della Rocca` | synthetic (fictional) | a full name | `Della` internal; whole span |
| `la casa della rocca` | synthetic | the fortress's house | same `della`, common noun |
| `Dammi Marco.` | synthetic | Give me Marco / hand me Marco | sentence-initial capitalized verb form before a name; only `Marco` is a candidate |
| `Dimmi dov'è Luca.` | synthetic | Tell me where Luca is | `dov'` elided adverb touching the following verb, not a name |

The sentence-initial enclitic verb (`Dammi`, `Fallo`) is capitalized by position and could be mistaken for a name by a capitalization-run rule; the sources describe the verb form, not that failure, so the risk is a hypothesis.

## NER implication and handoff

Hypothesis: contextual attachment features beat a rule that splits every apostrophe or every function word. Hold name inventory fixed; vary the preceding word (noun, verb, given name). See [ITA-001](findings/ITA-001.md) and the [decision brief](decision-brief.md). Disposition: ready-for-owner-review proposal; no result.

## Limits and next evidence

No source in hand covers an article before a first name or surname (la Rossi), a regional pattern the author knows exists but has not verified. Enclitic-verb capitalization collisions have no corpus data. Review by a competent Italian reader is missing.
