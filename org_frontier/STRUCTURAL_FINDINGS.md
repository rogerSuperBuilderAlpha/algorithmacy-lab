# Structural findings: what makes a coordination form irreducible

A synthesis of the org_frontier experiments. Each claim is computed with exact IIT-4.0 Φ via PyPhi,
on systems small enough to compute it exactly, and is reproducible from the named module. The
verdict throughout is Φ over the minimum-information partition: Φ_MIP = 0 means the form factors
(dyadic, demands only literacy); Φ_MIP > 0 means it does not (triadic, demands algorithmacy).

These are domain-neutral structural results about small mediated systems. The organizational reading
is in [`essays/literacy_or_algorithmacy.md`](essays/literacy_or_algorithmacy.md) and
[`COMMUNITY_NOTE.md`](COMMUNITY_NOTE.md).

## The eight findings

1. **The surface does not decide the verdict.** Party count and interface underdetermine it. A
   three-party arrangement can factor to a dyad; a worker alone with an app can be triadic.
   (`classifier/`)

2. **Topology does not decide it either.** Strict mediation — no direct edge between the outer
   parties — is necessary but not sufficient. In the complete 256-form strict-mediation n=3 family,
   only **9.4%** are triadic; 90.6% still factor. (`corpus/population.py`)

3. **Irreducibility needs two things together.** The mediator must read all parties (necessary:
   0% triadic without it), and the parties' own reads must keep each of them live to the mediator's
   commit. Neither alone suffices — a form with strict mediation and a both-reading mediator still
   factors if the downstream reads break liveness (P(triadic | mediator reads both) = 15.0% at n=3).
   (`corpus/`, `corpus/population.py`)

4. **Parity determinations support irreducibility most readily.** Among the two-input mediator
   functions, XOR and XNOR each yield 4/16 triadic forms, twice the 2/16 of monotone functions
   (AND, OR, NAND, NOR). One-input and constant functions yield none. (`corpus/determination.py`)

5. **Substitutability collapses irreducibility — for any role.** With multiple counterparts, the
   form is triadic only if the determination binds them all jointly (all-required, e.g. W ∧ C1 ∧ C2,
   Φ = 3.0); a substitutable (W ∧ (C1 ∨ C2)) or optional counterpart factors it. The same holds when
   the *mediator* is substitutable: a worker multi-homing across two platforms where either suffices
   factors (dyadic), while requiring both stays triadic. Interchangeability of any role — counterpart
   or platform — collapses the triad. (`multiparty/`)

6. **Breadth dilutes, depth preserves.** Adding parties makes irreducibility rarer, to vanishing:
   the random strict-mediation triadic rate falls **9.4% (n=3) → 2.3% (n=4) → 0% (n=5)**, confirmed
   genuine by noise robustness checks (not a reachability artifact). Adding mediation depth does the
   opposite: a chain W → S1 → ... → Sk → C stays triadic with **Φ = 2.0 at every length** (n=3-6),
   cut at a single balanced partition. Depth does not rescue substitutability, and breadth does not
   undo depth — the two act independently. (`multiparty/scaling.py`, `multiparty/chains.py`)

7. **Cheap proxies cannot recover the verdict.** A ΦID or whole-minus-sum proxy estimated from a
   form's time series separates dyadic from triadic only near chance (rank-AUC ≤ 0.63). It confuses
   statistical dependence with integration — a dyadic form with a back-channel scores highest. The
   route past the exact-Φ size ceiling does not hold for this verdict; the exact computation is
   needed, and is feasible because coordination units are small. (`proxy_bridge/`)

8. **Ownership is not constitutive; bidirectional participation is.** A corporate principal who
   authors the mediator joins the irreducible core (the major complex) **iff the coupling is
   bidirectional** — S reads P (gating) and P reads at least one party (a 16-form sweep pins this
   exactly). Owning the system, gating-only, or monitoring-only leaves the principal outside; the
   core stays the worker–system–counterpart triad. A heavily-coupled principal can even *contract*
   the core to {S, P}, displacing the worker and counterpart it ostensibly coordinates. This finding
   needs the major complex, not whole-system Φ: an idle principal makes the whole system factor while
   the triad inside stays irreducible. (`principal/`)

## The law they reduce to

A coordination form is triadic — it demands algorithmacy — **if and only if every party is bound
into a single irreducible joint determination.** Substitutability or optionality of any party
collapses it to dyadic. Mediation depth never does. The number of parties is not the variable; the
irreducibility of the joint determination is. Random coupling meets this condition ever more rarely
as parties multiply, but specific structures (an all-binding conjunction, a non-factoring chain,
a parity determination) meet it at any size.

## A validated account of core membership (the probe loop)

The `probes/` hypothesis loop (see `probes/PROBES.md`) ran eleven hypothesis → PyPhi-test cycles on
the construct's dimensions and scope conditions, and converged on a two-condition, quantitatively
validated account of *which parties are bound into the irreducible coordination*:

- **Bidirectional constraining coupling** (necessary): a party must both feed and be fed by the
  coordination; emit-only sources and read-only sinks stay out.
- **Pivotality** (graded, validated): given coupling, the probability a party is in the major complex
  rises monotonically with the determination's Boolean sensitivity to it — zero influence excludes,
  influence ≥ 0.75 guarantees inclusion (rank-AUC 0.89 over 256 determinations).

Notable probe results: a counterpart coalition can eject the worker; a worker's internal model of
the counterpart *substitutes for* the real counterpart in the core (they never coexist); a switching
rule does not bind the regime (temporal-tracking is a worker burden, not structural); majority/
redundant determinations factor entirely. The worker-competency dimensions correctly show up as not
structural; the structural scope conditions do.

## What this contributes

For the PyPhi community: a new application class (small mediated/coordination systems), a curated
labeled corpus, a reusable classifier, and clean minimal test cases where a single edge, read
function, or party toggles Φ. For organization theory: a computable criterion for when a coordination
form demands a new competency, with the structural conditions that produce it made precise.

## Reproduce

```bash
~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.validate
~/iit-playground/venv-4.0/bin/python -m org_frontier.corpus.build
~/iit-playground/venv-4.0/bin/python -m org_frontier.corpus.population
~/iit-playground/venv-4.0/bin/python -m org_frontier.corpus.determination
~/iit-playground/venv-4.0/bin/python -m org_frontier.multiparty.run
~/iit-playground/venv-4.0/bin/python -m org_frontier.multiparty.chains 4
~/iit-playground/venv-4.0/bin/python -m org_frontier.multiparty.scaling 5 400 7
~/iit-playground/venv-4.0/bin/python -m org_frontier.proxy_bridge.run
~/iit-playground/venv-4.0/bin/python -m org_frontier.principal.run
```
