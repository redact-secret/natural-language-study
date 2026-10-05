# Italian: PERSON boundary inclusion and exclusion questions

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested. Examples are **synthetic** (fictional people, repository MIT terms, author self-check only) unless marked attested.

## Research answer and basis

Question: which attached items are candidates for inside versus outside a PERSON span?

Candidates inside: surname-internal particles and apostrophe starts ([ITA-001](findings/ITA-001.md), [ITA-002](findings/ITA-002.md)), compound given names and second surnames ([ITA-006](findings/ITA-006.md)). Candidates outside: external articulated prepositions and elided articles before a name, enclitic verbs ([morphology](morphology.md)), and titles. Title status is policy: UD includes particles in flat:name but the extracts do not say that titles are inside names [ITA-S013](sources.md#ita-s013); Crusca writes titles as separate words [ITA-S001](sources.md#ita-s001), [ITA-S002](sources.md#ita-s002). UD word units do not define PERSON spans.

## Contrasts that challenge the shortcut

| Original | Provenance | Question |
| --- | --- | --- |
| `Avv. Mario Rossi` | attested form (ITA-S001) | title inside or outside is a policy choice |
| `il dottor Rossi` | synthetic | title lowercase in running text |
| `la signora Neri` | synthetic | full-word title |
| `la lettera dell'avvocato Neri` | synthetic | external `dell'` before a title; `avvocato Neri` candidate |
| `Anna Dell'Orso` | synthetic (fictional) | internal `Dell'` |

## NER implication and handoff

Hypothesis: boundary policy must state title treatment separately from particle treatment; a single rule for all attached function words will fail one of the two. Disposition: policy decisions ahead of any gold annotation in the [decision brief](decision-brief.md); no result.

## Limits and next evidence

This study sets no policy. No source says how Italian NER corpora treat titles. Possessive and reverential capitalization of pronouns in formal letters [ITA-S007] is outside the span question.
