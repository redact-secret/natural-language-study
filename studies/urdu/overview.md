---
language_key: urdu
display_name: Urdu
language_tags:
- ur
- ur-PK
- ur-Latn
scripts:
- Arab
- Latn
id_prefix: URD
status: draft
scope:
  varieties:
  - Standard written Urdu as used in Pakistan
  regions:
  - Pakistan
  registers:
  - edited prose and news (as reflected in cited datasets)
  - informal romanized Urdu (ur-Latn) as contrast only
  domains:
  - general text
  - news-derived corpora
  entity_types:
  - PERSON
research_issues: []
updated: '2026-10-04'
---

# Urdu (Pakistan): NER research dossier

## Research questions and motivation

Which properties of Urdu writing and naming change where a PERSON span starts and ends, or whether a string is a name at all? The dossier asks six concrete questions: code point variants of the same name ([URD-001](findings/URD-001.md)), unreliable whitespace ([URD-002](findings/URD-002.md)), name/common-noun ambiguity without letter case ([URD-003](findings/URD-003.md)), name structure and title policy ([URD-004](findings/URD-004.md)), script variation and mixing ([URD-005](findings/URD-005.md)), and postposition and nesting boundaries ([URD-006](findings/URD-006.md)).

## Scope and exclusions

Standard written Urdu in Pakistan, entity type PERSON, in the scripts `Arab` (Urdu orthography) and `Latn` (romanized Urdu, tag `ur-Latn`, used only for contrasts). Urdu text from India, the diaspora and historical or poetic registers is not studied.

**Scope gap: other languages of Pakistan.** Pakistan is multilingual (Punjabi, Sindhi, Pashto, Balochi, Saraiki and others). The request named "Pakistan"; this dossier covers Urdu only and **makes no claim about any other Pakistani language**, its naming conventions, or its Arabic-script orthographies, even though those languages share characters, names and text with Urdu. Language of text does not constrain a person's naming community; speakers of other Pakistani languages routinely appear in Urdu text. Separate dossiers would be needed for the other languages.

Also excluded: speech, handwriting and Nastaliq rendering, measured prevalence, model results, identity linking, and non-PERSON entities except where a source forces a boundary decision. No Hindi dossier existed when this was written, so Urdu-Devanagari comparison is limited to one transliteration paper ([URD-005](findings/URD-005.md)).

## Topic coverage

**Breadth delivered:** six topic syntheses plus six findings. **Review:** all in-progress; no independent language review. **NER outcomes:** untested. These states are independent.

- **morphology: in-progress**. [Postpositions, name-internal elements and what remains unverified](morphology.md).
- **tokenization: in-progress**. [Space omission and insertion, ZWNJ and token units](tokenization.md).
- **person-names: in-progress**. [Name parts, titles, honorifics and relational names](person-names.md).
- **entity-boundaries: in-progress**. [Right edges, nested versus maximal names, titles](entity-boundaries.md).
- **ambiguity: in-progress**. [Names that are also ordinary words](ambiguity.md).
- **mixed-script: in-progress**. [Code points, bidi, Roman Urdu and Devanagari](mixed-script.md).

Writing-system and casing questions are integrated into the topic files and URD-001 and URD-003. Context and word order, and domain and register, are not-started apart from the news-genre caveat.

## Finding index

- [URD-001: Urdu names have Arabic-letter and Urdu-letter code point variants that Unicode normalization does not unify](findings/URD-001.md), draft; observation confidence medium; hypothesis untested.
- [URD-002: Whitespace is an unreliable word and name boundary in Urdu because of joining behavior](findings/URD-002.md), draft; observation confidence medium; hypothesis untested.
- [URD-003: Without capitalization, Urdu person names that are also common nouns depend on local context](findings/URD-003.md), draft; observation confidence medium; hypothesis untested.
- [URD-004: Pakistani Muslim naming is not a single given-plus-family template, and title versus name-part status needs a policy](findings/URD-004.md), draft; observation confidence low; hypothesis untested.
- [URD-005: Romanized, Devanagari and mixed-script renderings of Urdu names are variable and not a reversible identity](findings/URD-005.md), draft; observation confidence medium; hypothesis untested.
- [URD-006: Following postpositions are a boundary cue but not a sufficient one, and maximal versus nested entity policy is unresolved](findings/URD-006.md), draft; observation confidence medium; hypothesis untested.

No downstream links exist; every handoff is deferred or proposal-only.

## Decision brief

Decide how to treat Urdu whitespace, code point variants and title policy before building any Urdu PERSON evidence. See the [decision brief](decision-brief.md).

## Known gaps and reviewer needs

- No qualified Urdu reviewer; all translations, readings and Urdu strings are author-constructed or quoted and unchecked.
- No primary orthographic or naming authority was located (National Language Authority, NADRA). The naming article ([URD-S013](sources.md#urd-s013)) was seen only as a search summary.
- No grammar was read ([URD-S017](sources.md#urd-s017) is a publisher page); postposition and izafat statements are unverified against a grammar.
- Several papers were read as extracted text with garbled Urdu glyphs; Urdu strings in them are not reproduced.
- Person/place and person/organization ambiguity, honorific suffixes, izafat, non-Muslim and non-Urdu-speaking naming communities, handwriting and OCR noise, and attested social-media text are not covered.
- No prevalence, no model or benchmark results, no claim that any language support exists.

See [sources](sources.md) for locators and limitations.

## Research issues and revisions

No research issue exists; none was created. 2026-10-04: initial broad desk-research dossier (overview, sources, six topics, six findings, decision brief). IDs URD-001 to URD-006 allocated; prefix URD checked against existing overviews (ENG, FRA, ITA, JPN, KOR, POR, SPA at that time).
