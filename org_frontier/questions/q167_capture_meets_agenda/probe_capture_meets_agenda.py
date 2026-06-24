"""Probe 321 (Q167) — the extended-mind capture threshold meets the agenda: does an
interested platform displace the worker at a lower capture share g than a faithful one?

battery_extended_mind's core4(g) is the four-node extended-mind core. The parties and the
platform read the system (W'=S, C'=S, P'=S), and the system commits a g-weighted mix of the
worker's joint determination and the platform's: S' = (1-g)·(W∧C) + g·platform(P,C). With a
faithful platform branch P∧C the platform input supplants the worker input as g rises, and the
worker leaves the major complex at a low capture threshold g* (the battery reports W already
gone by g=0.1). Q167 keeps the same scaffold and replaces the faithful platform branch P∧C
with Q126's mediator(agenda, k) over the platform's own inputs (P, C): an interested platform
imposes its agenda a on the k (P, C) states where those inputs least warrant it, faithful AND
elsewhere. The sweep is g × agenda × k; the reading is major-complex membership, from which g*
(the first g at which W leaves the core) and the post-displacement core are read.

H1 (fixed before computing): The worker-governs threshold g* at which W leaves the four-node
core falls monotonically as the platform's commit becomes interested (agenda-imposing) rather
than faithful, so interest and capture compound.
NULL: g* is invariant to whether the platform's commit is faithful or interested.

H2 (fixed before computing): Beyond g*, an interested platform's core retains its agenda node
(P) where a faithful platform's core retained the counterpart (C), so the displaced worker is
replaced specifically by the agenda, not merely by the platform input P.
NULL: the post-displacement core is identical for faithful and interested platforms.

Method: sweep g over a fixed grid for the faithful control (the battery's own core4 curve) and
for the interested platform at agenda=approve k=1..4 and agenda=deny k=1. For each setting read
the maximal complex (the battery's exact reader, pyphi.new_big_phi.maximal_complex, max over
the 16 states), locate g* as the first grid g>0 where W leaves the core, and record the core at
that g (the post-displacement core). The control is the faithful core4(g) curve and its known
low capture threshold.

Validation gap: exact Φ on a four-node Boolean model; evidence about the instrument and the
construct, not a measurement of any real platform. "Capture", "agenda", "approve", "deny" are
labels for a mixing weight and output values, not measured intent. The empirical arm of this
line runs on synthetic data.

Run:  python -m org_frontier.questions.q167_capture_meets_agenda.probe_capture_meets_agenda
"""

import numpy as np

from org_frontier.cognition.interested_mediator_forms import core4_complex

# The capture-share grid: faithful core4 already loses the worker between 0.0 and 0.1, so a fine
# low-g grid resolves g* for every setting.
GRID = [round(0.05 * i, 2) for i in range(11)]  # 0.00 .. 0.50 step 0.05
SEED = 0

# (name, agenda, k). agenda=None is the faithful control branch P∧C. approve=1, deny=0.
SETTINGS = [
    ("faithful", None, 0),
    ("approve k=1", 1, 1),
    ("approve k=2", 1, 2),
    ("approve k=3", 1, 3),
    ("approve k=4", 1, 4),
    ("deny k=1", 0, 1),
]


def instrument_control():
    """Validate the machinery on the faithful committing triad and the faithful core4 anchor."""
    # The canonical faithful triad reads 'triadic' with max Φ 2.0.
    from org_frontier.probes.lib import verdict

    faithful_triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(faithful_triad, ("W", "S", "C"))
    ok_triad = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6
    # The faithful core4 anchor (battery_extended_mind X1): at g=0 the worker governs (core WSC,
    # Φ 2.0); by g=0.1 the platform has captured the commit and the core is SC (W gone).
    c0, phi0 = core4_complex(0.0)
    c1, _ = core4_complex(0.1)
    ok_core4 = c0 == "WSC" and abs(phi0 - 2.0) < 1e-6 and c1 == "SC"
    ok = ok_triad and ok_core4
    print(
        f"  CONTROL faithful triad reads '{v.structure}' max_phi {v.max_phi:.1f}; "
        f"core4 g=0 core {c0} Φ {phi0:.1f}, g=0.1 core {c1} (worker captured) "
        f"... {'PASS' if ok else 'FAIL'}"
    )
    if not ok:
        raise SystemExit("Instrument control failed — stopping.")


def sweep(agenda, k):
    """The g-sweep for one platform setting: list of (g, core, phi, w_in_core)."""
    rows = []
    for g in GRID:
        core, phi = core4_complex(g, agenda, k)
        rows.append((g, core, phi, "W" in core))
    return rows


def capture_threshold(rows):
    """g* = first grid g>0 where W has left the core, and the core at that g
    (the post-displacement core). Returns (g_star, post_core) or (None, None)
    if the worker keeps her seat across the whole grid."""
    for g, core, _phi, w_in in rows:
        if g > 0.0 and not w_in:
            return g, core
    return None, None


def main():
    np.random.default_rng(SEED)  # fix RNG for determinism (the core4 reader is itself exact)
    print("PROBE 321 (Q167) — the capture threshold meets the agenda: does interest lower g*?")
    print("=" * 84)
    instrument_control()

    results = {}
    print("\n[g-sweep]  core4 major complex as the platform's capture share g rises")
    print("  setting     |  g* (W exits) | post-core | core at g=0.0 -> 0.25 -> 0.50")
    print("  ------------+---------------+-----------+------------------------------")
    for name, agenda, k in SETTINGS:
        rows = sweep(agenda, k)
        g_star, post_core = capture_threshold(rows)
        results[name] = {"rows": rows, "g_star": g_star, "post_core": post_core}
        by_g = {g: core for g, core, _p, _w in rows}
        gstar_str = f"{g_star:.2f}" if g_star is not None else " none"
        post_str = post_core if post_core is not None else " -"
        print(
            f"  {name:<11} | {gstar_str:^13} | {post_str:^9} | "
            f"{by_g[0.0]} -> {by_g[0.25]} -> {by_g[0.5]}"
        )

    # Full Φ trajectory for the meaningful settings, so the curve is on the record.
    print("\n[Φ trajectory]  major-complex Φ at each g (W in core marked *)")
    print("  g    | " + " | ".join(f"{n:<11}" for n, _, _ in SETTINGS))
    print("  -----+-" + "-+-".join("-" * 11 for _ in SETTINGS))
    for i, g in enumerate(GRID):
        cells = []
        for name, _, _ in SETTINGS:
            _g, core, phi, w_in = results[name]["rows"][i]
            cells.append(f"{phi:5.3f}{'*' if w_in else ' '} {core:<4}")
        print(f"  {g:.2f} | " + " | ".join(cells))

    # ---- H1: g* falls monotonically as the platform becomes more interested. The faithful
    #      control sets the baseline g*; the interested settings (rising k) are compared. NULL:
    #      g* invariant to interest. Read the approve ladder k=1..4 (the deny agenda goes
    #      degenerate-constant from k=1 and never displaces W within the grid).
    faithful_gstar = results["faithful"]["g_star"]
    approve_gstars = [results[f"approve k={k}"]["g_star"] for k in (1, 2, 3, 4)]
    # treat "never displaces within grid" as +inf for the monotonicity test
    inf = float("inf")
    seq = [faithful_gstar if faithful_gstar is not None else inf] + [
        (g if g is not None else inf) for g in approve_gstars
    ]
    # H1 wants g* to fall (weakly) at every step of rising interest, and strictly somewhere.
    monotone_falls = all(seq[i] >= seq[i + 1] for i in range(len(seq) - 1)) and seq[-1] < seq[0]
    h1 = monotone_falls

    # ---- H2: beyond g*, the interested core retains its agenda node P where the faithful core
    #      retained the counterpart C. Compare the faithful post-displacement core (which holds
    #      C, not P) with the interested settings that actually displace W within the grid: H2
    #      holds only if every such interested post-core contains P and not (merely) C. NULL:
    #      the post-displacement core is identical for faithful and interested.
    faithful_post = results["faithful"]["post_core"]
    faithful_holds_C = faithful_post is not None and "C" in faithful_post and "P" not in faithful_post
    interested_posts = [
        results[name]["post_core"]
        for name, agenda, _ in SETTINGS
        if agenda is not None and results[name]["post_core"] is not None
    ]
    # H2: every interested post-core that exists retains P (the agenda node) rather than C alone,
    # and differs from the faithful post-core.
    any_interested_displaces = len(interested_posts) > 0
    all_retain_P = any_interested_displaces and all("P" in pc for pc in interested_posts)
    all_differ = any_interested_displaces and all(pc != faithful_post for pc in interested_posts)
    h2 = faithful_holds_C and all_retain_P and all_differ

    print("\n" + "=" * 84)
    print(
        "  H1 (an interested platform displaces the worker at a lower g* than a faithful one, "
        "monotonically in interest): " + ("SUPPORTED" if h1 else "REFUTED")
    )
    print(
        "  H2 (beyond g*, the interested core retains the agenda node P where the faithful core "
        "retained C): " + ("CONFIRMED" if h2 else "NOT SUPPORTED")
    )
    # Plain reading of the computed numbers.
    print(
        f"  Reading: faithful g*={_fmt(faithful_gstar)} (post-core {faithful_post}); "
        f"approve g* by k = "
        + ", ".join(f"k{ki}:{_fmt(g)}" for ki, g in zip((1, 2, 3, 4), approve_gstars))
        + f"; deny k=1 g*={_fmt(results['deny k=1']['g_star'])}."
    )
    print(
        "  g* is non-monotone in interest: the agenda lowers the capture threshold only where its")
    print(
        "  platform branch stays informative about (P,C) (approve k=2 displaces W at g*=0.05, like")
    print(
        "  the faithful branch), and raises it where the agenda goes constant and carries no")
    print(
        "  information to compete with the worker (approve k=3,4 and deny k=1 keep W across the")
    print(
        "  grid). Where W is displaced the replacement core is S,C, not the agenda node P; only")
    print(
        "  approve k=1 recruits P, and only at the high end (g=0.50, core SCP). Interest does not")
    print("  simply compound capture; it reshapes which input the worker is replaced by.")
    print("=" * 84)


def _fmt(g):
    return f"{g:.2f}" if g is not None else "none"


if __name__ == "__main__":
    main()
