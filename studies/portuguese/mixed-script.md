# Portuguese: diacritics and normalization within Latin script

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Portuguese uses only Latn; mixed-script here means accent variants, Unicode forms and noisy accent loss, not transliteration. The Acordo sanctions António and Antônio and lets a person keep a registered spelling ([POR-S001](sources.md#por-s001), Bases XI 3º and XXI). NFC and NFD are canonically equivalent ([POR-S012](sources.md#por-s012)); accent loss is not. A paper reports 25,722 word pairs differing only by an accent in Portuguese and describes user-generated content as missing diacritics ([POR-S008](sources.md#por-s008)). Canonical claim: [POR-003](findings/POR-003.md).

## Contrasts that challenge the shortcut

Examples are synthetic (fictional people) unless marked adapted. Author self-check only; no qualified language review. Research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `João` (U+00E3) vs `João` (a + U+0303) | same name | NFC/NFD mapping. |
| `João` vs `Joao` | accent loss | not canonical equivalence. |
| `António` vs `Antônio` | two spellings | not a typo. |
| `sé` vs `se` | cathedral vs clitic | accent folding creates ambiguity. |

## NER decision and falsifiable handoff

Test NFC lookup separately from accent folding. Failure: folding gains recall with no false-match increase would challenge the separation.

## Limits and next evidence

Alternate scripts are out of scope. No name-specific noise corpus; foreign-letter names (k, w, y) not researched; the 2009 national implementation is unverified.
