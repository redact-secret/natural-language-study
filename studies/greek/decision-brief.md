# Greek: decision brief and downstream proposal

**Decision: Treat case-form handling, article and title boundaries, Unicode and accent normalization, transliteration and homograph disambiguation as separate experiments; do not equate a name lexicon of nominative forms with Greek PERSON coverage.** Scope is the [dossier scope](overview.md). This is draft desk research and a proposal for owner review; examples are synthetic, NER outcomes untested, and no independent language review is recorded.

## Basis and uncertainty

[GRE-001](findings/GRE-001.md) and [GRE-002](findings/GRE-002.md) rest on UD documentation plus secondary and community-edited pages. [GRE-003](findings/GRE-003.md) combines UD tokenization with a secondary grammar page and lacks any annotation-policy source. [GRE-004](findings/GRE-004.md) has locally verified Unicode behavior but secondary orthography claims. [GRE-005](findings/GRE-005.md) and [GRE-006](findings/GRE-006.md) are low confidence: the ELOT text and three lexical entries were not read. Highest uncertainty: accent convention on capitals, vocative distribution, and the person/word status of Ελπίδα, Αγάπη and Άνθος.

## Evidence packet proposed to ner-evidence

Each row is a contrast family, not a fixture or sample count. Preserve original text, provenance and finding ID.

| Family | Source finding | Controlled comparison |
| --- | --- | --- |
| Case forms | [GRE-001](findings/GRE-001.md): nominative, genitive, accusative, vocative of one fictional person | Nominative-only lookup vs stem-aware features |
| Feminine surname | [GRE-002](findings/GRE-002.md): Μαυρίδου as feminine nominative vs masculine genitive | Ending-only rule vs contextual scoring |
| Articles and titles | [GRE-003](findings/GRE-003.md): Ο/στον/κ. plus name vs plus common noun | Article-as-feature vs article-in-span |
| Unicode and accents | [GRE-004](findings/GRE-004.md): NFC, NFD, U+0384, all-caps, final sigma | Raw vs NFC-with-offsets vs accent folding |
| Transliteration | [GRE-005](findings/GRE-005.md): Greek, ELOT-style, Greeklish, homoglyph | Per-script recall, same names |
| Homographs | [GRE-006](findings/GRE-006.md): Ζωή, Δάφνη, Ελένη | Gazetteer-only vs context, with all-caps slice |

## Policy decisions before gold annotation

Define whether articles, fused prepositions, abbreviated and role titles are inside or outside PERSON; the treatment of mythological and place-named uses; whether Latin transliterations are annotated in the same class; and which Unicode normalization applies to stored text. Preserve original spelling and accents.

## Experiment proposed to ner-eval and fastner

Hold evidence snapshot, split, annotation policy, normalization contract and model artifact fixed except for the manipulated factor. Keep fictional identities and templates disjoint across splits. Report exact-span precision and recall, hard-negative false positives and boundary error type per family, with denominators. Add runtime and memory comparison in `fastner` only after a candidate exists. No threshold is set by this study.

## Rejected shortcut and reversal condition

Reject assuming the nominative form is the only surface form, treating -ου as a genitive-only cue, merging accent folding with canonical normalization, and equating a transliteration with identity. Reopen if nominative-only lookup matches stem-aware features on inflected mentions, if an adopted policy puts articles inside spans, or if script-specific recall shows no gap.

## Handoff disposition

- `ner-evidence`: ready for owner review, subject to Greek-language review and policy adjudication; no adoption asserted.
- `ner-eval`: experiment questions specified; execution pending reviewed evidence.
- `fastner`: options specified; no code changed.
- `fastner-benchmarks`: defer; no evaluated artifact and no language-support claim.

## Review and provenance

2026-10-04: produced with dossier-initialize, dossier-deep-research and dossier-document. Author checks include local Unicode verification; qualified independent language review not recorded. See [sources](sources.md) for limitations and the list of sources attempted but not used.
