# Korean: sources

Accessed 2026-10-04. Publication dates are unknown unless stated; search crawl dates are not publication dates. Links and relevant publisher text were checked; no source is a measured NER result.

## KOR-S001

```yaml
id: KOR-S001
title: '한국어 어문 규범: 한글 맞춤법'
authors_or_institution:
- National Institute of Korean Language
publication_date: null
url_or_identifier: https://www.korean.go.kr/kornorms/m/m_regltn.do
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- ko-KR
relevant_locators:
- Chapter 5, articles 41 and 48 and their explanations
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- South Korean spelling standard, not observed error frequencies; relevant sections
  verified through indexed publisher text.
```

## KOR-S002

```yaml
id: KOR-S002
title: 'Unicode Normalization Forms (UAX #15)'
authors_or_institution:
- Unicode Consortium
publication_date: null
url_or_identifier: https://www.unicode.org/reports/tr15/
accessed: '2026-10-04'
source_type: standard
language_scope:
- ko-KR
relevant_locators:
- Introduction; Normalization Forms; Hangul composition/decomposition
reuse_terms: Linked and paraphrased only; redistribution terms not verified.
limitations:
- Canonical and compatibility equivalence; not a NER or transliteration policy.
```

## KOR-S003

```yaml
id: KOR-S003
title: 한국어 교육 문법·표현 내용 개발 연구(2단계)
authors_or_institution:
- 양명희 (research lead)
- 중앙대학교 산학협력단
- National Institute of Korean Language (commissioning institution)
publication_date: null
url_or_identifier: https://www.korean.go.kr/common/download.do;front=4EB4A3495E3CECFAC3FA69EB248A7A71?c_file_name=659df6e4-5eff-4d52-bad9-44e413adbfcf_0.pdf&file_path=reportData&o_file_name=%ED%95%9C%EA%B5%AD%EC%96%B4%EA%B5%90%EC%9C%A1+%EB%AC%B8%EB%B2%95%C2%B7%ED%91%9C%ED%98%84+%EB%82%B4%EC%9A%A9+%EA%B0%9C%EB%B0%9C+%EC%97%B0%EA%B5%AC(2%EB%8B%A8%EA%B3%84).pdf
accessed: '2026-10-04'
source_type: grammar
language_scope:
- ko-KR
relevant_locators:
- Printed pp. 152–154; PDF pp. 162–164; 이 section, 형태 정보 and 제약 정보
reuse_terms: Short attributed excerpts and original paraphrases only; no corpus redistribution.
limitations:
- Pedagogical constraints should not be generalized to all informal usage.
- Same commissioning institution as KOR-S001; not independent institutional corroboration.
bibliographic_note: Report 2013-01-49; submission dated 2013-12-15. Publication day
  not established.
```

## KOR-S004

```yaml
id: KOR-S004
title: 2022년 말뭉치 개체명 분석 및 개체 연결 사업
authors_or_institution:
- 차정원 (사업 책임자)
- 데이터리
- 한림대학교 산학협력단
- National Institute of Korean Language (commissioning institution)
publication_date: null
url_or_identifier: https://www.korean.go.kr/common/download.do?c_file_name=6cb5bfe5-a6e8-4bd1-8b4d-27bfb58ca3bb.pdf&file_path=reportData&o_file_name=report.pdf
accessed: '2026-10-04'
source_type: corpus
language_scope:
- ko-KR
relevant_locators:
- PDF page 149 of 488; guideline printed page 57; 바. 세부분류 개체명 정의 / 1. PERSON / 태깅
  단위 - 접미사 -이
reuse_terms: Brief attributed fragments only; report and corpus redistribution rights
  not assumed.
limitations:
- An external annotation contract, not an automatically adopted ner-evidence policy.
- Its PERSON umbrella includes character/pet subtypes; only the PS_NAME suffix boundary
  rule is used here.
- Shares commissioning institution with KOR-S003; a different artifact/evidence type,
  not independent institutional corroboration.
bibliographic_note: Report 2022-01-14; submitted 2022-11-25. Full original PDF downloaded;
  title pages and relevant page extracted with pypdf.
sha256: e6f65252f41474129b8985198f2aff8da526ab79cffbd70199a60f318046ba69
```

## KOR-S005

```yaml
id: KOR-S005
title: ner-evidence PERSON taxonomy 0.2.0
authors_or_institution:
- ner-evidence maintainers
publication_date: null
url_or_identifier: https://github.com/redact-secret/ner-evidence/blob/b10b325b54061f5a9c86e8542189723c58442831/taxonomy/person.taxonomy.json
accessed: '2026-10-04'
source_type: other
language_scope:
- ko-KR
relevant_locators:
- language_profiles[ko].conventions, lines 54–61; span_conventions, lines 65–69
reuse_terms: Project contract paraphrased; no evidence fixtures copied.
limitations:
- Engineering annotation policy, not a linguistic authority.
- Pinned commit b10b325b54061f5a9c86e8542189723c58442831; local tracked taxonomy matched
  HEAD. Unrelated untracked LICENSE file was present and untouched.
```

## KOR-S006

```yaml
id: KOR-S006
title: Romanization of Korean
authors_or_institution:
- National Institute of Korean Language
publication_date: null
url_or_identifier: https://www.korean.go.kr/front_eng/roman/roman_01.do
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- ko-KR
relevant_locators:
- Special Provisions (4), (7), (8)
reuse_terms: Short attributed excerpts and original summaries only; source rights
  retained.
limitations:
- Prescriptive transcription with established-name exceptions; not observed variant
  frequencies.
```

## KOR-S007

```yaml
id: KOR-S007
title: 홍길동 씨, 홍길동씨의 띄어쓰기
authors_or_institution:
- National Institute of Korean Language
publication_date: '2020-01-16'
url_or_identifier: https://korean.go.kr/front/mcfaq/mcfaqView.do?mcfaq_seq=9122&mn_id=217&pageIndex=12
accessed: '2026-10-04'
source_type: official-guidance
language_scope:
- ko-KR
relevant_locators:
- 'Answer: dependent noun 씨 versus surname/family suffix -씨'
reuse_terms: Short attributed excerpts and original summaries only; source rights
  retained.
limitations:
- Edited-language distinction; missing spaces in informal text need contextual review.
```
