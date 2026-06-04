"""Probe 109 (D3) — is rebinding an ejected party path-dependent (hysteresis)?

Question: an adaptive mediator walks the form from triadic to dyadic as it drops a party (Probe 79). Is
re-including the party symmetric to dropping it, or path-dependent? A mediator with sticky memory should
latch: once coordination is established it persists as the drive falls, so the recovery path differs from
the loss path. Hypothesis: a sticky mediator shows a hysteresis loop in coordination as the engagement
drive is ramped up then down; a memoryless one does not. Method: simulate the worker–system–counterpart
loop while ramping the parties' engagement drive d up 0→1 then down 1→0, carrying state across levels;
measure the system's mean activity at each d on each leg; report the area between the up and down curves
for a sticky vs a memoryless mediator.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_hysteresis
"""

import numpy as np

LEVELS = np.concatenate([np.linspace(0, 1, 21), np.linspace(1, 0, 21)])
SETTLE = 200
WINDOW = 200
SEEDS = 40


def run(persist, rng):
    """Return (d, mean S-activity) per level; state carries across levels.

    The engagement drive d pulls each party to fire. The system commits when both fire, and a sticky
    mediator latches (stays committed while either it or both parties keep it alive). Once committed, the
    parties keep firing to sustain it — the loop that creates a self-holding coordination."""
    state = [0, 0, 0]   # W, S, C
    curve = []
    for d in LEVELS:
        acts = []
        for t in range(SETTLE + WINDOW):
            w, S, c = state
            Snew = 1 if ((w and c) or (S and persist)) else 0
            # a party fires if externally driven, or to sustain an already-active system
            wnew = 1 if (rng.random() < d or (Snew and rng.random() < 0.9)) else 0
            cnew = 1 if (rng.random() < d or (Snew and rng.random() < 0.9)) else 0
            state = [wnew, Snew, cnew]
            if t >= SETTLE:
                acts.append(Snew)
        curve.append((d, float(np.mean(acts))))
    return curve


def loop_area(persist):
    up = np.zeros(21)
    dn = np.zeros(21)
    rng = np.random.default_rng(109)
    for _ in range(SEEDS):
        curve = run(persist, rng)
        for i in range(21):
            up[i] += curve[i][1]
            dn[i] += curve[41 - i][1]      # down leg aligned to same d
    up /= SEEDS
    dn /= SEEDS
    return float(np.mean(np.abs(up - dn))), up, dn


def main():
    print("PROBE 109 (D3) — hysteresis in coordination under a sticky vs memoryless mediator")
    print("=" * 68)
    for persist, name in ((True, "sticky mediator"), (False, "memoryless mediator")):
        area, up, dn = loop_area(persist)
        print(f"  {name:<22} hysteresis area = {area:.4f}")
        print(f"    up-leg   S-activity (d=0.25,0.5,0.75): {up[5]:.2f} {up[10]:.2f} {up[15]:.2f}")
        print(f"    down-leg S-activity (d=0.25,0.5,0.75): {dn[5]:.2f} {dn[10]:.2f} {dn[15]:.2f}")
    print("=" * 68)
    print("  Reading: a non-zero loop area for the sticky mediator and a near-zero one for the memoryless")
    print("  one means rebinding is path-dependent — a mediator with memory keeps a coordination alive as")
    print("  engagement falls, so re-including a party is not the mirror of dropping it. Latching makes")
    print("  the coordination's history matter, the dynamical face of the Probe 43 stickiness result.")
    print("=" * 68)


if __name__ == "__main__":
    main()
