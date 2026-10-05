# Spanish: Names have two surnames, optional connectors and context-dependent particle case

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

Spanish registers allow `de`, `y` or `i` between surnames and let parents agree on the order of their surnames ([SPA-S006](sources.md#spa-s006)); Argentine law permits a spouse's surname with or without `de` ([SPA-S007](sources.md#spa-s007)). RAE guidance reportedly lowercases `de`, `del` and `de la` after a given name and capitalizes them when the given name is dropped ([SPA-S001](sources.md#spa-s001), [SPA-S002](sources.md#spa-s002)). Findings: [SPA-001](findings/SPA-001.md), [SPA-002](findings/SPA-002.md). Compound given names (`José Luis`) and the position of the given-name boundary were not sourced beyond example construction. Contrast with [French](../french/person-names.md), where the particle-case guidance of two authorities disagrees; no such disagreement was found for Spanish.

## Contrasts that challenge the shortcut

Examples are **synthetic** (authored for this study, fictional people, repository MIT terms) unless marked otherwise. Translations and proposed readings have author self-check only. They are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `José Luis Ortega Salas` | José Luis Ortega Salas | Four tokens; where does the given name end? |
| `María Pérez de Gómez` | María Pérez de Gómez | Connector versus marital `de`. |
| `Lucía Marín y Hugo Soto` | Lucía Marín and Hugo Soto | Coordination of two people, not one name. |

## NER decision and falsifiable handoff

Do not hard-code one given name plus one or two surnames. Test a contextual connector rule against coordination negatives. Mexican and other Latin American conventions are not researched; do not extend es-ES or es-AR statements to them. Destination: `ner-evidence`, `ner-eval`. Untested.

## Limits and next evidence

Legal texts show permission, not usage. Need Mexican and other civil-registry sources, plus attested usage with reuse rights.
