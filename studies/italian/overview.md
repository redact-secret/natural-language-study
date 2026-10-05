---
language_key: italian
display_name: Italian
language_tags:
- it-IT
scripts:
- Latn
id_prefix: ITA
status: draft
scope:
  varieties:
  - Contemporary standard written Italian
  regions:
  - Italy
  registers:
  - edited prose
  - formal correspondence
  - registry-style lists
  - constructed robustness contrasts
  domains:
  - general correspondence
  - general narrative
  - civil-registry-style naming
  entity_types:
  - PERSON
research_issues: []
updated: '2026-10-04'
---

# Italian: NER research dossier

## Research questions and motivation

Italian is studied as a Romance relative of [French](../french/overview.md), with Latin script only. The main questions: how to separate external elision and articulated prepositions from name-internal particles (dell'Anna versus Dell'Orso), whether particle case can decide membership, how titles and surname-first order sit around a name, which representation variants of accents and apostrophes matter, and which common words collide with names.

## Scope and exclusions

Contemporary standard written Italian, it-IT. `it-CH` is not included: no Swiss source was examined. PERSON only; Latn only. Excluded: dialects and regional variants (unless sourced, and none was), historical spelling, speech, identity linking, frequency claims, and non-Latin transliteration. Language of text does not constrain a person's nationality or naming community. Examples are illustrative, not fixtures.

## Topic coverage

**Breadth delivered:** six topic syntheses. **Review:** none independent; all in-progress. **NER outcomes:** untested. These states are independent.

- **morphology: in-progress.** [Elision, articulated prepositions and enclitics](morphology.md).
- **tokenization: in-progress.** [Apostrophe units and abbreviations](tokenization.md).
- **person-names: in-progress.** [Order, particles, titles, legal naming](person-names.md).
- **entity-boundaries: in-progress.** [Inside versus outside candidates](entity-boundaries.md).
- **ambiguity: in-progress.** [Person versus noun, place, demonym](ambiguity.md).
- **mixed-script: in-progress.** [Latin-internal variants; foreign scripts out of scope](mixed-script.md).

Writing-system and casing are integrated in the findings. A word-order feature is not-started.

## Finding index

- [ITA-001: Elided articles and prepositions can touch a name without belonging to it, while D'/Dell' can be name-internal](findings/ITA-001.md), draft; confidence medium; hypothesis untested; handoffs deferred.
- [ITA-002: Surname particles may be lowercase (da Vinci) or capitalized (De Luca, D'Eredità): case cannot decide membership](findings/ITA-002.md), draft; confidence medium; untested.
- [ITA-003: Titles and surname-first registry order sit outside or around the name span and depend on register](findings/ITA-003.md), draft; confidence medium; untested.
- [ITA-004: Accents, apostrophes and Unicode form](findings/ITA-004.md), draft; confidence medium; untested.
- [ITA-005: Italian name homographs](findings/ITA-005.md), draft; confidence medium; untested.
- [ITA-006: Italian naming law and practice](findings/ITA-006.md), draft; confidence low; untested.

## Decision brief

Do not let particle case or UD-style splitting decide PERSON membership; run elision role, particle case and encoding variants as separate experiments. See the [decision brief](decision-brief.md).

## Known gaps and reviewer needs

Sources are [recorded](sources.md) with fetch-tool limitations: extracts were condensed and some records are secondary. Missing: a competent Italian reader to review examples, an attested corpus with reuse rights, frequencies, sources for the article before first names (la Rossi), Ing./On. titles, ALL-CAPS surname-first registries, married-name forms with `in`, transliteration, and the text of ruling 131/2022. No measured accuracy or language support is claimed.

## Research issues and revisions

No issue linked; none created. 2026-10-04: new dossier created with six findings, sources, six topic files and a decision brief. Examples are synthetic or short attested fragments. No other dossier was edited.
