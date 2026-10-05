# Spanish: Word-token conventions do not define name boundaries

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

Spanish uses space-separated words, so a name usually spans several tokens. UD treats contractions and enclitics as multiword tokens, keeps abbreviations like `etc.` as one token with its period, and separates other punctuation ([SPA-S008](sources.md#spa-s008)). Names lacking internal structure may be annotated with a flat relation ([SPA-S011](sources.md#spa-s011)). The AnCora and GSD pages report thousands of multiword tokens ([SPA-S009](sources.md#spa-s009), [SPA-S010](sources.md#spa-s010)). CoNLL-2002 marks only the top-level entity when entities nest ([SPA-S013](sources.md#spa-s013)). None of these defines a PERSON span for the compound-surname connectors in [SPA-001](findings/SPA-001.md). Inverted punctuation (`¿`, `¡`) is a Spanish-specific adjacency issue but no source on it was verified here (see [SPA-005](findings/SPA-005.md) example-05).

## Contrasts that challenge the shortcut

Examples are **synthetic** (authored for this study, fictional people, repository MIT terms) unless marked otherwise. Translations and proposed readings have author self-check only. They are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `¡Lucía!` | Lucía! | Opening mark attaches to the token; the name boundary excludes it. |
| `Sr. Marín` | Mr Marín | Title abbreviation with period; period belongs to the abbreviation. |
| `Lucía Marín y Soto` | Lucía Marín y Soto | Connector inside a name span; the whitespace tokenizer sees three surname-region tokens. |

## NER decision and falsifiable handoff

Decide whether the system's tokens are orthographic words, UD syntactic words or subword pieces, and map spans back to original offsets. Compare span recovery for connector names across token conventions. Destination: `ner-evidence`, `ner-eval`. Untested.

## Limits and next evidence

Treebank pages were read as summaries. No tokenizer was run for this dossier. Social-media tokenization (hashtags, handles, abbreviated names) is not covered.
