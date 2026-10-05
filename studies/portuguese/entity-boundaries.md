# Portuguese: connector, title and clitic inclusion proposals

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[POR-001](findings/POR-001.md) shows lowercase connectors inside capitalized names (examples in the Acordo, [POR-S001](sources.md#por-s001); flat:name in [POR-S004](sources.md#por-s004)). [POR-005](findings/POR-005.md) shows titles and honorifics with mixed casing. [POR-002](findings/POR-002.md) shows that hyphens and contractions at the edge belong to other structures. Proposal, not adopted policy: include internal connectors, exclude Sr./Dr./Dra. and lowercase titles, decide Dona/Seu explicitly, exclude external fused prepositions.

## Contrasts that challenge the shortcut

Examples are synthetic (fictional people) unless marked adapted. Author self-check only; no qualified language review. Research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Maria da Silva` | fictional name | include da. |
| `a casa da Maria` | Maria's house | exclude da. |
| `Ana Souza e Silva` versus `Ana Souza e Rui Silva` | one person versus two | e inside versus coordination. |
| `Dra. Helena Matos` | Dr Helena Matos | title outside. |

## NER decision and falsifiable handoff

Hold annotation policy fixed and vary role. Error categories: lost internal connector, added external connector, title absorbed. Failure: errors indistinguishable across roles.

## Limits and next evidence

Policy gold belongs downstream. The Acordo gives no rule for particles inside surnames; behavior rests on examples and a treebank. No reviewer.
