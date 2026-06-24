"""Shared forms for the interested-mediator cognition line.

battery_computationalism in theory_batteries.py draws two objects out of the same triad: a channel
(S = f(W), relays the worker, Φ = 0) and an actor (S = W ∧ C, commits the joint determination,
Φ = 2.0). The mediator there is faithful. Q126 replaced the faithful gate with an interested one that
imposes an agenda on the k states where the parties least warrant it. This module joins the two: it
builds the channel form and the actor form at each interestedness level k, so a study can measure the
actor surplus Φ(actor) − Φ(channel) as the mediator goes from faithful to predatory.

The actor form reuses Q126's mediator(agenda, k) directly. The channel form is the matched relay: S
forwards W and imposes the same agenda on the W-values that least warrant it, so it is the channel
counterpart of the actor at the same level of interest.

Forms are lists of per-node lambdas over the little-endian current-state tuple x, labels ('W','S','C'),
ready for org_frontier.probes.lib.verdict / major_complex.
"""

from itertools import combinations

from org_frontier.questions.q126_interested_mediator.probe_interested_mediator import (
    mediator,
    override_order,
    parties_read_by_S,
    STATES,
)

LABELS = ("W", "S", "C")


def actor_rules(agenda, k):
    """The Q126 interested actor: W'=S, C'=S, S'=mediator(agenda,k) over (W,C). k=0 is faithful AND."""
    f = mediator(agenda, k)
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[1]]


def _channel_f(agenda, k):
    """S relays W, imposing the agenda on the W-values least warranting it. Two W-states, so k caps at 2."""
    order = sorted((0, 1), key=lambda w: (w if agenda == 1 else 1 - w))
    override = set(order[: min(k, 2)])
    return lambda w, c: agenda if w in override else w


def channel_rules(agenda, k):
    """The matched channel: W'=S, C'=S, S' relays W with the same agenda imposed (S never reads C)."""
    g = _channel_f(agenda, k)
    return [lambda x: x[1], lambda x, g=g: g(x[0], x[2]), lambda x: x[1]]


def actor_set_rules(agenda, override):
    """The actor when the agenda overrides an explicit set of (W,C) states (for order-averaging)."""
    override = set(override)
    f = lambda w, c: agenda if (w, c) in override else (w & c)
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[1]]


def override_sets(k):
    """All C(4,k) choices of which (W,C) states the agenda overrides."""
    return list(combinations(STATES, k))


# ---------------------------------------------------------------------------
# Embodiment line (q165): read-fidelity compression of an interested mediator,
# and nuance-bit eviction. Reuses battery_embodiment's noisy() sweep machinery
# (the parties read S with fidelity q; q<1 mixes in 0.5 noise) and its N-bit
# reads_n form, substituting the faithful gate with mediator(agenda, k).
# ---------------------------------------------------------------------------

import numpy as np
import pyphi
from pyphi import new_big_phi

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False


def _sphi3(T, labels=LABELS):
    """Max IIT-4.0 Φ over states of a (possibly stochastic) 3-node state-by-node TPM.
    The same reader battery_embodiment.sphi3 uses."""
    net = pyphi.Network(T, node_labels=labels)
    best = 0.0
    for s in range(2 ** len(labels)):
        st = tuple((s >> i) & 1 for i in range(len(labels)))
        try:
            best = max(best, float(new_big_phi.sia(pyphi.Subsystem(net, st)).phi))
        except Exception:
            pass
    return round(best, 4)


def noisy_phi(gate, q):
    """battery_embodiment.noisy: parties read S at fidelity q (q<1 mixes in 0.5),
    S commits gate(W, C). Returns max Φ over states."""
    T = np.zeros((8, 3))
    for s in range(8):
        W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
        T[s, 0] = q * S + (1 - q) * 0.5
        T[s, 2] = q * S + (1 - q) * 0.5
        T[s, 1] = float(gate(W, C))
    return _sphi3(T)


def fidelity_curve(agenda, k, qs):
    """Φ(q) over the fidelity grid qs for the interested mediator mediator(agenda, k).
    k=0 is the faithful AND control."""
    f = mediator(agenda, k)
    return [noisy_phi(f, q) for q in qs]


# --- nuance bit N (H2): the faithful nuanced gate reads N where both parties warrant;
# an interested mediator imposes its agenda on exactly those nuance-bearing states. ---

LABELS_N = ("W", "S", "C", "N")


def _faithful_nuanced_gate(w, c, n):
    """battery_embodiment's reads_n gate: S commits W ∧ C ∧ N. N changes the output
    only in the state where both parties warrant (W=C=1); there the output is N."""
    return w & c & n


def _interested_nuanced_gate(agenda):
    """The interested counterpart of the nuanced gate: on the nuance-bearing state
    (W=C=1, the one state where N would have decided the commit) the mediator imposes
    its agenda and ignores N; faithful AND∧N elsewhere."""
    def g(w, c, n):
        if w == 1 and c == 1:
            return agenda
        return w & c & n
    return g


def reads_n_rules():
    """battery_embodiment's faithful reads_n form over (W, S, C, N): S'=W∧C∧N, N'=W."""
    return [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[0]]


def interested_n_rules(agenda):
    """The interested nuanced mediator over (W, S, C, N): S imposes agenda on the
    nuance-bearing state, N'=W."""
    g = _interested_nuanced_gate(agenda)
    return [lambda x: x[1], lambda x, g=g: g(x[0], x[2], x[3]), lambda x: x[1], lambda x: x[0]]


def reads_nuance(rules):
    """Whether S's rule (node 1) depends on N (node 3), by the connectivity-matrix flip test."""
    from org_frontier.classifier.classifier import cm_from_rules
    return bool(cm_from_rules(rules)[3, 1])


# ---------------------------------------------------------------------------
# Theory-of-mind line (q166): the phantom addressee, made interested.
#
# battery_theory_of_mind reads its address structure off the phantom-addressee
# triad W'=S, S'=W∧C, C'=C: the worker binds the held position S (the major
# complex is {W,S}), the real counterpart C is a referent that the system reads
# but is not a member of the bound whole, and the address is one-way (cm[0,1]=1,
# S depends on W; cm[2,0]=0, the worker never reads C). These forms keep C as the
# self-looping referent and replace the faithful gate W∧C with mediator(agenda,k),
# so a study can watch core membership and the address connectivity cm[0,1] (S
# reads W) / cm[2,0] (W reads C) as the mediator goes from faithful (k=0) to
# agenda-serving (k=4).
# ---------------------------------------------------------------------------


def phantom_rules(agenda, k):
    """The interested phantom-addressee triad: W'=S, S'=mediator(agenda,k) over (W,C),
    C'=C (the counterpart remains the self-looping referent). k=0 is the faithful
    battery T1 form S'=W∧C."""
    f = mediator(agenda, k)
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[2]]


def phantom_set_rules(agenda, override):
    """The phantom-addressee triad when the agenda overrides an explicit set of (W,C)
    states (for order-averaging the robustness sweep)."""
    override = set(override)
    f = lambda w, c: agenda if (w, c) in override else (w & c)
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[2]]


# ---------------------------------------------------------------------------
# Drift-with-agenda bridge (q171): cross the PP4 drift parameter d with the
# Q126 interestedness level k on the same mediator. PP4 (predictive_processing)
# drifts a faithful gate A = W ∧ C toward a flipped rule B = W ∨ C with
# probability d, the moving target of a retraining system. Q126 makes the
# mediator interested: it imposes agenda a on the k least-warranted (W, C)
# states and runs the faithful arm elsewhere. This bridge applies the PP4 drift
# only to the faithful arm (the non-overridden states the parties still rule),
# holding the agenda on the overridden states, so a study can read sphi at each
# (d, k) cell and ask whether drift and interest erode the binding additively,
# super-additively, or whether one masks the other.
# ---------------------------------------------------------------------------

from org_frontier.questions.q126_interested_mediator.probe_interested_mediator import (
    override_order,
)
from org_frontier.threads.margin_to_dyad._sphi import sphi


def drift_target_gate(agenda, k):
    """The rule the interested mediator drifts toward: agenda on the k overridden states,
    the PP4 flipped arm W ∨ C on the rest (the faithful arm A = W ∧ C drifts to B = W ∨ C)."""
    override = set(override_order(agenda)[:k])
    return lambda w, c: agenda if (w, c) in override else (w | c)


def drift_binding_tpm(agenda, d, k):
    """State-by-node TPM for the mediator that is both drifting (PP4 d) and interested (Q126 k).

    S commits the interested gate mediator(agenda, k) with probability (1 − d) and the drifted gate
    drift_target_gate(agenda, k) with probability d; the parties read S faithfully (W' = S, C' = S).
    d = 0 is the pure-interest Q126 edge; k = 0 is the pure-drift PP4 edge (A = W∧C drifting to W∨C)."""
    import numpy as np

    A = mediator(agenda, k)
    B = drift_target_gate(agenda, k)
    T = np.zeros((8, 3))
    for s in range(8):
        W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
        T[s, 0] = S
        T[s, 2] = S
        T[s, 1] = (1 - d) * float(A(W, C)) + d * float(B(W, C))
    return T


def drift_binding_phi(agenda, d, k):
    """Max big-Φ (sphi) of the drifting interested mediator at cell (agenda, d, k)."""
    return sphi(drift_binding_tpm(agenda, d, k))


# ---------------------------------------------------------------------------
# Extended-mind line (q167): the capture threshold meets the agenda.
#
# battery_extended_mind's core4(g) is the four-node extended-mind core: the
# parties and the platform read the system (W'=S, C'=S, P'=S), and the system
# commits a g-weighted mix of the worker's joint determination and the
# platform's. The faithful platform branch is P ∧ C, so as g rises the platform
# input P supplants the worker input W in the system's commit and the worker
# leaves the major complex at a low capture threshold g*. q167 keeps the same
# four-node scaffold and replaces the faithful platform branch P ∧ C with Q126's
# mediator(agenda, k) over the platform's own inputs (P, C): an interested
# platform imposes its agenda a on the k (P, C) states where those inputs least
# warrant it, faithful AND elsewhere. The study sweeps g × agenda × k and reads
# the major-complex membership to locate g* (the first g at which W leaves the
# core) and the post-displacement core composition.
# ---------------------------------------------------------------------------

CORE4_LABELS = ("W", "S", "C", "P")
_CORE4_NM = {0: "W", 1: "S", 2: "C", 3: "P"}


def _platform_branch(agenda, k):
    """The platform's commit over its own inputs (P, C). agenda=None is the
    faithful battery branch P ∧ C; otherwise Q126's mediator(agenda, k) over
    (P, C) — the interested platform imposes its agenda on the k (P, C) states
    that least warrant it, faithful AND elsewhere. k=0 is faithful AND."""
    if agenda is None:
        return lambda p, c: float(p & c)
    f = mediator(agenda, k)
    return lambda p, c, f=f: float(f(p, c))


def core4_tpm(g, agenda=None, k=0):
    """battery_extended_mind's core4(g) TPM, with the platform branch optionally
    made interested. W'=S, C'=S, P'=S; S commits (1-g)·(W∧C) + g·platform(P,C).
    Returns a 16×4 state-by-node TPM over (W, S, C, P)."""
    import numpy as np

    plat = _platform_branch(agenda, k)
    T = np.zeros((16, 4))
    for s in range(16):
        W, S, C, P = s & 1, (s >> 1) & 1, (s >> 2) & 1, (s >> 3) & 1
        T[s, 0] = S
        T[s, 2] = S
        T[s, 3] = S
        T[s, 1] = (1 - g) * float(W & C) + g * plat(P, C)
    return T


def core4_complex(g, agenda=None, k=0):
    """(core_string, phi) of the maximal complex of core4_tpm(g, agenda, k),
    max over the 16 states — the exact reader battery_extended_mind.core4 uses
    (pyphi.new_big_phi.maximal_complex). core_string is the sorted node labels,
    e.g. 'WSC', or '-' if no complex. The platform branch is faithful P∧C when
    agenda is None, else the interested mediator(agenda, k)."""
    net = pyphi.Network(core4_tpm(g, agenda, k), node_labels=CORE4_LABELS)
    best = (-1.0, None)
    for st in range(16):
        stt = tuple((st >> i) & 1 for i in range(4))
        try:
            mc = new_big_phi.maximal_complex(net, stt)
            if hasattr(mc, "node_indices") and float(mc.phi) > best[0]:
                best = (float(mc.phi), tuple(sorted(mc.node_indices)))
        except Exception:
            pass
    core = "".join(_CORE4_NM[i] for i in best[1]) if best[1] else "-"
    return core, (round(best[0], 3) if best[1] else 0.0)


# ---------------------------------------------------------------------------
# Facet-difficulty bridge (q172). The six prior interested-mediator studies each
# read one theory battery's difficulty measure as a mediator goes from opaque
# (faithful) to interested (Q126's agenda on the least-warranted states). q172
# aggregates them into one difficulty vector per facet and reruns it across the
# four Q127 faithful baselines (AND/OR/XNOR/XOR). Each facet here is a function
# of a faithful baseline gate base(w, c) and an agenda, returning the difficulty
# the faithful (opaque) form carries and the difficulty the interested (k=1)
# form carries. The interested-minus-opaque gap, normalized per facet, is the
# "interest tax" the study ranks.
#
# The interested gate at level k overrides the agenda on the k (W, C) states the
# faithful baseline least warrants the agenda in (Q127's override_order), faithful
# baseline elsewhere — the same construction Q127 uses for every baseline.
# ---------------------------------------------------------------------------

import math
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.cognition.predictive_processing import (
    residual_surprise_under_mediator,
)

# The four Q127 faithful baselines as output tables over (W, C), little-endian.
Q127_BASELINES = {
    "AND": {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 1},
    "OR": {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 1},
    "XNOR": {(0, 0): 1, (0, 1): 0, (1, 0): 0, (1, 1): 1},   # AGREE (iff W==C)
    "XOR": {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0},    # DIFFER (iff W!=C)
}


def _override_order_baseline(agenda):
    """States ordered by least warrant for the agenda first (Q127's order)."""
    warrant = lambda wc: (wc[0] + wc[1]) if agenda == 1 else (2 - (wc[0] + wc[1]))
    return sorted(STATES, key=lambda wc: (warrant(wc), wc))


def baseline_gate(base, agenda, k):
    """The interested gate over a faithful baseline: agenda on the k least-warranted
    (W, C) states, the faithful baseline base[(w, c)] elsewhere. k=0 is the faithful
    baseline itself."""
    override = set(_override_order_baseline(agenda)[:k])
    return lambda w, c: agenda if (w, c) in override else base[(w, c)]


def _triad_from_gate(gate):
    """W'=S, C'=S, S'=gate(W, C) — the committing triad for a gate over (W, C)."""
    return [lambda x: x[1], lambda x, g=gate: g(x[0], x[2]), lambda x: x[1]]


def _phantom_from_gate(gate):
    """W'=S, C'=C, S'=gate(W, C) — the phantom-addressee triad (C self-loops)."""
    return [lambda x: x[1], lambda x, g=gate: g(x[0], x[2]), lambda x: x[2]]


def _noisy_gate_phi(gate, q):
    """battery_embodiment.noisy at fidelity q for an arbitrary gate(W, C)."""
    T = np.zeros((8, 3))
    for s in range(8):
        W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
        T[s, 0] = q * S + (1 - q) * 0.5
        T[s, 2] = q * S + (1 - q) * 0.5
        T[s, 1] = float(gate(W, C))
    return _sphi3(T)


def _marginal_fit_error(gate):
    """Share of (W, C) states the worker-marginal majority-over-C model mispredicts
    (the direct-perception D2 reader, computed exactly on the gate's truth table)."""
    fW = {}
    for w in (0, 1):
        ones = sum(gate(w, c) for c in (0, 1))
        fW[w] = 1 if ones >= 1.0 else 0   # majority over C (tie -> 1, matching D2)
    wrong = sum(fW[w] != gate(w, c) for w in (0, 1) for c in (0, 1))
    return wrong / 4.0


# Facet -> (survey-scale name, battery). The six facets, one per theory battery.
FACETS = [
    ("commitment", "computationalism"),
    ("counterpart_inference", "direct_perception"),
    ("signal_compression", "embodiment"),
    ("phantom_addressee", "theory_of_mind"),
    ("opacity_floor", "predictive_processing(opacity)"),
    ("rule_change_tracking", "predictive_processing(drift)"),
]

# The survey scale names three of the six facets directly; the bridge maps them.
SURVEY_FACETS = {"counterpart_inference", "signal_compression", "rule_change_tracking"}


def _drift_gate_phi(gate_faithful_arm, gate, d=0.25):
    """PP4 drift binding for a gate: S commits gate with prob (1-d), the flipped
    arm (W|C on the non-overridden states) with prob d. Returns sphi over states."""
    T = np.zeros((8, 3))
    for s in range(8):
        W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
        A = float(gate(W, C))
        B = float(gate_faithful_arm(W, C))
        T[s, 0] = S
        T[s, 2] = S
        T[s, 1] = (1 - d) * A + d * B
    return _sphi3(T)


def facet_difficulty(facet, base, agenda, k_interested=1):
    """(opaque_difficulty, interested_difficulty) for one facet on one faithful
    baseline. Difficulty is oriented so larger = harder. Opaque is the faithful
    baseline gate (k=0); interested is the Q126/Q127 gate at k_interested.

    commitment            — the actor's whole-system Φ is the binding it holds; the
                            difficulty the worker faces is the Φ she would lose, so the
                            difficulty is (Φ_max - Φ). Φ_max=2.0 is the faithful triad.
    counterpart_inference — the worker-marginal fit error with C hidden (direct
                            perception D2). Higher error = harder to infer the rule.
    signal_compression    — Φ lost under a reduced read fidelity (q=0.5): the
                            difficulty of pouring intent through the channel is the
                            meaning shed, (Φ(q=1) - Φ(q=0.5)) for the gate.
    phantom_addressee     — the phantom triad's major-complex Φ measures how much the
                            held position binds the worker; difficulty is (2.0 - coreΦ).
    opacity_floor         — the residual surprise H(out|W) the worker cannot model away.
    rule_change_tracking  — Φ lost when the gate drifts (PP4 d=0.25): a drifting commit
                            binds less, so difficulty is (Φ_static - Φ_drift)."""
    gate0 = baseline_gate(base, agenda, 0)             # opaque/faithful
    gatek = baseline_gate(base, agenda, k_interested)  # interested

    if facet == "commitment":
        d0 = 2.0 - verdict(_triad_from_gate(gate0), LABELS).max_phi
        dk = 2.0 - verdict(_triad_from_gate(gatek), LABELS).max_phi
        return d0, dk
    if facet == "counterpart_inference":
        return _marginal_fit_error(gate0), _marginal_fit_error(gatek)
    if facet == "signal_compression":
        d0 = _noisy_gate_phi(gate0, 1.0) - _noisy_gate_phi(gate0, 0.5)
        dk = _noisy_gate_phi(gatek, 1.0) - _noisy_gate_phi(gatek, 0.5)
        return d0, dk
    if facet == "phantom_addressee":
        c0 = major_complex(_phantom_from_gate(gate0), LABELS)
        ck = major_complex(_phantom_from_gate(gatek), LABELS)
        phi0 = c0[1] if c0[0] else 0.0
        phik = ck[1] if ck[0] else 0.0
        return 2.0 - phi0, 2.0 - phik
    if facet == "opacity_floor":
        return residual_surprise_under_mediator(gate0), residual_surprise_under_mediator(gatek)
    if facet == "rule_change_tracking":
        # the drifted arm flips the non-overridden states to W|C (the PP4 target)
        ov0 = set(_override_order_baseline(agenda)[:0])
        ovk = set(_override_order_baseline(agenda)[:k_interested])
        armk = lambda w, c: agenda if (w, c) in ovk else (w | c)
        arm0 = lambda w, c: agenda if (w, c) in ov0 else (w | c)
        d0 = _sphi_static(gate0) - _drift_gate_phi(arm0, gate0)
        dk = _sphi_static(gatek) - _drift_gate_phi(armk, gatek)
        return d0, dk
    raise ValueError(f"unknown facet {facet}")


def _sphi_static(gate):
    """sphi of the static committing triad for a gate (the d=0 drift edge)."""
    T = np.zeros((8, 3))
    for s in range(8):
        W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
        T[s, 0] = S
        T[s, 2] = S
        T[s, 1] = float(gate(W, C))
    return _sphi3(T)
