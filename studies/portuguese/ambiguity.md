# Portuguese: person versus common noun

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Priberam shows rosa as noun, colour, adjective and verb form, and silva as a noun and a verb form ([POR-S009](sources.md#por-s009)). The Acordo requires capitals for anthroponyms ([POR-S001](sources.md#por-s001)), so capitals discriminate in edited mid-sentence text. Canonical claim: [POR-006](findings/POR-006.md). Seu and Dona add possessive and common-noun readings ([POR-005](findings/POR-005.md)).

## Contrasts that challenge the shortcut

Examples are synthetic (fictional people) unless marked adapted. Author self-check only; no qualified language review. Research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `A Rosa chegou.` / `A rosa chegou.` | Rosa arrived / the rose arrived | capital decides in edited text. |
| `Rosa é minha tia.` / `Rosa é minha cor.` | person / colour | sentence-initial capital does not decide. |
| `Falei com o Costa.` / `pela costa` | person / coast | article cue. |

## NER decision and falsifiable handoff

Use matched templates under mixed, lowercase and uppercase conditions. Pereira, Costa, Barros, Ribeiro, Flor, Estrela, Santos and Dom are hypotheses only. Failure: capital alone suffices across conditions.

## Limits and next evidence

Only silva and rosa were checked. No frequency data; person/place/organization ambiguity beyond examples is not studied.
