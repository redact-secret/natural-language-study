---
name: dossier-deep-research
description: Investigate NER-relevant linguistic questions with verified primary sources, counterexamples and claim-level provenance in a scoped language dossier.
---

# Dossier Deep Research

Produce answers that change a downstream decision, not a longer grammar summary. Use the existing dossier scope or establish it with `$dossier-initialize` when absent.

## Source-led investigation

Read [claim/review conventions](../../../CONVENTIONS.md), the target overview, source records and relevant findings. Select the unresolved assumption with the strongest engineering consequence; preserve prior finding IDs.

Search and inspect original orthographic authorities, grammars, linguistic papers and documented corpora. Record exact title/institution, locator, access date, known publication date and access limitations. Search excerpts are leads or limited checks, not a claim of having read a full paper. Do not infer publication date from crawl metadata.

For each consequential observation:

1. State what the source establishes and its variety/domain scope.
2. Seek independent corroboration or a competing account where it could alter a design decision. Two pages from one publisher or a paper restating another are not independent evidence.
3. Deliberately seek exceptions and ambiguous surface forms. Resolve apparent conflicts by scope when supported; otherwise retain the disagreement.
4. Distinguish normative spelling, attested usage, corpus annotation choices and runtime behavior. UD word units do not define PERSON spans.
5. Turn the observation into a falsifiable prediction with a baseline, matched negative and failure condition. Do not assign an accuracy threshold without a downstream requirement.

## Research record

Use canonical findings and source records from [dossier patterns](../../../conventions/dossier-files.md). Preserve original text and relevant code points. Attribute each example as synthetic/adapted/attested, with translation, boundary question, validation state and reuse terms. Brief sourced fragments may anchor a claim; do not redistribute source prose or corpora by default.

If a task asks for relevance to the current implementation, inspect the relevant downstream code read-only. Record revision, dirty-state scope and exact lines; distinguish source inspection from execution. Never infer measured errors from code shape or modify another repository as part of research.

## Stop condition

A bounded question has a sourced answer or a precise unresolved result; meaningful counterexamples and downstream decisions are recorded. Do not stop merely because the next source is inconvenient; do stop expanding scope once further reading does not change the decision. Missing qualified review keeps examples/findings draft where appropriate and must not prevent completing the authorized desk research.

Use `$dossier-document` to make the research readable and handoff-ready. No invented reviewer, model score, support claim, or issue URL. Structural validation and author self-check are not independent linguistic review.

## Breadth and stopping

For a broad dossier, apply the bounded-question stop condition to each requested topic, not to the entire language after one finding. Cover name structure, attachment, segmentation, person/non-person ambiguity and script/transliteration with substantive source-backed syntheses. A synthetic counterexample tests a proposed rule; it does not establish attested usage. Keep a precise research gap when sources cannot settle a point, and continue independent topics.
