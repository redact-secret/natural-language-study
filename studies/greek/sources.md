# Greek: sources

Accessed 2026-10-04. Publication dates are unknown unless stated; search crawl dates are not publication dates. **Access caveat:** most pages were read through a summarizing WebFetch that returns a model-written summary rather than raw text, so locators are as reported and quoted wording is not verified. Several sources are community-edited secondary pages (Wikipedia, Wiktionary) and are leads, not authorities. No source is a measured NER result.

## GRE-S001

```yaml
id: GRE-S001
title: "UD for Greek (language overview and guidelines)"
authors_or_institution:
- Universal Dependencies contributors
publication_date: null
url_or_identifier: https://universaldependencies.org/el/index.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- el
- el-GR
relevant_locators:
- "Tokenization and Word Segmentation; Morphology (case); abbreviations; multiword tokens such as στον = σ + τον"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Read through a summarizing fetch, not raw text; locators as reported by the summary."
- "Annotation conventions, not an entity-boundary policy; a deeper tokenization page (universaldependencies.org/el/overview/tokenization.html) returned HTTP 404."
- "Whether UD Greek has a separate documented rule for apostrophe elision was not established."
```

## GRE-S002

```yaml
id: GRE-S002
title: "UD Greek GDT treebank page"
authors_or_institution:
- Universal Dependencies contributors
publication_date: null
url_or_identifier: https://universaldependencies.org/treebanks/el_gdt/index.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- el
- el-GR
relevant_locators:
- "Summary statistics: 2,521 sentences, 61,673 tokens, 63,441 syntactic words; 1,668 multiword tokens; genre and license lines"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Read through a summarizing fetch; figures are as reported by the summary and were not recounted."
- "PROPN tagging without dedicated NER annotation, so it gives no PERSON span policy."
- "Genre is news, wiki and spoken-derived text; not a representative corpus of names."
```

## GRE-S003

```yaml
id: GRE-S003
title: "UnicodeData.txt (Unicode Character Database)"
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://www.unicode.org/Public/UNIDATA/UnicodeData.txt
accessed: '2026-10-04'
source_type: standard
language_scope:
- el
- el-GR
relevant_locators:
- "Entries for U+0384, U+0385, U+0386, U+03AC, U+03C2, U+03C3, U+037E, U+0387, U+0375"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Lines were returned by a summarizing fetch and then re-checked with Python 3.14.7 unicodedata (Unicode 16.0.0) for normalization behavior; the raw file was not read directly."
- "Character properties, not an orthographic or NER policy."
- "Unicode chapter 7 (Europe I) PDF was fetched but could not be extracted, so no prose from the core specification is cited."
```

## GRE-S004

```yaml
id: GRE-S004
title: "SpecialCasing.txt (Unicode Character Database)"
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://www.unicode.org/Public/UNIDATA/SpecialCasing.txt
accessed: '2026-10-04'
source_type: standard
language_scope:
- el
- el-GR
relevant_locators:
- "Line for U+03A3 with the Final_Sigma condition; entries for U+0390 and U+03B0"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Read through a summarizing fetch of the file; line text as reported."
- "Describes default full case mapping, not Greek orthographic practice for capitals."
```

## GRE-S005

```yaml
id: GRE-S005
title: "Romanization of Greek"
authors_or_institution:
- Wikipedia contributors
publication_date: null
url_or_identifier: https://en.wikipedia.org/wiki/Romanization_of_Greek
accessed: '2026-10-04'
source_type: other
language_scope:
- el
- el-GR
relevant_locators:
- "Sections on ELOT 743 and ISO 843; official use on passports and identity documents; Greeklish"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Secondary encyclopedia page read through a summarizing fetch; a lead, not an authority."
- "Publication date and revision unknown; the page is community-edited."
- "Does not itself give the ELOT 743 text; see GRE-S013."
```

## GRE-S006

```yaml
id: GRE-S006
title: "Greek orthography"
authors_or_institution:
- Wikipedia contributors
publication_date: null
url_or_identifier: https://en.wikipedia.org/wiki/Greek_orthography
accessed: '2026-10-04'
source_type: other
language_scope:
- el
- el-GR
relevant_locators:
- "Monotonic orthography (1982); polytonic legacy; final sigma"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Secondary page read through a summarizing fetch; the summary reported that the page does not detail capital-letter accent conventions."
- "Revision unknown; use only as a lead for the date and shape of the reform."
```

## GRE-S007

```yaml
id: GRE-S007
title: "Greek diacritics"
authors_or_institution:
- Wikipedia contributors
publication_date: null
url_or_identifier: https://en.wikipedia.org/wiki/Greek_diacritics
accessed: '2026-10-04'
source_type: other
language_scope:
- el
- el-GR
relevant_locators:
- "Monotonic Greek: accents on capital letters; diaeresis retained in uppercase; 1982 reform"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Secondary page read through a summarizing fetch; the all-caps accent claim is a lead and needs an authoritative orthographic source."
- "Revision unknown."
```

## GRE-S008

```yaml
id: GRE-S008
title: "Modern Greek grammar"
authors_or_institution:
- Wikipedia contributors
publication_date: null
url_or_identifier: https://en.wikipedia.org/wiki/Modern_Greek_grammar
accessed: '2026-10-04'
source_type: other
language_scope:
- el
- el-GR
relevant_locators:
- "Noun declension examples (masculine -ος: άνθρωπος, ανθρώπου, άνθρωπο, άνθρωπε); accent shift in the genitive; definite article before proper names"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Secondary page read through a summarizing fetch; no section numbers captured."
- "Stands in for grammar access that failed: Holton et al. and Triantafyllidis texts were not accessible (see Attempted sources)."
```

## GRE-S009

```yaml
id: GRE-S009
title: "Greek name"
authors_or_institution:
- Wikipedia contributors
publication_date: null
url_or_identifier: https://en.wikipedia.org/wiki/Greek_name
accessed: '2026-10-04'
source_type: other
language_scope:
- el
- el-GR
relevant_locators:
- "Surname genitive forms for women; patronymic suffixes -opoulos, -idis; naming customs"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Secondary page read through a summarizing fetch."
- "Describes customs and historical practice; modern legal practice is separate. Does not establish how individuals choose to write their names."
```

## GRE-S010

```yaml
id: GRE-S010
title: "English Wiktionary entries Γιώργος, Παπαδόπουλος, Ελένη, Ζωή, Δάφνη"
authors_or_institution:
- Wiktionary contributors
publication_date: null
url_or_identifier: https://en.wiktionary.org/wiki/Γιώργος
accessed: '2026-10-04'
source_type: other
language_scope:
- el
- el-GR
relevant_locators:
- "Γιώργος: inflection table; Παπαδόπουλος: etymology, declension, feminine form; Ελένη, Ζωή, Δάφνη: senses and declension"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Community-edited lexicon pages read through a summarizing fetch; one summary contained a garbled accusative form for Παπαδόπουλος, which is not used here."
- "Other entry URLs follow the same pattern (https://en.wiktionary.org/wiki/Παπαδόπουλος, https://en.wiktionary.org/wiki/Ελένη, https://en.wiktionary.org/wiki/Ζωή, https://en.wiktionary.org/wiki/Δάφνη)."
- "Fetches for Άνθος, Ελπίδα and Αγάπη returned HTTP 404, so those words have no lexical verification here."
- "Not a prescriptive dictionary; frequency and register not given."
```

## GRE-S011

```yaml
id: GRE-S011
title: "All Greek to me! An automatic Greeklish to Greek transliteration system"
authors_or_institution:
- Aimilios Chalamandaris
- Athanassios Protopapas
- Pirros Tsiakoulis
- Spyros Raptis
publication_date: null
url_or_identifier: https://aclanthology.org/L06-1229/
accessed: '2026-10-04'
source_type: paper
language_scope:
- el
- el-GR
relevant_locators:
- "Abstract (ACL Anthology page): Greeklish is not standardized and competing conventions coexist"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Only the abstract page was read, via a summarizing fetch; the full paper and its consistency measurements were not read."
- "Published at LREC 2006 (May 2006, Genoa); usage patterns may have changed since."
```

## GRE-S012

```yaml
id: GRE-S012
title: "Datasets and Performance Metrics for Greek Named Entity Recognition (elNER) repository"
authors_or_institution:
- Nikolaos Bartziokas
- Thanassis Mavropoulos
- Constantine Kotropoulos
publication_date: null
url_or_identifier: https://github.com/nmpartzio/elNER
accessed: '2026-10-04'
source_type: corpus
language_scope:
- el
- el-GR
relevant_locators:
- "README: elNER-4 and elNER-18 newswire annotation, PERSON type, license, citation to SETN 2020 (DOI 10.1145/3411408.3411437)"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "README read through a summarizing fetch; the paper itself and the data were not read or inspected."
- "License reported as CC BY-NC-SA 4.0; no Greek-specific span policy documented in the README."
- "Reported in a search snippet only: PERSON F1 94.63 with spaCy; not verified and not used as evidence."
```

## GRE-S013

```yaml
id: GRE-S013
title: "ΕΛΟΤ 743.0 catalogue record (Transcription of hellenic alphabet with latin characters)"
authors_or_institution:
- Hellenic Organization for Standardization (ELOT)
publication_date: null
url_or_identifier: https://eshop.elot.gr/en/product/63894
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- el
- el-GR
relevant_locators:
- "Catalogue record: published 1993-08-17 per page, withdrawn 2001-05-04, replaced by ΕΛΟΤ 743 Ε2:2001, ISO 843 equivalent"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Catalogue metadata only, via a summarizing fetch; the standard text is paywalled and was not read, so no ELOT 743 letter-by-letter rule is claimed in this dossier."
- "The page refers to the older 743.0 record, not the 2001 edition."
```

## GRE-S014

```yaml
id: GRE-S014
title: "Απόφαση Α.Π.Δ.Π.Χ. 2368/2003 (ΦΕΚ 1562/Β/22-10-2003)"
authors_or_institution:
- Hellenic Data Protection Authority (as listed on e-nomothesia.gr)
publication_date: null
url_or_identifier: https://www.e-nomothesia.gr/kat-deltia-tautotetos/2368-2003.html
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- el
- el-GR
relevant_locators:
- "Decision text on Latin-character transcription of names on identity cards and consistency with earlier records (point numbers as reported by the summary)"
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- "Read through a summarizing fetch of a legal aggregator page; point numbers unverified."
- "Dated 2003; later legal changes (a search snippet mentioned a 2011 provision) were not read."
- "Concerns official documents, not informal writing."
```

## Attempted sources not used

- Holton, Mackridge, Philippaki-Warburton and Spyropoulos, *Greek: A Comprehensive Grammar of the Modern Language* (Routledge; a search result listed a 1997 first edition and a 2011/2012 second edition): only catalogue metadata appeared in search snippets; the text was not accessed and nothing in this dossier is cited to it.
- Triantafyllidis, *Μικρή Νεοελληνική Γραμματική* (Institute of Modern Greek Studies, Aristotle University of Thessaloniki): search found only book-review pages on greek-language.gr, not the grammar text, so no claim here rests on it.
- Unicode Standard chapter 7 PDF (Unicode 15.0): fetched but unreadable in the available tooling.
- greek-language.gr vocative PDF (repository-edulll.ekt.gr, 998_06_KLHTIKH.pdf): fetched as binary, likely scanned; not readable here.
- ΕΛΟΤ 743 Ε2:2001 text and Ministry of Interior (ypes.gr) documents: paywalled or HTTP 403.
- Qualified Greek-speaker review: none recorded.
