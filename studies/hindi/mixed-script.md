# Hindi: Devanagari, Roman and mixed forms of a name are separate surface forms to test

Scope: [dossier overview](overview.md), Hindi (Devanagari and `hi-Latn`), PERSON. Status: source-backed desk synthesis; independent review pending. NER proposals remain untested. Transliteration does not establish identity.

## Research answer and basis

Hindi appears in Devanagari, in informal Roman script (Hinglish), and mixed within a sentence. The ALA-LC romanization table prescribes a deterministic mapping with supplied inherent vowels and homorganic nasals [HIN-S010](sources.md#hin-s010), Notes 2-5, while spoken Hindi deletes schwas and predicting deletion is itself a research problem [HIN-S011](sources.md#hin-s011). A cataloguing table and an informal spelling therefore need not agree. Code-mixed corpora keep Hindi function words separate around Latin names (`modi/B-Per ji/I-Per na/Other`) and cover Roman-script text only [HIN-S008](sources.md#hin-s008), sections 3 and 3.1; a 2025 dataset includes Standard English, Romanized and Devanagari Hindi outputs [HIN-S009](sources.md#hin-s009). [HIN-006](findings/HIN-006.md) owns the finding; the nukta encodings in [HIN-003](findings/HIN-003.md) are a script-internal analogue.

## Contrasts that challenge the shortcut

"Match names across scripts with one transliterator" fails; "script change equals entity boundary" fails inside `Rajesh शर्मा`. Examples are **synthetic** (fictional people).

| Original | Meaning | Question |
| --- | --- | --- |
| `राजेश शर्मा ने कहा` / `Rajesh Sharma ne kaha` | Rajesh Sharma said | Same fictional name in two scripts. |
| `मैंने Rajesh Sharma को देखा।` | I saw Rajesh Sharma. | Script change at the name edge. |
| `Rajesh शर्मा ने कहा` | Rajesh Sharma said | Script change inside one name. |

## NER decision and falsifiable handoff

Evaluate Devanagari, Roman-capitalized, Roman-lowercase and mixed forms separately with unchanged annotation. Disposition: local proposal; `ner-evidence` and `ner-eval` deferred. See the [decision brief](decision-brief.md).

## Limits and next evidence

Primary romanization standards (ISO 15919, IAST, ITRANS) were not read, there is no count of informal variants, and the code-mixed sources are social media. Digits and nukta spelling in Roman text were not studied. Other Indian scripts used for Hindi-region names are out of scope.
