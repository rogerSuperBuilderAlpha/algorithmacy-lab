# Davis — findings

The Heider paper's verdict on the all-negative triad was the two-camp verdict. With one bit per person that
paper found ++− and −−− identical — Φ = 6, all three in the core, no rest state. Give each person a camp from
an alphabet of k and encode it in two bits: at k = 2 the all-negative triad still has all three in its core
and no rest state; at k = 3 and k = 4 it rests, in exactly one partition — three singletons — and its core
is two persons at Φ = 2.000 (H3, all-negative clause, confirmed). The forbidden triad ++− has all three in
its core at k = 4 with Φ = 6.000 — the Heider number — and no rest state at any k (its core dips to two
persons at k = 3, an encoding with a dead code; H3 partial on that clause). At k = 4 the four triangles sort
as Davis says: ppm alone has all three persons in the core; ppp has no complex, and pmm and mmm have a
two-person core at 2.000 (H2 confirmed). Davis's theorem holds on every one of the 64 signed K4 patterns —
rest states exist iff no cycle has exactly one negative line, the triangle test suffices, and each of the 15
clusterable patterns has one partition (H4 confirmed) — and on the four triangles (H1 confirmed). The
negative path with no closing line is clusterable in two partitions and its core is one negative pair
(H5 confirmed). The instrument sides with Davis over Cartwright–Harary once it is allowed a third camp, and
the Heider paper's H3 refutation is withdrawn as an artifact of the alphabet.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | Theorem 1 on triangles | **CONFIRMED** | k ≥ 3: ppp, pmm, mmm rest (3/6/… states), ppm never; k = 2: mmm 0 rest states |
| H2 | classes follow clusterability at k = 4 | **CONFIRMED** | ppm core {p, o, q} 6.000; ppp none; pmm {p, o} 2.000; mmm {p, q} 2.000 |
| H3 | the −−− verdict depends on the alphabet; ++− does not | **PARTIAL** | mmm core persons over k = 2, 3, 4: 3, 2, 2 ✓; ppm: 3, 2, 3 ✗ (k = 3) |
| H4 | Theorem 1 on K4; triangles decide; unique clustering | **CONFIRMED** | 64 patterns, 15 clusterable (8 balanced); rest ⇔ clusterable 64/64; triangle = cycle 64/64; 1 partition 15/15 |
| H5 | the incomplete graph | **CONFIRMED** | path −−: 2 partitions ({p}{o}{q}, {p,q}{o}); core {o, q} 2.000; Φ_MIP 0 |

Instrument control passed in all five probes (Φ = 2.000000, core {A, M, B}).

## Caveats

- Two-bit encodings with a dead code (k = 2 in two bits; k = 3) are not clean comparisons: k = 2 in two
  bits gives cores at Φ 1.024 (mmm) and 0.639 (ppm) where the Heider paper's one bit gave 6.000 for both,
  and k = 3 gives ppm a two-person core. The clean pair is the Heider paper's one bit (two camps, bits full)
  against k = 4 here (four camps, bits full): there ppm reproduces Φ 6.000 on the three high bits and mmm
  falls to a two-person core.
- Synchronous update: two persons swapping camps at once produce cycles even where rest states exist
  (pmm, mmm at k ≥ 3; 11 of 15 clusterable K4 patterns). The theorem is about the existence of rest states
  and is tested as such.
- Tie-break to the lowest camp is a bias; a random or held tie-break would move the core's bits, not
  (predictably) its person count.
- Φ on K4 (eight units) was not run.
- In-silico; no group is measured.

## Disclosure

Triangle and path dynamics, and the mmm k = 4 Φ run, were computed before `hypotheses.md` was fixed
(instrument check and timing). H2–H3's remaining runs and the K4 census were blind.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_theorem
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_classes    # ~18 min
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_alphabet   # ~18 min
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_census
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_path       # ~2 min
```
