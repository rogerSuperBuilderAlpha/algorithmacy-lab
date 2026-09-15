# Research Dossier — Algorithmacy Scaffolding

41 cards in `literature/library/`, built by six parallel research passes (Fable model), each
verifying claims against primary sources before writing anything down. This dossier maps what they
found back onto the essay's existing structure, names what needs fixing before the next draft, and
answers the open empirical-grounding question.

## 1. The novice/expert table — cell by cell

### Literacy (text & composition)

Solidly evidenced in outline, weaker than a two-column table implies in detail.
`flowerhayes1981.md` and `sommers1980.md` are both fully verified and do support a real
novice/expert contrast in composing behavior. But two complications surfaced that the table
currently hides:

- Flower & Hayes' own data shows novices *also* embed sub-processes — the difference is which
  goals drive the recursion, not whether recursion happens at all.
- Kellogg (`kellogg2008.md`) finds expert writers split between linear outline-planners and
  recursive redrafters, and the linear group often produces *better* text. "Linear = novice" is
  not the finding; "linear vs. recursive" is a strategy choice among experts, not a novice tell.
- `scardamaliabereiter1987.md` — the actual Rosenberg chapter (pp. 142–175) was not accessible
  (HathiTrust search-only). The card is built from secondary characterizations only. This citation
  needs a library-copy check before it goes back into a draft.

**Recommendation:** keep the knowledge-telling/knowledge-transforming distinction as the organizing
frame (it's real and citable), but soften "linear" as a synonym for "novice" — cite Kellogg
alongside it as the complicating case.

### Oracy (language acquisition & speech)

The expert half is old and well supported; the novice half is contested, not settled.

- `ellis1996.md` and `pawleysyder1983.md` fully verified: formulaic chunking in fluent speech is
  real and well documented.
- **DeKeyser 2007 citation problem:** two different "DeKeyser 2007" items exist in the SLA
  literature (the VanPatten & Williams chapter vs. the CUP *Practice in a Second Language* volume),
  and neither 2007 text was directly accessible — the card verifies against DeKeyser & Suzuki's 2025
  rewrite of the same chapter instead, flagged explicitly. Anyone quoting DeKeyser (2007) with a page
  number needs a library check first.
- DeKeyser (rule-driven novice) and Ellis (statistical-sequence-learning novice) are **rival
  accounts** of what a novice is doing, not a unified picture the table can cite as settled.
- The "rapid discourse repair" claim for experts is the weakest link in this row: Levelt
  (`levelt1999.md`) describes the monitor mechanism but says nothing about expertise, and Tavakoli &
  Uchihara's repair correlation (`tavakoliuchihara2020.md`) does not survive their own statistical
  correction.

**Recommendation:** keep formulaic fluency (well-supported); drop or heavily hedge the "rapid
discourse repair" claim, or replace it with something the Levelt/Tavakoli-Uchihara evidence actually
carries.

### Numeracy (mathematical reasoning)

Best-evidenced row for the novice half, weakest for the specific "offloading" claim.

- `yarlassloutsky2000.md` is the strongest single piece of evidence in the whole dossier: a
  controlled, ability-matched experiment showing novices choose on surface features 10–20% of the
  time against experts' ~80%, and — the useful nuance — novices *have* the relational knowledge but
  lose it to surface salience under competition. Real citation, correctly attributed, full text read.
- `inglisalcock2012.md` verified, but its actual finding is narrower than "non-linear scanning":
  experts move back-and-forth between *adjacent* lines seeking warrants; the paper found **no**
  global back-and-forth scanning. "Non-linear scanning across proof dependencies" overstates what
  this source shows.
- `stylianousilver2004.md` and `shepherdvandesande2014.md` are abstract-only (paywalled) — flagged,
  not fully verified.
- **Quinby et al. 2021 citation is wrong and doesn't support the claim it's attached to.** The
  original draft cites "Quinby, B. et al." — there is no B. Quinby; the actual author is **Francis**
  Quinby (Quinby, Kim, Pollanen, Burr & Reynolds, HCII 2021, LNCS 12767). Worse: the paper is a study
  of *typesetting software input models* (structure-based vs. free-form equation editors), not of
  problem-solving offloading, found "few differences" by expertise, and its own abstract calls the
  cognitive-load results inconclusive. **It cannot carry the "offload working-memory strain into 2D
  notation" claim as written.** The card names a real candidate replacement (Risko & Gilbert 2016 on
  cognitive offloading, or the external-representations-in-problem-solving literature) — that
  citation still needs to be run down before the offloading sentence can stand.

**Recommendation:** this row needs the most repair of the three — fix the Quinby attribution, soften
"non-linear scanning" to Inglis & Alcock's actual finding (local back-tracking for warrants), and
either find a real offloading source or cut that clause.

## 2. Theoretical framing — status

Adapted (not re-verified from scratch, since already verified elsewhere) into this paper's own
library with fresh "Relation to the argument" sections: Stark (`starkvandenbroeck2024.md` as the
central coopt/platform source, `stark2009.md` for the heterarchy/network boundary case), Reich 1964,
Selznick 1949, Aneesh 2009, Wilkinson 1965.

**One correction that matters for the essay's own argument:** Wilkinson (1965) coined "oracy" but is
**not** the source for the scribal-monopoly-to-universal-literacy historical sequence the essay
leans on ("only a select class needed to be literate until the printing press"). That specific claim
needs a different citation — Goody, Ong, or Eisenstein on print and the democratization of literacy.
Cite Wilkinson only for the oracy/literacy/numeracy naming convention itself, not for the print-press
history.

New research (genuinely new cards, not adaptations):

- **Gold-standard-to-floating-FX shift:** `knorrcetinabruegger2002.md` is a strong find — a
  sociology-of-finance account of FX trading becoming a decentralized "flow structure" through the
  1970s–80s (end of exchange controls, Reuters Monitor 1973, Reuters dealing 1981), which is exactly
  the institutional-algorithmacy case the essay wants. `eichengreen2019.md` supports the broader
  history but full text wasn't read — flagged, check before quoting.
- **Common-law litigation as procedural algorithmacy:** `llewellyn1930.md` (Llewellyn's *Bramble
  Bush*, read in full) directly supports "the strict doctrine... is the technique to be learned" —
  a clean fit. `galanter1974.md` read at second hand via citing literature; flagged for a full-text
  check.

## 3. Human factors / design considerations — the open empirical-grounding question

You asked which of the three candidate case studies has the strongest grounding. Both HCI agents
returned honest, not flattering, assessments:

**Algorithmic feed controls — recommended as the primary anchor.** `eslami2015.md` (FeedVis, CHI
'15) is the strongest single empirical grounding in the whole design-considerations section: a built
and tested artifact that instantiates three of the four proposed affordances directly (counterfactual
curated-vs-unfiltered view, chunked "Friend View," frictional revelation of the algorithm's
existence). `radercottercho2018.md` then supplies the controlled-experiment failure mode — text
explanations raise awareness but *lower* felt control and fairness (n=681) — which is exactly the
kind of finding a design section needs to state its affordances' costs honestly rather than as pure
wins.

**Algorithmic/gig-work scheduling — recommended as a secondary case, not primary.** Strong as
organizational theory (`kellogg2020.md`, `lee2015.md`, `rahman2021.md`), weak as evidence *for* the
proposed affordances: no source in this domain tests a scaffolding intervention, platforms have a
documented interest in blocking exactly this kind of transparency (Lee's "strategic ignorance,"
Rahman's anti-gaming rationale), and Lee reports drivers didn't feel entitled to more control in the
first place. Use this case to show what happens when the affordances are *absent and actively
resisted* — a contrast case, not a demonstration case.

**Prompt-engineering/AI interfaces — weakest grounding, use with named caveats or drop.** The
agent's own assessment: "nothing measures expert prompters," sample sizes for the relevant tooling
studies run 10–20, and — most importantly — one verified finding directly **contradicts** affordance
(1) as written. `bo2025.md` found token-level confidence-highlighting on GPT-4o *worsened*
calibration and induced aversion; `bucinca2021.md`'s confidence-percentage baseline did nothing.
Chunking (affordance 3) is the best-supported piece here (`wu2022.md`, within-subjects, logged
behavior change). If this case study stays in the paper, affordance (1) — "expose optimization
functions and system confidence directly" — needs to be reframed as a contested hypothesis, not a
supported design move, or cut back to the chunking claim alone.

**Bottom line:** lead the design section with feeds (Eslami + Rader/Cotter/Cho), use gig-work
scheduling as the "what happens without these affordances" counterpoint, and either heavily caveat
or drop the confidence-exposure claim in the AI-interface case — the evidence you now have runs
against it, not for it.

## 4. Citation and access flags requiring action before next draft

- **Fix:** "Quinby, B. et al. (2021)" → Francis Quinby et al. (2021); the source doesn't support the
  offloading claim regardless — find or cut.
- **Fix:** Wilkinson 1965 is cited for the wrong historical claim (oracy naming, not the
  print-and-literacy-democratization sequence).
- **Check before quoting:** DeKeyser (2007) — verified against a 2025 rewrite, not the 2007 text
  itself; Scardamalia & Bereiter (1987) — verified only from secondary characterizations, not the
  primary chapter; Stylianou & Silver (2004) and Shepherd & van de Sande (2014) — abstract-only;
  Eichengreen (2019) and Galanter (1974) — not read in full.
- **Soften:** "non-linear scanning across proof dependencies" (Inglis & Alcock found local
  back-tracking, not global scanning); "rapid discourse repair" for oracy experts (weakest-supported
  claim in that row); "linear = novice" for literacy (Kellogg's expert linear-planners complicate this).

## 5. What's solid and needs no repair

Flower & Hayes 1981, Ellis 1996, Yarlas & Sloutsky 2000, Eslami et al. 2015, Rader, Cotter & Cho
2018, Reich 1964, Stark & Vanden Broeck 2024, Llewellyn 1930, and Knorr Cetina & Bruegger 2002 are
all fully verified against primary sources and directly support the claims the essay attaches to
them. These can be cited with confidence.
