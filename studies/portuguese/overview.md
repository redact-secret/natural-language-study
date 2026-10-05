---
language_key: portuguese
display_name: Portuguese
language_tags:
- pt-PT
- pt-BR
scripts:
- Latn
id_prefix: POR
status: draft
scope:
  varieties:
  - Contemporary standard written Portuguese, European (pt-PT) and Brazilian (pt-BR)
  regions:
  - Portugal
  - Brazil
  registers:
  - edited prose
  - constructed informal and noisy contrasts
  domains:
  - general correspondence
  - general narrative
  entity_types:
  - PERSON
research_issues: []
updated: '2026-10-04'
---

# Portuguese: NER research dossier

## Research questions and motivation

Portuguese is a Latin-script relative of French. The questions are: when do connectors (da, de, do, das, dos, e) belong inside a personal name; how do preposition-article contractions and hyphenated clitics sit next to names; how do spelling variants, diacritics and Unicode forms behave; and where do person names collide with common nouns?

## Scope and exclusions

Contemporary written pt-PT and pt-BR; script Latn only, so mixed-script means accents, normalization and borrowed Latin spellings, not alternate scripts. PERSON only. Other Lusophone varieties (Angola, Mozambique, Cabo Verde and others), speech, historical spelling, Indigenous and immigrant naming communities, and exhaustive name inventories are excluded. Language of a text does not constrain a person's naming community. Language tags are a research envelope; no coverage of either variety is claimed.

## Topic coverage

**Breadth delivered:** six topic syntheses. **Review:** all in-progress; no independent language review recorded. **NER outcomes:** untested. These states are independent.

- **morphology: in-progress**. [Contractions and clitics](morphology.md).
- **tokenization: in-progress**. [Contraction, hyphen and Unicode token units](tokenization.md).
- **person-names: in-progress**. [Registered versus everyday names and titles](person-names.md).
- **entity-boundaries: in-progress**. [Connector, title and clitic inclusion proposals](entity-boundaries.md).
- **ambiguity: in-progress**. [Person versus common noun](ambiguity.md).
- **mixed-script: in-progress**. [Diacritics, NFC/NFD and accent loss within Latin script](mixed-script.md).

Casing and writing-system questions are integrated into these files. Context and word order are not started as an independent feature. Domain and register coverage is edited-language sources plus constructed contrasts, not a corpus.

## Finding index

- [POR-001: Connectors da, de, do, das, dos and e can be name-internal or external, and spelling alone does not decide](findings/POR-001.md), draft; observation confidence medium; hypothesis untested.
- [POR-002: Preposition-article contractions and hyphenated enclitic or mesoclitic clitics create sub-token and hyphen boundaries that are not name boundaries](findings/POR-002.md), draft; medium; untested.
- [POR-003: Portuguese person names are sanctioned in several spellings, so accent and Unicode form must not define identity](findings/POR-003.md), draft; medium; untested.
- [POR-004: Registered names and everyday names diverge: Portuguese registration limits versus unofficial Brazilian apelidos](findings/POR-004.md), draft; low; untested.
- [POR-005: Titles and honorifics such as Sr., Dr., Dra., Dona, Seu and Dom have mixed casing status and need an explicit span policy](findings/POR-005.md), draft; medium; untested.
- [POR-006: Portuguese surnames and given names collide with common nouns, so capitalization and article cues carry the decision](findings/POR-006.md), draft; low; untested.

## Decision brief

Run connector role, contraction/clitic handling and normalization as separate experiments, and settle title policy first. See the [decision brief](decision-brief.md).

## Known gaps and reviewer needs

Need qualified review of pt-PT and pt-BR examples; the Brazilian statute on registered names could not be read from the official page; no source was found for hyphenated given names, pt-PT versus pt-BR clitic placement frequency, or name-specific noise behavior; Priberam entries were checked only for silva and rosa. The suggested Fernando versus Fernão contrast is unsupported and not used. The 2009 national implementation timeline of the Acordo is not verified from the text read. No corpus frequency or measured accuracy exists. [Sources](sources.md) record locators and limits.

## Research issues and revisions

No research issue exists; none was created. 2026-10-04: initial six-finding dossier with six topic syntheses and a decision brief, based on desk research; applied dossier-initialize, dossier-deep-research and dossier-document.
