# Boundary roles and candidate capabilities

**Decision:** share the ability to propose and score boundaries, not a universal rule that removes attached text. The first-wave research now identifies different work for each language, supported by scoped findings and a pinned runtime inspection.

Tracked by [Global Language Typology #3](https://github.com/redact-secret/natural-language-study/issues/3). Draft linguistic review; source inspection and tokenizer probing completed; model hypotheses untested.

## Decisions by language

| Language and scope | Research result that changes the decision | Immediate handoff |
| --- | --- | --- |
| English, edited British/US prose | Shared possession does not imply one person; possessive tokenizer cuts already exist. [ENG-004](../studies/english/findings/ENG-004.md). | Test coordinated-mention merging and name/common-noun cues with the current tokenizer. |
| Korean, South Korean written forms | NIKL includes name suffix 이, but target ner-evidence 0.2.0 excludes it. [KOR-004](../studies/korean/findings/KOR-004.md). | Preserve target policy and explicitly map imported annotations before computing boundary errors. |
| Japanese, contemporary written forms | The current kana run can contain a proposed name edge; the inspected character-NER paper has no PERSON evaluation. [JPN-004](../studies/japanese/findings/JPN-004.md). | Verify endpoint capability and profile eligibility, then run PERSON-specific evaluation. |
| French, scoped standard writing/editorial guidance | Particle casing has conflicting guidance; external elision and internal d’ can look alike. [FRA-004](../studies/french/findings/FRA-004.md), [FRA-002](../studies/french/findings/FRA-002.md). | Separate elision endpoints, contextual particle membership and canonical lookup experiments. |

## Pattern 1: attachment role is not attachment shape

Compare English clitics, Korean case particles/name suffixes, Japanese address forms and French surname components. All can touch names, but their roles and target inclusion differ. The Korean source/target policy conflict demonstrates why a linguistically correct analysis does not uniquely specify a gold span.

Candidate shared capability: propose alternative cuts with role/context information and retain the annotation-policy identity. **Rejected shortcut:** a cross-language suffix or apostrophe deletion list. A listed surface string is neither sufficient evidence of a person nor sufficient evidence for exclusion.

Sources: [ENG-001](../studies/english/findings/ENG-001.md), [KOR-004](../studies/korean/findings/KOR-004.md), [JPN-002](../studies/japanese/findings/JPN-002.md), [FRA-002](../studies/french/findings/FRA-002.md).

## Pattern 2: boundary capability precedes boundary accuracy

Token ends, morphological units and entity ends need not coincide. The [runtime audit](../research/runtime-boundary-audit.md) observed `アリスさんが` and `d’Élodie` as individual units, while Hangul syllable edges and English possessive separation already exist. These observations concern the inspected tokenizer, not every downstream decoder.

Candidate shared capability: endpoints inside a unit where needed, plus multi-unit candidates. First count which reviewed gold spans can be represented; only then compare candidate selection quality. A tokenizer/projection that cannot express the relevant cut cannot be rescued merely by changing a lexical feature. Conversely, existing sufficient boundaries do not justify tokenizer replacement.

**Rejected shortcut:** “all four languages need a new tokenizer.” No concrete API or neural architecture is selected by this study.

## Pattern 3: orthographic cues need disconfirming contexts

Casing, script transitions, title-like forms and conjunctions can be helpful without defining PERSON. French particle-casing disagreement and English coordinated possessors add distinct failure modes to the earlier script/name-common-noun contrasts.

Candidate shared capability: context-sensitive cue scoring with hard negatives and mention-count errors. Preserve individual name spelling. **Rejected shortcut:** uppercase-only candidates or katakana-as-PERSON.

Sources: [ENG-002](../studies/english/findings/ENG-002.md), [ENG-004](../studies/english/findings/ENG-004.md), [JPN-003](../studies/japanese/findings/JPN-003.md), [FRA-004](../studies/french/findings/FRA-004.md).

## Pattern 4: equivalent representation and equivalent identity differ

[KOR-003](../studies/korean/findings/KOR-003.md) and [FRA-003](../studies/french/findings/FRA-003.md) motivate canonical-equivalence tests. The inspected runtime composes conjoining Hangul jamo for hashing, but two observed French NFC/NFD surname forms produced distinct hashes. Keeping combining marks in a token is not sufficient for canonical lookup equivalence.

Candidate shared capability: original-coordinate preservation and clearly named lookup transformations. **Rejected shortcut:** treating NFC, width folding, accent removal and transliteration as interchangeable. The current evidence contract stores NFC text; raw NFD inputs require a compatible projection/adapter rather than silently changing fixtures.

This comparison does not establish script-mixing coverage for English, Korean or French. Those dossier dimensions remain incomplete.

## Controlled handoff sequence

1. **ner-evidence:** confirm target conventions, explicitly map incompatible external annotation rules, review matched contrast families and retain provenance. The four briefs below propose 16 families, not a statistically sufficient sample size or gold corpus.
2. **ner-eval:** define or reuse slices and calculate boundary capability, exact spans and hard-negative errors with denominators. Fix policy/data/splits across comparisons. Report unresolved cases rather than assuming a single interpretation.
3. **fastner:** compare only the mechanism implicated by a gap. Keep training budget/data fixed; retrain when the unit/model contract changes. Verify source-coordinate fidelity and quality/cost tradeoffs in that repository.
4. **fastner-benchmarks:** accept actual evaluated artifacts after the above. This repository does not determine support readiness.

A proposed shared mechanism is rejected if it cannot express reviewed cuts, if benefits disappear under the target policy, or if matched-negative errors offset gains. Thresholds and release gates belong to downstream owners; no numerical targets are invented here.

## Owner-ready packets and remaining uncertainty

[English](../studies/english/decision-brief.md), [Korean](../studies/korean/decision-brief.md), [Japanese](../studies/japanese/decision-brief.md), [French](../studies/french/decision-brief.md).

All four packets are concrete local proposals ready for review. They do not constitute downstream adoption. Representative attested sampling, qualified language review, PERSON model experiments and cost measurements remain pending. Source disagreements and the non-PERSON scope of the Japanese paper are explicit limits, not discarded evidence.
