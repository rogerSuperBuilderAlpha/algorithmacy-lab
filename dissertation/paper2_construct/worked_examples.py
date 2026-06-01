"""Paper 2 worked examples: the dyadic limit vs the irreducible triad.

Each coordination form is rendered as a 3-node application-layer system (Worker, System,
Counterpart) under the pre-registered state-individuation rule. The TPMs are derived from
each case's ACTUAL coupling structure — who-depends-on-whom — not chosen for a target Φ.
We compute exact IIT-4.0 Φ and report whatever results.

  A. Chat with a language model (dyadic limit): two parties only; the model commits nothing
     that couples a third. Counterpart decoupled  ->  expect the form to factor (Φ_triad = 0).

  B. Résumé -> applicant-tracking-system -> hiring manager (irreducible triad): the parties
     reach each other ONLY through the system's committed determination. Mediator topology
     W<->S<->C, no direct W-C edge. Irreducibility is the open question -> compute it.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/worked_examples.py
"""

from phi_instrument import (
    tpm_from_rules, cm_from_rules, system_phi_over_states, sia_report, NODE_LABELS,
)
import numpy as np


# --------------------------------------------------------------------------------------
# A. Dyadic limit: chat with a language model
# --------------------------------------------------------------------------------------
def chat_dyad():
    """W and S form a real two-party loop (the worker prompts, the model answers, the worker
    responds to the answer); there is no third human party, so C is unconstituted/decoupled.
        W' = S,  S' = W,  C' = C.
    The model commits determinations, but none alters its causal disposition toward a C."""
    rules = [
        lambda x: x[1],   # W' = S   (worker's next move tracks the model's last answer)
        lambda x: x[0],   # S' = W   (model's answer tracks the worker's prompt)
        lambda x: x[2],   # C' = C   (no third party)
    ]
    return tpm_from_rules(rules), cm_from_rules(rules)


# --------------------------------------------------------------------------------------
# B. Irreducible triad: résumé -> ATS -> hiring manager
#    Derived purely from the case's coupling, respecting the mediator topology
#    (W<->S<->C, NO direct W-C edge — the parties never meet except through the system).
# --------------------------------------------------------------------------------------
def ats_triad_mediator():
    """Strict mediator topology.
        S' = W AND C : the ATS commits 'forward' iff the résumé carries the match-signal (W)
                       AND the manager's configured keyword profile is active (C).
        W' = S       : the applicant's live-candidate state tracks the ATS determination.
        C' = S       : the manager learns of the applicant only through what the ATS forwards.
    No direct W-C edge. Is a pure bottleneck irreducible? Compute."""
    rules = [
        lambda x: x[1],            # W' = S
        lambda x: x[0] & x[2],     # S' = W AND C
        lambda x: x[1],            # C' = S
    ]
    return tpm_from_rules(rules), cm_from_rules(rules)


def ats_triad_feedback():
    """Mediator topology with the realistic feedback the case actually has: the applicant
    revises against the determination, the manager re-tunes the profile against what the
    system surfaced, and the system re-commits against both — all THROUGH S (no W-C edge).
        S' = W AND C : forward iff match-signal present and profile active.
        W' = NOT S   : the applicant revises (changes her résumé signal) when NOT forwarded,
                       and stops revising once through — her action is a response to S.
        C' = S OR C  : the manager's interest is set by what was forwarded and persists.
    Still strict mediator topology (W and C each couple only to S)."""
    rules = [
        lambda x: 1 - x[1],            # W' = NOT S
        lambda x: x[0] & x[2],         # S' = W AND C
        lambda x: x[1] | x[2],         # C' = S OR C
    ]
    return tpm_from_rules(rules), cm_from_rules(rules)


# --------------------------------------------------------------------------------------
# C. The false dyad: rideshare driver -> platform -> rider
#    PRESENTS as a driver<->app two-party relationship — the driver only ever touches the
#    app and can neither see nor choose the rider — yet the rider is causally constitutive
#    of the platform's dispatch determination. Strict mediator topology (no direct W-C edge).
#    The whole dyad/triad verdict turns on ONE dependency: whether the dispatch reads C.
# --------------------------------------------------------------------------------------
def gig_false_dyad():
    """Rideshare with the rider constitutive of the determination.
        W' = NOT S        : the driver's availability is consumed by a dispatch, returns otherwise.
        S' = W AND C      : the platform dispatches iff a driver is available AND a rider is
                            waiting — the determination reads BOTH sides.
        C' = C AND NOT S  : the rider keeps waiting until a dispatch serves the request.
    The driver and rider never directly interact (no W-C edge); the driver experiences only
    the app. Is the structure she cannot see irreducible? Compute."""
    rules = [
        lambda x: 1 - x[1],            # W' = NOT S
        lambda x: x[0] & x[2],         # S' = W AND C
        lambda x: x[2] & (1 - x[1]),   # C' = C AND NOT S
    ]
    return tpm_from_rules(rules), cm_from_rules(rules)


def gig_dyadic_model():
    """The SAME situation as a dyadic construct models it: the analyst sees only the visible
    driver<->app channel and treats the (invisible) rider as non-constitutive, so the dispatch
    is read as a function of the driver alone.
        W' = NOT S        : unchanged.
        S' = W            : dispatch tracks the driver only — the rider is dropped from the
                            determination (the one edge the dyadic model omits).
        C' = C AND NOT S  : the rider is still on the interface, but reads nothing into S.
    Exactly one dependency removed (S no longer reads C). Recompute the verdict."""
    rules = [
        lambda x: 1 - x[1],            # W' = NOT S
        lambda x: x[0],                # S' = W   (rider not constitutive)
        lambda x: x[2] & (1 - x[1]),   # C' = C AND NOT S
    ]
    return tpm_from_rules(rules), cm_from_rules(rules)


def report(name, builder, expect):
    tpm, cm = builder()
    print(f"\n### {name}")
    print(f"connectivity (rows=from, cols=to; W,S,C):\n{cm}")
    results = system_phi_over_states(tpm, cm)
    if not results:
        print("  no reachable evaluable states")
        return None
    phis = [p for _, p in results]
    for state, phi in results:
        print(f"    state {state} -> Φ = {phi:.6f}")
    print(f"  reachable evaluated: {len(results)}   mean Φ = {np.mean(phis):.6f}   "
          f"max Φ = {np.max(phis):.6f}   (expected {expect})")
    best = max(results, key=lambda r: r[1])
    s = sia_report(tpm, cm, best[0])
    print(f"  sia at max-Φ state {best[0]}: Φ = {float(s.phi):.6f}")
    try:
        print(f"    minimum-information partition: {s.partition}")
    except Exception as e:
        print(f"    (partition repr unavailable: {e})")
    return float(np.max(phis))


if __name__ == "__main__":
    print("=" * 78)
    print("PAPER 2 — worked application: dyadic limit vs irreducible triad")
    print("=" * 78)
    a = report("A. Chat with a language model (dyadic limit)", chat_dyad, "Φ ≈ 0")
    b1 = report("B1. Résumé -> ATS -> hiring manager (strict bottleneck)", ats_triad_mediator, "Φ ?")
    b2 = report("B2. Résumé -> ATS -> hiring manager (with feedback)", ats_triad_feedback, "Φ ?")
    c1 = report("C1. Rideshare driver–app–rider (rider constitutive: the FALSE DYAD)", gig_false_dyad, "Φ ?")
    c2 = report("C2. Same case, dyadic model (rider dropped from determination)", gig_dyadic_model, "Φ ≈ 0")
    print("\n" + "=" * 78)
    print(f"CONTRAST:  dyad Φ = {a:.4f}   |   triad(bottleneck) Φ = {b1:.4f}   |   "
          f"triad(feedback) Φ = {b2:.4f}")
    print(f"FALSE DYAD:  full triad (rider constitutive) Φ = {c1:.4f}   |   "
          f"dyadic model (rider dropped) Φ = {c2:.4f}")
    print("  -> the dyad/triad verdict turns on the single edge S'<-C (does the determination read the unseen third party)")
    print("=" * 78)
