# Research Conventions

These conventions apply to research issues, dossier files, comparative studies, and downstream handoffs.

## 1. Purpose and ownership

Follow [research purpose and scope](conventions/research-purpose.md) and [dossier file patterns](conventions/dossier-files.md). This repository owns linguistic research. Executable fixtures, evaluation code, inference code, and benchmark results remain in their respective repositories.

Use English for shared prose and preserve original-language examples in their original script. Add a translation and, when useful, a gloss or transliteration. Translation must not replace the original text.

## 2. Claim discipline

Label the following separately:

- **Observation:** a source-backed description of language behavior within a stated scope.
- **Hypothesis:** a proposed effect on NER that still needs testing.
- **Experiment proposal:** a method for testing the hypothesis.
- **Downstream result:** a linked result produced by an evidence, evaluation, implementation, or benchmark repository.

Do not turn typological descriptions into universal rules. A language, script, region, and naming community are different dimensions. Record exceptions, competing explanations, and uncertainty explicitly.

Avoid language-wide claims based on one example or one domain. Record negative results and disagreements rather than removing inconvenient evidence.

## 3. Sources and provenance

Prefer grammars, linguistic reference works, peer-reviewed studies, authoritative orthographic guidance, and documented corpora or datasets. Distinguish official spelling conventions from observed usage. Secondary sources can identify leads but should not silently substitute for primary evidence.

For each source, record a stable URL or identifier, title, author or institution, publication date when known, access date, and the relevant section or page. Map each substantive observation to source IDs. State when a source is unavailable or supports only part of a claim.

Independent corroboration is desirable for consequential findings. When only one source is available, explain that limitation. A native-speaker review can clarify examples but must record the reviewer's scope of competence and is not a substitute for all documentary evidence.

AI-assisted suggestions are research leads, not sources. Verify citations and language examples before marking a finding reviewed. Do not invent publications, quotations, reviewer identities, or source details.

## 4. Examples and text fidelity

Mark every example as `synthetic`, `adapted`, or `attested`. For adapted and attested examples, link the source and record reuse restrictions. Use fictional people in synthetic examples; do not publish sensitive personal records.

Preserve spelling, punctuation, whitespace, diacritics, and relevant Unicode distinctions. If normalized text is useful, show it separately and name the transformation. Record invisible characters explicitly when they affect a claim.

A research example is illustrative, not an executable fixture or authoritative gold annotation. Any proposed span must state the boundary question and remain subject to `ner-evidence` review. Do not imply that illustrative examples measure coverage.

Include contrasts that can challenge the hypothesis: ordinary nouns, alternative entity readings, different attached forms, and variations in script or register where relevant.

## 5. Files and identifiers

Use UTF-8 Markdown with a final newline. Use lowercase kebab-case filenames. Use stable language keys and finding IDs as defined in [dossier file patterns](conventions/dossier-files.md).

Never renumber a published finding or reuse its ID. Update it in place, with a revision note, or mark it superseded and link its replacement. Keep relative documentation links valid.

Each topic file has one clear purpose. Avoid copying the same finding into multiple topic files; summarize and link to its canonical file.

## 6. Issue and epic structure

A language epic tracks the dossier scope, research questions, and topic sub-issues. A comparative epic tracks a specific cross-language question. Avoid splitting research into empty issues merely to match every taxonomy dimension.

Each research issue should contain:

1. Question and motivation.
2. Language varieties, scripts, registers, and entity types in scope.
3. Explicit exclusions and known gaps.
4. Source plan and expected dossier paths.
5. Required contrasts or counterexamples.
6. Expected downstream decisions and handoff destinations.
7. Completion criteria and links to related work.

An issue is complete when its findings are merged, review and limitations are recorded, and applicable handoffs are linked or a reason for no handoff is documented. Completion does not require a favorable model result.

## 7. Review and status

Findings progress through `draft`, `reviewed`, and optionally `superseded` or `withdrawn`. `reviewed` means the documented research has passed the checks below; it does not mean the NER hypothesis was confirmed or a language is supported.

Before marking a finding reviewed, verify:

- Citations exist and support the stated observations.
- Language scope and example provenance are explicit.
- Original text, translations, and relevant boundary distinctions are checked.
- Counterexamples and limitations are present.
- Hypotheses are distinguishable from facts and can be tested.
- Downstream ownership and links are accurate.

Record reviewer identity or handle, date, review scope, and remaining gaps. If qualified language review is missing, say so and lower confidence where appropriate. The author may self-check a draft but must not present that as independent review.

## 8. Confidence and downstream outcomes

Use `low`, `medium`, or `high` confidence for the linguistic observation and explain why. Confidence is an editorial assessment of source and scope quality, not a numerical probability, model confidence, or accuracy score.

Track NER hypothesis outcomes separately as `untested`, `inconclusive`, `supported`, or `not-supported`, always within a named experiment and scope. `supported` requires a linked downstream result. It is not a permanent language-wide guarantee.

## 9. Contributions and rights

Keep contributions focused and include a short description of the question, findings, limitations, and handoffs. Record materially changed claims in a revision note.

Original contributions use the repository's MIT license. Do not copy source chapters or redistribute corpora unless their terms permit it. Record third-party attribution and licensing separately; original commentary under MIT does not relicense source material.
