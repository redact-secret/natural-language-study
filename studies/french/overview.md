---
language_key: french
display_name: French
language_tags:
- fr-FR
- fr-CA
scripts:
- Latn
- Hang
id_prefix: FRA
status: draft
scope:
  varieties:
  - Contemporary standard written French; Québec guidance is explicitly scoped
  regions:
  - France
  - Québec
  registers:
  - edited prose
  - constructed robustness contrasts
  domains:
  - general correspondence
  - general narrative
  entity_types:
  - PERSON
research_issues:
- https://github.com/redact-secret/natural-language-study/issues/2
updated: '2026-10-04'
---

# French: NER research dossier

## Research questions and motivation

How can external elision be distinguished from internal name particles, while preserving accents, compound names and the difference between direct and figurative reference?

## Scope and exclusions

Contemporary standard written French, with a France/Québec research envelope. The consulted editorial authorities are Canadian; their recommendations are not assumed to represent all French usage. PERSON in general correspondence and narrative; synthetic noisy variants are stress tests, not observed prevalence. Language of text does not constrain a person's nationality or naming community. Scripts listed in metadata are the research envelope, not claims of complete coverage. Hangul is limited to constructed quoted-name carrier sentences.

Exclude historical language, dialect coverage, speech, exhaustive naming inventories, identity linking and release readiness. Regional coverage is provisional; no exhaustive naming-community coverage is claimed.

## Topic coverage

**Breadth delivered:** six substantive topic syntheses. **Review:** all in-progress; no independent language review recorded. **NER outcomes:** untested. These states are independent.

- **morphology: in-progress**. [External elision versus internal surname particle](morphology.md).
- **tokenization: in-progress**. [Within-Latin-token starts and cross-token names](tokenization.md).
- **person-names: in-progress**. [Compound names and conflicting particle-casing guidance](person-names.md).
- **entity-boundaries: in-progress**. [Explicit French title/particle boundary proposals](entity-boundaries.md).
- **ambiguity: in-progress**. [Antonomasia and direct versus figurative reference](ambiguity.md).
- **mixed-script: in-progress**. [Accents, decomposition and constructed cross-script quotation](mixed-script.md).

Writing-system and casing questions are integrated into the topic files. Context is studied through matched local contrasts; an independent word-order feature remains not-started. Domain/register coverage consists of edited-language sources and constructed stress examples, not a representative corpus.

## Finding index

- [FRA-005: Name-derived common-noun uses require a referent policy](findings/FRA-005.md), draft; observation confidence medium; hypothesis untested; local owner-review proposal.

- [FRA-004: Official particle-casing guidance disagrees, so case must not decide membership](findings/FRA-004.md), draft; observation confidence high; hypothesis untested.
- [FRA-001: Lowercase particles can belong inside personal names](findings/FRA-001.md), draft; observation confidence high; hypothesis untested; handoffs deferred.
- [FRA-002: Elided prepositions can touch a name without belonging to it](findings/FRA-002.md), draft; observation confidence high; hypothesis untested; handoffs deferred.
- [FRA-003: Compound names and canonical accents must survive matching](findings/FRA-003.md), draft; observation confidence high; hypothesis untested; handoffs deferred.

## Decision brief

Reject a hard casing gate for surname particles; keep external-elision handling a distinct boundary experiment. See the [handoff proposal](decision-brief.md) for contrast families, policy choices and falsification criteria.

## Known gaps and reviewer needs

Findings are source-backed desk research, with the deeper pass documented in the decision brief. Obtain competent language review of translations, ambiguous examples and proposed spans; expand attested/domain coverage with reuse rights before downstream fixture adoption. No corpus frequency, measured accuracy or language support is established. [Sources](sources.md) record locators and limitations.

## Research issues and revisions

[Research epic](https://github.com/redact-secret/natural-language-study/issues/2); GitHub issue created. 2026-10-04: initial three-finding dossier, now extended to four findings. Next action: use the decision brief and review finding FRA-001 and its matched negatives, then resolve evidence-policy questions.

2026-10-04: applied dossier scope audit, deep research and documentation skills; added FRA-004 and a decision brief. Prior findings and issue IDs preserved.

2026-10-04 breadth completion: added all six topic syntheses, expanded source records and indexed new findings. Existing IDs and review states retained; see the [delivery audit](../../research/dossier-expansion.md).
