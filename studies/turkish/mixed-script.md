# Turkish script mixing: Latin only, with diacritic loss and foreign names as the live cases

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis from summaries and abstracts; independent review pending. NER proposals remain untested.

## Research answer and basis

Scope is Latin script; Arabic-script Ottoman is out of scope. Within Latin script the relevant representation questions are the six diacritic letters and ASCII folding ([TUR-004](findings/TUR-004.md), [TUR-S007](sources.md#tur-s007), [TUR-S010](sources.md#tur-s010), abstracts only), dotted/dotless I and normalization ([TUR-003](findings/TUR-003.md)), and foreign names taking Turkish suffixes. The stemmer note that an internal apostrophe in foreign names such as `o'connor` is a hazard ([TUR-S012](sources.md#tur-s012)) is the only sourced foreign-name point; whether the TDK rule applies to non-Turkish names was not verified. Transliteration of Arabic or Persian-origin names and Ottoman versus modern spelling were not researched.

## Contrasts that challenge the shortcut

Examples are **synthetic** (invented, non-referential people, author-written, no native review) unless marked adapted from a cited source. They are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Caglar Gokce'ye yazdi.` | Çağlar wrote to Gökçe, ASCII-fied | Suffix cue survives, diacritics do not. |
| `Işıl` lowercased by default code | `işıl` | Representation, not language. |
| `O'Connor` in a Turkish sentence | fictional foreign name | Internal apostrophe versus suffix apostrophe. |

## NER decision and falsifiable handoff

Evaluate ASCII-fold and foreign-name-apostrophe slices separately from the main apostrophe slice. Disposition: proposal; [decision brief](decision-brief.md).

## Limits and next evidence

No foreign-name suffix source, no transliteration source, no Ottoman coverage; mixed-script coverage is partial.

