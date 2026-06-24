"""Per-worker Φ-based coordination measure for the simulated algorithmacy cohort.

The survey arm fields an Algorithmacy Competence Scale (ACS) and several coordination scales:
perceived task interdependence (TI), perceived system authority commit-vs-convey (SA), and
perceived substitutability (SU). The classifier line treats a coordination form as a small
W-S-C Boolean dynamical system and reads its irreducibility with exact IIT-4.0 Φ over the MIP.
This module bridges the two: it maps each simulated worker's coordination row to a W-S-C form
and computes a per-worker Φ_coord (the form's max Φ_MIP), so a Φ-based measure can be regressed
on the latent algorithmacy construct.

The map (one worker, one form):

  - Worker W reads the system S:                      W' = S
  - Counterpart C reads the system S:                 C' = S
  - System S commits a joint determination of W and C when the worker reports a binding,
    interdependent, non-substitutable coordination, and otherwise conveys a single party's
    signal (a pass-through that factors along party lines):
        commit:  S' = W AND C        (irreducible: neither party alone fixes S)
        convey:  S' = W              (factors: {W,S} | {C}, Φ_MIP = 0)

Three reported conditions gate the commit form. A worker's form commits iff all three hold:
  - interdependence high     (TI  >= TI_THRESH):  the two parties' work is reciprocally coupled,
  - system commits           (SA  >= SA_THRESH):  the gate determines rather than relays,
  - worker is pivotal        (SU  <  SU_THRESH):  the worker is not freely substitutable.
Otherwise the form conveys and Φ_coord is 0 by construction.

Φ_coord is the form's max exact Φ_MIP over reachable states (probes.lib.max_phi_float on the
TPM from classifier.tpm_from_rules). The commit form is the faithful mediated triad up to a
relabelling and carries Φ_coord = 2.0; the convey form factors and carries Φ_coord = 0.0.

CONTROL rewiring: the forced-dyadic cohort replaces every worker's S rule with a pass-through
(S' = W) regardless of the reported conditions, so Φ_coord is identically 0 across the cohort.
A surviving Φ_coord-to-ACS association in the bridge cohort that vanishes in the control shows
the association rides on irreducibility, not on a shared scale artifact.

Scope: the cohort here is SIMULATED. No worker is measured. Φ_coord is a structural property of
the Boolean form a worker's reported conditions map to, read by the exact-Φ instrument. The
construct association is evidence about the instrument and the bridge on synthetic data.

Reuses: classifier.tpm_from_rules, probes.lib.max_phi_float, the cohort simulation in analysis.py.
"""

import re

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import max_phi_float

LABELS = ("W", "S", "C")

# Midpoint of the 7-point agreement scale gates commit-vs-convey; the SU threshold sits at the
# midpoint so reporting "more substitutable than not" removes pivotality.
TI_THRESH = 4.5
SA_THRESH = 4.5
SU_THRESH = 4.0


def worker_rules(ti, sa_commit, su, control=False):
    """W-S-C Boolean rules for one worker's reported coordination row.

    ``control=True`` forces the dyadic pass-through (S' = W) so the form factors and Φ_coord = 0,
    regardless of the reported conditions.
    """
    w_rule = lambda x: x[1]          # W reads S
    c_rule = lambda x: x[1]          # C reads S
    commit = (ti >= TI_THRESH) and (sa_commit >= SA_THRESH) and (su < SU_THRESH)
    if control or not commit:
        s_rule = lambda x: x[0]      # S conveys W: factors {W,S}|{C}
    else:
        s_rule = lambda x: x[0] & x[2]  # S commits AND(W,C): irreducible mediated triad
    return [w_rule, s_rule, c_rule]


# Φ_coord depends only on which of the two distinct forms a worker maps to, so it is memoised on
# the form to keep the cohort sweep cheap and exactly deterministic.
_PHI_CACHE = {}


def phi_coord(ti, sa_commit, su, control=False):
    """Per-worker Φ_coord: max exact Φ_MIP over the worker's W-S-C form."""
    commit = (not control) and (ti >= TI_THRESH) and (sa_commit >= SA_THRESH) and (su < SU_THRESH)
    key = bool(commit)
    if key not in _PHI_CACHE:
        rules = [lambda x: x[1],
                 (lambda x: x[0] & x[2]) if key else (lambda x: x[0]),
                 lambda x: x[1]]
        tpm = tpm_from_rules(rules)
        mx, _ = max_phi_float(tpm)
        _PHI_CACHE[key] = float(mx)
    return _PHI_CACHE[key]


def simulate_cohort(n, rng):
    """A simulated cohort row per worker: reported coordination scales, an ACS-total factor score,
    and the bridge/control Φ_coord.

    The reported conditions (TI, SA-commit, SU) load on a single latent coordination factor, and
    the ACS-total factor score loads on the same latent plus noise, so a worker whose form is
    irreducible tends to score higher on algorithmacy. The association is built into the synthetic
    data on purpose; the bridge recovers it through the Φ instrument.
    """
    # latent coordination capability; higher = more interdependent/committing/pivotal coordination
    z = rng.normal(0, 1, n)
    ti = np.clip(np.round(4.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    sa = np.clip(np.round(4.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    # substitutability runs opposite to the latent: capable coordinators are less substitutable
    su = np.clip(np.round(4.0 - 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    # ACS-total factor score: the same latent plus independent noise (a standardized factor score)
    acs_raw = 0.7 * z + rng.normal(0, 0.7, n)
    acs_total = (acs_raw - acs_raw.mean()) / acs_raw.std(ddof=1)

    phi_bridge = np.array([phi_coord(ti[i], sa[i], su[i], control=False) for i in range(n)])
    phi_control = np.array([phi_coord(ti[i], sa[i], su[i], control=True) for i in range(n)])
    return {
        "ti": ti, "sa": sa, "su": su,
        "acs_total": acs_total,
        "phi_bridge": phi_bridge,
        "phi_control": phi_control,
    }


def simulate_cohort_full(n, rng):
    """A richer simulated cohort that adds two nuisance constructs for discriminant-validity tests:
    general self-efficacy (SE) and belonging (BE).

    Same coordination latent ``z`` as ``simulate_cohort`` drives the reported conditions (TI, SA, SU)
    and the Φ_coord map. ACS-total loads on ``z`` (algorithmacy tracks coordination capability). SE is
    a generic-competence latent: it shares variance with ACS through a common-competence component but
    runs partly on its own, so SE correlates with ACS yet is not the algorithmacy-specific signal. BE
    is belonging, weakly tied to competence. The Φ instrument should carry association with ACS that
    survives partialling SE and BE (H1), and should track ACS more tightly than SE (H2).
    """
    # coordination latent driving the W-S-C form (as in simulate_cohort)
    z = rng.normal(0, 1, n)
    ti = np.clip(np.round(4.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    sa = np.clip(np.round(4.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    su = np.clip(np.round(4.0 - 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)

    # generic-competence latent g: shared by ACS and SE, independent of the coordination latent z
    g = rng.normal(0, 1, n)
    # belonging latent b: mostly its own, with a light competence tie
    b = rng.normal(0, 1, n)

    # ACS-total loads on the coordination latent z (the algorithmacy-specific signal) and on generic
    # competence g; Φ_coord (a function of z) is the part SE does not reach.
    acs_raw = 0.7 * z + 0.4 * g + rng.normal(0, 0.6, n)
    # SE loads on generic competence g and only lightly on z, so SE is competence, not coordination.
    se_raw = 0.8 * g + 0.2 * z + rng.normal(0, 0.6, n)
    # belonging loads on its own latent b plus a light competence tie.
    be_raw = 0.8 * b + 0.3 * g + rng.normal(0, 0.6, n)

    def zscore(v):
        return (v - v.mean()) / v.std(ddof=1)

    acs_total = zscore(acs_raw)
    se = zscore(se_raw)
    be = zscore(be_raw)

    phi_bridge = np.array([phi_coord(ti[i], sa[i], su[i], control=False) for i in range(n)])
    phi_control = np.array([phi_coord(ti[i], sa[i], su[i], control=True) for i in range(n)])
    return {
        "ti": ti, "sa": sa, "su": su,
        "acs_total": acs_total, "se": se, "be": be,
        "phi_bridge": phi_bridge, "phi_control": phi_control,
    }


def simulate_commit_convey_cohorts(n, rng):
    """Two simulated cohorts for the commit-vs-convey moderation study (q196).

    Commit cohort: SA-commit varies over the full scale, so a worker who reports a high-commit,
    interdependent, non-substitutable coordination maps to the irreducible AND(W,C) form
    (Φ_coord = 2.0) and a worker who reports convey maps to the pass-through (Φ_coord = 0). The
    ACS-total factor score is generated so the Φ_coord-to-ACS link is concentrated where the system
    commits: ACS loads on Φ_coord only through an interaction with SA-commit. A worker whose form is
    irreducible and who reports a committing system scores higher; an irreducible form under a low
    reported commit carries no ACS lift.

    Convey cohort (control): SA-commit is floored below SA_THRESH for every worker, so no form can
    commit. Φ_coord is identically 0, and any Φ_coord-to-ACS slope is flat by construction.

    Returns a dict keyed by arm ("commit", "convey") of per-cohort arrays.
    """
    out = {}
    for arm in ("commit", "convey"):
        z = rng.normal(0, 1, n)
        ti = np.clip(np.round(4.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
        if arm == "commit":
            sa = np.clip(np.round(4.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
        else:
            # convey-floored: SA capped below the commit threshold so every form stays dyadic
            sa = np.clip(np.round(2.0 + 0.5 * z + rng.normal(0, 0.6, n)), 1, SA_THRESH - 0.5)
        su = np.clip(np.round(4.0 - 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)

        phi = np.array([phi_coord(ti[i], sa[i], su[i], control=False) for i in range(n)])
        sd_sa = sa.std(ddof=1)
        sa_z = (sa - sa.mean()) / (sd_sa if sd_sa > 1e-9 else 1.0)
        phi_s = phi / 2.0  # 0/1 indicator of the irreducible form

        # ACS-total: Φ_coord predicts ACS only through the interaction with reported commit. The
        # main Φ effect is null; the lift appears for irreducible-and-committing workers.
        latent = 0.4 * z
        interaction_signal = 0.9 * phi_s * sa_z
        acs_raw = latent + interaction_signal + rng.normal(0, 0.7, n)
        acs_total = (acs_raw - acs_raw.mean()) / acs_raw.std(ddof=1)

        out[arm] = {
            "ti": ti, "sa": sa, "su": su, "sa_z": sa_z,
            "phi": phi, "phi_s": phi_s, "acs_total": acs_total,
        }
    return out


def simulate_substitutability_cohorts(n, rng):
    """Two simulated cohorts for the substitutability/displacement-capture study (q201).

    The displacement prediction: a worker whose role admits an interchangeable copy sits in a more
    factorizable coordination form. When perceived substitutability (SU) is high, a substitutable
    copy relays the worker's signal and the system no longer needs the worker as one of two parties
    it cannot reduce, so the form factors and Phi_coord drops to 0. When SU is low the worker is
    pivotal: the system commits a joint determination of worker and counterpart that neither fixes
    alone (AND(W,C)), the irreducible mediated triad, Phi_coord = 2.0.

    Bridge cohort: SU varies over the full scale and gates the W-node's duplicability. A high-SU row
    (SU >= SU_THRESH) maps to the convey pass-through (Phi_coord = 0); a low-SU, interdependent,
    committing row maps to AND(W,C) (Phi_coord = 2.0). ACS-total loads on the coordination latent z,
    and the lower Phi_coord that high SU induces is the structural channel SU runs through: SU lowers
    Phi_coord and the lower Phi_coord tracks lower ACS (the capture path SU -> Phi_coord -> ACS).

    Control cohort (pivotal-W): every worker is held pivotal, so substitutability cannot factor the
    form. Phi_coord is read on a forced-low SU (the worker is never duplicable here), so Phi_coord is
    near-constant and the SU -> Phi_coord slope is flat. SU still varies as a reported scale, but it
    no longer reaches the form, so no SU -> Phi_coord -> ACS path can open.

    Returns a dict keyed by arm ("bridge", "control") of per-cohort arrays.
    """
    out = {}
    for arm in ("bridge", "control"):
        # coordination latent: capable coordinators report more interdependence/commit and lower
        # substitutability. SU runs opposite the latent.
        z = rng.normal(0, 1, n)
        ti = np.clip(np.round(5.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
        sa = np.clip(np.round(5.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
        su = np.clip(np.round(4.0 - 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)

        if arm == "bridge":
            # SU gates the form: a substitutable worker (high SU) factors the coordination.
            phi = np.array([phi_coord(ti[i], sa[i], su[i], control=False) for i in range(n)])
        else:
            # pivotal-W control: every worker is held pivotal AND committing, so substitutability
            # cannot factor the form. The reported conditions are forced past every threshold, so
            # Phi_coord is the irreducible AND(W,C) value (2.0) for every worker and is constant. SU
            # still varies as a reported scale but never reaches the form, so its Phi slope is flat.
            phi = np.array([phi_coord(7.0, 7.0, 1.0, control=False) for _ in range(n)])

        sd_su = su.std(ddof=1)
        su_z = (su - su.mean()) / (sd_su if sd_su > 1e-9 else 1.0)
        phi_s = phi / 2.0  # 0/1 indicator of the irreducible form

        # ACS-total rides predominantly on Phi_coord (the irreducible form), which high SU drives
        # down in the bridge arm. A small coordination-latent residual leaves a thin direct SU -> ACS
        # path, so the capture thesis is encoded: most of SU's reach into ACS runs through Phi_coord
        # (indirect path dominant), with a minor direct leg that does not pass through the form.
        acs_raw = 0.12 * z + 0.85 * phi_s + rng.normal(0, 0.7, n)
        acs_total = (acs_raw - acs_raw.mean()) / acs_raw.std(ddof=1)

        out[arm] = {
            "ti": ti, "sa": sa, "su": su, "su_z": su_z,
            "phi": phi, "phi_s": phi_s, "acs_total": acs_total,
        }
    return out


def ols_with_ci(X, y, alpha=0.05):
    """Ordinary least squares for a design matrix ``X`` (n x p, includes the intercept column) with
    Normal-theory (1 - alpha) confidence intervals on each coefficient.

    Returns (beta, lo, hi, se). The critical value is the Normal quantile (n is large), so no SciPy
    dependency is needed.
    """
    X = np.asarray(X, float)
    y = np.asarray(y, float)
    n, p = X.shape
    XtX_inv = np.linalg.inv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    resid = y - X @ beta
    dof = n - p
    sigma2 = float(resid @ resid) / dof
    cov = sigma2 * XtX_inv
    se = np.sqrt(np.diag(cov))
    zcrit = 1.959963984540054
    lo = beta - zcrit * se
    hi = beta + zcrit * se
    return beta, lo, hi, se


def partial_corr(x, y, covars, alpha=0.05):
    """Partial Pearson correlation of x and y controlling for the columns of ``covars``.

    Residualizes x and y on [1, covars] by least squares, then correlates the residuals. Returns
    (partial_r, lo, hi) with a Fisher-z interval whose df is reduced by the number of controls.
    If a residual vector is constant, returns zeros.
    """
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    C = np.asarray(covars, float)
    if C.ndim == 1:
        C = C[:, None]
    n = len(x)
    k = C.shape[1]
    design = np.column_stack([np.ones(n), C])

    def resid(v):
        beta, *_ = np.linalg.lstsq(design, v, rcond=None)
        return v - design @ beta

    rx = resid(x)
    ry = resid(y)
    if np.std(rx) < 1e-12 or np.std(ry) < 1e-12:
        return 0.0, 0.0, 0.0
    r = float(np.corrcoef(rx, ry)[0, 1])
    r = max(min(r, 1 - 1e-12), -1 + 1e-12)
    zr = np.arctanh(r)
    # df reduced by the number of partialled covariates
    se = 1.0 / np.sqrt(n - 3 - k)
    zcrit = 1.959963984540054
    lo = np.tanh(zr - zcrit * se)
    hi = np.tanh(zr + zcrit * se)
    return r, float(lo), float(hi)


def steiger_diff(x, y1, y2, n_boot=5000, seed=0, alpha=0.05):
    """Bootstrap CI for the difference r(x,y1) - r(x,y2) on the same sample (dependent, overlapping).

    Resamples rows with replacement (fixed seed) and returns
    (delta, lo, hi, r_xy1, r_xy2) with a percentile (1 - alpha) interval on the difference.
    """
    x = np.asarray(x, float)
    y1 = np.asarray(y1, float)
    y2 = np.asarray(y2, float)
    n = len(x)

    def corr(a, b):
        if np.std(a) < 1e-12 or np.std(b) < 1e-12:
            return 0.0
        return float(np.corrcoef(a, b)[0, 1])

    r_xy1 = corr(x, y1)
    r_xy2 = corr(x, y2)
    delta = r_xy1 - r_xy2

    rng = np.random.default_rng(seed)
    deltas = np.empty(n_boot)
    for k in range(n_boot):
        idx = rng.integers(0, n, n)
        deltas[k] = corr(x[idx], y1[idx]) - corr(x[idx], y2[idx])
    lo = float(np.quantile(deltas, alpha / 2))
    hi = float(np.quantile(deltas, 1 - alpha / 2))
    return delta, lo, hi, r_xy1, r_xy2


def bootstrap_mediation(treat, mediator, outcome, n_boot=5000, seed=0, alpha=0.05):
    """Bootstrap a single-mediator path: treat -> mediator -> outcome, controlling nothing else.

    Standardizes treat, mediator, outcome to unit variance, then fits
        mediator ~ 1 + treat                     (path a)
        outcome  ~ 1 + treat + mediator          (paths c' direct, b)
    The indirect (mediated) effect is a*b; the direct effect is c'. Returns a dict with point
    estimates and percentile (1 - alpha) bootstrap CIs for a, b, indirect (a*b), and direct (c').
    Row-resamples with a fixed seed so the interval reproduces exactly on re-run.
    """
    t = np.asarray(treat, float)
    m = np.asarray(mediator, float)
    y = np.asarray(outcome, float)
    n = len(t)

    def zz(v):
        sd = v.std(ddof=1)
        return (v - v.mean()) / (sd if sd > 1e-9 else 1.0)

    def fit(ti, mi, yi):
        ti, mi, yi = zz(ti), zz(mi), zz(yi)
        # path a: mi ~ 1 + ti
        Xa = np.column_stack([np.ones(len(ti)), ti])
        a = float(np.linalg.lstsq(Xa, mi, rcond=None)[0][1])
        # paths b, c': yi ~ 1 + ti + mi
        Xb = np.column_stack([np.ones(len(ti)), ti, mi])
        coef = np.linalg.lstsq(Xb, yi, rcond=None)[0]
        cprime = float(coef[1])
        b = float(coef[2])
        return a, b, a * b, cprime

    a0, b0, ind0, dir0 = fit(t, m, y)
    rng = np.random.default_rng(seed)
    A = np.empty(n_boot); B = np.empty(n_boot); IND = np.empty(n_boot); DIR = np.empty(n_boot)
    for k in range(n_boot):
        idx = rng.integers(0, n, n)
        A[k], B[k], IND[k], DIR[k] = fit(t[idx], m[idx], y[idx])
    q = [alpha / 2 * 100, (1 - alpha / 2) * 100]

    def ci(arr):
        lo, hi = np.percentile(arr, q)
        return float(lo), float(hi)

    return {
        "a": a0, "a_ci": ci(A),
        "b": b0, "b_ci": ci(B),
        "indirect": ind0, "indirect_ci": ci(IND),
        "direct": dir0, "direct_ci": ci(DIR),
    }


def pearson_ci(x, y, alpha=0.05):
    """Pearson r and a Fisher-z (1 - alpha) confidence interval. Returns (r, lo, hi).

    If either vector is constant (no variance), r and the interval are 0 by convention.
    """
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    if np.std(x) < 1e-12 or np.std(y) < 1e-12:
        return 0.0, 0.0, 0.0
    r = float(np.corrcoef(x, y)[0, 1])
    r = max(min(r, 1 - 1e-12), -1 + 1e-12)
    zr = np.arctanh(r)
    se = 1.0 / np.sqrt(n - 3)
    # 95% normal quantile, hard-coded so no SciPy dependency is needed
    zcrit = 1.959963984540054
    lo = np.tanh(zr - zcrit * se)
    hi = np.tanh(zr + zcrit * se)
    return r, float(lo), float(hi)


# ----------------------------------------------------------------------------------------
# Partition-restricted Φ: the counterpart (W-C) component
# ----------------------------------------------------------------------------------------
#
# Whole-system Φ_coord reads how irreducible a worker's W-S-C form is overall. A facet-specific
# question needs a finer reading: how much of that irreducibility runs through the worker-
# counterpart (W-C) relation specifically, as opposed to being mediated entirely through the
# system gate S. The survey_bridge map ties counterpart inference (ACS-CI) to a hidden counterpart
# behind a committing third party, so the prediction is that ACS-CI tracks the W-C-restricted
# component above and beyond whole-system Φ.
#
# The W-C component is read with exact IIT-4.0 machinery: at each reachable state, evaluate every
# system partition that places W and C in different blocks (a cut that severs the worker-counterpart
# relation), take the least informative such cut (the partition-restricted analogue of the MIP),
# and take the max over states. The whole-system Φ is the max over states of the global MIP value.

_PHI_PROFILE_CACHE = {}


def _wc_separated(part):
    """True iff a SystemPartition places W and C in different blocks (severs the W-C relation)."""
    head = str(part).splitlines()[0]
    inside = re.findall(r"\{([^}]*)\}", head)[0]
    blocks = inside.split(",")
    wi = ci = None
    for bi, b in enumerate(blocks):
        if "W" in b:
            wi = bi
        if "C" in b:
            ci = bi
    return wi is not None and ci is not None and wi != ci


def phi_whole_and_wc(rules, labels=LABELS):
    """Exact (Φ_whole, Φ_WC) for a W-S-C Boolean form.

    Φ_whole is the max over reachable states of the global Φ_MIP. Φ_WC is the max over reachable
    states of the least-informative W-C-separating cut at that state (the partition-restricted
    irreducibility attributable to the worker-counterpart relation). Memoised on the form's TPM.
    """
    import pyphi
    from pyphi import new_big_phi
    from foundations.proxy_audit.exact_phi import reachable_states

    tpm = tpm_from_rules(rules)
    cm = cm_from_rules(rules)
    key = tpm.tobytes()
    if key in _PHI_PROFILE_CACHE:
        return _PHI_PROFILE_CACHE[key]

    n = len(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels[:n])
    phi_whole = 0.0
    phi_wc = 0.0
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            sub = pyphi.Subsystem(net, state)
        except Exception:
            continue
        sia = new_big_phi.sia(sub)
        phi_whole = max(phi_whole, float(sia.phi))
        try:
            wc_phis = [
                float(new_big_phi.evaluate_partition(p, sub, sia.system_state).phi)
                for p in new_big_phi.system_partitions(sub.node_indices, node_labels=net.node_labels)
                if _wc_separated(p)
            ]
            if wc_phis:
                phi_wc = max(phi_wc, min(wc_phis))
        except Exception:
            pass
    out = (float(phi_whole), float(phi_wc))
    _PHI_PROFILE_CACHE[key] = out
    return out


def coordination_form(commit, coupled):
    """W-S-C Boolean rules keyed on two reported conditions.

    ``commit``  (TI/SA high, SU low): the system commits a joint determination rather than conveying
                a single party's signal.
    ``coupled`` (counterpart coupling): the counterpart C reads the worker directly, so the
                irreducibility runs through the W-C relation; otherwise C reads only the gate S and
                the counterpart sits hidden behind it.

    Φ readings (exact, deterministic):
      commit=0            -> convey pass-through, Φ_whole = 0, Φ_WC = 0
      commit=1, coupled=0 -> mediated AND gate, Φ_whole = 2.0, Φ_WC = 1.0 (W-C fraction 0.5)
      commit=1, coupled=1 -> counterpart-coupled, Φ_whole = 1.0, Φ_WC = 1.0 (W-C fraction 1.0)
    """
    if not commit:
        return [lambda x: x[1], lambda x: x[0], lambda x: x[1]]            # convey
    if coupled:
        return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[0] & x[1]]  # C reads W&S
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]         # mediated, C hidden


def simulate_facet_cohort(n, rng):
    """Simulated facet-specific cohort for the facet-specificity study (q194).

    Two binary coordination conditions drive each worker's W-S-C form:
      - ``commit``  from the coordination latent z (interdependent, committing, non-substitutable),
      - ``coupled`` from a counterpart-coupling latent c (whether C reads the worker directly).

    Each worker carries whole-system Φ (Φ_whole) and the W-C-restricted component (Φ_WC), read by
    the exact instrument from the worker's form. The three ACS facets and the discriminant covariate
    are generated to a facet-to-structure map drawn from survey_bridge:

      - ACS-CI  (counterpart inference) loads on the W-C component Φ_WC: it is the skill against a
        hidden counterpart, so it tracks irreducibility through the worker-counterpart relation.
      - ACS-SC  (signal compression) and ACS-RT (rule-change tracking) load on whole-system Φ
        through the committing gate, not on the W-C relation specifically.
      - SE      (general self-efficacy) loads on a generic-competence latent g, independent of the
        coordination structure: the discriminant covariate.

    The map is built into the synthetic data on purpose; the study tests whether the partition-
    restricted instrument recovers the facet-differential the map predicts. All on synthetic data.
    """
    # coordination latent -> commit gate. The scale midpoints are shifted up so roughly half the
    # cohort reports a committing coordination, populating both committing forms (mediated and
    # counterpart-coupled) well enough to decouple Φ_whole from Φ_WC.
    z = rng.normal(0, 1, n)
    ti = np.clip(np.round(5.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    sa = np.clip(np.round(5.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    su = np.clip(np.round(3.0 - 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    commit = (ti >= TI_THRESH) & (sa >= SA_THRESH) & (su < SU_THRESH)

    # counterpart-coupling latent -> coupled flag (independent of z so Φ_WC is not collinear with z)
    cc = rng.normal(0, 1, n)
    coupled = cc > 0.0

    # exact Φ readings per worker (memoised on the form, four distinct forms)
    phi_whole = np.empty(n)
    phi_wc = np.empty(n)
    for i in range(n):
        pw, pwc = phi_whole_and_wc(coordination_form(bool(commit[i]), bool(coupled[i])))
        phi_whole[i] = pw
        phi_wc[i] = pwc

    # generic-competence latent for the discriminant covariate
    g = rng.normal(0, 1, n)

    def zscore(v):
        sd = v.std(ddof=1)
        return (v - v.mean()) / (sd if sd > 1e-9 else 1.0)

    phi_whole_z = zscore(phi_whole)
    phi_wc_z = zscore(phi_wc)

    # ACS-CI loads on the W-C component (and lightly on z); the counterpart-specific facet.
    ci_raw = 0.85 * phi_wc_z + 0.15 * z + rng.normal(0, 0.55, n)
    # ACS-SC and ACS-RT load on whole-system Φ, not the W-C relation.
    sc_raw = 0.75 * phi_whole_z + 0.20 * z + rng.normal(0, 0.55, n)
    rt_raw = 0.70 * phi_whole_z + 0.20 * z + rng.normal(0, 0.55, n)
    # SE loads on generic competence g only: the discriminant covariate.
    se_raw = 0.85 * g + rng.normal(0, 0.55, n)

    return {
        "ti": ti, "sa": sa, "su": su,
        "commit": commit.astype(int), "coupled": coupled.astype(int),
        "phi_whole": phi_whole, "phi_wc": phi_wc,
        "acs_ci": zscore(ci_raw),
        "acs_sc": zscore(sc_raw),
        "acs_rt": zscore(rt_raw),
        "se": zscore(se_raw),
    }


def simulate_panel(n_persons, n_waves, rng):
    """A simulated longitudinal panel: ``n_waves`` rows per person, in long format.

    Each person carries a stable coordination trait ``u_i`` (between-person standing). Each wave adds a
    within-person, time-varying coordination state ``v_it`` (state fluctuation around the person's own
    mean). The reported conditions (TI, SA-commit, SU) -- and therefore the Phi_coord map -- respond to
    the person's current total coordination ``u_i + v_it``, so a person's Phi_coord moves wave to wave as
    the state fluctuates. ACS-total loads on the same current total coordination plus independent noise,
    so a wave where a person's coordination rises (raising the chance the form commits and Phi_coord
    jumps to 2.0) is also a wave where that person's ACS rises. The within-person coupling is built into
    the panel on purpose; the bridge recovers it through the Phi instrument after person-mean centering.

    Returns a dict of long-format arrays of length ``n_persons * n_waves``:
      person (int id), wave (1..n_waves), ti, sa, su, acs_total, phi_bridge, phi_control.
    """
    rows_person, rows_wave = [], []
    rows_ti, rows_sa, rows_su = [], [], []
    rows_acs, rows_phi_b, rows_phi_c = [], [], []

    # ACS loads more on the within-person state v than on the stable trait u: algorithmacy moves with a
    # person's current coordination state (a person-level dynamic), beyond stable between-person selection.
    W_WITHIN, W_BETWEEN = 1.1, 0.20
    u = rng.normal(0, 1, n_persons)  # between-person stable coordination standing
    for i in range(n_persons):
        for t in range(n_waves):
            v = rng.normal(0, 1.0)  # within-person, time-varying coordination state
            total = u[i] + v
            ti = float(np.clip(np.round(4.0 + 0.9 * total + rng.normal(0, 0.6)), 1, 7))
            sa = float(np.clip(np.round(4.0 + 0.9 * total + rng.normal(0, 0.6)), 1, 7))
            su = float(np.clip(np.round(4.0 - 0.9 * total + rng.normal(0, 0.6)), 1, 7))
            acs = W_BETWEEN * u[i] + W_WITHIN * v + rng.normal(0, 0.7)
            rows_person.append(i)
            rows_wave.append(t + 1)
            rows_ti.append(ti)
            rows_sa.append(sa)
            rows_su.append(su)
            rows_acs.append(acs)
            rows_phi_b.append(phi_coord(ti, sa, su, control=False))
            rows_phi_c.append(phi_coord(ti, sa, su, control=True))

    acs_arr = np.asarray(rows_acs, float)
    acs_arr = (acs_arr - acs_arr.mean()) / acs_arr.std(ddof=1)  # standardized factor score
    return {
        "person": np.asarray(rows_person, int),
        "wave": np.asarray(rows_wave, int),
        "ti": np.asarray(rows_ti, float),
        "sa": np.asarray(rows_sa, float),
        "su": np.asarray(rows_su, float),
        "acs_total": acs_arr,
        "phi_bridge": np.asarray(rows_phi_b, float),
        "phi_control": np.asarray(rows_phi_c, float),
    }


def person_center(values, person):
    """Split ``values`` into between-person means (per row) and within-person deviations.

    Returns (between, within): ``between`` is each row's person mean, ``within`` is the row value minus
    that person mean. Person-mean centering separates a stable between-person component from a
    wave-to-wave within-person component.
    """
    values = np.asarray(values, float)
    person = np.asarray(person, int)
    between = np.empty_like(values)
    within = np.empty_like(values)
    for pid in np.unique(person):
        m = person == pid
        pm = values[m].mean()
        between[m] = pm
        within[m] = values[m] - pm
    return between, within


def within_between_slopes(phi, acs, person, n_boot=5000, seed=0, alpha=0.05):
    """Multilevel within- and between-person slopes of ACS on Phi_coord, via person-mean centering.

    Person-mean-centers Phi_coord into a within-person deviation and a between-person mean, then
    regresses ACS on [1, within_phi, between_phi]. The within coefficient is the within-person slope; the
    between coefficient is the between-person slope. Confidence intervals come from a person-level cluster
    bootstrap (resample whole persons with replacement, fixed seed), so the dependence among a person's
    repeated waves is respected. Returns
    (b_within, bw_lo, bw_hi, b_between, bb_lo, bb_hi, b_diff, bd_lo, bd_hi) with b_diff = within - between.
    """
    phi = np.asarray(phi, float)
    acs = np.asarray(acs, float)
    person = np.asarray(person, int)

    def fit(phi_v, acs_v, person_v):
        between, within = person_center(phi_v, person_v)
        D = np.column_stack([np.ones(len(acs_v)), within, between])
        beta, *_ = np.linalg.lstsq(D, acs_v, rcond=None)
        return float(beta[1]), float(beta[2])

    b_within, b_between = fit(phi, acs, person)
    b_diff = b_within - b_between

    persons = np.unique(person)
    rows_by_person = {pid: np.where(person == pid)[0] for pid in persons}

    rng = np.random.default_rng(seed)
    bw = np.empty(n_boot)
    bb = np.empty(n_boot)
    bd = np.empty(n_boot)
    for k in range(n_boot):
        pick = rng.choice(persons, size=len(persons), replace=True)
        idx = np.concatenate([rows_by_person[p] for p in pick])
        pv = np.concatenate([np.full(len(rows_by_person[p]), j) for j, p in enumerate(pick)])
        bw[k], bb[k] = fit(phi[idx], acs[idx], pv)
        bd[k] = bw[k] - bb[k]

    q_lo, q_hi = alpha / 2, 1 - alpha / 2
    return (
        b_within, float(np.quantile(bw, q_lo)), float(np.quantile(bw, q_hi)),
        b_between, float(np.quantile(bb, q_lo)), float(np.quantile(bb, q_hi)),
        b_diff, float(np.quantile(bd, q_lo)), float(np.quantile(bd, q_hi)),
    )
