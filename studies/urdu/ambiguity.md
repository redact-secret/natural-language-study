# Urdu: Name/common-noun collisions need context because script gives no case cue

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested.

## Research answer and basis

Two Urdu NER papers list names that are also ordinary words: barkat and salamat ([URD-S005](sources.md#urd-s005), p. 2510), and Shan, Kamran, Fazal, Kiran, Aftab, Manzoor ([URD-S006](sources.md#urd-s006), section IV item 10). They attribute the difficulty to the absence of capitalization; dataset slides name the same cause ([URD-S007](sources.md#urd-s007), slide 7). One system fails on a case where title, designation, surname and postposition checks are all uninformative ([URD-S005](sources.md#urd-s005), p. 2516). The minimal pair "us per khuda ka fazal hai" versus "fazal aik laek talabilm hai" ([URD-S006](sources.md#urd-s006), section V) shows the same string as a common noun and a PERSON. See [URD-003](findings/URD-003.md).

## Contrasts that challenge the shortcut

Examples are **synthetic** unless marked attested; no qualified review.

| Original | Meaning | Question |
| --- | --- | --- |
| `گل نے خط لکھا۔` vs `باغ میں گل کھلا ہے۔` | Gul wrote a letter; a flower bloomed in the garden | Same string, name versus flower. |
| `امید نے دروازہ کھولا۔` vs `مجھے امید ہے` | Umeed opened the door; I hope | Name versus hope. |
| `سردی نے ہمیں تنگ کیا۔` | The cold bothered us | `نے` after a common noun, so the postposition is not sufficient. |

## NER decision and falsifiable handoff

Use matched minimal pairs with the string held fixed, and keep false positives on the common-noun reading separate from misses on the name reading. A gazetteer-only baseline should be expected to over-fire. Disposition: proposal for `ner-evidence`; deferred. Other candidates listed in the task (such as `نور`, `شمع`, `چاند`, `ساجد`) were not attested in any cited source and are not claimed; they remain candidate controls needing native-speaker review.

## Limits and next evidence

Person/place and person/organization collisions, and ambiguity prevalence, are not covered. Examples rely on author judgment of usage.
