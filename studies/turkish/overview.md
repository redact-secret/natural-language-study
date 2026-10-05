---
language_key: turkish
display_name: Turkish
language_tags:
- tr
- tr-TR
scripts:
- Latn
id_prefix: TUR
status: draft
scope:
  varieties:
  - Contemporary standard written Turkish
  regions:
  - Turkey
  registers:
  - edited prose
  - constructed noisy-text contrasts
  domains:
  - general narrative and correspondence
  - news (only as described by corpus abstracts)
  entity_types:
  - PERSON
research_issues: []
updated: '2026-10-04'
---

# Turkish: NER research dossier

## Research questions and motivation

How do apostrophe-separated suffixes, unmarked suffixes, dotted and dotless I, diacritic loss, honorific words and name/common-noun collisions affect the existence and extent of PERSON mentions in Turkish?

## Scope and exclusions

Contemporary standard written Turkish in Turkey, Latin script, PERSON. Synthetic noisy variants are stress tests, not observed prevalence. The language of a text does not constrain a person's naming community. Excluded: Arabic-script Ottoman Turkish, dialects, speech, other Turkic languages, minority naming communities, exhaustive name inventories, identity linking and release readiness. Scope lists are the research envelope, not coverage claims.

## Topic coverage

**Breadth delivered:** six topic syntheses. **Review:** all in-progress; no independent language review. **NER outcomes:** untested. These states are independent.

- **morphology: in-progress**. [Suffixes after names, exceptions and a gap in grammar sources](morphology.md).
- **tokenization: in-progress**. [Apostrophe tokens and treebank units](tokenization.md).
- **person-names: in-progress**. [Surname law, titles before and after names](person-names.md).
- **entity-boundaries: in-progress**. [Suffix, honorific and plural boundaries](entity-boundaries.md).
- **ambiguity: in-progress**. [Names that are common words](ambiguity.md).
- **mixed-script: in-progress**. [Diacritic loss, foreign names; partial](mixed-script.md).

Casing and writing-system questions are covered in [TUR-003](findings/TUR-003.md) and [TUR-004](findings/TUR-004.md). Context and word order is not-started. Domain and register rest on constructed contrasts and abstract-level corpus information.

## Finding index

- [TUR-001: The apostrophe after a proper name marks a name/suffix boundary inside one whitespace token](findings/TUR-001.md), draft; observation confidence medium; hypothesis untested; proposal ready for owner review.
- [TUR-002: Where no apostrophe is written (exceptions and noisy text) the name/suffix boundary has no orthographic cue](findings/TUR-002.md), draft; observation confidence medium; hypothesis untested.
- [TUR-003: Dotted and dotless I: locale-unaware case conversion corrupts Turkish names and breaks round trips](findings/TUR-003.md), draft; observation confidence medium; hypothesis untested.
- [TUR-004: ASCII-fied Turkish (diacritic loss) hides name identity and creates collisions with common words](findings/TUR-004.md), draft; observation confidence low; hypothesis untested.
- [TUR-005: Post-1934 surnames and titles around Turkish names: which neighbouring tokens belong to the PERSON span](findings/TUR-005.md), draft; observation confidence medium; hypothesis untested.
- [TUR-006: Many Turkish given names are common nouns: capitalization and the apostrophe are the surface cues](findings/TUR-006.md), draft; observation confidence medium; hypothesis untested.

## Decision brief

Treat suffix attachment as three cases (apostrophe-marked, unmarked by rule, unmarked by noise) and test casing and diacritic folds separately. See the [decision brief](decision-brief.md).

## Known gaps and reviewer needs

Almost all sources were read as fetch summaries or abstracts; PDFs could not be decoded. No Turkish grammar was read (Göksel and Kerslake 2005 was identified, not accessed), so vowel harmony, suffix chains, `-oğlu` and `-gil`, and Arabic/Persian-origin or Ottoman spelling variation are unsourced. No Turkish NER annotation guideline or dataset documentation was read in full. Obtain qualified Turkish review of all examples and re-verify TDK, Unicode and law text against the primary pages. No corpus frequency, measured accuracy or language support is established. See [sources](sources.md).

## Research issues and revisions

No research issue exists and none was created. 2026-10-04: initial dossier with six findings, six topic files and a decision brief, produced with the dossier-initialize, dossier-deep-research and dossier-document skills; prefix TUR checked unique across studies at the time.
