"""Prior exploration for the neonatal-third study: the constitutive triad under exact Phi.

The study reads the NICU bedside against the lab's coordination catalog. Before any fieldwork,
the catalog's instruments already say something about the proposed structure. This script runs
four probes that turn the study's verbal claims into measured rates over random Boolean forms,
each built from a harness already on main, so the numbers are reproducible and tied to a thread.

The wiring uses four roles. P is the parent, S is the apparatus-and-nurse (the committing
tertius), T is the care team, I is the infant. An edge a<-b means a reads b's state.

Run from the repo root with the IIT-4.0 interpreter:
    PYTHONPATH=. PYPHI_WELCOME_OFF=true python org_frontier/qualitative/neonatal_third/iit_probes.py

Findings (400 forms, seed 11), held in PRIOR_ANALYSIS.md:
  PROBE 1  committing triad P-S-T binds 10%; S is a veto player in 159/159 integrating coalitions.
  PROBE 2  realistic 4-node NICU binds 6%; S veto 214/214; S always in the core; infant in 17%.
  PROBE 3  a pure observer (in-only) is never in the core (0%); a read emitter is in it 34%.
  PROBE 4  a symmetric parent-team back-channel drops S's veto from 100% to 45% (disintermediation);
           no such channel can exist to the infant, so the referent side stays constitutive.
"""

import random

from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set
from org_frontier.threads.coalition_structure._harness import network, complex_over_states
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.classifier.classifier import classify_rules

FORMS = 400
SEED = 11


def build(arch, n, rng):
    """A random Boolean form on n nodes with the given read-wiring (node -> list of inputs)."""
    r = [None] * n
    for node, ins in arch.items():
        if len(ins) == 1:
            r[node] = _rule_of_one(rng.randint(0, 3), ins[0])
        else:
            r[node] = _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(ins))], ins)
    return r


def probe1():
    print(f"PROBE 1 - committing triad P(0)-S(1)-T(2), strict star, {FORMS} forms seed {SEED}")
    arch = {0: [1], 1: [0, 2], 2: [1]}            # P<-S ; S<-P,T ; T<-S
    rng = random.Random(SEED)
    labels = tuple("PST")
    tri = integ = sveto = 0
    for _ in range(FORMS):
        rules = build(arch, 3, rng)
        if classify_rules(rules, labels).structure == "triadic":
            tri += 1
        net, tpm = network(rules, labels)
        W = integrating_coalitions(net, tpm, 3)
        if W:
            integ += 1
            if 1 in veto_set(W):
                sveto += 1
    print(f"  triadic(commits) {tri}/{FORMS} = {100*tri/FORMS:.0f}%   "
          f"S(apparatus) veto | integrating {sveto}/{integ}")


def probe2():
    print(f"PROBE 2 - realistic NICU P(0) S(1) T(2) I(3): I<-T, S<-P,T,I, P<-S, T<-S, {FORMS} forms seed {SEED}")
    arch = {0: [1], 1: [0, 2, 3], 2: [1], 3: [2]}
    rng = random.Random(SEED)
    labels = tuple("PSTI")
    usable = Iin = integ = sveto = Sin = 0
    for _ in range(FORMS):
        rules = build(arch, 4, rng)
        net, tpm = network(rules, labels)
        W = integrating_coalitions(net, tpm, 4)
        if W:
            integ += 1
            if 1 in veto_set(W):
                sveto += 1
        _, core, _ = complex_over_states(net, tpm, 4)
        if core is not None:
            usable += 1
            if 1 in core:
                Sin += 1
            if 3 in core:
                Iin += 1
    print(f"  triadic S(apparatus) veto | integrating {sveto}/{integ}   "
          f"S in core {Sin}/{usable}   I(infant) in core {Iin}/{usable} = {100*Iin/max(usable,1):.0f}%")


def probe3():
    print(f"PROBE 3 - membership duality of a half-coupled fourth node, {FORMS} forms seed {SEED}")
    for name, arch in [
        ("X in-only  (pure observer: reads S, is read by no one)", {0: [1], 1: [0, 2], 2: [1], 3: [1]}),
        ("X out-only (read emitter: read by S, self-driven)     ", {0: [1], 1: [0, 2, 3], 2: [1], 3: [3]}),
    ]:
        rng = random.Random(SEED)
        labels = tuple("PSTX")
        usable = Xin = 0
        for _ in range(FORMS):
            rules = build(arch, 4, rng)
            net, tpm = network(rules, labels)
            _, core, _ = complex_over_states(net, tpm, 4)
            if core is not None:
                usable += 1
                if 3 in core:
                    Xin += 1
        print(f"  {name}: X in major complex {Xin}/{usable} = {100*Xin/max(usable,1):.0f}%")


def probe4():
    print(f"PROBE 4 - disintermediation: a parent-team back-channel against S's veto, {FORMS} forms seed {SEED}")
    labels = tuple("PST")
    for name, arch in [
        ("no back-channel (committing triad)", {0: [1], 1: [0, 2], 2: [1]}),
        ("one-way P->T                      ", {0: [1], 1: [0, 2], 2: [1, 0]}),
        ("symmetric P<->T back-channel      ", {0: [1, 2], 1: [0, 2], 2: [1, 0]}),
    ]:
        rng = random.Random(SEED)
        integ = sveto = 0
        for _ in range(FORMS):
            rules = build(arch, 3, rng)
            net, tpm = network(rules, labels)
            W = integrating_coalitions(net, tpm, 3)
            if W:
                integ += 1
                if 1 in veto_set(W):
                    sveto += 1
        print(f"  {name}: S(apparatus) veto | integrating {sveto}/{integ} = {100*sveto/max(integ,1):.0f}%")
    print("  No symmetric channel to the infant can exist, so the referent side stays constitutive.")


if __name__ == "__main__":
    probe1()
    probe2()
    probe3()
    probe4()
