# Source audit — all 124 cited references — 2026-08-18

Six reviewers, one slice each, no gaps and no overlaps. Per-source evidence in `sources_01.md`
through `sources_06.md`. This file adjudicates.

**Method.** Identity was established only at the publisher's own record or at the DOI resolver's
publisher-deposited registration metadata. No aggregator, search summary or trade page was accepted
as evidence of identity. That rule was chosen because all three of this project's prior
author-fabrication catches entered through exactly those channels.

**Independent spot-check.** Three findings were re-verified by hand against the DOI resolver, drawn
from three different reviewers' slices: `zhou2025competency` (confirmed — Lian Zhou, Mingwei Liu,
Xinran Huang), `choichao2024reactions` (confirmed — Jungmin Choi, and now in print at 52(3),
671–691), `pijls2017measuring` (authors confirmed correct; that reviewer's finding was about
content, not identity). The reviewers are reliable.

---

## Verdict

**No reference is fabricated. Every one of the 124 resolves to a real, published work.** That was
the first question and the answer is clean.

**But roughly one reference in four carries a wrong author list**, and the manuscript cannot be
submitted with them.

| | count |
|---|---|
| references checked | 124 |
| identity confirmed as recorded | 90 |
| **divergent** | **34** |
| of which **corrupted author given names** | **~27** |
| full texts newly obtained and read | ~55 |

---

## The systemic finding

The corruption has one signature, and it is consistent across all six slices: **family names correct,
author order correct, given names wrong.**

- `brochado2026phygital` — 6 of 9 given names wrong
- `devos2026employee` — 7 of 10 wrong
- `lin2026voice` — all four wrong
- `shabnam2026tpsr` — four wrong, plus a volume that does not exist
- `moganadas2026wellbeing` — three wrong, in an entry claiming `readdepth=full-text`
- `hemmer2025complementarity` — a fifth author omitted entirely, two others swapped

Two properties make it dangerous.

**The wrong names belong to real people.** Yijun Xing, Xu Huang, Le Zhou, Gurmeet Singh, Jaee Choi
and Woo Hyuk Lee are all real scholars — simply not the authors of these papers. A spot check finds a
plausible person and stops. This is why the corruption survived three prior verification sweeps.

**It concentrates in recent work.** In one slice, seven of the eight 2025–26 entries were corrupted.
Recent papers are thinly indexed, so whatever assembled these entries had least ground truth exactly
where it confabulated most.

**Several corrupted entries claim `readdepth=full-text`.** `moscalarosa2019` has both a wrong
co-author given name and wrong pages while claiming a full-text read on 2026-08-11.
`casalegno2020circular` and `moganadas2026wellbeing` are the same shape. Those reads did not happen
as recorded, and the read-depth field cannot be trusted as evidence.

**Why no tool here could have caught it.** `check_citations.py`, `preflight.py` and
`build_index.py` all compare the manuscript against the bibliography, or the bibliography against
itself. Nothing in this repository has ever compared the bibliography against the world. The audit
that found this is the first of its kind on this project.

---

## Corrections to make in `references.bib`

At source, never in the rendered list — a rendered-list edit was silently reverted twice on
2026-08-17.

| citekey | correction |
|---|---|
| brochado2026phygital | Bora Qesja · Samaneh Soleimani · Sarah Renee Brodhead Ahmadi · Kay-Anne Haykal · Gediminas Lipnickas · Joanne Harris |
| devos2026employee | same author team, seven given names |
| devos2024disabilities | Bora Qesja · Ged Lipnickas · Joanne Harris |
| devos2023einteraction | same names; **and see the size problem below** |
| lin2026voice | Wanliang Lin · Mingyu Zhang · Wenjia Zhang · Can Zhang |
| shabnam2026tpsr | Saadia Shabnam · Yonathan Silvain Roten · Gaganpreet Singh · Hairong Li; **delete volume 40(4) — ahead of print, no issue** |
| zhou2025competency | Lian Zhou · Mingwei Liu · Xinran Huang |
| spektor2025working | Somang Min · Grace Sarfo |
| xing2026algorithmic | Yunfei Xing · Justin Z. Zhang |
| schmidt2025field | Alexander Lennart Schmidt · Klaas Koerten |
| shi2025residents | all three given names, incl. Carla Estefanía Samaniego-Chávez |
| choichao2024reactions | **Jungmin** Choi; untruncate title; add 52(3), 671–691 |
| leelu2024consciousness | **Wangoo** Lee |
| hemmer2025complementarity | add fifth author **Gerhard Satzger**; unswap Kühl/Vössing; 34(6), 979–1002 |
| duggan2026tensions | **Prakriti** Dasgupta |
| gaothebault2026townie | **Zihan** Gao; add PACM HCI 10(2) |
| pan2025dark | Su-Ying Pan · Yangpeng Lin |
| park2026lobbies | Soona Park · Jianan Z. Lee |
| pigac2026transparency | Tilen Pigac · Ava Huang |
| mosca2025phygital | Hafsa Shakil; 46(3) is the Sept **2026** issue |
| moganadas2026wellbeing | Sharmila Rani Moganadas · Gerald Guan Gan Goh · Chew Sze Cheah |
| andreev2025destination | **Petros** Kosmas |
| moscalarosa2019 | **Emily** La Rosa; pages **82–94** |
| casalegno2020circular | pages **149–164** |
| sharmamattila2025rights | now **2026**, 50(6), 904–920 — no longer OnlineFirst |
| mosca2026ai | version of record self-cites as **2025** |
| filippas2022inflation | Golden, Joseph **M.** |
| nguyen2024stereotypes | 80(7):1413–1426 is the **2025** issue |
| pedersen2022 | 33(1):80–93 is the **2023** issue |

**Three prior disputes are resolved in the bibliography's favour — no change needed.**
`phillips2024physical` has exactly three authors and the invented names appear nowhere; its 2024 +
print-issue locators are internally consistent. `padigar2024friction`'s year field (2025) is right.
`odekerken2021service`'s 2022 is right.

---

## Sources cited against what they actually found

Worse than a wrong name, and only visible once someone reads the paper.

1. **`folger1977voice` — the claim is contradicted and the source is unreachable.** Identity confirmed
   at the APA-deposited record; the full text is closed on every route tried since 8 August. But the
   reviewer read **Lind, Kanfer & Earley (1990)** in full, and it classifies Folger 1977 among the
   **frustration effect** studies. The manuscript's "voice has value independent of outcome" reading
   is supported by nothing reachable and contradicted by everything. `claim-contradicted` stands.
2. **`huanglo2025failure` — the bib title is not the paper's title**, and the note's gloss reverses
   the finding: the paper shows a humanness **penalty** in process failures, not a preference for
   humans.
3. **`lin2026voice` — algorithmic feedback *raises* voice (+.345)** while directing, scheduling and
   monitoring suppress it. Any flat silence claim misstates a quarter of the result.
4. **`christin2017practice` — her finding is decoupling and buffering**: practitioners blunt the
   algorithms. Cite contest over discretion, not accomplished relocation.
5. **`garcia2026strategic` — its punchline favours full automation.** The manuscript deploys it
   against automation.
6. **`pijls2017measuring` — the instrument cannot carry a guest-agency claim.** The two agency items,
   "having choice" and "feeling independent," were **dropped during CFA for low loadings**. The
   project's own audit called this "the paper's most exposed citation"; it was right.
7. **`spektor2023designing` — two overstatements.** The rejection affordance was a prototype **the
   workers themselves rejected**, and full-task-list withholding occurred "only in the most limited
   configurations," with many systems letting attendants see their whole board.
8. **`manfreda2025reciprocal` — framed as altruism, generosity and fictive kinship, not gratitude.**
   The gratitude-versus-obligation contrast in §2 is unverified.
9. **`zhou2025competency` — the appeal argument rests on one weak item.** Three validated remediating
   items; only one mentions appeal, and it carries the weakest loadings.
10. **`fink2025oversight` — "liability sponges" is Fink quoting Crootof, Kaminski and Nicholson
    Price**, not her coinage. Still unpublished (forthcoming chapter), so the don't-carry-alone rule
    stands.
11. **`devos2023einteraction` is a one-page conference abstract** (p. 438) carrying a substantive
    claim about employees reformulating guest requests.
12. **`mohlmann2021algorithmic` — matching and control are two parallel dimensions**, not a temporal
    conversion.
13. **`martinwaldman2022legitimate` — oversight and audit *lowered* perceived legitimacy**; only
    appeals raised it. A caution for the fourth design principle.

---

## Resolved in the manuscript's favour

- **`bovens2007accountability` — read in full** (Utrecht DSpace API). The actor–forum definition is
  verbatim correct at p. 450, and Bovens's insistence that transparency is not accountability
  strengthens the paper's use of him. Both the card and the bib were wrong about this, in opposite
  directions.
- **`okhuysenbechky2009`** — accountability, predictability and common understanding confirmed
  verbatim as the three integrating conditions, from the publisher's own abstract.
- **`lind1990voice` — obtained and read.** It does carry post-decision voice. But it arrives with
  conditions the manuscript must state: pre-decision beats post-decision, a perceived-control
  confound absorbs most of the effect, and it carries **Folger's own frustration-effect boundary** —
  sham voice backfires.
- **`lynch2011theorizing` — read in full**, closing a metadata-only gap on the journal's founding
  editorial. Its "Hospitality and virtuality" agenda item and Ciborra discussion of technology as
  guest and host are the strongest available fit warrant — and a caution, since the editorial already
  contemplated non-human hosts.
- **`germannmolz2026`** — settled from the deposited abstract: "originally conceived to describe the
  **blurring** of hosting and guesting practices," read in two directions, with erasure one of three
  operations. The §1 pivot's erasure-only reading overreads her.

---

## What this audit did not settle

Roughly 69 of 124 full texts remain unobtained. Publishers block programmatic clients almost
universally: ScienceDirect, SAGE, Springer, Emerald, Wiley, Taylor & Francis, ACM, INFORMS, MDPI,
Intellect and MIT Press all refused. The ranked list of what to obtain, and what rides on each, is
in `OBTAIN.md`.

Claim-fit — whether each source supports the sentence citing it in **Pierre's v3** — is not covered
here. v3 does not yet exist as a file. That is the other half of the job.
