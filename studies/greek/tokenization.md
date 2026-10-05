# Greek: Whitespace tokens are mostly name-safe, but fused preposition-article forms and abbreviations need explicit policy

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

Greek separates words with spaces, so a full name is normally several whitespace tokens with an article before it. UD Greek says words are separated by whitespace or punctuation with exceptions, treats σε plus a definite article as a multiword token split into syntactic words (στον = σ + τον), and treats abbreviations as single words that may contain punctuation (χλμ., π.Χ.) ([GRE-S001](sources.md#gre-s001)). The GDT treebank reports 1,668 multiword tokens among 61,673 tokens and about 10% of tokens without a trailing space ([GRE-S002](sources.md#gre-s002), as reported by a summary). The boundary consequences for names are in [GRE-003](findings/GRE-003.md). UD syntactic words are not PERSON spans, so a split such as σ + τον is a treebank convention, not evidence about entity edges.

## Contrasts that challenge the shortcut

| Original | Meaning | Question |
| --- | --- | --- |
| `Μίλησα στον Γιώργο.` | I spoke to George. | `στον` is one orthographic token before the name; keep it outside. |
| `κ. Μαυρίδης` | Mr Mavridis | Title abbreviation with a period; sentence splitters may treat the period as a boundary. |
| `Γιώργο-Νίκο` hyphen coordination | George-Nikos (compound written with hyphen; synthetic and unsourced as usage) | Hyphen between two names: one entity or two? Not researched. |
| `Μίλησα απ' τον Γιώργο.` | I spoke from (colloquial) George. | Apostrophe with U+0027 is attached to a function word, not to the name; apostrophe handling is not covered by the sources read. |

All synthetic, author self-check only.

## NER decision and falsifiable handoff

Test whether whitespace tokenization with preserved punctuation suffices for Greek name boundaries, and separately whether UD-style splitting of fused forms changes span agreement. Hold annotation policy fixed. Falsified if the split changes no boundary or if it adds name-truncation errors. Destination: `ner-evidence` then `ner-eval`; `fastner` only if warranted. No result exists.

## Limits and next evidence

The UD tokenization page could not be fetched (HTTP 404); the elision and hyphen cases are unsourced. Missing: corpus counts for apostrophe-elided prepositions near names, sentence-splitting behavior after abbreviated titles, and web or social text tokenization.
