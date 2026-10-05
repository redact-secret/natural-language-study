# Korean: A plausible surname is not always an individual mention

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[KOR-006](findings/KOR-006.md) adds a source-backed lexical/grammatical contrast: NIKL [KOR-S007](sources.md#kor-s007) distinguishes respectful 씨 from a family/surname suffix. The key design consequence is that correct edge removal cannot replace classifying the referent.

[KOR-004](findings/KOR-004.md) is a morphological ambiguity with different annotation consequences. Keep those two causes separate in evaluation: one can change whether a PERSON exists, the other can change where an agreed PERSON ends.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `김 씨가 도착했다.` | Mr/Ms Kim arrived. | Constructed individual reading. |
| `김씨라는 성을 쓴다.` | [Someone] uses the surname Kim. | Surname mentioned as a name category; do not automatically tag its prefix as a person. |
| `김씨가 도착했다.` | Kim arrived under an intended informal reading. | Missing-space stress input; a spelling-only classifier should not decide the referent. |

## NER decision and falsifiable handoff

Test individual, metalinguistic and family/clan contexts while varying spacing independently. Keep collective-policy gaps visible. Reject a surname stripper if it improves individual edges but creates category-reference false positives.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Common-noun/name homographs beyond 씨, person/location collisions and discourse-dependent reference need source-reviewed samples. This dossier establishes one consequential ambiguity family, not a complete collision lexicon.
