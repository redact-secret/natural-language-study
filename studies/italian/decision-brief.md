# Italian: decision brief and downstream proposal

**Decision: treat external elision and articulated prepositions, name-internal particles and encoding variants as three separate experiments, and do not use particle case or UD word splitting as a membership rule.** Scope: [dossier overview](overview.md). This is draft desk research and a proposal for owner review; NER outcomes are untested.

## Basis

[ITA-001](findings/ITA-001.md): the same `dell'` shape is external in one context and name-internal in another. [ITA-002](findings/ITA-002.md): Crusca describes lowercase `da` in da Vinci and a capitalized fused particle in D'Eredità. [ITA-003](findings/ITA-003.md): titles and surname-first order are register matters. [ITA-004](findings/ITA-004.md): normalization-safe variants versus distinct spellings. [ITA-005](findings/ITA-005.md): homographs. [ITA-006](findings/ITA-006.md): multi-component names.

## Contrast families proposed to ner-evidence

Families, not fixtures; add reviewed names and registers, keep original text and finding ID.

| Family | Source finding | Controlled comparison |
| --- | --- | --- |
| Elision role | ITA-001 | dell'Anna versus Dell'Orso versus dell'orso, contexts matched |
| Particle case | ITA-002 | De/de, Di/di, Della, da; ALL-CAPS |
| Titles and order | ITA-003 | Dott.ssa, Sig.ra, Avv., surname-first |
| Encoding | ITA-004 | NFC/NFD, U+0027/U+2019; Niccolò versus Nicolò kept distinct |
| Homographs | ITA-005 | Rosa, Conte, Re, Romano, matched common-noun readings |
| Multi-component names | ITA-006 | two or three given names, double surnames, two-person conjunctions |

## Policy questions before annotation

Are titles inside a PERSON span? Is an internal particle always included? How are surname-first lists marked? Are fictional or antonomastic uses PERSON? This dossier decides none of them.

## Experiment proposal for ner-eval and fastner

Hold the name inventory, split, annotation policy and model fixed; change one factor per slice. Report omission of internal particles and inclusion of external function words separately, with denominators and boundary error types, and list unresolved cases apart. For tokenization changes, measure candidate reachability before span accuracy. No threshold is defined.

## Rejected shortcuts and reversal condition

Reject stripping every apostrophe prefix, requiring a capital for a particle, folding accents into identity and merging Niccolò with Nicolò. Reopen if a fixed rule matches the contextual approach on matched negatives.

## Handoff disposition

- `ner-evidence`: ready for owner review after Italian-language review of examples.
- `ner-eval`: slice names proposed (`ita-elision-role`, `ita-particle-case`, `ita-title-order`, `ita-encoding-variants`, `ita-homograph-readings`, `ita-multi-component`); not run.
- `fastner`: options only; downstream code not inspected or changed.
- `fastner-benchmarks`: deferred until evaluated artifacts exist.

## Review and provenance

2026-10-04: produced from source checks through a fetch tool that condenses pages; limitations are in [sources](sources.md). No independent language review is recorded.
