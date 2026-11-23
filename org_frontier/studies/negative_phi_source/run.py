"""Trace one published negative φ to PyPhi's signed GID formula.

Run from the repo root: python org_frontier/studies/negative_phi_source/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md (committed before any run of this script).
"""
import argparse
import json
import os
import sys
from importlib.metadata import version
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi  # noqa: E402
from pyphi import new_big_phi  # noqa: E402
from pyphi.direction import Direction  # noqa: E402

from org_frontier.classifier.classifier import PHI_EPS  # noqa: E402
from org_frontier.probes.weighted_quorum.input_noise.probe_input_noise import input_tpm  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import (  # noqa: E402
    cm_numeric, gate_c1, labels_for, table_of,
)

PUBLISHED = -0.13178321094580336
ETA = 0.3
STATE = (0, 0, 0, 0)
SUBSETS = (("SP1", (0, 1)), ("SP2", (0, 2)))
REL_PHI = 1e-12
REL_GID = 1e-10


def _as_vector(x):
    if x is None:
        return None
    return np.asarray(x, dtype=float).reshape(-1)


def _state_tuple(value):
    if value is None:
        return None
    if hasattr(value, "state"):
        value = value.state
    if isinstance(value, (int, np.integer)):
        return (int(value),)
    return tuple(int(v) for v in np.asarray(value).reshape(-1))


def _state_index(state, n_entries):
    if state is None:
        return None
    bits = _state_tuple(state)
    n_bits = int(np.log2(n_entries)) if n_entries > 1 else 1
    if bits is None:
        return None
    if len(bits) == 1 and n_entries == 1:
        return 0
    if 2 ** len(bits) == n_entries:
        return sum(b << i for i, b in enumerate(bits))
    if len(bits) == 1 and 0 <= bits[0] < n_entries:
        return bits[0]
    return None


def gid_product(ria):
    """Recompute selectivity × log2(forward / partitioned) at the specified state."""
    if ria is None:
        return None
    forward = _as_vector(ria.repertoire)
    partitioned = _as_vector(ria.partitioned_repertoire)
    sel = None if ria.selectivity is None else float(ria.selectivity)
    specified = _state_tuple(getattr(ria, "specified_state", None)) or _state_tuple(
        getattr(ria, "purview_state", None)
    )
    if forward is None or partitioned is None or sel is None:
        return dict(selectivity=sel, informativeness=None, product=None,
                    specified_state=specified, forward=None if forward is None else forward.tolist(),
                    partitioned=None if partitioned is None else partitioned.tolist())
    if partitioned.size == 1 and forward.size > 1:
        idx = _state_index(specified, forward.size)
        f = float(forward[idx]) if idx is not None else None
        p = float(partitioned[0])
    elif forward.size == partitioned.size:
        idx = _state_index(specified, forward.size)
        if idx is None and forward.size == 1:
            idx = 0
        f = float(forward[idx]) if idx is not None else None
        p = float(partitioned[idx]) if idx is not None else None
    else:
        f, p = None, None
    if f is None or p is None or f <= 0 or p <= 0:
        info, product = None, None
    else:
        info = float(np.log2(f / p))
        product = float(sel * info)
    return dict(
        selectivity=sel,
        informativeness=info,
        product=product,
        forward_at_state=f,
        partitioned_at_state=p,
        specified_state=specified,
        forward=forward.tolist(),
        partitioned=partitioned.tolist(),
    )


def ria_record(ria):
    if ria is None:
        return None
    gid = gid_product(ria)
    direction = getattr(ria, "direction", None)
    return dict(
        phi=float(ria.phi),
        direction=None if direction is None else str(direction),
        purview=list(ria.purview) if ria.purview is not None else None,
        partition=str(ria.partition) if ria.partition is not None else None,
        selectivity=gid["selectivity"],
        informativeness=gid["informativeness"],
        gid_product=gid["product"],
        forward_at_state=gid.get("forward_at_state"),
        partitioned_at_state=gid.get("partitioned_at_state"),
        specified_state=list(gid["specified_state"]) if gid["specified_state"] is not None else None,
        repertoire=gid["forward"],
        partitioned_repertoire=gid["partitioned"],
    )


def analyze(subset_name, indices):
    labels = labels_for(3)
    tpm = input_tpm(table_of((1, 1, 1), 1), 3, ETA)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels)
    sia = new_big_phi.sia(pyphi.Subsystem(net, STATE, indices))
    return dict(
        subset=subset_name,
        indices=list(indices),
        state="".join(map(str, STATE)),
        eta=ETA,
        system_phi=float(sia.phi),
        mip=str(sia.partition) if sia.partition is not None else None,
        cause=ria_record(sia.cause),
        effect=ria_record(sia.effect),
    )


def rel_ok(a, b, tol):
    if a is None or b is None:
        return False
    return abs(a - b) <= tol * max(abs(b), 1e-18)


def show(x):
    c = x["cause"] or {}
    e = x["effect"] or {}
    print(f"{x['subset']} state={x['state']} system={x['system_phi']:.12f} "
          f"cause={c.get('phi')} effect={e.get('phi')} "
          f"effect_sel={e.get('selectivity')} effect_info={e.get('informativeness')} "
          f"effect_gid={e.get('gid_product')} mip={x['mip']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    rows = [analyze(name, idx) for name, idx in (SUBSETS[:1] if args.quick else SUBSETS)]
    for x in rows:
        show(x)
    sp1 = rows[0]
    if not rel_ok(sp1["system_phi"], PUBLISHED, REL_PHI):
        raise SystemExit(f"control failed: system_phi={sp1['system_phi']} != {PUBLISHED}")
    print(f"C2 OR3 SP1 0000 eta=0.3 control system={sp1['system_phi']:.15f}: PASS")
    if args.quick:
        return
    cause, effect = sp1["cause"], sp1["effect"]
    scores = {
        "H1": (
            effect is not None and cause is not None
            and rel_ok(sp1["system_phi"], effect["phi"], REL_PHI)
            and rel_ok(sp1["system_phi"], PUBLISHED, REL_PHI)
            and cause["phi"] >= 0
        ),
        "H2": (
            effect is not None
            and effect["informativeness"] is not None
            and effect["informativeness"] < 0
            and effect["selectivity"] is not None
            and effect["selectivity"] > 0
            and rel_ok(effect["gid_product"], effect["phi"], REL_GID)
            and rel_ok(effect["gid_product"], sp1["system_phi"], REL_GID)
        ),
        "H3": False,
    }
    if len(rows) > 1:
        sp2 = rows[1]
        scores["H3"] = (
            rel_ok(sp2["system_phi"], sp1["system_phi"], REL_PHI)
            and rel_ok(sp2["cause"]["phi"], cause["phi"], REL_PHI)
            and rel_ok(sp2["effect"]["phi"], effect["phi"], REL_PHI)
        )
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"),
            phi_eps=PHI_EPS,
            published=PUBLISHED,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows,
        ), indent=1) + "\n")


if __name__ == "__main__":
    main()
