# English: Recognize the surface name without requiring a two-part parser

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

W3C [ENG-S003](sources.md#eng-s003), Middle initials, Multiple family names and Mixing it up, documents name structures that exceed a first/last template. This supports testing flexible surface spans, not importing every described naming custom as an English rule. English carrier text can mention people from many naming communities.

[ENG-003](findings/ENG-003.md) owns initials/title boundaries. [ENG-005](findings/ENG-005.md) adds script eligibility. Honorifics are contextual clues; their exclusion from the target span does not mean discarding them before classification.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Dr. Nora E. Vale spoke.` | Nora E. Vale spoke, with a professional title. | Propose the name including E., not the title. |
| `Nora van Dalen spoke.` | A fictional person spoke. | Lowercase internal surname component challenges capitalized-token-only joining. |
| `Nora spoke.` | A fictional person referred to by given name spoke. | A valid mention need not expose all parts of a legal name. |

## NER decision and falsifiable handoff

Test complete surface spans with titles, initials, lowercase components and shortened mentions. Evaluate full-span recall against a two-capitalized-word baseline; do not require surname parsing as a prerequisite for PERSON recognition.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

These examples are constructed, not a naming-frequency survey. Generational suffix and postnominal boundaries must follow the evidence taxonomy recorded in the runtime audit.
