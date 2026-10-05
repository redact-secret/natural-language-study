# Portuguese: contractions and clitics at the name edge

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Portuguese fuses prepositions with articles (do = de + o, no = em + o, pelo = por + o) and attaches pronouns to verbs, with a hyphen in enclisis and mesoclisis. UD analyzes these as multiword tokens ([POR-S003](sources.md#por-s003)); the Acordo's Base XVII prescribes the hyphen for enclisis and tmesis ([POR-S001](sources.md#por-s001)). Canonical claims: [POR-002](findings/POR-002.md) and [POR-001](findings/POR-001.md).

## Contrasts that challenge the shortcut

Examples are synthetic (fictional people) unless marked adapted. Author self-check only; no qualified language review. Research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `A casa da Maria` | Maria's house | da = de + a is external; the fused form carries the article. |
| `Maria da Silva` | fictional full name | da is inside the proposed name. |
| `Dá-lhe o livro, Rui.` | Give him/her the book, Rui. | Hyphen joins verb and pronoun, not name parts. |

## NER decision and falsifiable handoff

Treat contraction splitting as optional candidate exposure, and keep source offsets. A prediction: contraction-aware handling reduces left-edge errors only where the fused word is external. Failure: no change on matched pairs.

## Limits and next evidence

Morphology of surnames (gender and plural, for example dos Santos as family label) is not sourced here. Clitic placement differences between pt-PT and pt-BR were not verified. See the [decision brief](decision-brief.md).
