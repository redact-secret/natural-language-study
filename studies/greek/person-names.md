# Greek: Name structure is given name plus inflecting surname, with genitive-form women's surnames

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

A secondary reference page describes the traditional pattern in which a woman's surname is the genitive of the family name (Yannatos to Yannatou), common patronymic-type suffixes (-opoulos, -idis), and naming-after-grandparents customs ([GRE-S009](sources.md#gre-s009)). Wiktionary gives Παπαδόπουλος from παπάδ(ες) plus -όπουλος with the feminine form Παπαδοπούλου ([GRE-S010](sources.md#gre-s010)). The canonical claim is [GRE-002](findings/GRE-002.md); inflection is in [GRE-001](findings/GRE-001.md). Consequences: the same string can be a masculine genitive or a feminine nominative surname, and surname suffixes cue names but common nouns can carry endings such as -ου.

## Contrasts that challenge the shortcut

| Original | Meaning | Question |
| --- | --- | --- |
| `Ο Γιώργος Παπαδόπουλος και η Μαρία Παπαδοπούλου` | George Papadopoulos and Maria Papadopoulou | Do not merge forms by string equality. |
| `Ιωαννίδης` versus `Ιωαννίδη` | Fictional surname, nominative and non-nominative | Ending -ης versus -η; author reading of the pattern, unsourced. |
| `Γιωργάκης` | Diminutive of a given name (author knowledge) | Diminutive and familiar forms inflect and may not appear in a name lexicon. |
| `Η Ελένη Παπαδοπούλου-Μαυρίδου` | Eleni Papadopoulou-Mavridou | Double-barreled surname in genitive form, hyphenated; practice not sourced. |

All synthetic, fictional people, author self-check only.

## NER decision and falsifiable handoff

Test suffix-based surname cues (-όπουλος, -ίδης) and feminine -ου forms against matched common nouns and non-Greek names, rather than assuming a closed shape. Falsified if suffix cues add false positives on place names or common nouns that offset gains. Destination: `ner-evidence` for contrast families, then `ner-eval`. No result exists.

## Limits and next evidence

The two sources are secondary and not independent. Missing: current registry or legal naming rules, regional (Cypriot, Pontic, Arvanitic-origin) naming variation, diaspora forms, double surnames, and attested corpus frequencies. Greek is not described here as a single naming community.
