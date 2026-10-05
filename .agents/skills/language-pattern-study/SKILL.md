---
name: language-pattern-study
description: Compare a defined NER-relevant phenomenon across scoped language findings and derive testable shared capabilities with language-specific exceptions.
---

# Language Pattern Study

Compare the same phenomenon across languages to decide what might be shared. Do not treat this as generic typology or as authorization to implement a language profile.

Read [taxonomy](../../../taxonomy.md), [ownership contract](../../../conventions/research-purpose.md), the relevant dossier findings and prior [boundary comparison](../../../comparative/person-boundaries.md). Use `$dossier-deep-research` when a comparison cell lacks a defensible source.

## Comparison method

Choose a concrete axis such as attachment role, boundary visibility, source-coordinate preservation or person/common-noun ambiguity. For each language, retain variety/register, finding IDs, confidence, counterexample and unresolved annotation question. Absence of an investigated pattern is not evidence of linguistic absence.

Separate three layers:

- Observable operation: candidate must start/end inside a token, join tokens, or preserve representation.
- Linguistic cause: clitic, case particle, address suffix, internal surname component, etc.
- Downstream policy: whether the cause belongs in the target span and how ambiguity is adjudicated.

Shared operations can motivate experiments; unlike causes must not be collapsed into one affix list. Compare disconfirming cases before proposing shared profile fields. Prefer a capability requirement over an invented API until experiments justify an interface.

## Durable result

Write `comparative/<specific-topic>.md` linking canonical findings. Include a compact comparison, rejected shortcuts, testable candidate capabilities, a baseline/controlled comparison, falsification criteria and owner-specific handoffs. Record missing cells and source disagreements. Link the comparative epic when one exists.

When current implementation context was requested, cite only inspected code at a recorded revision and keep unmeasured behavior conditional. Do not infer release support from research, a profile enum or a tiny example set.

Run repository validation. Complete the requested analysis and local handoff documents; publishing issues/results or changing downstream code is a separate action requiring applicable user authorization.

## Compare the expanded dossier

When synthesizing a broad wave, include both boundary capability and person/non-person classification. Distinguish natural mixed writing, transliteration, canonical normalization and artificial confusable substitutions. Compare the same controlled operation across languages and retain language-specific negative cases; file count and shared typological labels do not establish a shared implementation.
