# Korean: Whitespace units are too coarse; syllable units still need joining

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

[KOR-001](findings/KOR-001.md) establishes the need to inspect within eojeol boundaries. [KOR-002](findings/KOR-002.md), based on spelling article 48, separates name spacing from title spacing; permitted name-spacing exceptions do not make all whitespace optional.

The pinned [runtime audit](../../research/runtime-boundary-audit.md) found Hangul syllable units. That exposes many possible edges, but the Korean statistical candidate path has a four-unit limit and no GAP joining at the inspected revision. Those are backend-specific constraints, not universal FastNER behavior.

## Contrasts that challenge the shortcut

Examples are **synthetic** unless explicitly marked adapted. Codex-authored original examples use fictional people and repository MIT terms; source material retains its rights. Translations and proposed readings have author self-check only, not qualified review. These are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `김민수는 왔다.` | Kim Minsu came. | Whitespace-only tokenization would include 는 in the unit containing the name. |
| `김 교수는 왔다.` | Professor Kim came. | Do not merge the title merely because it is adjacent. |
| `남궁 민수는 왔다.` | Namgung Minsu came, with deliberate surname/given-name separation. | Constructed spacing contrast; review applicability of the ambiguity exception before fixture adoption. |

## NER decision and falsifiable handoff

Probe candidate reachability for joined names, reviewed spaced names, titles and longer names before retraining. Compare boundary coverage per backend. Do not infer that syllable tokenization by itself yields correct PERSON classification.

Disposition: local proposal for `ner-evidence` review, then `ner-eval` measurement and a `fastner` experiment if warranted. The [decision brief](decision-brief.md) sets the order; no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Whitespace deletion is a robustness transformation, not a sanctioned orthographic rule. The audit does not test all runtimes, nor establish how often candidate length limits matter.
