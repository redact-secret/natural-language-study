# Urdu: Right-edge postposition cues and nested-versus-maximal policy decide span edges

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Right edges: a following postposition is used as a cue in Urdu NER ([URD-S006](sources.md#urd-s006)), but fails to distinguish names from common nouns when both take the same postposition ([URD-S005](sources.md#urd-s005), p. 2516). Left edges and inclusion: titles are a separate class in the IJCNLP-08 tag set ([URD-S005](sources.md#urd-s005), Table 1). Nesting: the IJCNLP-08 task required nested entities ([URD-S008](sources.md#urd-s008)); one paper using that corpus annotates maximal entities, so a person name inside "Quaid-e-Azam Library" is not tagged Person ([URD-S006](sources.md#urd-s006), section V). Name length: a rule capped at three words splits longer names ([URD-S005](sources.md#urd-s005), p. 2515). See [URD-006](findings/URD-006.md) and [URD-004](findings/URD-004.md).

## Contrasts that challenge the shortcut

Examples are **synthetic** unless marked attested; no qualified review.

| Original | Meaning | Question |
| --- | --- | --- |
| `عبدالرحمن کی کتاب` | Abdul Rahman's book | Stop before `کی`. |
| `عبدالرحمن لائبریری` | Abdul Rahman Library | Person inside a facility name: nested or maximal. |
| `کتاب پر لکھا نام` vs `احمد پر ہنسا` | Name written on the book; laughed at Ahmad | `پر` after a common noun versus after a name. |
| "Quaid-e-Azam Library" (attested, [URD-S006](sources.md#urd-s006)) | A named library | Maximal Location, inner name untagged. |

## NER decision and falsifiable handoff

Fix an annotation policy for titles and nested names before comparing datasets, since IJCNLP-08 and maximal-entity annotation differ. Test right-edge errors by following token type and nested-inner recall separately. Disposition: proposal for `ner-evidence` then `ner-eval`; deferred.

## Limits and next evidence

No izafat or honorific-suffix evidence; no attested edge cases beyond the cited papers; scores not compared. The IJCNLP-08 tag guidelines page was not read.
