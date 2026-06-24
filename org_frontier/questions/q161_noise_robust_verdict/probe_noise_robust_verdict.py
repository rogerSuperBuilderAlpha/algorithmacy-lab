"""Probe 315 (Q161) — noise-robust structural verdict: which CRQA-derived verdict survives
update-noise misspecification between the flip rate used and the form's natural regime?

QUESTION
    A CRQA reading of a Boolean coordination form is taken from a stochastic run whose update
    noise (the per-node flip rate) is set by the analyst, not by the form. The flip rate the
    analyst picks need not match the form's natural regime. Three structural verdicts are read
    from such a run and compared to a fixed exact-Φ ground truth: the triadic/dyadic verdict
    (major-complex core size >= 3 vs == 2), per-node membership (in-core vs spectator), and the
    bottleneck node (the form's structural articulation point). Which of the three is most robust
    to flip-rate misspecification?

H1 (fixed before computing)
    The triadic/dyadic verdict stays correct across flip in {0.02 .. 0.30} for more than 80% of
    forms, while bottleneck-node recovery degrades by more than 20 points between the best and
    worst flip rate. Null: all three verdicts show the same flip-rate sensitivity (the spread in
    agreement across flip is the same for each verdict).

H2 (fixed before computing)
    Each form has a flip rate that maximizes verdict agreement, and that optimum is not constant
    across forms: the per-form optimum correlates with the form's intrinsic update entropy (a
    flip-independent property of its truth table). Null: a single flip rate is optimal for all
    forms (the per-form optima are constant), so there is nothing for entropy to track.

METHOD
    Corpus: the curated 3-node forms_library plus the named multiparty forms (n = 4, 5). Each
    form is labeled by its exact IIT-4.0 major complex over reachable states: the triadic/dyadic
    label from core size, the per-node membership vector from the core node_indices, and the
    structural bottleneck set from the leave-one-node-out drop in major-complex Φ. Sub-dyadic
    forms (core < 2) are dropped. The ground truth is fixed and flip-independent.

    Sweep flip over {0.02, 0.05, 0.08, 0.12, 0.18, 0.30}. At each flip a trajectory is sampled
    (seeded) for every form and the three CRQA verdicts are recomputed:
      triadic/dyadic - the prominence spread (count of pairwise links above PROM_FLOOR) read
          against a threshold calibrated once at the natural flip (0.08): triadic if spread is at
          or above the threshold, else dyadic. Agreement = 1 if the read label matches the
          structural label.
      membership     - per-node coupling_centrality read against a per-form median threshold:
          a node is called in-core if its centrality is above the form's median centrality.
          Agreement = fraction of nodes whose call matches the structural membership vector.
      bottleneck     - argmax coupling_centrality against the structural argmax-drop set.
          Agreement = 1 if the behavioral argmax lies in the structural set, else 0.
    Each verdict's agreement is averaged over SEEDS seeded runs per flip, then over the corpus.

    Control = the worker-system-counterpart triad [x[1], x[0]&x[2], x[1]] with labels (W, S, C):
    structural verdict triadic, max_phi 2.0, full {W, S, C} core, and the mediator S (node 1) is
    the coupling-centrality argmax at the natural flip.

    H1 is SUPPORTED if the fraction of forms whose triadic/dyadic verdict is correct at every
    swept flip exceeds 0.80 AND the bottleneck recovery rate drops by more than 20 points between
    its best and worst flip. H2 is SUPPORTED if the per-form optimal flip is not constant and its
    Spearman rank correlation with the form's intrinsic update entropy is non-zero in the
    predicted direction; otherwise NOT SUPPORTED.

    Intrinsic update entropy is the mean per-node Bernoulli entropy of the deterministic
    next-state output over the uniform state distribution — a flip-independent measure of how
    balanced the form's truth-table columns are.

    Determinism: every trajectory uses numpy.random.default_rng(seed) with a fixed seed loop, and
    the Φ library seeds its state search with numpy.random.default_rng(0). Re-runs reproduce byte
    for byte.

    Validation gap: exact IIT-4.0 Φ on small synthetic Boolean coordination forms. "Verdict",
    "membership", "bottleneck", "coupling centrality", and "update noise" name graph-and-Φ
    quantities, not measured organizations. In-silico scope; the Φ-to-organization bridge is open.
    The CRQA arm runs on synthetic trajectories, so every agreement rate is a baseline on
    synthetic data.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict
"""

import os
import sys
import math

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import new_big_phi, exceptions

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.recurrence.crqa import trajectory, coupling_centrality, coupling_matrix
from org_frontier.corpus.forms_library import FORMS as FORMS3
from org_frontier.multiparty import forms as mp

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

# ---- fixed configuration (all RNG seeded so the run reproduces byte-for-byte) -------------
TOL = 1e-6
SEEDS = 20                       # seeded trajectory runs per form per flip
STEPS = 400
WARMUP = 20
PROM_FLOOR = 0.05
MAX_LAG = 10
NATURAL_FLIP = 0.08              # the flip at which thresholds are calibrated
FLIPS = (0.02, 0.05, 0.08, 0.12, 0.18, 0.30)
SPREAD_THRESHOLD_N = {3: 4, 4: 7, 5: 9}   # spread cutoff per node count (triadic if >= cutoff)
H1_FORM_FRACTION = 0.80          # > this fraction of forms correct at every flip
H1_BOTTLENECK_DROP = 0.20        # bottleneck best-minus-worst must exceed this
H2_RHO_FLOOR = 0.30              # |Spearman| must clear this for entropy-tracking to count


# --------------------------------------------------------------------------------------
# Structural ground truth (fixed, flip-independent), read by exact IIT-4.0 Φ.
# --------------------------------------------------------------------------------------

def core_indices(rules, labels):
    """(core_index_tuple, phi) of the maximal complex, max over reachable states."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best = (None, -1.0)
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except (exceptions.StateUnreachableError, ValueError):
            continue
        if isinstance(mc, new_big_phi.NullPhiStructure):
            continue
        if float(mc.phi) > best[1]:
            best = (tuple(mc.node_indices), float(mc.phi))
    return best


def mc_phi(rules, labels):
    """Major-complex Φ over reachable states; 0.0 when no irreducible complex exists."""
    _, phi = major_complex(rules, labels)
    return float(phi) if phi is not None and phi > 0 else 0.0


def bottleneck_set(rules, labels):
    """Structural articulation node(s): the argmax of the leave-one-node-out drop in mc Φ."""
    base = mc_phi(rules, labels)
    drops = []
    for k in range(len(rules)):
        frozen = list(rules)
        frozen[k] = (lambda x: 0)
        drops.append(base - mc_phi(frozen, labels))
    mx = max(drops)
    if mx <= TOL:
        return set(), base, drops
    return {i for i, d in enumerate(drops) if abs(d - mx) <= TOL}, base, drops


def intrinsic_entropy(rules):
    """Mean per-node Bernoulli entropy of the deterministic next-state output over uniform states.

    A flip-independent property of the form: how balanced each node's truth-table column is. A
    constant node has entropy 0; a node that is 1 in exactly half the states has entropy 1.
    """
    tpm = tpm_from_rules(rules)
    n = tpm.shape[1]
    h = 0.0
    for j in range(n):
        p = float(tpm[:, j].mean())
        if 0.0 < p < 1.0:
            h += -(p * math.log2(p) + (1 - p) * math.log2(1 - p))
    return h / n


# --------------------------------------------------------------------------------------
# CRQA verdicts recomputed at a given flip from a seeded trajectory.
# --------------------------------------------------------------------------------------

def crqa_readings(rules, seed, flip):
    """(spread, centrality_vector) from one seeded trajectory at the given flip."""
    rng = np.random.default_rng(seed)
    traj = trajectory(rules, STEPS, rng, flip=flip, warmup=WARMUP)
    _, prom = coupling_matrix(traj, max_lag=MAX_LAG)
    mask = prom > PROM_FLOOR
    np.fill_diagonal(mask, False)
    spread = int(mask.sum())
    cc = coupling_centrality(traj, max_lag=MAX_LAG, prom_floor=PROM_FLOOR)
    return spread, cc


def triadic_call(spread, n):
    """CRQA triadic/dyadic call from the prominence spread against the per-n threshold."""
    return "triadic" if spread >= SPREAD_THRESHOLD_N[n] else "dyadic"


def membership_call(cc):
    """Per-node in-core call: centrality above the form's own median centrality."""
    thr = float(np.median(cc))
    return [1 if c > thr else 0 for c in cc]


# --------------------------------------------------------------------------------------
# Corpus assembly with fixed structural ground truth.
# --------------------------------------------------------------------------------------

def build_corpus():
    """List of dicts: key, rules, labels, n, td_label, member_vec, gt_bottleneck, intrinsic_H."""
    raw = [(f.key, f.rules, ("W", "S", "C")) for f in FORMS3]
    raw += [(f.key, f.rules, f.labels) for f in mp.FORMS]
    corpus = []
    for key, rules, labels in raw:
        ci, _phi = core_indices(rules, labels)
        size = len(ci) if ci else 0
        if size < 2:
            continue  # sub-dyadic: neither triadic nor dyadic, drop
        n = len(rules)
        td = "triadic" if size >= 3 else "dyadic"
        member = [1 if i in set(ci) else 0 for i in range(n)]
        bset, _base, _drops = bottleneck_set(rules, labels)
        corpus.append({
            "key": key, "rules": rules, "labels": labels, "n": n,
            "td": td, "member": member, "bottleneck": bset,
            "intrinsic_H": intrinsic_entropy(rules),
        })
    return corpus


# --------------------------------------------------------------------------------------
# Spearman rank correlation (exact, no scipy dependency).
# --------------------------------------------------------------------------------------

def spearman(a, b):
    """Spearman rank correlation between two equal-length sequences; nan if undefined."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if a.size < 2:
        return float("nan")

    def rankdata(x):
        order = np.argsort(x, kind="mergesort")
        ranks = np.empty(x.size, dtype=float)
        s = x[order]
        i = 0
        while i < s.size:
            j = i
            while j + 1 < s.size and s[j + 1] == s[i]:
                j += 1
            ranks[order[i:j + 1]] = (i + j) / 2.0 + 1.0
            i = j + 1
        return ranks

    ra, rb = rankdata(a), rankdata(b)
    if np.std(ra) < TOL or np.std(rb) < TOL:
        return float("nan")
    return float(np.corrcoef(ra, rb)[0, 1])


# --------------------------------------------------------------------------------------
# Instrument control.
# --------------------------------------------------------------------------------------

def control():
    """INSTRUMENT CONTROL: the faithful worker-system-counterpart triad reads structurally
    triadic with max_phi 2.0 and full {W, S, C} core, and the mediator S (node 1) is the
    coupling-centrality argmax at the natural flip."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = verdict(rules, labels)
    ci, phi = core_indices(rules, labels)
    _, cc = crqa_readings(rules, 0, NATURAL_FLIP)
    cc_pick = int(np.argmax(cc))
    ok = (v.structure == "triadic" and abs(v.max_phi - 2.0) < TOL
          and set(ci) == {0, 1, 2} and abs(phi - 2.0) < TOL and cc_pick == 1)
    print("CONTROL faithful triad: structure=%s max_phi=%.3f core=%s cc_pick=%d -> %s"
          % (v.structure, v.max_phi, str(ci), cc_pick, "PASS" if ok else "FAIL"), flush=True)
    if not ok:
        raise SystemExit("instrument control failed")


# --------------------------------------------------------------------------------------
# Main.
# --------------------------------------------------------------------------------------

def main():
    control()
    print("=" * 92, flush=True)
    print("q161 — noise-robust structural verdict (triadic/dyadic vs membership vs bottleneck)", flush=True)
    print("=" * 92, flush=True)

    corpus = build_corpus()
    n_tri = sum(1 for f in corpus if f["td"] == "triadic")
    print("corpus: %d forms (%d triadic, %d dyadic); flips swept: %s; %d seeds/form/flip"
          % (len(corpus), n_tri, len(corpus) - n_tri, str(FLIPS), SEEDS), flush=True)
    print("ground truth fixed by exact IIT-4.0 Φ; thresholds calibrated once at natural flip %.2f"
          % NATURAL_FLIP, flush=True)
    print(flush=True)

    # Per-flip corpus-mean agreement for each verdict, and per-form per-flip agreement records.
    td_by_flip = {}        # flip -> corpus-mean triadic/dyadic agreement
    mem_by_flip = {}       # flip -> corpus-mean membership agreement
    bot_by_flip = {}       # flip -> corpus-mean bottleneck recovery
    # per-form agreement averaged across the THREE verdicts, by flip, for H2 optimum.
    form_flip_agree = {f["key"]: {} for f in corpus}
    # per-form triadic/dyadic correctness across flips, for H1 "correct at every flip".
    form_td_allcorrect = {}

    for flip in FLIPS:
        td_vals, mem_vals, bot_vals = [], [], []
        for f in corpus:
            rules, labels, n = f["rules"], f["labels"], f["n"]
            td_hits = []
            mem_scores = []
            bot_hits = []
            for seed in range(SEEDS):
                spread, cc = crqa_readings(rules, seed, flip)
                td_call = triadic_call(spread, n)
                td_hits.append(1.0 if td_call == f["td"] else 0.0)
                mcall = membership_call(cc)
                mem_scores.append(np.mean([1.0 if mcall[i] == f["member"][i] else 0.0
                                           for i in range(n)]))
                pick = int(np.argmax(cc))
                bot_hits.append(1.0 if pick in f["bottleneck"] else 0.0)
            td_a = float(np.mean(td_hits))
            mem_a = float(np.mean(mem_scores))
            bot_a = float(np.mean(bot_hits))
            td_vals.append(td_a)
            mem_vals.append(mem_a)
            bot_vals.append(bot_a)
            form_flip_agree[f["key"]][flip] = (td_a + mem_a + bot_a) / 3.0
            form_td_allcorrect.setdefault(f["key"], []).append(td_a)
        td_by_flip[flip] = float(np.mean(td_vals))
        mem_by_flip[flip] = float(np.mean(mem_vals))
        bot_by_flip[flip] = float(np.mean(bot_vals))

    # ---- table: corpus-mean agreement by flip --------------------------------------------
    print("Corpus-mean verdict agreement vs flip (1.0 = always matches fixed exact-Φ ground truth)",
          flush=True)
    print("-" * 92, flush=True)
    header = "  %-10s" % "flip" + "".join("%10.2f" % fl for fl in FLIPS)
    print(header, flush=True)
    print("  %-10s" % "triad/dyad" + "".join("%10.3f" % td_by_flip[fl] for fl in FLIPS), flush=True)
    print("  %-10s" % "membership" + "".join("%10.3f" % mem_by_flip[fl] for fl in FLIPS), flush=True)
    print("  %-10s" % "bottleneck" + "".join("%10.3f" % bot_by_flip[fl] for fl in FLIPS), flush=True)
    print("-" * 92, flush=True)

    # spread = best-minus-worst across flips, per verdict
    td_spread = max(td_by_flip.values()) - min(td_by_flip.values())
    mem_spread = max(mem_by_flip.values()) - min(mem_by_flip.values())
    bot_spread = max(bot_by_flip.values()) - min(bot_by_flip.values())
    print("  best-minus-worst across flip:  triad/dyad %.3f   membership %.3f   bottleneck %.3f"
          % (td_spread, mem_spread, bot_spread), flush=True)

    # fraction of forms whose triadic/dyadic call is correct (>= 0.5 seed-majority) at EVERY flip
    n_allcorrect = 0
    for key, vals in form_td_allcorrect.items():
        if all(v >= 0.5 for v in vals):
            n_allcorrect += 1
    frac_allcorrect = n_allcorrect / len(corpus)
    bot_best = max(bot_by_flip.values())
    bot_worst = min(bot_by_flip.values())
    bot_drop = bot_best - bot_worst
    print(flush=True)
    print("triadic/dyadic correct (seed-majority) at EVERY swept flip: %d/%d forms = %.3f"
          % (n_allcorrect, len(corpus), frac_allcorrect), flush=True)
    print("bottleneck recovery best=%.3f worst=%.3f drop=%.3f"
          % (bot_best, bot_worst, bot_drop), flush=True)
    print(flush=True)

    # ---- H2: per-form optimal flip and its correlation with intrinsic entropy ------------
    print("Per-form optimal flip (argmax mean three-verdict agreement) vs intrinsic update entropy",
          flush=True)
    print("-" * 92, flush=True)
    print("  %-26s %-10s %-12s %-10s" % ("form", "opt_flip", "best_agree", "intrinsic_H"), flush=True)
    opt_flips, entropies = [], []
    for f in corpus:
        agr = form_flip_agree[f["key"]]
        best_flip = max(FLIPS, key=lambda fl: agr[fl])
        opt_flips.append(best_flip)
        entropies.append(f["intrinsic_H"])
        print("  %-26s %-10.2f %-12.3f %-10.4f"
              % (f["key"], best_flip, agr[best_flip], f["intrinsic_H"]), flush=True)
    print("-" * 92, flush=True)
    distinct_opt = sorted(set(opt_flips))
    rho = spearman(entropies, opt_flips)
    print("distinct optimal flips across forms: %s" % str(distinct_opt), flush=True)
    print("Spearman(intrinsic_H, optimal_flip) = %s"
          % ("%.3f" % rho if not math.isnan(rho) else "nan"), flush=True)
    print(flush=True)

    # ---- Verdicts ------------------------------------------------------------------------
    h1_td = frac_allcorrect > H1_FORM_FRACTION
    h1_bot = bot_drop > H1_BOTTLENECK_DROP
    h1 = h1_td and h1_bot
    print("H1 (triad/dyad robust > %.0f%% of forms AND bottleneck degrades > %d pts): %s"
          % (100 * H1_FORM_FRACTION, int(100 * H1_BOTTLENECK_DROP),
             "SUPPORTED" if h1 else "REFUTED"), flush=True)
    print("    triad/dyad correct-at-every-flip fraction %.3f (> %.2f: %s); "
          "bottleneck drop %.3f (> %.2f: %s)"
          % (frac_allcorrect, H1_FORM_FRACTION, h1_td, bot_drop, H1_BOTTLENECK_DROP, h1_bot),
          flush=True)

    # H2: optima must vary AND track entropy in the predicted (positive) direction, with the
    # rank correlation clearing a meaningful floor. A weak or wrong-signed rho is NOT SUPPORTED.
    not_constant = len(distinct_opt) > 1
    h2 = not_constant and (not math.isnan(rho)) and rho > H2_RHO_FLOOR
    print("H2 (per-form optimal flip varies AND tracks intrinsic update entropy): %s"
          % ("SUPPORTED" if h2 else "NOT SUPPORTED"), flush=True)
    print("    optima vary across forms: %s (%d distinct); Spearman vs entropy = %s "
          "(needs > %.2f in the positive direction)"
          % (not_constant, len(distinct_opt),
             "%.3f" % rho if not math.isnan(rho) else "nan", H2_RHO_FLOOR), flush=True)


if __name__ == "__main__":
    main()
