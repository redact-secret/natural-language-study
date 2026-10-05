---
language_key: japanese
display_name: Japanese
language_tags:
- ja-JP
scripts:
- Hani
- Hira
- Kana
- Latn
id_prefix: JPN
status: draft
scope:
  varieties:
  - Contemporary standard written Japanese
  regions:
  - Japan
  registers:
  - edited prose
  - constructed robustness contrasts
  domains:
  - general correspondence
  - general narrative
  entity_types:
  - PERSON
research_issues:
- https://github.com/redact-secret/natural-language-study/issues/4
updated: '2026-10-04'
---

# Japanese: NER research dossier

## Research questions and motivation

Which candidate edges are required inside kana runs, which script transitions are internal to names, and how can naming and address context help without presuming one analyzer or romanized order?

## Scope and exclusions

Contemporary standard written Japanese in Japan. PERSON in general correspondence and narrative; synthetic noisy variants are stress tests, not observed prevalence. Language of text does not constrain a person's nationality or naming community. Scripts listed in metadata are the research envelope, not claims of complete coverage.

Exclude historical language, dialect coverage, speech, exhaustive naming inventories, identity linking and release readiness. Regional coverage is provisional; no exhaustive naming-community coverage is claimed.

## Topic coverage

**Breadth delivered:** six substantive topic syntheses. **Review:** all in-progress; no independent language review recorded. **NER outcomes:** untested. These states are independent.

- **morphology: in-progress**. [Address suffix versus following particle and ordinary role nouns](morphology.md).
- **tokenization: in-progress**. [Within-kana candidate reachability before model choice](tokenization.md).
- **person-names: in-progress**. [Written name order, kana/Han names and address forms](person-names.md).
- **entity-boundaries: in-progress**. [Internal endpoints versus internal middle dots](entity-boundaries.md).
- **ambiguity: in-progress**. [Script- and suffix-matched non-name controls](ambiguity.md).
- **mixed-script: in-progress**. [Script_Extensions, internal script transitions and width distinctions](mixed-script.md).

Writing-system and casing questions are integrated into the topic files. Context is studied through matched local contrasts; an independent word-order feature remains not-started. Domain/register coverage consists of edited-language sources and constructed stress examples, not a representative corpus.

## Finding index

- [JPN-005: Romanized name order and readings do not provide a unique name parser](findings/JPN-005.md), draft; observation confidence medium; hypothesis untested; local owner-review proposal.

- [JPN-004: Within-token boundary capability must be verified before a PERSON model choice](findings/JPN-004.md), draft; observation confidence high; hypothesis untested.
- [JPN-001: Segmentation units do not define PERSON spans](findings/JPN-001.md), draft; observation confidence high; hypothesis untested; handoffs deferred.
- [JPN-002: Address suffixes and following particles need separate decisions](findings/JPN-002.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [JPN-003: Script transitions are cues, not entity boundaries](findings/JPN-003.md), draft; observation confidence high; hypothesis untested; handoffs deferred.

## Decision brief

Resolve kana candidate granularity and profile eligibility before selecting a Japanese model architecture. See the [handoff proposal](decision-brief.md) for contrast families, policy choices and falsification criteria.

## Known gaps and reviewer needs

Findings are source-backed desk research, with the deeper pass documented in the decision brief. Obtain competent language review of translations, ambiguous examples and proposed spans; expand attested/domain coverage with reuse rights before downstream fixture adoption. No corpus frequency, measured accuracy or language support is established. [Sources](sources.md) record locators and limitations.

## Research issues and revisions

[Research epic](https://github.com/redact-secret/natural-language-study/issues/4); GitHub issue created. 2026-10-04: initial three-finding dossier, now extended to four findings. Next action: use the decision brief and review finding JPN-001 and its matched negatives, then resolve evidence-policy questions.

2026-10-04: applied dossier scope audit, deep research and documentation skills; added JPN-004 and a decision brief. Prior findings and issue IDs preserved.

2026-10-04 breadth completion: added all six topic syntheses, expanded source records and indexed new findings. Existing IDs and review states retained; see the [delivery audit](../../research/dossier-expansion.md).
