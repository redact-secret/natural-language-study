# Urdu: Code points, bidi display, Roman Urdu and Devanagari renderings are variation axes, not identity

Scope: [dossier overview](overview.md). Status: source-limited desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Code points: Urdu letters such as Farsi yeh U+06CC and keheh U+06A9 coexist with Arabic yeh U+064A and kaf U+0643; NFKC does not unify them (local unicodedata check; [URD-S001](sources.md#urd-s001), [URD-S003](sources.md#urd-s003)); see [URD-001](findings/URD-001.md). Display: Arabic letters are class AL and neutrals take surrounding direction ([URD-S002](sources.md#urd-s002)), so Latin names inside Urdu text change display order but not logical order. Roman Urdu has no standard spelling and mixes with English ([URD-S011](sources.md#urd-s011)). Urdu-to-Devanagari mapping is many-to-many, with missing diacritics and short vowels ([URD-S012](sources.md#urd-s012)). See [URD-005](findings/URD-005.md).

## Contrasts that challenge the shortcut

Examples are **synthetic**; no qualified review.

| Original | Meaning | Question |
| --- | --- | --- |
| `Muhammad Bilal نے کہا۔` | Muhammad Bilal said | Latin name followed by Urdu postposition. |
| `محمد بلال (Muhammad Bilal) نے کہا۔` | Same person, two renderings | One or two spans. |
| `Muhammad` / `Mohammad` / `Mohd` | Roman variants | Variant set author-constructed. |
| `محمد` vs `मोहम्मद` | Urdu and Devanagari | Candidate rendering, many-to-many mapping. |

## NER decision and falsifiable handoff

Evaluate Latin-script and Urdu-script renderings of the same fictional names separately and keep original text and coordinates beside any folded or romanized form. Do not use transliteration similarity as identity. Compare with a Hindi dossier once one exists; none existed when this was written, so no comparison is made. Disposition: proposal for `ner-evidence`; deferred.

## Limits and next evidence

No name-specific Roman Urdu or Devanagari data; the bidi source was read as a summary; English code-mixing prevalence is unmeasured; social-media text is not sampled.
