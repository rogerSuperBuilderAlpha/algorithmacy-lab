"""Agent-based coordination experiment: does the determination STRUCTURE that Φ keys on
predict coordination difficulty at FIXED party count (n=3), when only that structure varies?

WHAT THIS IS, AND IS NOT. The agents are independent contextual-bandit learners that maximize
joint reward from the information their structural position gives them; they never see Φ, the
condition label, or each other's policy. So the result is not circular in the trivial sense —
nothing tells the agents the answer. But it is NOT an independent validation of Φ either: a
condition's Φ and its coordination difficulty are BOTH deterministic consequences of the same
wiring + mediator function (e.g. a lossy AND determination both raises Φ and destroys the
information the receiver needs). This experiment is therefore a behavioral CONSISTENCY CHECK —
it shows the structural classifier tracks a real coordination cost — not a test of Φ against a
criterion measured separately from the structure. The honest claim is consistency, not
non-circular validation. (See Paper 3 §4.5.)

ROUNDS is configurable via the SIM_ROUNDS env var (default 600, the committed run). A longer run
(e.g. SIM_ROUNDS=3000) tests whether the difficulty gap is an asymptote rather than under-training;
non-default runs write a suffixed CSV so the committed 600-round artifact stays reproducible.

TASK (transmit-and-agree, fresh target every round, sequential within-round flow):
  1. A target bit T is drawn iid each round and shown to the SENDER only.
  2. The sender acts (sets its node to signal T).
  3. The mediator commits its determination S from the sender's current value and the
     receiver's standing (previous) value.
  4. The RECEIVER observes only the nodes its structural position lets it read, then acts.
  5. Reward (joint) = 1 iff sender and receiver both output T.
Because T is fresh each round and reward arrives only after acting, the receiver CANNOT
learn T from reward; it must DECODE T from the channel its structure provides. That is the
whole point: the structure's information loss is what makes coordination hard or easy.
Sender role alternates across episodes so both channel directions are tested.

Difficulty = 1 - asymptotic success. Hyperparameters fixed a priori, identical across
conditions; the only thing that varies is the wiring + mediator function. Party count = 3.

Run:  ~/iit-playground/venv-4.0/bin/python coordination_sim.py
Writes ../results/sim_runs.csv
"""

import csv
import os
import zlib

import numpy as np


def _cell_seed(seed, name, sender):
    """Deterministic per-cell seed. Uses zlib.crc32 (stable across processes) rather than
    the built-in hash(), which is salted per-process and made the experiment irreproducible."""
    return seed * 100003 + (zlib.crc32((name + sender).encode()) % 9973)

# ---- a-priori hyperparameters (frozen; identical across conditions) -------------------
LR = 0.1
EPS_START, EPS_FLOOR, EPS_DECAY_FRAC = 1.0, 0.05, 0.7
ROUNDS = int(os.environ.get("SIM_ROUNDS", "600"))   # 600 = committed run; set 3000 for robustness
PAIRS_PER_CELL = 120
SEEDS = [1, 2, 3, 4, 5]
TAIL_FRAC = 0.2

AND = lambda a, b: a & b
OR = lambda a, b: a | b
XOR = lambda a, b: a ^ b

# name, phi, reads_W, reads_C, s_rule, back_channel  (reads_* = nodes that party observes)
CONDITIONS = [
    ("C0_dyadic", 0.00, ("C",),      ("W",),      None, True),
    ("C1_parity", 0.50, ("S",),      ("S",),      XOR,  False),
    ("C2_partial", 0.83, ("S", "C"), ("S", "W"),  AND,  True),
    ("C3_strict", 2.00, ("S",),      ("S",),      AND,  False),
]


def eps_at(t):
    frac = t / (EPS_DECAY_FRAC * ROUNDS)
    return max(EPS_FLOOR, EPS_START - (EPS_START - EPS_FLOOR) * frac)


def act(Q, obs, eps, rng):
    q = Q.setdefault(obs, [0.0, 0.0])
    if rng.random() < eps:
        return int(rng.integers(2)), q
    return int(np.argmax(q)), q


def run_episode(cond, sender, rng):
    _, _, reads_W, reads_C, s_rule, _ = cond
    recv = "C" if sender == "W" else "W"
    recv_reads = reads_C if recv == "C" else reads_W
    Q_s, Q_r = {}, {}            # sender, receiver Q-tables
    w_prev, s_prev, c_prev = (int(rng.integers(2)) for _ in range(3))
    own_r_prev = c_prev if recv == "C" else w_prev
    tail_start = int((1 - TAIL_FRAC) * ROUNDS)
    hits, n = 0.0, 0

    for t in range(ROUNDS):
        eps = eps_at(t)
        T = int(rng.integers(2))

        # 1-2. sender observes T, acts
        a_s, qs = act(Q_s, (T,), eps, rng)

        # 3. mediator commits: sender's current value + receiver's previous value
        if sender == "W":
            w_val, c_val = a_s, c_prev
        else:
            w_val, c_val = w_prev, a_s
        s_val = s_rule(w_val, c_val) if s_rule is not None else s_prev

        # 4. receiver observes only what its wiring permits (post-sender state) + own prev
        node_vals = {"W": w_val, "S": s_val, "C": c_val}
        o_r = (own_r_prev,) + tuple(node_vals[nm] for nm in recv_reads)
        a_r, qr = act(Q_r, o_r, eps, rng)

        # 5. reward + learn (bandit)
        r = 1.0 if (a_s == T and a_r == T) else 0.0
        qs[a_s] += LR * (r - qs[a_s])
        qr[a_r] += LR * (r - qr[a_r])

        # roll state forward
        if sender == "W":
            w_prev, c_prev = a_s, a_r
        else:
            w_prev, c_prev = a_r, a_s
        s_prev = s_rule(w_prev, c_prev) if s_rule is not None else s_prev
        own_r_prev = a_r

        if t >= tail_start:
            hits += r
            n += 1

    return hits / n


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    fname = "sim_runs.csv" if ROUNDS == 600 else f"sim_runs_{ROUNDS}.csv"
    out = os.path.join(here, "..", "results", fname)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    print(f"[ROUNDS={ROUNDS}]")
    rows = []
    print(f"{'condition':<12}{'Φ':>6}  {'success (mean over senders, seeds)':>34}")
    for cond in CONDITIONS:
        name, phi = cond[0], cond[1]
        cell_means = []
        for sender in ("W", "C"):
            for seed in SEEDS:
                rng = np.random.default_rng(_cell_seed(seed, name, sender))
                s = [run_episode(cond, sender, rng) for _ in range(PAIRS_PER_CELL)]
                m = float(np.mean(s))
                rows.append({"condition": name, "phi": phi, "sender": sender,
                             "seed": seed, "success": round(m, 4)})
                cell_means.append(m)
        print(f"{name:<12}{phi:>6.2f}  {np.mean(cell_means):>20.3f}  (sd {np.std(cell_means):.3f})")
    with open(out, "w", newline="") as fh:
        wts = csv.DictWriter(fh, fieldnames=["condition", "phi", "sender", "seed", "success"])
        wts.writeheader()
        wts.writerows(rows)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
