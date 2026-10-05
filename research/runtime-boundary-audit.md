# Runtime boundary audit: research relevance, not NER evaluation

**Observed on 2026-10-04:** existing English and Korean tokenizer behavior already addresses some first-wave concerns; French elision and Japanese kana runs expose different candidate-boundary questions. This changes experiment priority, not language support status.

## Provenance and method

Read-only inspection of the adjacent `fastner` checkout at commit `544484a240af62d0208a7eff70649e447ea7599c`; `git status --short` was empty when inspected. Tokenizer schema **3**, compiled with `rustc 1.98.1 (48a229cea 2026-09-01)`. Tokenizer source SHA-256: `f0247983278c54891c407425cae33ed7801a6389a0af85046850afc19aafc63f`.

A temporary Rust harness imported the unchanged `tokenizer.rs` as a module, called `tokenize(text, 0, &mut units)` on **11 synthetic strings**, and printed each unit’s original substring, class, coordinates and hash. No model was loaded, no gold spans supplied and no precision/recall computed. Only the observations needed for research are retained below; this repository does not acquire executable inference fixtures. The downstream checkout was not edited.

To reproduce in an isolated temporary directory: check out the pinned revision, import `crates/fastner/src/tokenizer.rs` via a Rust module path, call the public tokenizer on the literal inputs below, and inspect `Unit` fields using original UTF-8 text. Compile the temporary harness with `rustc --edition=2021`. Never substitute normalized strings when checking original-coordinate behavior.

## Observed tokenizer units

The vertical bar below is a display separator, never input text. Whitespace is represented by unit flags rather than its own token. These cuts are **observed tokenizer units**, not proposed gold PERSON annotations.

### English

- `Nora O’Neil’s report` → `Nora | O’Neil | ’ | s | report`.
- `James’ report` → `James | ’ | report`.

Internal apostrophe retention and external possessive cuts are already present. This supports retaining the current tokenizer as a baseline for [ENG-001](../studies/english/findings/ENG-001.md); mention coordination in [ENG-004](../studies/english/findings/ENG-004.md) remains a separate question. These two strings do not prove complete clitic coverage.

### Korean

- `김민수에게도` → `김 | 민 | 수 | 에 | 게 | 도`.
- `영철이가` → `영 | 철 | 이 | 가`.
- `가나` → `가 | 나`, each classified as Hangul.

The required syllable cut is available; choosing it is another task. The decomposed-jamo composition path exists in [tokenizer.rs, lines 229–245](https://github.com/redact-secret/fastner/blob/544484a240af62d0208a7eff70649e447ea7599c/crates/fastner/src/tokenizer.rs#L229). Prioritize annotation/suffix decisions from [KOR-004](../studies/korean/findings/KOR-004.md), rather than asserting that Korean currently requires whitespace-only segmentation to be replaced.

### Japanese

- `アリスさんが来た。` → `アリスさんが | 来 | た | 。`.
- `田中さんが来た。` → `田 | 中 | さんが | 来 | た | 。`.

The first name’s proposed right edge falls inside the first `OtherWord` unit. The Han spelling has a unit edge before さん. A profile flag alone will not create the missing kana edge. The generic alphabetic-run path is in [tokenizer.rs, lines 354–370](https://github.com/redact-secret/fastner/blob/544484a240af62d0208a7eff70649e447ea7599c/crates/fastner/src/tokenizer.rs#L354). See [JPN-004](../studies/japanese/findings/JPN-004.md).

### French

- `Le dossier d’Élodie` → `Le | dossier | d’Élodie`.
- `Élodie d’Aubemont` → `Élodie | d’Aubemont`.
- `Anne-Claire Évrard` → `Anne-Claire | Évrard`.
- `Anne-Claire Évrard` → `Anne-Claire | Évrard`.

External d’ and a name-internal d’ both remain joined, so their differing roles cannot be decided by a universal punctuation cut. The accented surname forms each remain one unit but have **different word hashes**. Token containment of combining marks is not canonical-equivalent lexical lookup. These are distinct experiments in [FRA-002](../studies/french/findings/FRA-002.md) and [FRA-003](../studies/french/findings/FRA-003.md), not measured recognition failures.

## Inspected integration constraints

[Profile enum/dispatch, lines 107–145](https://github.com/redact-secret/fastner/blob/544484a240af62d0208a7eff70649e447ea7599c/crates/fastner/src/features/mod.rs#L107) contains En and Ko. [English eligibility, lines 19–21](https://github.com/redact-secret/fastner/blob/544484a240af62d0208a7eff70649e447ea7599c/crates/fastner/src/features/en.rs#L19) admits Latin words and periods; [Korean eligibility, lines 18–19](https://github.com/redact-secret/fastner/blob/544484a240af62d0208a7eff70649e447ea7599c/crates/fastner/src/features/ko.rs#L18) admits Hangul and, for feature schema ≥ 3, Han. Kana `OtherWord` is not admitted by these inspected gates. This is code scope, not an official support statement.

The Korean **statistical baseline** has `STAT_MAX_SPAN = 4` and joins only without `GAP` ([ko.rs, lines 15–23](https://github.com/redact-secret/fastner/blob/544484a240af62d0208a7eff70649e447ea7599c/crates/fastner/src/features/ko.rs#L15)). These restrictions must not be reported as universal limits of every backend. A spaced-name experiment needs to identify its backend explicitly.

## Result and limits

The source inspection and tokenizer probes are completed observations. Full recognition, representability after every decoding/postprocessing stage, model accuracy, latency and memory are **unmeasured**. In particular, a missing tokenizer edge is a concern for unit-aligned candidates, not proof that every possible postprocessor must fail. Proposed downstream work is summarized in the [pattern study](../comparative/boundary-roles-and-candidate-capabilities.md).

## Evidence-contract interoperability

Read-only inspection of `ner-evidence` commit `b10b325b54061f5a9c86e8542189723c58442831`, taxonomy **0.2.0**, found two requirements that affect these handoffs. The tracked taxonomy matched HEAD; an unrelated untracked LICENSE was untouched.

1. [Korean conventions, lines 55–61](https://github.com/redact-secret/ner-evidence/blob/b10b325b54061f5a9c86e8542189723c58442831/taxonomy/person.taxonomy.json#L55) exclude informal name suffix 이 as well as particles. [KOR-004](../studies/korean/findings/KOR-004.md) documents the mismatch with the NIKL suffix-inclusive policy. This requires import provenance/annotation mapping, not an unversioned local policy change.
2. [Span conventions, lines 65–69](https://github.com/redact-secret/ner-evidence/blob/b10b325b54061f5a9c86e8542189723c58442831/taxonomy/person.taxonomy.json#L65) define Unicode code-point offsets over **NFC-normalized text**, with additional UTF-8 and UTF-16 offsets. NFC/NFD raw-input studies must preserve both input views and follow an approved projection/adapter or separately reviewed contract. Do not add NFD fixture text that violates the current NFC contract or compare normalized gold coordinates directly with raw input coordinates.

The English conventions already exclude titles/possessive ’s and include initials/periods and generational suffixes. Language briefs should use these established rules, while sending unresolved cases to evidence owners. No taxonomy, evidence, evaluation or runtime code was modified.
