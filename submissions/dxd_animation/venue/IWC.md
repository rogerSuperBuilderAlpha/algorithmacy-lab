[Compiled by Claude (Opus 5.5 subagent), 2026-11-11, from the journal's official pages. Facts only; nothing from memory.]

# Interacting with Computers (IwC), Oxford University Press for BCS: submission fact sheet

## Access status

WebFetch opened the academic.oup.com pages listed below. curl received HTTP 403 from academic.oup.com, so I could not download a page and check its quotations byte for byte as I did for Taylor & Francis. Quotations below are the fetch tool's extraction of the live page, requested as exact text. On the About page the tool would give only short phrases, not the full paragraph.

## Sources (all accessed 2026-11-11)

| Key | URL | How read |
|---|---|---|
| O1 | https://academic.oup.com/iwc/pages/General_Instructions | WebFetch, three passes |
| O2 | https://academic.oup.com/iwc/pages/About | WebFetch; short phrases only |
| O3 | https://academic.oup.com/pages/for-authors/journals/preparing-and-submitting-your-manuscript/ai-principles-for-oxford-journals/policy-on-ai-use-and-disclosure-for-oxford-journals-authors | WebFetch (policy body at offset 100000) |
| O4 | https://academic.oup.com/pages/open-research/open-access/charges-licences-and-self-archiving/author-self-archiving-policy | WebFetch (offset 100000) |
| O5 | https://academic.oup.com/journals/pages/open_access/charges | WebFetch; charge appears only through a lookup form |
| O6 | https://academic.oup.com/iwc/pages/special-issues | WebFetch |
| O7 | https://academic.oup.com/iwc/pages/call-for-papers-special-issue-the-quality-of-speculation-in-human-computer-interaction | WebFetch |
| O8 | https://academic.oup.com/iwc/pages/call-for-papers-methodological-contributions-to-hci | WebFetch |
| O9 | https://academic.oup.com/iwc/pages/call-for-papers-axai-and-synergy | WebFetch |
| C1 | https://api.crossref.org/journals/0953-5438 | Crossref API |
| C2 | https://api.crossref.org/journals/0953-5438/works (queries: AI framework, human-AI conceptual, automation theory, algorithmic theoretical, provocation AI, decision/algorithm/design, agency AI theory, literacy competence AI, framework propositions; from 2024-01-01) and https://api.crossref.org/works/{DOI} | Crossref API |

## 1. Identity

- Publisher: Oxford University Press. ISSN print 0953-5438, electronic 1873-7951 [C1].
- O1's footer reads "Copyright © 2026 British Computer Society" [O1]. O8 names Helen Petrie as "Editor in Chief" [O8].
- Submission site: http://mc.manuscriptcentral.com/iwc [O1].

## 2. Aims and scope

- IwC "publishes original work from all areas of Human-Computer Interaction (HCI)" [O1]. Per O2, it advances HCI theories, methods and practices, and it "mainly publishes original empirical work" [O2, short phrase]. O2's topic list includes "Human-centered AI", "Interaction design and user interface design", "Ethical and societal implications of HCI", and "Privacy, security, and trust in HCI" [O2].
- **Framing caveat** [O1]: "Note that if your paper primarily concerns the psychological impact of computer use or uses a framing from another discipline than HCI (e.g., media and communication, information science, marketing, business management) without a central consideration for the interaction and the use of relevant literature in HCI, other journals are likely to be a better fit."
- **Theory papers without new data** [O1]:
  - "Research papers may have a substantial theoretical basis and/or contain the findings of empirical work." "Typically, papers in this category will contain both."
  - "Authors of theoretical papers are expected to make a serious attempt to relate their work to application-related problems."
  - "Authors of research papers are encouraged to be explicit about the applied relevance of their work." Such papers should describe "the practical consequences of the research for the design, evaluation, and use of computer systems (design implications or implications for practice)."
- **Fit query:** "If you are uncertain about the suitability of your paper for IwC, we kindly invite you to submit an abstract to the Editor-in-Chief for further evaluation and guidance." [O1]

## 3. Article types and length limits [O1 unless noted]

| Type | Length | Notes |
|---|---|---|
| Research paper, long | "7,000-12000" words | "(excluding abstract and references)". "For papers exceeding 12.000 words, the authors are invited to justify the length regarding its expected contributions or the methodology used (e.g., multiple studies or in-depth qualitative data) in the cover letter to the Editor-in-Chief." |
| Research paper, short | "around 3,000-5,000 words" | Same exclusions. |
| Provocation | "short (3,000 – 5,000 words) pieces that tackle timely, difficult, or controversial issues in HCI" | "These might present a new perspective, suggest a radically new approach, or critique a known theory, method, or topic." "We strongly advise authors interested in submitting such a piece to send a short outline to the Editor-in-Chief in advance for feedback." |
| State-of-the-art review | no limit stated | "Reviews need to go beyond a descriptive presentation of a research topic and provide a critical appraisal." |
| Pictorial | "around 12 pages (excluding references)" | Papers that rely heavily on visual elements. |
| Case study | no limit found | Listed as a contribution type [O1, O2]. |

- **What the count includes:** O1 excludes the abstract and references. It says nothing about tables or figures **[NOT FOUND]**.

## 4. Abstract, keywords, structure, statements [O1]

- Abstract: "Provide a short abstract (around 150-200 words), avoiding any abbreviations and reference citations."
- Keywords: "Provide up to six keywords from the keywords lists based on the" 2012 ACM Computing Classification System.
- Structure: "There is no particular structure for a paper in Interacting with Computers". For empirical work, O1 suggests Introduction, Background/Related Work, Method, Results, Discussion and Conclusions, and References.
- Data: "Authors are required to include a data availability statement in their paper."

## 5. Reference style [O1]

- At first submission: "References and in-text citations can be formatted in any readable style at submission."
- At final submission: APA, "American Psychological Association Publication Manual (7th edition)".

## 6. Review model and anonymised file [O1]

- "The journal operates double-anonymized peer review."
- Title page: "Submit all identifying information using the ‘Title Page’ option". That covers title, authors, affiliations, correspondence and acknowledgements.
- Manuscript file: it must not include "descriptions that can easily reveal authors' names and/or affiliations". Self-citations "should be left unanonymised but cited in the third person".
- "Papers that violate the anonymization policy will be desk rejected."
- **Process:**
  - The Editor-in-Chief screens every submission first. "usually within 3 weeks after submission, manuscripts may be desk rejected without peer review".
  - Papers that pass go "most usually to three independent reviewers".
  - "In general, authors may expect a reply within three to five months from the initial submission."
  - Minor revisions: "20 days is usually given". Major revisions are expected "within 1-2 months at the most".

## 7. Preprint and prior posting

- **Journal [O1]:** "Authors retain the right to make an Author's Original Version (preprint) available through various channels, and this does not prevent submission to the journal." After acceptance, "the authors are required to update the status of any preprint, including your published paper's DOI".
- **Originality [O1]:** the manuscript must not have been "published elsewhere (except as an academic thesis, an abstract only, or as part of a published lecture)". It must not be "under consideration for publication elsewhere, such as in another journal, or in conference or workshop proceedings."
- **OUP-wide [O4]:** "Authors may make their AOV available anywhere at any time." The policy names "their own personal websites, institutional or non-commercial or subject based repositories," and "commercial websites or repositories, or social media". It also warns: "Please be aware that policies and embargo periods may differ from journal to journal".
- **GitHub repository or Substack post:** neither page names either. Both fall under O4's named categories ("commercial websites or repositories, or social media"); that classification is mine, not OUP's. Neither page says how a public preprint interacts with double-anonymized review.

## 8. Generative AI policy

- **Journal [O1]:** "Natural language processing tools driven by artificial intelligence (AI) do not qualify as authors, and the Journal will screen for them in author lists." Also: "The use of AI (for example, to help generate content or images, write code, process data, or for translation) should be disclosed both in cover letters to editors and in the Methods or Acknowledgements section of manuscripts." O1 refers authors to "the COPE position statement on Authorship and AI".
- **OUP-wide [O3, "Policy last updated on: 13 July 2026"]:**
  - Precedence: authors "should follow the journal's specific guidance" where the two differ.
  - No disclosure needed for "Improving clarity of language (e.g. spelling or grammar correction)" or "Formatting references to comply with journal style requirements". Authors must still ensure "all references are accurate and valid with no hallucinations."
  - "Typically permitted with disclosure": "Substantially editing, rewriting, or reorganizing text using AI"; "Translating text using AI"; "Generating or refining code using AI"; "Generating illustrative or explanatory images, such as graphical abstracts, using AI".
  - Not permitted: "Creating content by Gen AI Tools and misrepresenting as though it is original research data/results created by humans"; "Creating or altering primary factual, scientific, or technical images".
  - Where: "Any use of Gen AI Tools should be disclosed both in your cover letter to editors and in the Acknowledgements section of manuscripts". Also: "You may also be required to disclose specific uses in the Methodology section".
  - Content, required: "Name and version of the Gen AI Tool used"; "A description of how the Gen AI Tool was used"; "The author's role in directing and reviewing the work". Strongly recommended: "Date(s) of use"; "Specific sections of the document where the Gen AI Tool was used".
  - Principle: "Disclosure is essential to ensure that AI-generated content is not presented as entirely human-created." "Authors are accountable for complete and accurate disclosure."
  - The fetch tool found no row for drafting text from scratch, idea generation or literature search **[NOT FOUND as a named row, O3]**.

## 9. Open access and charges

- [O1] "Interacting with Computers offers the option of publishing under either a standard licence or an open access licence." "You will need to pay an open access charge to publish under an open access licence." O1 adds that Read and Publish agreements may cover the charge for authors at participating institutions.
- No charge for the standard licence is mentioned on O1.
- **OA charge amount: [NOT FOUND].** O5 shows the charge only through a lookup form ("Use the form below to check the open access charge"; "Please note that these prices are subject to change").

## 10. Special issues and calls (O6, as listed 2026-11-11)

- **Open, rolling [O8]:** "Ways of Knowing: An Open Call for Methodological Contributions to Human-Computer Interaction, Interaction Design and User Experience". "Submissions are accepted at any time." Its categories are methodological ("Novel methodological approaches", "Reflective and critical perspectives", and others). It does not name theory or framework papers outside a methods focus.
- **Upcoming issue, closed to new authors [O7]:** "The Quality of Speculation in Human–Computer Interaction".
  - Extended abstracts were due 17 September 2026. Full manuscripts are due 17 December 2026, by invitation only.
  - The call welcomes "contributions that advance conceptual and theoretical understandings of quality".
- **Closed [O9]:** "Special Issue on Synergistic and Adaptive Interaction in Hybrid Human-AI Systems".
  - Extended abstracts were due 23 March 2026 and full manuscripts 27 July 2026.
  - The call encouraged "Philosophical and theoretical foundations of human-AI collaboration".
- **Past:** "Human Work in the Age of AI and Automation" (2025) and "Self-Determination Theory in HCI" (2023) [O6].

## 11. Recent IwC papers in the genre (Crossref only) [C2]

I could not find a 2024–2026 IwC paper that is clearly a theoretical framework on human–AI interaction. Most AI papers that Crossref returned are empirical; Kraishan (2026), for example, analysed 1,469,549 conversations. The closest genre matches are conceptual or design-theory papers. I read only their abstracts, from the Crossref records:

| Year | Authors | Title | Vol(issue), pages | DOI | Why listed (abstract only) |
|---|---|---|---|---|---|
| 2025 | Mauro Coccoli; Livio Gatta | A cinematographic approach to web design | 38(1), 24–39 | 10.1093/iwc/iwaf026 | Proposes "a novel web design paradigm" drawn from cinema; the closest precedent for borrowing a moving-image craft |
| 2025 | Torkil Clemmensen | Stop doing user experience design, start doing relation artefact design | 38(4), 517–526 | 10.1093/iwc/iwaf044 | "In this provocation, I propose relation artefact design (RAD)"; built on "theoretical analysis"; shows the Provocation genre at 10 pages |
| 2024 | Rebecca Gerstenberg; Marc Hassenzahl; Matthias Laschke | Designing for Autonomy: A Process-Oriented Approach Based on Organismic Integration Theory | 38(3), 367–378 | 10.1093/iwc/iwae022 | A design approach derived from a psychological theory |
| 2025 | Jeffrey Bardzell; Maliheh Ghajargar | Alterity and kinship: co-writing posthumanist speculative nonfiction with AI | 38(2), 264–279 | 10.1093/iwc/iwaf013 | A theory-led methodology with AI as co-writer |
| 2025 | Gavin Sim | Provocation: Is there an assumed need for participatory design with children? | 37(6), 497–503 | 10.1093/iwc/iwaf003 | A labelled Provocation, 7 pages |

## 12. Corrections to the earlier venue note (`submissions/dxd_foundation/venue/V1_human_factors_hci.md`, §11)

- **Provocation outline:** V1 quotes "recommend sending an outline to the Editor-in-Chief first". The page says: "We strongly advise authors interested in submitting such a piece to send a short outline to the Editor-in-Chief in advance for feedback." [O1]
- **Theory papers:** V1 writes "Theoretical papers are accepted but are expected to relate their work to application-related problems". The page says: "Authors of theoretical papers are expected to make a serious attempt to relate their work to application-related problems." [O1]
- **AI disclosure:** V1 writes "any use of AI … must be disclosed". The page says "should be disclosed", and its example list reads "to help generate content or images, write code, process data, or for translation" [O1]. V1 also omits the OUP-wide policy of 13 July 2026, which requires the tool name and version, how it was used, and the author's role [O3].
- **Framing caveat:** V1 paraphrases it as "another discipline's framing". The page names "business management" explicitly among the other disciplines [O1].
- **Article types:** V1 omits **case studies** [O1, O2].
- **Special issues:** V1 says "none found". O6 lists several (§10), but none is open to this paper except the rolling methods call.
- **Not re-confirmed:** V1 says the OA charge "is paid after acceptance". I did not see that wording in this pass [O1].

## 13. Not found (URLs tried, 2026-11-11)

- OA charge amount: O5 (lookup form only).
- Whether tables and figures count toward the word limit: O1.
- A named OUP policy row for AI-drafted text, idea generation or literature search: O3.
- Byte-level verification of quotations: curl to academic.oup.com returned 403.

## Fit for this paper

1. Length: 9–12k words falls inside the long research paper range (7,000–12,000, "excluding abstract and references"). Anything over 12,000 needs a justification in the cover letter. The Provocation route would mean cutting to 3,000–5,000 words and sending an outline first.
2. Theory fit: IwC accepts theory, but it "mainly publishes original empirical work" and expects theoretical papers "to relate their work to application-related problems". It also sends business-management framings without "a central consideration for the interaction" elsewhere, so the paper must lead with interaction design (Coccoli & Gatta 2025 is the precedent for borrowing from cinema).
3. Preprint: a public GitHub or Substack version is permitted ("available anywhere at any time"; "does not prevent submission"). Under double-anonymized review, however, an anonymization breach brings desk rejection, so the manuscript file must not point to the named repo.
4. AI: use is allowed with disclosure in the cover letter and the Methods or Acknowledgements section. OUP adds the tool name and version, a description of the use, and "The author's role in directing and reviewing the work". I found no ban on AI-assisted drafting.
5. Blockers: none found. To prepare: a data availability statement (even for a no-data paper), up to six ACM CCS 2012 keywords, a 150–200-word abstract, and the OA charge only if the author chooses OA.
