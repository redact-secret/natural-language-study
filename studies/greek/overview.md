---
language_key: greek
display_name: Greek
language_tags:
- el
- el-GR
scripts:
- Grek
- Latn
id_prefix: GRE
status: draft
scope:
  varieties:
  - Contemporary standard Modern Greek (monotonic orthography); polytonic only as a contrast
  regions:
  - Greece
  registers:
  - edited prose
  - official identity-document romanization
  - informal Greeklish (abstract-level evidence)
  - constructed robustness contrasts
  domains:
  - news and general prose (via treebank descriptions)
  - general correspondence
  entity_types:
  - PERSON
research_issues: []
updated: '2026-10-04'
---

# Greek: NER research dossier

## Research questions and motivation

How should a PERSON recognizer handle Modern Greek names that inflect for case (so the surface mention differs from the lemma), take an article and fused preposition on the left, carry feminine surnames in genitive form, vary in accent, case and Unicode form, appear in Latin transliteration, and collide with common nouns?

## Scope and exclusions

Contemporary standard Modern Greek in Greece, monotonic orthography. The tag `el-GR` is a scope label for Greece; `el-CY` (Cyprus) is not included because no Cypriot source was gathered. Script is Grek; Latn appears only for transliteration, Greeklish and homoglyph contrasts, not as general Latin-script coverage. PERSON only. Excludes Ancient and Koine Greek, dialects, speech, historical orthography beyond the polytonic contrast, identity linking and release readiness. Synthetic examples are stress contrasts, not observed prevalence; no naming community is treated as representative of all Greek speakers.

## Topic coverage

**Breadth delivered:** six substantive topic syntheses. **Review:** all in-progress; no independent language review recorded. **NER outcomes:** untested. These states are independent.

- **morphology: in-progress**. [Case endings and accent shifts](morphology.md).
- **tokenization: in-progress**. [Fused preposition-article forms and abbreviations](tokenization.md).
- **person-names: in-progress**. [Genitive-form women's surnames and suffixes](person-names.md).
- **entity-boundaries: in-progress**. [Articles, fused prepositions and titles](entity-boundaries.md).
- **ambiguity: in-progress**. [Names that are also words](ambiguity.md).
- **mixed-script: in-progress**. [Transliteration, Greeklish and look-alike letters](mixed-script.md).

Orthography and Unicode form (writing-system) is covered in [GRE-004](findings/GRE-004.md). Casing is integrated into GRE-004 and GRE-006. Context is studied only through matched local contrasts; word-order features are not-started. Domain coverage is secondary descriptions plus constructed examples, not a representative corpus.

## Finding index

- [GRE-001: Greek names inflect for case, so the surface mention often differs from the lemma](findings/GRE-001.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [GRE-002: The Greek feminine surname is genitive in form, so a surname string can be masculine genitive or feminine nominative](findings/GRE-002.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [GRE-003: Greek articles, fused preposition-article forms and abbreviated titles sit next to names as external cues](findings/GRE-003.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [GRE-004: Greek tonos, final sigma, capitals and Unicode forms give one name several strings](findings/GRE-004.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [GRE-005: Greek names appear in official, informal and look-alike Latin forms, so transliteration is not identity](findings/GRE-005.md), draft; observation confidence low; hypothesis untested; handoffs deferred.
- [GRE-006: Greek given names that are also common nouns or places need context, since case and article cues are weak](findings/GRE-006.md), draft; observation confidence low; hypothesis untested; handoffs deferred.

## Decision brief

Keep case-form handling, article/title boundary policy, Unicode/accent normalization, transliteration and homograph disambiguation as separate experiments. See the [decision brief](decision-brief.md).

## Known gaps and reviewer needs

Neither major Greek reference grammar (Holton et al.; Triantafyllidis) nor the ELOT 743 text was read; most sources are Wikipedia, Wiktionary or treebank documentation read through summarizing fetches, so claims are leads that need primary verification. Missing: Cypriot and dialect evidence, current legal naming and passport rules, apostrophe elision near names, vocative -ε versus -ο distribution, verified lexical status of Ελπίδα, Αγάπη, Άνθος and Μύρτος, attested corpus examples with reuse rights, and qualified Greek review of translations, spans and the examples. No corpus frequency, accuracy or language support is established. [Sources](sources.md) record locators and limitations.

## Research issues and revisions

No research issue is linked; none was created. 2026-10-04: new dossier with six topic syntheses, six draft findings, fourteen source records and a decision brief, produced with the dossier-initialize, dossier-deep-research and dossier-document skills.
