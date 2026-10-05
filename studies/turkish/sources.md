# Turkish: sources

Accessed 2026-10-04. Publication dates are unknown unless stated; search crawl dates are not publication dates. **Access caveat:** nearly every record below was read through a WebFetch model-generated summary or a search excerpt rather than raw text or a full PDF; PDFs from arXiv and Unicode could not be decoded. Quoted figures and rule wording are therefore as reported by those summaries and need re-checking against the live pages before any record is promoted to reviewed. Grammar coverage is thin: Göksel and Kerslake, *Turkish: A Comprehensive Grammar* (Routledge, 2005) was identified but not read and has no source record. No source here is a measured NER result.

## TUR-S001

```yaml
id: TUR-S001
title: 'TDK Yazım Kuralları: Kesme İşareti (apostrophe rules)'
authors_or_institution:
- Türk Dil Kurumu (TDK)
publication_date: null
url_or_identifier: https://tdk.gov.tr/icerik/yazim-kurallari/kesme-isareti/
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- tr-TR
relevant_locators:
- Rule on separating possessive, case and predicate suffixes from proper nouns; exception paragraphs for institution/organization names and for derivational/plural suffixes; examples with Bey/Hanım, abbreviations and numbers
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Page content was obtained through a WebFetch model-generated summary, not raw page text; wording and rule numbering were not verified against the page or the printed Yazım Kılavuzu.
- Normative spelling, not observed usage frequency.
- Examples listed in findings are those reported by the summary; re-check against the live page.
```

## TUR-S002

```yaml
id: TUR-S002
title: 'TDK Yazım Kuralları: Büyük Harflerin Kullanıldığı Yerler (capitalization)'
authors_or_institution:
- Türk Dil Kurumu (TDK)
publication_date: null
url_or_identifier: https://tdk.gov.tr/icerik/yazim-kurallari/buyuk-harflerin-kullanildigi-yerler/
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- tr-TR
relevant_locators:
- Capitalization of personal names and of titles, respect words and ranks before or after names; kinship terms used as ordinary words versus as titles
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Obtained through a WebFetch model-generated summary, not raw text; wording not verified.
- The summary reported nothing on i/İ casing; absence in the summary is not evidence of absence on the page.
- Normative, not usage frequency.
```

## TUR-S003

```yaml
id: TUR-S003
title: Unicode SpecialCasing.txt (Turkish and Azeri conditional mappings)
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://www.unicode.org/Public/UCD/latest/ucd/SpecialCasing.txt
accessed: '2026-10-04'
source_type: standard
language_scope:
- tr-TR
relevant_locators:
- 'Language-sensitive section: lines for U+0130, U+0049 (Not_Before_Dot), U+0307 (After_I) and U+0069 with tr and az conditions'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Lines were relayed by a WebFetch summarizer; the exact line text was not independently confirmed against the raw file, and the file header and version were not recorded.
- Defines case mappings, not NER policy or what real software applies by default.
```

## TUR-S004

```yaml
id: TUR-S004
title: Local Python unicodedata and str-method probe of İ, ı and combining dot above
authors_or_institution:
- Author's local check (not a published source)
publication_date: null
url_or_identifier: python3 3.14.7, standard library unicodedata and str.lower/upper/normalize, run 2026-10-04 in the author's environment
accessed: '2026-10-04'
source_type: other
language_scope:
- tr-TR
relevant_locators:
- Code points of U+0130, U+0131; NFD of U+0130 is U+0049 U+0307; NFC recomposes; str.lower() of U+0130 gives U+0069 U+0307; str.lower() of 'ISPARTA' gives 'isparta'; NFKC equals NFC for U+0130
reuse_terms: Author-generated observation; repository MIT license.
limitations:
- One runtime and one version; default non-locale behavior only, so it shows what a locale-unaware lowercase does and says nothing about other runtimes.
- Reproducible observation by the author, not an independent source.
```

## TUR-S005

```yaml
id: TUR-S005
title: 'Universal Dependencies: UD Turkish BOUN treebank'
authors_or_institution:
- TABILAB, Boğaziçi University (Büşra Marşan, Furkan Akkurt, Utku Türk and others)
- Universal Dependencies
publication_date: null
url_or_identifier: https://universaldependencies.org/treebanks/tr_boun/index.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- tr-TR
relevant_locators:
- 'Summary section: size, genre, multi-word token statistics, letters-plus-punctuation word types, license'
reuse_terms: Linked and paraphrased only; treebank licence reported as CC BY-SA 4.0, no text reused.
limitations:
- Obtained through a WebFetch summary of the treebank landing page; counts quoted are as reported there (9,761 sentences; 3,374 multi-word tokens; 2,148 word types mixing letters and punctuation).
- UD word and token units do not define PERSON spans; the page does not describe an NER annotation.
```

## TUR-S006

```yaml
id: TUR-S006
title: 'Universal Dependencies: UD Turkish IMST treebank'
authors_or_institution:
- Utku Türk, Şaziye Betül Özateş, Büşra Marşan, Furkan Akkurt, Çağrı Çöltekin, Gülşen Cebiroğlu Eryiğit and others (as reported)
- Universal Dependencies
publication_date: null
url_or_identifier: https://universaldependencies.org/treebanks/tr_imst/index.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- tr-TR
relevant_locators:
- 'Summary section: size, genre, tokens not followed by space, word types combining letters and punctuation, multi-word tokens'
reuse_terms: Linked and paraphrased only; treebank licence reported as CC BY-NC-SA 4.0, no text reused.
limitations:
- Obtained through a WebFetch summary; reported 5,635 sentences, 611 letters-plus-punctuation types and 1,639 multi-word tokens. Licence reported as CC BY-NC-SA 4.0, so no reuse of text here.
- UD units are not NER spans.
```

## TUR-S007

```yaml
id: TUR-S007
title: A statistical information extraction system for Turkish (PhD thesis)
authors_or_institution:
- Gökhan Tür (advisor Kemal Oflazer), Bilkent University
publication_date: null
url_or_identifier: https://repository.bilkent.edu.tr/items/bd25a51a-e7bb-499d-804d-8e8860f70fbb
accessed: '2026-10-04'
source_type: paper
language_scope:
- tr-TR
relevant_locators:
- 'Repository abstract page: lists text deasciification, word segmentation, vowel restoration, sentence segmentation, topic segmentation and name tagging as tasks'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Only the repository abstract summary was read, not the thesis; publication year 2000 as reported by the repository.
- The deasciification method and any accuracy figures were not read.
```

## TUR-S008

```yaml
id: TUR-S008
title: Initial Explorations on using CRFs for Turkish Named Entity Recognition (COLING 2012)
authors_or_institution:
- Gökhan Akın Şeker
- Gülşen Eryiğit
publication_date: null
url_or_identifier: https://preview.aclanthology.org/menus/C12-1150/
accessed: '2026-10-04'
source_type: paper
language_scope:
- tr-TR
relevant_locators:
- 'Abstract: CRF model using morphological features and gazetteers for Turkish NER'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Only the abstract as relayed by a search result was read; no treatment of apostrophes or suffix spans was verified.
- Publication date within 2012 not recorded.
```

## TUR-S009

```yaml
id: TUR-S009
title: Extending a CRF-based Named Entity Recognition Model for Turkish Well Formed Text and User Generated Content
authors_or_institution:
- Gökhan Akın Şeker
- Gülşen Eryiğit
publication_date: null
url_or_identifier: https://semantic-web-journal.net/content/extending-crf-based-named-entity-recognition-model-turkish-well-formed-text-and-user-0
accessed: '2026-10-04'
source_type: paper
language_scope:
- tr-TR
relevant_locators:
- 'Abstract page: news versus Web 2.0 results, re-annotated data'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Only the abstract page was read, as summarized by a fetch tool; the summarizer reported roughly 92% F1 on news and about 65% on Web 2.0 data, which are quoted from that summary only and not recomputed.
- Normalization, apostrophe and deasciification details were not found in the abstract.
```

## TUR-S010

```yaml
id: TUR-S010
title: Named Entity Recognition for Turkish Tweets (arXiv 1410.8668; EACL workshop on Language Analysis for Social Media, 2014)
authors_or_institution:
- Dilek Küçük
- Ralf Steinberger
publication_date: '2014-10-31'
url_or_identifier: https://arxiv.org/abs/1410.8668
accessed: '2026-10-04'
source_type: paper
language_scope:
- tr-TR
relevant_locators:
- 'Abstract: relaxed capitalization constraints, diacritics-based expansion of lexical resources, tweet normalization'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Only the arXiv abstract page was read, as summarized by a fetch tool; the full paper PDF could not be decoded.
- Submission date used as publication date; the arXiv listing title was reported differently by the search tool ('Experiments to Improve Named Entity Recognition on Turkish Tweets').
```

## TUR-S011

```yaml
id: TUR-S011
title: To What Extent are Name Variants Used as Named Entities in Turkish Tweets? (arXiv 1912.07940)
authors_or_institution:
- Dilek Küçük
publication_date: '2019-12-17'
url_or_identifier: https://arxiv.org/abs/1912.07940
accessed: '2026-10-04'
source_type: paper
language_scope:
- tr-TR
relevant_locators:
- 'Abstract: categories of informal name variants in a tweet dataset: abbreviations, nicknames, contractions, diminutives, capitalization inconsistency, spelling mistakes'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Only the abstract page was read; the PDF could not be decoded, so counts and category definitions were not verified.
- The abstract does not name apostrophe omission or ASCII-fication as categories.
```

## TUR-S012

```yaml
id: TUR-S012
title: Snowball Turkish stemming algorithm
authors_or_institution:
- Snowball project (Martin Porter's Snowball; Turkish stemmer authorship not verified)
publication_date: null
url_or_identifier: https://snowballstem.org/algorithms/turkish/stemmer.html
accessed: '2026-10-04'
source_type: other
language_scope:
- tr-TR
relevant_locators:
- 'Description of apostrophe handling: truncation at the first apostrophe when at least two characters precede it; use of U+0131 in the rules'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Obtained through a WebFetch summary; documents a stemmer's design, not an NER recommendation.
- Shows one deployed heuristic that treats the apostrophe as a stem boundary, including a caveat for foreign names such as o'connor.
```

## TUR-S013

```yaml
id: TUR-S013
title: 2525 sayılı Soyadı Kanunu (Surname Law), 2 July 1934, text reproduced by a commercial site
authors_or_institution:
- Türkiye Büyük Millet Meclisi (law); text reproduced on alomaliye.com
publication_date: '1934-07-02'
url_or_identifier: https://alomaliye.com/1934/07/02/2525-sayili-kanun-soyadi-kanunu/
accessed: '2026-10-04'
source_type: other
language_scope:
- tr-TR
relevant_locators:
- 'Articles 1 to 3 as summarized: surname obligation, given name first then surname, restrictions on surnames based on rank, position, tribe, foreign ethnic names'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Secondary reproduction, not the official gazette or mevzuat.gov.tr text; read as a fetch-tool summary.
- Law date taken from the page header as reported. Later amendments (for example on Article 3) and the Nüfus Hizmetleri Kanunu were not read.
```

## TUR-S014

```yaml
id: TUR-S014
title: 'TDK Güncel Türkçe Sözlük (sozluk.gov.tr) entries: gül, deniz, yıldız, çiçek, umut, kaya, demir, aslan, can, ay, bey, hanım, efendi'
authors_or_institution:
- Türk Dil Kurumu (TDK)
publication_date: null
url_or_identifier: https://sozluk.gov.tr/gts?ara=gül
accessed: '2026-10-04'
source_type: other
language_scope:
- tr-TR
relevant_locators:
- JSON returned by the dictionary's search endpoint for each headword; first one or two senses and the ozel_mi (proper-noun) flag inspected
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Only the first one or two senses per entry were inspected; the dictionary headword is a common-noun entry for every word except 'Aslan', which has a separate proper-noun entry referring to the zodiac sign.
- Absence of a given-name sense in the inspected senses does not show the dictionary has none; the endpoint is not a documented stable API.
- Sense wording is not reproduced beyond short fragments.
```

## TUR-S015

```yaml
id: TUR-S015
title: Mehmedim nasıl yazılır? TDK'ye göre doğru yazım nedir, özel isimlere ek nasıl gelir? (Yeni Birlik Gazetesi)
authors_or_institution:
- Yeni Birlik Gazetesi (author not identified)
publication_date: '2026-03-09'
url_or_identifier: https://www.gazetebirlik.com/genel/mehmedim-nasil-yazilir-tdkye-gore-dogru-yazim-nedir-ozel-isimlere-ek-nasil-gelir/956805
accessed: '2026-10-04'
source_type: other
language_scope:
- tr-TR
relevant_locators:
- 'Whole article, as summarized: claims that consonant softening does not apply to proper names (Mehmet''im, not Mehmedim) and cites the TDK apostrophe rule'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Newspaper explainer, secondary and not authoritative; read through a fetch summary; used only as a lead for the softening contrast, not as a grammar source.
- Publication date from the page byline as reported.
```
