# Hindi: Postpositions are mostly outside names; pronoun fusion and oblique forms need separate tests

Scope: [dossier overview](overview.md), Hindi only. Status: source-backed desk synthesis; independent review pending. NER proposals remain untested. No claim about other Indian languages.

## Research answer and basis

In the standard written norm, case postpositions (ने, को, से, में, पर, का, की, के) follow names as separate words, while pronouns take them as part of the same word (उसने, मुझको); with two postpositions, the first is fused to a pronoun and the second is separate [HIN-S001](sources.md#hin-s001), section 3.2. [HIN-001](findings/HIN-001.md) owns the finding. The ergative ने after a name (`राजेश शर्मा ने`) is therefore an external word in edited text, which is a different attachment profile from languages that attach case to the noun. That contrast is a statement about what is documented for Hindi, not a claim about Marathi, Bengali or any other language, which this dossier did not examine.

## Contrasts that challenge the shortcut

The shortcut "strip ने/को/से from the end of the token" fails twice: on pronouns it splits a word that has no name in it, and in noisy text where the space is omitted it may be right but only for names. Examples are **synthetic** (fictional people, repository MIT license, author self-check only).

| Original | Meaning | Question |
| --- | --- | --- |
| `राजेश शर्मा ने खाना खाया।` | Rajesh Sharma ate. | Propose राजेश शर्मा; ने is outside. |
| `उसने खाना खाया।` | He/she ate. | ने fused to a pronoun; no name. |
| `उसके लिए` | for him/her | Postposition fused, then separate (adapted from the standard). |

## Leads not supported by a source in this dossier

The following are linguistic leads from the author's background knowledge, **not** sourced here, and need a grammar reference and a Hindi reviewer before being cited: (1) many masculine nouns ending in -आ take an -ए oblique form before postpositions, so a nickname such as a synthetic मुन्ना could surface as `मुन्ने को`, which would change the final character of a name before a postposition; (2) names ending in -आ that are not inflected, and names in -ई/-ऊ/-ा that may not change; (3) the vocative (for example a spoken `राम!` or `रामा`) and gender endings. These generate a testable slice, not a finding. Whether proper names follow common-noun inflection should be checked against a grammar.

## NER decision and falsifiable handoff

Test separate-word postposition behavior and pronoun-fusion controls first; test the oblique-form lead only after sourcing. Compare whitespace candidates with a suffix guard and score name boundaries, pronoun false positives and oblique-form misses separately. Disposition: local proposal for `ner-evidence` review, then `ner-eval`; `fastner` experiment only if warranted. See the [decision brief](decision-brief.md); no downstream adoption or benchmark result is claimed.

## Limits and next evidence

Spacing rules are prescriptive. The HDTB page was a fetch summary. No Hindi grammar was read, so inflection and agreement are open. Next: acquire Kachru (2006) or McGregor (1977), or another verified grammar, and verify the oblique and vocative claims. Do not infer behavior of Urdu or Marathi.
