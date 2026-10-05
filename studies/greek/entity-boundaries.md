# Greek: Articles, fused prepositions and titles are external cues unless a policy says otherwise

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

The definite article regularly precedes a proper name in Greek, with the example Ο Αλέξανδρος ήρθε χθες ([GRE-S008](sources.md#gre-s008)); σε plus article fuses (στον) and is split by UD into syntactic words ([GRE-S001](sources.md#gre-s001)). Abbreviations such as χλμ. are single UD words with punctuation. The canonical claim is [GRE-003](findings/GRE-003.md): the article, fused preposition and abbreviated title sit next to the name and carry its case, so they are best studied as boundary and cue features rather than span members. This is a proposal for policy, not a source finding about gold spans.

## Contrasts that challenge the shortcut

| Original | Meaning | Question |
| --- | --- | --- |
| `Ο Γιώργος Μαυρίδης` | George Mavridis | Article outside the name. |
| `κ. Μαυρίδης` | Mr Mavridis | Title outside the name; the period belongs to the title. |
| `Ο Μαύρος έφυγε.` | The black one left. | Article plus adjective; no name. |
| `Γιώργο, έλα.` | George, come. | Vocative comma outside the span. |
| `Ο Πρωθυπουργός Μαυρίδης` | The Prime Minister Mavridis (synthetic title) | Role noun with capital: part of the span or a title? A policy question. |

All synthetic, fictional, author self-check only.

## NER decision and falsifiable handoff

Fix a policy for articles, fused forms, abbreviated and role titles, then compare article-as-feature with article-in-span on one name inventory. Falsified if an adopted policy requires article inclusion or if no boundary change appears. Destination: `ner-evidence` policy review first. No result exists.

## Limits and next evidence

No Greek annotation guideline was read for title or article policy; the UD GDT has PROPN but no NER spans ([GRE-S002](sources.md#gre-s002)). Missing: role-title conventions, quoted names, nicknames, patronymic with father's name in genitive (a naming practice not researched here).
