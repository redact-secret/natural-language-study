# Greek: Names that are also words rely on context, not article or case

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

Wiktionary lists Ζωή as a given name from the word for life, Ελένη as a given name and mythological figure, and Δάφνη as a given name, an Athens place name and the Ancient Greek word for laurel ([GRE-S010](sources.md#gre-s010); community-edited). Fetches for Άνθος, Ελπίδα and Αγάπη failed, so those homographs are unverified. The canonical claim is [GRE-006](findings/GRE-006.md). Neither article nor inflection cleanly discriminates (η Δάφνη, Ζωής), capitalization discriminates only in mixed-case text ([GRE-004](findings/GRE-004.md)), and article gender may help for some words (Ο Άνθος versus Το άνθος) as an unverified author reading.

## Contrasts that challenge the shortcut

| Original | Meaning | Question |
| --- | --- | --- |
| `Η Ζωή ήρθε.` / `Η ζωή είναι δύσκολη.` | Zoe came. / Life is hard. | Capitalization separates in running text. |
| `ΖΩΗ ΚΑΙ ΕΛΠΙΔΑ` | Life and hope, or Zoe and Elpida | All caps remove the cue. |
| `Η Δάφνη είναι γειτονιά.` | Dafni is a neighbourhood. | Place reading. |
| `Η Ελένη της Τροίας` | Helen of Troy | Mythological person; policy question. |

All synthetic, author self-check only.

## NER decision and falsifiable handoff

Build matched name/non-name frames and compare gazetteer-only, case-aware and context-aware conditions, reporting all-caps separately. Falsified if gazetteer-only matches context. Preserve unresolved contexts. Destination: `ner-evidence` for pairs and policy, then `ner-eval`. No result exists.

## Limits and next evidence

Only three words were checked and by a community lexicon; no frequencies, no surname-as-word cases (such as Παπάς), and no dictionary authority such as the Triantafyllidis or Institute of Modern Greek Studies lexica was accessed. Person/place and person/organization collisions beyond Δάφνη are not researched.
