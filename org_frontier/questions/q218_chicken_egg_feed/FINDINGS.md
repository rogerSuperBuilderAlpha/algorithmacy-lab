# Q218 findings — no first cause needs a loop, but a loop is not enough; the engagement feed with look-alike fans factors

Three hypotheses confirmed, two refuted. Every arrangement with an unmoved first mover reads dyadic, as IIT
requires; that part is a known property, not a discovery. The surprise is the headline chicken-and-egg form:
a celebrity who posts again when trending, an engagement feed, and fans who react to the feed close a loop
in which nothing comes first, and the whole still factors (Φ = 0). The celebrity and the feed bind as a pair
({P,F}, Φ = 2.000); the fans, who react identically, are interchangeable and fall outside. Word of mouth with
a reacting celebrity and no algorithm at all is the most integrated form (Φ = 6.000).

These are stylized models; nothing here measures a real platform, account, or audience.

## Per-form results

"First cause?" = is the causal graph not strongly connected (some part influences the rest without being
influenced back).

| form | first cause? | whole-system verdict | whole Φ | major complex | core Φ | subsets tied at top Φ (exploratory) |
|---|---|---|---|---|---|---|
| BROADCAST | yes (celebrity) | dyadic | 0.000 | {P} only | 1.000 | none of size ≥ 2 |
| CONTAGION | yes (celebrity) | dyadic | 0.000 | {A,B} | 2.000 | {A,B} |
| WOM-REACT | **no** | **triadic** | **6.000** | {P,A,B} | 6.000 | {P,A,B} |
| FEED-CHRONO | yes (celebrity) | dyadic | 0.000 | {P} only | 1.000 | none of size ≥ 2 |
| FEED-CHRONO-REACT | **no** | **triadic** | 1.000 | {P,F,B} | 2.000 | {P,F,A} {P,F,B} |
| FEED-ENG | yes (celebrity) | dyadic | 0.000 | {F,A,B} | 2.000 | {F,A} {F,B} {F,A,B} |
| FEED-ENG-REACT | **no** | dyadic | 0.000 | {P,F} | 2.000 | {P,F} |
| FEED-ENG-COUNTS | yes (celebrity) | dyadic | 0.000 | {F,A,B} | 6.000 | {F,A,B} |
| FEED-ENG-REACT-COUNTS | **no** | dyadic | 0.000 | {A,B} | 2.000 | {P,F} {A,B} |
| CHAIN (control) | yes | dyadic | 0.000 | {P} only | 1.000 | none of size ≥ 2 |
| RING (control) | **no** | **triadic** | 2.000 | {P,F,A,B} | 2.000 | {P,F,A,B} |

The {P}-only cores are the celebrity's persistence self-loop (P' = P), not a coordination.

Encoding sweeps (triadic of 10): S1 FEED-ENG-REACT feed rule 4/10 (OR, NOR, XOR, XNOR bind; AND, NAND and
the four one-input-negated rules factor); S2 FEED-ENG feed rule 0/10 (never strongly connected); S3
FEED-ENG-REACT-COUNTS fan rule 6/10; S4 WOM-REACT celebrity rule 9/10.

Connectivity over all 51 forms (11 + 40 sweep variants): triadic and strongly connected 22; dyadic and
strongly connected 13; triadic and not strongly connected 0; dyadic and not strongly connected 16.

## Hypotheses

| H | verdict | key numbers |
|---|---|---|
| H1 feedforward forms Φ = 0 (known IIT property) | confirmed | BROADCAST, FEED-CHRONO, CHAIN: Φ = 0.000, no subset of ≥ 2 nodes with Φ > 0 |
| H2 unmoved celebrity factors the whole; loop core excludes them | confirmed (6/6) | CONTAGION core {A,B} 2.000; FEED-ENG core {F,A,B} 2.000; FEED-ENG-COUNTS core {F,A,B} 6.000; all three Φ = 0 |
| H3 reacting celebrity closes the loop, triadic with full core | **refuted (0/4)** | FEED-ENG-REACT Φ = 0, core {P,F}; FEED-ENG-REACT-COUNTS Φ = 0, core {A,B} (tied with {P,F}) |
| H4 recurrence, not the algorithm, removes the first cause | confirmed (3/3) | WOM-REACT 6.000; FEED-CHRONO-REACT 1.000; RING 2.000 |
| H5 Φ > 0 ⇔ strongly connected; S1 robust | **refuted (1/3)** | Φ > 0 ⇒ strongly connected: 0 exceptions in 51 (met, and expected from IIT); strongly connected ⇒ Φ > 0: 22/35 = 0.63 (threshold 0.90, failed); S1 4/10 (threshold 8, failed) |

## Exploratory, after the first run (not pre-registered)
To see why FEED-ENG-REACT factors, three variants were run:
- **One fan** (P' = F, F' = P ∧ A, A' = F): triadic, Φ = 2.000, core {P,F,A}. This is exactly the lab's
  canonical triad.
- **Fans differ** (B reacts only if the feed shows the post and A reacted): dyadic, core {P,F}.
- **Feed needs both fans** (F' = P ∧ A ∧ B): triadic, Φ = 3.000, core {P,F,A,B}.
With two fans who react the same way and a feed that needs any one of them, neither fan is needed, so the
loop runs through the celebrity and the feed alone. When the feed needs every fan, every fan is bound in.
This matches the lab's quorum and substitution results (atlas Theme A; `studies/gig_substitution/`):
interchangeable parties drop out of the core.

## What it says
- **"First cause" has an exact counterpart, and it is not new.** A one-way source makes Φ = 0 in every
  form, with no exception in 51. That is how IIT defines Φ (a cut along a one-way link costs nothing;
  Oizumi et al. 2014), so H1 and the forward half of H5 restate the theory rather than discover anything.
- **No first cause is necessary but not sufficient.** Thirteen of 35 loop forms still factor. The
  intuition "a loop means no part comes first, so the whole is irreducible" is half right.
- **The algorithm is not what binds.** The engagement feed with a reacting celebrity factors under its base
  rule and binds in only 4 of 10 feed rules; word of mouth with a reacting celebrity and no feed binds in 9
  of 10 and reaches the highest Φ. A chronological feed with a reacting celebrity also binds (1.000).
- **Who is bound depends on whether each party is needed.** The chicken-and-egg loop that survives in
  the engagement-feed models is celebrity ↔ feed; the audience is bound only when each audience member
  makes a difference (one fan, or a feed that needs all of them).

## Caveats
- Stylized 3–4 node synchronous models with rules chosen by the study (`methods.md`). Two fans stand in
  for an audience; real audiences are large and heterogeneous.
- Several verdicts depend on the rule encoding (S1 4/10, S3 6/10).
- Major-complex ties occur in four forms; the tie table and the exploratory variants were not
  pre-registered.
- Φ reads causal structure, not observed behavior: by the unfolding argument (Doerig et al. 2019), a
  feedforward system can reproduce a loop's behavior with Φ = 0. Nothing here is a claim about consciousness.
- IIT 4.0 only (Q215). The validation gap is unchanged.

**Reproduce.** `python -m org_frontier.questions.q218_chicken_egg_feed.probe_chicken_egg_feed` (about 30 s;
`--plot` writes `results/chicken_egg.png`). Outputs: `results/forms.csv`, `results/sweeps.csv`,
`results/run.txt`.
