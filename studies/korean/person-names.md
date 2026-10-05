# Korean: Separate name form, title and romanized rendering

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[KOR-002](findings/KOR-002.md) covers article 48 spacing. [KOR-005](findings/KOR-005.md) records the NIKL romanization options and established-spelling exception ([KOR-S006](sources.md#kor-s006), provisions 4 and 7). Together they invalidate a single fixed visual template as a completeness claim.

A surname alone can refer to an individual in suitable context; treating it as PERSON still requires a referent decision. Respectful 씨 is outside the target name span, while surname-as-category reference needs classification review ([KOR-006](findings/KOR-006.md)).

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `김 교수에게 물었다.` | [Someone] asked Professor Kim. | Propose surname 김 under the intended individual reading; title is context. |
| `박 씨가 왔다.` | Mr/Ms Park came. | Spaced respectful form with following subject particle. |
| `Min Yong-ha가 왔다.` | Min Yong-ha came. | Constructed Latin rendering with attached Korean particle; preserve the internal hyphen. |

## NER decision and falsifiable handoff

Collect surname-only, full-name, title-bearing and romanized mentions, with ordinary noun/title controls. Test boundary coverage without requiring an assumed syllable count or recovering family/given-name fields.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Compound surnames, adopted names and non-Korean naming communities are not exhaustively sampled. Romanization resemblance cannot establish that two mentions denote the same individual.
