# Portuguese: registered names, everyday names and titles

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Portugal's registration rule caps a name at six grammatical words with at most two as the proper (given) name ([POR-S002](sources.md#por-s002)), so long chains with connectors are normal in registered pt-PT names. Everyday Brazilian reference also uses apelidos and ballot names outside the register ([POR-S011](sources.md#por-s011)). Titles and forms of address vary in casing ([POR-S001](sources.md#por-s001), [POR-S006](sources.md#por-s006)). See [POR-004](findings/POR-004.md) and [POR-005](findings/POR-005.md).

## Contrasts that challenge the shortcut

Examples are synthetic (fictional people) unless marked adapted. Author self-check only; no qualified language review. Research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Joana Maria Costa Ferreira Lopes` | fictional five-word name | full chain as one PERSON? |
| `Zé do Bar` | nickname-like | do Bar inside the mention? |
| `Dona Célia` versus `dona de casa` | Mrs Célia versus housewife | honorific versus common noun. |

## NER decision and falsifiable handoff

Do not cap span length at registration limits; test mononym and short-chain mentions. Decide title inclusion before annotation. Failure: apelido-style mentions behave no differently from chains.

## Limits and next evidence

Brazilian statute not read; no pt-PT style guide for titles; no hyphenated given-name source; plural/gendered surname practices and non-Lusophone name communities uncovered.
