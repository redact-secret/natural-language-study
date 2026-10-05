# Greek: Case endings and accent shifts make the surface mention differ from the lemma

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

Greek names decline. UD Greek documents four cases ([GRE-S001](sources.md#gre-s001)); a grammar overview gives masculine -ος nouns as -ος / -ου / -ο / -ε with stress that can move forward in the genitive ([GRE-S008](sources.md#gre-s008)); Wiktionary lists Γιώργος, Γιώργου, Γιώργο and Παπαδόπουλος with genitive variants Παπαδόπουλου and Παπαδοπούλου ([GRE-S010](sources.md#gre-s010)). See [GRE-001](findings/GRE-001.md) for the case-form claim and [GRE-002](findings/GRE-002.md) for the feminine surname that is genitive in form. The practical answer is that a mention such as `Γιώργου` or `Νίκο` is a legitimate PERSON surface form that differs from the nominative lexicon entry, and the accusative `Νίκο` is shorter than the lemma `Νίκος`.

## Contrasts that challenge the shortcut

Examples are **synthetic** (fictional people, repository MIT terms) with author self-check only; they are not gold fixtures.

| Original | Meaning | Question |
| --- | --- | --- |
| `Είδα τον Νίκο.` | I saw Nikos. | Accusative shorter than the lemma; is stem-based lookup needed? |
| `Η Μαρία Μαυρίδου μίλησε.` | Maria Mavridou spoke. | Feminine surname in `-ου`; reading it as a genitive modifier would drop it from the span. |
| `Το σπίτι του ανθρώπου.` | The person's house. | Common noun with the same `-ου`; ending alone does not mark a name. |
| `Ο Τζον ήρθε.` | John came. | Foreign-origin name without Greek endings; inflection is not universal. |

## NER decision and falsifiable handoff

Compare nominative-only lexicon lookup with stem-plus-ending families and character n-gram features on held-out inflected mentions, holding the name inventory fixed. Falsified if the baseline matches the stem-aware condition or false positives on common nouns offset the gain. Disposition: proposal for `ner-evidence` review; `ner-eval` and `fastner` deferred. No downstream result exists.

## Limits and next evidence

Name-specific forms rest on secondary and community pages; the Holton et al. and Triantafyllidis grammars were not read ([sources](sources.md)). Vocative -ε versus -ο for names is unsettled. Missing: plural and diminutive names, Cypriot forms, dialect forms, and corpus counts of case distribution in person mentions.
