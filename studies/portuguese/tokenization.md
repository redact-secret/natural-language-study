# Portuguese: token units, hyphens and Unicode forms

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

UD Portuguese treats contractions as multiword tokens and says hyphenated words are handled inconsistently ([POR-S003](sources.md#por-s003)); UD also notes many multiword proper nouns are not split ([POR-S005](sources.md#por-s005)). These are syntactic word units, not PERSON spans. The same visible sequence can therefore be one entity token run or several syntactic words. See [POR-002](findings/POR-002.md) and [POR-003](findings/POR-003.md).

## Contrasts that challenge the shortcut

Examples are synthetic (fictional people) unless marked adapted. Author self-check only; no qualified language review. Research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Joana dos Santos` | fictional full name | dos has a space on both sides but is name-internal. |
| `Entregar-lhe-ei` | I will hand him/her | one orthographic token, three UD words, no name. |
| `João` (a + U+0303) | João | one visible letter, two code points. |

## NER decision and falsifiable handoff

Compare raw whitespace tokens, UD-style splits and role-aware units under a constant offset contract. Prediction: no single splitter is best for both contractions and hyphenated names. Failure: one splitter wins everywhere.

## Limits and next evidence

No Portuguese tokenizer was run. No treebank data was read directly; only documentation pages. The apostrophe is not a major Portuguese name feature in the sources read, and no claim is made.
