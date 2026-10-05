# Hindi: Name structure is community-dependent, so title and surname rules need scoped evidence

Scope: [dossier overview](overview.md), Hindi-language text (hi-IN). Language of text does not constrain a person's naming community. Status: desk synthesis with weak sources for naming practice; independent review pending. NER proposals remain untested. No claim about other Indian languages, whose naming practices differ.

## Research answer and basis

Two things can be stated with sources. First, honorific and title tokens are written as separate words unless they are part of the name (श्री अजय वर्मा, कन्हैयालाल जी versus श्रीराम, रामजी लाल), and the spelling standard keeps South Indian personal and family names as in their source language [HIN-S001](sources.md#hin-s001), sections 3.5.3 and 3.11.2. [HIN-002](findings/HIN-002.md) owns the honorific finding. Second, a W3C guide notes that some Indian communities use a given name plus patronymic and that a single "given plus family name" assumption fails [HIN-S012](sources.md#hin-s012); that passage concerns Southern India and is not evidence about Hindi speakers.

A tertiary encyclopedia lead, read as a fetch summary, describes North Indian names as first, optional middle, and last name, with last names often tied to caste or community (Sharma, Singh) and Kumar as a caste-neutral choice that can occur as a middle or last name, the honorific -ji, titles Shri and Smt, and Devi and Kumari used by women [HIN-S013](sources.md#hin-s013). It is a lead only: it cites a single government naming guide that was not obtained, and it states that women in rural areas adopt Devi or Kumari on marriage, which sits uneasily with the common use of कुमारी as a title or given-name element for unmarried women. That conflict is unresolved here. Regional and community variation (patronymic or husband's-name conventions) is therefore not established for Hindi speakers.

## Contrasts that challenge the shortcut

Do not assume that the last token is a surname or that two tokens mean given plus family name. Examples are **synthetic** (fictional people, repository MIT license, author self-check only):

| Original | Meaning | Question |
| --- | --- | --- |
| `अजय कुमार सिंह` | Ajay Kumar Singh | Three components; कुमार and सिंह may be name-internal, not titles. |
| `सुनीता देवी` | Sunita Devi | Second token may be a name element; not claimed as marital. |
| `श्रीमती सुनीता वर्मा` | Mrs. Sunita Verma | Title before name. |
| `मोहन` | Mohan | Mononym; a "given plus surname" detector must not require two tokens. |

## NER decision and falsifiable handoff

Test whether components such as कुमार, सिंह, देवी, कुमारी are treated as part of a name and not as a title or ordinary word, using matched pairs with and without a following given name. Compare a multi-token-name feature with a mononym-friendly baseline. Disposition: local proposal; `ner-evidence` deferred pending a reliable naming source. See the [decision brief](decision-brief.md).

## Limits and next evidence

This is the weakest topic by source quality. Need: an anthropological or sociolinguistic source on Hindi-belt naming, and a corpus-based count of name patterns by genre and community. Caste, religion and region must be treated as separate dimensions, and the study should avoid sensitive inferences from names.
