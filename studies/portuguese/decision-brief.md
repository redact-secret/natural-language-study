# Portuguese: decision brief and downstream proposal

**Decision: Separate connector role, contraction/clitic handling, Unicode and accent handling, and title policy into distinct experiments.** Scope is the [dossier scope](overview.md). This is desk research and a proposal for owner review; examples are draft and NER outcomes are untested.

## Basis

- [POR-001](findings/POR-001.md): connectors inside names versus external; spelling alone does not decide.
- [POR-002](findings/POR-002.md): contractions and clitic hyphens are other structures.
- [POR-003](findings/POR-003.md): several sanctioned spellings; NFC/NFD is not accent deletion.
- [POR-004](findings/POR-004.md), [POR-005](findings/POR-005.md): name forms and titles need explicit policy.
- [POR-006](findings/POR-006.md): name/noun collisions.

## Evidence packet proposed to ner-evidence

Contrast families, not fixtures.

| Family | Source finding | Controlled comparison |
| --- | --- | --- |
| Internal versus external connectors | POR-001 | role-aware versus capitalization-run versus always-drop |
| Contractions and clitics | POR-002 | raw versus UD-style versus role-aware units |
| Spelling and Unicode | POR-003 | NFC lookup versus accent-folded fallback |
| Name forms and titles | POR-004, POR-005 | title-in versus title-out, mononym versus chain |
| Name versus noun | POR-006 | mixed, lower, upper case matched pairs |

## Policy decisions before gold annotation

Decide title inclusion (Sr., Dr., Dra., Dona, Seu, Dom), internal connector inclusion, and treatment of apelidos. Preserve registered spelling.

## Experiment proposed to ner-eval and fastner

Hold evidence, split, policy, normalization contract and model fixed except the manipulated factor. Report exact-span precision/recall, false positives on hard negatives and boundary error types by family. No threshold is defined here.

## Uncertainty and reversal

Reopen if role-aware handling does not reduce connector errors, or if accent folding does not raise false matches. Unverified: Brazilian statute text, pt-PT versus pt-BR clitic placement, hyphenated given names, 2009 timeline.

## Handoff disposition

- `ner-evidence`: ready for owner review, after language review and policy decision.
- `ner-eval`: question specified; execution pending evidence.
- `fastner`: options specified; no code inspected or changed.
- `fastner-benchmarks`: deferred until evaluated artifacts exist.

## Review and provenance

2026-10-04: desk research via dossier-initialize, dossier-deep-research and dossier-document. Author checks only; no independent language review. No GitHub issue created. See [sources](sources.md).
