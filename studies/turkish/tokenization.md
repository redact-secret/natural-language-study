# Turkish tokenization: the whitespace token hides a boundary that the apostrophe sometimes exposes

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis from summaries and abstracts; independent review pending. NER proposals remain untested.

## Research answer and basis

Whitespace tokens such as `İstanbul'da` contain a name and a suffix. UD Turkish BOUN and IMST treat many such forms with multi-word tokens (3,374 and 1,639) and report 2,148 and 611 letters-plus-punctuation types ([TUR-S005](sources.md#tur-s005), [TUR-S006](sources.md#tur-s006), summaries). The Snowball stemmer cuts at the first apostrophe with a two-character guard ([TUR-S012](sources.md#tur-s012)). [TUR-001](findings/TUR-001.md) holds the claim; [TUR-003](findings/TUR-003.md) covers NFD `İ` that changes character counts. UD units do not define PERSON spans.

## Contrasts that challenge the shortcut

Examples are **synthetic** (invented, non-referential people, author-written, no native review) unless marked adapted from a cited source. They are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Selim Karaca'nın evi` | Selim Karaca's house. | Apostrophe cut gives `Selim Karaca'` plus `nın`: where does the apostrophe go, and which side owns it? |
| `Nihat Bey'e` (adapted, TUR-S001) | to Mr Nihat | Cut at apostrophe leaves `Nihat Bey`; title membership is separate. |
| `TBMM'nin` (adapted, TUR-S001) | of the Grand National Assembly | An abbreviation, not a person; apostrophe alone does not select PERSON. |

## NER decision and falsifiable handoff

Test whether apostrophe-aware candidate edges raise exact-span recall without raising false boundaries on titles, abbreviations and foreign names. Report counts by apostrophe type. Disposition: proposal; the [decision brief](decision-brief.md) orders it.

## Limits and next evidence

Apostrophe character variants (U+0027 versus U+2019) are an unverified variation axis. No tokenizer or runtime in this repository was inspected.

