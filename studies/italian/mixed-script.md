# Italian: orthographic variants, diacritics and foreign-name carriers

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested. Examples are **synthetic** (fictional people, repository MIT terms, author self-check only) unless marked attested.

## Research answer and basis

Question: for a Latin-script-only language, what representation variation matters, and where does foreign-script material enter?

Scripts are Latn only. Variation is within Latin: accent versus apostrophe, U+0027 versus U+2019, NFC versus NFD, and accent loss ([ITA-004](findings/ITA-004.md)). Niccolò and Nicolò are both correct and coexist [ITA-S008](sources.md#ita-s008). U+2019 is the preferred apostrophe, U+0027 is common [ITA-S015](sources.md#ita-s015); precomposed and decomposed letters are canonically equivalent [ITA-S014](sources.md#ita-s014). Foreign names in Italian civil registry keep original diacritics and extra letters J K X Y W, and non-alphabetic names are written alphabetically per a secondary 2014 commentary [ITA-S016](sources.md#ita-s016).

## Contrasts that challenge the shortcut

| Original | Provenance | Question |
| --- | --- | --- |
| `Niccolò` vs `Nicolò` | attested forms (ITA-S008) | distinct accepted spellings; do not merge by default |
| `Niccolo` | synthetic noise | accent stripped |
| `Nicolo` + U+0300 | synthetic | NFD form of `Nicolò` |
| `Björn Åkesson` | synthetic (fictional) | a foreign Latin name with diacritics inside Italian text |
| `Il signor Čajkovskij` | synthetic | a Cyrillic-derived name in scholarly Latin transliteration |

## NER implication and handoff

Hypothesis: canonical-equivalence and apostrophe-equivalence normalization with an offset map recover encoding variants; accent folding is a separate, lossy experiment. Disposition: ready-for-owner-review; no result.

## Limits and next evidence

Transliteration conventions for Cyrillic, Arabic or Chinese names in Italian text were not verified; search snippets mentioning ISO 9 and practical Italian renderings were not read at source, so this dossier makes no transliteration claim. Code-switching with English anglicisms was not investigated. Accent-for-apostrophe substitutions (perche') and È versus E' are unsourced. Foreign scripts inside Italian text are out of scope except as noted.
