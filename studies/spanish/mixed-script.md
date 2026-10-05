# Spanish: Script is Latin; the research question is diacritic fidelity and Unicode form

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

Spanish is written in Latin script, so there is no alternate-script requirement. The relevant dimension is orthography: capitals take the tilde when the accent rules call for it ([SPA-S004](sources.md#spa-s004), excerpt only), and Unicode treats precomposed and combining forms as canonically equivalent ([SPA-S012](sources.md#spa-s012)). Finding: [SPA-005](findings/SPA-005.md). Accent loss in noisy text (`García` to `Garcia`) is a lossy transformation distinct from NFC/NFD equivalence. Code-switching with English or other languages, and Catalan, Galician or Basque names in Spanish text, are not researched. Name transliteration from non-Latin scripts into Spanish is out of scope.

## Contrasts that challenge the shortcut

Examples are **synthetic** (authored for this study, fictional people, repository MIT terms) unless marked otherwise. Translations and proposed readings have author self-check only. They are research illustrations, not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Garcia` (accents removed) | Garcia | Accent-folded form; separate from NFD. |
| `García` in NFD (a plus U+0301) | García | Canonical equivalent of the NFC form. |
| `Núñez` / `Nunez` | Núñez / Nunez | Tilde or accent variants; not pooled as one identity. |

## NER decision and falsifiable handoff

Report NFC/NFD and accent-loss slices separately; keep original offsets. Destination: `ner-evidence`, `ner-eval`. Untested.

## Limits and next evidence

No attested noisy-text corpus was used. Code-switching, social-media orthography and OCR errors are gaps.
