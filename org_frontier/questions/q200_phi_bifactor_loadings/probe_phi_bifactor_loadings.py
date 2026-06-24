"""Probe 354 (Q200) — does Φ_coord load on the general algorithmacy factor, not a specific facet?

Question: in a bifactor model of the Algorithmacy Competence Scale (a general algorithmacy factor g
plus three orthogonal specific facets — computational interpretation CI, system coordination SC,
recursive thinking RT), does a worker's Φ_coord predict the GENERAL factor rather than one specific
facet, in the simulated W2 cohort?

H1: Φ_coord predicts the bifactor GENERAL algorithmacy factor (β > 0, 95% CI excludes 0) and this
    general-factor path exceeds each specific-facet path (Δ = β_g − β_facet has a 95% CI that excludes
    0 for every facet).
    Null: Φ_coord's general-factor path is no larger than its specific-facet paths.
H2: The model where Φ_coord predicts the general factor fits better than the competing model where
    Φ_coord predicts only the SC specific factor (ΔCFI ≥ .01 favouring the general path).
    Null: routing Φ_coord to the SC specific facet fits as well as routing it to g.

Method: import the shared bridge (phi_bridge). Each simulated worker's reported (TI, SA-commit, SU)
row maps to a W-S-C Boolean form whose exact IIT-4.0 Φ_coord is 2.0 (commit, irreducible) or 0.0
(convey, factorizable). The coordination latent z that drives those reported conditions is built to
load on the general algorithmacy factor g, so Φ_coord (a function of z) tracks g. ACS is fielded as
nine items: three per facet (CI/SC/RT). Each item loads on g and on its own specific facet plus a
unique. A bifactor CFA is fit by orthogonal factor extraction (general factor from the full item
pool; specific facets from the within-block residuals after the general factor is partialled), and
factor scores are recovered by regression. Φ_coord is then regressed on the general-factor score and
on each specific-facet score. Path differences (β_g − β_facet) get bootstrap CIs. Model fit (CFI)
compares the Φ→g model against the competing Φ→SC model by the model-implied vs observed covariance.

Determinism: one fixed seed (numpy.random.default_rng(0)). Φ_coord depends only on which of two forms
a worker maps to; the cohort draw and the bootstrap are each freshly seeded, so the run is
byte-identical on re-run.

Scope: the cohort is SIMULATED. No worker is measured. The bifactor structure and the Φ-to-g coupling
are built into the synthetic data on purpose; the probe recovers them through the exact-Φ instrument
and the bifactor fit. The result is evidence about the bridge and the bifactor pipeline on synthetic
data, not a measured loading in a real cohort.

Run:  python -m org_frontier.questions.q200_phi_bifactor_loadings.probe_phi_bifactor_loadings
"""

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import max_phi_float, verdict
from org_frontier.survey.cohort_algorithmacy.phi_bridge import (
    LABELS, phi_coord, worker_rules,
)

N = 400
FACETS = ("CI", "SC", "RT")  # computational interpretation, system coordination, recursive thinking
ITEMS_PER_FACET = 3


def instrument_control():
    """Validate the Φ instrument on the canonical faithful mediated triad."""
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    tpm = tpm_from_rules(triad)
    mx, _ = max_phi_float(tpm)
    v = verdict(triad, LABELS)
    ok = (v.structure == "triadic") and (abs(mx - 2.0) < 1e-9)
    print(f"CONTROL faithful triad [x1, x0&x2, x1]: verdict={v.structure}, max_phi={mx:.6f} "
          f"-> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed"
    return ok


def zscore(v):
    v = np.asarray(v, float)
    return (v - v.mean()) / v.std(ddof=1)


def ols_with_ci(X, y, alpha=0.05):
    """OLS β with classical normal-theory standard errors and a (1-alpha) CI per coefficient.

    X already includes an intercept column. Returns (beta, se, lo, hi) arrays.
    """
    X = np.asarray(X, float)
    y = np.asarray(y, float)
    n, k = X.shape
    XtX_inv = np.linalg.inv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    resid = y - X @ beta
    dof = n - k
    sigma2 = float(resid @ resid) / dof
    cov = sigma2 * XtX_inv
    se = np.sqrt(np.diag(cov))
    zcrit = 1.959963984540054  # 0.975 normal quantile
    lo = beta - zcrit * se
    hi = beta + zcrit * se
    return beta, se, lo, hi


def simulate_bifactor_cohort(n, rng, control=False):
    """A simulated W2 cohort with a bifactor ACS and a Φ_coord coupled to the general factor.

    A general algorithmacy factor g and three orthogonal specific facets (CI, SC, RT) generate nine
    ACS items (three per facet); each item loads on g and on its own facet plus a unique. The
    coordination latent z that drives the reported conditions (TI, SA-commit, SU) — and so the
    W-S-C form and Φ_coord — is built to load on g (Φ_coord is a general-algorithmacy signal, not a
    facet-specific one). ``control=True`` forces the dyadic pass-through so Φ_coord is identically 0.
    """
    # general algorithmacy factor and three orthogonal specific facets (all standard-normal)
    g = rng.normal(0, 1, n)
    s = {f: rng.normal(0, 1, n) for f in FACETS}

    # coordination latent z loads on the general factor g plus its own part; z drives the W-S-C form
    z = 0.85 * g + rng.normal(0, np.sqrt(1 - 0.85 ** 2), n)

    # reported conditions from z (as in the shared bridge cohort)
    ti = np.clip(np.round(4.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    sa = np.clip(np.round(4.0 + 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    su = np.clip(np.round(4.0 - 0.9 * z + rng.normal(0, 0.7, n)), 1, 7)
    phi = np.array([phi_coord(ti[i], sa[i], su[i], control=control) for i in range(n)])

    # nine ACS items: item = lam_g*g + lam_s*specific + unique. Strong general, moderate specific.
    lam_g = 0.70
    lam_s = 0.45
    unique_sd = np.sqrt(max(1 - lam_g ** 2 - lam_s ** 2, 0.05))
    items = {}
    for f in FACETS:
        for j in range(ITEMS_PER_FACET):
            items[f"{f}{j+1}"] = lam_g * g + lam_s * s[f] + unique_sd * rng.normal(0, 1, n)

    item_names = list(items.keys())
    X = np.column_stack([zscore(items[name]) for name in item_names])  # (n, 9), standardized
    return {
        "g_true": g, "s_true": s, "z": z,
        "ti": ti, "sa": sa, "su": su, "phi": phi,
        "items": X, "item_names": item_names,
    }


def bifactor_scores(X, item_names):
    """Recover bifactor factor scores (one general, three specific) by orthogonal extraction.

    General factor: first principal component of the full item correlation matrix (the dominant common
    dimension), scored by regression. Specific facets: within each three-item block, partial the
    general-factor score out of the block items, take the first PC of the residual block, scored by
    regression. The specific scores are residualized on the general score, so the four scores are
    (near-)orthogonal, the bifactor identification.
    """
    n = X.shape[0]
    # --- general factor: first PC of the standardized item matrix ---
    U, sv, Vt = np.linalg.svd(X - X.mean(axis=0), full_matrices=False)
    v1 = Vt[0]
    if v1.sum() < 0:               # fix sign so the general factor points with the items
        v1 = -v1
    g_score = zscore(X @ v1)

    # --- specific facets: first PC of each block's residual after partialling the general score ---
    design = np.column_stack([np.ones(n), g_score])
    proj = design @ np.linalg.inv(design.T @ design) @ design.T  # residual-maker base

    s_scores = {}
    for f in FACETS:
        cols = [k for k, name in enumerate(item_names) if name.startswith(f)]
        block = X[:, cols]
        resid = block - proj @ block            # partial the general score out of the block
        Ur, svr, Vtr = np.linalg.svd(resid - resid.mean(axis=0), full_matrices=False)
        u1 = Vtr[0]
        if u1.sum() < 0:
            u1 = -u1
        sc = resid @ u1
        # residualize on the general score so the specific score is orthogonal to g
        sc = sc - proj @ sc
        s_scores[f] = zscore(sc)
    return g_score, s_scores


def routed_implied_cov(X, phi_z, g_score, s_scores, route):
    """Model-implied covariance of the augmented [items | Φ] block under a routing of Φ.

    The bifactor measurement part regresses each item on [1, g, CI, SC, RT]; the common part is the
    fitted value. Φ is then modelled as predicted by exactly one latent — the routed factor. ``route``
    is 'g' (Φ predicted by the general factor) or 'SC' (Φ predicted by the SC specific factor). The
    implied Φ is the fit of Φ on that single routed factor. The implied covariance of the augmented
    (items + Φ) block is the covariance of [common-item-part | implied-Φ]. Routing Φ to g lets Φ
    covary with every item (g loads on all nine); routing Φ to SC lets Φ covary only with the SC
    block. The observed data has Φ covarying with all blocks, so the g routing reproduces it.
    """
    n, p = X.shape
    lat = np.column_stack([np.ones(n), g_score, s_scores["CI"], s_scores["SC"], s_scores["RT"]])
    B = np.linalg.lstsq(lat, X, rcond=None)[0]
    item_common = lat @ B                              # (n, p): bifactor common part of the items

    routed = g_score if route == "g" else s_scores["SC"]
    d = np.column_stack([np.ones(n), routed])
    phi_implied = d @ np.linalg.lstsq(d, phi_z, rcond=None)[0]  # Φ from the single routed factor

    aug = np.column_stack([item_common, phi_implied])  # (n, p+1)
    return np.cov(aug, rowvar=False)


def cfi_routed(X, phi_z, g_score, s_scores, route):
    """CFI for a routed model against the independence baseline on the augmented [items | Φ] block.

    Discrepancy is the sum of squared off-diagonal residuals between the observed augmented covariance
    and the model-implied augmented covariance. The independence model implies a diagonal covariance.
    CFI = 1 − max(d_model, 0) / max(d_null, 0), bounded to [0, 1]. The Φ-item off-diagonals are the
    cells the routing controls, so a routing that mis-predicts where Φ covaries pays in discrepancy.
    """
    aug_obs = np.column_stack([X, phi_z])
    S = np.cov(aug_obs, rowvar=False)
    q = S.shape[0]
    off = ~np.eye(q, dtype=bool)

    def discrepancy(implied):
        return float(np.sum(((S - implied)[off]) ** 2))

    d_null = discrepancy(np.diag(np.diag(S)))
    d_model = discrepancy(routed_implied_cov(X, phi_z, g_score, s_scores, route))
    cfi = 1.0 - max(d_model, 0.0) / max(d_null, 1e-12)
    return max(min(cfi, 1.0), 0.0), d_model, d_null


def main():
    print("=" * 80)
    print("Q200 — does Φ_coord load on the GENERAL algorithmacy factor, not a facet? (SIMULATED W2)")
    print("=" * 80)

    instrument_control()

    # Show the two W-S-C forms a worker maps to, so the bridge map is auditable.
    print("\nBridge map — the two W-S-C forms a worker can map to:")
    for name, rules in (("commit S'=W AND C", worker_rules(7, 7, 1, control=False)),
                        ("convey S'=W", worker_rules(7, 7, 7, control=False))):
        v = verdict(rules, LABELS)
        mx, _ = max_phi_float(tpm_from_rules(rules))
        print(f"  {name:18s}: {v.structure:8s}  Φ_coord={mx:.6f}")

    rng = np.random.default_rng(0)
    coh = simulate_bifactor_cohort(N, rng, control=False)
    X = coh["items"]
    phi = coh["phi"]
    n_commit = int((phi > 1e-9).sum())
    print(f"\nCohort: N={N}; {n_commit} irreducible (commit) forms, {N - n_commit} factorizable "
          f"(convey); 9 ACS items (3 per facet CI/SC/RT).")

    # --- bifactor factor scores ---
    g_score, s_scores = bifactor_scores(X, coh["item_names"])

    # --- Φ_coord paths to g and to each specific facet (single-predictor standardized betas) ---
    def path(target):
        Xd = np.column_stack([np.ones(N), zscore(phi)])
        b, se, lo, hi = ols_with_ci(Xd, zscore(target))
        return b[1], lo[1], hi[1]

    beta_g, lo_g, hi_g = path(g_score)
    facet_paths = {f: path(s_scores[f]) for f in FACETS}

    # --- bootstrap CIs for Δ = β_g − β_facet (dependent, same sample) ---
    def std_beta(xv, yv):
        xz, yz = zscore(xv), zscore(yv)
        return float(np.corrcoef(xz, yz)[0, 1])  # standardized single-predictor β = correlation

    boot_rng = np.random.default_rng(0)
    NB = 4000
    deltas = {f: np.empty(NB) for f in FACETS}
    for k in range(NB):
        idx = boot_rng.integers(0, N, N)
        pz = phi[idx]
        bg = std_beta(pz, g_score[idx])
        for f in FACETS:
            deltas[f][k] = bg - std_beta(pz, s_scores[f][idx])
    delta_ci = {f: (float(np.mean(deltas[f])),
                    float(np.quantile(deltas[f], 0.025)),
                    float(np.quantile(deltas[f], 0.975))) for f in FACETS}

    print("\n" + "-" * 80)
    print(f"{'Φ_coord path target':<26}{'β (std)':<12}{'95% CI':<24}{'Δ vs g (β_g−β)':<18}")
    print("-" * 80)
    print(f"{'GENERAL g':<26}{beta_g:<+12.4f}[{lo_g:+.4f}, {hi_g:+.4f}]")
    for f in FACETS:
        b, lo, hi = facet_paths[f]
        dm, dlo, dhi = delta_ci[f]
        print(f"{'specific ' + f:<26}{b:<+12.4f}[{lo:+.4f}, {hi:+.4f}]"
              f"   {dm:+.4f} [{dlo:+.4f}, {dhi:+.4f}]")
    print("-" * 80)

    # --- H2: Φ→g model vs competing Φ→SC model, by CFI on the augmented [items | Φ] covariance ---
    phi_z = zscore(phi)
    cfi_g, d_g, d_null = cfi_routed(X, phi_z, g_score, s_scores, route="g")
    cfi_sc, d_sc, _ = cfi_routed(X, phi_z, g_score, s_scores, route="SC")
    dcfi = cfi_g - cfi_sc

    print(f"\nModel fit (CFI on the augmented 9-item + Φ covariance):")
    print(f"  Φ→g  model (Φ routed to the general factor):  CFI={cfi_g:.4f}  (discrepancy {d_g:.4f})")
    print(f"  Φ→SC model (Φ routed to the SC specific):     CFI={cfi_sc:.4f}  (discrepancy {d_sc:.4f})")
    print(f"  ΔCFI (Φ→g minus Φ→SC) = {dcfi:+.4f}   (null-model discrepancy {d_null:.4f})")

    # --- verdicts ---
    # H1: β_g > 0, CI excludes 0, AND every Δ(g − facet) CI excludes 0 (g path exceeds each facet path).
    h1_g_positive = (beta_g > 0.0) and (lo_g > 0.0)
    h1_exceeds = all(delta_ci[f][1] > 0.0 for f in FACETS)
    h1 = h1_g_positive and h1_exceeds
    # H2: Φ→g fits better than Φ→SC by ΔCFI ≥ .01.
    h2 = dcfi >= 0.01

    print(f"\n  general-factor path positive & CI excludes 0: {h1_g_positive}")
    print(f"  general path exceeds each specific path (all Δ CI exclude 0): {h1_exceeds}")

    print(f"\nH1 (Φ_coord loads on the GENERAL factor, β>0 & CI excludes 0, and the general path "
          f"exceeds each specific-facet path): {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"   β_g={beta_g:+.4f} CI=[{lo_g:+.4f}, {hi_g:+.4f}]; "
          f"facet βs " + ", ".join(f"{f}={facet_paths[f][0]:+.4f}" for f in FACETS))
    print(f"H2 (the Φ→general model fits better than the Φ→SC-specific model by ΔCFI ≥ .01): "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}")
    print(f"   ΔCFI={dcfi:+.4f} (Φ→g CFI={cfi_g:.4f}, Φ→SC CFI={cfi_sc:.4f})")


if __name__ == "__main__":
    main()
