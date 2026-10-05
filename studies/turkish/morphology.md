# Turkish morphology: suffixes after names are bounded by an apostrophe only in some cases

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis from summaries and abstracts; independent review pending. NER proposals remain untested.

## Research answer and basis

Case, possessive and predicate suffixes after a personal name are written after an apostrophe; plural and derivational suffixes on names, and suffixes on institution names, are not ([TUR-S001](sources.md#tur-s001), summary only). [TUR-001](findings/TUR-001.md) owns the apostrophe case and [TUR-002](findings/TUR-002.md) owns the exceptions and the noisy-text hypothesis. Vowel harmony and suffix chains were not documented by any source read, so no claim is made about them beyond the suffixes in the examples. Consonant softening on names is reported not to apply by a newspaper explainer only ([TUR-S015](sources.md#tur-s015)).

## Contrasts that challenge the shortcut

Examples are **synthetic** (invented, non-referential people, author-written, no native review) unless marked adapted from a cited source. They are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Ayşe'ye mektup yazdım.` | I wrote a letter to Ayşe. | Candidate `Ayşe` before `'ye`. |
| `Ahmetler geldi.` (adapted form, TUR-S001) | The Ahmets came. | Plural without apostrophe: person, group, or out of scope? |
| `Kapıya kitap bıraktım.` | I left a book at the door. | Common noun with a case suffix, no apostrophe, no name. |

## NER decision and falsifiable handoff

Treat suffix attachment as three cases, not one: apostrophe-marked, unmarked by rule, unmarked by noise. Compare apostrophe-cut, suffix-list and learned boundaries on matched sets; score truncated names (suffix-list risk). Disposition: ready-for-owner-review proposal; see the [decision brief](decision-brief.md).

## Limits and next evidence

No grammar was read (Göksel and Kerslake 2005 not accessed), so suffix chains, harmony and alternation need a primary source. Productive affix inventory not attempted.

