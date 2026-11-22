# akhil2026

- **Reference.** S.G., A., & Lyytinen, K. (2026). Invisible labor of argumentation: How radiologists interpret AI in everyday practice. *ICIS 2026 Proceedings*, 25 (Future of Work track, paper ICIS2026-3630, completed paper). https://aisel.aisnet.org/icis2026/fow/fow/25 . No DOI. OpenAlex W7222909517. (OpenAlex lists the first author as "S. G. Akhil"; the key follows that record.)
- **Batch / triage.** P2. TRIAGE_T2, justesen2024, possible_answer, candidate 6.
- **Read depth.** abstract. The AISeL PDF (`oa_pdf_url`) returned a Cloudflare bot-check page to curl and HTTP 403 to WebFetch; no PDF saved. The AISeL landing page loaded (title, authors, track, paper number). The abstract quoted below is the OpenAlex abstract, reconstructed from `citing/justesen2024_openalex.json`.
- **Citation line found.** Not seen. The reference list was not reachable. OpenAlex's `referenced_works` for W7222909517 includes Justesen and Plesner (2024) (W4392883145), and the work appears in OpenAlex's `cites:` list for that article. Citation is confirmed by index metadata only.
- **Citing passages.** Not seen.

## Candidates touched

**6. Invisible work and opacity — takes_up, possible answer (abstract only).** [S10f: was "answers (on the abstract)". The card rests on the same title and abstract from which triage judged the work `possible_answer:6`; no text was added, so the class cannot be stronger than the triage's. See Fable check.]
> "we introduce argumentation labor to describe the cognitive and communicative meta-work required to adjudicate machine-generated reasoning" (abstract)

> "We position argumentation labor as a layered, additive form of invisible labor that extends, rather than replaces, the classical articulation, coordination, and infrastructural work." (abstract)

**5. Expertise and the division of labour — takes_up (on the abstract).**
> "We show how knowledge experts repairs the limits of machine reasoning and in process absorb asymmetric liability." (abstract; the error is in the source)

## What the work says

From a 25-month ethnography of a radiology department running 17 FDA-cleared models, S.G. and Lyytinen name "argumentation labor", the work of reconstructing, comparing, adjudicating and integrating AI claims that arrive without warrants or rebuttals, and file it as a new layer of invisible labor on top of articulation, coordination and infrastructural work. Experts repair what the machine's reasoning lacks and, in doing so, take on liability out of proportion to their control.

## Caution

Abstract only: no page locators, no view of how the paper cites Justesen and Plesner, and no check that "invisible" is used in their sense. Of all the works in this batch, this one comes closest to algorithmacy's "interpreting" part as unrecognized work, since adjudicating machine-generated reasoning is interpretation. But the counterpart here is the machine's claim, not a colleague reached through the system, so the triad is absent on present evidence. Read the full paper before citing it as prior art.

## Verification

- **Verifier.** Claude Opus 5.5, S10e (independent check; did not write the card).
- **Date.** 22 November 2026.
- **Bibliographic line.** No DOI, so no Crossref record. The AISeL landing page (fetched 22 Nov 2026) gives title, authors "S.G., Akhil" and "Lyytinen, Kalle", and paper ICIS2026-3630, matching the card.
- **Citation of the OT article.** OpenAlex W7222909517 in `citing/justesen2024_openalex.json` lists W4392883145 (Justesen & Plesner 2024) among its 28 referenced works. Index metadata only, as the card says.
- **Quotes checked / corrected.** 3 / 0. All three match the OpenAlex abstract reconstructed from the inverted index, including the source error "knowledge experts repairs".
- **Classification changes.** None. answers (6) and takes_up (5) are supported by the abstract's own claims; both stay provisional on abstract evidence.
- **Read depth.** abstract, stated correctly.
- **Verdict.** verified

## Fable check

[Written by Fable (claude-fable-5-2), S10f, 2026-11-22]

- **Date.** 22 November 2026. Counting follows the plan's rule that "a citing work counts only if its reference list holds the OT article": for each candidate I say whether the work cites an asker of that candidate, and for what.
- **Read against.** The OpenAlex abstract for W7222909517, which I rebuilt from the inverted index in `citing/justesen2024_openalex.json`. The local store holds no text for this key, neither `akhil2026.txt` nor `akhil2026_crossref.txt`.
- **Quotations.** 3 of 3 match the abstract word for word, the source's "knowledge experts repairs" included.
- **Classes.** Candidate 6: I lower `answers` to `takes_up, possible answer (abstract only)`. Triage T2 judged this work `possible_answer:6` from its title and abstract (`TRIAGE_T2.tsv`, row "Invisible Labor of Argumentation"). The reader could not open the paper and read the same abstract, so the card adds no evidence to the triage and cannot carry a stronger class. The abstract supports this much: the authors name a new form of invisible labor in an AI-integrated department and tie it to machine claims that arrive "lacking transparent warrants and rebuttals" (abstract). It cannot show whether they take up Justesen and Plesner's invitation, whether "invisible" carries the askers' sense, or what the citing passage says. Candidate 5: `takes_up` stands at abstract depth.
- **Counting.** Candidate 6: the citation of justesen2024 rests on OpenAlex's `referenced_works` (28 entries; W4392883145 is among them); no one has seen the reference line. Candidate 5: W7222909517 appears in the harvested citing lists of none of that candidate's askers (I searched `hsu2024_openalex.json`, `hinds2024_openalex.json` and `stark2024_openalex.json`), so on candidate 5 the work is convergent evidence with no citation edge.
- **Use.** An abstract-level neighbour for the interpreting part. The paper is not citable as prior art, and its class on candidate 6 is not settled, until someone reads it in full.
- **Verdict.** used_with_corrections
