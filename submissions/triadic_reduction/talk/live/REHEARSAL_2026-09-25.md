# Rehearsal — 25 September 2026

Opus 5.5 (`claude-opus-5-5`, the model that will run live) rehearsed the live session on the author's
laptop (10 cores, 16 GB; other sessions running, load average about 3.3). Python 3.12.13 from
`~/iit-playground/venv-4.0`, `PYPHI_WELCOME_OFF=true`, repo root
`/Users/ludwitt/iit-playground/wt-triadic-reduction`. Times are wall clock. "Compute" is the time
inside the call, and "process" includes the Python start and PyPhi import.

**Result.** Every rehearsed output matched its registered string in `ci/reproduce.json`, both through the
raw reader and through `show.py`. No mismatch. Six nodes are too slow for the room.

## 1. Instrument

```
$ python -m org_frontier.classifier.validate
...
  All controls and built-in forms pass. Instrument validated.
real 3.22
```

## 2. Raw calls, one process each (no helper)

```
$ python -c 'from org_frontier.thinkers.peirce.probe_peirce_joint_determination import read; r=read("dispatcher", (("A","M","B"), [lambda x: x[1], lambda x: x[0]&x[2], lambda x: x[1]])); print(r["seconds"])'
  dispatcher             Φ_MIP=2.000000  core=('A', 'B', 'M')        jd=True  in_whole=True   M <- AB (φ=2.000)
0.17
real 1.87

$ python -c '... from org_frontier.thinkers.simmel.forms import MEDIATOR_ELIMINATED as F; r=read("mediator_eliminated", F) ...'
  mediator_eliminated    Φ_MIP=0.000000  core=('A', 'B')             jd=False in_whole=False  none
0.07
real 1.57

$ python -c '... MAJORITY_TRIAD, then UNANIMITY_TRIAD ...'
  majority_triad         Φ_MIP=0.000000  core=()                     jd=True  in_whole=False  C <- AB (φ=0.500, tied)
0.28
  unanimity_triad        Φ_MIP=6.000000  core=('A', 'B', 'C')        jd=True  in_whole=True   A <- BC (φ=0.250), B <- AC (φ=0.250), C <- AB (φ=0.250)
0.37
real 2.16

$ python -c '... from org_frontier.thinkers.simmel.forms import clique; r=read("clique_4", clique(4)) ...'
  clique_4               Φ_MIP=12.000000  core=('A', 'B', 'C', 'D')   jd=True  in_whole=True   A <- BCD (φ=0.250), B <- ACD (φ=0.250), C <- ABD (φ=0.250), D <- ABC (φ=0.250)
7.19
real 8.76

$ python -c 'from org_frontier.classifier.contingency import contingency_test as ct; print(ct([lambda x: x[2], lambda x: x[0], lambda x: x[1]], ("M","D","B"), "D", downstream="B", upstream="M").line())'
contingent margin=2.000  D in core: constrained=True bypass=False  (Phi 2.000 -> 0.000)
real 1.91
```

## 3. Helper against the registry

`final.py` (scratch, not kept) ran each form through the raw reader and through `show()` in one
process, and looked the registered line up in `ci/reproduce.json` by check name. For the jd reader's
own check (`thinkers-peirce-jd`) it required the registered line as an exact substring of the raw
line; for the others it required the registered Φ and core substrings.

```
### 1 dispatcher
registered (thinkers-peirce-jd): control                Φ_MIP=2.000000  core=('A', 'B', 'M')        jd=True  in_whole=True   M <- AB (φ=2.000)
raw read()  [0.28 s]: control                Φ_MIP=2.000000  core=('A', 'B', 'M')        jd=True  in_whole=True   M <- AB (φ=2.000)
helper      [0.27 s]:
Whole, Φ = 2.0
Core: A, B, M
Set by two others: M by A+B, inside the core
MATCH: True

### 2 manager listens in
registered (thinkers-simmel-h4-nonpartisan): mediator_eliminated    dyadic   Φ_MIP=0.000000  core=('A', 'B') coreΦ=2.000
raw read()  [0.12 s]: mediator_eliminated    Φ_MIP=0.000000  core=('A', 'B')             jd=False in_whole=False  none
helper      [0.11 s]:
Factors, Φ = 0.0
Core: A, B   (outside: M)
Set by two others: nobody
MATCH: True

### 3a committee, majority
registered (thinkers-peirce-jd): majority_triad         Φ_MIP=0.000000  core=()                     jd=True  in_whole=False  C <- AB (φ=0.500, tied)
raw read()  [0.42 s]: majority_triad         Φ_MIP=0.000000  core=()                     jd=True  in_whole=False  C <- AB (φ=0.500, tied)
helper      [0.36 s]:
Factors, Φ = 0.0
Core: none
Set by two others: C by A+B, no whole holds them (tied reading)
MATCH: True

### 3b committee, unanimity
registered (thinkers-simmel-h3-majority): unanimity_triad        triadic  Φ_MIP=6.000000  core=('A', 'B', 'C') coreΦ=6.000
raw read()  [0.44 s]: unanimity_triad        Φ_MIP=6.000000  core=('A', 'B', 'C')        jd=True  in_whole=True   A <- BC (φ=0.250), B <- AC (φ=0.250), C <- AB (φ=0.250)
helper      [0.48 s]:
Whole, Φ = 6.0
Core: A, B, C
Set by two others: A by B+C; B by A+C; C by A+B, inside the core
MATCH: True

### P clique_4 (practice)
registered (thinkers-simmel-h2-number): clique_4               triadic  Φ_MIP=12.000000
raw read()  [10.53 s]: clique_4               Φ_MIP=12.000000  core=('A', 'B', 'C', 'D')   jd=True  in_whole=True   A <- BCD (φ=0.250), B <- ACD (φ=0.250), C <- ABD (φ=0.250), D <- ABC (φ=0.250)
helper      [10.52 s]:
Whole, Φ = 12.0
Core: A, B, C, D
Set by several others: A by B+C+D; B by A+C+D; C by A+B+D; D by A+B+C, inside the core
MATCH: True

### 4 dealer, then direct sale
registered (q213): contingent  (car dealer)      : contingent margin=2.000  D in core: constrained=True bypass=False  (Phi 2.000 -> 0.000)
raw contingency_test [0.55 s]: contingent margin=2.000  D in core: constrained=True bypass=False  (Phi 2.000 -> 0.000)
raw read() on the dealer [0.81 s]: car_dealer             Φ_MIP=2.000000  core=('B', 'D', 'M')        jd=False in_whole=False  none
helper [1.18 s]:
Whole, Φ = 2.0  ->  B deals with M directly: Factors, Φ = 0.0
Core: B, D, M  ->  B, M
D: needed only while the direct deal is barred
MATCH: True
```

The clique_4 time (10.5 s) ran beside two long background jobs; alone it took 7.2 s.

The helper's bypass mode also classified q213's intrinsic case. Its registered line is
`intrinsic  margin=0.000  S in core: constrained=True bypass=True  (Phi 2.000 -> 2.000)`:

```
### 4' clearinghouse, direct line
  clearinghouse          Φ_MIP=2.000000  core=('C', 'S', 'W')        jd=True  in_whole=True   S <- WC (φ=2.000)
  intrinsic  margin=0.000  S in core: constrained=True bypass=True  (Phi 2.000 -> 2.000)
Whole, Φ = 2.0  ->  C deals with W directly: Whole, Φ = 2.0
Core: C, S, W  ->  S, W
S: still needed when they can deal directly
[0.45 s]
```

## 4. Command-line helper and fallback one-liners

```
$ python submissions/triadic_reduction/talk/live/show.py dispatcher AMB "x[1]" "x[0] & x[2]" "x[1]"
Whole, Φ = 2.0
Core: A, B, M
Set by two others: M by A+B, inside the core
real 1.81

$ python submissions/triadic_reduction/talk/live/show.py car_dealer MDB "x[2]" "x[0]" "x[1]" --bypass D B M
Whole, Φ = 2.0  ->  B deals with M directly: Factors, Φ = 0.0
Core: B, D, M  ->  B, M
D: needed only while the direct deal is barred
real 2.38

$ python -c 'from org_frontier.thinkers.peirce.probe_peirce_joint_determination import read; read("dispatcher", (("A","M","B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]))'
  dispatcher             Φ_MIP=2.000000  core=('A', 'B', 'M')        jd=True  in_whole=True   M <- AB (φ=2.000)
real 1.61
```

## 5. Fresh sentences

**"A platform that shows each driver's rating to the rider only after both accept."** Labels `DPR`
(driver, platform, rider). The sentence fixes the platform's rule, `P' = D & R`, and says nothing about
what the driver and rider respond to. Three readings:

```
### rating (a): both respond to what the platform shows          D'=P  P'=D&R  R'=P
Whole, Φ = 2.0
Core: D, P, R
Set by two others: P by D+R, inside the core
[0.17 s]

### rating (b): each keeps their own acceptance                  D'=D  P'=D&R  R'=R
Factors, Φ = 0.0
Core: none that binds two parties   (R only keeps its own state)
Set by two others: nobody
[0.07 s]

### rating (c): rider reacts to the rating, driver keeps own     D'=D  P'=D&R  R'=P
Factors, Φ = 0.0
Core: P, R   (outside: D)
Set by two others: P by D+R, no whole holds them
[0.08 s]
```

Reading (a) is the dispatcher form under new letters. Reading (b) first printed `Core: R`, a self-copying
node counted as a complex of one; `show.py` now names that case in words. The lesson for the runbook:
the verdict turns on what each party responds to, so ask, or show two readings.

**"Four suppliers bidding through one auctioneer."** Labels `ABCDU`; each supplier bids on the
auctioneer's call (`x[4]`), and the auctioneer calls on any bid or on two.

```
### auction n=5, any bid          A..D' = U   U' = A|B|C|D
  auction_any            Φ_MIP=4.000000  core=('A', 'B', 'C', 'D', 'U') jd=True  in_whole=True   U <- ABCD (φ=4.000)
Whole, Φ = 4.0
Core: A, B, C, D, U
Set by several others: U by A+B+C+D, inside the core
[9.17 s]

### auction n=5, two bids         A..D' = U   U' = sum(A..D) >= 2
  auction_two            Φ_MIP=0.000000  core=()                     jd=True  in_whole=False  U <- AB (φ=0.758)
Factors, Φ = 0.0
Core: none
Set by two others: U by A+B, no whole holds them
[2.09 s]
```

None of these numbers is registered. They show only that the recipe runs end to end.

## 6. Size ceiling

Every call is `show(..., raw=True)` in one process, beside other jobs.

```
### clique_5          each party: all(x[j] for j in range(5) if j != i)
  clique_5               Φ_MIP=20.000000  core=('A', 'B', 'C', 'D', 'E') jd=True  in_whole=True   A <- BCDE (φ=0.125), B <- ACDE (φ=0.125), C <- ABDE (φ=0.125), D <- ABCE (φ=0.125), E <- ABCD (φ=0.125)
Whole, Φ = 20.0
Core: A, B, C, D, E
Set by several others: A by B+C+D+E; B by A+C+D+E; C by A+B+D+E; D by A+B+C+E; E by A+B+C+D, inside the core
[569.51 s]
real 571.25
```

The Φ matches the registered `clique_5 … Φ_MIP=20.000000` (thinkers-simmel-h2-number).

```
### auction n=6, any bid     A..E' = U   U' = A|B|C|D|E      (show, full read)
stopped by hand after 15:04 elapsed, no output

$ python -c '... verdict(rules, labels) ... major_complex(rules, labels) ...'   (the same form, Φ and core only)
verdict Φ_MIP=5.000000  [28.91 s]
major_complex core=('A', 'B', 'C', 'D', 'E', 'U') coreΦ=5.000  [26.59 s]
```

| form | nodes | wiring | compute |
| --- | --- | --- | --- |
| rehearsed forms | 3 | any | 0.07–1.2 s |
| clique_4 | 4 | everyone reads everyone | 7.2 s alone, 10.5 s under load |
| auction, any bid | 5 | star: one party reads four | 9.2 s |
| auction, two bids | 5 | star | 2.1 s |
| clique_5 | 5 | everyone reads everyone | 569.5 s |
| auction, any bid | 6 | star | Φ and core 55.5 s; full read over 15 min |

In the six-node run the joint-determination reader took more than 14 of the 15 minutes: it re-scores
every cause purview of every one-element mechanism at every reachable state. Density costs more than
size, since the five-node star finished in 9 s and the five-node clique took 9.5 minutes.

## 7. Fixes made to show.py during rehearsal

- `Set by two others` misdescribed clique_4, whose members are each set by three; the label now reads
  `Set by several others` when any purview holds more than two.
- The first draft tagged every jointly determined member with one any-member test, so a mixed form
  (some members inside the core, some not) would read all one way. `show.py` now tags each member with
  read()'s own in-whole condition.
- A self-copying node printed as a one-member core; it now prints as "keeps its own state".
- String rules with a generator (`all(x[j] for j in range(5) if j != i)`) failed: `range` was not
  allowed, and `x` was invisible inside the generator. Both fixed; clique_5 then ran.
