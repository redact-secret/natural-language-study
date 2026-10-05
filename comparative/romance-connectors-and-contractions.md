# Romance name connectors, contractions and Unicode: French, Spanish, Portuguese, Italian

Question: when a surname connector or a preposition contraction touches a PERSON mention, which operations look shared across the four Latin-script Romance dossiers, and which causes must stay language-specific? This is a draft comparison of desk research. Every cited finding is untested and unreviewed by a qualified language reviewer; nothing here selects an implementation or measures an effect.

## Compact comparison

| Axis | French | Spanish | Portuguese | Italian |
| --- | --- | --- | --- | --- |
| Name-internal connector | `de`, `d’`, `du`, `des` ([FRA-001](../studies/french/findings/FRA-001.md)) | `de`, `de la`, `y`, `i` in double surnames ([SPA-001](../studies/spanish/findings/SPA-001.md)) | `da`, `de`, `do`, `das`, `dos`, `e` ([POR-001](../studies/portuguese/findings/POR-001.md)) | `da`, `De`, `Di`, `Della`, `D’` ([ITA-002](../studies/italian/findings/ITA-002.md)) |
| External look-alike | `le dossier de Claire` ([FRA-002](../studies/french/findings/FRA-002.md)) | `la casa de María`; `del`/`al` ([SPA-003](../studies/spanish/findings/SPA-003.md)) | `a casa da Maria`; `do`, `no`, `pelo` ([POR-002](../studies/portuguese/findings/POR-002.md)) | `la casa di Maria`; `dell’` before a common noun ([ITA-001](../studies/italian/findings/ITA-001.md)) |
| Case of the particle | Sources disagree ([FRA-004](../studies/french/findings/FRA-004.md)) | Lowercase after a given name, capitalized without one ([SPA-002](../studies/spanish/findings/SPA-002.md)) | Not settled by a verified source | `da Vinci` versus `D’Eredità` ([ITA-002](../studies/italian/findings/ITA-002.md)) |
| Apostrophe or hyphen | Elision `d’`; compound-name hyphen ([FRA-003](../studies/french/findings/FRA-003.md)) | Not a name-boundary issue in the sources read | Clitic hyphens `dá-lhe` ([POR-002](../studies/portuguese/findings/POR-002.md)) | Elision `dell’`; U+0027 versus U+2019 ([ITA-004](../studies/italian/findings/ITA-004.md)) |
| Accent and Unicode | Accents must survive matching ([FRA-003](../studies/french/findings/FRA-003.md)) | Capital accents; NFC/NFD versus accent loss ([SPA-005](../studies/spanish/findings/SPA-005.md)) | `António`/`Antônio`; NFC/NFD versus accent loss ([POR-003](../studies/portuguese/findings/POR-003.md)) | `Niccolò` versus `Nicolò` stay distinct ([ITA-004](../studies/italian/findings/ITA-004.md)) |
| Titles and cues | Not a first-wave finding | `Sr.`, personal `a` ([SPA-004](../studies/spanish/findings/SPA-004.md)) | `Sr.`, `Dra.`, `Dona`, `Dom` ([POR-005](../studies/portuguese/findings/POR-005.md)) | `Dott.ssa`, surname-first order ([ITA-003](../studies/italian/findings/ITA-003.md)) |
| Name/common-noun overlap | Name-derived nouns ([FRA-005](../studies/french/findings/FRA-005.md)) | `Pilar`, `Mercedes` ([SPA-006](../studies/spanish/findings/SPA-006.md)) | `Rosa`, `Silva` ([POR-006](../studies/portuguese/findings/POR-006.md)) | `Rosa`, `Conte`, `Re`, `Romano` ([ITA-005](../studies/italian/findings/ITA-005.md)) |

Empty or hedged cells mean the dossier did not establish the point. They are not evidence that the pattern is absent.

## Three layers

- **Observable operation (candidate shared).** The same surface string, such as `de`, `da`, `dell’` or `del`, is name-internal in one context and external grammar in a matched one. A mention may need to join tokens, end inside a contraction, or keep its original spelling. All four dossiers contain this pair.
- **Linguistic cause (language-specific).** Elision in French and Italian, article contraction in Spanish and Portuguese, coordinating `y`/`e`/`i` in Iberian double surnames, and clitic hyphens in Portuguese differ. Do not collapse them into one affix list.
- **Downstream policy (unresolved).** Whether titles, nickname articles and connector `y` belong inside PERSON spans is open in every decision brief. UD word splitting of `del`, `dell’` and Portuguese contractions is a syntactic convention, not a PERSON span definition.

## Rejected shortcuts

1. Use particle case as a membership gate. French sources disagree, Spanish case depends on whether a given name precedes, and Italian has both `da Vinci` and `D’Eredità`.
2. Strip every apostrophe or connector prefix. It truncates `Dell’Orso`-style surnames. Keeping all of them adds external prepositions.
3. Fold accents into identity. Italian `Niccolò` and `Nicolò` are distinct, and Portuguese `António` and `Antônio` are both standard.
4. Fix the name shape at one given name plus one or two surnames. Spanish connectors and Italian multi-component names counter it.
5. Treat shared Latin script as a shared profile. File count and script do not establish a shared implementation.

## Testable candidate capabilities

1. **Role-sensitive connector handling.** Compare contextual membership of connectors against a capitalized-run baseline and an always-drop baseline.
2. **Contraction-aware candidate ends.** Compare raw-token, UD-style split and role-aware units for `del`, `al`, `do`, `no`, `dell’`.
3. **Normalization with traceability.** Treat NFC/NFD and apostrophe code points as lookup-equivalent with an offset map. Run accent folding as a separate, lossy experiment.
4. **Cue features with hard negatives.** Test titles and the Spanish personal `a` on and off, with `A Coruña`-style and dative contrasts.

## Controlled comparison and falsification

Hold the name inventory, split, annotation policy, model and scorer fixed and change one mechanism per slice. Report omitted internal connectors and added external function words separately, with denominators, boundary-error type and a separate list of unresolved cases. Check candidate reachability before span accuracy for tokenizer changes.

Reject a candidate if it gives no gain over the baseline, or if it adds false positives on the matched negatives. Reject a shared Romance abstraction if per-language rules perform equally well while the shared one needs per-language exceptions.

## Handoffs

- `ner-evidence`: decide title, connector and nickname-article span policy first. Use the contrast families in the four decision briefs ([French](../studies/french/decision-brief.md), [Spanish](../studies/spanish/decision-brief.md), [Portuguese](../studies/portuguese/decision-brief.md), [Italian](../studies/italian/decision-brief.md)).
- `ner-eval`: slice names are proposals, not registered dimensions. Nothing has been run.
- `fastner`: options only. No downstream code was inspected here, so no runtime claim follows.
- `fastner-benchmarks`: deferred until evaluated artifacts exist.

## Gaps and source disagreements

- The RAE pages were inaccessible. Spanish case and contraction findings rest on search excerpts and need re-verification.
- Several Italian sources are secondary commentary. Brazilian statute text and Portuguese case guidance were not obtained.
- Mexican and other Latin American Spanish, Swiss Italian, dialects and African Portuguese are not covered.
- No corpus frequency, annotation agreement or independent language review exists for any cell.
- Related first-wave comparisons: [person boundaries](person-boundaries.md) and [boundary roles](boundary-roles-and-candidate-capabilities.md).
