---
key: pinhanez2017design
apa: "Pinhanez, C. S. (2017). Design methods for personified interfaces. In *Proceedings of the International Conference on Computer-Human Interaction Research and Applications (CHIRA 2017)* (pp. 27–38). SciTePress. https://doi.org/10.5220/0006487500270038"
authors: "Pinhanez, Claudio S."
year: 2017
title: "Design Methods for Personified Interfaces"
venue: "CHIRA 2017"
volume: ""
issue: ""
pages: "27–38"
doi: "10.5220/0006487500270038"
url: "https://www.scitepress.org/Papers/2017/64875/64875.pdf"
type: proceedings
facets: [F11, F12, G2]
claims: [m1, m2, m3, m4, m5, m7]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "SciTePress open PDF (12 pages, no printed page numbers), https://www.scitepress.org/Papers/2017/64875/64875.pdf, obtained 2026-11-11 with curl; ~/iit-playground/dxd_animation_local/pdfs/pinhanez2017design/pinhanez2017design.pdf; sha256 94113b8a1566e27ce243fe00394742b43fb2b0fa02cb2c8a60fc7ed6fe5c5a11; read in full from the reading-order text layer; Crossref record crossref.json"
verified: corrected
verified_against: "both text layers split by form feed; pdfinfo (12 pages); page image of PDF p. 5 (pdftoppm, 50 dpi); crossref.json; provenance.txt; sha256 of PDF recomputed"
prior_cards: []
status: candidate
added: 2026-11-11
run: dxda-lib-2026-11b
---

## What it argues

Claudio Pinhanez, at IBM Research São Paulo, argues that chatbots, voice assistants and humanoid robots form a class of **personified interfaces** that "need to portray coherent human traits, deal with conflict, and handle drama" (abstract), and that these needs call for design methods drawn from personality theory, improvisational theatre, comics, puppetry and "movie animation" (abstract). He treats the three needs as "working hypotheses" and says "we will not try to validate them experimentally here" (p. 28); the student workshops on a service-recovery interface for e-commerce illustrate the methods and are "not as validation of the usefulness or efficacy of the design methods" (p. 34).

Two passages in §3 carry craft into chatbots (p. 31).
- **Puppetry.** Puppeteers help the audience suspend disbelief by exposing the puppet's workings or "openly showcasing the puppeteer on the stage as in bunraku theatre". In a chatbot, Pinhanez says, this becomes displaying "alternative understandings of an utterance from the user" and asking the user to choose, and he claims that exposing the bot's limitations "increases the confidence and trust of the user in it". He gives no evidence for that claim.
- **Animation.** He cites "a set of 12 fundamental principles of animation" compiled at Disney in the 1930s, quotes Thomas and Johnston's anticipation principle (giving their p. 52), and applies it to a binding act: "an important action such as charging a credit card is clearly anticipated by actions which potentially could be stopped by the user: after the user agrees verbally, there can be a depiction of the preparation for charging which allows one more chance for the user to change her mind." The other principles "may also be applied" but "We do not explore them further in this paper due to space restrictions."

His method, **puppet prototyping**, turns workshop skits into "interface comics" that specify interface actions expressing the machine's emotions and social behaviours (§4.4). His orientation is the persona: the machine should express regret "with acts of repair and renouncing, such as giving a voucher" (p. 31).

## What the paper uses it for

- **m3 and m2 (contrast, nearest precedent).** Pinhanez is the earliest read source that applies an animator's principle — anticipation — to a **binding** act in a conversational interface, with the anticipation placed where the user can still stop it. Row 2's commit-or-cancel and row 3's cue-before-change both have him as a precedent, and the paper must cite him. His aim differs: the anticipation protects the user's last chance before a charge; it does not signal a change in the rules, and it is not chosen through any account of what the user must do.
- **m1 (support, with a caution).** The bunraku move — show the user the bot's alternative readings of what they said and let them choose — is a precedent for staging alternatives at the point of interpretation. It runs the other way from idempotent interpretation: it asks the user to resolve the system's ambiguity about the user, not the user's ambiguity about the system. His trust claim is unsupported.
- **m4 (support).** He picks principles by the designer's requirements (coherent traits, conflict, drama), not by the user's decision competencies; he applies one principle and leaves the rest unexplored. He does have an account of the user — users personify machines, take an intentional stance toward them and turn interaction into drama (§§2.1–2.3) [lead, hand-check S7, after the verifier's note] — so the paper must not say he borrows craft with no account of the receiver. That narrows the paper's novelty claim to the selection by competencies.
- **m5 (contrast).** His goal is a more believable persona — "it is surprisingly easy to make audiences believe that there is an intelligent, emotional human being inside every puppet" — which is the character craft the model's placement rule keeps off the decision layer.
- **m7 (contrast).** A design method for chatbots drawn from puppetry and animation exists (2017). The paper's gap claim cannot be "no one has turned animation craft into chatbot design".

## Loci

Matched against the reading-order text layer of the SciTePress copy. The copy prints no page numbers; page numbers below are journal pages inferred from Crossref's range 27–38 (copy p. *n* = p. 26 + *n*), with the copy page given in brackets. Inner double quotation marks are changed to single; curly apostrophes are rendered straight.

1. "personified interfaces need to portray coherent human traits, deal with conflict, and handle drama" Abstract, p. 27 [copy p. 1].
2. "The design methods are exemplified with results from three student workshops aimed at designing a service recovery interface for e-commerce." Abstract, p. 27 [copy p. 1].
3. "The requirements can be treated as our working hypotheses for this paper and we will not try to validate them experimentally here." §2, p. 28 [copy p. 2].
4. "regret is better expressed with acts of repair and renouncing, such as giving a voucher to compensate for a service failure." §3, p. 31 [copy p. 5].
5. "An alternative body of knowledge can be used borrowing from concepts and techniques from puppetry and movie animation, whose fundamental quest is to vent humanity onto inanimate objects and drawings." §3, p. 31 [copy p. 5].
6. "puppetry shows that it is surprisingly easy to make audiences believe that there is an intelligent, emotional human being inside every puppet" §3, p. 31 [copy p. 5].
7. "openly showcasing the puppeteer on the stage as in bunraku theatre" §3, p. 31 [copy p. 5].
8. "An example of this principle in a chatbot is when it displays alternative understandings of an utterance from the user, and ask the user to choose the option that best represents what he or she means." §3, p. 31 [copy p. 5].
9. "By exposing (instead of hiding) its limitations such chatbot not only improves the overall interaction but also increases the confidence and trust of the user in it." §3, p. 31 [copy p. 5].
10. "a set of 12 fundamental principles of animation was compiled by Walt Disney's animators in the 1930s" §3, p. 31 [copy p. 5].
11. "In personified interfaces, we can apply anticipation by making sure that an important action such as charging a credit card is clearly anticipated by actions which potentially could be stopped by the user: after the user agrees verbally, there can be a depiction of the preparation for charging which allows one more chance for the user to change her mind." §3, p. 31 [copy p. 5].
12. "We do not explore them further in this paper due to space restrictions." §3, p. 31 [copy p. 5].
13. "the workshop results are included in this paper only to better illustrate the design methods proposed and not as validation of the usefulness or efficacy of the design methods." §4, p. 34 [copy p. 8].

## Caution

- **Page numbers inferred.** The open copy has no printed page numbers. The mapping copy p. *n* = p. 26 + *n* follows from Crossref's 27–38 and the copy's 12 pages; it is unchecked against the printed proceedings. Cite with the copy page until checked.
- **Thomas and Johnston at second hand, with a page.** Pinhanez quotes Thomas and Johnston (1981) on anticipation and gives "pp. 52". That is the only page locator for the book in the library; it is Pinhanez's, not checked against the book.
- **"12 principles".** Pinhanez says twelve; Lasseter (1987) lists eleven (`lasseter1987principles`). The count is unsettled until the book is read.
- **No evaluation.** Every design claim, including the trust claim in locus 9, is unsupported by data in the paper.
- **Gender of the user.** Pinhanez writes "her" and "he or she"; the paper should not carry that over.
- Found by the run-2 gap check (`../GAP_CHECK_2.md`), which read it through a Consensus full-text copy; this card was written from the SciTePress PDF.

## Verification

2026-11-11 · S6 verifier, batch C (Opus 5.5; not the writer) · verdict: corrected · checked: 13/13 loci found verbatim in the reading-order text layer, each on the copy page the card gives (copy pp. 1, 2, 5, 8 by form feed; the layout layer interleaves the two columns, so it was used only to check wording such as "and ask the user" and the §4.3/§4.4 headings); the copy-page-to-journal-page mapping is stated as an inference in the Loci note and in Caution, and it holds arithmetically (pdfinfo gives 12 pages; the copy p. 1 footer reads "CHIRA 2017), pages 27-38"); the page image of PDF p. 5 prints no page number; frontmatter vs crossref.json (sole author Claudio S. Pinhanez, 2017, title, proceedings container, pp. 27–38, SciTePress, DOI) and the copy p. 1 footer; sha256 of the PDF recomputed (94113b…), matches sha256.txt and object_read; read_depth full_text honest; body quotations: every quoted phrase found on its stated page, including "movie animation" (abstract), "working hypotheses" (copy p. 2), "interface comics" (copy pp. 10–11), and "pp. 52" for Thomas and Johnston (copy p. 5); second-hand material marked: the card gives the Thomas and Johnston anticipation passage only as Pinhanez's quotation, with his page, and does not reproduce it; claim uses; "earliest read source" checked against the library's cards that mention anticipation (Chang and Ungar 1993, Thomas and Calder 2001, Takayama et al. 2011, Ribeiro and Paiva 2012): none applies it to a binding act in a conversational interface · changed: (1) locus 3, "§1" → "§2": the sentence sits in §2 "Personified Interfaces" (copy p. 2); (2) What it argues, puppet prototyping "(§4.3)" → "(§4.4)": the layout layer prints "4.3 Comics Workshop" and "4.4 Puppet Prototyping", and §4's own list orders the methods that way; the reading-order layer puts the "4.3" label beside "Puppet Prototyping", which is the likely source of the slip · for the lead: (1) `provenance.txt` in the local folder says "6 PDF pages carrying the 12-page paper"; pdfinfo gives 12 pages, one journal page each. The card is right and the provenance note is wrong. I did not edit it. (2) m4: Pinhanez does ground his transfer in an account of the receiver: users personify machines, adopt Dennett's intentional stance and dramatize the interaction (§§2.1–2.3, copy pp. 2–3). The bullet's "not by the user's competencies" is accurate, but the paper should not say he transfers craft with no account of the receiver. (3) Locus 6 is Pinhanez's own sentence citing Blumenthal (2005), not a quotation of Blumenthal, and locus 10 is his sentence citing Thomas and Johnston; quote both as Pinhanez. (4) The body gives inferred journal pages without the copy page in brackets; Caution says to cite the copy page until the mapping is checked against the printed proceedings.

## Hand-check

- 2026-11-11, Claude (Opus 5.5, lead; S7). Verdict: **index**. Writer: the lead; check: S6 verifier, batch C (corrected: section numbers). Checked: the verifier's section fixes. Changed: the m4 bullet now records that Pinhanez has an account of the user (§§2.1–2.3). For the author: journal pages are inferred (copy p. + 26); the copy prints none.
