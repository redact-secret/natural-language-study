# PERSON boundary comparison: four-language first wave

The research motivates **candidate spans that can end within a tokenizer unit or cross multiple units**. This is an engineering hypothesis, not a selected architecture or a measured improvement. Every finding below remains draft and untested.

A deeper [pattern study](boundary-roles-and-candidate-capabilities.md) now incorporates source disagreement, the Korean source/target annotation mismatch and observed tokenizer behavior. Use that study and the language decision briefs for current priorities.

## Comparable observations

| Scoped dossier | Boundary pressure | Counterexample that prevents a global rule |
| --- | --- | --- |
| English | Attached possessive/auxiliary; name-internal apostrophe and initials ([ENG-001](../studies/english/findings/ENG-001.md), [ENG-003](../studies/english/findings/ENG-003.md)). | Splitting all apostrophes damages O’Neil; a possessive common noun is not a person. |
| Korean | Attached particle chains and sometimes internal name spacing ([KOR-001](../studies/korean/findings/KOR-001.md), [KOR-002](../studies/korean/findings/KOR-002.md)). | A particle-bearing common noun is not a name; standard spacing exceptions are narrowly scoped. |
| Japanese | Ordinary unspaced text, analyzer units and address suffixes ([JPN-001](../studies/japanese/findings/JPN-001.md), [JPN-002](../studies/japanese/findings/JPN-002.md)). | One analyzer token need not equal a name; さん endings alone are insufficient. |
| French | External elision versus internal surname particle; compound name punctuation ([FRA-001](../studies/french/findings/FRA-001.md), [FRA-002](../studies/french/findings/FRA-002.md)). | Removing d’ globally truncates surnames; retaining it globally adds external prepositions. |

## Candidate shared capabilities

1. **Role-sensitive boundaries:** preserve raw text and score candidate boundaries using context. Test name-internal and grammatical attachments separately; do not unify Korean case particles and French surname particles as one linguistic category.
2. **Token-independent spans:** compare candidates within/across token units with the existing baseline. Tokenizer interfaces and allowable offsets remain `fastner`/`ner-eval` decisions.
3. **Optional orthographic cues:** casing and script transitions are soft hypotheses, with name/common-noun controls ([ENG-002](../studies/english/findings/ENG-002.md), [JPN-003](../studies/japanese/findings/JPN-003.md)). A Latin baseline does not establish Japanese behavior.
4. **Normalization with traceability:** distinguish NFC/NFD equivalence from width folding, accent deletion and transliteration. Preserve original coordinates ([KOR-003](../studies/korean/findings/KOR-003.md), [FRA-003](../studies/french/findings/FRA-003.md)).

## Smallest useful downstream experiment

First resolve named-span policy with `ner-evidence`: titles, surname-only mentions, attached grammar and ambiguous cases. Build matched positive/negative contrast families from reviewed findings. Keep evidence, model/data version and scorer fixed; change one candidate mechanism at a time. `ner-eval` should report exact-span errors plus precision/recall and denominators by attachment role, token crossing, casing/script and normalization, using its existing contracts.

Any quality gain must be checked against hard-negative errors and runtime/memory cost in `fastner`. Lack of improvement, poor generalization or worse false positives can reject the proposed abstraction. `fastner-benchmarks` receives actual results, not a typological support label. No numerical success threshold is invented by this research.

## Limits and next decision

Four languages do not represent global diversity. Synthetic contrasts identify questions, not frequencies or coverage. Concrete owner-review packets are now available in each dossier; adoption and execution remain pending review and applicable policy decisions. Review [the first-wave epics](../research/README.md), then test before proposing concrete `LanguageProfile` fields.
