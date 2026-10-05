# Urdu: Whitespace tokens and orthographic words differ, so name candidates need sub-token and cross-token reach

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Whitespace is an unreliable boundary in Urdu. A segmentation paper explains that the cursive script has no intrinsic space; a typed space is used for shaping, so words ending in a non-joining letter may be followed by no space, and morphemes ending in a joining letter may be separated by a space ([URD-S004](sources.md#urd-s004), sections 1 and 2.1). It introduces an "Orthographic Word" as the whitespace unit that may be less than, or more than, a word (section 3). A rule-based Urdu NER system lists the unsolved space problem as a limitation ([URD-S005](sources.md#urd-s005), p. 2515), and a transliteration paper makes the same point ([URD-S012](sources.md#urd-s012), section 2). Treebank documentation, in contrast, treats whitespace-delimited tokens as the unit ([URD-S010](sources.md#urd-s010)); UD word units do not define PERSON spans. See [URD-002](findings/URD-002.md) and [URD-001](findings/URD-001.md) for ZWNJ and code points.

## Contrasts that challenge the shortcut

Examples are **synthetic**, generic names, author self-check only. ZWNJ is U+200C.

| Original | Meaning | Question |
| --- | --- | --- |
| `عبدالرحمن` / `عبد الرحمن` / `عبد‌الرحمن` (ZWNJ) | Abdul Rahman in three spellings | One span in all three; a whitespace tokenizer yields one, two, one tokens. |
| `احمدشیر` / `احمد شیر` | Ahmad Sher | Non-joiner final letter makes the unspaced form plausible. |
| `غلام رسول` | Ghulam Rasool | Final joiner makes the space visually important; the two-token form is the stable one. |

## NER decision and falsifiable handoff

Measure whether a whitespace-token baseline loses recall on spacing variants relative to a candidate generator that reaches across and within tokens. Treat ZWNJ as a tokenization input, preserve it, and report boundary errors apart from missed mentions. Disposition: proposal for `ner-evidence`; deferred. See the [decision brief](decision-brief.md).

## Limits and next evidence

No name-specific frequency or measured effect. Version identity of [URD-S004](sources.md#urd-s004) with the 2010 Durrani and Hussain work is unverified. Handwriting and Nastaliq rendering were not studied; whether ZWNJ is common in current Pakistani typing was not measured. The UDTB 5 percent no-space-after-token figure ([URD-S009](sources.md#urd-s009)) is not name-specific.
