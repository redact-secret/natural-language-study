# Hindi: Whitespace tokens are a good start, but danda, joiners and digits need handling

Scope: [dossier overview](overview.md), Hindi only (Devanagari with Latin contrasts). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Hindi is written with spaces between words, so word-level candidates exist, in contrast to scripts that omit spaces. Three representation facts still affect span edges. First, the danda U+0964 is the sentence-final sign and the standard states it is the only full-stop sign adopted from the Indian tradition [HIN-S001](sources.md#hin-s001), section 3.16.2; it is written adjacent to the last word, so whitespace splitting leaves `वर्मा।` as one token. Second, ZWNJ U+200C and ZWJ U+200D can be present inside a conjunct after a virama and are invisible [HIN-S002](sources.md#hin-s002) (fetch summary). Third, digits may be Devanagari (U+0966..U+096F) or the international form; the standard prescribes the international form for official purposes [HIN-S001](sources.md#hin-s001), section 2.2. [HIN-004](findings/HIN-004.md) owns the representation findings; [HIN-001](findings/HIN-001.md) covers the postposition word boundary.

The UD Hindi HDTB page (fetch summary) reports 6,170 tokens (2%) lacking a trailing space and no multiword tokens [HIN-S006](sources.md#hin-s006). UD word units define annotation, not PERSON spans. HiNER's reported errors are mostly missed entities followed by B-/I- confusion [HIN-S005](sources.md#hin-s005), section 5, which is a reminder that boundary labeling is part of the difficulty; it does not isolate tokenization.

## Contrasts that challenge the shortcut

The shortcut "split on whitespace and stop" is wrong at sentence ends. The opposite shortcut, "split at every script change or punctuation", is wrong for names inside parentheses or for Roman-Devanagari names (see [mixed script](mixed-script.md)). Examples are **synthetic** (fictional people).

| Original | Meaning | Question |
| --- | --- | --- |
| `अध्यक्ष: सुनीता वर्मा।` | Chair: Sunita Verma. | Danda inside the final token; span should exclude it. |
| `कमरा ४०२ में राजेश है।` | Rajesh is in room 402. | Devanagari digits next to a name context; digits outside the span. |
| `सत्यम` with U+200C inside | Satyam (fictional) | Invisible control inside a name; compare keys and display differ. |

## NER decision and falsifiable handoff

Hold the model fixed and compare raw whitespace tokenization with a tokenizer that separates U+0964 and ignores joiners for matching only. Report boundary errors on sentence-final names and lexicon misses on joiner-bearing names. Disposition: ready as local proposal; `ner-evidence` and `ner-eval` deferred, no issue opened. See the [decision brief](decision-brief.md).

## Limits and next evidence

No corpus frequency of danda spacing or joiner presence was measured. Hyphenated and compound names, abbreviations like डॉ. with a period, and Roman initials were not studied. Subword tokenizers of specific models were not inspected.
