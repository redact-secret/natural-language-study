# Italian: tokenization and word/entity boundaries

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested. Examples are **synthetic** (fictional people, repository MIT terms, author self-check only) unless marked attested.

## Research answer and basis

Question: where do Italian word-level units and PERSON spans disagree?

UD Italian uses multiword tokens for articulated prepositions and enclitic pronouns and keeps abbreviations and numerals with internal punctuation [ITA-S012](sources.md#ita-s012). Its flat:name page includes particles inside names, with `Dell'` shown as a name-internal token in `Marcello Dell' Utri` [ITA-S013](sources.md#ita-s013). The apostrophe is the elision mark [ITA-S004](sources.md#ita-s004), and Unicode prefers U+2019 though U+0027 dominates keyboards [ITA-S015](sources.md#ita-s015). Caffarelli notes that print alphabetization ignores apostrophes and spaces while digital systems count them [ITA-S001](sources.md#ita-s001), so tokenization-visible differences exist between `D'Auria`, `DAuria` and `D Auria`. Findings: [ITA-001](findings/ITA-001.md), [ITA-004](findings/ITA-004.md).

## Contrasts that challenge the shortcut

| Original | Provenance | Question |
| --- | --- | --- |
| `Anna D'Angelo` / `Anna D’Angelo` | synthetic | two apostrophe code points, same boundary expectation |
| `Anna D' Angelo` | synthetic noisy variant | spurious space after the apostrophe; mirrors the UD fragment but is not claimed to occur in text |
| `Anna DAngelo` | synthetic noisy variant | apostrophe lost; one token |
| `Dott.ssa Elena Moretti` | synthetic | internal period; sentence-split trap |
| `dott. Moretti` | synthetic | lowercase title with period |

## NER implication and handoff

Hypothesis: preserve the original string and expose both the whole apostrophe-joined unit and an inner start candidate; do not let a UD-style split decide the span. Compare candidate reachability before comparing final spans. Disposition: ready-for-owner-review; no run.

## Limits and next evidence

UD's page does not say how elision is tokenized in all treebanks, and a dedicated tokenization page was unavailable. No tokenizer was probed in this study. Real-text frequency of space or apostrophe corruption is unknown.
