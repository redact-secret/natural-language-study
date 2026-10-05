# Four-language dossier expansion

2026-10-04. Scope retained: English, Korean, Japanese and French. Chinese and Arabic in the original illustrative tree are not added to the agreed first wave.

## Delivered scope

Each dossier now has the requested `overview.md`, `morphology.md`, `tokenization.md`, `person-names.md`, `entity-boundaries.md`, `ambiguity.md`, `mixed-script.md` and canonical findings, plus sources and a decision brief. The 24 new topic syntheses contain concrete questions, source links, synthetic/adapted contrasts, downstream comparisons and specific limits. They are not empty topic inventories.

There are 21 draft findings: English 5, Korean 6, Japanese 5 and French 5. Five are new in this pass; IDs 001–004 remain stable in every language. Draft state and untested hypotheses are preserved. No independent reviewer is invented.

## Decisions added by this pass

- [ENG-005](../studies/english/findings/ENG-005.md): script properties and confusability do not define PERSON membership. Separate accented Latin, quoted-script names and artificial substitutions.
- [KOR-005](../studies/korean/findings/KOR-005.md): standard romanization admits variation and established spellings; a converter is not an exhaustive name validator.
- [KOR-006](../studies/korean/findings/KOR-006.md): 씨 needs an individual/category/collective referent decision, not just suffix removal.
- [JPN-005](../studies/japanese/findings/JPN-005.md): preserve written name order without requiring unique readings or name-part parsing. The inspected agency request is dated 2000-12-26, not 2019.
- [FRA-005](../studies/french/findings/FRA-005.md): direct, fictional and figurative name-origin expressions require an explicit referent policy.

The [comparative result](../comparative/capability-and-referent-matrix.md) separates candidate capability, entity classification, annotation-policy mismatch and representation fidelity. Existing code observations remain pinned in the [runtime audit](runtime-boundary-audit.md); this pass did not repeat or expand the tokenizer harness, train a model or measure F1.

## Source work and limits

Eleven source records were added (English 3, Korean 2, Japanese 4, French 2), bringing the dossier-local total to 33. New sources include NIKL romanization and 씨 guidance; the Japanese Agency for Cultural Affairs historical request; Unicode script/confusability standards; Cambridge's rose entry; W3C name-reading guidance; OQLF antonomasia; and Shogakukan dictionary corroboration of ミラー as a common word and personal-name rendering. Source records give locators, access dates and limitations. The same Unicode document appears in several language dossiers; source-record count must not be described as independent corroboration.

Normative guidance is distinguished from attested usage, annotation conventions and engineering inference. Constructed sentences do not establish frequency. French mixed-script coverage is a bounded quoted-name/representation stress study, not a researched transliteration inventory. Broad person/place/organization ambiguity, domain distributions, ruby extraction and community-specific naming coverage remain explicit gaps.

## Skills applied and corrected

`dossier-initialize` now distinguishes a one-question initialization from broad dossier scope. `dossier-deep-research` applies its stop condition per requested topic. `dossier-document` requires substantive topic answers for broad work. `language-pattern-study` compares classification and representation alongside boundaries. The shared completion contract is in [dossier patterns](../conventions/dossier-files.md).

Breadth delivered, linguistic review completed and NER hypotheses evaluated are separate states. The first is delivered for this bounded wave; the latter two remain pending. No new skill was needed. GitHub epic URLs remain unchanged, and local epic drafts remain deleted.

## Verification

Passed after reconciliation: repository validation (4 dossiers, 21 findings, 78 authored Markdown files), all four skill validators, and whitespace checks. All 24 requested topic paths and 33 source records were counted; local epic drafts remain absent. Unicode checks confirmed the Cyrillic substitution and the NFC equivalence of the French decomposed example. These checks establish structure and representation, not linguistic truth. Author checks include source dates, exact Unicode examples, proposed-versus-existing policies and overview/finding counts. No commit, push, issue closure or downstream mutation is part of this pass.
