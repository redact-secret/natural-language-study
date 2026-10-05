# French: Particles and compound components belong to observed spelling

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[FRA-001](findings/FRA-001.md) and [FRA-003](findings/FRA-003.md) motivate multi-component names. [FRA-004](findings/FRA-004.md) preserves an actual disagreement between OQLF and Canadian federal editorial guidance on du/des capitalization. It must not be simplified to a France-versus-Québec split.

For recognition, the key consequence is to avoid mandatory uppercase at every name component. A lowercase particle may be internal, but the same written form outside a name does not inherit that status.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Anne-Claire du Val est arrivée.` | Anne-Claire du Val arrived. | Constructed compound given name and lowercase surname particle. |
| `Anne-Claire Du Val est arrivée.` | Anne-Claire Du Val arrived. | Constructed casing contrast, not a claim that this is the same person’s authorized spelling. |
| `Mme Anne-Claire Évrard est arrivée.` | Ms Évrard arrived. | Title can support classification; proposed exclusion needs French policy review. |

## NER decision and falsifiable handoff

Test internal particles, compound names and title contexts without rewriting personal spelling to one editorial standard. Match negatives containing ordinary de/du/des phrases. Judge exact observed spans, not reconstructed canonical names.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Name spelling can be individual-specific. Titles and fictional-person scope require a French evidence policy; recommendations here do not silently inherit English gold rules.
