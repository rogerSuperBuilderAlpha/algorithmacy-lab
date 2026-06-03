"""Paper 2 instrument (rebuild, from scratch) — exact IIT-4.0 system Φ as a
moderated-dyad / mediated-triad classifier.

A coordination form is modelled as a 3-node application-layer system:
    W = worker, S = system/mediator, C = counterpart.
Each node's next state is a Boolean function of the current (W, S, C). Exact IIT-4.0
system integrated information Φ over the minimum-information partition measures whether
that cause-effect structure is irreducible.

    Φ = 0 at every reachable state  -> the structure factors  -> MODERATED DYAD
    Φ > 0 at some reachable state   -> the structure does not  -> MEDIATED TRIAD

Depends only on PyPhi 4.0 (`pyphi.new_big_phi.sia`) and numpy — no prior project code.
Run: ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/rebuild/instrument.py
"""

import os
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import new_big_phi, exceptions

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

LABELS = ("W", "S", "C")


# ----- build the application-layer model from per-node Boolean rules -----------------

def tpm_from_rules(rules, n=3):
    """Deterministic state-by-node TPM, shape (2^n, n), little-endian (bit 0 = W).
    rules[j](state_tuple) -> next value of node j in {0,1}."""
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        cur = tuple((s >> i) & 1 for i in range(n))
        for j in range(n):
            tpm[s, j] = float(bool(rules[j](cur)))
    return tpm


def cm_from_rules(rules, n=3):
    """Connectivity: cm[i,j]=1 iff node j's rule depends on node i (flip test)."""
    cm = np.zeros((n, n), dtype=int)
    for s in range(2 ** n):
        cur = [(s >> i) & 1 for i in range(n)]
        for i in range(n):
            flipped = list(cur); flipped[i] ^= 1
            for j in range(n):
                if bool(rules[j](tuple(cur))) != bool(rules[j](tuple(flipped))):
                    cm[i, j] = 1
    return cm


def reachable_states(tpm, n=3):
    """Decimal indices of states with at least one predecessor (PyPhi will analyze)."""
    from pyphi import convert
    sbs = convert.state_by_node2state_by_state(tpm)
    incoming = sbs.sum(axis=0)
    return [j for j in range(2 ** n) if incoming[j] > 1e-12]


def strongly_connected(cm):
    """Is the connectivity graph strongly connected? (necessary for Φ>0.)"""
    n = cm.shape[0]
    reach = cm.astype(bool) | np.eye(n, dtype=bool)
    for _ in range(n):
        reach = reach | (reach @ reach)
    return bool(reach.all())


def system_phi(tpm, cm, state):
    """Exact IIT-4.0 system Φ in `state`, with the MIP. Returns (phi, mip_repr) or
    (None, None) if the state is unreachable."""
    network = pyphi.Network(tpm, cm=cm, node_labels=LABELS)
    try:
        subsystem = pyphi.Subsystem(network, tuple(state))
    except exceptions.StateUnreachableError:
        return None, None
    sia = new_big_phi.sia(subsystem)
    phi = max(0.0, float(sia.phi))
    mip = getattr(sia, "partition", None)
    return phi, str(mip)


def classify(rules, name=""):
    """Run the classifier over all reachable states. Returns a dict with the binary
    verdict, max/mean Φ, the MIP at the max-Φ state, and connectivity."""
    tpm = tpm_from_rules(rules)
    cm = cm_from_rules(rules)
    states = reachable_states(tpm)
    rows = []
    for s in states:
        st = tuple((s >> i) & 1 for i in range(3))
        phi, mip = system_phi(tpm, cm, st)
        if phi is not None:
            rows.append((st, phi, mip))
    if not rows:
        return {"name": name, "verdict": "n/a", "max_phi": 0.0, "mean_phi": 0.0,
                "mip_at_max": None, "strongly_connected": strongly_connected(cm),
                "n_states": 0, "cm": cm}
    phis = [r[1] for r in rows]
    imax = int(np.argmax(phis))
    max_phi = max(phis)
    return {
        "name": name,
        "verdict": "MEDIATED TRIAD" if max_phi > 1e-9 else "MODERATED DYAD",
        "max_phi": max_phi,
        "mean_phi": float(np.mean(phis)),
        "mip_at_max": rows[imax][2],
        "max_state": rows[imax][0],
        "strongly_connected": strongly_connected(cm),
        "n_states": len(rows),
        "cm": cm,
    }


def report(res):
    print(f"  {res['name']:<28} verdict={res['verdict']:<15} "
          f"maxΦ={res['max_phi']:.3f} meanΦ={res['mean_phi']:.3f} "
          f"strongly_conn={res['strongly_connected']} "
          f"n={res['n_states']}")
    if res.get("mip_at_max"):
        print(f"      MIP @ {res.get('max_state')}: {res['mip_at_max']}")


# ----- the validation gate (run before any worked example) ---------------------------

def validation_gate():
    print("VALIDATION GATE")
    # Factoring control: C causally decoupled. Expect Φ = 0 (reduces along party lines).
    factoring = [
        lambda s: s[1],   # W' = S
        lambda s: s[0],   # S' = W
        lambda s: s[2],   # C' = C  (C reads only itself; decoupled)
    ]
    # Irreducible control: each party reads the other two. Expect Φ > 0 (up to ~0.83).
    irreducible = [
        lambda s: s[1] or s[2],     # W' = S ∨ C
        lambda s: s[0] and s[2],    # S' = W ∧ C
        lambda s: s[0] ^ s[1],      # C' = W ⊕ S
    ]
    report(classify(factoring, "factoring (C decoupled)"))
    report(classify(irreducible, "irreducible (each reads 2)"))


if __name__ == "__main__":
    validation_gate()
