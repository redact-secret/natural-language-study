---
name: dossier-document
description: Write or reconcile canonical dossier findings, source records and concise downstream decision briefs from completed research without strengthening its claims.
---

# Dossier Document

Turn investigated claims into durable, concise research artifacts. This skill organizes verified research; it does not substitute for missing source investigation.

Read [dossier patterns](../../../conventions/dossier-files.md), [conventions](../../../CONVENTIONS.md), [schema guide](../../../schemas/README.md), and existing target files. Use English prose and original-language examples with translations unless the user explicitly requests otherwise.

## Canonical documents

- Keep each observation in one finding. Preserve IDs, append source IDs without reuse, and record materially changed claims in revision notes. Use the [finding template](../../../templates/finding.md) for new findings; replace all sample metadata.
- Separate observation confidence, finding review status and NER hypothesis outcome. `reviewed` requires documented review; `supported` needs linked evaluation. A checked link is not a checked hypothesis.
- Update overview questions, finding index, coverage and gaps to match the work actually completed. Do not claim script-mixing coverage from normalization alone.
- Put an actionable synthesis in a topic or `decision-brief.md` when several findings jointly answer a decision. Link canonical claims rather than repeating their full text.

## Decision brief requirements

State the immediate decision, its basis, what remains uncertain, and what would reverse it. A handoff should specify positive/negative contrast families, policy questions, held-fixed variables, comparison, relevant error categories and destination. Label proposed slices and annotation choices as proposals; do not create executable gold fixtures here.

Record one of: linked downstream work, ready-for-owner-review proposal, explicitly deferred work, or no-action with rationale. A complete proposal does not require publication or favorable model results. Do not silently create GitHub issues, comment, close epics, commit or push without user authorization for those actions.

## Verification and delivery

Run the repository validator using the [documented command](../../../schemas/README.md); check changed local links, source locators and Unicode examples. Resolve failures. Structural checks cannot verify linguistic correctness, so accurately state remaining review needs.

Finish with the concrete decisions and artifact entry points. Mention the material limitation beside the result; do not bury it under a file inventory. If requested research remains incomplete, continue `$dossier-deep-research` instead of polishing around the gap.

## Broad dossier delivery

Use the six core topic files required by [dossier patterns](../../../conventions/dossier-files.md) for broad language research. Each needs an answer, source-backed basis, concrete contrast, design/evaluation consequence and limits; do not fill it with a repeated introduction or just links. Keep new consequential claims in canonical findings. Reconcile overview coverage, decision brief and comparative handoffs. Report breadth, independent review and model evaluation separately.
