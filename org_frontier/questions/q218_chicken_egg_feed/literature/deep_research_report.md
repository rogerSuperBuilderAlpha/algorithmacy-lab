# Q218 — Stage 2 literature report

**Scope.** Eighteen external sources in four strands, plus the lab's own prior studies. Each was verified
against its Crossref record (title, authors, venue, volume, pages, year) before inclusion. OA is marked only
where the venue is open access. A targeted search, not a systematic review.

## 1. Social contagion, thresholds, and cascades

| source | what it establishes | bearing on Q218 | access |
|---|---|---|---|
| Granovetter (1978), *AJS* 83(6):1420–1443 | collective behavior from individual adoption thresholds | the fans' reaction rules are threshold rules over what they see | DOI |
| Bikhchandani, Hirshleifer & Welch (1992), *JPE* 100(5):992–1026 | informational cascades: people follow predecessors' observed actions | an audience reacting to others' reactions (the COUNTS variants) | DOI |
| Banerjee (1992), *QJE* 107(3):797–817 | herd behavior from sequential observation | same | DOI |
| Kempe, Kleinberg & Tardos (2003), KDD, pp. 137–146 | independent-cascade and linear-threshold diffusion models; influence maximization | the standard formal diffusion models, which are seeded from a source set (a first cause by construction) | DOI |
| Centola & Macy (2007), *AJS* 113(3):702–734 | complex contagions need multiple exposures | why an AND-type versus OR-type reaction rule matters (encoding sweeps) | DOI |
| Centola (2010), *Science* 329:1194–1197 | behavior spreads further in clustered networks in an online experiment | fan–fan reinforcement (CONTAGION) | DOI |

## 2. Online diffusion and popularity

| source | what it establishes | bearing | access |
|---|---|---|---|
| Salganik, Dodds & Watts (2006), *Science* 311:854–856 | showing download counts increases inequality and unpredictability of success | the "audience sees raw counts" variant | DOI |
| Goel, Anderson, Hofman & Watts (2016), *Management Science* 62(1):180–196 | online cascades range from broadcast-like to viral; structural virality measures the difference | BROADCAST versus CONTAGION as the two ends of that range | DOI |
| Vosoughi, Roy & Aral (2018), *Science* 359:1146–1151 | false news spreads farther and faster than true news on Twitter | motivation: controversial content spreads through reactions | DOI |

## 3. Algorithmic amplification and recommender feedback loops

| source | what it establishes | bearing | access |
|---|---|---|---|
| Bakshy, Messing & Adamic (2015), *Science* 348:1130–1132 | Facebook's ranked feed modestly reduces exposure to cross-cutting content, with individual choice mattering more | a ranked feed as a mediator between source and audience | DOI |
| Chaney, Stewart & Engelhardt (2018), RecSys, pp. 224–232 | recommenders trained on data their own recommendations shaped homogenize behavior (algorithmic confounding) | the feed–audience loop: the feed reads reactions it caused | DOI |
| Jiang et al. (2019), AIES, pp. 383–390 | degenerate feedback loops between recommender and user interest | the same loop, formalized | DOI |
| Huszár et al. (2022), *PNAS* 119(1):e2025334119 | a randomized comparison of Twitter's ranked timeline with a reverse-chronological control found algorithmic amplification of political content | the empirical counterpart of FEED-ENG versus FEED-CHRONO | OA |

## 4. IIT, feedforward structure, and PyPhi

| source | what it establishes | bearing | access |
|---|---|---|---|
| Tononi (2004), *BMC Neuroscience* 5:42 | introduces Φ, integrated information over the minimum information bipartition | origin of the measure | OA |
| Oizumi, Albantakis & Tononi (2014), *PLoS Comput. Biol.* 10(5):e1003588 | IIT 3.0; purely feedforward systems have Φ = 0 | the "no first cause ↔ Φ > 0" link in its known form; H1 is this property | OA |
| Albantakis et al. (2023), *PLoS Comput. Biol.* 19(10):e1011465 | IIT 4.0; system Φ over the minimum partition (a unidirectional cut costs nothing) | the measure used | OA |
| Mayner et al. (2018), *PLoS Comput. Biol.* 14(7):e1006343 | PyPhi | the software | OA |
| Doerig, Schurger, Hess & Herzog (2019), *Consciousness and Cognition* 72:49–59 | the "unfolding argument": a recurrent network can be unfolded into a feedforward one with the same input–output behavior and Φ = 0 | a caution: Φ reads causal structure, not observed behavior; two arrangements that spread a post identically can differ in Φ | DOI |

## 5. The lab's own prior work
The atlas (one-way gates sink whole-system Φ; rotations bind), `studies/hybrid_ff_recurrent_seam/` (cores
stay in the recurrent zone), the canonical triad and controls, Q215 (measure dependence), and the recurrence
arm. See `review.md`.

## What is known and what is open
Known: a feedforward system has Φ = 0 (Oizumi et al. 2014), so any arrangement with an unmoved first mover
reads dyadic at the whole system; the lab's atlas and seam studies show the same for coordination forms.
The diffusion literature models spread from seed sets and the recommender literature documents feed–user
loops, but none uses a structural irreducibility criterion or asks which ingredient (ranking algorithm,
audience visibility, or a reacting source) removes the first cause. Q218 asks that, and reports which of its
answers are restatements of known IIT properties.

## What a further pass should check
Empirical work on creators' responses to engagement metrics (the "celebrity reacts" link); cascade data in
which the platform's ranking decisions are logged, so that a model could be elicited rather than stipulated;
and the recurrence arm's lead–lag measures as a behavioral complement.
