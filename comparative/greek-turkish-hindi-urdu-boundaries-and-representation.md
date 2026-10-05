# Greek, Turkish, Hindi and Urdu: boundary visibility, casing and representation

Question: for PERSON mentions, which operations look shared across these four dossiers, and which causes must stay language-specific? The four were chosen as a second wave and do not form a typological group. This is a draft comparison of desk research. Every cited finding is untested and has no qualified language review. The comparison selects no implementation and reports no measurement.

Scope notes: Hindi means Hindi only, not other Indian languages. Urdu means Urdu only, not other Pakistani languages. Greek excludes Cyprus. Turkish is modern Latin-script Turkish.

## Compact comparison

| Axis | Greek | Turkish | Hindi (Deva) | Urdu (Arab) |
| --- | --- | --- | --- | --- |
| How grammar attaches to a name | Case endings change the name form; articles and fused `στον` precede it ([GRE-001](../studies/greek/findings/GRE-001.md), [GRE-003](../studies/greek/findings/GRE-003.md)) | Suffix inside the whitespace token, marked by an apostrophe after a proper name ([TUR-001](../studies/turkish/findings/TUR-001.md)) | Postposition is a separate word after a name, fused to pronouns ([HIN-001](../studies/hindi/findings/HIN-001.md)) | Postposition is a boundary cue but not a sufficient one ([URD-006](../studies/urdu/findings/URD-006.md)) |
| Where the boundary cue is missing | Surname form is genitive-shaped; ending alone is ambiguous ([GRE-002](../studies/greek/findings/GRE-002.md)) | No apostrophe for institution names, plurals and noisy text ([TUR-002](../studies/turkish/findings/TUR-002.md)) | Honorifics `श्री`, `जी` are separate unless part of the name ([HIN-002](../studies/hindi/findings/HIN-002.md)) | Whitespace is unreliable: omitted, inserted, plus ZWNJ ([URD-002](../studies/urdu/findings/URD-002.md)) |
| Case cue for name versus common noun | Present, but weak with all-caps accent dropping ([GRE-004](../studies/greek/findings/GRE-004.md), [GRE-006](../studies/greek/findings/GRE-006.md)) | Present; dotted/dotless I breaks locale-unaware casing ([TUR-003](../studies/turkish/findings/TUR-003.md), [TUR-006](../studies/turkish/findings/TUR-006.md)) | None ([HIN-005](../studies/hindi/findings/HIN-005.md)) | None ([URD-003](../studies/urdu/findings/URD-003.md)) |
| Unicode representation | Tonos U+0384 versus U+0301; final sigma; Greek/Latin look-alikes ([GRE-004](../studies/greek/findings/GRE-004.md)) | `İ` NFD is `I` + U+0307 ([TUR-003](../studies/turkish/findings/TUR-003.md)) | Nukta two encodings; anusvara/chandrabindu; ZWJ/ZWNJ ([HIN-003](../studies/hindi/findings/HIN-003.md), [HIN-004](../studies/hindi/findings/HIN-004.md)) | `ی/ي`, `ک/ك`, `ہ/ه` are not unified by NFKC ([URD-001](../studies/urdu/findings/URD-001.md)) |
| Diacritic or letter loss | Accent dropping in capitals ([GRE-004](../studies/greek/findings/GRE-004.md)) | ASCII-fied `Sukru` ([TUR-004](../studies/turkish/findings/TUR-004.md)) | Nukta dropped as spelling variation ([HIN-003](../studies/hindi/findings/HIN-003.md)) | Diacritics normally unwritten; not a finding by itself |
| Transliteration | Official, informal and look-alike Latin forms ([GRE-005](../studies/greek/findings/GRE-005.md)) | Not a first-wave finding | Romanization versus Hinglish ([HIN-006](../studies/hindi/findings/HIN-006.md)) | Roman, Devanagari and mixed renderings ([URD-005](../studies/urdu/findings/URD-005.md)) |
| Titles and name structure | Titles outside the name; articles as cues ([GRE-003](../studies/greek/findings/GRE-003.md)) | Titles before and after names ([TUR-005](../studies/turkish/findings/TUR-005.md)) | Honorific policy differs between annotation designs ([HIN-002](../studies/hindi/findings/HIN-002.md)) | No single given-plus-family template ([URD-004](../studies/urdu/findings/URD-004.md)) |

Empty or hedged cells mean the dossier did not establish the point. They are not evidence that the pattern is absent.

## Three layers

- **Observable operation (candidate shared).**
  - A candidate span may need to end inside a whitespace token (Turkish `Ahmet'in`).
  - It may need to join tokens (Urdu compound names).
  - It may need to match across representation variants while keeping the original spelling (all four).
- **Linguistic cause (language-specific).** Greek case endings, Turkish agglutinative suffixes, Hindi postpositions, and Urdu space omission and joining differ. Do not collapse them into one affix list.
- **Downstream policy (unresolved).** Whether honorifics, titles, plurals and suffixes sit inside PERSON is open in every brief. Treebank word units, such as UD splitting, are syntactic conventions and not PERSON span definitions.

## Rejected shortcuts

1. Treat Hindi and Urdu as one language for evaluation. They share a spoken register but differ in script, Unicode behavior and boundary evidence. Compare them on the same names, not by pooling.
2. Use capitalization as a name cue everywhere. Hindi and Urdu have no case. Turkish casing needs a locale-aware step, and Greek capitals lose the accent.
3. Match names by NFC/NFKC alone. Urdu letter variants, the Hindi nukta policy and Greek look-alikes survive normalization or need a separate decision.
4. Strip case endings or suffixes without a role check. A Greek surname or a Turkish institution name loses part of its form.
5. Treat transliteration as identity. Greek, Hindi and Urdu transliteration is many-to-many in the sources read.

## Testable candidate capabilities

1. **Sub-token span ends.** Compare apostrophe-aware Turkish boundaries against the raw-token baseline, with a no-apostrophe matched negative.
2. **Representation-aware lookup with offsets.** Test a Unicode-equivalence layer per script as a separate slice, and keep accent, nukta and letter-variant folding as distinct lossy experiments.
3. **Whitespace-independent candidates for Urdu.** Compare whitespace-token, joined and ZWNJ-aware candidates.
4. **Context-only name versus noun features** for caseless scripts, against a lexicon-only baseline, with matched common-noun pairs.

## Controlled comparison and falsification

Hold the name inventory, split, annotation policy, model and scorer fixed, and change one mechanism per slice. Report omissions and false inclusions separately, with denominators, boundary-error type and a separate list of unresolved cases. For tokenizer-related changes, measure candidate reachability before span accuracy.

Reject a candidate if it gives no gain over the baseline or adds false positives on the matched negatives. Reject a shared abstraction if per-language rules perform equally well and the shared one needs per-language exceptions.

## Handoffs

- `ner-evidence`: decide honorific, title and suffix span policy first. Use the contrast families in the four briefs ([Greek](../studies/greek/decision-brief.md), [Turkish](../studies/turkish/decision-brief.md), [Hindi](../studies/hindi/decision-brief.md), [Urdu](../studies/urdu/decision-brief.md)).
- `ner-eval`: slice names in the briefs are proposals, not registered dimensions. Nothing has been run.
- `fastner`: options only. No downstream code was inspected here, so no runtime claim follows.
- `fastner-benchmarks`: deferred until evaluated artifacts exist.

## Gaps and source disagreements

- Most sources were read through fetch summaries or abstracts. Primary grammars were not accessed for any of the four, and ELOT 743 is paywalled.
- Hindi `person-names.md` is the weakest file. The Urdu naming sources were partly inaccessible.
- The Urdu–Hindi comparison rests on one transliteration paper plus the two dossiers.
- No corpus frequency, annotation agreement or independent language review exists for any cell.
- Related comparisons: [Romance connectors and contractions](romance-connectors-and-contractions.md), [person boundaries](person-boundaries.md) and [boundary roles](boundary-roles-and-candidate-capabilities.md).
