# Italian: naming practices, order, titles and particles

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis; independent review pending. NER proposals remain untested. Examples are **synthetic** (fictional people, repository MIT terms, author self-check only) unless marked attested.

## Research answer and basis

Question: which Italian name structures must a PERSON span accommodate?

- Order: given name before surname normally; public administration inverts [ITA-S001](sources.md#ita-s001), Posizione.
- Particles: lowercase in origin phrases such as da Vinci, capitalized where the particle is part of the surname (D'Eredità) [ITA-S001], Grafia; patronymic types with Di and De are listed by Treccani [ITA-S006](sources.md#ita-s006). See [ITA-002](findings/ITA-002.md).
- Titles: sig., sig.ra, dott., dott.ssa, prof. may be abbreviated; capitalization of professional titles is optional except high offices [ITA-S002](sources.md#ita-s002). See [ITA-003](findings/ITA-003.md).
- Law and practice: up to three given names [ITA-S010](sources.md#ita-s010); wife adds the husband's surname [ITA-S009](sources.md#ita-s009); children's double surname after 131/2022 per a commentary [ITA-S011](sources.md#ita-s011). See [ITA-006](findings/ITA-006.md).

## Contrasts that challenge the shortcut

| Original | Provenance | Question |
| --- | --- | --- |
| `Maria Chiara Ferrari` | synthetic | three-token fictional name; first two tokens are a compound given name |
| `Maria e Chiara Ferrari` | synthetic | two people |
| `FERRI Giulia` | synthetic | surname-first, upper-case surname |
| `Giulia Ferri in Rossi` | synthetic | a married-name form with `in`; the author knows this convention exists but no consulted source documents it, so treat it as an unverified lead |

## NER implication and handoff

Hypothesis: spans of two to four name tokens with internal particles and optional titles, without inferred legal roles, beat a fixed two-token pattern. Disposition: ready-for-owner-review; no result.

## Limits and next evidence

Compound given names (Gian Luca versus Gianluca) have no source here. Married-name forms with `in` or `ved.` and the identity-document practice for women's surnames are unverified. Name inventories and frequencies (for example from ANPR or Caffarelli and Marcato's dictionary) were not obtained. Dialectal and regional variants are out of scope. It-CH is not included because no Swiss source was examined.
