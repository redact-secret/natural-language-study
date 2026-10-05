# Korean: Attached material needs role and scope, not a suffix blacklist

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Particle attachment permits an entity edge inside an eojeol; the spelling basis is [KOR-S001](sources.md#kor-s001), article 41. [KOR-001](findings/KOR-001.md) owns that finding. Name-forming 이 and subject-marker 이 need separate interpretation ([KOR-004](findings/KOR-004.md)).

Crucially, an external NIKL corpus and the target taxonomy disagree about including some name-forming suffixes. Use the explicit mapping in KOR-004. [KOR-006](findings/KOR-006.md) adds a different problem: 씨 can change the kind of referent, so edge trimming alone is insufficient.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `김민수에게도 편지를 보냈다.` | [Someone] also sent a letter to Kim Minsu. | Propose 김민수; the particle sequence is outside the name. |
| `영철이가 왔다.` | Yeongcheol came. | Separate morphological analysis from the target policy excluding informal suffix 이. |
| `책에도 이름이 있다.` | There is a name in the book too. | An attached particle on an ordinary noun does not establish PERSON. |

## NER decision and falsifiable handoff

Test particle sequences alongside ordinary nouns and name-final syllables. Compare role-aware context with longest-suffix stripping; score truncated names and ordinary-noun false positives. Freeze the target taxonomy before importing external annotations.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

The small suffix examples are not a complete grammar or productive suffix inventory. Phonological alternation, discourse particles and colloquial stacking need further attested data.
