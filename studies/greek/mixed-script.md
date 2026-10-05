# Greek: Official transliteration, Greeklish and look-alike letters are three different mixed-script problems

Scope: [dossier overview](overview.md). Status: source-backed desk synthesis, in-progress; independent review pending. NER proposals remain untested.

## Research answer and basis

Official romanization uses ELOT 743 (equivalent to ISO 843) on passports and identity documents per a secondary page ([GRE-S005](sources.md#gre-s005)); the ELOT catalogue record shows the 1993 edition withdrawn in 2001 and replaced by ΕΛΟΤ 743 Ε2:2001 ([GRE-S013](sources.md#gre-s013)); a 2003 Data Protection Authority decision stresses consistency with earlier records over strict conversion ([GRE-S014](sources.md#gre-s014), summary). Greeklish is informal and not standardized ([GRE-S011](sources.md#gre-s011), abstract only). Look-alike Greek and Latin capitals are distinct code points (verified locally; [GRE-S003](sources.md#gre-s003)). The canonical claim is [GRE-005](findings/GRE-005.md). Normalization within Greek script (NFC, NFD, U+0384) is in [GRE-004](findings/GRE-004.md); it is not script-mixing coverage.

## Contrasts that challenge the shortcut

| Original | Meaning | Question |
| --- | --- | --- |
| `Παπαδόπουλος` / `PAPADOPOULOS` | Fictional surname, two scripts | Same person, but a transliteration does not establish identity. |
| `Giorgos` / `Yiorgos` | Latin spellings of Γιώργος | Variation among writers. |
| `ΑΝΝΑ` / `ANNA` | Greek letters versus Latin letters | Same look, different strings. |
| `Ο Giorgos είπε` | Greek article, Latin name | Code-switched name; the article stays outside. |

All synthetic, author self-check only.

## NER decision and falsifiable handoff

Test degradation from Greek-script to Latin transliterations and homoglyph strings, with script-aware normalization for detection only and not to merge identities. Falsified if recall is equal across scripts for the same names. Destination: `ner-evidence`, then `ner-eval` (slices `el-latin-translit`, `el-greeklish`, `el-homoglyph`). No result exists.

## Limits and next evidence

ELOT 743 rules were not read; no mapping is asserted. Greeklish sources are a 2006 abstract. Missing: current social-media Greeklish usage, passport name-change rules, Greek names in other scripts, Cypriot practice and measured homoglyph frequency.
