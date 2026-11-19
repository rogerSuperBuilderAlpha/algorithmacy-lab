# HAND_CHECK — S7, run dxda-lib-2026-11

> [Built by Claude, 2026-11-05.] Fable read every card against its source folder in four batches
> (brief: `hand_check/BRIEF.md`). The batch files below are concatenated unchanged.

**Result: 78/78 cards hand-checked. 75 index, 3 index after fix (schneider2018digital, wu2026ainimation,
siles2019mutual, each change marked "[Corrected by Fable, S7]" in the card), 0 hold.**

Follow-up after S7: `hoerl2015seeing` — the Warwick WRAP accepted version (28 pp.) is now in the
local folder (FETCH_LOG); the card is still abstract-depth and needs a re-write + verify + hand-check
to upgrade. `gnewuch2018faster` — AIS eLibrary returned HTML; stays on BROWSER_LIST. Stark's range
pp. 1663–1671 confirmed on the Crossref record (saved as `crossref_page.txt` in its folder).


# S7 hand-check, batch 1 (Fable, 2026-11-05)

Twenty cards, abercrombie2023mirages to furniss2008art, read against the folders under
`~/iit-playground/dxd_animation_local/pdfs/<key>/` and the registry records. Method: each quotation
grepped against the .txt text layer; where the stored .txt interleaves the two columns (Abercrombie,
Bhat, Cameron, Chevalier, Dragicevic, Endsley) I re-extracted the same PDF with pdftotext (sha256
unchanged) and mapped pages by form feed. Frontmatter checked against crossref.json, openalex.json or
openlibrary_search.json; abstract and metadata cards checked for Loci = None and for every quoted phrase
in the record's abstract. Cameron and Chiou checked against Checkpoint B ruling 4.

Verdicts: 20 index, 0 index after fix, 0 hold. Changed: nothing in any card beyond the appended
Hand-check section.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| abercrombie2023mirages | full_text | 9/9 | index | nothing | card names a possible c6 use not in DECISIONS; add the tag or leave it |
| ananny2018seeing | abstract | 0/0 | index | nothing | cited in SOURCE.md on an abstract; "across a relational environment" and the step to the user are the author's until the article arrives (BROWSER_LIST 8) |
| anderl2024conversational | full_text | 10/10 | index | nothing | nothing (cite Experiment 2 for the dynamic-text effect alone) |
| anderson1993myth | abstract | 0/0 | index | nothing | earlier card's active-viewer claims unverified until the text is read (BROWSER_LIST 28) |
| appel2012does | abstract | 0/0 | index | nothing | `load: exists` vs a c6 bullet that leans on the result; gold OA per DECISIONS but 403 three times (BROWSER_LIST 50) |
| ash2018digital | abstract | 0/0 | index | nothing | nothing |
| bettman1998constructive | abstract | 0/0 | index | nothing | anchor for c1, c2 rests on an abstract; read before §1–§2 lean on it (BROWSER_LIST 11) |
| bhat2025dynamic | full_text | 12/12 | index | nothing | nothing |
| bukatman2012poetics | metadata | 0/0 | index | nothing | nothing |
| cameron2024social | full_text | 15/15 | index | nothing | the read Checkpoint D waits for: Deployer has varied interests, not modelled; acts through the robot as a reading, not a measurement; model proposed, untested. Clark and Fischer (BBS) cited as 2022 here and 2023 in Abercrombie; check at source |
| chang1993animation | metadata | 0/0 | index | nothing | nothing (BROWSER_LIST 34) |
| chen2026do | abstract | 0/0 | index | nothing | nothing |
| chevalier2016animations | full_text | 12/12 | index | nothing | SOURCE.md cites it for "the core methodologies of the animator", which the source does not carry (CHECK F11); author's sentence to keep, re-cite or reword |
| chiou2023trusting | abstract | 0/0 | index | nothing | Checkpoint D needs the full text (BROWSER_LIST 9); on the abstract, no third party, "conflicting goals" with no owner named |
| cholodenko2014first | abstract | 0/0 | index | nothing | approved as full text but 403 (BROWSER_LIST 40); editor stays out of the APA until the title page is seen |
| dragicevic2011temporal | full_text | 10/10 | index | nothing | FACETS F9 lists "Chevalier" in place of Elmqvist; FACETS left alone |
| endsley2017from | full_text | 9/9 | index | nothing | `registered_year: 2016` and online date rest on triage, no record in the folder; version-of-record check (S4) open |
| epley2007seeing | abstract | 0/0 | index | nothing | not located by any open route (BROWSER_LIST 35) |
| flyverbom2016transparency | abstract | 0/0 | index | nothing | nothing |
| furniss2008art | metadata | 0/0 | index | nothing | §4.1 McLaren line still has no citable source (finding e); a copy of either edition needed (BROWSER_LIST 3) |

## Notes across the batch

- Four of the twenty are load-bearing on an abstract or a record only (ananny2018seeing, bettman1998constructive as anchors; chiou2023trusting, epley2007seeing as contrast/support). None is wrong, but the paper should mark those uses as resting on the abstract until copies arrive.
- Two full-text folders hold no registry record (anderl2024conversational, endsley2017from); both cards say so and take the imprint from the printed page. Endsley's `registered_year` is the only frontmatter value in the batch that no folder record supports.
- The Clark and Fischer BBS article is cited with a different year in two sources of this batch (Cameron 2022; Abercrombie 2023). It is the work behind the "depicted character with an unseen authority" move that matters for c9.

# S7 hand-check, batch 2 (Fable, 2026-11-05)

Twenty cards, `gambino2020building` to `magliano2011impact`. Each card was read against its local folder
(`~/iit-playground/dxd_animation_local/pdfs/<key>/`): frontmatter against the Crossref or OpenAlex record (or
the printed PDF header where no record exists), sha256 recomputed, every quotation grepped against the
`.txt` text layer and a fresh `pdftotext` extraction (two-column layouts rebuilt), every page locator checked
against the printed page, and each claim use read against what the source says. Cross-references to
OUTLINE, SOURCE, CHECK, FACETS, DECISIONS, BROWSER_LIST, CITED_WORKS and FETCH_LOG were opened and confirmed.

Verdicts: 20 index, 0 index after fix, 0 hold. Nothing changed in any card.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| gambino2020building | abstract | 0/0 (None) | index | nothing | nothing beyond the browser list |
| gnewuch2018faster | abstract | 0/0 (None) | index | nothing | OpenAlex's ECIS location lands on https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1112&context=ecis2018_rp, normally the AIS eLibrary PDF; the script never tried it; a browser may take the card to full text |
| gnewuch2022opposing | full_text | 11/11 | index | nothing | OUTLINE §4.1 (lines 144, 247) and CITED_WORKS row 31 call the paper "Typing delays in chatbots" (the file name); the delay is a wait before the reply, not a typing animation; fix is the author's (README rule 3) |
| gonzalez1996does | metadata | 0/0 (None) | index | nothing | nothing beyond the browser list (row 16) |
| guttman1998agent | abstract | 0/0 (None) | index | nothing | c1 contrast cannot be supported until the CBB stages are read (row 17); fallback he2003agent (reserve) |
| heer2007animated | metadata | 0/0 (None) | index | nothing | nothing beyond the browser list (row 15) |
| heider1944experimental | metadata | 0/0 (None) | index | nothing | JSTOR copy through the library (row 29) |
| hoerl2015seeing | abstract | 0/0 (None; abstract phrases verbatim) | index | nothing | OpenAlex also lists an accepted-version PDF at Warwick WRAP (wrap.warwick.ac.uk/50746/1/WRAP_Hoerl_ejop565.pdf) and a PhilPapers archive copy (HOESMA); either would answer DECISIONS finding (b), which the abstract leaves open |
| hollanek2023ai | full_text | 10/10 | index | nothing | nothing |
| horvitz1999principles | metadata | 0/0 (None) | index | nothing | nothing beyond the browser list (row 33) |
| jachimowicz2019when | partial | 10/10 | index | nothing | wording: "58 studies" (abstract, CHECK F5) vs "58 datasets from 55 studies" (p. 163); the step from endorsement to "defaults presuppose a fixed goal" is the paper's own inference |
| johnson2012beyond | full_text | 9/9 | index | nothing | SOURCE Pass 2 line 25 says "proves"; card and CHECK F5 recommend "shows" with Jachimowicz et al. (2019) as the evidence; the author's wording, the author's call. OJS republication's authorisation unconfirmed |
| jones2026animating | full_text | 11/11 | index | nothing | triage's "independent use of Silvio" holds only in part (Jones credits Stark 2023 with the same argument); §6 should say so |
| klein2006making | metadata | 0/0 (None) | index | nothing | nothing beyond the browser list (row 31) |
| lamarre2009anime | metadata | 0/0 (None) | index | nothing | chapter(s) on limited animation (row 25); Ruddell 2008 carries the claim meanwhile |
| lasseter1987principles | abstract | 0/0 (None; abstract phrases verbatim) | index | nothing | the principle list c8 needs is in no record read; full text (row 39) |
| lipshitz2001taking | abstract | 0/0 (None) | index | nothing | nothing beyond the browser list (row 42) |
| luger2016like | abstract | 0/0 (None; abstract phrases verbatim) | index | nothing | nothing beyond the browser list (row 37) |
| maeda2025anthropomorphism | full_text | 21/21 | index | nothing | (1) how §6 states the difference from Maeda & L. Stark's governance move (finding c); (2) whether the paper's single "animator" is a role many parties fill, against their three-layer network (c7); (3) Silvio 2010 vs 2019 attribution of the "projection of qualities" definition |
| magliano2011impact | abstract | 0/0 (None) | index | nothing | PMC3208769 accepted version (row 45); upgrade before §4.2 cites a finding |

## Notes

- The one locator that my page-matching script first flagged (Jachimowicz, "opt-out defaults lead to greater
  uptake … d = 0.68", p. 164) is correct: the sentence sits under "Results: effect size" on the page headed
  164; a near-duplicate sentence with V+ = 0.29 sits on p. 165. No change.
- Ruling 4 (the human-factors triads) names no card in this batch. The `maeda2025anthropomorphism` card
  nonetheless records what the source counts as third parties (corporate actors with interests of their own;
  interfaces that act on users; a named but unformalised three-layer network), which the author may want when
  ruling at Checkpoint D.
- Two cards (`hoerl2015seeing`, `maeda2025anthropomorphism`) carry an H1 title line above the four body
  sections. README does not prescribe one; `build_index.py --check` was not run here. Left as is.

# S7 hand-check, batch 3 (Fable, 2026-11-05)

Twenty cards: maier2022no … simon1955behavioral. Every quotation was re-read against the folder's text layer
(or, for shi2026siren, a fresh reading-order extraction of the held PDF, because the folder's .txt
interleaves the columns); every frontmatter field against the folder's Crossref, OpenAlex, CSL or Open
Library record; every sha256 recomputed. Verdicts: 18 index, 2 index after fix, 0 hold.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| maier2022no | full_text | 5/5 | index | nothing | nothing |
| may2003using | partial | 12/12 | index | nothing | abstract's "6 of the 10 classes" vs §6.2's seven classes is unreconciled in the parts read; quote §6.2–6.3 figures |
| mccloud1993understanding | metadata | 0/0 | index | nothing | nothing new (BROWSER_LIST row 27) |
| mori2012uncanny | abstract | 0/0 | index | nothing | nothing |
| natale2019if | full_text | 7/7 | index | nothing | untagged c3/c5 fit (opacity breeds narratives) offered by the card; decide whether to tag |
| ngai2004animatedness | metadata | 0/0 | index | nothing | author's name is in no record in the folder; confirm from the title page (row 4) |
| norman1986cognitive | metadata | 0/0 | index | nothing | anchor + load-bearing on metadata; the OpenAlex abstract the triage quoted (W4239943223) was never fetched; chapter is row 12 |
| payne1992behavioral | metadata | 0/0 | index | nothing | anchor rests on the title alone until read (row 10) |
| ruddell2008from | full_text | 5/5 | index | nothing | untagged c6 fit (suture, ms pp. 18–22); decide whether to tag |
| saracay2026beyond | partial | 9/9 | index | nothing | CoPref keeps the target fixed: supports "preference is constructed", cuts against "the goal moves"; rule on the c1 scope |
| schneider2018digital | abstract | 0/0 | index after fix | Caution "The 2016 work has no card in this run" → names `weinmann2016digital`, which exists and is approved (DECISIONS F6) | anchor + load-bearing on a one-sentence abstract; ACM 403 (FETCH_LOG 53), row 24; "no neutral way to present choices" unconfirmed |
| schwan2000do | full_text | 8/8 | index | nothing | second author's given name follows the OCR layer ("Barbel"); no Crossref/OpenAlex record in the folder to settle the umlaut |
| shanahan2023role | full_text | 10/10 | index | nothing | nothing |
| sheridan2002humans | metadata | 0/0 | index | nothing | author's name comes from the triage file, not the record (key OL828637A only); confirm from the book (row 14) |
| shi2026siren | partial | 12/12 | index | nothing | (1) arXiv v4 read, not the ACM version of record; (2) Shi et al. treat authorship as "diffuse" and keep the organisation accountable, which sits against the triad (c3, c7); decide whether §3.2 answers it |
| shneiderman1984response | abstract | 0/0 | index | nothing | anchor + load-bearing on an abstract; ACM 403 (FETCH_LOG 47), row 19 |
| siles2019mutual | abstract | 0/0 | index after fix | Caution "None of these were seen in the records read here" → the folder's openalex.json oa_url carries `ccc/12/4/499`; frontmatter stays blank (a URL path is not a bibliographic field) | DECISIONS F7's UCR fallback (handle 10669/79031) was never tried; FETCH_LOG 57 and 79 show only the OUP attempts |
| silvio2010animation | abstract | 0/0 | index | nothing | status cited, anchor, load-bearing, and every page locus (422, 428, 432) reaches the lab only through L. Stark (2024); read before quoting Silvio directly (row 2) |
| silvio2019puppets | metadata | 0/0 | index | nothing | (1) Alexy: Crossref says editor, the triage's Open Library reading says second author; the title page settles it. (2) p. 52 is quoted only through Stark (2024, p. 1664); cite as "quoted in Stark" until seen (row 1) |
| simon1955behavioral | metadata | 0/0 | index | nothing | nothing (end page unconfirmed; row 33) |

## Notes on method

- Loci: the two-column PDFs (maier, schwan, shanahan) have interleaved columns in the folder .txt, so a
  straight string match fails; each sentence was found by matching its prefix and reading the continuation
  in its own column. All were present. Page locators were confirmed from running heads or footers (may,
  schwan, shanahan), printed page numbers (saracay), manuscript footers (ruddell), or form-feed counts
  (natale, shi).
- Ruling 4 (the HF triads) names cameron2024social, stanton2006distributed, chiou2023trusting and
  oneill2022human, none in this batch. sheridan2002humans is the only F8 card here; it attributes no model
  to the book, so nothing had to be recorded.
- Four anchor, load-bearing cards in this batch rest on an abstract or a record alone: norman1986cognitive,
  schneider2018digital, shneiderman1984response, silvio2010animation (plus silvio2019puppets, metadata).
  Each card says so. They can be indexed, but the paper cannot lean on them until the browser copies arrive.

# S7 hand-check, batch 4 (Fable, 2026-11-05)

Cards simonson2008will through wertheimer2012experimental (17). Every quotation was searched in the folder's .txt text layer with line-break, hyphenation and ligature differences allowed; two-column layers were split by column before searching. Frontmatter was read against the registry record in the folder; sha256 values were recomputed. Note: `oneill2022human` has no card here (pointer), so ruling 4 is answered for `stanton2006distributed` only in this batch.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| simonson2008will | abstract | 0/0 (None); 3 abstract phrases match the records | index | nothing | nothing |
| siskind2024would | full_text | 11/11 | index | nothing | nothing new |
| slovic1995construction | metadata | 0/0 (None) | index | nothing | nothing |
| smith2008edit | full_text | 9/9, on the stated pages | index | nothing | nothing |
| smith2012attentional | metadata | 0/0 (None) | index | nothing | nothing |
| stanton2006distributed | full_text | 9/9, on the stated manuscript pages; third-party claims traced to pp. 3–7, 16, 26, 29 | index | nothing | Ruling 4: the source has no interested third party. Its agents are task roles (human and artefact) with "different, but potentially compatible" purposes (p. 5); no designer or deployer acts through the artefact on the user; the agents are modelled in task and propositional networks. Narrows "HF is dyadic", not "HF has no interested third party". Author rules at Checkpoint D. |
| stark2024animation | full_text | 19/19, on the stated PDF pages | index | nothing | (1) pp. 1663–1671 rest only on Maeda & L. Stark's reference list; no Crossref record in the folder; S8 DOI check to confirm. (2) CHECK.md places "structuring trope" at p. 1663 (it is p. 1664); OUTLINE §4.2 and triage tie the ELIZA effect to p. 1667 (its definition is p. 1665). (3) c7's singular "animator" stretches Stark's many animators, who include the user. |
| steinman2000phi | metadata | 0/0 (None) | index | nothing | nothing new (finding b waits on the read) |
| subramonyam2024bridging | partial | 9/9, on the stated PDF pages | index | nothing | Cite for the intention-stage gap, not a moving goal: the triage's mapping of "what the task should be" onto c1 is generous; the body defines that gap as "how to" procedures (p. 6). |
| tan2026impact | full_text | 13/13, on the stated PDF pages | index | nothing | nothing to decide; the arXiv stamp (2604.*, 9 Feb 2026) is odd and the ACM version settles it |
| thomas1981illusion | metadata | 0/0 (None) | index | nothing | 1981, the subtitle and the 1981 publisher have no record behind them this run (OL2924612W not in the folder); supply the edition or accept the marked entry |
| wadi2026shopping | partial | 10/10, on the stated pages | index | nothing | nothing |
| weinmann2016digital | full_text | 9/9, on the stated journal pages | index | nothing | nothing |
| weizenbaum1966eliza | abstract | 0/0 (None); paraphrase matches the abstract | index | nothing | nothing |
| wells1998understanding | metadata | 0/0 (None) | index | nothing | nothing |
| wertheimer1912experimentelle | metadata | 0/0 (None) | index | nothing | (1) registry row carries Sekuler's DOI 10.1068/p251243 for this key; S8 must not emit it. (2) URN route to the German scan untried (BROWSER_LIST row 54). |
| wertheimer2012experimental | metadata | 0/0 (None) | index | nothing | chapter record names no author, editor or translator; the book record or title page settles the credit |

Counts: 17 index, 0 index after fix, 0 hold. Nothing changed in any card beyond the appended Hand-check section.

# S7 hand-check, batch 5 (Fable, 2026-11-06)

One card, `wu2026ainimation`, read against `~/iit-playground/dxd_animation_local/pdfs/wu2026ainimation/`: the held arXiv v1 PDF (sha256 recomputed, matches provenance.txt and sha256.txt), its reading-order text layer for every quotation (whitespace collapsed, pages counted by form feed), and datacite.json, openalex.json and arxiv_abs.xml for the frontmatter. The full text was read, so the claim uses c4–c9 and the word checks (Stark, Silvio, Maeda, Johnston, Lasseter, Disney, puppet, animator, "Illusion of Life", principles, decision: zero hits in both layers) rest on the whole paper. I also read `library/GAP_CHECK.md` to answer whether its c9 wording must change given this card; I did not edit it.

Verdicts: 0 index, 1 index after fix, 0 hold.

| key | read_depth | loci found | verdict | changed | for the author |
|---|---|---|---|---|---|
| wu2026ainimation | full_text | 15/15, each on the stated PDF page | index after fix | (1) "(the paper does not state their order)" → the paper's own "completed … in succession" (§5, PDF p. 6); (2) Caution: Experiment 2 confidence sentence is on PDF p. 8, not p. 7 | (a) whether "in succession" fixes the order 1→2→3 is a reading, not a statement in the paper. (b) The card keeps c4, c6, c7 bullets (all "not supported") for tags absent from its `claims` list; README asks one bullet per claim tag. (c) GAP_CHECK c9: see below. |

## GAP_CHECK.md, claim c9, given this card

The c9 verdict holds and the suggested §6 sentence can stay as written. The full text confirms what the abstract showed: Wu and Masson never use "decision", cite no animation theory, and never read the LLM as a character. Their "animation" is UI transition animation in the Heer & Robertson and Chevalier line (card, Caution, first bullet), so they take neither half (A) nor half (B) of c9. They do take something smaller, which GAP_CHECK already concedes: interface animation of AI responses as a tested design method.

Four wording updates, all small, for the author to make or decline:

1. Part 2, narrowing point 2, "Their abstract stops short of decisions and of the character reading … Card it before §6 is drafted": the card now exists and reads the full text, so "abstract" → "full text" and the instruction is done.
2. Hits table, first row: the paper and all three records spell the first author "Jiaqi Wu", not "Jia-Qi Wu"; "carded? **No**" → carded (`wu2026ainimation`, full_text, status candidate); the row's reading can rest on the full text rather than the abstract.
3. Verdict paragraph, "most of this check rests on abstracts": now true of every leg except Wu & Masson.
4. The §6 sentence "Interface research animates LLM output to help users review it (Wu & Masson, 2026)" is accurate, but the card's Caution asks §6 to say outright that "animation" there means UI transitions, not Stark's sense, so a reviewer does not read the sentence as the animation reading already taken. One clause would do it.

One addition beyond c9. Wu and Masson pose the pacing question directly — "Should AI answers be shown as fast as possible using technology-driven animations, or would slower but well-crafted animations be preferable?" (PDF p. 2, §2.1) — and answer it with the only lab datum the library holds for a crafted, slower display beating an instant one (n = 16, review tasks). That bears on c8 and OUTLINE §4.1/§5 more than on c9, as GAP_CHECK's "For the author" already notes.
