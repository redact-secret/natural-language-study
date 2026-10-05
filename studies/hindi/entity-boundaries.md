# Hindi: Boundary policy must be declared per source because honorifics and titles are treated differently

Scope: [dossier overview](overview.md), Hindi, PERSON. Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Three layers sit outside or beside a Hindi name: case postpositions, honorific particles and titles, and punctuation. The spelling standard places postpositions outside names and joins them only to pronouns [HIN-S001](sources.md#hin-s001), section 3.2, and separates श्री and जी from names unless part of the name (section 3.5.3); [HIN-001](findings/HIN-001.md) and [HIN-002](findings/HIN-002.md) own these. Annotation designs differ: the IJCNLP shared-task slides separate person (NEP) from person-title (NETP) and describe maximal-entity manual annotation without nesting [HIN-S007](sources.md#hin-s007); the Roman tweet corpus puts ji inside the Per span [HIN-S008](sources.md#hin-s008), section 3.1; HiNER follows CoNLL-2003 and the sections read give no honorific rule [HIN-S005](sources.md#hin-s005), section 3. The danda boundary is covered in [HIN-004](findings/HIN-004.md).

HiNER's error analysis reports that boundary confusion between B-Person and I-Person is the second most common error type after missed entities [HIN-S005](sources.md#hin-s005), section 5, so boundary conventions matter for the number that gets reported.

## Contrasts that challenge the shortcut

"Exclude every honorific" fails for name-internal श्री and जी; "include every honorific" mismatches the IJCNLP-style separate title class. Examples are **synthetic** or adapted (fictional people).

| Original | Meaning | Question |
| --- | --- | --- |
| `श्री अजय वर्मा आए।` | Mr. Ajay Verma came. | Is श्री inside? Policy. |
| `श्रीकांत वर्मा आए।` | Shrikant Verma came. | श्री is part of the name; excluding it would damage it. |
| `सुनीता जी आईं।` | Sunita (respectful) came. | Include जी? Roman tweet corpus includes it. |

## NER decision and falsifiable handoff

Before importing any Hindi corpus, record its span policy for titles, honorifics and postpositions and map it explicitly to the target; score exact span under each declared policy. Disposition: local proposal; `ner-evidence` to decide policy. See the [decision brief](decision-brief.md).

## Limits and next evidence

Other titles (religious, military, royal), nested entities (the IJCNLP scheme marks nested NEs in system output) and organization names containing persons are not studied. Obtain the HiNER and IJCNLP guideline documents.
