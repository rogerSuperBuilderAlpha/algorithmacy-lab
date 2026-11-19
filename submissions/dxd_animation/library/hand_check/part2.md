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
