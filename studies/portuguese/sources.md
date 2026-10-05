# Portuguese: sources

Accessed 2026-10-04 unless stated. Publication dates are given only when the source states them; search-result crawl dates are not publication dates. Each record states what was actually read. No source here is a measured NER result. Fetches of some official Brazilian legislation pages failed (connection reset), so POR-S010 is a search-excerpt lead only.

## POR-S001

```yaml
id: POR-S001
title: Acordo Ortográfico da Língua Portuguesa (1990), text of approval instrument and Anexo I Bases (copy hosted by APEL)
authors_or_institution:
- Signatory states of the Acordo (Angola, Brasil, Cabo Verde, Guiné-Bissau, Moçambique, Portugal, São Tomé e Príncipe); copy hosted by APEL
publication_date: '1990-12-16'
url_or_identifier: https://www.apel.pt/wp-content/uploads/2023/02/AcordoOrtogrLinguaPortug.pdf
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- pt-PT
- pt-BR
relevant_locators:
- 'Base XI 3º (facultative accent: António/Antônio)'
- 'Base XVII 1º and Obs. 2 (hyphen in enclisis and tmesis; eis-me)'
- 'Base XIX 1º f) and 2º a) (lowercase axionyms; capital in anthroponyms; Branca de Neve)'
- 'Base XXI (signatures: a person may keep the spelling adopted by custom or legal registration)'
reuse_terms: Treaty/official text; short quotations only; redistribution terms of the APEL copy not verified.
limitations:
- 'Text read from a PDF copy; the PDF text extraction shows a few OCR-like artifacts, so wording was checked only for the passages cited.'
- Normative spelling, not attested usage. Dates of national entry into force and the 2009 timeline are not established by this text and were not verified in this study.
- The Bases do not state a rule for lowercase particles inside surnames; only example forms (for example Joaquim da Silva) are evidence of practice.
```

## POR-S002

```yaml
id: POR-S002
title: Pedir a atribuição de nome no nascimento (gov.pt service page)
authors_or_institution:
- Portuguese Government / Instituto dos Registos e do Notariado (service page on gov.pt)
publication_date: null
url_or_identifier: https://www.gov.pt/servicos/pedir-a-atribuicao-de-nome-no-nascimento
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- pt-PT
relevant_locators:
- Name composition rules (maximum of six grammatical words, at most two of them the proper name; names Portuguese or adapted; no doubt about sex)
reuse_terms: Paraphrase and short quote only; terms not verified.
limitations:
- Page states "Last Updated 27.03.2026" (observed in fetch). Applies to registration in Portugal and does not describe naming outside the register.
- The underlying statute (Código do Registo Civil) was not read directly.
- Does not cover Brazil.
```

## POR-S003

```yaml
id: POR-S003
title: UD for Portuguese (language documentation), Tokenization and Word Segmentation
authors_or_institution:
- Universal Dependencies contributors
publication_date: null
url_or_identifier: https://universaldependencies.org/pt/index.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- pt-PT
- pt-BR
relevant_locators:
- Tokenization and Word Segmentation (contractions such as do = de+o and pelo = por+o; hyphenated compounds; mesoclisis and enclisis as multiword tokens)
reuse_terms: Linked and paraphrased only; terms not verified.
limitations:
- Annotation conventions for syntactic words. They are not PERSON span rules.
- The page itself says hyphenated words are currently treated inconsistently, so corpus-level behavior varies across Portuguese treebanks.
```

## POR-S004

```yaml
id: POR-S004
title: UD Portuguese-Bosque, relation flat:name
authors_or_institution:
- Universal Dependencies contributors (treebank documentation page)
publication_date: null
url_or_identifier: https://universaldependencies.org/treebanks/pt_bosque/pt_bosque-dep-flat-name.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- pt-PT
- pt-BR
relevant_locators:
- Statistics (5,652 instances; 97% PROPN-PROPN) and examples with intervening DA, e and a
reuse_terms: Treebank documentation linked only; corpus license not verified.
limitations:
- Documents a syntactic annotation choice; the examples show that function words occur inside multiword proper names in this treebank but do not give a rate for personal names versus organizations or titles.
- The cited example text (an upper-case personal name and an organization name) was read through the fetch summary, not the underlying CoNLL-U data.
```

## POR-S005

```yaml
id: POR-S005
title: UD Portuguese, PROPN part-of-speech page
authors_or_institution:
- Universal Dependencies contributors
publication_date: null
url_or_identifier: https://universaldependencies.org/pt/pos/PROPN.html
accessed: '2026-10-04'
source_type: corpus
language_scope:
- pt-PT
- pt-BR
relevant_locators:
- Multiword proper nouns paragraph (many proper nouns that are multiword expressions are not split)
reuse_terms: Linked and paraphrased only; terms not verified.
limitations:
- Page is brief and does not address titles or prepositions inside names; read through a fetch summary.
```

## POR-S006

```yaml
id: POR-S006
title: Forma de tratamento (Manual de Comunicação)
authors_or_institution:
- Senado Federal (Brasil), Secretaria de Comunicação Social
publication_date: null
url_or_identifier: https://www12.senado.leg.br/manualdecomunicacao/estilos/forma-de-tratamento
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- pt-BR
relevant_locators:
- Entries Senhor/Senhora, Doutor/Doutora, Dona/Seu, Dom, Pronomes de reverência
reuse_terms: Short attributed excerpts and original summaries only; rights retained.
limitations:
- Institutional house style for Brazilian news-style writing, not a general orthographic authority and not European usage. Example Dona Ivone Lara is the source's own example.
```

## POR-S007

```yaml
id: POR-S007
title: Rua D. Pedro V (Ciberdúvidas da Língua Portuguesa, consultório)
authors_or_institution:
- João Carreira Bom, answer published by Ciberdúvidas da Língua Portuguesa
publication_date: '1998-03-20'
url_or_identifier: https://ciberduvidas.iscte-iul.pt/consultorio/perguntas/rua-d-pedro-v/2025
accessed: '2026-10-04'
source_type: other
language_scope:
- pt-PT
relevant_locators:
- Whole answer (capital or lowercase for the common noun in street names; contemporary tendency toward lowercase)
reuse_terms: Linked and paraphrased only; terms not verified.
limitations:
- Dated 1998, before the Acordo came into force, and about public-place names rather than personal names. It does not decide the case of particles inside surnames. A search summary of other Ciberdúvidas pages about prepositions in names was not confirmed by reading those pages and is not used as evidence.
```

## POR-S008

```yaml
id: POR-S008
title: A Importância dos Falsos Homógrafos para a Correção Automática de Erros Ortográficos em Português
authors_or_institution:
- Magali Sanches Duran
- Lucas Vinícius Avanço
- Maria das Graças Volpe Nunes
publication_date: null
url_or_identifier: https://sol.sbc.org.br/index.php/stil/article/view/3989
accessed: '2026-10-04'
source_type: paper
language_scope:
- pt-BR
relevant_locators:
- Abstract (25,722 Portuguese word pairs differing only by an accent; 2,052 candidates for exclusion from spell-checker lexicons)
reuse_terms: Linked and summarized only; license not verified.
limitations:
- Only the abstract page was read, not the full PDF. Year shown by the venue: 2015 (STIL); exact date not read. Concerns common words, not personal names.
```

## POR-S009

```yaml
id: POR-S009
title: Priberam Dicionário, entries silva and rosa
authors_or_institution:
- Priberam Informática
publication_date: null
url_or_identifier: https://dicionario.priberam.org/silva
accessed: '2026-10-04'
source_type: other
language_scope:
- pt-PT
relevant_locators:
- 'silva: feminine noun senses (bramble shrubs, a verse form, archaic forest) and verb-form reading'
- 'rosa (https://dicionario.priberam.org/rosa): feminine noun (flower), masculine noun (colour), adjective, verb-form reading'
reuse_terms: Linked and paraphrased only; terms not verified.
limitations:
- Entries were read through a fetch summary. The silva entry as summarized has no proper-name sense, which does not show absence of the surname in use. Entries for Pereira, Costa, Barros, Ribeiro, Flor and Estrela were not checked.
```

## POR-S010

```yaml
id: POR-S010
title: Lei n.º 6.015/1973 art. 55 as amended by Lei n.º 14.382/2022 (Brazil, registration of names)
authors_or_institution:
- República Federativa do Brasil
publication_date: null
url_or_identifier: https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- pt-BR
relevant_locators:
- Art. 55 (nome = prenome plus sobrenomes)
reuse_terms: Unknown.
limitations:
- The official page could not be fetched (connection reset, several attempts). Only search-result excerpts were available, so the wording of art. 55 is a lead and is not quoted or relied on here beyond the general statement that a name has a prenome and sobrenomes and that Lei 14.382/2022 changed alteration procedures.
```

## POR-S011

```yaml
id: POR-S011
title: 'Pesquisas onomásticas sobre nomes não oficiais: Revisão sistemática de literatura'
authors_or_institution:
- Julia Machado (Universidade Estadual do Oeste do Paraná)
publication_date: null
url_or_identifier: https://e-revista.unioeste.br/index.php/onomastica/article/download/33919/24146/140011
accessed: '2026-10-04'
source_type: paper
language_scope:
- pt-BR
relevant_locators:
- Abstract and introduction (non-official names such as apelidos not registered at the civil registry; summaries of four works including football-player apelidos and ballot names)
reuse_terms: Journal article; short paraphrase only; license not verified.
limitations:
- Secondary literature review of four works in one database, journal volume dated 2025 (exact date not read). The reviewed primary works were not read. Not evidence of frequency of apelidos in running text.
```

## POR-S012

```yaml
id: POR-S012
title: 'UAX #15: Unicode Normalization Forms'
authors_or_institution:
- Unicode Consortium
publication_date: '2026-08-12'
url_or_identifier: https://www.unicode.org/reports/tr15/
accessed: '2026-10-04'
source_type: standard
language_scope:
- pt-PT
- pt-BR
relevant_locators:
- Introduction and Normalization Forms (canonical equivalence of precomposed and combining sequences; NFC, NFD)
reuse_terms: Linked and paraphrased only; terms not verified.
limitations:
- Version and date as shown on the page when fetched (Unicode 18.0.0). Says nothing about accent deletion, which is not a canonical equivalence.
```
