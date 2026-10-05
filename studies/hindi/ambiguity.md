# Hindi: Without case, context and attached cues have to separate names from common words

Scope: [dossier overview](overview.md), Hindi, PERSON versus common noun or adjective. Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Hindi names are often ordinary words in the same script, and Devanagari has no capital letters or camel case [HIN-S005](sources.md#hin-s005), sections 1 and 3, which cites the name Pushpa and the noun meaning flower. The IJCNLP shared-task slides list lack of capitalization as a major missing clue and note that proper nouns are not always named entities in context [HIN-S007](sources.md#hin-s007). [HIN-005](findings/HIN-005.md) owns the finding. A Roman-script contrast exists: the tweet corpus authors include capitalization features for Roman text [HIN-S008](sources.md#hin-s008), though no loss under lowercase was measured. HiNER also records annotation ambiguity for borderline entities (for example a mythological bird), which shows the person label itself can be contested [HIN-S005](sources.md#hin-s005), section 3.4.

## Contrasts that challenge the shortcut

A name lexicon alone fails in both directions. Examples are **synthetic** (fictional people, author self-check only).

| Original | Meaning | Question |
| --- | --- | --- |
| `कल कमल आया था।` | Kamal came yesterday. | Person. |
| `तालाब में कमल खिला है।` | A lotus has bloomed in the pond. | Not a person. |
| `सागर वर्मा आए।` / `सागर में लहरें हैं।` | Sagar Verma came / There are waves in the sea. | Following surname and locative में. |
| `मुझे आशा है।` / `आशा ने फ़ोन किया।` | I hope / Asha called. | ने after a name versus a noun phrase. |

Other candidates to test: प्रेम, किरण, राजा, गुलाब, सुंदर. No attested frequency is claimed.

## NER decision and falsifiable handoff

Build matched pairs and keep uncertain contexts as such. Compare contextual models with and without lexicon features; report false positives on the common reading and misses on the person reading separately. Disposition: local proposal; `ner-evidence` deferred. See the [decision brief](decision-brief.md).

## Limits and next evidence

Native-speaker review of every pair is needed; some may be unnatural. Person/place and person/organization ambiguity are not covered. No source gave homograph error rates. Next: find an annotated Hindi corpus with both readings and count them under a reuse license.
