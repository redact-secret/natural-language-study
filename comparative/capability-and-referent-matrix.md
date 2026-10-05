# PERSON recognition: capability and referent matrix

Scope: the English, Korean, Japanese and French dossiers, edited-language sources plus explicitly constructed stress inputs. This is a desk-research synthesis for [global epic #3](https://github.com/redact-secret/natural-language-study/issues/3), not an evaluated model result. The [earlier boundary study](boundary-roles-and-candidate-capabilities.md) and [pinned runtime audit](../research/runtime-boundary-audit.md) remain its implementation baseline.

## Result that changes the experiment order

Three independent failure classes require different remedies: a proposed span cannot be generated; a reachable span is assigned the wrong entity class; or a source annotation follows a different policy. Treating all three as tokenizer failures would produce misleading improvements. Representation transformations add another independent axis because equal-looking text may have different coordinates or lexical hashes.

| Language and sources | Capability question | Matched classification challenge | Policy prerequisite |
| --- | --- | --- | --- |
| [English](../studies/english/overview.md), ENG-001–005 | Preserve internal connectors, join components, keep coordinated people separate | Rose noun/verb controls; ordinary possessives; script-matched quoted words | Existing title/possessive contract; collective and corrupted-input adjudication |
| [Korean](../studies/korean/overview.md), KOR-001–006 | Within-eojeol edges, reviewed spaced names, romanized-name plus particle | 씨 individual versus surname category; ordinary nouns with particles | Map external suffix-inclusive annotations to target 0.2.0; resolve collective referents |
| [Japanese](../studies/japanese/overview.md), JPN-001–005 | Internal kana endpoints; names spanning script changes or middle dots | Kana ordinary words and ordinary roles with さん | Define Japanese address/title treatment; do not import UD units as spans |
| [French](../studies/french/overview.md), FRA-001–005 | Optional internal start after external d’, preserving internal surname d’ | Ordinary elision and figurative name-origin expressions | Define French particle/title and fictional/figurative policies |

## Shared capabilities, bounded by counterexamples

**Alternative endpoints** may be useful for Korean right edges, French left edges and Japanese internal edges. This supports a common capability to investigate, not one shared suffix list. [Korean morphology](../studies/korean/morphology.md) and [French morphology](../studies/french/morphology.md) distinguish the causes. Counterexample: splitting every apostrophe damages English and French internal surname components.

**Contextual classification** must receive clues outside the emitted span. An excluded title or particle can help identify a name; it cannot prove the referent is a person. Compare [Korean 씨](../studies/korean/findings/KOR-006.md), [Japanese ordinary address forms](../studies/japanese/ambiguity.md), [English lexical collisions](../studies/english/ambiguity.md) and [French antonomasia](../studies/french/findings/FRA-005.md). Reject a boundary-only improvement that increases matched-negative false positives.

**Representation-aware matching** must distinguish canonical normalization, transliteration and visual confusability. [Korean romanization](../studies/korean/findings/KOR-005.md) and [Japanese written-order/reading research](../studies/japanese/findings/JPN-005.md) do not authorize identity merging. [English script research](../studies/english/findings/ENG-005.md) and [French mixed-script contrasts](../studies/french/mixed-script.md) do not establish natural usage frequencies.

## Controlled experiment sequence

1. **ner-evidence: fix the meaning of the label.** Record target taxonomy version, inclusion rules, normalization contract and unresolved referents. Map imported policies explicitly. Review language examples before turning proposals into executable fixtures.
2. **fastner and ner-eval: check candidate coverage.** On the same reviewed spans, count whether both endpoints and a complete candidate can be represented by each backend. Report failure causes and denominators. Hold text and annotation fixed; this is not yet NER accuracy.
3. **ner-eval: measure selection/classification.** With comparable candidate capabilities, compare context features against the current baseline on positives and matched negatives. Separate truncation, leakage, mention merging and wrong entity class. Keep name identities and templates separated across train/test.
4. **fastner: evaluate cost and representation.** Compare candidate volume, latency and memory on the same workload. Test NFC/NFD mappings separately from width or confusable transformations; preserve original emitted spans. If a representation change requires retraining, document it rather than testing an incompatible old model.
5. **fastner-benchmarks: assess the evaluated artifact.** Only downstream results can support a readiness claim. No thresholds or language support decisions are invented here.

## Falsification and remaining limits

A shared endpoint mechanism is not justified if existing backends already expose all reviewed target spans, or if extra candidates cause unacceptable quality/cost tradeoffs under downstream requirements. A context feature is not justified if gains disappear on identity/template-held-out data or are offset by matched-negative errors. A normalization strategy fails its contract if it returns wrong source coordinates even when normalized lookup succeeds.

The requested six-topic breadth is now documented for each language. Independent language review, representative attested samples, broad naming-community coverage and measured NER effects remain outstanding. These are explicit limits on the result, not claims that every language question has been answered. Handoffs are local proposals ready for owner review; no downstream issue or implementation was created in this pass.
