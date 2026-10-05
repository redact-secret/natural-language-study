# Spanish: sources

Accessed 2026-10-04. Publication dates are unknown unless stated; search crawl dates are not publication dates. **Access caveat:** the RAE site (rae.es, dle.rae.es) returned HTTP 403 to every direct fetch attempt (WebFetch and curl). Records SPA-S001 to SPA-S005 and SPA-S014 are therefore supported only by search-result excerpts of the named pages, which this author did not read in full; section numbers are not verified. Their claims are labelled accordingly in findings and should be re-checked against the live pages. SPA-S006 to SPA-S013 were fetched, but several fetches returned a model-generated summary of the page rather than raw text; locators are as reported by that summary. No source is a measured NER result.

## SPA-S001

```yaml
id: SPA-S001
title: "mayúsculas (Diccionario panhispánico de dudas)"
authors_or_institution:
- Real Academia Española
- Asociación de Academias de la Lengua Española
publication_date: null
url_or_identifier: https://www.rae.es/dpd/may%C3%BAsculas
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- es
- es-ES
relevant_locators:
- 'Search-result excerpt only: capitalization of anthroponyms, preposition or preposition plus article in surnames (anchor #431 appeared in a search result; section number unverified)'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Page not fetched (HTTP 403); claim relies on a search excerpt reporting that such particles are lowercase after a given name and capitalized when the given name is omitted.
- Normative guidance, not a description of how individuals spell their own names or how news text capitalizes them.
```

## SPA-S002

```yaml
id: SPA-S002
title: "Alfabetización de antropónimos (Ortografía de la lengua española)"
authors_or_institution:
- Real Academia Española
- Asociación de Academias de la Lengua Española
publication_date: null
url_or_identifier: https://www.rae.es/ortograf%C3%ADa/alfabetizaci%C3%B3n-de-antrop%C3%B3nimos
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- es
relevant_locators:
- 'Search-result excerpt only: first surname is the ordering axis; preceding de, del, de la are disregarded when alphabetizing and written lowercase after the given name (e.g. Torre Ibarra, Ramón de la)'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Page not fetched (HTTP 403); excerpt only.
- Concerns alphabetical ordering of lists; it says nothing about NER span policy.
```

## SPA-S003

```yaml
id: SPA-S003
title: "Uso de la tilde y las mayúsculas en las abreviaturas (Ortografía de la lengua española)"
authors_or_institution:
- Real Academia Española
- Asociación de Academias de la Lengua Española
publication_date: null
url_or_identifier: https://www.rae.es/ortograf%C3%ADa/uso-de-la-tilde-y-las-may%C3%BAsculas-en-las-abreviaturas
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- es
relevant_locators:
- 'Search-result excerpt only: abbreviations of treatment formulas (Sr., D., Ud., Ilmo.) are written with initial capital; abbreviations keep a tilde when they include the accented vowel'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Page not fetched (HTTP 403); excerpt only.
- Dña. and Lic. were not seen in the excerpt; their treatment here is unsourced.
```

## SPA-S004

```yaml
id: SPA-S004
title: "Tilde en las mayúsculas (Español al día)"
authors_or_institution:
- Real Academia Española
publication_date: null
url_or_identifier: https://www.rae.es/espanol-al-dia/tilde-en-las-mayusculas
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- es
relevant_locators:
- 'Search-result excerpt only: capital letters take the tilde whenever the accentuation rules require it'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Page not fetched (HTTP 403); excerpt only.
- Normative rule; says nothing about how often accents are dropped in real text.
```

## SPA-S005

```yaml
id: SPA-S005
title: "complemento directo con a personal, complemento directo preposicional (Glosario de términos gramaticales)"
authors_or_institution:
- Real Academia Española
- Asociación de Academias de la Lengua Española
publication_date: null
url_or_identifier: https://www.rae.es/gtg/complemento-directo-con-a-personal-complemento-directo-preposicional
accessed: '2026-10-04'
source_type: grammar
language_scope:
- es
relevant_locators:
- 'Search-result excerpt only: direct objects with an animate, specific referent are usually marked with a; animate but non-specific referents typically are not (Visitó a su abuela; Busco un buen fontanero)'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Page not fetched (HTTP 403); excerpt only. Exceptions and variation by variety were not seen.
- Describes grammar, not a mention-boundary rule; dative a is a separate use.
```

## SPA-S006

```yaml
id: SPA-S006
title: "Ley 20/2011, de 21 de julio, del Registro Civil (BOE-A-2011-12628)"
authors_or_institution:
- Jefatura del Estado (Spain), published in the Boletín Oficial del Estado
publication_date: '2011-07-22'
url_or_identifier: https://www.boe.es/buscar/act.php?id=BOE-A-2011-12628
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- es-ES
relevant_locators:
- 'Article 49 (nombre y apellidos): parents agree the order of transmission of their first surnames; the preposition de and the conjunctions y or i may appear between surnames'
reuse_terms: Official legislative text; reuse terms not verified. Paraphrased only.
limitations:
- The fetch returned a summary of the page; the article number and the quoted fragments were not checked against raw text. Publication date 22 July 2011 is as reported in search results.
- Spanish state law; regional registers and later amendments were not checked. Not representative of other countries.
```

## SPA-S007

```yaml
id: SPA-S007
title: "Código Civil y Comercial de la Nación (Ley 26.994), articles 62-70"
authors_or_institution:
- Argentine Republic, via argentina.gob.ar normative database
publication_date: null
url_or_identifier: https://www.argentina.gob.ar/normativa/nacional/ley-26994-235975/texto
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- es-AR
relevant_locators:
- 'Article 67: either spouse may opt to use the other spouse''s surname with the preposition de or without it'
reuse_terms: Official legislative text; reuse terms not verified. Paraphrased only.
limitations:
- The fetch returned a summary; the article text was not checked against raw text. Consolidated-text currency and amendments were not checked.
- Argentina only; says nothing about Mexico, Spain or common social practice.
```

## SPA-S008

```yaml
id: SPA-S008
title: "UD Spanish: Tokenization and Word Segmentation"
authors_or_institution:
- Universal Dependencies contributors
publication_date: null
url_or_identifier: https://universaldependencies.org/es/index.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- es
relevant_locators:
- 'Tokenization and Word Segmentation: multiword tokens for contractions (al = a + el, del = de + el) and enclitic pronouns (hacerlo)'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Fetch returned a summary. Treebank annotation convention, not an orthographic norm or a PERSON span contract.
```

## SPA-S009

```yaml
id: SPA-S009
title: "UD Spanish-AnCora treebank page"
authors_or_institution:
- Universal Dependencies contributors
publication_date: null
url_or_identifier: https://universaldependencies.org/treebanks/es_ancora/index.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- es-ES
relevant_locators:
- 'Summary statistics: news genre; 12,557 multiword tokens including del; PROPN present, no dedicated NER layer; licence reported as CC BY 4.0'
reuse_terms: Reported CC BY 4.0 with inherited-licence note; verify before any reuse.
limitations:
- Fetch returned a summary; figures not independently checked. Newswire domain only. This study did not read the treebank data.
```

## SPA-S010

```yaml
id: SPA-S010
title: "UD Spanish-GSD treebank page"
authors_or_institution:
- Universal Dependencies contributors
publication_date: null
url_or_identifier: https://universaldependencies.org/treebanks/es_gsd/index.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- es
relevant_locators:
- 'Summary statistics: blog, news, reviews, wiki genres; 8,236 multiword tokens (del, al, enclitic forms); licence reported as CC BY-SA 4.0'
reuse_terms: Reported CC BY-SA 4.0; verify before any reuse.
limitations:
- Fetch returned a summary; figures not independently checked. This study did not read the treebank data.
```

## SPA-S011

```yaml
id: SPA-S011
title: "UD relation: flat"
authors_or_institution:
- Universal Dependencies contributors
publication_date: null
url_or_identifier: https://universaldependencies.org/u/dep/flat.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- es
relevant_locators:
- 'Names; Flat vs. non-flat names'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Cross-linguistic guideline, not Spanish-specific. Dependency structure is not a PERSON span definition.
```

## SPA-S012

```yaml
id: SPA-S012
title: "Unicode Normalization Forms (UAX #15)"
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://www.unicode.org/reports/tr15/
accessed: '2026-10-04'
source_type: standard
language_scope:
- es
relevant_locators:
- 'Canonical equivalence; Normalization Forms NFC and NFD (precomposed versus combining sequences)'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- The fetch summary used a cedilla example; the Spanish acute and tilde cases are this author's application of the same principle. Not a NER or accent-restoration policy.
```

## SPA-S013

```yaml
id: SPA-S013
title: "Introduction to the CoNLL-2002 Shared Task: Language-Independent Named Entity Recognition"
authors_or_institution:
- Erik F. Tjong Kim Sang
publication_date: '2002-09-05'
url_or_identifier: https://arxiv.org/abs/cs/0209010
accessed: '2026-10-04'
source_type: paper
language_scope:
- es-ES
relevant_locators:
- 'Data description: Spanish newswire from the EFE News Agency, May 2000, annotated by TALP (UPC) and CLiC (UB); entities are non-recursive and non-overlapping, with only the top-level entity marked when nested'
reuse_terms: Paper reuse terms not verified; corpus redistribution not assessed.
limitations:
- Text was extracted from the arXiv PDF with a library and read only for the data-description passage; the arXiv v1 date is used as publication date (conference proceedings pages 155-158 per the arXiv listing).
- Newswire from one month; says nothing about personal-name conventions beyond annotation scope.
```

## SPA-S014

```yaml
id: SPA-S014
title: "El artículo en los nombres propios (Ortografía de la lengua española)"
authors_or_institution:
- Real Academia Española
- Asociación de Academias de la Lengua Española
publication_date: null
url_or_identifier: https://www.rae.es/ortograf%C3%ADa/el-art%C3%ADculo-en-los-nombres-propios
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- es
relevant_locators:
- 'Search-result excerpt only: when El is part of a capitalized proper name, the contraction with a or de is not written (a El Salvador, de El País); for nicknames such as El Greco the article is lowercase and contracts (al Greco)'
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Page not fetched (HTTP 403); excerpt only. A search excerpt supplied the examples; they were not read in context.
- Normative; real text may contract anyway, and no frequency is claimed.
```
