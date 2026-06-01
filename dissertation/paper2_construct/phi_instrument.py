"""Paper 2 instrument: exact IIT-4.0 Φ over an application-layer coordination form.

A coordination form is modelled as a 3-node system — Worker (W), System/mediator (S),
Counterpart (C) — whose application-layer transition matrix encodes how each party's next
state depends on the current states of all three. Φ (via IIT-4.0 `sia`) measures whether
that cause-effect structure is irreducible to its parts. "Triadic" = the structure does not
factor along party lines; "dyadic" = it does.

This module wraps the repo's exact-Φ oracle (`proxy_audit.exact_phi`) and runs the
validation controls the paper requires BEFORE any worked example:
  - a factoring form (C causally decoupled) must give system Φ ≈ 0 / a complex that excludes C;
  - a known-irreducible coupling must give Φ > 0 over the full W–S–C system.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/phi_instrument.py
"""

import os
import sys

# Repo root on the path so the sibling `proxy_audit` package imports.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import new_big_phi

from proxy_audit.exact_phi import exact_big_phi, reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

NODE_LABELS = ("W", "S", "C")  # worker, system/mediator, counterpart


# --------------------------------------------------------------------------------------
# Building application-layer transition matrices
# --------------------------------------------------------------------------------------

def tpm_from_rules(rules, n=3):
    """Build a deterministic state-by-node TPM of shape (2^n, n) from per-node Boolean
    rules. ``rules[j]`` is a function mapping the current node-state tuple (little-endian:
    index 0 = W) to node j's next value in {0,1}. PyPhi convention is little-endian state
    indexing, matching `proxy_audit.exact_phi`.
    """
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        cur = tuple((s >> i) & 1 for i in range(n))
        for j in range(n):
            tpm[s, j] = float(rules[j](cur))
    return tpm


def cm_from_rules(rules, n=3):
    """Infer the connectivity matrix: cm[i, j] = 1 iff node j's rule actually depends on
    node i (flip-test over all states)."""
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            depends = False
            for s in range(2 ** n):
                cur = list((s >> k) & 1 for k in range(n))
                flipped = cur.copy()
                flipped[i] ^= 1
                if rules[j](tuple(cur)) != rules[j](tuple(flipped)):
                    depends = True
                    break
            cm[i, j] = 1 if depends else 0
    return cm


# --------------------------------------------------------------------------------------
# The two validation controls
# --------------------------------------------------------------------------------------

def irreducible_control():
    """Canonical integrated 3-node network (the standard PyPhi example):
        W' = S OR C,  S' = W AND C,  C' = W XOR S.
    Every node depends on the other two; the cause-effect structure does not factor."""
    rules = [
        lambda x: x[1] | x[2],   # W' = S OR C
        lambda x: x[0] & x[2],   # S' = W AND C
        lambda x: x[0] ^ x[1],   # C' = W XOR S
    ]
    return tpm_from_rules(rules), cm_from_rules(rules)


def factoring_control():
    """A form that factors along party lines: the worker and mediator are coupled, but the
    counterpart is causally decoupled (C copies itself; nothing reads or writes C).
        W' = S,  S' = W,  C' = C.
    The system splits into {W,S} ⊗ {C}; the W–S–C partition reduces it."""
    rules = [
        lambda x: x[1],   # W' = S
        lambda x: x[0],   # S' = W
        lambda x: x[2],   # C' = C   (independent)
    ]
    return tpm_from_rules(rules), cm_from_rules(rules)


# --------------------------------------------------------------------------------------
# Φ over reachable states
# --------------------------------------------------------------------------------------

def system_phi_over_states(tpm_sbn, cm, n=3):
    """Exact IIT-4.0 system Φ for each reachable state. Returns list of (state, phi)."""
    out = []
    for s in reachable_states(tpm_sbn, n):
        state = tuple((s >> i) & 1 for i in range(n))
        phi = exact_big_phi(tpm_sbn, cm, state)
        if phi is not None:
            out.append((state, phi))
    return out


def sia_report(tpm_sbn, cm, state):
    """Full system irreducibility analysis for one state: returns the IIT-4.0 sia object,
    exposing Φ, the minimum-information partition, and the complex's node set."""
    network = pyphi.Network(tpm_sbn, cm=cm, node_labels=NODE_LABELS)
    subsystem = pyphi.Subsystem(network, tuple(state))
    return new_big_phi.sia(subsystem)


def _run_controls():
    print("=" * 78)
    print("PAPER 2 INSTRUMENT — validation controls (compute, don't assert)")
    print("=" * 78)
    for name, builder, expect in [
        ("FACTORING control  (W'=S, S'=W, C'=C; C decoupled)", factoring_control, "Φ ≈ 0"),
        ("IRREDUCIBLE control (W'=S|C, S'=W&C, C'=W^S)", irreducible_control, "Φ > 0"),
    ]:
        tpm, cm = builder()
        print(f"\n### {name}")
        print(f"connectivity matrix (rows=from, cols=to; order W,S,C):\n{cm}")
        results = system_phi_over_states(tpm, cm)
        if not results:
            print("  no reachable states evaluable")
            continue
        phis = [p for _, p in results]
        print(f"  reachable states evaluated: {len(results)}")
        for state, phi in results:
            print(f"    state {state}  ->  Φ = {phi:.6f}")
        print(f"  mean Φ = {np.mean(phis):.6f}   max Φ = {np.max(phis):.6f}   (expected {expect})")
        # Detailed sia for the max-Φ state
        best_state = max(results, key=lambda r: r[1])[0]
        s = sia_report(tpm, cm, best_state)
        print(f"  sia at state {best_state}: Φ = {float(s.phi):.6f}")
        try:
            print(f"    minimum-information partition: {s.partition}")
        except Exception as e:
            print(f"    (partition repr unavailable: {e})")


if __name__ == "__main__":
    _run_controls()
