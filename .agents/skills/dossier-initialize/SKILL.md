---
name: dossier-initialize
description: Initialize or scope a language research dossier in natural-language-study; use for a new language or a deliberate scope check, not to reset existing research.
---

# Dossier Initialize

Establish a bounded research question and a navigable dossier. Run from the repository root; resolve root from `CONVENTIONS.md` and `studies/`, not a fixed personal path.

## Repository contract

Read [conventions](../../../CONVENTIONS.md), [dossier patterns](../../../conventions/dossier-files.md), [taxonomy](../../../taxonomy.md), and the target overview if it exists. Follow applicable AGENTS/graft instructions before source discovery.

## Scope and initialization

- Resolve language key, BCP 47 tags, script identifiers, variety, region, register, domain and entity type. Default to PERSON only when consistent with the request. Script, language and naming community are different dimensions.
- For an existing dossier, preserve IDs, findings, source records and issue URLs. Record the scope gap or next research question; do not regenerate its contents.
- For a new dossier, check all overview prefixes, allocate a unique prefix and create the smallest useful `overview.md`. Add `sources.md` when verified sources are available, not fabricated bibliography. Do not create empty topic inventories.
- Use concrete decisions to select questions: within-token boundary, cross-token name, surface ambiguity or representation fidelity. Broad grammar labels alone are not research questions.
- Mark uncovered dimensions honestly. Choose a source strategy and a falsifying contrast, including at least one non-name or alternate reading when relevant.

## Handoff and completion

Link the existing research issue from [research queue](../../../research/README.md) if applicable. New external issues/messages require user authorization; initialization itself does not grant it. Pass the bounded questions to `$dossier-deep-research` if research is requested in the same task. Do not stop at a scope plan when the user requested research too.

An initialized scope is not a reviewed finding. Before research files are submitted, use the [validation guide](../../../schemas/README.md). A new empty dossier may remain a draft while sources are gathered; do not weaken validation merely to mark it complete.

## Broad dossier requests

Distinguish initializing one question from completing a broad language dossier. For the latter, map all six core topic syntheses in [dossier patterns](../../../conventions/dossier-files.md) to concrete questions and source needs. Prioritize work, but do not silently reduce the requested breadth to the easiest boundary findings. Preserve the user's language list; examples of other languages do not expand it.
