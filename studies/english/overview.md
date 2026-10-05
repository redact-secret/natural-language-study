---
language_key: english
display_name: English
language_tags:
- en-GB
- en-US
scripts:
- Latn
- Hang
- Cyrl
id_prefix: ENG
status: draft
scope:
  varieties:
  - Contemporary edited British and American English
  regions:
  - United Kingdom
  - United States
  registers:
  - edited prose
  - constructed robustness contrasts
  domains:
  - general correspondence
  - general narrative
  entity_types:
  - PERSON
research_issues:
- https://github.com/redact-secret/natural-language-study/issues/1
updated: '2026-10-04'
---

# English: NER research dossier

## Research questions and motivation

Which punctuation belongs inside a name, how do coordinated mentions stay separate, and when do casing or script gates reject names or accept ordinary words?

## Scope and exclusions

Contemporary edited British and American English in United Kingdom, United States. PERSON in general correspondence and narrative; synthetic noisy variants are stress tests, not observed prevalence. Language of text does not constrain a person's nationality or naming community. Scripts listed in metadata are the research envelope, not claims of complete coverage. Hangul is limited to constructed quoted-name carrier sentences. Cyrillic is limited to artificial one-character robustness substitutions.

Exclude historical language, dialect coverage, speech, exhaustive naming inventories, identity linking and release readiness. Regional coverage is provisional; no exhaustive naming-community coverage is claimed.

## Topic coverage

**Breadth delivered:** six substantive topic syntheses. **Review:** all in-progress; no independent language review recorded. **NER outcomes:** untested. These states are independent.

- **morphology: in-progress**. [Possessive and name-internal roles; coordinated owners](morphology.md).
- **tokenization: in-progress**. [Initial periods and joining; audit before replacing tokenizer](tokenization.md).
- **person-names: in-progress**. [Surface components without mandatory first/last parsing](person-names.md).
- **entity-boundaries: in-progress**. [Punctuation roles under the target contract](entity-boundaries.md).
- **ambiguity: in-progress**. [Rose lexical readings and matched casing controls](ambiguity.md).
- **mixed-script: in-progress**. [Accented Latin, quoted Hangul and artificial Cyrillic substitution](mixed-script.md).

Writing-system and casing questions are integrated into the topic files. Context is studied through matched local contrasts; an independent word-order feature remains not-started. Domain/register coverage consists of edited-language sources and constructed stress examples, not a representative corpus.

## Finding index

- [ENG-005: Script identity and visual similarity must not determine PERSON membership](findings/ENG-005.md), draft; observation confidence medium; hypothesis untested; local owner-review proposal.

- [ENG-004: Joint possession does not merge the people mentioned](findings/ENG-004.md), draft; observation confidence high; hypothesis untested.
- [ENG-001: Apostrophes inside names versus attached clitics](findings/ENG-001.md), draft; observation confidence high; hypothesis untested; handoffs deferred.
- [ENG-002: Capitalization is a contextual cue, not a PERSON test](findings/ENG-002.md), draft; observation confidence high; hypothesis untested; handoffs deferred.
- [ENG-003: Initials, titles and multipart names cross token boundaries](findings/ENG-003.md), draft; observation confidence high; hypothesis untested; handoffs deferred.

## Decision brief

The next English experiment is about separating mentions, not rebuilding apostrophe splitting. See the [handoff proposal](decision-brief.md) for contrast families, policy choices and falsification criteria.

## Known gaps and reviewer needs

Findings are source-backed desk research, with the deeper pass documented in the decision brief. Obtain competent language review of translations, ambiguous examples and proposed spans; expand attested/domain coverage with reuse rights before downstream fixture adoption. No corpus frequency, measured accuracy or language support is established. [Sources](sources.md) record locators and limitations.

## Research issues and revisions

[Research epic](https://github.com/redact-secret/natural-language-study/issues/1); GitHub issue created. 2026-10-04: initial three-finding dossier, now extended to four findings. Next action: use the decision brief and review finding ENG-001 and its matched negatives, then resolve evidence-policy questions.

2026-10-04: applied dossier scope audit, deep research and documentation skills; added ENG-004 and a decision brief. Prior findings and issue IDs preserved.

2026-10-04 breadth completion: added all six topic syntheses, expanded source records and indexed new findings. Existing IDs and review states retained; see the [delivery audit](../../research/dossier-expansion.md).
