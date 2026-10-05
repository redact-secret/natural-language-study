---
language_key: hindi
display_name: Hindi
language_tags:
- hi-IN
- hi
- hi-Latn
scripts:
- Deva
- Latn
id_prefix: HIN
status: draft
scope:
  varieties:
  - Contemporary standard written Hindi (Khari Boli based)
  regions:
  - India
  registers:
  - edited prose and official orthography
  - romanized Hindi and Hindi-English code-mixed social media text (contrast only)
  - constructed robustness contrasts
  domains:
  - general narrative and correspondence
  - news and tourism text as represented in cited corpora
  entity_types:
  - PERSON
research_issues: []
updated: '2026-10-04'
---

# Hindi: NER research dossier

## Research questions and motivation

How do postposition attachment, honorific tokens, Devanagari encoding variation, the lack of casing, name/common-word collisions and romanization affect the existence and extent of PERSON mentions in Hindi?

## Scope and exclusions

**Language scope.** This dossier covers Hindi (hi, hi-IN) only. The original request used the word "Indian". India has many languages in several scripts, and no single set of findings describes them. Nothing here is a claim about Marathi, Bengali, Urdu, Tamil or any other Indian language. Where another language is mentioned, it is only to say that its behavior is not examined. Because Hindi, Marathi and Nepali share the Devanagari script, script findings (nukta, bindu, danda) are stated for Hindi text and must not be assumed for them.

**Scope gap recorded.** A pan-Indian study would need separate dossiers per language (and per script), each with its own sources and review. None is started here.

Scripts: Devanagari (Deva) is the main script. Latin (Latn) is used for romanized Hindi and Hinglish contrasts and is tagged `hi-Latn`. PERSON in edited prose; synthetic noisy variants are stress tests, not observed prevalence. Language of text does not constrain a person's nationality or naming community. Exclude Urdu in Perso-Arabic script (also a Hindustani register but a different script and a separate study), dialects and Bhojpuri/Maithili/Rajasthani, historical Hindi, speech, exhaustive naming inventories, identity linking and release readiness. The regional coverage is "India" only as a label; no state, caste or religious community is studied.

## Topic coverage

**Breadth delivered:** six substantive topic syntheses. **Review:** all in-progress; no independent language review recorded. **NER outcomes:** untested. These states are independent.

- **morphology: in-progress**. [Postpositions, pronoun fusion, ergative ने and oblique-form leads](morphology.md).
- **tokenization: in-progress**. [Whitespace, danda, joiners and digits](tokenization.md).
- **person-names: in-progress**. [Name structure, surnames, honorifics and titles](person-names.md).
- **entity-boundaries: in-progress**. [Title, honorific and postposition policy mapping across sources](entity-boundaries.md).
- **ambiguity: in-progress**. [Name and common-word collisions without a casing cue](ambiguity.md).
- **mixed-script: in-progress**. [Romanization, Hinglish and Devanagari-Latin mixing](mixed-script.md).

Writing-system and casing questions are integrated into findings HIN-003 to HIN-005. Context and word-order is not a separate topic: free word order is noted only as a source-reported challenge. Domain coverage is limited to the corpora cited by sources and constructed examples, not a representative corpus.

## Finding index

- [HIN-001: Standard Hindi writes case postpositions after names as separate words but fuses them to pronouns](findings/HIN-001.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [HIN-002: Honorific श्री and जी are separate words unless part of the name, and annotation schemes disagree on including them](findings/HIN-002.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [HIN-003: Nukta letters have two encodings that NFC collapses, and standard Hindi spelling may drop the nukta in names](findings/HIN-003.md), draft; observation confidence high (encoding facts; the orthographic part is medium); hypothesis untested; handoffs deferred.
- [HIN-004: Anusvara, chandrabindu, half-consonant and joiner variation changes name strings without changing the name; danda sticks to the last word](findings/HIN-004.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [HIN-005: Devanagari offers no capitalization cue, and Hindi names collide with common words in the same script](findings/HIN-005.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.
- [HIN-006: Romanized Hindi names have no single mapping from Devanagari, and code-mixed text keeps Hindi grammar words around Latin names](findings/HIN-006.md), draft; observation confidence medium; hypothesis untested; handoffs deferred.

## Decision brief

See the [handoff proposal](decision-brief.md) for contrast families, held-fixed variables and reversal conditions. It is a proposal for owner review, not an adopted policy.

## Known gaps and reviewer needs

- No Hindi grammar (for example Kachru's or McGregor's) was accessible, so oblique, vocative and gender-inflected name forms are unsourced leads in [morphology](morphology.md).
- Naming practice rests on a W3C general page and a tertiary encyclopedia lead; a reliable anthropological or sociolinguistic source on North Indian naming is needed. See [person names](person-names.md).
- The IJCNLP-08 workshop proceedings, HiNER annotation guideline detail and the HiNER dataset itself were not examined beyond what the sources record; no corpus counts of name variants are available.
- ISO 15919, IAST and ITRANS standards were not read at primary sources.
- The Central Hindi Directorate PDF was read through extracted text with font artifacts; a visual check of its examples is needed.
- Competent Hindi review of all translations and examples; all examples here are synthetic or adapted and author-checked only.
- No model result, benchmark or fastner code inspection was performed.

[Sources](sources.md) record locators and limitations.

## Research issues and revisions

No GitHub issue was created for this dossier (none authorized). 2026-10-04: new dossier created with six topic syntheses, thirteen source records and six draft findings. Next action: obtain a qualified Hindi reviewer, then decide whether the decision brief should become `ner-evidence` work.
