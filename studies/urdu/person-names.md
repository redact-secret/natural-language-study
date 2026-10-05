# Urdu: Name parts, titles and relational names do not fit one template

Scope: [dossier overview](overview.md). Status: source-limited desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Pakistani Muslim naming varies by class, ethnicity and region ([URD-S015](sources.md#urd-s015), a book review) and is tied to identity, religiosity and class ([URD-S014](sources.md#urd-s014), abstract only). A linguistic study of Muslim names in Urdu, known only through a search summary, reports name types of one to four parts, with honorific, caste, patronymic and husband's-name components, and treats `عبد` and forms in -ul or -ur as titles ([URD-S013](sources.md#urd-s013)). The national identity card prints given and family name in Urdu and English, plus a father's or husband's name ([URD-S016](sources.md#urd-s016), encyclopedia page). The NER literature separates Person Name from Title Person ([URD-S005](sources.md#urd-s005), p. 2508 Table 1), so title inclusion is a design choice, not a given. See [URD-004](findings/URD-004.md).

## Contrasts that challenge the shortcut

Examples are **synthetic**; fictional or generic names; no qualified review.

| Original | Meaning | Question |
| --- | --- | --- |
| `ثمینہ` | Samina | Mononym. |
| `محمد بلال چوہدری` | Muhammad Bilal Chaudhry | Prefix `محمد` and final caste/title-like part. |
| `بی بی مریم`, `بیگم نسرین احمد` | Bibi Maryam; Begum Nasreen Ahmad | Female honorific prefix; husband-derived final part is plausible but unverified here. |
| `ملک صاحب` vs `ملک ترقی کر رہا ہے` | Malik sahib vs the country is progressing | Family name or title versus common noun. |

## NER decision and falsifiable handoff

Decide, outside this repository's research, whether titles and honorifics are inside PERSON spans, and measure truncation by name length. Do not cap name length (a documented three-word rule truncates four-part names, [URD-S005](sources.md#urd-s005) p. 2515). Disposition: proposal for `ner-evidence`; deferred pending a primary naming source and Urdu review.

## Limits and next evidence

Key naming sources are summaries; no primary National Language Authority or NADRA naming rule was found. Non-Muslim, Pashtun, Baloch, Sindhi and Punjabi naming conventions are not studied and not claimed. Rahman's work analyzes names, not mention behavior in text.
