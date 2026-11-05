# Fable's decisions on the triage files — run dxda-lib-2026-11

> **[Written by Claude (Fable), 2026-11-05.]** The approved list per facet, with the reasons where I
> departed from a triage file. S4 fetches from this file; S5 writes from it. Ceiling for the run: **60 new
> cards**, with the 17 upgrades outside it (Checkpoint A, ruling 3). The author holds no books (ruling 4), so
> every book anchor is a metadata card and a `BROWSER_LIST.md` row. Every identifier below is copied from a
> triage file, which recorded a Crossref, OpenAlex or Open Library record opened on 2026-11-05; nothing comes
> from memory. Where a triage file gave two routes, the one named first is the one S4 tries first.

## The count

The six triage files propose 62 new cards. Two works sit in two files: `shanahan2023role` (F3 #3 and G #2)
and `maeda2025anthropomorphism` (F1 #8 and G #1). Each is carded once with both facet tags, which gives 60.
`stark2024animation` is a cited work (CITED_WORKS row 23: no card, no registry row), the library's own anchor,
and its PDF and text layer are already in `~/iit-playground/dxd_animation_local/pdfs/stark2024animation/`. No
triage file lists it because FACETS treats it as "this library's own first card". It is a new card and it
counts, which makes 61. To hold the line at 60 I move **`miller1968response`** (F4 #7, the stretch slot its
own triage file named first to cut) to reserve: Shneiderman (1984) reviews the response-time line Miller
opened, and nothing in the outline rests on Miller. If the author rules at Checkpoint B that
`stark2024animation` sits outside the ceiling as a pre-existing anchor, Miller returns.

| Facet | Approved new | Listed under | Upgrades | Writer: opus / sonnet (new) |
|---|---|---|---|---|
| F1 | 9 | F1 (incl. `maeda2025anthropomorphism` [F1, G] and `stark2024animation` [F1, F3, G]) | 5 | 8 / 1 |
| F2 | 7 | F2 | 3 | 2 / 5 |
| F3 | 6 | F3 (incl. `shanahan2023role` [F3, G]) | 3 | 0 / 6 |
| F4 | 6 | F4 | 0 | 0 / 6 |
| F5 | 8 | F5 | 3 | 3 / 5 |
| F6 | 5 | F6 | 1 | 0 / 5 |
| F7 | 4 | F7 | 0 | 1 / 3 |
| F8 | 5 | F8 | 1 | 2 / 3 |
| F9 | 6 | F9 | 1 | 0 / 6 |
| F10 | 2 | F10 | 0 | 0 / 2 |
| G | 2 | G (the other two G cards are counted under F1 and F3) | 0 | 0 / 2 |
| **Total** | **60** | | **17** | **16 / 44** |

Upgrades: 6 opus, 11 sonnet. Run-wide: 77 cards, 22 opus, 55 sonnet.

**Writer rule (S5).** `opus` writes books, book chapters, dense theory, non-English text and the cards the
thesis rests on (Silvio, Ngai, Bukatman, Furniss, both Wertheimers, L. Stark 2024 and his 2025 sequel, Ananny
& Crawford, Payne/Bettman/Johnson and Bettman/Luce/Payne, Cholodenko, Hoerl, Norman 1986, Sheridan, Chiou &
Lee, Epley et al.). `sonnet` writes full-text open journal and proceedings articles. A metadata card is short
whichever model writes it; the model is set by the work, so that the same writer takes the card up to full
text when a browser copy arrives.

## Swaps proposed by the triage agents

| Facet | Proposal | Ruling | Reason |
|---|---|---|---|
| F5 | Lichtenstein & Slovic 2006, Klein 1993, Klein 1998 → reserve; add `chen2026do`, `subramonyam2024bridging`, `simonson2008will` | **Approved** | The author holds no books, so all three would be metadata cards saying only that the work exists. Bettman et al. 1998 is reprinted as ch. 17 of Lichtenstein & Slovic (10.1017/cbo9780511618031.018), so the collection's claim is carded through the article. Lipshitz et al. 2001 (open) carries recognition-primed decision, and `kahneman2009conditions` (dxdfound, full) carries Klein's own words. The three additions give F5 what it lacked: a chatbot measured at goal formation (Chen), Norman's gulfs carried into LLM prompting (Subramonyam), and the contrast that preferences may be inherent (Simonson). All three Klein/Lichtenstein records stay confirmed in reserve. |
| F3 | Holtgraves et al. 2007 and Turkle 1984 → reserve | **Approved** | Holtgraves has no abstract on any service and is closed, so it could only be a metadata card; Appel et al. 2012 (open) tests the same cue-versus-agency question. Turkle is a book. Natale 2019, Shanahan 2023, Gambino 2020 and Abercrombie 2023 fill the ELIZA, persona and contrast slots with open text. |
| F7–F8 | Hollnagel & Woods 2005 → reserve | **Approved** | FACETS's "still two parties" is unread, and a metadata card cannot test it. `klein2004ten`, `klein2005common` and `christoffersenwoods2002` (full-text pointers) carry joint activity. Endsley 2017 (held PDF) takes the slot and states the dyad from inside HF. |
| F2 | Cutting 2005 → reserve; `magliano2011impact` takes the slot | **Approved** | The chapter has no record (S3 rule 2), and Magliano & Zacks 2011 (open, PMC) joins §4.2's (a) continuity editing and (b) event segmentation in one paper. Cutting stays in reserve on the volume record (OL18489457W). |
| F1 | Sifianos 1995 stays in reserve | **Approved, with a probe** | No record on Crossref, OpenAlex or Open Library, so it cannot be carded (S3 rule 2). The McLaren line in §4.1 now has no confirmed source except Furniss 2008 (closed). S4 fetches the open reserve `century2022norman` (10.7551/mitpress/10818.003.0005, CC BY-NC-ND) and reports whether its text quotes "movements that are drawn" with a source; promotion is the author's call at Checkpoint B (finding e). |
| F4 | `miller1968response` → reserve (my cut, see above) | **Decided here** | Holds the ceiling at 60 with `stark2024animation` counted. |
| F7 | `ananny2018seeing` takes one of F7's three slots as a new full-read card | **Approved** | FACETS planned a pointer, but all seven lab cards are abstract or metadata and OUTLINE §3.2 and §5 lean on it. The key already exists in four libraries; the new card declares them under `prior_cards` (README, "Keys"). |
| G | 4 new (one past FACETS's stretch) | **Approved at 2 listed + 2 shared** | Maeda & L. Stark and Shanahan are counted under F1 and F3; Jones 2026 and Siskind et al. 2024 are G's own. The run stays at 60. |

Keys as the triage files set them (`natale2019if`, `appel2012does`, `schwan2000do`, `chen2026do`,
`maier2022no`, `gonzalez1996does`, `jachimowicz2019when`, `schneider2018digital`): approved. README's key
rule skips articles only; S5 does not rename.

## F1 — approved (9), from `triage/F1-F2.md`

| key | read as (depth + identifier / OA route) | decision | writer |
|---|---|---|---|
| `stark2024animation` | full_text, held: `dxd_animation_local/pdfs/stark2024animation/` (PDF + text layer, provenance.txt); 10.1145/3630106.3658995 | **in**, anchor, c4, c6, c7; `facets: [F1, F3, G]`. The library's first card; the loci CHECK already names (pp. 1663, 1664, 1667, 1668) are re-read from the held copy, not copied from CHECK. | opus |
| `silvio2010animation` | abstract (Crossref carries one); 10.1111/j.1548-1395.2010.01078.x → BROWSER_LIST (Wiley) | **in**, anchor, c4, c7. The projection/introjection contrast and "hard to separate" (CHECK F4). Full text when the browser copy arrives. | opus |
| `silvio2019puppets` | metadata; 10.1515/9780824880989, OL21338441W → BROWSER_LIST (p. 52) | **in**, anchor, c4, c7. The definition Stark quotes (CHECK F3). The card records that the paper's quotation comes through Stark 2024 p. 1664 until p. 52 is seen; checks the second-author question on the title page. | opus |
| `ngai2004animatedness` | metadata; 10.4159/9780674041523-003 → BROWSER_LIST (pp. 89–125) | **in**, support, c7, `load: exists` until read. The author approved it as an F1 anchor; the card keeps the citation honest by saying no text was read. | opus |
| `bukatman2012poetics` | metadata; 10.1525/9780520951501, OL21528072W → BROWSER_LIST | **in**, support, c7, `load: exists` until read. Same rule as Ngai. | opus |
| `furniss2008art` | metadata; OL25196771W (2008), OL767180W (1998) → BROWSER_LIST (the McLaren page) | **in**, support, c5. The only recorded route to McLaren's definition (CHECK F1). Key becomes `furniss1998art` if the 1998 edition is the one seen. | opus |
| `cholodenko2014first` | full_text, open (bronze): Duke chapter PDF; 10.1215/9780822376811-007; fallback De Gruyter 10.1515/9781478091950-008 | **in**, support, c5, c7. F1's open text of animation theory; claims follow the read. | opus |
| `ruddell2008from` | full_text, open (Brunel repository, version to be recorded); 10.1177/1746847708091890 | **in**, support, c5, c8. Gives limited animation an open text while Lamarre stays closed. | sonnet |
| `maeda2025anthropomorphism` | full_text, open (AAAI OJS); 10.1609/aies.v8i2.36664 | **in**, contrast, c4, c6, c7, c9; `facets: [F1, G]`. The closest prior (G verdict) and the plural-animator challenge to §4.3. Caution separates it from `stark2024animation` and from D. Stark (CHECK F8). | opus |

Reserve: `sifianos1995definition` (library request only; no record), `century2022norman` (open; S4 probes it
for McLaren's wording), `cholodenko1991illusion`, `starosielski2011movements`, `gunning2007moving`,
`hosseinishakib2019puppet`. Left out as the triage file lists.

## F2 — approved (7), from `triage/F1-F2.md`

| key | read as (depth + identifier / OA route) | decision | writer |
|---|---|---|---|
| `wertheimer2012experimental` | metadata; 10.7551/mitpress/9222.003.0003 (book 10.7551/mitpress/9222.001.0001) → BROWSER_LIST | **in**, anchor, c6. The English text to gloss the German against (README rule 7); the same writer takes the 1912 upgrade. Editor confirmed from the title page. | opus |
| `smith2012attentional` | abstract; 10.3167/proj.2012.060102 → BROWSER_LIST (Berghahn). Smith's 2006 Birkbeck thesis is background only, never quoted as the article | **in**, anchor, c6 | sonnet |
| `smith2008edit` | full_text, open (gold, CC BY); 10.16910/jemr.2.2.6 | **in**, support, c6 | sonnet |
| `schwan2000do` | full_text, held: `S/notebook_sources/C_experiment/Schwan et al 2000 …pdf` (copy with provenance.txt); 10.3758/bf03213801; fallback Springer PDF | **in**, support, c6 | sonnet |
| `magliano2011impact` | full_text, open (PMC 3208769); 10.1111/j.1551-6709.2011.01202.x | **in**, support, c6 (replaces Cutting 2005) | sonnet |
| `hoerl2015seeing` | full_text, open (Wiley bronze); 10.1111/j.1468-0378.2012.00565.x; `registered_year: 2012` | **in**, contrast, c6. Finding (b). | opus |
| `steinman2000phi` | full_text, open (ScienceDirect bronze; BROWSER_LIST if walled); 10.1016/s0042-6989(00)00086-9 | **in**, contrast, c6. Finding (b). | sonnet |

Reserve: `hochberg1992film`, `cutting2005perceiving` (volume record only), `berliner2011illusion`,
`zacks2010brains` (open), `langkjaer2023matching`, `galifret2006visual`, `sekuler1996motion` (the DOI the old
Wertheimer card mistook; the browser session for the MIT volume can take its chapter too),
`anderson1996reality`.

## F3 — approved (6), from `triage/F3-F4.md`

| key | read as (depth + identifier / OA route) | decision | writer |
|---|---|---|---|
| `weizenbaum1966eliza` | full_text, open (ACM bronze; BROWSER_LIST if refused); 10.1145/365153.365168 | **in**, anchor, c4, c6. The card names which object it read (1966 or the 1983 reprint 10.1145/357980.357991). | sonnet |
| `natale2019if` | full_text, open (author draft, Turin IRIS; version of record closed); 10.1177/1461444818804980; `registered_year: 2018` | **in**, support, c4, c6 | sonnet |
| `shanahan2023role` | full_text, open (Nature bronze); 10.1038/s41586-023-06647-8 | **in**, contrast, c4, c7, c9; `facets: [F3, G]`. The rival role-play frame. | sonnet |
| `appel2012does` | full_text, open (gold, CC BY); 10.1155/2012/324694 | **in**, support, c6 (replaces Holtgraves) | sonnet |
| `gambino2020building` | full_text, open (diamond); 10.30658/hmc.1.5 | **in**, contrast, c6 | sonnet |
| `abercrombie2023mirages` | full_text, open (ACL, CC BY); 10.18653/v1/2023.emnlp-main.290 | **in**, contrast, c4, c8. Kept: F3's stretch slot is cheaper than Miller's and §5 needs the "damp the character" position stated. | sonnet |

Reserve: `holtgraves2007perceiving`, `turkle1984second`, `ciston2026inventing` (open), `placani2024anthropomorphism`
(open), `peter2025benefits` (open), `maeda2024when` (open; also G R2), `riehm2026interpersonal` (open),
`lombard2021social` (open), `johnson2004experience`.

## F4 — approved (6), from `triage/F3-F4.md`

| key | read as (depth + identifier / OA route) | decision | writer |
|---|---|---|---|
| `gnewuch2022opposing` | full_text, held: `S/notebook_sources/A1_review_agents_streams/Gnewuch et al 2022 …pdf` (EconStor published version, sha256 f7fea1e4…); 10.1007/s12599-022-00755-x | **in**, anchor, c5. Caution: OUTLINE §4.1 and CITED_WORKS row 31 call it "Typing delays in chatbots", the file's name, not the title. | sonnet |
| `tan2026impact` | full_text, held text (arXiv 2604.06183v1, sha256 98931690…); 10.1145/3772318.3790716; S4 tries the ACM CC BY version | **in**, contrast, c5, c6 | sonnet |
| `anderl2024conversational` | full_text, held text (PMC11272919, sha256 63705927…); 10.1038/s41598-024-67829-6 | **in**, support, c5, c6. Card says the dynamic condition was recorded screencasts. | sonnet |
| `bhat2025dynamic` | full_text, held PDF (sha256 714377dc…); 10.1145/3708359.3712131 | **in**, support, c4, c5 | sonnet |
| `gnewuch2018faster` | full_text if AIS opens (aisel.aisnet.org/ecis2018_rp/113; Newcastle handle 1959.13/1404369), else metadata; OpenAlex W2906833531, no DOI | **in**, contrast, c5, c6. FACETS decision 7's condition is met. Venue cited as ECIS 2018 from the object. | sonnet |
| `shneiderman1984response` | full_text, open (ACM bronze; BROWSER_LIST if refused); 10.1145/2514.2517 | **in**, anchor, c5. The HF baseline. | sonnet |

Reserve: `miller1968response` (10.1145/1476589.1476628; returns if the ceiling allows), `mackenzie1993lag`,
`gnewuch2018chatbot` (open; swap for Miller if §4.1 discusses the indicator itself), `kim2026seconds`,
`zhang2024explaining`, `zhou2025thoughtful`, `abbas2021making`, `wang2026more`, `lew2018interactivity`,
`mitsuno2026non`. Xie et al. 2024 (WaitGPT) is handed to F8 as a lead, not carded.

## F5 — approved (8), from `triage/F5-F6.md`

| key | read as (depth + identifier / OA route) | decision | writer |
|---|---|---|---|
| `payne1992behavioral` | metadata (no abstract on OpenAlex); 10.1146/annurev.ps.43.020192.000511 → BROWSER_LIST | **in**, anchor, c1. Annual Reviews sits behind nearly every university login, so the browser copy is likely. | opus |
| `bettman1998constructive` | abstract; 10.1086/209535 → BROWSER_LIST | **in**, anchor, c1, c2. Caution names the 2006 reprint chapter. | opus |
| `lipshitz2001taking` | full_text, open (green, UCF STARS record 8094; S4 confirms a PDF is attached; CiteSeerX second); 10.1002/bdm.381 | **in**, support, c1, c2. Carries RPD for the reserve Klein works. | sonnet |
| `norman1986cognitive` | abstract; 10.1201/9780367807320-3 → BROWSER_LIST (ch. 3, pp. 31–62) | **in**, anchor, c1 | opus |
| `chen2026do` | abstract; 10.1002/mar.70189 → BROWSER_LIST | **in**, anchor, c1 | sonnet |
| `subramonyam2024bridging` | full_text, open (arXiv 2309.14459); 10.1145/3613904.3642754 | **in**, support, c1, c2 | sonnet |
| `saracay2026beyond` | full_text, open (arXiv 2606.30863); 10.48550/arxiv.2606.30863, W7166830829, `type: preprint` | **in**, support, c1. Kept over Miller: "agents assume an expert user with well-formed preferences" is c1's claim in agent terms and no other card carries it. | sonnet |
| `simonson2008will` | full_text, open (SSRN; BROWSER_LIST if blocked); 10.1016/j.jcps.2008.04.002 | **in**, contrast, c1 | sonnet |

Reserve: `klein1998sources`, `klein2010rapid`, `klein1993recognition` (W1623168575), `lichtenstein2006construction`
(the overview chapter 10.1017/cbo9780511618031.002 if a slot opens), `warren2011values` (open). Pointers:
`haublmurray2003` (research, abstract only; an upgrade for that library, not a card here),
`kahneman2009conditions`.

## F6 — approved (5), from `triage/F5-F6.md`

| key | read as (depth + identifier / OA route) | decision | writer |
|---|---|---|---|
| `weinmann2016digital` | full_text, open (Springer hybrid; BROWSER_LIST if walled again); 10.1007/s12599-016-0453-1 | **in**, anchor, c1. CHECK F6. | sonnet |
| `schneider2018digital` | full_text, open (ACM hybrid; BROWSER_LIST if 403 again); 10.1145/3213765 | **in**, anchor, c1. Key avoids the registry homonym `schneider2018`. | sonnet |
| `jachimowicz2019when` | full_text, open (Cambridge Core hybrid); 10.1017/bpp.2018.43 | **in**, anchor, c1. CHECK F5's evidence; the *d* = 0.68 and 58 studies are re-read from the card's own copy. | sonnet |
| `shi2026siren` | full_text, open (ACM hybrid); 10.1145/3772318.3791149 | **in**, support, c1 | sonnet |
| `maier2022no` | full_text, open (PNAS hybrid; UvA-DARE CC BY copy as fallback); 10.1073/pnas.2200300119 | **in**, contrast, c1. Pairs with the pointer `mertens2022effectiveness` (dxdfound, full; cite the 2022 correction's figures). | sonnet |

Reserve: `szaszi2022no` (open), `dellavigna2022rcts`, `ersoy2026investigating` (open), `ilyankou2026scenic`
(open), `caraban2019ways`, `jesse2021digital` (open). Pointer added for POINTERS.md: `mertens2022effectiveness`.

## F7 — approved (4), from `triage/F7-F8.md`

| key | read as (depth + identifier / OA route) | decision | writer |
|---|---|---|---|
| `ananny2018seeing` | full_text only via the browser (SAGE; no OA copy on OpenAlex or Unpaywall), else abstract; 10.1177/1461444816676645; `registered_year: 2016`; `prior_cards` lists the seven lab cards the triage file names | **in**, anchor, c3, c8. Finding (d). | opus |
| `flyverbom2016transparency` | full_text, open (IJoC diamond); OpenAlex W2908084374, no DOI | **in**, support, c3, c8. Not `flyverbometal2016` (research). | sonnet |
| `siles2019mutual` | full_text, open (OUP bronze; UCR handle 10669/79031 as fallback); 10.1093/ccc/tcz025 | **in**, contrast, c3, c6 | sonnet |
| `hollanek2023ai` | full_text, open (Springer CC BY; Cambridge Apollo fallback); 10.1007/s00146-020-01110-y; `registered_year: 2020` | **in**, support, c8, c3 | sonnet |

Reserve: `felzmann2019transparency` (open), `nguyen2022transparency` (open), `devrio2022toward` (open),
`gillespie2010politics` (an upgrade only if §3.2 defines "platform"; open green copy). Pointers for
POINTERS.md as the triage file lists (seamful design, folk theories, Pasquale as exists-only).

## F8 — approved (5), from `triage/F7-F8.md`

| key | read as (depth + identifier / OA route) | decision | writer |
|---|---|---|---|
| `sheridan2002humans` | metadata; OL4274945W (editions OL7613807M Wiley, OL9392247M HFES) → BROWSER_LIST | **in**, contrast, c3, `load: exists`. With §3.2 softened, the dyad is cited from `parasuraman2000types` (full) and Endsley 2017 (held); Sheridan stands as the standard reference only until read. | opus |
| `cameron2024social` | full_text, open (Springer CC BY; PMC11842407); 10.1007/s12369-023-01048-3; `registered_year: 2023` | **in**, contrast, c3, c7, c9. Finding (a). Not Lindsey D. Cameron. | sonnet |
| `stanton2006distributed` | full_text, open (Brunel submitted version; journal pagination noted where shown); 10.1080/00140130600612762 | **in**, contrast, c3, c7. Finding (a). | sonnet |
| `chiou2023trusting` | full_text only via the browser (SAGE), else abstract; 10.1177/00187208211009995; `registered_year: 2021` | **in**, contrast, c3, c7. Finding (a). | opus |
| `endsley2017from` | full_text, held: `S/notebook_sources/B_theory/Endsley 2017 - From here to autonomy.pdf` (copy with provenance.txt; S4 checks it is the version of record); 10.1177/0018720816681350; `registered_year: 2016` | **in**, support, c3 (replaces Hollnagel & Woods). Subtitle from the title page only. | sonnet |

Reserve: `hollnagel2005joint`, `afgiansyah2026ai` (open), `natale2021communicating` (open), `johnson2014coactive`
(open), `janssen2019history` (open), `mcneese2018teaming`, `miller2007designing`. Pointer to add to
POINTERS.md: `hohenstein2020ai` (monograph, full; FACETS omits it).

## F9 — approved (6), from `triage/F9-F10.md`

| key | read as (depth + identifier / OA route) | decision | writer |
|---|---|---|---|
| `chevalier2016animations` | full_text, open (HAL hal-01322962); 10.1145/2909132.2909255 | **in**, anchor, c8. CHECK F11: interface roles, not the animator's craft. | sonnet |
| `heer2007animated` | abstract; 10.1109/tvcg.2007.70539 → BROWSER_LIST | **in**, support, c8 | sonnet |
| `dragicevic2011temporal` | full_text, open (HAL inria-00556177); 10.1145/1978942.1979233 | **in**, support, c8, c5. Caution: FACETS lists "Chevalier" where the record has Elmqvist. | sonnet |
| `may2003using` | full_text, open (White Rose eprint 470); 10.1207/s15327051hci1804_1 | **in**, support, c8, c5 | sonnet |
| `gonzalez1996does` | abstract; 10.1145/238386.238396 → BROWSER_LIST | **in**, support, c8, c9 (replaces Baecker & Small, which has no chapter record). The card keeps "animation" (moving imagery in a DSS) apart from the character sense. | sonnet |
| `ash2018digital` | full_text, open (Durham accepted manuscript); 10.1177/0263775818767426 | **in**, contrast, c8, c1 | sonnet |

Reserve: `baecker1990animation` (volume OL25220275W; metadata card possible if the author wants the origin
cited directly), `huhtala2010animated`, `thomas2001applying`, `gonzalez1997animation`, `avilamunoz2021communicative`
(open), `dehn2000impact`, `lewis2026invisible` (open).

## F10 — approved (2), from `triage/F9-F10.md`

| key | read as (depth + identifier / OA route) | decision | writer |
|---|---|---|---|
| `guttman1998agent` | abstract; 10.1017/s0269888998002082 → BROWSER_LIST | **in**, contrast, c1. The card tests whether the CBB model lets the buyer return to need identification; if the text leaves it open, `he2003agent` (reserve) is read next. | sonnet |
| `wadi2026shopping` | full_text, open (arXiv 2609.28372); 10.48550/arxiv.2609.28372, W7214217042, `type: preprint` | **in**, support, c1, c3 | sonnet |

Reserve: `he2003agent`, `tafesse2026comparison` (held PDF), `kim2023decisions` (open), `debellis2020autonomous`
(open), `moukas2000agent`, `luo2026ai`. Pointer: `alavi2026when`, not `alavinozari2026`.

## G — approved (2 listed here; 4 carded), from `triage/G.md`

| key | read as (depth + identifier / OA route) | decision | writer |
|---|---|---|---|
| `maeda2025anthropomorphism` | see F1 | counted under F1; `facets: [F1, G]` | opus |
| `shanahan2023role` | see F3 | counted under F3; `facets: [F3, G]` | sonnet |
| `jones2026animating` | full_text, open (Cambridge Core hybrid via the OpenAlex oa_url); 10.1017/s0267190526100312 | **in**, support, c4, c6, c9 | sonnet |
| `siskind2024would` | full_text, open (Frontiers gold); 10.3389/frobt.2024.1256937 | **in**, contrast, c8, c9. The structural twin of c8 with the opposite aim; §5's foil. | sonnet |

Reserve: `so2026beyond` (open; promote over Siskind if §5 wants an LLM-specific contrast), `maeda2024when`,
`hau2026prosopopoeia`, `bernini2025ai`, `keane2026talking`. S9 opens the abstract of Maeda & Buening 2026
(10.1145/3805689.3812282) before `GAP_CHECK.md` closes. The G verdict (finding c) is logged there with the
Semantic Scholar leg marked as failed (429).

## The 17 upgrades (outside the ceiling)

Each is a new card here with `prior_cards: [<dxd_animator key>]`; the dxd_animator file is left alone
(Checkpoint A, ruling 2 and 5). All 17 keys exist in `../../dxd_animator/literature/library/cards/` (checked
today).

| key | facets | read as (depth + identifier / OA route) | writer |
|---|---|---|---|
| `thomas1981illusion` | F1 | metadata; OL2924612W (author field garbled; the card takes the title page) → BROWSER_LIST | opus |
| `lamarre2009anime` | F1 | metadata; OL17203968W → BROWSER_LIST | opus |
| `wells1998understanding` | F1 | metadata; OL2708440W (Crossref 10.4324/9781315004044 is the 2013 e-edition) → BROWSER_LIST | opus |
| `lasseter1987principles` | F1, F9 | full_text, open (ACM bronze): **10.1145/37401.37407**, the SIGGRAPH '87 proceedings record (W2121378366). The old card and the registry give **10.1145/37402.37407**, the *ACM SIGGRAPH Computer Graphics* 21(4) record (W2999276620), which is closed. Both are Crossref records of the same paper, pp. 35–44. The card's `doi` is the one read (37401); Caution records the 37402 record as the journal-issue DOI the prior card used. | sonnet |
| `mccloud1993understanding` | F1 | metadata; OL276032W → BROWSER_LIST | opus |
| `wertheimer1912experimentelle` | F2 | full_text, German first (README rule 7): **OpenAlex W3088045382** (Wertheimer, 1912, vol. 61 issue 3, pp. 161–265; no DOI). Route: the record's URN https://nbn-resolving.org/urn:nbn:de:kobv:11-717944 (digi-hub.de viewer, BV049313576); the old card's gestalttheory.net scan is the second route. Caution records that the dxd_animator card's DOI 10.1068/p251243 resolves to Sekuler 1996 (ruling 5). | opus |
| `anderson1993myth` | F2 | metadata until the browser copy; OpenAlex W165434426, ERIC EJ477391, no DOI → BROWSER_LIST | sonnet |
| `heider1944experimental` | F2, F3 | metadata until the browser copy; 10.2307/1416950 → BROWSER_LIST | sonnet |
| `epley2007seeing` | F3 | abstract; 10.1037/0033-295x.114.4.864; OA route not recorded in triage, S4 checks; BROWSER_LIST if closed | opus |
| `mori2012uncanny` | F3 | abstract; 10.1109/mra.2012.2192811; S4 checks the route; BROWSER_LIST if closed | sonnet |
| `luger2016like` | F3 | abstract; 10.1145/2858036.2858288; S4 tries ACM; BROWSER_LIST if refused | sonnet |
| `slovic1995construction` | F5 | abstract until the browser copy; 10.1037/0003-066x.50.5.364 (closed) → BROWSER_LIST | sonnet |
| `klein2006making` | F5 | abstract until the browser copy; 10.1109/mis.2006.75 (closed) → BROWSER_LIST | sonnet |
| `simon1955behavioral` | F5 | metadata or abstract until the browser copy; 10.2307/1884852 (closed; Crossref gives first page 99 only) → BROWSER_LIST | sonnet |
| `johnson2012beyond` | F6 | full_text if the UNBC OJS copy (article 1264/1080) or the EUR record is this paper and an authorised republication (S4 confirms), else abstract (OpenAlex now carries the authors' abstract); 10.1007/s11002-012-9186-1 → BROWSER_LIST otherwise | sonnet |
| `horvitz1999principles` | F8 | abstract until the browser copy; 10.1145/302979.303030 (closed on OpenAlex and Unpaywall) → BROWSER_LIST | sonnet |
| `chang1993animation` | F9 | abstract until the browser copy; 10.1145/168642.168647 (closed) → BROWSER_LIST | sonnet |

## Metadata-only cards (author holds no books)

A metadata card says only that the work exists (`## Loci` = None, `load: exists` unless the paper's claim
rests on it, in which case Caution says the claim is unread). Each of these is still worth carding, for the
reason given; the card is what carries the BROWSER_LIST request and turns into a read card when the copy
arrives.

| key | why it is still worth a card |
|---|---|
| `silvio2019puppets` | The paper quotes p. 52 through Stark; the card records that chain and asks for the page. Top of the browser list. |
| `ngai2004animatedness` | Author-approved F1 anchor for c7. The card keeps the citation at `exists` until the chapter is read. |
| `bukatman2012poetics` | Same as Ngai. |
| `furniss2008art` | The only recorded route to McLaren's definition; the card holds the request for the page. |
| `wertheimer2012experimental` | The gloss text for the German; MIT Press ebook through the library. |
| `payne1992behavioral` | First statement of constructive processing; Annual Reviews is behind most logins. |
| `sheridan2002humans` | Standard reference for the dyad; `exists` only, since the softened §3.2 no longer rests on it. |
| `thomas1981illusion` (upgrade) | §5 cites the principles (CHECK F11); load-bearing once read. |
| `lamarre2009anime` (upgrade) | Limited animation as style; Ruddell supplies the open text meanwhile. |
| `wells1998understanding` (upgrade) | Reference for terms; weak, but outside the ceiling and already a dxd_animator card. |
| `mccloud1993understanding` (upgrade) | Closure between panels (c6); same standing as Wells. |
| `anderson1993myth` (upgrade) | CHECK F12 names it; JSTOR or ERIC through the library. |
| `heider1944experimental` (upgrade) | The co-optive mechanism before any character is drawn; JSTOR through the library. |
| `simon1955behavioral` (upgrade) | If no abstract reaches the record; JSTOR through the library. |

Thirteen metadata cards (7 new, 6 upgrades), fourteen if Simon 1955 yields no abstract. The abstract-depth
closed works (Silvio 2010, Smith 2012, Bettman 1998, Norman 1986, Chen 2026, Heer & Robertson, González 1996,
Guttman et al., and Ananny & Crawford and Chiou & Lee if the browser fails) are on the same list but carry
their abstracts.

## BROWSER_LIST seed

Works whose OA route is closed or likely bot-walled. The author downloads these by hand; S4 copies
`FETCH_LOG.tsv` outcomes into `BROWSER_LIST.md` and keeps this order. "Page" is what the paper needs first.

**Closed outright — new cards (17)**

| # | key | identifier | page or part the paper needs |
|---|---|---|---|
| 1 | `silvio2019puppets` | 10.1515/9780824880989; OL21338441W | p. 52 (the definition Stark quotes), and the chapter around it |
| 2 | `silvio2010animation` | 10.1111/j.1548-1395.2010.01078.x | whole article, pp. 422–438; p. 422 ("structuring trope"), p. 428 ("illusion of life"), p. 432 ("hard to separate") |
| 3 | `furniss2008art` | OL25196771W (2008 rev. ed.); OL767180W (1998) | the page reprinting McLaren's three-part definition (page unknown; CHECK F1) |
| 4 | `ngai2004animatedness` | 10.4159/9780674041523-003 | ch. "Animatedness", pp. 89–125 |
| 5 | `bukatman2012poetics` | 10.1525/9780520951501; OL21528072W | the passage on animated spirits and the animating spirit (not yet located; start with the introduction) |
| 6 | `wertheimer2012experimental` | 10.7551/mitpress/9222.003.0003 (book 10.7551/mitpress/9222.001.0001) | the whole chapter; Sekuler's chapter 10.7551/mitpress/9222.003.0005 in the same session |
| 7 | `smith2012attentional` | 10.3167/proj.2012.060102 | whole article, pp. 1–27 |
| 8 | `ananny2018seeing` | 10.1177/1461444816676645 | whole, pp. 973–989; the ten limitations and the "across, not inside" passage |
| 9 | `chiou2023trusting` | 10.1177/00187208211009995 | whole, pp. 137–165; the relational framing and "co-operators of automation" |
| 10 | `payne1992behavioral` | 10.1146/annurev.ps.43.020192.000511 | whole, pp. 87–131; the constructive-processing statement |
| 11 | `bettman1998constructive` | 10.1086/209535 | whole, pp. 187–217; "inherently constructive" |
| 12 | `norman1986cognitive` | 10.1201/9780367807320-3 | ch. 3, pp. 31–62; where goal formation precedes the gulfs |
| 13 | `chen2026do` | 10.1002/mar.70189 | whole, pp. 2623–2636; the goal-formation versus goal-fulfilment results |
| 14 | `sheridan2002humans` | OL4274945W; ISBN 9780471234289 | the chapter stating the human–automation model (unlocated) |
| 15 | `heer2007animated` | 10.1109/tvcg.2007.70539 | whole, pp. 1240–1247 |
| 16 | `gonzalez1996does` | 10.1145/238386.238396 | whole, pp. 27–34; the smooth-versus-abrupt result |
| 17 | `guttman1998agent` | 10.1017/s0269888998002082 | whole, pp. 147–159; the CBB model and its stages |

**Likely bot-walled — new cards; only if S4 is refused (7)**

| # | key | identifier | page or part |
|---|---|---|---|
| 18 | `weizenbaum1966eliza` | 10.1145/365153.365168 | whole, pp. 36–45; the psychological-issues discussion |
| 19 | `shneiderman1984response` | 10.1145/2514.2517 | whole, pp. 265–285; display rate |
| 20 | `gnewuch2018faster` | OpenAlex W2906833531; aisel.aisnet.org/ecis2018_rp/113 | whole |
| 21 | `steinman2000phi` | 10.1016/s0042-6989(00)00086-9 | whole, pp. 2257–2264; the phi/beta distinction |
| 22 | `simonson2008will` | 10.1016/j.jcps.2008.04.002 | whole, pp. 155–169 |
| 23 | `weinmann2016digital` | 10.1007/s12599-016-0453-1 | whole, pp. 433–436; the definition |
| 24 | `schneider2018digital` | 10.1145/3213765 | whole, pp. 67–73; "no neutral way to present choices" |

**Closed outright — upgrades (11)**

| # | key | identifier | page or part |
|---|---|---|---|
| 25 | `thomas1981illusion` | OL2924612W | the chapter stating the principles (timing, anticipation, staging, slow-in/slow-out) |
| 26 | `lamarre2009anime` | OL17203968W | the chapter(s) on limited animation |
| 27 | `wells1998understanding` | OL2708440W | the definitions of terms §4–§5 use |
| 28 | `mccloud1993understanding` | OL276032W | the chapter on closure between panels |
| 29 | `anderson1993myth` | OpenAlex W165434426; ERIC EJ477391 | whole, pp. 3–12 |
| 30 | `heider1944experimental` | 10.2307/1416950 | whole, from p. 243 |
| 31 | `slovic1995construction` | 10.1037/0003-066x.50.5.364 | whole, pp. 364–371 |
| 32 | `klein2006making` | 10.1109/mis.2006.75 | whole, pp. 70–73 |
| 33 | `simon1955behavioral` | 10.2307/1884852 | whole, from p. 99 (end page to be confirmed) |
| 34 | `horvitz1999principles` | 10.1145/302979.303030 | whole, pp. 159–166 |
| 35 | `chang1993animation` | 10.1145/168642.168647 | whole, pp. 45–55 |

**Conditional or unrecorded route — upgrades (4)**

| # | key | identifier | condition |
|---|---|---|---|
| 36 | `johnson2012beyond` | 10.1007/s11002-012-9186-1 | if the UNBC OJS or EUR copy is not this paper or not authorised |
| 37 | `epley2007seeing` | 10.1037/0033-295x.114.4.864 | route not recorded in triage; S4 checks |
| 38 | `mori2012uncanny` | 10.1109/mra.2012.2192811 | same |
| 39 | `luger2016like` | 10.1145/2858036.2858288 | if ACM refuses |

**Library request (1)**

| # | key | identifier | note |
|---|---|---|---|
| 40 | `sifianos1995definition` | none confirmed; *Animation Journal* 3(2), 1995 | reserve; promote only if the author sees the page |

Forty rows: 28 certain (17 new, 11 upgrades), 11 conditional, 1 library request.

## Findings for the author (Checkpoint B)

These are not decisions I can make. Each triage file left the outline, CHECK and FACETS untouched (README
rule 3); the flags sit here and in `../OUTLINE.md` §3.2.

**(a) HF already has multi-party and triadic models; does c9 survive?** `oneill2022human` (dxdfound, full)
counts 22 of 76 human–autonomy-teaming studies with two or more humans; `parasuraman2000types` records
"two-node loop" as a draft's phrase, not the source's; Stanton et al. (2006) give agents "different purposes";
Cameron et al. (2024) propose a Social Triad of User, Robot and Deployer because "the dyadic model of HRI
misses a key complexity"; Chiou & Lee (2023), in *Human Factors*, make operators "co-operators of automation".
OUTLINE §3.2 is flagged. The triage agent's softened wording (HF's canonical models take one operator and one
aid; where HF admits more parties they share a goal; an interested third party enters only recently, and the
paper builds on that move) is Claude's, for the author to accept, rewrite or reject. c9 can survive only in a
narrower form: the triad is new to DXD and to animation-as-interface, not to HF or HRI. Cameron et al. must be
cited as prior work on a triad either way.

**(b) CHECK F12's fix is itself disputed.** CHECK tells the author to call the lock-in "apparent motion", after
Wertheimer (1912). Hoerl (2015) argues against the claim "that apparent motion is the psychological phenomenon
that underlies motion experience in the cinema" (abstract), and Steinman, Pizlo & Pizlo (2000) title their paper
"Phi is not beta": if film shows beta motion, "apparent motion, after Wertheimer" names the wrong phenomenon.
Both are carded as contrast, open, and read before §4.2 is drafted. The safe wording may be "apparent (beta)
motion" or a hedge; the two reads decide. Nothing in CHECK.md was changed.

**(c) The G verdict.** The closest prior is Maeda & L. Stark (2025): a distributed network of human agents
collectively animates the chatbot, and the response is distributed governance. Jones (2026) applies Silvio's
animation to voice interfaces independently of Stark. Siskind et al. (2024) make c8's structural move with
another craft (magic) and the opposite aim (steering decisions). González (1996) ties interface animation to
decision quality before LLMs. No single work joins the two halves, in OpenAlex, Crossref, arXiv, Consensus and
two snowballs; the Semantic Scholar leg failed (429), so the verdict holds for those sources only. The paper
must state in §6 how its move differs from Maeda & Stark's governance move.

**(d) Ananny & Crawford (2018) has no full read anywhere.** Seven lab cards, all abstract or metadata; no OA
copy on OpenAlex or Unpaywall; the local folder `monograph_library_local/pdfs/ananny2018seeing/` is empty. CHECK
F10's "supported in substance" rests on an abstract. OUTLINE §3.2 and §5 lean on it twice. It is the first
journal article on the browser list; until it arrives the card is abstract-depth and the paper's use of it
must be marked as resting on the abstract.

**(e) Sifianos (1995) is unconfirmed, and the McLaren line has no confirmed source.** No record on Crossref,
OpenAlex or Open Library; an OpenAlex search returned 19 hits, none this article. The only recorded route to
McLaren's definition is Furniss 2008 (closed book; page unknown). S4 probes the open reserve `century2022norman`
for the wording. The author chooses at Checkpoint B: request *Animation Journal* 3(2) through the library,
cite Furniss once the page is seen, or promote Century 2022 if it quotes McLaren with a source. Until one of
these lands, §4.1's "McLaren (1968)" has no citable source, and CHECK F1 stays open.

## Smaller corrections the cards record under Caution (files left alone)

- OUTLINE §3.2 "Burrell (2016) *abs*" and "To fetch" 5 are stale: `burrell2016how` (monograph) is full text
  and quotes the three forms at p. 1 (lead correction in FACETS).
- OUTLINE §4.1 and CITED_WORKS row 31 call Gnewuch et al. 2022 "Typing delays in chatbots"; that is the file
  name. CITED_WORKS row 3 says `johnson2012beyond` is not in the registry; it is (dxdanimator, "partial").
- FACETS F9 lists "Chevalier" among Dragicevic et al. 2011's authors; the record gives Elmqvist. FACETS F4's
  pointer `cho2021giving` is about users' typing, not stream timing. FACETS F8 omits `hohenstein2020ai`.
- The research card `ananny2016` dates a 2018 volume 2016; `natale2019if`, `hollanek2023ai`, `cameron2024social`,
  `chiou2023trusting`, `endsley2017from`, `warren2011values` and `hoerl2015seeing` take the volume year with
  `registered_year` set (README rule 4).

## Checkpoint B — the author's rulings (2026-11-05)

1. Shortlist approved as written: 60 new + 17 upgrades (Stark in; Miller 1968 in reserve).
2. Closed works: "Do what you can leave a list for me for later." S4 fetches every open copy; every closed
   or blocked work is carded now at the depth reached (abstract or metadata) and listed in
   `BROWSER_LIST.md` for the author to supply later. No wait at Checkpoint C.
3. S5–S6 run as a Workflow (author opted in).
4. On the HF-triad finding (Cameron et al. 2024 and the multi-party HF models), the author's words:
   "Their triad isn't a real triad and certainly isn't as well examined". Cards for
   `cameron2024social`, `stanton2006distributed`, `chiou2023trusting` and the pointer `oneill2022human`
   must therefore record precisely, with loci, what each source counts as its third party: whether the
   third party (e.g. Cameron's Deployer) has interests of its own, acts *through* the artefact on the
   user, and is modelled in the analysis or only named. The cards report what the source says; the
   author's ruling is not written into "What it argues". The §3.2 flag in `../OUTLINE.md` stays until
   the author rules at Checkpoint D with these reads in hand.
