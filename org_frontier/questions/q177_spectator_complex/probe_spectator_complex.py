"""q177 — Does an idle spectator sink whole-system Φ while the major complex keeps the triadic core?

QUESTION
    A coded account of a coordination may name a party who reads nobody and whom nobody reads — an
    idle spectator (a bystander, an inactive seat on an org chart, a logged-but-disconnected role).
    Adding such a party to the model drives whole-system Φ to zero, because the system no longer
    integrates as a whole: the spectator factors off. The question is whether the major complex —
    the maximal irreducible subsystem PyPhi finds — still returns the original triadic core, and
    whether a core-aware verdict (read off the major complex) survives the spectator where the
    whole-system verdict does not.

H1  Adding a genuinely idle spectator (reads nobody, nobody reads it) leaves the original triadic
    core (W,S,C) as the major complex, at the same Φ, in more than 95% of synthetic triadic-core
    accounts.
    NULL: the spectator changes the major complex's membership or its Φ on at least one account, so
    it is not inert to the core.

H2  The core-aware verdict (irreducible core present in the major complex) agrees with the
    no-spectator verdict in 100% of (account, spectator) cases, whereas the whole-system verdict
    disagrees in more than 50%.
    NULL: the core-aware verdict flips on at least one case, so reading the complex does not
    immunize the verdict against spectators.

METHOD
    Synthetic coded accounts are three-party coordination forms: the mediator S binds W and C
    through a two-input Boolean gate, with W and C each reading S (directly or negated). Sweeping
    six gates and the four feedback signs yields 24 accounts. A genuinely idle spectator X is
    injected as a fourth node whose rule reads nobody (constant 0 or constant 1) and whom no other
    rule reads. For each (account, spectator) pair the probe records the whole-system verdict
    (classifier Φ over the MIP) and the major complex (PyPhi maximal_complex over reachable
    states), with and without the spectator. CONTROL = the no-spectator baseline (whole-system
    equals core) plus two wired-in distinguishers: an active party that reads S and is read by S,
    which must enter the core; and a self-loop "spectator" that reads only itself, which carries
    its own irreducible self-Φ and so is not idle.

    All inputs are synthetic coded rule sets, not measured worker states. Exact Φ is reused from the
    classifier and probes.lib; it is not reimplemented here.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q177_spectator_complex.probe_spectator_complex
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "yes")

import numpy as np

from org_frontier.field.rule_to_phi import rule_to_phi
from org_frontier.probes.lib import verdict, major_complex

PHI_EPS = 1e-9
L3 = ("W", "S", "C")
L4 = ("W", "S", "C", "X")
CORE = ("W", "S", "C")


# --------------------------------------------------------------------------------------
# Synthetic account population
# --------------------------------------------------------------------------------------

GATES = {
    "AND":  lambda a, c: a & c,
    "OR":   lambda a, c: a | c,
    "XOR":  lambda a, c: a ^ c,
    "NAND": lambda a, c: 1 - (a & c),
    "NOR":  lambda a, c: 1 - (a | c),
    "XNOR": lambda a, c: 1 - (a ^ c),
}
FEEDBACK = {"id": lambda s: s, "not": lambda s: 1 - s}

# Genuinely idle spectators: read nobody (constant), and no other rule reads them.
IDLE_SPECTATORS = {"const0": lambda x: 0, "const1": lambda x: 1}


def base_form(g, wf, cf):
    """Three-party account: W reads S (signed), S binds (W,C) through gate g, C reads S (signed)."""
    return [
        lambda x, wf=wf: wf(x[1]),
        lambda x, g=g: g(x[0], x[2]),
        lambda x, cf=cf: cf(x[1]),
    ]


def synthetic_accounts():
    out = []
    for gname, g in GATES.items():
        for wname, wf in FEEDBACK.items():
            for cname, cf in FEEDBACK.items():
                out.append((f"{gname}/{wname}/{cname}", base_form(g, wf, cf)))
    return out


# --------------------------------------------------------------------------------------
# Instrument control
# --------------------------------------------------------------------------------------

def instrument_control():
    """Validate the machinery on known cases before computing the real result."""
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = rule_to_phi(triad, L3)
    mc = major_complex(triad, L3)
    assert v["structure"] == "triadic" and abs(v["max_phi"] - 2.0) < 1e-9, v
    assert mc[0] == CORE and abs(mc[1] - 2.0) < 1e-9, mc

    # Idle spectator on the faithful triad: whole-system Φ -> 0, core intact at 2.0.
    sp = triad + [IDLE_SPECTATORS["const0"]]
    vs = rule_to_phi(sp, L4)
    mcs = major_complex(sp, L4)
    assert abs(vs["max_phi"]) < 1e-9 and vs["structure"] == "dyadic", vs
    assert mcs[0] == CORE and abs(mcs[1] - 2.0) < 1e-9, mcs

    # Active party: X reads S and S reads X — X must enter the core.
    active = [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]]
    mca = major_complex(active, L4)
    assert mca[0] == ("W", "S", "C", "X"), mca

    # Self-loop node: reads only itself, carries its own irreducible Φ — NOT idle.
    selfloop = triad + [lambda x: x[3]]
    mcl = major_complex(selfloop, L4)
    assert mcl[0] == CORE and abs(mcl[1] - 2.0) < 1e-9, mcl  # strong core survives self-loop

    print("CONTROL faithful triad reads triadic max_phi=2.0; idle spectator sinks whole-system "
          "to 0 with core (W,S,C)=2.0 intact; active party enters core; self-loop not idle: PASS")


# --------------------------------------------------------------------------------------
# Main study
# --------------------------------------------------------------------------------------

def run():
    instrument_control()
    np.random.default_rng(0)  # fixed seed; the sweep is exhaustive and deterministic

    accounts = synthetic_accounts()

    rows = []
    n_pairs = 0
    whole_disagree = 0
    core_disagree = 0
    n_triadic = 0
    core_stable = 0

    for name, form in accounts:
        v0 = verdict(form, L3)
        mc0 = major_complex(form, L3)
        base_triadic_core = (mc0[0] == CORE and mc0[1] > PHI_EPS)
        for sname, sp in IDLE_SPECTATORS.items():
            spf = form + [sp]
            vw = verdict(spf, L4)
            mcw = major_complex(spf, L4)
            n_pairs += 1

            whole_same = (vw.structure == v0.structure)
            if not whole_same:
                whole_disagree += 1

            core_present_base = mc0[1] > PHI_EPS
            core_present_sp = mcw[1] > PHI_EPS
            if core_present_sp != core_present_base:
                core_disagree += 1

            stable = (mcw[0] == mc0[0] and abs(mcw[1] - mc0[1]) < PHI_EPS)
            if base_triadic_core:
                n_triadic += 1
                if mcw[0] == CORE and abs(mcw[1] - mc0[1]) < PHI_EPS:
                    core_stable += 1

            rows.append((name, sname, v0.structure, round(v0.max_phi, 3),
                         vw.structure, round(vw.max_phi, 3),
                         "".join(mc0[0]), round(mc0[1], 3),
                         "".join(mcw[0]), round(mcw[1], 3),
                         "yes" if stable else "no"))

    # ---- table -------------------------------------------------------------------
    print()
    print("Per-account whole-system verdict vs major complex, with idle spectator injected")
    print(f"{'account':<13} {'spec':<7} {'base':<8} {'bΦ':>5}  {'+spec':<8} {'sΦ':>5}  "
          f"{'core0':<5} {'Φ0':>5}  {'core+sp':<7} {'Φsp':>5}  {'stable':<6}")
    print("-" * 92)
    for r in rows:
        print(f"{r[0]:<13} {r[1]:<7} {r[2]:<8} {r[3]:>5.3f}  {r[4]:<8} {r[5]:>5.3f}  "
              f"{r[6]:<5} {r[7]:>5.3f}  {r[8]:<7} {r[9]:>5.3f}  {r[10]:<6}")

    # ---- summary -----------------------------------------------------------------
    h1_frac = core_stable / n_triadic if n_triadic else float("nan")
    h2_whole = whole_disagree / n_pairs if n_pairs else float("nan")
    h2_core = core_disagree / n_pairs if n_pairs else float("nan")

    print()
    print("Summary")
    print(f"  (account, spectator) pairs            : {n_pairs}")
    print(f"  triadic-core accounts (over pairs)    : {n_triadic}")
    print(f"  core stable (orig W,S,C core, same Φ) : {core_stable}/{n_triadic} = {h1_frac:.3f}")
    print(f"  whole-system verdict disagrees        : {whole_disagree}/{n_pairs} = {h2_whole:.3f}")
    print(f"  core-aware verdict disagrees          : {core_disagree}/{n_pairs} = {h2_core:.3f}")

    # ---- verdicts ----------------------------------------------------------------
    h1_ok = (n_triadic > 0) and (h1_frac > 0.95)
    h2_ok = (h2_core == 0.0) and (h2_whole > 0.50)

    print()
    print(f"H1 (idle spectator leaves the triadic core intact in >95% of accounts): "
          f"{'SUPPORTED' if h1_ok else 'REFUTED'} "
          f"(core stable in {h1_frac:.3f} of triadic-core accounts)")
    print(f"H2 (core-aware verdict agrees in 100%, whole-system disagrees in >50%): "
          f"{'SUPPORTED' if h2_ok else 'REFUTED'} "
          f"(core-aware disagree {h2_core:.3f}; whole-system disagree {h2_whole:.3f})")


if __name__ == "__main__":
    run()
