---
language_key: korean
display_name: Korean
language_tags:
- ko-KR
scripts:
- Hang
- Hani
- Latn
id_prefix: KOR
status: draft
scope:
  varieties:
  - Contemporary South Korean standard written Korean
  regions:
  - South Korea
  registers:
  - edited prose
  - constructed robustness contrasts
  domains:
  - general correspondence
  - general narrative
  entity_types:
  - PERSON
research_issues:
- https://github.com/redact-secret/natural-language-study/issues/5
updated: '2026-10-04'
---

# Korean: NER research dossier

## Research questions and motivation

How do attached particles, name/title spacing, suffix annotation, 씨 reference and romanized forms affect the existence and extent of PERSON mentions?

## Scope and exclusions

Contemporary South Korean standard written Korean in South Korea. PERSON in general correspondence and narrative; synthetic noisy variants are stress tests, not observed prevalence. Language of text does not constrain a person's nationality or naming community. Scripts listed in metadata are the research envelope, not claims of complete coverage.

Exclude historical language, dialect coverage, speech, exhaustive naming inventories, identity linking and release readiness. Regional coverage is provisional; no exhaustive naming-community coverage is claimed.

## Topic coverage

**Breadth delivered:** six substantive topic syntheses. **Review:** all in-progress; no independent language review recorded. **NER outcomes:** untested. These states are independent.

- **morphology: in-progress**. [Particles, name-forming 이 and referent-sensitive 씨](morphology.md).
- **tokenization: in-progress**. [Eojeol edges, syllable units and spaced-name constraints](tokenization.md).
- **person-names: in-progress**. [Titles, surname references and romanized variants](person-names.md).
- **entity-boundaries: in-progress**. [Target/external corpus mapping and source coordinates](entity-boundaries.md).
- **ambiguity: in-progress**. [Individual versus surname-category and collective reference](ambiguity.md).
- **mixed-script: in-progress**. [Romanized names plus particles and alternate-script spans](mixed-script.md).

Writing-system and casing questions are integrated into the topic files. Context is studied through matched local contrasts; an independent word-order feature remains not-started. Domain/register coverage consists of edited-language sources and constructed stress examples, not a representative corpus.

## Finding index

- [KOR-005: Romanized personal names admit variation that a single transliterator cannot define](findings/KOR-005.md), draft; observation confidence medium; hypothesis untested; local owner-review proposal.
- [KOR-006: 씨 requires a referent decision as well as a spacing decision](findings/KOR-006.md), draft; observation confidence medium; hypothesis untested; local owner-review proposal.

- [KOR-004: Name-forming 이 and subject-marker 이 require different boundary policies](findings/KOR-004.md), draft; observation confidence medium; hypothesis untested.
- [KOR-001: Attached particles require boundaries within an eojeol](findings/KOR-001.md), draft; observation confidence high; hypothesis untested; handoffs deferred.
- [KOR-002: Name spacing and title spacing are distinct rules](findings/KOR-002.md), draft; observation confidence high; hypothesis untested; handoffs deferred.
- [KOR-003: Hangul normalization must preserve the original text coordinates](findings/KOR-003.md), draft; observation confidence high; hypothesis untested; handoffs deferred.

## Decision brief

Preserve target taxonomy 0.2.0 and explicitly map external suffix-inclusive annotations before scoring. See the [handoff proposal](decision-brief.md) for contrast families, policy choices and falsification criteria.

## Known gaps and reviewer needs

Findings are source-backed desk research, with the deeper pass documented in the decision brief. Obtain competent language review of translations, ambiguous examples and proposed spans; expand attested/domain coverage with reuse rights before downstream fixture adoption. No corpus frequency, measured accuracy or language support is established. [Sources](sources.md) record locators and limitations.

## Research issues and revisions

[Research epic](https://github.com/redact-secret/natural-language-study/issues/5); GitHub issue created. 2026-10-04: initial three-finding dossier, now extended to four findings. Next action: use the decision brief and review finding KOR-001 and its matched negatives, then resolve evidence-policy questions.

2026-10-04: applied dossier scope audit, deep research and documentation skills; added KOR-004 and a decision brief. Prior findings and issue IDs preserved.

2026-10-04 breadth completion: added all six topic syntheses, expanded source records and indexed new findings. Existing IDs and review states retained; see the [delivery audit](../../research/dossier-expansion.md).
