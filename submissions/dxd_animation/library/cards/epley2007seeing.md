---
key: epley2007seeing
apa: "Epley, N., Waytz, A., & Cacioppo, J. T. (2007). On seeing human: A three-factor theory of anthropomorphism. *Psychological Review*, *114*(4), 864–886. https://doi.org/10.1037/0033-295X.114.4.864"
authors: "Epley, Nicholas; Waytz, Adam; Cacioppo, John T."
year: 2007
title: "On seeing human: A three-factor theory of anthropomorphism"
venue: "Psychological Review"
volume: "114"
issue: "4"
pages: "864–886"
doi: "10.1037/0033-295x.114.4.864"
url: "https://doi.apa.org/doi/10.1037/0033-295X.114.4.864"
type: article
facets: [F3]
claims: [c4, c6]
role: support
load: load-bearing
read_depth: abstract
object_read: "Crossref work record (JSON) for DOI 10.1037/0033-295x.114.4.864 (no abstract) and OpenAlex work record W2115040353 (JSON) whose abstract_inverted_index I rebuilt into the abstract text; no text of the article; local folder ~/iit-playground/dxd_animation_local/pdfs/epley2007seeing/ (crossref.json, openalex.json); original URL none recorded (FETCH_LOG.tsv row epley2007seeing: 'no candidates', status closed; no provenance.txt); read 2026-11-05; sha256 crossref.json c2da9038b7af074dd42e06e0bcf37037bdc56a664b1438bec00d7fa7916a6b86, openalex.json 7e6dfeb024c5df7aceffe2dbe23422faa4adc53230a3750c06a491ae5e5a8292"
verified: corrected
verified_against: "crossref.json (DOI 10.1037/0033-295x.114.4.864) and openalex.json (W2115040353, abstract rebuilt from the inverted index by the verifier), sha256 of both recomputed; FETCH_LOG row 69; BROWSER_LIST row 35"
prior_cards: [epley2007seeing (dxd_animator)]
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

This card rests on the abstract only (OpenAlex's, rebuilt from its word index). Epley, Waytz and Cacioppo define anthropomorphism as "the tendency to imbue the real or imagined behavior of nonhuman agents with humanlike characteristics, motivations, intentions, or emotions". They call it "surprisingly common" but "not invariant", and they offer a theory of when people are likely to anthropomorphise and when they are not.

The theory names three determinants. The first is "elicited agent knowledge", the accessibility and applicability of anthropocentric knowledge. The second is "effectance motivation", the motivation to explain and understand other agents' behaviour. The third is "sociality motivation", the desire for social contact and affiliation. The authors predict that people anthropomorphise more "when anthropocentric knowledge is accessible and applicable, when motivated to be effective social agents, and when lacking a sense of social connection to other humans". They say the factors explain why anthropomorphism varies and offer "testable predictions about dispositional, situational, developmental, and cultural influences". The discussion, per the abstract, extends the theory to "robotics and human-computer interaction" and to dehumanization as the inverse process.

## What the paper uses it for

- **c4.** FACETS F3 lists the theory for the character claim: an LLM interface is an animated character. The abstract supports a narrower point. People attribute humanlike minds to nonhuman agents, more so under named conditions, and the authors apply this to human–computer interaction. The abstract says nothing about animation, characters as designed objects, or an animator behind them; that link is the paper's (through L. Stark, 2024).
- **c6.** If the paper uses the theory for the user's lock-in, the abstract helps in one way and cuts in another. It helps: the three factors are conditions in the user, so the user supplies the humanlike reading, which fits "the viewer's own perception" doing the work. It cuts: the theory is about attributing minds, not about perceptual continuity, so it does not explain why frame gaps disappear.
## Loci

None.

## Caution

- Depth. Everything above rests on the OpenAlex abstract. FETCH_LOG records no open candidate and BROWSER_LIST row 35 lists the article as not located.
- The OpenAlex abstract is rebuilt from an inverted word index. Word order follows the index positions; punctuation such as the double hyphen in "determinants--the accessibility" comes from the index. Check the wording against the article before quoting it in the paper.
- DOI case. Crossref stores the DOI as 10.1037/0033-295x.114.4.864; its resource URL uses 0033-295X. The card treats the two as one DOI; resolution of either form was not tested this run. The APA line uses the upper-case X as the publisher's URL does.
- Crossref gives the title with a final full stop ("...of anthropomorphism."); the card drops it.
- Earlier card (dxd_animator, "partial (abstract and catalogue record only)"). Its three factors match the abstract. Two points go beyond it. (1) It says anthropomorphism "is a predictable inference, not a mistake of the naive". The abstract says only that it is common, variable and predictable from three factors; it does not contrast it with a naive mistake. (2) It gives a Semantic Scholar count of 3628 and a Crossref count of 3511 (2026-11-03). The records read here give 3521 (Crossref is-referenced-by, 2026-11-05) and 4192 (OpenAlex). Counts move; neither belongs in the paper. The earlier file was not edited.
- Not cited in SOURCE.md or OUTLINE.md; status candidate.
- Related pointer, not read: `waytz-heafner-epley-2014-mind-in-the-machine` (dial), named in the F3 triage file.

## Verification

2026-11-05 · S6 verifier, batch b09 (opus; not the writer) · verdict: corrected · checked: loci 0/0 (None, correct for abstract); every quoted phrase found verbatim in the rebuilt abstract; authors, 114(4), pp. 864-886, DOI, URL, counts 3521 (Crossref) and 4192 (OpenAlex) match; depth abstract honest; sha256 matches; four sections in order · changed: removed the untested claim that both DOI case forms 'resolve to the same record'; moved the 'Not cited ... status candidate' line from the uses section to Caution, since it is not a claim-tag bullet

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index**.
- Checked: 0/0 loci (None, correct); every quoted phrase in "What it argues" is in the OpenAlex abstract rebuilt from the inverted index (including the double hyphen before "the accessibility"); frontmatter vs crossref.json and openalex.json (three authors, Psych Review 114(4), 864–886, DOI stored with lower-case x, title with a final full stop, counts 3521 and 4192); sha256 of both files matches; claim uses: c4 marks the animation link as the paper's; c6 states both what helps and what cuts.
- Changed: nothing.
- For the author: not located by any open route (BROWSER_LIST row 35); a library copy would take an F3 support card to full text.
