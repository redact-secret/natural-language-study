# Hindi: sources

Accessed 2026-10-04. Publication dates are null unless the source states them. Search-result snippets were used only to find candidate sources. Each record says what was actually read. No source here is a measured result for this repository's NER systems. A source about Hindi does not by itself describe other Indian languages.

Reading modes used below: **full text** means the text of the document was extracted and read in the relevant parts; **fetch summary** means a fetch tool returned a model-generated summary of the page, so wording was not independently confirmed against the page text; **local computation** means a deterministic check run for this dossier.

## HIN-S001

```yaml
id: HIN-S001
title: "देवनागरी लिपि एवं हिंदी वर्तनी का मानकीकरण (Devanagari Lipi evam Hindi Vartani ka Manakikaran), revised edition 2024"
authors_or_institution:
- Central Hindi Directorate, Department of Higher Education, Ministry of Education, Government of India
publication_date: null
url_or_identifier: https://chd.education.gov.in/sites/default/files/devanagarilipiandhindivartanikamankikaran.pdf
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- hi-IN
relevant_locators:
- "Section 2.1.1 (anusvara and chandrabindu both retained), printed p. 9"
- "Section 2.2 (numerals: international form of Indian numerals for official purposes; Devanagari numerals may additionally be authorized), printed p. 9-10"
- "Section 3.2.1-3.2.2 (postpositions written separately from nouns, joined to pronouns), printed p. 26-27"
- "Section 3.5.3 (श्री and जी written separately unless part of the proper noun), printed p. 28"
- "Section 3.6 (anusvara and chandrabindu usage rules), printed p. 28-30"
- "Section 3.11.2 (South Indian personal and family names kept as in the source language), printed p. 32"
- "Section 3.15.1-3.15.2 (nukta not retained in Hindi alphabet for Urdu-origin loanwords; ॉ for English o), printed p. 33-34"
- "Section 3.16 (danda is the only full-stop sign; other punctuation adopted from English), printed p. 34"
relevant_locators_note: "Printed page numbers are taken from the PDF's own page numbers and table of contents. PDF page = printed page + 11."
reuse_terms: "Government of India publication; reuse terms not verified. Paraphrased only; at most short rule examples are reproduced."
limitations:
- "Full text read from the downloaded PDF (56 pages, 14.5 MB) with a text extractor. The embedded legacy font produced systematic artifacts in extracted text (for example dependent vowel signs rendered with extra characters), so rule wording and examples were decoded by the author from the readable parts. The PDF pages were not visually rendered here (no renderer installed). The decoded examples in section 3.2 and 3.5.3 are therefore adapted from this source with that caveat."
- "Prescriptive standard for official and educational Hindi, not a description of attested usage or of how people spell their own names."
- "Does not give a rule for how personal names must be spelled in general; section 3.11.2 only addresses South Indian names."
- "A landing page for the standard on the same host was also read (fetch of the HTML page succeeded only with certificate verification disabled, so only the PDF is used as evidence)."
```

## HIN-S002

```yaml
id: HIN-S002
title: "The Unicode Standard, Version 16.0, Chapter 12 South and Central Asia-I (Devanagari, section 12.1)"
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-12/
accessed: '2026-10-04'
source_type: standard
language_scope:
- hi-IN
- hi
relevant_locators:
- "12.1 Devanagari, Combining Marks (nukta U+093C, virama U+094D, candrabindu U+0901, anusvara U+0902)"
- "Explicit virama and half-consonants (ZERO WIDTH NON-JOINER and ZERO WIDTH JOINER after a virama)"
- "Punctuation (U+0964 DEVANAGARI DANDA, U+0965) and Digits (U+0966..U+096F)"
reuse_terms: "Unicode Terms of Use; linked and paraphrased only; terms not re-verified."
limitations:
- "Fetch summary only: the fetch tool returned a model-generated summary, not the page text. The summary's statements about nukta, virama, ZWJ/ZWNJ, candrabindu and anusvara, danda and digits were consistent with Unicode character names and properties checked locally (HIN-S004). A summary statement about U+0958..U+095F being Sindhi implosive letters was inconsistent with the local character names and is not used."
- "Describes encoding and rendering, not name recognition or Hindi orthography."
```

## HIN-S003

```yaml
id: HIN-S003
title: "Unicode Standard Annex #15: Unicode Normalization Forms"
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://www.unicode.org/reports/tr15/
accessed: '2026-10-04'
source_type: standard
language_scope:
- hi
relevant_locators:
- "Section 5.1 Composition exclusion, script-specific exclusions (U+0958 DEVANAGARI LETTER QA given as the example; nukta-bearing Devanagari, Bangla, Gurmukhi and Odia characters)"
reuse_terms: "Unicode Terms of Use; linked and paraphrased only."
limitations:
- "Fetch summary only (model-generated summary of the page, not the page text). The central claim, that excluded characters do not occur in NFD, NFC, NFKD or NFKC output, was confirmed independently by local computation (HIN-S004)."
- "Normalization policy for NER is not defined by this source."
```

## HIN-S004

```yaml
id: HIN-S004
title: "Python 3 unicodedata module, Unicode Character Database 16.0.0 (local check)"
authors_or_institution:
- Python Software Foundation (module); Unicode Consortium (data)
publication_date: null
url_or_identifier: "unicodedata.unidata_version == '16.0.0' in the Python 3 interpreter on the research machine, run 2026-10-04"
accessed: '2026-10-04'
source_type: other
language_scope:
- hi
relevant_locators:
- "normalize('NFC'/'NFD') and name() applied to U+0958..U+095F, U+0929, U+0931, U+0934, U+0901, U+0902, U+094D, U+200C, U+200D, U+0964, U+0966..U+096F"
reuse_terms: "Computation by the dossier author; no third-party text reproduced."
limitations:
- "A single implementation and data version. Other runtimes may ship older or newer Unicode data, which is itself a reason to record the version in fixtures."
- "Shows what the algorithm does to specified strings; it does not show how names are typed or stored in any corpus."
```

## HIN-S005

```yaml
id: HIN-S005
title: "HiNER: A Large Hindi Named Entity Recognition Dataset"
authors_or_institution:
- Rudra Murthy
- Pallab Bhattacharjee
- Rahul Sharnagat
- Jyotsana Khatri
- Diptesh Kanojia
- Pushpak Bhattacharyya
publication_date: null
url_or_identifier: https://aclanthology.org/2022.lrec-1.475 (arXiv:2204.13743v1)
accessed: '2026-10-04'
source_type: corpus
language_scope:
- hi-IN
relevant_locators:
- "Section 1 (listed challenges: no capitalization, ambiguity, spelling variation, free word order; the Pushpa example)"
- "Section 3 (guidelines follow CoNLL-2003; 11 tags; single annotator; ILCI tourism and news domains), Table 1 and Table 3"
- "Section 3.4 and Table 4 (annotation ambiguity examples)"
- "Section 5 (error analysis: most errors are named entities tagged as non-entities, then B-/I- boundary confusion)"
reuse_terms: "Paper: Creative Commons Attribution 4.0 (ACL Anthology statement for 2022 papers). Dataset terms were not verified."
limitations:
- "Full arXiv text read through a text extractor; Devanagari examples in the extraction were garbled, so no Devanagari example is taken from this paper. English transliterations of examples and prose were read."
- "Month is stated as June 2022 (LREC, Marseille); day unknown, so publication_date is left null."
- "Single annotator and no inter-annotator agreement, as the paper states. The paper reports no explicit rule on honorifics, titles or postpositions inside PERSON spans in the sections read."
- "Annotation choices of one dataset; not a linguistic authority."
```

## HIN-S006

```yaml
id: HIN-S006
title: "UD Hindi HDTB treebank page, Universal Dependencies"
authors_or_institution:
- Universal Dependencies contributors (Hindi Dependency Treebank from IIIT Hyderabad, automatically converted)
publication_date: null
url_or_identifier: https://universaldependencies.org/treebanks/hi_hdtb
accessed: '2026-10-04'
source_type: corpus
language_scope:
- hi-IN
relevant_locators:
- "Summary: size and genre; conversion note; license; statistics; case values; ADP examples"
reuse_terms: "Page reports CC BY-NC-SA 4.0 for the treebank (via fetch summary); not re-verified."
limitations:
- "Fetch summary only. It reported news genre, 16,649 sentences and 351,704 tokens, case postpositions such as ने, को, का, की as separate ADP tokens, and PROPN used for person, place and organization names. Counts and wording are not independently confirmed."
- "UD word units are an annotation design and do not define PERSON spans."
```

## HIN-S007

```yaml
id: HIN-S007
title: "Shared Task on Named Entity Recognition for South Asian Languages (tutorial slides, NLPAI Machine Learning Contest 2007)"
authors_or_institution:
- Anil Kumar Singh, Language Technologies Research Centre, IIIT Hyderabad
publication_date: null
url_or_identifier: https://cdn.iiit.ac.in/cdn/ltrc.iiit.ac.in/ner-ssea-08/NER-SAL-TUT.pdf
accessed: '2026-10-04'
source_type: corpus
language_scope:
- hi
relevant_locators:
- "Slides on the twelve-class tagset (NEP person, NETP title-person, NED designation), maximal entity and no nesting in manual annotation, nested output expected"
- "Slide with the romanized example 'saba aanand hii aanand hai'"
reuse_terms: "Unknown; paraphrased only."
limitations:
- "Slides, 26 pages; the page text was read in full but formatting and slide order are lost in extraction. Date is inferred only from the slide's contest label (2007), not from publication metadata."
- "The slides cover several South Asian languages. This dossier uses them only for the annotation scheme as described for the shared task, not for any claim about languages other than Hindi."
- "The IJCNLP-08 workshop proceedings (ACL Anthology I08-5) were located by search but not read."
```

## HIN-S008

```yaml
id: HIN-S008
title: "Named Entity Recognition for Hindi-English Code-Mixed Social Media Text"
authors_or_institution:
- Vinay Singh
- Deepanshu Vijay
- Syed S. Akhtar
- Manish Shrivastava
publication_date: '2018-07-20'
url_or_identifier: https://aclanthology.org/W18-2405/
accessed: '2026-10-04'
source_type: corpus
language_scope:
- hi-Latn
- hi
relevant_locators:
- "Section 3 Corpus and Annotation (tweets, Roman-script code-mixed only; Devanagari-only and English-only tweets removed)"
- "Section 3.1 (Per tag covers names, handles and nicknames; example T3 'modi/B-Per ji/I-Per na/Other')"
- "Section on features (capitalization feature in Roman script) and error analysis (hashtag forms such as #Modi / gi)"
reuse_terms: "ACL Anthology paper; CC BY terms assumed for 2018 papers but not verified for this PDF; dataset terms not verified."
limitations:
- "Full text read (9 pages). Twitter 2010s political and sports domain; romanized only, so it says nothing about Devanagari text."
- "Date from the proceedings footer (July 20, 2018)."
- "The reported scores are not used here."
```

## HIN-S009

```yaml
id: HIN-S009
title: "COMI-LINGUA: Expert Annotated Large-Scale Dataset for Multitask NLP in Hindi-English Code-Mixing"
authors_or_institution:
- Rajvee Sheth
- Himanshu Beniwal
- Mayank Singh
publication_date: '2025-09-17'
url_or_identifier: arXiv:2503.21670v3 (https://arxiv.org/abs/2503.21670)
accessed: '2026-10-04'
source_type: corpus
language_scope:
- hi-Latn
- hi
relevant_locators:
- "Abstract; Section on tasks (NER entity types in Table 1; machine translation into Standard English, Romanized Hindi and Devanagari Hindi)"
reuse_terms: "Not verified."
limitations:
- "Preprint (version 3, date from the arXiv stamp). Only the abstract and the task and schema description were read closely; results and annotation guideline appendices were not."
- "Its entity types include Hashtags, Mentions and Emoji beside Person; treat as a schema comparison, not a PERSON definition."
- "The paper describes both Romanized and Devanagari Hindi outputs for translation; this record does not establish the script of its NER annotations."
```

## HIN-S010

```yaml
id: HIN-S010
title: "ALA-LC Romanization Tables: Hindi (2025 version)"
authors_or_institution:
- Library of Congress Cataloging Policy and Support Office; American Library Association
publication_date: null
url_or_identifier: https://www.loc.gov/catdir/cpso/romanization/hindi.pdf
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- hi-IN
relevant_locators:
- "Table and Notes 2-5 (inherent a supplied unless a vowel sign or virama; dotted nukta letters bracketed as Urdu-origin; anusvara rendered by a homorganic nasal or m; anunasika as n̐ or m̐)"
reuse_terms: "Library of Congress publication; reuse terms not verified. Paraphrased only."
limitations:
- "Full two-page text read. Cataloguing scheme, not a spelling standard for personal names in daily use. ISO 15919 and IAST were not read at the primary standard; they appear in this dossier only as unverified names to check."
- "The extracted table had a few combining-mark rendering artifacts; only the Notes were relied on."
```

## HIN-S011

```yaml
id: HIN-S011
title: "Supervised Grapheme-to-Phoneme Conversion of Orthographic Schwas in Hindi and Punjabi"
authors_or_institution:
- Aryaman Arora
- Luke Gessler
- Nathan Schneider
publication_date: '2020-07-05'
url_or_identifier: https://aclanthology.org/2020.acl-main.696
accessed: '2026-10-04'
source_type: paper
language_scope:
- hi-IN
relevant_locators:
- "Abstract and Section 1 (whether an orthographic schwa is pronounced is hard to predict; a word-final deletion rule is reliable only as a rough rule)"
reuse_terms: "Creative Commons Attribution 4.0 (ACL Anthology)."
limitations:
- "Opening pages read only (abstract, Introduction). Date is the conference start date in the proceedings header (July 5-10, 2020)."
- "About pronunciation of common vocabulary, not names or romanization conventions. It supports only that Devanagari-to-Roman mapping is not a deterministic letter mapping."
```

## HIN-S012

```yaml
id: HIN-S012
title: "Personal names around the world"
authors_or_institution:
- W3C Internationalization Activity
publication_date: null
url_or_identifier: https://www.w3.org/International/questions/qa-personal-names
accessed: '2026-10-04'
source_type: other
language_scope:
- hi
relevant_locators:
- "Sections on given name plus patronymic (mentions parts of Southern India) and on name order"
reuse_terms: "W3C document license; paraphrased only."
limitations:
- "General guidance. The Indian content seen concerns Southern India, not the Hindi-speaking north, so it supports only the claim that single-pattern 'given plus family name' assumptions fail in India generally."
- "Page text was downloaded and searched for India and patronymic passages, not read in full."
```

## HIN-S013

```yaml
id: HIN-S013
title: "Indian name (English Wikipedia)"
authors_or_institution:
- Wikipedia contributors
publication_date: null
url_or_identifier: https://en.wikipedia.org/wiki/Indian_name
accessed: '2026-10-04'
source_type: other
language_scope:
- hi
relevant_locators:
- "Section on North India / Hindi belt (first-middle-surname pattern; Sharma, Singh, Kumar; -ji; Shri and Smt; Devi and Kumari)"
reuse_terms: "CC BY-SA; paraphrased only."
limitations:
- "Tertiary source and a research lead only. Fetch summary only. The summary said the section cites a single UK government naming guide; that citation was not obtained. Do not treat as independent corroboration."
- "A fetch summary stated that women in rural areas adopt Devi or Kumari at marriage. This conflicts in emphasis with the dossier's expectation that कुमारी also appears as a title or in given names of unmarried women. The disagreement is unresolved and recorded in person-names.md."
```
