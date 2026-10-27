# Rayner, K., Fischer, M. H., & Pollatsek, A. (1998). Unspaced text interferes with both word identification and eye movement control. *Vision Research, 38*(8), 1129–1144. https://doi.org/10.1016/S0042-6989(97)00274-5

⚠ Not read in full.

**Identifier:** doi:10.1016/S0042-6989(97)00274-5; PMID 9666972 · **Read depth:** partial: PubMed abstract (efetch, 2026-10-14) and the OpenAlex/Crossref bibliographic record only. The publisher's open (bronze) PDF at ScienceDirect returned a Cloudflare block page to curl and HTTP 403 to WebFetch; I did not try to get past it. No PMC, repository or author copy was found (OpenAlex lists no repository full text; a web search found citing papers only). · **Source-tier:** peer-reviewed article · **Evidence basis:** abstract only · **Design and sample:** eye-tracking reading experiments (two, per the abstract) comparing normal text, text with spaces removed or filled with x, and text with spaces kept but words flanked by x; participants called "Subjects", N and population not seen · **Parties modeled:** person–artefact (reader and text) · **Facets:** as the bib lists it (spacing cost, P3) · **Read:** 2026-10-14

## What it argues

From the abstract only. Reading rate "decreased by approx. 50% when space information was not available." Removing space information "increased the effect of word frequency on the fixation times for selected target words," which the authors read as interference with word identification. It also "influenced the initial landing positions on words," which they read as an effect on eye-movement control. The abstract adds that further analyses explored the relation between the two effects; I could not see them.

I could not see the number of participants, their language background, the materials, the measure of reading rate, the size of the frequency effect or the landing-position shift, or how the x-filled and space-removed conditions differed from each other.

## Relation to the argument

**P3 (spacing cost for habituated readers).** The abstract supports the upper end of P3's "a third to a half": approximately 50% when space information is absent. It concerns readers used to spaced English text, not readers trained on *scriptio continua*, so it says nothing about the burden on ancient trained readers, the point that P1 records as disputed (Heilmann 2020). The paper should keep the qualifier "modern readers" that line 113 already uses.

**P5 (re-representation).** The two effects in the title (word identification and saccade targeting) fit the paper's claim that spacing does perceptual work: the same letters, laid out differently, change where the eyes go and how quickly words are recognised.

**Use in DRAFT_v2:**
- **Line 113, first citation** ("removing the spaces changes where the eyes land as well as how fast words are identified (Rayner et al., 1998)"). Consistent with the abstract: landing positions changed, and the word-frequency effect on fixation times grew. "How fast words are identified" is a fair gloss of a larger frequency effect on fixation times, but the abstract does not state identification speed directly. Not checked against the body.
- **Line 113, second citation** ("Deprived of these spatial markers, modern readers lose roughly half their reading rate (Rayner et al., 1998)"). Consistent with the abstract's "approx. 50%," which pools both no-space conditions ("either spaces were removed [or] filled with x"). The x-filled condition removes spacing but adds visual clutter, so the 50% is not a pure measure of removing spaces. Whether the two conditions gave similar costs could not be checked.
- The sentence before it ("Under Wolfe's (2021) Guided Search model, bottom-up feature salience guides ...", "spacing gives the oculomotor system targets for the next saccade") is the draft's interpretation and is not attributed to Rayner; the change log (line 736) marks it so.

## In conversation with

- `raynerpollatsek1996reading`: Rayner & Pollatsek's reply to Epelboim et al. on reading unspaced text; same research programme, two years earlier.
- `epelboim1994reading`, `epelboim1997fillers`: the critique that spaces are not needed for guiding saccades; Rayner et al. 1998 is likely a response, but I could not see its reference list to confirm.
- `morris1990parafoveal`: Morris, Rayner & Pollatsek (1990), "Eye movement guidance in reading: The role of parafoveal letter and space information"; earlier work by two of the same authors on space information and saccade targeting; citation relation unverified.
- `perea2009space`, `sheridan2013unsegmented`, `winskel2009eye`, `bai2008reading`: later studies that cite this paper's ~50% figure or test spacing in other scripts; the range "a third to a half" in P3 comes from combining them.
- Leads: none given; the reference list was not seen.

## Caution

Abstract only. Every number beyond "approx. 50%" (N, language, effect sizes, landing-position shift) is unseen. English readers habituated to spaces; not a test of readers of unspaced scripts. Before submission someone with library access should open the PDF and check the per-condition reading rates, since the draft quotes the headline figure.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** Tried the open routes again. OpenAlex and Semantic Scholar both list only the ScienceDirect bronze PDF, which returned HTTP 403 with a block page to curl. The file the writer saved as `r4_50/rayner1998.pdf` is that same block page (HTML, 832,805 bytes), not the article. OpenAlex reports no repository full text, and a web search found citing papers only. I did not try to get past the block. I re-fetched the PubMed abstract (PMID 9666972) and checked every quoted phrase in the card against it word for word. I checked the reference record against Crossref (Rayner, Fischer, Pollatsek; *Vision Research* 38(8), 1129–1144, April 1998). I confirmed that the bib keys named in "In conversation with" exist in references.bib. I re-read DRAFT_v2.md lines 113 and 736.

**Findings:**
1. The quotations ("approx. 50% when space information was not available", "increased the effect of word frequency on the fixation times for selected target words", "influenced the initial landing positions on words") match the abstract. So does the card's bracketed "[or]": the abstract reads "either spaces were removed filled with x", missing a word, and the card marks its insertion.
2. The abstract says "In two experiments"; the card's "two, per the abstract" is right.
3. Use in DRAFT_v2, line 113: both verdicts stand. The ~50% figure pools space-removed and x-filled conditions, and the identification-speed gloss is an inference from a larger frequency effect. Neither can be checked against the body.
4. The read depth (abstract only, ⚠ Not read in full) is accurate. Nothing to correct.

## Also used by facet W (2026-10-15)

Facet W did not reach the full text either (ScienceDirect returned HTTP 403 to a plain request on 2026-10-15; no repository copy found). It adds the restatement in `perea2015colours` (p. 8): "the lack of spaces between words in English hinders the process of word identification (e.g., lexical effects such as word-frequency are magnified in unspaced sentences relative to spaced sentences) as well as eye movement guidance (e.g., landing sites are closer to the beginning of the word than to the centre of the word ...)" (S2 correction of page and wording, 2026-10-15). Perea et al. reproduce the design with Spanish and report the one-colour unspaced cost as 3,701 against 2,188 ms (69%), which is the nearest open-text number to the "approx. 50%" of this abstract.
