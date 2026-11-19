# Fable's decisions on the triage files — run pta-lib-2026-11

> **[Written by Claude (Fable), 2026-11-08; run pta-lib-2026-11, stage S3 decisions.]** The approved list per
> facet, with the reasons where I departed from a triage file. S4 fetches from this file; S5 writes from it.
> Ceiling for the run: **75 new cards**, with the 4 upgrades outside it (FACETS header: `silvio2019puppets`,
> `thomas1981illusion`, `lasseter1987principles`, `hoerl2015seeing`). Every identifier below (DOI, OpenAlex W-id,
> Open Library OL-id, arXiv id, URL) is copied from the record lookup a triage file made on 2026-11-08
> (`F1-F4.md`, `F5-F9.md`, `F10-G.md`); none comes from memory. Where a triage file gave two routes, the one
> named first is the one S4 tries first. The triage files, FACETS, CITED_WORKS and the sketch are left unchanged.

## The count

The three triage files propose 75 core cards and one stretch: F1–F4 30 (8 + 9 + 7 + 6), F5–F9 28 (7 + 2 + 7 +
7 + 5), F10–G 17 (2 + 3 + 10 + 2) plus `karelin2025indeterminism` as G's stretch. I checked each work that two
files mention for a double count: Floridi 2023 and 2025 are counted under F3 only (F12 lists them as in-run
pointers); `hayesroth2006puppetry` and `sun2025between` are counted under F5 only (G lists them as in-run, not in
its two); `schumann2022machines` under F10 only (F12 points to it); `rolla2026embodiment` under F12 only (G tags
it); `zerilli2019transparency` under F7 only. So the core list is exactly 75 and nothing needs merging; each
shared work carries both facet tags on one card. The stretch is the one card over the line. **`karelin2025indeterminism`
moves to reserve**: Masumori et al. already carry (B) as practice, Karelin's design proposal is one step further
from the thesis, and the ceiling is the author's. It returns first if Roger lifts the ceiling to 76 (Checkpoint B, 6).

| Facet | Approved new | Listed under | Upgrades | Writer: opus / sonnet (new) |
|---|---|---|---|---|
| F1 | 8 | F1 | 0 | 4 / 4 |
| F2 | 9 | F2 | 0 | 7 / 2 |
| F3 | 7 | F3 (incl. `floridi2023ai`, `floridi2025ai` [F3, F12]) | 0 | 5 / 2 |
| F4 | 6 | F4 | 2 | 5 / 1 |
| F5 | 7 | F5 (incl. `hayesroth2006puppetry`, `sun2025between` [F5, G]) | 1 | 5 / 2 |
| F6 | 2 | F6 | 1 | 0 / 2 |
| F7 | 7 | F7 (incl. `zerilli2019transparency` [F7, F12]) | 0 | 3 / 4 |
| F8 | 7 | F8 | 0 | 3 / 4 |
| F9 | 5 | F9 | 0 | 4 / 1 |
| F10 | 2 | F10 (incl. `schumann2022machines` [F10, F12]) | 0 | 1 / 1 |
| F11 | 3 | F11 | 0 | 1 / 2 |
| F12 | 10 | F12 (incl. `rolla2026embodiment` [F12, G]) | 0 | 5 / 5 |
| G | 2 | G | 0 | 2 / 0 |
| **Total** | **75** | | **4** | **45 / 30** |

Upgrades: 3 opus, 1 sonnet. Run-wide: **79 cards, 48 opus, 31 sonnet.**

**Writer rule (S5).** `opus` writes books and book chapters, dense theory, the gap cards and the cards the thesis
rests on: Govind, Hayes-Roth, Rolla, Masumori, the three Floridi papers, Moreno & Mossio and Montévil & Mossio,
Villalobos & Dewhurst, both Dennetts, Coleridge, Walton, Maturana & Varela, Varela et al., Di Paolo, Froese &
Ziemke, Humphreys, Creel, Boge, Clark & Fischer, Bernini, Kleist, Kaplin, Catmull, Zaharia, Zhou et al.,
Bommasani et al., Howdle, Gubelmann, Coeckelbergh, and every book (metadata card or not). `sonnet` writes open
full-text journal, proceedings and arXiv articles. A metadata card is short whichever model writes it; the model
is set by the work, not by the depth reached, so the same writer takes the card up to full text when a browser
copy arrives. Two departures from the triage files' assignments: `allison2011more` to sonnet (a closed film-studies
article at abstract depth; §5 cites it for one fact about Serkis and credit) and the upgrade `lasseter1987principles`
to sonnet (an open ten-page ACM article). `green2000role` is sonnet whatever depth S4 reaches, under the rule
that the work sets the model.

## Swaps proposed by the triage agents

Every swap below is accepted; none is reversed. One-line reasons.

| Facet | Proposal | Ruling | Reason |
|---|---|---|---|
| F1 | Schrödinger 1944 → reserve; Bedau, McCaskill, Packard & Rasmussen 2010 "Living technology" in | **Approved** | Schrödinger would be a metadata card the sketch never quotes; Bedau et al. define life as something engineers make (c4, c12), which is §2's sense and the boundary with Berthon's lineage question, and the copy is open. |
| F2 | Thompson 2007 *Mind in Life* → reserve; Villalobos & Dewhurst 2018 in | **Approved, flagged** | Ruling 1 makes the self-production counter the one c4 must answer head-on, and Villalobos & Dewhurst is the only record found that argues a computational system can meet enactivism's autonomy criteria; Thompson is a closed book whose ground Di Paolo and Froese & Ziemke cover in open text. This changes the named list in Roger's ruling 1, so he sees it (Checkpoint B, 6). Thompson stays on BROWSER_LIST. |
| F3 | Dennett 1971, Turing 1950, Sternberg & Detterman 1986 → reserve; Chollet 2019 in; "Real patterns" read via the 2026 MIT Press open reprint | **Approved** | All four Dennett texts are closed; the reprint is the stance argument's only open text, and Chollet states the benchmark frame §6 needs. Legg & Hutter's collection already counts Sternberg & Detterman; Turing enters only if §2 needs the test's origin. |
| F4 | Reeves 1981 → reserve; Purves 2014 *Stop-motion Animation* in | **Approved** | §3 and §5 name stop-motion as the contrast case and no F4 or F5 anchor covered it; Catmull 1978 already carries in-betweening as the problem and Burtnyk & Wein the rig. Reeves returns first if §3 keeps the "decoding = in-betweening" row and a slot opens. |
| F5 | Jurkowski → reserve; Auslander 3rd ed. (2022) over the 2nd (2008) | **Approved** | FACETS allowed Jurkowski only "if the counter needs it" and Tillis carries the visible double; the 2022 edition answers the internet, which an LLM argument must meet. |
| F5 | Hayes-Roth 2006 and Sun & Gualeni 2025 carded under F5 with G tags | **Approved** | Both are puppetry works about AI that c12 must know exist; carding them in F5 keeps G's two slots for Govind and Masumori. See the record correction on Sun & Gualeni below. |
| F7 | Humphreys 2004 *Extending Ourselves* → reserve; Sullivan 2022 in | **Approved** | The 2009 article carries the term "essential epistemic opacity"; the book would be a metadata card, and the facet needed the understanding counter more than a second Humphreys. |
| F8 | Sculley et al. 2015 → reserve; Amershi, Lewis, Schick/Yao/Khattab → reserve; Zaharia (web card) and Zhou et al. 2026 in; Bommasani and Schaeffer inside the seven | **Approved, with a conditional slot** | No bibliographic record for the NeurIPS paper reached any triage tool (S3 rule 2); Paleyes and Zaharia carry c1, and Zhou et al. state c1 and c2 in the engineers' words. The Sculley slot is held conditionally (below). |
| F9 | Ferri 2007 and Murray 1997 → reserve; Gerrig 1993 and Green & Brock 2000 in | **Approved** | Green & Brock give c8 a measured construct with a *JPSP* record, which the four books lack; Gerrig is the psychology of entering a narrative world. Murray returns first if §5 needs "active creation of belief" for liveness. |
| F10 | Stovel & Shaw and Nissenbaum → pointers (already in `coordsov`, `slacker`); Clark & Fischer 2023 and Schumann & Du 2022 in | **Approved** | FACETS rule 3 makes registry hits pointers; both replacements put the makers inside the triad, which is c9's own claim, and Schumann & Du is the venue's own development-team triad that c9 must cite and distinguish. |
| F12 | Vaassen → reserve; Hähnel & Hauswald, Schmidt & Putora, García-Valdecasas out; Rolla, Gubelmann, Arora, Popa, Coeckelbergh, von Eschenbach, Zednik, Floridi 2026, Howdle, Bottazzi Grifoni & Ferrario in | **Approved** | The ten were chosen by what each forces the paper to say (life inside the venue, who stands behind the machine, the stance and its errors, opacity); F7 already holds eight opacity cards, so two venue opacity papers suffice. |
| G | Pasquinelli 2026 → reserve; Masumori et al. 2026 (OpenLife) in; Karelin et al. 2025 stretch | **Approved for Pasquinelli and Masumori; Karelin → reserve** | Pasquinelli historicises the organism analogy rather than arguing AI is life; OpenLife is the closest work on (B) and fixes c12's wording. Karelin is cut for the ceiling (The count). |

Keys as the triage files set them (`bich2018is`, `chollet2019on`, `bommasani2021on`, `kleist1972on`,
`purves2014stopmotion`, `hayesroth2006puppetry`, `montevil2015biological`, `duran2018grounds`,
`bottazzigrifoni2025bewitching`, `voneschenbach2021transparency`, `howdle2026anthropomorphising`): approved. Two
keys change here: `sun2025between` → `sun2026between` (version of record is a 2026 chapter; see corrections) and
`govind2026illusion` is provisional (Checkpoint B, 3). README's key rule skips articles only; S5 does not rename
otherwise.

### The Sculley slot (conditional)

`sculley2015hidden` stays in F8 reserve with a slot held for it. It is promoted at S4 **only if the author opens the
NeurIPS 2015 proceedings page in a browser** (proceedings.neurips.cc or papers.nips.cc; both refused this machine)
and the card can copy from that page: the full author list (Consensus gives "D. Sculley, Gary Holt, and 8 others"),
the exact title, the venue line "Advances in Neural Information Processing Systems 28", the page range, and the PDF
URL as printed on the proceedings index. Nothing is typed from memory; if the page is not opened, the sketch's
Sculley sentence is cited through `paleyes2023challenges` and the card is not written. If Sculley is promoted, the
run is at 76; to hold 75, **`schaeffer2023are` moves to reserve** (it answers Wei et al., itself in reserve, so it
sits two steps from c2, and Bommasani's own abstract already concedes the model's "incomplete character"), unless
Roger lifts the ceiling (Checkpoint B, 6). If Sculley is promoted, `newman2016epistemic` (F7 R6) is the first F7
reserve to promote should a slot ever open: it joins Humphreys's opacity to Sculley's technical debt in one title.

### MacCormick (2026), *Thinking AI*, ch. 12 "Flight and life"

**Not carded now; an S9 must-read for `GAP_CHECK.md`.** The Crossref chapter record (10.1515/9780691200231-014,
pp. 210–224) carries no author and no abstract; the book record names John MacCormick. A card at S5 would say only
that a chapter with that title exists, which is not worth a slot. S4 puts the chapter on `BROWSER_LIST.md` under
"S9 needs this whether or not it is carded"; S9 opens it before the G verdict closes. If the chapter argues that
life is the better analogy for AI *as something made*, it is a prior work on (B) and the author decides at S9
whether it takes a 76th card; if it uses life as an analogy for AI's capacities, it is logged as a near miss.

## F1 — approved (8), from `triage/F1-F4.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `trifonov2011vocabulary` | Trifonov, E. N. (2011). Vocabulary of definitions of life suggests a definition. *J. Biomolecular Structure and Dynamics*, 29(2), 259–266. | 10.1080/073911011010524992; W2115613299 | closed → BROWSER_LIST | sonnet | full_text if the browser gets it; else abstract. Anchor, c3. |
| `machery2012why` | Machery, E. (2012). Why I stopped worrying about the definition of life... and why you should as well. *Synthese*, 185(1), 145–164. | 10.1007/s11229-011-9880-1; W2004689716; `registered_year: 2011` | closed → BROWSER_LIST | opus | full_text if fetched; else metadata. Contrast, c3. |
| `cleland2019quest` | Cleland, C. E. (2019). *The quest for a universal theory of life*. Cambridge UP. | 10.1017/9781139046893; W3171467138 | closed → BROWSER_LIST (book) | opus | metadata (abstract). Anchor, c3. |
| `cleland2002defining` | Cleland, C. E., & Chyba, C. F. (2002). Defining 'life'. *Origins of Life and Evolution of the Biosphere*, 32(4), 387–393. | 10.1023/a:1020503324273; W3191793628 | closed → BROWSER_LIST | opus | full_text if fetched; else metadata. Anchor, c3; the article substitute for the book. |
| `bich2018is` | Bich, L., & Green, S. (2018). Is defining life pointless? Operational definitions at the frontiers of biology. *Synthese*, 195(9), 3919–3946. | 10.1007/s11229-017-1397-9; W2602557110; `registered_year: 2017` | open (green): researchprofiles.ku.dk landing page `3a84eb91-2e8e-4b1f-a3f6-f7d30320ac2a`; S4 records the version | opus | full_text. Contrast to Machery, c3, c4. |
| `bedau2003artificial` | Bedau, M. A. (2003). Artificial life: Organization, adaptation and complexity from the bottom up. *TICS*, 7(11), 505–512. | 10.1016/j.tics.2003.09.012; W2122739151 | closed → BROWSER_LIST | sonnet | full_text if fetched; else metadata. Support, c3, c12. |
| `dorin2024what` | Dorin, A., & Stepney, S. (2024). What is artificial life today, and where should it go? *Artificial Life*, 30(1), 1–15. | 10.1162/artl_e_00435; W4393241411 | the PDF held in Berthon's arm, copied with `provenance.txt`; fallback the MIT Press bronze PDF | sonnet | full_text. Support, c3, c12; carries Langton's "life as it could be" by quotation. |
| `bedau2010living` | Bedau, M. A., McCaskill, J. S., Packard, N. H., & Rasmussen, S. (2010). Living technology: Exploiting life's principles in technology. *Artificial Life*, 16(1), 89–97. | 10.1162/artl.2009.16.1.16103; W2130707354 (Crossref 2010, OpenAlex 2009; key takes the volume year) | open (green): zenodo.org/record/3439357 | sonnet | full_text. Support, c4, c12 (replaces Schrödinger). |

Reserve, as the triage file lists: `knuuttila2017what` (open; promote if Bich & Green cannot be read),
`dorin2023editorial` (open; G(B) neighbour), `nisioti2024from` (open), `ruizmirazo2010universal`, `smith2016life`,
`malaterre2021beyond` (open), `bedau1998four`, `schrodinger1944what` / `langton2019artificial` (exists-only).
Pointer: `monograph/albantakis2014evolution` (full_text in the registry, not metadata as FACETS says).

## F2 — approved (9), from `triage/F1-F4.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `maturana1980autopoiesis` | Maturana, H. R., & Varela, F. J. (1980). *Autopoiesis and cognition: The realization of the living*. D. Reidel. | OL15015691W; W1916207017; chapter DOIs under 10.1007/978-94-009-8947-4 | closed → BROWSER_LIST (book) | opus | metadata. Anchor, c4. Author line from the title page (records disagree). |
| `varela1974autopoiesis` | Varela, F. G., Maturana, H. R., & Uribe, R. (1974). Autopoiesis: The organization of living systems, its characterization and a model. *BioSystems*, 5(4), 187–196. | 10.1016/0303-2647(74)90031-8; W2093020640 | open (green): repositorio.uchile.cl/handle/2250/160309 | opus | full_text. Anchor, c4. |
| `moreno2015biological` | Moreno, A., & Mossio, M. (2015). *Biological autonomy: A philosophical and theoretical enquiry*. Springer. | 10.1007/978-94-017-9837-2; W4249319693 | partial: HAL hal-01151449 `Book_Autonomy_web.pdf` (S4 reports what it holds); the rest → BROWSER_LIST | opus | full_text of what HAL holds; else metadata. Anchor and counter, c4. |
| `montevil2015biological` | Montévil, M., & Mossio, M. (2015). Biological organisation as closure of constraints. *J. Theoretical Biology*, 372, 179–191. | 10.1016/j.jtbi.2015.02.029; W2107475155 | open (green): HAL hal-01192916 | opus | full_text. Anchor, c4. |
| `dipaolo2005autopoiesis` | Di Paolo, E. A. (2005). Autopoiesis, adaptivity, teleology, agency. *Phenomenology and the Cognitive Sciences*, 4(4), 429–452. | 10.1007/s11097-005-9002-y; W2068670723 | open (green): figshare 23368025 | opus | full_text. Support, c4, c11. |
| `froese2009enactive` | Froese, T., & Ziemke, T. (2009). Enactive artificial intelligence: Investigating the systemic organization of life and mind. *Artificial Intelligence*, 173(3–4), 466–500. | 10.1016/j.artint.2008.12.001; W1989974095 | open (bronze): ScienceDirect PDF; if refused → BROWSER_LIST, no bypass | opus | full_text. Anchor, c4, c12. |
| `bongard2021living` | Bongard, J., & Levin, M. (2021). Living things are not (20th century) machines. *Frontiers in Ecology and Evolution*, 9, 650726. | 10.3389/fevo.2021.650726; W3137009159 | open (gold) | sonnet | full_text. Contrast, c4. |
| `meincke2019autopoiesis` | Meincke, A. S. (2019). Autopoiesis, biological autonomy and the process view of life. *European J. for Philosophy of Science*, 9(1), Article 5. | 10.1007/s13194-018-0228-2; W2885752831; `registered_year: 2018` | open (green): eprints.soton.ac.uk/426378 | sonnet | full_text. Contrast, c4. |
| `villalobos2018enactive` | Villalobos, M., & Dewhurst, J. (2018). Enactive autonomy in computational systems. *Synthese*, 195(5), 1891–1908. | 10.1007/s11229-017-1386-z; W2602626577; `registered_year: 2017` | open (hybrid): Springer PDF | opus | full_text. Contrast, c4 (replaces Thompson). |

Reserve: `thompson2007mind` (OL3475244W; stays on BROWSER_LIST; promote to a metadata card if Roger opens it),
`villalobos2015living` (open; the venue's own autopoiesis paper, outside F12's window; card once, here or in F12,
only if Roger wants the precedent), `bich2024biological` (open Cambridge Element; the book-length substitute if
Moreno & Mossio stays closed), `rubin2026genealogies` (open), `roli2022how` (open), `bianchini2023autopoiesis`
(open), `dung2025understanding` (open), `mossio2009organizational` (open), `luisi2003autopoiesis`,
`chanet2019towards` (open). G's `barandiaran2025transforming` (open; the enactive counter with the agent extensions
in view) is offered to F2 first and sits here as the first reserve to promote if a slot opens.

## F3 — approved (7), from `triage/F1-F4.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `legg2007collection` | Legg, S., & Hutter, M. (2007). *A collection of definitions of intelligence* (arXiv:0706.3639). | 10.48550/arxiv.0706.3639; W2142753384 | open: arXiv | sonnet | full_text. Anchor, c3. |
| `legg2007universal` | Legg, S., & Hutter, M. (2007). Universal intelligence: A definition of machine intelligence. *Minds and Machines*, 17(4), 391–444. | 10.1007/s11023-007-9079-x; W2101493843 | open (green): arXiv 0712.3329 (S4 records the version) | opus | full_text. Anchor, c3, c5. |
| `chollet2019on` | Chollet, F. (2019). *On the measure of intelligence* (arXiv:1911.01547). | 10.48550/arxiv.1911.01547; W2984217758 | open: arXiv | sonnet | full_text. Support, c5, c11. |
| `dennett1987intentional` | Dennett, D. C. (1987). *The intentional stance*. MIT Press. | OL2463706W | closed → BROWSER_LIST (book) | opus | metadata. Anchor, c5. |
| `dennett1991real` | Dennett, D. C. (1991). Real patterns. *J. Philosophy*, 88(1), 27–. | 10.2307/2027085; W4230736257; read via the 2026 MIT Press open reprint 10.7551/mitpress/15550.003.0005, pp. 33–58 | open (hybrid): MIT Press chapter PDF | opus | full_text (reprint). Quotations carry reprint pages and the card says so; never mixed with *J. Phil.* pagination. Anchor, c5. |
| `floridi2023ai` | Floridi, L. (2023). AI as agency without intelligence: On ChatGPT, large language models, and other generative models. *Philosophy & Technology*, 36(1), Article 15. | 10.1007/s13347-023-00621-y; W4360957277 | open (bronze): Springer PDF | opus | full_text. Contrast, c5, c12; `facets: [F3, F12]`. |
| `floridi2025ai` | Floridi, L. (2025). AI as agency without intelligence: On artificial intelligence as a new form of artificial agency and the multiple realisability of agency thesis. *Philosophy & Technology*, 38(1), Article 30. | 10.1007/s13347-025-00858-9; W4408055303 | open (green): SSRN 10.2139/ssrn.5135645 (preprint; S4 tries the Springer PDF for the version of record) | opus | full_text (preprint unless Springer opens). Contrast, c4, c5; `facets: [F3, F12]`. |

Reserve: `dennett1971intentional` (closed; promote if the browser gets *J. Phil.* and the book stays closed),
`dennett1988precis` (closed; the better closed substitute: "whatever its innards" bears on c2),
`debrigard2026artificial` (open; a direct test of the "vital stance" move), `bechtel1985realism` (open),
`turing1950computing`, `sternberg1986what`, `hernandezorallo2017measure`, `hernandezorallo2017evaluation` (open),
`floridi2020gpt3` (open). Pointers: `designeth/floridisanders2004` (full_text), `triadic/ali2025intelligence`
(only if Φ enters §2).

## F4 — approved (6), from `triage/F1-F4.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `williams2001animators` | Williams, R. (2001). *The animator's survival kit*. Faber and Faber. | OL6073254W | closed → BROWSER_LIST (book) | opus | metadata. Support, c6. |
| `catmull1978problems` | Catmull, E. (1978). The problems of computer-assisted animation. *SIGGRAPH '78*, pp. 348–353. ACM. | 10.1145/800248.807414; W1979705324 (same paper: 10.1145/965139.807414, W3006169675) | closed per OpenAlex → S4 tries the ACM DL PDF; if refused → BROWSER_LIST | opus | full_text if fetched; else abstract. Contrast, c6, c7, c10. |
| `burtnyk1976interactive` | Burtnyk, N., & Wein, M. (1976). Interactive skeleton techniques for enhancing motion dynamics in key frame animation. *CACM*, 19(10), 564–569. | 10.1145/360349.360357; W2047353909 | open (bronze): ACM DL PDF | sonnet | full_text. Support, c6, c1. |
| `crafton2012shadow` | Crafton, D. (2012). *Shadow of a mouse: Performance, belief, and world-making in animation*. U. of California Press. | 10.1525/9780520352520; W4387486745 | closed → BROWSER_LIST (book) | opus | metadata (abstract). Anchor, c6, c8, c10. |
| `hooks2023acting` | Hooks, E. (2023). *Acting for animators* (5th ed.). Routledge. | 10.4324/9781003289753; W594927527; pipeline chapter 10.4324/9781003289753-4, pp. 19–20 | closed → BROWSER_LIST (book; the pipeline chapter first) | opus | metadata (abstract). Support, c6, c1. |
| `purves2014stopmotion` | Purves, B. J. C. (2014). *Stop-motion animation: Frame by frame film-making with puppets and models* [edition unconfirmed]. Bloomsbury. | 10.5040/9781474222365; W4234684970; ch. "What is stop-motion?" 10.5040/9781474222365.0005 | closed → BROWSER_LIST (book; that chapter first) | opus | metadata (abstract). Contrast, c6, c10 (replaces Reeves). |

Reserve: `reeves1981inbetweening` (returns first if §3 keeps the decoding row), `burtnyk1971computer`,
`gasek2013frame`, `chandramouli2021production`, `kerlow2004art`, `catmull2014creativity`, `bishko2014animation`.
Pointers (seven dxda keys, all cited for terms): `wells1998understanding`, `furniss2008art`, `bukatman2012poetics`,
`lamarre2009anime`, `mccloud1993understanding`, `chang1993animation`, `cholodenko2014first`.

## F5 — approved (7), from `triage/F5-F9.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `auslander2022liveness` | Auslander, P. (2022). *Liveness: Performance in a mediatized culture* (3rd ed.). Routledge. | 10.4324/9781003031314; W4307511423 | closed → BROWSER_LIST (book; Introduction -1 and ch. 2 -2 first) | opus | metadata (abstract). Anchor, c10. |
| `tillis1992toward` | Tillis, S. (1992). *Toward an aesthetics of the puppet* [subtitle unconfirmed]. Greenwood Press. | OL1857491W (edition OL1561974M; ISBN 0313283591) | closed → BROWSER_LIST (book) | opus | metadata. Contrast, c10, c6. |
| `kaplin1999puppet` | Kaplin, S. (1999). A puppet tree: A model for the field of puppet theatre. *TDR*, 43(3), 28–35. | 10.1162/105420499760347306; W2109326195 | closed → BROWSER_LIST | opus | full_text if the browser gets it; else abstract. Anchor, c10. |
| `kleist1972on` | von Kleist, H. (1972). On the marionette theatre. *The Drama Review*, 16(3), 22–26. (Original work published 1810; clause to be confirmed from the headnote or the German source.) | 10.2307/1144768; W2795663071; German text at de.wikisource.org "Über das Marionettentheater" | German original open (Wikisource); translation closed → BROWSER_LIST | opus | full_text (German); translation if fetched. Anchor, c5, c10. |
| `allison2011more` | Allison, T. (2011). More than a man in a monkey suit: Andy Serkis, motion capture, and digital realism. *Quarterly Review of Film and Video*, 28(4), 325–341. | 10.1080/10509208.2010.500947; W2063617998 | closed → BROWSER_LIST | sonnet | full_text if fetched; else abstract. Support, c10, c9. |
| `hayesroth2006puppetry` | Hayes-Roth, F. [initial unconfirmed] (2006). Puppetry vs. creationism: Why AI must cross the chasm. *IEEE Intelligent Systems*, 21(5), 7–9. | 10.1109/mis.2006.102; W2168516896 | closed → BROWSER_LIST (IEEE Xplore) | opus | full_text if fetched; else abstract. Support, c5, c10, c12; `facets: [F5, G]`. |
| `sun2026between` (was `sun2025between`) | Sun, Y., & Gualeni, S. (2026). Between puppet and actor: Reframing authorship in this age of AI agents. In *Artificial Media* (Springer Series on Cultural Computing), pp. 49–63. Springer. | chapter 10.1007/978-3-031-89037-6_3 (online 2025-07-30; `registered_year: 2025`); preprint arXiv 2501.15346 v1, W4412732348 | open (green): um.edu.mt OAR handle 123456789/139132; arXiv v1 as the fallback, named as the preprint if read | sonnet | full_text. Contrast, c10, c12; `facets: [F5, G]`. The card cites the chapter as version of record (G triage, note 4). |

Reserve: `jurkowski2013aspects`, `mihailova2016collaboration` (hidden animator labour in performance capture; promote
if §4.4 wants an animation-side labour source), `bestor2016technologically`, `phelan2003unmarked`,
`bode2019making`, `bell2008american`, `timplalexi2024intermedial` [G]. Pointers: `dxda/silvio2010animation`
(abstract), `dxda/stark2024animation` (full); in-run `crafton2012shadow`, `purves2014stopmotion`.

## F6 — approved (2), from `triage/F5-F9.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `scholl2000perceptual` | Scholl, B. J., & Tremoulet, P. D. (2000). Perceptual causality and animacy. *TICS*, 4(8), 299–309. | 10.1016/s1364-6613(00)01506-0; W2123393961 | open (author page): perception.yale.edu `00-Scholl-Tremoulet-TICS.pdf` (version recorded by S4) | sonnet | full_text. Anchor, c7, c8. |
| `gao2009psychophysics` | Gao, T., Newman, G. E., & Scholl, B. J. (2009). The psychophysics of chasing: A case study in the perception of animacy. *Cognitive Psychology*, 59(2), 154–179. | 10.1016/j.cogpsych.2009.03.001; W2121381319 | open (author page): perception.yale.edu `09-Gao-Newman-Scholl-CogPsych.pdf` | sonnet | full_text. Support, c7. |

Reserve: `michotte2017perception`, `sekuler1996motion`. Pointers (six works): `dxda/wertheimer1912experimentelle`,
`dxda/wertheimer2012experimental`, `dxda/anderson1993myth`, `dxda/heider1944experimental`, `dxda/epley2007seeing`,
`dxda/mori2012uncanny`, `dxdfound/wagemans2012century`.

## F7 — approved (7), from `triage/F5-F9.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `humphreys2009philosophical` | Humphreys, P. (2009). The philosophical novelty of computer simulation methods. *Synthese*, 169(3), 615–626. | 10.1007/s11229-008-9435-2; W2055250996; `registered_year: 2008` | CiteSeerX submitted version (doi 10.1.1.468.829) first; else BROWSER_LIST | opus | full_text if fetched; else metadata. Anchor, c7. |
| `creel2020transparency` | Creel, K. A. (2020). Transparency in complex computational systems. *Philosophy of Science*, 87(4), 568–589. | 10.1086/709729; W2991187744 | open (bronze): Cambridge Core PDF | opus | full_text. Contrast, c7. |
| `zerilli2022explaining` | Zerilli, J. (2022). Explaining machine learning decisions. *Philosophy of Science*, 89(1), 1–19. | 10.1017/psa.2021.13; W3164398698 | open (green, accepted version): philsci-archive 19096 | sonnet | full_text. Contrast, c7. |
| `zerilli2019transparency` | Zerilli, J., Knott, A., Maclaurin, J., & Gavaghan, C. (2019). Transparency in algorithmic and human decision-making: Is there a double standard? *Philosophy & Technology*, 32(4), 661–683. | 10.1007/s13347-018-0330-6; W2892104346; `registered_year: 2018` | open (green): Cambridge repository 10.17863/cam.47045 | sonnet | full_text. Contrast, c7, c5; `facets: [F7, F12]`. |
| `duran2018grounds` | Durán, J. M., & Formanek, N. (2018). Grounds for trust: Essential epistemic opacity and computational reliabilism. *Minds and Machines*, 28(4), 645–666. | 10.1007/s11023-018-9481-6; W2898854870 | open (hybrid): Springer PDF | sonnet | full_text. Support, c7, c11. |
| `boge2022two` | Boge, F. J. (2022). Two dimensions of opacity and the deep learning predicament. *Minds and Machines*, 32(1), 43–75. | 10.1007/s11023-021-09569-4; W3197302864; `registered_year: 2021` | open (hybrid): Springer PDF | opus | full_text. Support, c7. |
| `sullivan2022understanding` | Sullivan, E. (2022). Understanding from machine learning models. *BJPS*, 73(1), 109–133. | 10.1093/bjps/axz035; W2965860133; `registered_year: 2019` | open (green, accepted version): philsci-archive 16276 | sonnet | full_text. Contrast, c7 (replaces Humphreys 2004). |

Reserve: `humphreys2004extending`, `beisbart2021opacity` (open), `lipton2018mythos` (open), `sullivan2022inductive`
(open), `gunther2022algorithmic`, `newman2016epistemic` (open; first to promote if Sculley enters). Pointers:
`monograph/burrell2016how` (full; cite this key, not `coordsov/burrell2016machine`), `monograph/ananny2018seeing`
(abstract; `dial/ananny-crawford-2018-seeing-without-knowing` verified), `dial/pasquale-2015-black-box-society`,
`dxda/stark2024animation`, `designeth/rudin2019`.

## F8 — approved (7), from `triage/F5-F9.md`

| key | APA (from the record or page) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `zaharia2024shift` | Zaharia, M., Khattab, O., Chen, L., Davis, J. Q., Miller, H., Potts, C., Zou, J., Carbin, M., Frankle, J., Rao, N., & Ghodsi, A. (2024, February 18). *The shift from models to compound AI systems*. BAIR Blog. | web; byline and date from the page; access date 2026-11-08 | open: bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/ (S4 saves the HTML with access date) | opus | full_text (web). Anchor, c1, c2. `type: web`. |
| `paleyes2023challenges` | Paleyes, A., Urma, R.-G., & Lawrence, N. D. (2023). Challenges in deploying machine learning: A survey of case studies. *ACM Computing Surveys*, 55(6), 1–29. | 10.1145/3533378; W3104128335; `registered_year: 2022` | open (hybrid): ACM DL PDF | sonnet | full_text. Anchor, c1; carries the sketch's Sculley sentence until Sculley is promoted. |
| `zhou2026externalization` | Zhou, C., Chai, H., Chen, W., … Zhang, W. (2026). *Externalization in LLM agents: A unified review of memory, skills, protocols and harness engineering* [Preprint]. arXiv. (21 authors; APA lists 19, ellipsis, last.) | arXiv 2604.08224 v1 (2026-04-09) | open: arXiv | opus | full_text. Anchor, c1, c2; also stocks "harnesses are CS too". |
| `park2023generative` | Park, J. S., O'Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. *UIST '23*, pp. 1–22. ACM. | 10.1145/3586183.3606763; W4387835442 | open (bronze): ACM DL PDF | sonnet | full_text. Support, c1, c6, c11. |
| `wang2024survey` | Wang, L., Ma, C., Feng, X., … [full list from the record] (2024). A survey on large language model based autonomous agents. *Frontiers of Computer Science*, 18(6), Article 186345. | 10.1007/s11704-024-40231-1; W4393065402 | open (hybrid): Springer PDF | sonnet | full_text. Support, c1. The card takes all authors from Crossref (the triage printout stopped at twelve). |
| `bommasani2021on` | Bommasani, R., Hudson, D. A., Adeli, E., … Liang, P. (2021). *On the opportunities and risks of foundation models* [Preprint]. arXiv. | arXiv 2108.07258 (v3, 2022-07-12); W3195577433 | open: arXiv | opus | partial (introduction and §1). Contrast, c2. |
| `schaeffer2023are` | Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? *NeurIPS 36*, pp. 55565–55581. | 10.52202/075280-2425; W7133219754 | open (green): arXiv 2304.15004 | sonnet | full_text. Contrast, c2. **Moves to reserve if Sculley is promoted** (The Sculley slot). |

Reserve: `sculley2015hidden` (conditional slot, above), `amershi2019software`, `sumers2023cognitive` (open),
`gu2026from` (open), `cho2026its` (open), `lewis2020retrievalaugmented`, `yao2022react`, `schick2023toolformer`,
`khattab2023dspy`, `wei2022emergent`, `kaplan2020scaling`, `kapoor2024ai` (unconfirmed). G offers de Macedo
(2026, arXiv 2606.10106, "What makes a harness a harness") as a c1 definition beside Zhou; it enters only if a
slot opens. No pointers.

## F9 — approved (5), from `triage/F5-F9.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `coleridge1817biographia` | Coleridge, S. T. (1817). *Biographia literaria; or, Biographical sketches of my literary life and opinions* (Vols. 1–2). Rest Fenner. | OL26034W (edition OL23281404M); Internet Archive `biographialitera00colerich` | open (public domain): archive.org/details/biographialitera00colerich | opus | full_text (ch. XIV). Anchor, c8. Every quotation carries that scan's volume and page; never mixed with the Engell & Bate edition. |
| `walton1990mimesis` | Walton, K. L. (1990). *Mimesis as make-believe: On the foundations of the representational arts*. Harvard UP. | OL4801866W (edition OL2216209M; ISBN 0674576195) | closed → BROWSER_LIST (book) | opus | metadata. Contrast, c8. |
| `gerrig1993experiencing` | Gerrig, R. J. (1993). *Experiencing narrative worlds: On the psychological activities of reading*. Yale UP. | OL4313731W (edition OL1736610M; ISBN 0300054343) | closed → BROWSER_LIST (book) | opus | metadata. Support, c8 (replaces Ferri). |
| `green2000role` | Green, M. C., & Brock, T. C. (2000). The role of transportation in the persuasiveness of public narratives. *JPSP*, 79(5), 701–721. | 10.1037/0022-3514.79.5.701 (OA status unchecked: OpenAlex budget) | S4 looks for an author copy; else BROWSER_LIST | sonnet | full_text if fetched; else metadata. Support, c8 (replaces Murray). |
| `tomko2015beyond` | Tomko, M. (2015). *Beyond the willing suspension of disbelief: Poetic faith from Coleridge to Tolkien*. Bloomsbury Academic. | 10.5040/9781474218627; OL21146931W; ch. 1 10.5040/9781474218627.ch-001 | closed → BROWSER_LIST (book; ch. 1 first) | opus | metadata. Contrast, c8. |

Reserve: `murray1997hamlet` (returns first if §5 needs "active creation of belief"), `ferri2007willing`,
`galgut2002poetic`. Pointers (nine, lock-in economics and co-optation, all held in `research`): `shapirovarian1999`,
`arthur1989`, `farrellklemperer2007`, `selznick1949` (and `selznick1948`), `stark2024` (**D.** Stark & Vanden Broeck;
also `monograph/stark2024principles`), `dial/seaver-2019-captivating-algorithms`, `kellogg2020`, `gillespie2010`,
`zuboff2019`.

## F10 — approved (2), from `triage/F10-G.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `clark2023social` | Clark, H. H., & Fischer, K. (2023). Social robots as depictions of social agents. *Behavioral and Brain Sciences*, 46, Article e21. | 10.1017/s0140525x22000668; W4221071943; `registered_year: 2022`. The authors' reply is e51, 10.1017/s0140525x22002825 (closed), not the target article. | open (green): portal.findresearcher.sdu.dk publication `d790c03c-4181-429c-bc5b-36fd59f8eae9` | opus | full_text. Anchor, c9, c10. The card notes which commentaries press the "authorities" class. |
| `schumann2022machines` | Schumann, N., & Du, Y. (2022). Machines in the triangle: A pragmatic interactive approach to information. *Philosophy & Technology*, 35(2), Article 32. | 10.1007/s13347-022-00516-4; W4226288743 | open (hybrid): Springer PDF | sonnet | full_text. Contrast, c9, c12; `facets: [F10, F12]`. Flag for opus if §4.4 makes it the main foil. |

Reserve: `thompson1980moral`, `list2021group` (open), `vandepoel2015moral`. Pointers (thirteen keys plus the Paper 1
criterion): `coordsov/stovel2012brokerage` (abstract), `slacker/nissenbaum1996accountability` (metadata-only; record
10.1007/bf02639315), `triadic/simmel1902number1`, `triadic/simmel1902number2`, `designeth/simmel1950`,
`triadic/caplow1956theory`, `triadic/caplow1968coalitions`, `lima/obstfeld2005`, `designeth/burt1992`,
`peircean/halevy2019brokerage`, `peircean/peirce1906prolegomena`, `dxda/cameron2024social`, `dxda/stark2024animation`,
and `D/current/paper1/` for the lab's criterion.

## F11 — approved (3), from `triage/F10-G.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `bernini2025ai` | Bernini, M. (2025). AI as character: Real patterns in fictive interactions. *Style*, 59(3), 466–507. | 10.5325/style.59.3.0466; W7155074459; Crossref's only date 2026-04-17, recorded in the card | open (green per OpenAlex; the oa_url is the DOI page; if no PDF → BROWSER_LIST) | opus | full_text. Contrast, c12, c5, c10. |
| `magee2023structured` | Magee, L., Arora, V., & Munn, L. (2023). Structured like a language model: Analysing AI as an automated subject. *Big Data & Society*, 10(2). | 10.1177/20539517231210273; W4388534853 | open (gold): SAGE PDF | sonnet | full_text. Contrast, c12, c2. The card says whether "construction" means training only or the system around the model. |
| `shanahan2024talking` | Shanahan, M. (2024). Talking about large language models. *CACM*, 67(2), 68–79. | 10.1145/3624724; W4391215636 | open (bronze): ACM DL PDF | sonnet | full_text. Contrast, c10, c5. |

Reserve: `mitchell2023debate` (open), `timplalexi2024intermedial` (counted in F5's reserve). Pointers (seven dxda keys):
`stark2024animation`, `shanahan2023role`, `maeda2025anthropomorphism`, `jones2026animating`, `abercrombie2023mirages`,
`weizenbaum1966eliza`, `siskind2024would`; in-run `hayesroth2006puppetry`, `sun2026between`, `floridi2026ai`.

## F12 — approved (10), from `triage/F10-G.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `rolla2026embodiment` | Rolla, G. (2026). The embodiment challenge for artificial intelligence. *Philosophy & Technology*, 39(3), Article 125. | 10.1007/s13347-026-01139-9; W7166733588 | open (hybrid): Springer PDF | opus | full_text. Contrast, c4, c12; `facets: [F12, G]`. |
| `gubelmann2024large` | Gubelmann, R. (2024). Large language models, agency, and why speech acts are beyond them (for now) – A Kantian-cum-pragmatist case. *Philosophy & Technology*, 37(1), Article 32. | 10.1007/s13347-024-00696-1; W4392110156 | open (hybrid): Springer PDF | opus | full_text. Contrast, c4, c5. |
| `arora2024proxy` | Arora, C. (2024). Proxy assertions and agency: The case of machine-assertions. *Philosophy & Technology*, 37(1), Article 15. | 10.1007/s13347-024-00703-5; W4391328240 | open (hybrid): Springer PDF | sonnet | full_text. Support, c9. |
| `popa2021human` | Popa, E. (2021). Human goals are constitutive of agency in artificial intelligence (AI). *Philosophy & Technology*, 34(4), 1731–1750. | 10.1007/s13347-021-00483-2; W3210886175 | closed → BROWSER_LIST | sonnet | full_text if the browser gets it; else metadata (no abstract on any record; the card claims nothing until read). Support, c9, c4. |
| `coeckelbergh2021time` | Coeckelbergh, M. (2021). Time machines: Artificial intelligence, process, and narrative. *Philosophy & Technology*, 34(4), 1623–1638. | 10.1007/s13347-021-00479-y; W3210338272 (not `coordsov/coeckelbergh2024ai`) | open (hybrid): Springer PDF | opus | full_text. Support, c4, c6. |
| `voneschenbach2021transparency` | von Eschenbach, W. J. (2021). Transparency and the black box problem: Why we do not trust AI. *Philosophy & Technology*, 34(4), 1607–1622. | 10.1007/s13347-021-00477-0; W3198525581 | closed → BROWSER_LIST | sonnet | full_text if fetched; else metadata. Support, c7. |
| `zednik2021solving` | Zednik, C. (2021). Solving the black box problem: A normative framework for explainable artificial intelligence. *Philosophy & Technology*, 34(2), 265–288. | 10.1007/s13347-019-00382-7; W2955132579; `registered_year: 2019` | open (green): arXiv 1903.04361 (preprint; version named in the card) | sonnet | full_text (preprint). Support, c7. |
| `floridi2026ai` | Floridi, L. (2026). AI and semantic pareidolia: When we see intelligent consciousness where there is none. *Philosophy & Technology*, 39(1), Article 36. | 10.1007/s13347-026-01052-1; W7130505239 | open (bronze): Springer PDF | opus | full_text. Contrast, c5, c12. |
| `howdle2026anthropomorphising` | Howdle, G. (2026). Anthropomorphising AI: Two modes, two errors. *Philosophy & Technology*, 39(3), Article 140. | 10.1007/s13347-026-01133-1; W7168404739 | open (hybrid): Springer PDF | opus | full_text. Contrast, c5, c11. |
| `bottazzigrifoni2025bewitching` | Bottazzi Grifoni, E., & Ferrario, R. (2025). The bewitching AI: The illusion of communication with large language models. *Philosophy & Technology*, 38(2), Article 61. | 10.1007/s13347-025-00893-6; W4410092719 | open (hybrid): Springer PDF | sonnet | full_text. Contrast, c8, c7. |

Reserve: `villalobos2015living` (card once, here or F2), `conradie2024no` (open), `sakr2026beyond` (promote with
Howdle if §4.4 wants institutional anthropomorphism), `tritschler2025undead` (open), `agar2020how`, `vaassen2022ai`
(open), `bianchini2025generative` (open), `schmidt2023interacting` (open), `list2021group` (F10 reserve),
`batista2026beyond` (open). In-run pointers: `floridi2023ai`, `floridi2025ai` (F3), `zerilli2019transparency` (F7),
`schumann2022machines` (F10).

## G — approved (2), from `triage/F10-G.md`

| key | APA (from the record) | doi / id | route | writer | expected depth |
|---|---|---|---|---|---|
| `govind2026illusion` (provisional key; Checkpoint B, 3) | Govind Reddy. (2026). *The illusion of mind: What Disney animation teaches us about AI's missing inbetween frames* (Version 1.0) [Preprint]. Zenodo. | 10.5281/zenodo.18859161 (concept DOI; version DOI 10.5281/zenodo.18859162); W7133553834; ORCID 0009-0002-4373-9166 | open (green; CC BY 4.0 per DataCite): zenodo.org/doi/10.5281/zenodo.18859161 (S4 saves the version-1.0 file and the DataCite JSON) | opus | full_text. Contrast, c7, c12. Full card by ruling 2; the card's Caution records the surname question. |
| `masumori2026openlife` | Masumori, A., Doi, I., Maruyama, N., Takata, R., & Ikegami, T. (2026). *OpenLife: Toward open-world artificial life with autonomous LLM agents* [Preprint]. arXiv. (Accepted at ALIFE 2026; no proceedings record yet.) | arXiv 2606.31046 v1 (2026-06-30) | open: arXiv | opus | full_text. Contrast, c12, c4, c1. The card confirms that the body makes no conceptual claim about AI development in general. |

Reserve: `karelin2025indeterminism` (open; W7110543113; **six** authors; first to return if the ceiling lifts),
`sun2025sophia` (open), `zhang2026nurturefirst` (open; c11), `ribeiro2012illusion` (the closest work on (A); closed),
`pasquinelli2026machine` (open), `barandiaran2025transforming` (open; offered to F2), `maccormick2026thinking`
(S9 must-read, above), `timplalexi2024intermedial` (F5 reserve). Pointers: `dxda/stark2024animation`,
`dxda/jones2026animating`, `research/seaver2017`; in-run `hayesroth2006puppetry`, `sun2026between`, `rolla2026embodiment`.

The G verdict stands as the triage file states it, for the sources it names: (A) no work frames the development of an
AI system as animation-like craft; (B) no work argues AI development in general is better conceived as making
artificial life, though the engineering side already practises it (OpenLife, Sophia, Nurture-First). The OpenAlex
and Semantic Scholar list legs failed (429) and `GAP_CHECK.md` must say so; S9 reruns them once the budget resets.

## The 4 upgrades (outside the ceiling)

Each is a new card here with `prior_cards: [<dxda key>, <dxdanimator key>]`; the prior files are left alone.

| key | facets | read as (depth + identifier / route) | writer |
|---|---|---|---|
| `thomas1981illusion` | F4 | metadata; OL2924612W (author field garbled: "Thomas, Frank", "Thomas Johnson", "Ollie Johnson"; the card takes the title page) → BROWSER_LIST (the principles chapter) | opus |
| `lasseter1987principles` | F4 | full_text, open (bronze): **10.1145/37401.37407** (SIGGRAPH '87 proceedings; W2121378366), pp. 35–44. The dxdanimator card uses 10.1145/37402.37407 (*Computer Graphics* 21(4); W2999276620, closed); Caution records both. | sonnet |
| `silvio2019puppets` | F5 | metadata (abstract); 10.1515/9780824880989; W4285785079; OL21338441W → BROWSER_LIST (ch. 1 "Animation versus performance", pp. 18–52, 10.1515/9780824880989-006, first; then the Introduction -005). Crossref types it "edited-book" with Alexy as editor; the card checks the title page. | opus |
| `hoerl2015seeing` | F6 | full_text, open (Wiley bronze): 10.1111/j.1468-0378.2012.00565.x; W2121842656; *EJP* 23(3), 676–702; `registered_year: 2012` | opus |

## S5–S6 workflow batches

The split the brief prescribes, with the counts it yields. Upgrades ride with their facet.

| Batch | Facets | New cards | Upgrades | Total | opus / sonnet |
|---|---|---|---|---|---|
| W1 | F1, F2, F3, F7 | 8 + 9 + 7 + 7 = 31 | 0 | **31** | 19 / 12 |
| W2 | F4, F5, F6, F9 | 6 + 7 + 2 + 5 = 20 | 4 (`thomas1981illusion`, `lasseter1987principles`, `silvio2019puppets`, `hoerl2015seeing`) | **24** | 17 / 7 |
| W3 | F8, F10, F11, F12, G | 7 + 2 + 3 + 10 + 2 = 24 | 0 | **24** | 12 / 12 |

W1 is the heaviest batch and the one §2 rests on, so it runs first; it is 31 rather than 25 because F2 rose to 9 at
Checkpoint A and F7 is a seven-card facet. If the Workflow wants three equal batches, move F7 (7 cards, 3 opus) from
W1 to W3, which gives 24 / 24 / 31; I prefer the prescribed order because F7's opacity reads should land before §4.2 is
drafted, alongside F1–F3's §2 reads. Within each batch, open full-text works go first, metadata cards last, so a
browser copy arriving mid-batch can still be taken up by the same writer. The verifier (writer ≠ verifier) re-checks
every card in the batch before Fable's hand check (S7).

## Record corrections S5 must apply (files left alone; the cards record them under Caution)

- **Registered years** (volume year in the key, online year in `registered_year`): `machery2012why` 2011; `bich2018is`
  2017; `meincke2019autopoiesis` 2018; `villalobos2018enactive` 2017; `humphreys2009philosophical` 2008;
  `zerilli2019transparency` 2018; `boge2022two` 2021; `sullivan2022understanding` 2019; `paleyes2023challenges` 2022;
  `clark2023social` 2022; `zednik2021solving` 2019; `sun2026between` 2025; `hoerl2015seeing` 2012. `bedau2010living`:
  Crossref 2010, OpenAlex 2009; Caution notes it. `bernini2025ai`: Crossref's only date is 2026-04-17; volume 59 is
  2025; the card records the date. `dipaolo2005autopoiesis`: print 2005, online 2006; no `registered_year`.
- **Govind / Reddy.** DataCite stores the single string "Govind Reddy" as `familyName`; OpenAlex displays "Reddy Govind".
  The key `govind2026illusion` follows Checkpoint A until the PDF byline or Roger settles it (Checkpoint B, 3); if Reddy
  is the surname the key becomes `reddy2026illusion` before S8.
- **Sun & Gualeni.** The version of record is the Springer chapter 10.1007/978-3-031-89037-6_3, pp. 49–63 (*Artificial
  Media*, Springer Series on Cultural Computing; online 2025-07-30, volume 2026); the key is `sun2026between`, the arXiv
  v1 (2501.15346) is the preprint and is named as such if it is the copy read.
- **Bottazzi Grifoni & Ferrario**, not "Bottazzi & Ferrario": the family name is two words (Crossref).
- **Meincke 2019**, *EJPS* 9(1), Article 5, not "EJPS 8" (2018).
- **Paleyes 2023** (volume 55(6)), not 2022; online 2022-12-07.
- **Karelin et al.** has six authors (Karelin, Nakajima, Soto-Astorga, Carr, James, Froese), not three; the card in
  reserve carries all six.
- **Crafton 2012**, not 2013. **Hooks**: the 2023 fifth edition (10.4324/9781003289753), not the 2017 DOI FACETS gives.
  **Tomko 2015**, subtitle "Poetic faith from Coleridge to Tolkien", not 2016 "…to the Present". **Kleist**: the 1972 *TDR*
  translation record lifts FACETS's "[unconfirmed]". **Clark & Fischer**: 10.1017/s0140525x22002825 is the reply, not the
  target article. **Magee et al.** subtitle is "Analysing AI as an automated subject" (CITED_WORKS row 13 stays wrong until
  S8's reference list is built from the records). **Montévil & Mossio 2015** replaces the sketch's "Mossio & Moreno 2010,
  HPLS" (no record). **Stovel & Shaw** and **Nissenbaum** are registry hits, not new cards. `monograph/albantakis2014evolution`
  is full_text, not metadata. `burrell2016how` is in `monograph`; the search tool's `burrell2016machine` tag is the
  `coordsov` key. **Hayes-Roth's initial** "F." is unconfirmed until the byline. **Tillis's subtitle**, **Purves's edition**,
  **Williams's edition** come from the title page or stay off the card.
- **Two Starks.** `stark2024animation` is Luke Stark (FAccT); `research/stark2024` is David Stark & Vanden Broeck. Cite with
  initials (APA 7 §8.20).
- **OpenAlex budget.** F8's arXiv items and all of F9 were checked without OpenAlex (429 from mid-F8); F10–G's list searches
  failed, single lookups answered. `SEARCH_LOG.md` carries this; S9's gap re-run and S4's OA checks for F9 (`green2000role`)
  happen after the daily reset.

## Checkpoint B — decisions for Roger

Each one line, with my recommendation. Everything else above is decided.

1. **c12 wording.** The G triage proposes: "AI development as a craft of animation, argued as a claim about what AI is:
   not the interface (Stark), not the illusion (Govind), not an ALife experiment (OpenLife)." **Recommend: accept**;
   it names the three nearest priors the gap search found and keeps the claim conceptual, which is where the verdict
   says it survives.
2. **Does c9 (triad) stay central?** Schumann & Du (end user / development team / product, in *P&T*) and Clark & Fischer
   (authorities as a third class of agent) show the venue and HRI have both seen a makers' triad; they help as precedent
   and threaten novelty. **Recommend: keep c9 central in the narrower form** "the studio *determines* what the viewer
   gets", cite both as prior triads and distinguish by the lab criterion (binding determination, own interest, keeping
   the parties apart), with the cards recording exactly what each source's third does, as ruling 4 of the dxd run did
   for Cameron et al.
3. **Govind vs Reddy key.** The record cannot settle the surname. **Recommend:** S4 reads the Zenodo PDF byline (CC BY,
   no login) and the key follows the byline's order; Roger decides only if the PDF is also ambiguous; default
   `govind2026illusion`.
4. **Where the life philosophy is carded.** Berthon's ALife arm holds only Dorin & Stepney 2024 locally, as a PDF with
   no card, and asks the lineage question. **Recommend: card it here** (F1 8 + F2 9 = 17 cards, with `dorin2024what`
   written from the copy Berthon's arm holds and `provenance.txt` naming it); `GAP_CHECK.md` cites the arm as Roger's
   own prior work, not as external prior work, and Berthon's arm points to these cards rather than duplicating them.
5. **Books he could open** (unanswered since Checkpoint A; until he does, each is a metadata card and a BROWSER_LIST row).
   §2: Moreno & Mossio 2015 (10.1007/978-94-017-9837-2, Springer, likely institutional), Maturana & Varela 1980
   (OL15015691W), Cleland 2019 (10.1017/9781139046893, Cambridge Core), Dennett 1987 (OL2463706W), Thompson 2007
   (OL3475244W, now reserve). §3–§5: Williams 2001 (OL6073254W), Crafton 2012 (10.1525/9780520352520), Hooks 2023
   (10.4324/9781003289753, pp. 19–20 first), Purves 2014 (10.5040/9781474222365), Auslander 2022 (10.4324/9781003031314),
   Tillis 1992 (OL1857491W), Thomas & Johnston 1981 (OL2924612W), Silvio 2019 (10.1515/9780824880989, ch. 1 pp. 18–52).
   §4.3: Walton 1990 (OL4801866W), Gerrig 1993 (OL4313731W), Tomko 2015 (10.5040/9781474218627). **Recommend:** open
   four first, in this order: Moreno & Mossio (the counter c4 must answer), Silvio ch. 1 (the definition the paper
   quotes through Stark), Dennett 1987, Walton; the rest can wait for Checkpoint C.
6. **Anything else.** (a) The F2 swap Thompson → Villalobos & Dewhurst changes the named list in his ruling 1; I
   approved it (reason above) and he can reverse it at no cost since Thompson stays on BROWSER_LIST. (b) If Sculley is
   promoted at S4, hold 75 by dropping `schaeffer2023are` to reserve (my default) or lift the ceiling to 76; if he lifts
   it, `karelin2025indeterminism` is the other candidate for a 76th or 77th card. **Recommend: hold 75.** (c) Zaharia et
   al. is a blog post carded as a web source with access date; *P&T* will take it as a citation, but the sketch's
   compound-AI premise then rests on a blog and a survey until Sculley lands. **Recommend: accept the web card and open
   the NeurIPS page.** (d) MacCormick ch. 12 is not carded; S9 opens it before the gap verdict closes (above). No
   decision needed unless it turns out to make the (B) claim.

## Checkpoint B — rulings (Roger, 2026-11-08)

Recorded by Claude from the author's answers.

1. **c12 wording: accepted.** "AI development as a craft of animation, argued as a claim about what AI
   is: not the interface (Stark 2024), not the illusion (Govind 2026), not an ALife experiment
   (OpenLife, Masumori et al. 2026)."
2. **c9: central, narrowed.** "The studio *determines* what the viewer gets." Schumann & Du (2022) and
   Clark & Fischer (2023) are cited as prior triads and distinguished by the lab criterion (binding
   determination, own interest, keeping the parties apart); their cards record exactly what each
   source's third party does.
3. **Life philosophy carded here.** The 17 F1–F2 cards live in this library; `dorin2024what` is written
   from the copy Berthon's arm holds, with `provenance.txt` naming it; Berthon's arm points here.
4. **Books: no answer again.** Treated as unopened; every book is a metadata card and a
   `BROWSER_LIST.md` row until a copy lands in `pt_ai_animation_local/inbox/`. Fable's order stands
   for when he opens them: Moreno & Mossio, Silvio ch. 1, Dennett 1987, Walton.
5. **Defaults taken (not asked):** Govind/Reddy key follows the Zenodo PDF byline at S4 (default
   `govind2026illusion`); ceiling holds at 75 (Sculley, if promoted, displaces `schaeffer2023are`);
   Zaharia accepted as a web card; MacCormick ch. 12 is an S9 must-read.
