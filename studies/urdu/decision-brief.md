# Urdu: decision brief and downstream proposal

**Decision: Before building Urdu PERSON evidence, settle three representation and policy choices: whether candidates may cross or start inside whitespace tokens, whether Urdu-letter and Arabic-letter code point variants are matched, and whether titles and nested names are inside spans.** Scope is the [dossier overview](overview.md): Urdu in Pakistan only, with no claim about other Pakistani languages. This is desk research and a proposal for owner review; examples are draft and NER outcomes are untested.

## Basis

- [URD-002](findings/URD-002.md): space omission and insertion make whitespace unreliable ([URD-S004](sources.md#urd-s004)).
- [URD-001](findings/URD-001.md): NFKC does not unify Farsi yeh/Arabic yeh, keheh/kaf, or heh goal/Arabic heh (local check).
- [URD-003](findings/URD-003.md): no letter case, so name/common-noun pairs rely on context.
- [URD-004](findings/URD-004.md) and [URD-006](findings/URD-006.md): name structure, titles and nesting policy differ across sources.
- [URD-005](findings/URD-005.md): Latin, Roman Urdu and Devanagari renderings vary and are not identity.

## Evidence packet proposed to ner-evidence

Contrast families, not fixtures; expand with independently reviewed names.

| Family | Source finding | Controlled comparison |
| --- | --- | --- |
| Spacing and ZWNJ | URD-002 | Same fictional name with no space, space, ZWNJ (U+200C) |
| Code point variants | URD-001 | Farsi/Arabic yeh, keheh/kaf, heh variants; precomposed versus decomposed hamza; U+06BE deletion as hard negative |
| Name/common-noun pairs | URD-003 | Fixed string, varied context; common noun plus `نے` as negative |
| Name structure and titles | URD-004 | Mononym to four-part names; honorific present or absent |
| Script variants | URD-005 | Urdu-script, Latin variants, both in one sentence |
| Postposition edges and nesting | URD-006 | Following `نے`, `کو`, `کی`, `پر`; person inside facility name |

## Policy decisions before gold annotation

Title/honorific inclusion; maximal versus nested entities (the shared-task design and a paper using its data differ); how to record alternate-script mentions of one person; whether ZWNJ is preserved in the evidence text. Do not treat UD tokens as PERSON gold.

## Experiment proposed to ner-eval and fastner

Hold evidence snapshot, split, model, decoding and scorer fixed except the manipulated factor. Compare a whitespace-token baseline with sub-token or cross-token candidates, and no-change versus offset-preserving code point folding. Report exact-span precision and recall, false positives on hard negatives, boundary error types and denominators by family. Keep fictional names and templates separated across splits. No threshold is set.

## What would reverse the decision

If a whitespace-token baseline matches character-reaching candidates across spacing variants on reviewed data, defer sub-token candidates; if the model already treats code point variants identically, drop folding; if native-speaker review shows an example is unnatural, remove its family.

## Handoff disposition

- `ner-evidence`: ready for owner review after Urdu language review; nothing adopted.
- `ner-eval`: slices proposed (urdu-space-variants, urdu-codepoint-variants, urdu-name-common-noun-minimal-pairs, urdu-name-structure, urdu-script-variants, urdu-postposition-boundary); execution pending evidence.
- `fastner` and `fastner-benchmarks`: deferred; nothing inspected or executed.

## Review and provenance

2026-10-04: produced with dossier-initialize, dossier-deep-research and dossier-document. Source checks are author reads of the pages and PDFs noted in [sources](sources.md), several via summarizing fetch or extracted text; no independent language review recorded. No GitHub issue was created.
