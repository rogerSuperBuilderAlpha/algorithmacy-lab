"""best_time_pilot — the variance problem in four ChatGPT answers to one prompt.

Four students each asked a fresh ChatGPT session "what was the best time in history?" and submitted the
answer. The four answers are read across three similarity layers and an effective sample size is computed
per layer:

  lexical     token-Jaccard (primary) and TF-IDF cosine (secondary) on the raw text
  structural  Ward clustering of layout features (the template)
  semantic    Jaccard over a hand-coded claim/era taxonomy (the content)

n_eff(L) = N^2 / (1^T K^L 1) is the effective number of independent answers at layer L: N when all distinct,
collapsing toward 1 as the kernel saturates. The script also reads which eras the answers name (a
consensus-core / tail analysis) and a pairwise integration signature of how claims bundle.

Pre-registered gate + H1-H5 are in HYPOTHESES.md, fixed before this script was written. N=4: every test is
descriptive, none powered. See FINDINGS.md for the model and the scaled study.

Run:  python org_frontier/llm_variance/best_time_pilot/analyze_variance.py
"""

import os
import re
import sys

import numpy as np
import pandas as pd

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from sklearn.feature_extraction.text import TfidfVectorizer  # noqa: E402
from sklearn.metrics.pairwise import cosine_similarity  # noqa: E402
from scipy.cluster.hierarchy import linkage, fcluster  # noqa: E402
from sklearn.metrics import silhouette_score  # noqa: E402

from org_frontier.probes._info import mutual_information  # noqa: E402

SEED = 0
N_PERM = 2000
_HERE = os.path.dirname(__file__)
DATA = os.path.join(_HERE, "data")

# fixed claim-column order (must match data/claims_coding.csv; load-bearing for determinism)
CLAIM_COLUMNS = (
    "verdict_present_best", "verdict_hedged_nobest",
    "era_classical_athens", "era_pax_romana", "era_islamic_golden_age", "era_renaissance",
    "era_age_of_discovery", "era_late_1990s", "era_post_wwii", "era_present_day",
    "frame_subjective_disclaimer", "frame_lists_criteria", "frame_best_for_whom",
)
ERA_COLUMNS = tuple(c for c in CLAIM_COLUMNS if c.startswith("era_"))


def _z(x):
    x = x + 0.0
    return 0.0 if abs(x) < 5e-4 else x


def tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def token_jaccard(a, b):
    A, B = set(tokens(a)), set(tokens(b))
    if not A and not B:
        return 1.0
    return len(A & B) / len(A | B)


def set_jaccard(a, b):
    A, B = set(a), set(b)
    if not A and not B:
        return 1.0
    return len(A & B) / len(A | B)


def load_responses():
    df = pd.read_csv(os.path.join(DATA, "responses.csv")).sort_values("response_id").reset_index(drop=True)
    analysis = df[df["role"] == "analysis"].reset_index(drop=True)
    control = df[df["role"] == "control"].reset_index(drop=True)
    return analysis, control


def load_coding(ids):
    df = pd.read_csv(os.path.join(DATA, "claims_coding.csv")).set_index("response_id")
    df = df.reindex(index=list(ids))
    return df[list(CLAIM_COLUMNS)].to_numpy(dtype=int)


def lexical_kernels(texts):
    n = len(texts)
    jac = np.eye(n)
    for i in range(n):
        for j in range(i + 1, n):
            jac[i, j] = jac[j, i] = token_jaccard(texts[i], texts[j])
    vec = TfidfVectorizer(lowercase=True, token_pattern=r"[a-z0-9]+", norm="l2")
    cos = cosine_similarity(vec.fit_transform(texts))
    return jac, cos


def structural_features(texts):
    """Deterministic layout features that separate the templates without using the hand label."""
    feats = []
    for t in texts:
        low = t.lower()
        f_if_value = len(re.findall(r"if you value", low))
        f_for_header = len(re.findall(r"\bfor (health|peace|scientific|economic|culture|adventure|overall)", low))
        f_contender = len(re.findall(r"contenders|bce|–180|1950s–1970s|late 1990s", low))
        f_terminal = len(re.findall(r"depends on the metric|depends on your criteria|→", low))
        feats.append([f_if_value, f_for_header, f_contender, f_terminal])
    X = np.array(feats, dtype=float)
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd[sd == 0] = 1.0
    return (X - mu) / sd


def template_cluster(feat, ids):
    Z = linkage(feat, method="ward")
    best = None
    for k in (2, 3):
        labels = fcluster(Z, t=k, criterion="maxclust")
        if len(set(labels)) < 2:
            continue
        s = silhouette_score(feat, labels, metric="euclidean")
        # tie-break toward fewer families
        if best is None or s > best[0] + 1e-9:
            best = (s, k, labels)
    _, k, labels = best
    groups = {}
    for rid, lab in zip(ids, labels):
        groups.setdefault(int(lab), []).append(rid)
    grouping = sorted((sorted(v) for v in groups.values()))
    return len(groups), grouping


def semantic_kernel(coding):
    n = coding.shape[0]
    sets = [tuple(np.where(coding[i] == 1)[0].tolist()) for i in range(n)]
    K = np.eye(n)
    for i in range(n):
        for j in range(i + 1, n):
            K[i, j] = K[j, i] = set_jaccard(sets[i], sets[j])
    return K


def mean_off(K):
    n = K.shape[0]
    s = (K.sum() - np.trace(K)) / (n * (n - 1))
    return s


def n_eff_kernel(K):
    n = K.shape[0]
    return n * n / K.sum()


def n_eff_icc(K):
    """Design-effect form (flagged degenerate at N=4): n_eff = N / (1 + (N-1) r)."""
    n = K.shape[0]
    r = mean_off(K)
    return n / (1.0 + (n - 1) * r)


def gini(vals):
    x = np.sort(np.asarray(vals, dtype=float))
    n = len(x)
    if x.sum() == 0:
        return 0.0
    diffs = np.abs(x[:, None] - x[None, :]).sum()
    return diffs / (2 * n * n * x.mean())


def norm_entropy(vals):
    p = np.asarray(vals, dtype=float)
    if p.sum() == 0:
        return 0.0
    q = p / p.sum()
    q = q[q > 0]
    return float(-np.sum(q * np.log2(q)) / np.log2(len(vals)))


def era_concentration(coding):
    idx = [CLAIM_COLUMNS.index(c) for c in ERA_COLUMNS]
    inc = coding[:, idx].mean(axis=0)
    n = coding.shape[0]
    head = int(np.sum(inc >= 1.0 - 1e-9))
    singles = int(np.sum(np.abs(inc - 1.0 / n) < 1e-9))
    return inc, gini(inc), norm_entropy(inc), head, singles


def integration_signature(coding):
    """Pairwise claim bundling (descriptive). MI over varying claim columns, in bits."""
    p = coding.mean(axis=0)
    varying = [i for i in range(coding.shape[1]) if 0.0 < p[i] < 1.0]
    mis = []
    for a in range(len(varying)):
        for b in range(a + 1, len(varying)):
            mis.append(mutual_information(coding, [varying[a]], [varying[b]]))
    mean_mi = float(np.mean(mis)) if mis else 0.0
    era_idx = [CLAIM_COLUMNS.index(c) for c in ERA_COLUMNS]
    # o-information over eras, flagged exploratory (undersampled at 4 rows)
    from org_frontier.probes._info import o_information
    o_era = o_information(coding, era_idx)
    return mean_mi, o_era


def permutation_null(coding, observed):
    rng = np.random.default_rng(SEED)
    n, m = coding.shape
    ge = 0
    for _ in range(N_PERM):
        shuf = np.empty_like(coding)
        for c in range(m):
            shuf[:, c] = coding[rng.permutation(n), c]
        K = semantic_kernel(shuf)
        if mean_off(K) >= observed - 1e-12:
            ge += 1
    return (ge + 1) / (N_PERM + 1)


def main():
    print("LLM_VARIANCE — best-time pilot: the variance problem, four responses")
    print("=" * 84)
    analysis, control = load_responses()
    ids = list(analysis["response_id"])
    texts = list(analysis["response_text"])
    n = len(ids)
    print('  n responses: %d   prompt: "what was the best time in history?"   model: chatgpt' % n)

    # ---- gate: instrument control ----
    jac, cos = lexical_kernels(texts)
    dup_text = control["response_text"].iloc[0]
    dup_sim = token_jaccard(dup_text, texts[0])  # control is a copy of r1
    max_distinct = max(jac[i, j] for i in range(n) for j in range(i + 1, n))
    gate = abs(dup_sim - 1.0) < 1e-9 and max_distinct < 1.0
    print("  GATE instrument control: duplicate pair sim=%.3f ; max distinct lexical sim=%.3f : %s"
          % (dup_sim, max_distinct, "PASS" if gate else "FAIL"))
    assert gate, "instrument control failed; aborting"

    coding = load_coding(ids)
    sem = semantic_kernel(coding)

    jac_mean, jac_min, jac_max = mean_off(jac), jac[np.triu_indices(n, 1)].min(), jac[np.triu_indices(n, 1)].max()
    cos_mean = mean_off(cos)
    sem_mean = mean_off(sem)
    sem_min, sem_max = sem[np.triu_indices(n, 1)].min(), sem[np.triu_indices(n, 1)].max()

    feat = structural_features(texts)
    k_fam, grouping = template_cluster(feat, ids)

    neff_lex, neff_str, neff_sem = n_eff_kernel(jac), n_eff_kernel(_struct_kernel(feat)), n_eff_kernel(sem)
    icc_lex, icc_sem = n_eff_icc(jac), n_eff_icc(sem)

    inc, g, h_norm, head, singles = era_concentration(coding)
    verdict_idx = CLAIM_COLUMNS.index("verdict_present_best")
    unanim = float(coding[:, verdict_idx].mean())

    mean_mi, o_era = integration_signature(coding)
    p_perm = permutation_null(coding, sem_mean)

    print("  lexical    token-Jaccard mean=%.3f (min %.3f, max %.3f) ; TF-IDF cosine mean=%.3f"
          % (_z(jac_mean), _z(jac_min), _z(jac_max), _z(cos_mean)))
    print("  structural n_families=%d (ward, silhouette over K in {2,3}) ; grouping=%s"
          % (k_fam, grouping))
    print("  semantic   claim-Jaccard mean=%.3f (min %.3f, max %.3f)" % (_z(sem_mean), _z(sem_min), _z(sem_max)))
    print("  effective N (n_eff = N^2 / sum K): lexical=%.2f  structural=%.2f  semantic=%.2f  (nominal %d)"
          % (neff_lex, neff_str, neff_sem, n))
    print("    [flagged] ICC/deff n_eff lexical=%.2f semantic=%.2f (degenerate at N=4, scaled-study only)"
          % (icc_lex, icc_sem))
    print("  era concentration: Gini=%.3f  norm_entropy=%.3f  head(p=1.0)=%d  singletons(p=0.25)=%d"
          % (_z(g), _z(h_norm), head, singles))
    print("  verdict unanimity=%.3f" % unanim)
    print("  integration: mean pairwise MI over varying claims=%.3f bits ; o_information(eras)=%.3f bits [exploratory]"
          % (_z(mean_mi), _z(o_era)))
    print("  semantic Jaccard vs column-shuffle null: mean_obs=%.3f  p=%.4f" % (_z(sem_mean), p_perm))

    # ---- verdicts ----
    h1 = jac_mean < 0.45 and cos_mean < 0.80
    h2 = k_fam == 3 and [["r3", "r4"]] == [g2 for g2 in grouping if len(g2) > 1]
    h3 = (sem_mean - jac_mean) >= 0.25
    h4 = neff_sem <= 1.5 and neff_lex >= 1.5 * neff_sem
    h5 = abs(unanim - 1.0) < 1e-9 and head >= 3 and singles >= 2 and g > 0.20

    print("=" * 84)
    print("  H1 (surface divergence: token-Jaccard mean < 0.45 and cosine < 0.80): %s" % _v(h1))
    print("  H2 (template convergence: K=3 families, non-singleton {r3,r4}): %s" % _v(h2))
    print("  H3 (semantic beats lexical: claim-Jaccard - token-Jaccard >= 0.25): %s" % _v(h3))
    print("  H4 (effective-N collapse: n_eff_sem <= 1.5 and n_eff_lex >= 1.5x n_eff_sem): %s" % _v(h4))
    print("  H5 (consensus core: verdict unanimous, >=3 head eras, >=2 singletons, Gini > 0.20): %s" % _v(h5))
    print("=" * 84)


def _struct_kernel(feat):
    """Structural similarity kernel from standardized features: K = 1/(1+euclidean), unit diagonal."""
    n = feat.shape[0]
    K = np.eye(n)
    for i in range(n):
        for j in range(i + 1, n):
            d = float(np.linalg.norm(feat[i] - feat[j]))
            K[i, j] = K[j, i] = 1.0 / (1.0 + d)
    return K


def _v(b):
    return "SUPPORTED" if b else "REFUTED"


if __name__ == "__main__":
    main()
