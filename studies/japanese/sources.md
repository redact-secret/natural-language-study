# Japanese: sources

Accessed 2026-10-04. Publication dates are unknown unless stated; search crawl dates are not publication dates. Links and relevant publisher text were checked; no source is a measured NER result.

## JPN-S001

```yaml
id: JPN-S001
title: 'Introduction: UD Japanese (version 2)'
authors_or_institution:
- Universal Dependencies Japanese contributors
publication_date: null
url_or_identifier: https://universaldependencies.org/ja/overview/introduction.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- ja-JP
relevant_locators:
- Basic Policy; Word Units
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Different segmentation standards are documented; no NER superiority result.
```

## JPN-S002

```yaml
id: JPN-S002
title: 'Irodori Starter, Lesson 3: よろしくお願いします (audio-script edition)'
authors_or_institution:
- The Japan Foundation
publication_date: null
url_or_identifier: https://www.irodori.jpf.go.jp/assets/data/starter/pdf/X_L03_au.pdf
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- ja-JP
relevant_locators:
- L3-9, asking names and origins
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Indexed publisher lesson text shows name + さん + も; narrow teaching context, not
  exhaustive honorific guidance.
```

## JPN-S003

```yaml
id: JPN-S003
title: Japanese Script Resources
authors_or_institution:
- W3C Internationalization
publication_date: null
url_or_identifier: https://www.w3.org/TR/jpan-lreq/
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- ja-JP
relevant_locators:
- Script overview; Japanese and Western mixed text composition links
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Writing/layout description; does not establish how often scripts indicate PERSON.
```

## JPN-S004

```yaml
id: JPN-S004
title: 'Unicode Normalization Forms (UAX #15)'
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://www.unicode.org/reports/tr15/
accessed: '2026-10-04'
source_type: standard
language_scope:
- ja-JP
relevant_locators:
- Introduction; Normalization Forms; Hangul composition/decomposition
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Canonical and compatibility equivalence; not a NER or transliteration policy.
```

## JPN-S005

```yaml
id: JPN-S005
title: Character-based Bidirectional LSTM-CRF with words and characters for Japanese
  Named Entity Recognition
authors_or_institution:
- Shotaro Misawa
- Motoki Taniguchi
- Yasuhide Miura
- Tomoko Ohkuma
publication_date: null
url_or_identifier: https://aclanthology.org/W17-4114/
accessed: '2026-10-04'
source_type: paper
language_scope:
- ja-JP
relevant_locators:
- 'PDF pp. 98–100: sections 3, 4.2, 5.1 and table 4'
reuse_terms: Short attributed excerpts and original paraphrases only; no corpus redistribution.
limitations:
- Experiments cover Product, Location, Organization and Time, not PERSON.
- 2017 architecture and Mainichi newspaper data; no FastNER outcome.
bibliographic_note: September 2017, pp. 97–102; DOI 10.18653/v1/W17-4114. PDF text
  inspected; no table scores imported.
```

## JPN-S006

```yaml
id: JPN-S006
title: Japanese Named Entity Recognition Using Structural Natural Language Processing
authors_or_institution:
- Ryohei Sasano
- Sadao Kurohashi
publication_date: null
url_or_identifier: https://aclanthology.org/I08-2080/
accessed: '2026-10-04'
source_type: paper
language_scope:
- ja-JP
relevant_locators:
- 'PDF p. 609: section 4.2, Morphological Analysis and Figure 1'
reuse_terms: Short attributed excerpts and original paraphrases only; no corpus redistribution.
limitations:
- Different analyzers/dictionaries can produce different granularity; no PERSON gain
  inferred here.
- Used for the documented boundary problem, not as a current model recommendation.
bibliographic_note: 2008, IJCNLP Volume II. Publisher metadata and section text checked.
```

## JPN-S007

```yaml
id: JPN-S007
title: 外来語・外国語の取扱い及び姓名のローマ字表記について(依頼)
authors_or_institution:
- Agency for Cultural Affairs, Japan
publication_date: '2000-12-26'
url_or_identifier: https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/sanko/gairai/pdf/roma_hyoki.pdf
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- ja-JP
relevant_locators:
- 'Page 1: family-name/given-name recommendation'
reuse_terms: Short attributed excerpts and original summaries only; source rights
  retained.
limitations:
- Historical 2000 request to institutions; not evidence that all writers follow one
  order.
```

## JPN-S008

```yaml
id: JPN-S008
title: 'Unicode Script Property (UAX #24)'
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://unicode.org/reports/tr24/
accessed: '2026-10-04'
source_type: standard
language_scope:
- ja-JP
relevant_locators:
- 'Section 3, Table 7: U+30FC and U+3099'
reuse_terms: Short attributed excerpts and original summaries only; source rights
  retained.
limitations:
- Properties are character-level; they do not identify personal names.
```

## JPN-S009

```yaml
id: JPN-S009
title: Personal names around the world
authors_or_institution:
- W3C Internationalization
publication_date: null
url_or_identifier: https://www.w3.org/International/questions/qa-personal-names
accessed: '2026-10-04'
source_type: other
language_scope:
- ja-JP
relevant_locators:
- Ambiguity in written forms
reuse_terms: Short attributed excerpts and original summaries only; source rights
  retained.
limitations:
- Internationalization guidance, not a Japanese naming dictionary or corpus.
```

## JPN-S010

```yaml
id: JPN-S010
title: 'ミラー: デジタル大辞泉 entries'
authors_or_institution:
- Shogakukan, Digital Daijisen; hosted by Kotobank
publication_date: null
url_or_identifier: https://kotobank.jp/word/%E3%81%BF%E3%82%89%E3%83%BC-1598684
accessed: '2026-10-04'
source_type: dictionary
language_scope:
- ja-JP
relevant_locators:
- 'Digital Daijisen: mirror sense and Henry/Arthur/Glenn Miller entries'
reuse_terms: Original summary only; dictionary rights retained.
limitations:
- Publisher dictionary content presented by an aggregator; entries establish lexical/name
  readings, not corpus frequency or sentence-level gold.
```
