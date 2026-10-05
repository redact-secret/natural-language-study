# Urdu: sources

Accessed 2026-10-04. Publication dates are null unless the page or PDF states one; search-result or crawl dates are not publication dates. Each record states what was actually read. Several pages were read through a summarizing fetch tool; those are marked "summary read" and are limited checks, not full reads. PDFs marked "text extracted" were parsed locally; their Urdu-script glyphs were garbled by extraction, so Urdu strings from those papers are described in English rather than reproduced. No source here is a measured result for any NER system in this repository.

## URD-S001

```yaml
id: URD-S001
title: 'The Unicode Standard, Version 16.0, Chapter 9: Middle East-I, Archaic Scripts (Arabic section)'
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-9/
accessed: '2026-10-04'
source_type: standard
language_scope:
- ur
relevant_locators:
- 9.2.1 Arabic (script extended for Urdu among other languages; Eastern Arabic-Indic digits U+06F0..U+06F9)
- 9.2.2 Arabic Cursive Joining (non-joiner use, Persian proper names)
- 9.2.4 Arabic Joining Groups (yeh barree U+06D2, Farsi yeh U+06CC)
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Summary read through a fetch tool, not the complete chapter; section statements were not re-checked against the printed text.
- Describes characters and joining, not Urdu spelling norms or name boundaries.
- Code-point names and decompositions in this dossier were also checked locally with Python 3.14 unicodedata (Unicode data 16.0.0); that check is an implementation observation, not an additional source.
```

## URD-S002

```yaml
id: URD-S002
title: 'Unicode Standard Annex #9: Unicode Bidirectional Algorithm'
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://www.unicode.org/reports/tr9/
accessed: '2026-10-04'
source_type: standard
language_scope:
- ur
- ur-Latn
relevant_locators:
- 3.2 Bidirectional character types (AL, AN, EN)
- 3.3.4 Resolving weak types (W2, W3)
- 3.3.5 Resolving neutral and isolate formatting types (N1, N2)
- 2.4 isolates versus embeddings
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Page header read as Unicode 18.0.0, revision 52, dated 2026-09-01; summary read through a fetch tool.
- Governs display order, not logical storage order or entity spans.
- Does not mention Urdu names.
```

## URD-S003

```yaml
id: URD-S003
title: 'Unicode Standard Annex #15: Unicode Normalization Forms'
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://www.unicode.org/reports/tr15/
accessed: '2026-10-04'
source_type: standard
language_scope:
- ur
relevant_locators:
- Introduction; canonical versus compatibility equivalence
- 1.2 Normalization Forms (NFC, NFKC definitions)
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Page header read as Unicode 18.0.0, revision 58, dated 2026-08-12; summary read through a fetch tool.
- The fetched summary reported no Arabic-letter discussion; the Urdu-specific consequences in URD-001 come from a local unicodedata run, not from this annex.
- Normalization is not an NER or transliteration policy.
```

## URD-S004

```yaml
id: URD-S004
title: A word segmentation system for handling space omission problem in urdu script
authors_or_institution:
- Nadir Durrani (sole author shown on the PDF first page; Institute for NLP, Universitat Stuttgart)
publication_date: null
url_or_identifier: https://alt.qcri.org/~ndurrani/pubs/SpaceOmission.pdf
accessed: '2026-10-04'
source_type: paper
language_scope:
- ur
relevant_locators:
- Abstract
- 1 Introduction (Nastalique, space not a reliable delimiter)
- 2 Space Omission Problem and 2.1 Non-Joiner Word Ending
- Table 2 (segmentation ambiguity; one example sentence contains a person name in the English translation)
- 3 Segmentation System (Orthographic Word concept; diacritic removal and normalization preprocessing)
- 4 Results, Tables 3-5
reuse_terms: Short attributed paraphrases only; no redistribution of the PDF.
limitations:
- PDF text extracted locally; Urdu glyphs garbled, so no Urdu string is quoted from it.
- A web search associated the topic with Durrani and Hussain (2010), but this specific PDF shows one author and no date; identity with that publication was not verified.
- Test corpus is 2367 words with 404 segmentation errors; a small, non-NER evaluation.
- Not a PERSON study; the person-name sentence is an incidental example.
```

## URD-S005

```yaml
id: URD-S005
title: Named Entity Recognition System for Urdu
authors_or_institution:
- Umrinder Pal Singh
- Vishal Goyal
- Gurpreet Singh Lehal
publication_date: '2012-12-01'
url_or_identifier: https://aclanthology.org/C12-1153.pdf
accessed: '2026-10-04'
source_type: paper
language_scope:
- ur
relevant_locators:
- 'COLING 2012 Technical Papers, pp. 2507-2518; day of month is not stated in the PDF (December 2012, Mumbai), so 2012-12-01 is a placeholder for the month'
- 'p. 2508: Table 1, the twelve IJCNLP-08 tags including Person Name and Title Person'
- 'pp. 2509-2510: section 4 Issues in Urdu NER (no capitalization, ambiguous names, spelling variation, resource scarcity)'
- 'p. 2515: Conclusion limitation 1 (three-word person-name rule) and limitation 5 (no segmentation technique)'
- 'p. 2516: limitation 7 (unresolved person/common-noun ambiguity)'
reuse_terms: Short attributed paraphrases only; no redistribution.
limitations:
- PDF text extracted locally; Urdu glyphs garbled, so Urdu examples are cited by their English glosses and transliterations only.
- Rule-based system with small gazetteers; reported scores are not imported and are not comparable to any FastNER result.
- Publication day is not stated; the placeholder date marks the month only.
```

## URD-S006

```yaml
id: URD-S006
title: 'Named Entity Recognition System for Postpositional Languages: Urdu as a Case Study'
authors_or_institution:
- Muhammad Kamran Malik
- Syed Mansoor Sarwar
publication_date: null
url_or_identifier: https://thesai.org/Downloads/Volume7No10/Paper_19-Named_Entity_Recognition_System_for_Postpositional_Languages.pdf
accessed: '2026-10-04'
source_type: paper
language_scope:
- ur
- ur-Latn
relevant_locators:
- IJACSA Vol. 7, No. 10, 2016; Introduction (hypothesis that a following postposition such as nay decides the preceding NE)
- IV Issues with the Urdu language, pp. 143-144 (items 1, 5, 8, 9, 10)
- V Data Collection, p. 144 (IJCNLP-08 NERSSEAL corpus, fazal examples, maximal-entity rule)
reuse_terms: Short attributed paraphrases only; no redistribution.
limitations:
- PDF text extracted locally; examples appear in the paper's own Roman transliteration, which is what this dossier cites.
- Journal year is from the page header; month and day not recorded.
- Compares tagging schemes on IJCNLP-08 data; scores are not imported and no claim is made about the BIL2 scheme beyond the authors' stated hypothesis.
```

## URD-S007

```yaml
id: URD-S007
title: Named Entity Dataset for Urdu NER Task (presentation slides)
authors_or_institution:
- Wahab Khan
- Ali Daud
- Jamal Abdul Nasir
- Tehmina Amjad
- International Islamic University, Islamabad
publication_date: null
url_or_identifier: https://www.cle.org.pk/clt16/Presentations/Named%20Entity%20Dataset%20for%20Urdu%20NER%20Task.pdf
accessed: '2026-10-04'
source_type: corpus
language_scope:
- ur
relevant_locators:
- 'Slides 7 (challenges: lack of capitalization, nested entities, complex orthography), 11-13 (IJCNLP-2008 and Jahangir et al. datasets), 14-19 (UNER dataset, BBC Urdu text, seven classes, 1207 Person mentions of 4621 entities)'
reuse_terms: Statistics paraphrased only; dataset terms not verified.
limitations:
- Slides, not the full paper; a one-sentence slide size figure ("about 0.48 k words") conflicts with the statistics slide (48,673 words), so the statistics slide is used and the discrepancy is recorded.
- Slide Urdu glyphs garbled by extraction; no Urdu string is quoted.
- Annotation guidelines for titles or honorifics are not visible in the slides.
```

## URD-S008

```yaml
id: URD-S008
title: 'NER for South and South East Asian Languages (NERSSEAL) IJCNLP-08 shared task, task description page'
authors_or_institution:
- IJCNLP-08 workshop organizers (LTRC, IIIT Hyderabad site)
publication_date: null
url_or_identifier: https://ltrc.iiit.ac.in/ner-ssea-08/index.cgi?topic=2
accessed: '2026-10-04'
source_type: other
language_scope:
- ur
relevant_locators:
- Task description (data for Hindi, Bengali, Oriya, Telugu and Urdu; nested named entities required, with a Person nested inside an Organization example)
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Summary read through a fetch tool; the linked Tagset and Annotation Guidelines pages were not read.
- The twelve-tag list is taken from the secondary table in URD-S005, not from this page.
```

## URD-S009

```yaml
id: URD-S009
title: UD Urdu UDTB treebank page
authors_or_institution:
- Universal Dependencies contributors; underlying treebank from IIIT Hyderabad
publication_date: null
url_or_identifier: https://universaldependencies.org/treebanks/ur_udtb/index.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- ur
relevant_locators:
- Summary statistics (5130 sentences, 138077 tokens, news genre)
- Tokenization note (6729 tokens, 5 percent, not followed by spaces)
- Provenance and license (CC BY-NC-SA 4.0)
reuse_terms: Treebank license reported as CC BY-NC-SA 4.0 on the page; verify before reuse.
limitations:
- Summary read through a fetch tool.
- Single genre (news); automatically converted annotation; UD word units do not define PERSON spans.
```

## URD-S010

```yaml
id: URD-S010
title: UD Urdu language documentation
authors_or_institution:
- Universal Dependencies contributors
publication_date: null
url_or_identifier: https://universaldependencies.org/ur/index.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- ur
relevant_locators:
- Tokenization (words delimited by whitespace, punctuation separated)
reuse_terms: Linked and paraphrased only.
limitations:
- Summary read through a fetch tool; the page was reported silent on ZWNJ, compounds, izafat and proper-noun policy, which means those points were not found, not that no policy exists.
```

## URD-S011

```yaml
id: URD-S011
title: A Clustering Framework for Lexical Normalization of Roman Urdu
authors_or_institution:
- Abdul Rafae Khan
- Asim Karim
- Hassan Sajjad
- Faisal Kamiran
- Jia Xu
publication_date: null
url_or_identifier: https://arxiv.org/abs/2004.00088
accessed: '2026-10-04'
source_type: paper
language_scope:
- ur-Latn
relevant_locators:
- Introduction (no standard Roman Urdu spelling; zindagi variants)
- Problem description (kaun/kon; bahar with two meanings; English-matching spellings; Roman Urdu/English code-switching)
reuse_terms: Short attributed paraphrases only.
limitations:
- Published as Natural Language Engineering vol. 28 (2022), pp. 93-123 per the arXiv abstract page; the arXiv preprint text (extracted locally) was read, not the journal version.
- Concerns common words, not personal names; name variation is an extrapolation.
```

## URD-S012

```yaml
id: URD-S012
title: Development of a Complete Urdu-Hindi Transliteration System
authors_or_institution:
- Gurpreet Singh Lehal
- Tejinder Singh Saini
publication_date: '2012-12-01'
url_or_identifier: https://learnpunjabi.org/pdf/COLING2012POSTERS063.pdf
accessed: '2026-10-04'
source_type: paper
language_scope:
- ur
- hi
relevant_locators:
- 'COLING 2012 Posters, pp. 643-652; day of month is not stated, so 2012-12-01 marks the month only'
- Abstract and 1 Introduction (same spoken language, different scripts)
- 2 Challenges in Urdu-Hindi Transliteration (missing diacritics, one-to-many mappings, word-level ambiguity, word segmentation, compounds)
reuse_terms: Short attributed paraphrases only.
limitations:
- PDF text extracted locally from a third-party mirror (learnpunjabi.org); the same proceedings are indexed by ACL Anthology but that copy was not opened.
- Reported accuracy (over 97 percent at word level) is the authors' figure for common words; no claim about names.
- The claim that Hindi and Urdu are variants of the same language is the authors' framing; it is a contested sociolinguistic statement and is used here only for the shared spoken register.
```

## URD-S013

```yaml
id: URD-S013
title: 'Muslim personal names in Urdu: Structure, meaning, and change'
authors_or_institution:
- Ahmad, Kulikov and Iqbal (given names not verified)
publication_date: null
url_or_identifier: https://qspace.qu.edu.qa/handle/10576/48419
accessed: '2026-10-04'
source_type: paper
language_scope:
- ur
relevant_locators:
- Abstract only, via a web search excerpt
reuse_terms: Unknown.
limitations:
- Landing pages returned HTTP 403 or access denied; only a search-result summary was read, which reported four name-length types, honorific, caste and patronymic components, husband's names for married women, and that Abdul and forms ending in -ul or -ur are titles rather than personal names.
- The summary attributes it to the International Journal of the Sociology of Language, 2023; volume, pages and DOI not verified.
- Treat as a lead; do not rely on the title/name-part classification until the article text is read.
```

## URD-S014

```yaml
id: URD-S014
title: 'Personal Names of Pakistani Muslims: An Essay on Onomastics'
authors_or_institution:
- Tariq Rahman
publication_date: null
url_or_identifier: https://journal.psc.edu.pk/index.php/pp/article/view/172
accessed: '2026-10-04'
source_type: paper
language_scope:
- ur
relevant_locators:
- Pakistan Perspectives vol. 18 no. 1 (2013); abstract only
reuse_terms: Unknown.
limitations:
- Abstract read; it frames names as markers of identity, religiosity and class and reports trends of Islamization, Arabization or Westernization; full text with naming-component detail not read.
- Concerns Pakistani Muslim names generally, not Urdu text specifically.
```

## URD-S015

```yaml
id: URD-S015
title: Review of Names, A Study of Personal Names, Identity and Power in Pakistan (Dawn)
authors_or_institution:
- Munizeh Zuberi (reviewer), Dawn newspaper
publication_date: null
url_or_identifier: https://www.dawn.com/news/amp/1216632
accessed: '2026-10-04'
source_type: other
language_scope:
- ur
relevant_locators:
- Whole review (summary read)
reuse_terms: Linked and paraphrased only; newspaper rights retained.
limitations:
- Secondary book review, not the book; the fetch tool reported a date of 2015-11-01 that was not otherwise confirmed.
- Reports that Pakistani naming lacks standardized conventions, varying by class, ethnicity and region, and a trend of a husband's or father's first name serving as a surname; used only as a caution against a single naming template.
```

## URD-S016

```yaml
id: URD-S016
title: CNIC (Pakistan)
authors_or_institution:
- Wikipedia contributors
publication_date: null
url_or_identifier: https://en.wikipedia.org/wiki/CNIC_(Pakistan)
accessed: '2026-10-04'
source_type: other
language_scope:
- ur
- ur-Latn
relevant_locators:
- Card layout (summary read)
reuse_terms: CC BY-SA per Wikipedia policy; not verified on this page.
limitations:
- Secondary encyclopedia page; no NADRA or National Language Authority primary naming guidance was located.
- Reported that the card prints given and family name in English and Urdu, plus a father's name or, for married women, a husband's name.
```

## URD-S017

```yaml
id: URD-S017
title: 'Urdu: An Essential Grammar (publisher description)'
authors_or_institution:
- Ruth Laila Schmidt
publication_date: '1999-10-07'
url_or_identifier: https://www.routledge.com/products/9780203979280
accessed: '2026-10-04'
source_type: grammar
language_scope:
- ur
relevant_locators:
- Publisher description and chapter overview only (postpositions chapter; Persian and Arabic influence chapter)
reuse_terms: Unknown.
limitations:
- Only the publisher page was read; the grammar itself was not available, so no grammatical claim in this dossier is sourced from it.
- The 1999 date comes from a search result for the book, not from the publisher page.
- Listed so that postposition and izafat claims remain explicitly unverified against a grammar.
```
