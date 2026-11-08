---
key: legg2007collection
apa: "Legg, S., & Hutter, M. (2007). *A collection of definitions of intelligence* (Technical Report IDSIA-07-07; arXiv:0706.3639v1). IDSIA. https://doi.org/10.48550/arxiv.0706.3639"
authors: "Legg, Shane; Hutter, Marcus"
year: 2007
title: "A Collection of Definitions of Intelligence"
venue: "IDSIA technical report IDSIA-07-07 (arXiv:0706.3639)"
volume: ""
issue: ""
pages: ""
doi: "10.48550/arxiv.0706.3639"
url: "https://arxiv.org/abs/0706.3639"
type: report
facets: [F3]
claims: [c3]
role: anchor
load: load-bearing
read_depth: full_text
object_read: "arXiv v1 PDF (12 pp., stamped 'arXiv:0706.3639v1 [cs.AI] 25 Jun 2007', dated 15 June 2007 on p. 1) and its text layer, at ~/iit-playground/pt_ai_animation_local/pdfs/legg2007collection/legg2007collection.pdf and legg2007collection.txt; no copy in inbox/; read 2026-11-08; sha256 8091798aca00bdb28d6d6f2d92262470eb4be309c7c734a57f266b54a41d72f3 (PDF, sha256.txt, recomputed with shasum -a 256, matches)"
verified: corrected
verified_against: "csl.json (arXiv DataCite record, v1); PDF p. 1 header; full text layer per page with pdftotext, 8 quotations traced; sha256 recomputed"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Legg and Hutter (2007), A collection of definitions of intelligence

Full text read: the abstract, §1 to §5 (pp. 1-9) and a look through the reference list (pp. 9-12). The PDF page number equals the printed page number (the title page is page 1).

## What it argues

Shane Legg and Marcus Hutter list the informal definitions of "intelligence" they have gathered over the years and call the list, "to the best of our knowledge", the largest and best-referenced one there is (p. 2). They sort the entries into three groups: collective definitions from dictionaries, encyclopedias and expert statements (§2), definitions by psychologists (§3) and definitions by AI researchers (§4). They quote no author's argument at length; the entries are one or two lines each. They state that there is no standard definition, but reject the view that intelligence therefore cannot be defined (p. 2). In §5 they pull three shared features out of the list (an individual agent in an environment, success at goals, adaptation across environments) and adopt their own sentence as the working definition: "Intelligence measures an agent's ability to achieve goals in a wide range of environments." (p. 9). The formal version sits in a separate paper, `legg2007universal`.

## What the paper uses it for

- **c3** (neither life nor intelligence has a consensus definition): this is the source for the sketch's sentence that Legg and Hutter collected "about 70" definitions of intelligence. The use fits the count: the authors write "70 odd" (p. 2). It stretches the source on the conclusion. Legg and Hutter do not argue that the lack of consensus is a reason to defend a theory instead of a definition; they argue the opposite. They say the pessimism that intelligence "cannot be fully defined" "is too strong" (p. 2), and they offer one definition as the right summary (p. 9). So the Collection supports the premise (many definitions, no standard one) and is also a source the paper must answer when it says a definitional project is the wrong target. For the life side the paper has Trifonov and Machery, not this source.
- One entry bears on c4 and c5 without being tagged for them: Warwick's definition, "the mental ability to sustain successful life" (§4, item 17, p. 8), ties intelligence to living. It is one line quoted from a newspaper, so it is a pointer, not support.

## Loci

Each quotation was matched against legg2007collection.txt. Where the text layer breaks a word at a line end with a hyphen, the word is joined here.

- p. 2, §1 (epigraph, R. J. Sternberg quoted in [14]): "Viewed narrowly, there seem to be almost as many definitions of intelligence as there were experts asked to define it."
- p. 2, §1: "Despite a long history of research and debate, there is still no standard definition of intelligence."
- p. 2, §1: "This has lead some to believe that intelligence may be approximately described, but cannot be fully defined. We believe that this degree of pessimism is too strong."
- p. 2, §1: "Although there is no single standard definition, if one surveys the many definitions that have been proposed, strong similarities between many of the definitions quickly become obvious."
- p. 2, §1: "the 70 odd definitions presented below are, to the best of our knowledge, the largest and most well referenced collection there is."
- p. 8, §4, item 17 (K. Warwick quoted in [4]): "the mental ability to sustain successful life."
- p. 9, §5: "In matters of definition, it is difficult to argue that there is an objective sense in which one definition could be considered to be the correct one."
- p. 9, §5: "Intelligence measures an agent’s ability to achieve goals in a wide range of environments."

## Caution

- **Version.** This is arXiv v1, which the PDF's own header calls "Technical Report IDSIA-07-07". The authors say they keep "the most up to date version of the collection ... online [21]" (p. 2), so the list a reader finds today may be longer than the one read here. The "70 odd" count belongs to v1.
- **Record type.** csl.json in the folder types the work "article-journal" with container "arXiv". The PDF itself is a technical report. I set `type: report`. The paper should cite it as the arXiv report, and I did not check for a later journal or proceedings version.
- **Count.** I did not count the entries. The sketch's "about 70" and the authors' "70 odd" agree; the exact number is not fixed by this card.
- **Chollet's attribution.** Chollet (`chollet2019on`, p. 3) quotes "no general survey of tests and definitions has been published" and credits "A collection of definitions of intelligence" [53]. I did not find that sentence in this v1 text. Chollet may mean another Legg and Hutter text.
- **Self-citation.** The adopted definition in §5 is the authors' own, from `legg2007universal`; it appears here as item 8 of §4 as well, so the collection is not a neutral list on that point.
- **No registry record.** The folder holds csl.json only (no Crossref or OpenAlex file). Authors, title and year are matched to the PDF's first page.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 4
- verdict: corrected
- checked: frontmatter against csl.json (Shane Legg, Marcus Hutter, 2007, title, DOI 10.48550/arxiv.0706.3639, version 1) and the PDF's p. 1 ('Technical Report IDSIA-07-07', 'arXiv:0706.3639v1 [cs.AI] 25 Jun 2007', '15 June 2007'); `type: report` against the record's 'article-journal' is justified by the PDF and flagged under Caution; sha256 of the PDF recomputed, matches; all 8 quotations found verbatim on the stated page; item numbers checked: Warwick is §4 item 17 'quoted in [4]', the authors' own definition is §4 item 8, the Sternberg epigraph is 'quoted in [14]'; the 'most up to date' online-version sentence is on p. 2.
- changed: page count in object_read, 13 pp. to 12 pp. (pdfinfo gives 12 pages; the last printed page is 12), and the reference-list range in the read note, pp. 9-13 to pp. 9-12. Small point left as is: the source prints the Warwick entry as '. . . the mental ability to sustain successful life.'; the card quotes it without the leading ellipsis, which is a fair fragment.
