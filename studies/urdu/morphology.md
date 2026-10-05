# Urdu: Postpositions and name-internal elements must be separated by evidence, not assumed

Scope: [dossier overview](overview.md). Status: source-limited desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

The question is which attached or following elements an Urdu PERSON model must treat as outside the name: postpositions (`نے`, `کو`, `کا/کی/کے`, `سے`, `میں`, `پر`), and which belong inside it (`عبد`-compounds with `ال`, honorific parts). An Urdu NER paper hypothesizes that the following postposition decides the preceding entity, using "Ali nay" and "Muhammad Ali nay" as examples ([URD-S006](sources.md#urd-s006), introduction); a rule-based system strips name suffixes and relies on postpositions only as a late check ([URD-S005](sources.md#urd-s005), p. 2516). These agree that the postposition is context, not name. See [URD-006](findings/URD-006.md).

What is not established: this dossier did not read a grammar. Schmidt's reference grammar was seen only as a publisher description ([URD-S017](sources.md#urd-s017)), so statements that `کا/کی/کے` agree with the possessed noun, that masculine nouns have oblique forms before postpositions, or that izafat links words, are unverified author knowledge and carry no source weight here. [URD-S006](sources.md#urd-s006) calls Urdu agglutinative; that descriptor is not used to select any method.

## Contrasts that challenge the shortcut

Examples are **synthetic** with generic names, author self-check only.

| Original | Meaning | Question |
| --- | --- | --- |
| `عبدالرحمن نے کتاب پڑھی۔` | Abdul Rahman read the book. | Span stops before `نے`, includes the `ال` piece. |
| `عبدالرحمن کی کتاب` and `عبدالرحمن کے بھائی` | Abdul Rahman's book; Abdul Rahman's brother | Same name, different possessive form; the span should not change with `کی` versus `کے`. |
| `سردی نے ہمیں تنگ کیا۔` | The cold bothered us. | `نے` after a common noun: the cue is not name-specific ([URD-003](findings/URD-003.md)). |

## NER decision and falsifiable handoff

Test span stability across following postposition variants with the name held fixed, and over-triggering of any postposition feature on matched common nouns. Disposition: proposal for `ner-evidence`, then `ner-eval`; not yet requested. The immediate gap is a verified grammar: read the grammar's postposition and oblique chapters before any fixture design.

## Limits and next evidence

Verb morphology, light verbs, honorific verb forms, izafat and oblique name forms are unstudied. No frequency data. The "separate word" status of postpositions in common orthography should be confirmed against a grammar or treebank annotation guide.
