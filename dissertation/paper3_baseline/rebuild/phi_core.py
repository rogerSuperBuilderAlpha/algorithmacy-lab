"""Paper 3 rebuild — the Φ core, re-derived from scratch, depending only on PyPhi.

Paper 2's instrument classifies a single three-node Worker–System–Counterpart system.
Paper 3 runs the same measure across a whole family of wirings and over four-node
higher-order forms, so the core here generalizes Paper 2's rebuild `instrument.py` to an
arbitrary node count n. At n=3 it computes the identical value (a cross-check the catalog
and typology rely on); the only change is that the node labels and the state enumeration
follow n rather than being fixed at three.

A coordination form is a deterministic Boolean system. Each node updates as a function of
the current state of all nodes. Exact IIT-4.0 system Φ over the minimum-information
partition measures whether that system's cause-effect power is irreducible:

    Φ = 0 at every reachable state  -> the structure factors  -> moderated dyad
    Φ > 0 at some reachable state   -> the structure does not  -> mediated triad

Depends only on PyPhi 4.0 (`pyphi.new_big_phi.sia`) and numpy.
"""

import os
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import new_big_phi, exceptions, convert

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

# Node labels for up to six parties. Paper 3 uses at most four (W, S, C, D).
_LABELS = ("W", "S", "C", "D", "E", "F")


def labels(n):
    return _LABELS[:n]


def tpm_from_rules(rules, n):
    """Deterministic state-by-node TPM, shape (2^n, n), little-endian (bit 0 = node 0).
    rules[j](state_tuple) -> next value of node j in {0,1}."""
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        cur = tuple((s >> i) & 1 for i in range(n))
        for j in range(n):
            tpm[s, j] = float(bool(rules[j](cur)))
    return tpm


def cm_from_rules(rules, n):
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


def reachable_states(tpm, n):
    """Decimal indices of states with at least one predecessor (in-degree >= 1).
    This is the predecessor sense of reachable, the same convention Paper 2 uses: a
    coordination form's verdict rests on states the form can actually occupy."""
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


def system_phi(tpm, cm, state, n):
    """Exact IIT-4.0 system Φ in `state`, with the MIP. Returns (phi, mip_repr) or
    (None, None) if the state is unreachable."""
    network = pyphi.Network(tpm, cm=cm, node_labels=labels(n))
    try:
        subsystem = pyphi.Subsystem(network, tuple(state))
    except exceptions.StateUnreachableError:
        return None, None
    sia = new_big_phi.sia(subsystem)
    phi = max(0.0, float(sia.phi))
    return phi, str(getattr(sia, "partition", None))


def phi_over_states(tpm, cm, n):
    """List of (state_tuple, phi) over every reachable, evaluable state."""
    rows = []
    for s in reachable_states(tpm, n):
        st = tuple((s >> i) & 1 for i in range(n))
        phi, _ = system_phi(tpm, cm, st, n)
        if phi is not None:
            rows.append((st, phi))
    return rows


def placement(rules, n):
    """A form's placement: max and mean Φ over reachable states, the MIP at the max-Φ
    state, connectivity, and the strongly-connected flag. max Φ is the form's band."""
    tpm, cm = tpm_from_rules(rules, n), cm_from_rules(rules, n)
    rows = phi_over_states(tpm, cm, n)
    if not rows:
        return {"max": 0.0, "mean": 0.0, "mip": None, "best_state": None,
                "n_reachable": 0, "cm": cm, "strongly_connected": strongly_connected(cm)}
    phis = [p for _, p in rows]
    imax = int(np.argmax(phis))
    best_state = rows[imax][0]
    _, mip = system_phi(tpm, cm, best_state, n)
    return {"max": float(np.max(phis)), "mean": float(np.mean(phis)), "mip": mip,
            "best_state": best_state, "n_reachable": len(rows), "cm": cm,
            "strongly_connected": strongly_connected(cm)}


# ----- self-check: the n=3 core must reproduce Paper 2's controls exactly --------------

def _selfcheck():
    print("phi_core self-check (must match Paper 2's rebuilt instrument at n=3):")
    factoring = [lambda x: x[1], lambda x: x[0], lambda x: x[2]]          # W'=S, S'=W, C'=C
    irreducible = [lambda x: x[1] or x[2], lambda x: x[0] and x[2], lambda x: x[0] ^ x[1]]
    strict = [lambda x: x[1], lambda x: x[0] and x[2], lambda x: x[1]]     # W'=S, S'=W∧C, C'=S
    for name, rules, want in [
        ("factoring control   (expect maxΦ 0.000)", factoring, 0.0),
        ("irreducible control (expect maxΦ 0.830)", irreducible, 0.830),
        ("strict mediation    (expect maxΦ 2.000)", strict, 2.0),
    ]:
        r = placement(rules, 3)
        ok = abs(r["max"] - want) < 5e-3
        print(f"  {name:42s} got maxΦ={r['max']:.3f} meanΦ={r['mean']:.3f} "
              f"sc={r['strongly_connected']}  {'OK' if ok else 'MISMATCH'}")


if __name__ == "__main__":
    _selfcheck()
