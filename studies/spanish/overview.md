---
language_key: spanish
display_name: Spanish
language_tags:
- es
- es-ES
- es-AR
scripts:
- Latn
id_prefix: SPA
status: draft
scope:
  varieties:
  - Contemporary standard written Spanish (RAE pan-Hispanic norm)
  regions:
  - Spain
  - Argentina (civil-law marital naming only)
  registers:
  - edited prose
  - administrative and legal naming
  - constructed robustness contrasts
  domains:
  - newswire (CoNLL-2002 context)
  - general correspondence
  entity_types:
  - PERSON
research_issues: []
updated: '2026-10-04'
---

# Spanish: NER research dossier

## Research questions and motivation

How should a PERSON recognizer treat Spanish double surnames with optional connectors, lowercase or capitalized particles, the contractions del and al, titles and personal a, accented and decomposed letters, and given-name homographs? Spanish is studied as a Latin-script relative of [French](../french/overview.md), but nothing here assumes the two behave alike.

## Scope and exclusions

Contemporary standard written Spanish with a Spain and Argentina source envelope. The tags `es-ES` and `es-AR` are justified only by the Spanish state registry law and the Argentine civil code cited in [sources](sources.md); `es` marks the RAE norm. Mexico and other Latin American varieties are not researched because no source was gathered, even though they hold most Spanish speakers; Rio de la Plata beyond Argentine marital naming, Caribbean, Andean and US Spanish are gaps. PERSON only. Script is Latn; there is no alternate-script research, only orthography and Unicode form. Excludes speech, historical Spanish, Catalan, Galician and Basque naming, identity linking and release readiness. Synthetic examples are stress contrasts, not observed prevalence.

## Topic coverage

**Breadth delivered:** six substantive topic syntheses. **Review:** all in-progress; no independent language review recorded. **NER outcomes:** untested. These states are independent.

- **morphology: in-progress**. [Contractions and enclitics](morphology.md).
- **tokenization: in-progress**. [Token conventions versus name boundaries](tokenization.md).
- **person-names: in-progress**. [Double surnames, connectors, particle case](person-names.md).
- **entity-boundaries: in-progress**. [Titles, personal a, article cases](entity-boundaries.md).
- **ambiguity: in-progress**. [Given-name homographs](ambiguity.md).
- **mixed-script: in-progress**. [Diacritics and Unicode form; no alternate script](mixed-script.md).

Casing is integrated in SPA-002. Context is studied only through matched local contrasts. Domain coverage is edited-language sources and constructed examples, not a representative corpus.

## Finding index

- [SPA-001: Spanish double surnames may carry optional de, y or i connectors, so surname count is not fixed](findings/SPA-001.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [SPA-002: Spanish surname particles are lowercase after a given name and capitalized without it, so case cannot decide membership](findings/SPA-002.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [SPA-003: The contractions del and al are external boundaries unless El is part of a name; nicknames differ](findings/SPA-003.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [SPA-004: Titles and the personal a are left-context cues outside the PERSON span, with exceptions](findings/SPA-004.md), draft; observation confidence low; hypothesis untested; handoffs deferred.
- [SPA-005: Capitals carry accents and Unicode forms vary, so canonical normalization is separate from accent loss](findings/SPA-005.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [SPA-006: Common-noun and place homographs of Spanish given names need context, not a name lexicon alone](findings/SPA-006.md), draft; observation confidence low; hypothesis untested; handoffs deferred.

## Decision brief

Reject fixed name shapes and case gates; keep contraction, connector and normalization handling as separate experiments. See the [decision brief](decision-brief.md).

## Known gaps and reviewer needs

The RAE site returned HTTP 403 to every fetch, so RAE-based claims rest on search-result excerpts and must be re-verified against live pages. Several other sources were read as page summaries. Missing: Mexican and wider Latin American civil-registry and usage sources, dictionary verification of homographs, any inverted-punctuation or accent-loss source, attested corpus examples with reuse rights, and qualified Spanish review of translations and spans. No corpus frequency, accuracy or language support is established.

## Research issues and revisions

No research issue is linked; none was created. 2026-10-04: new dossier with six topic syntheses, six draft findings, fourteen source records and a decision brief, produced with the dossier-initialize, dossier-deep-research and dossier-document skills.
