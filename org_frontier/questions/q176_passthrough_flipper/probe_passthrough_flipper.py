"""q176 — Does the pass-through flipper flip the verdict, and is the commit-vs-convey bit the rule the CI is most sensitive to?

QUESTION
    A coded account of a worker-system-counterpart coordination names a Boolean
    determination rule for each party. The system rule can COMMIT (S = D & R: act only
    when the worker decision D and the counterpart request R both hold) or RELAY
    (S = D: pass the worker decision through unchanged). Switching commit to relay is
    the pass-through flip. Two questions: does the flip move the structural verdict from
    triadic to dyadic, and across coder disagreement is the system's commit-vs-convey
    bit the single rule the Phi verdict is most sensitive to.

H1  Switching the system rule from commit (S = D & R) to relay (S = D) flips every
    synthetic account that reads triadic under commit to dyadic (100% flip rate).
    NULL: at least one such account stays triadic under pure relay, so relaying does
    not guarantee a literacy pipe.

H2  A per-rule CI-sensitivity decomposition attributes the largest share of Phi-CI
    width to the system's commit-vs-convey bit (median S share > 0.5, above the worker
    and counterpart rules). NULL: the system rule's median share <= 0.33, so it is not
    the dominant driver of verdict uncertainty.

METHOD
    Reuse the field bridge org_frontier/field/rule_to_phi.py (study 1 of the field
    line): rule_to_phi encodes per-party rules into a TPM and reads the exact IIT-4.0
    Phi verdict; phi_ci propagates coder disagreement into a bootstrap-t Phi interval.
    H1: enumerate a basis family of synthetic accounts (worker and counterpart rules
    over a fixed source basis, the system rule the manipulated bit), keep those triadic
    under commit, and measure the fraction that read dyadic under relay.
    H2: for each account give every party a set of plausible coder readings (the system
    always carries the commit / relay / store ambiguity). Hold two parties at their
    consensus reading, split a coder panel across the third party's plausible readings,
    and read the induced Phi-CI width. Each party's share of the total induced width is
    its sensitivity. Report the median system share over accounts.
    CONTROL: the faithful triad reads triadic with max Phi 2.0; a decoupled relay reads
    dyadic; a fully committed account reads triadic with a degenerate (zero-width) CI.
    All inputs are synthetic coded rule sets, not measured worker states.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
      python -m org_frontier.questions.q176_passthrough_flipper.probe_passthrough_flipper
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.field.rule_to_phi import rule_to_phi, phi_ci

LABELS = ("W", "S", "C")
# little-endian current state x = (W, S, C); index 0=W, 1=S, 2=C.

# System rules: the manipulated bit.
S_COMMIT = lambda x: x[0] & x[2]   # act only when worker decision and counterpart request hold
S_RELAY = lambda x: x[0]           # pass the worker decision through
S_STORE = lambda x: x[2]           # hold the counterpart state


def ci_width(coder_phis, rng):
    r = phi_ci(coder_phis, rng=rng)
    return r["ci_high"] - r["ci_low"]


# --------------------------------------------------------------------------------------
# INSTRUMENT CONTROL
# --------------------------------------------------------------------------------------

def control():
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    t = rule_to_phi(triad, LABELS)
    assert t["structure"] == "triadic" and abs(t["max_phi"] - 2.0) < 1e-9, t

    decoupled_relay = [lambda x: x[0], S_RELAY, lambda x: x[2]]
    d = rule_to_phi(decoupled_relay, LABELS)
    assert d["structure"] == "dyadic" and d["max_phi"] < 1e-9, d

    committed = [lambda x: x[1], S_COMMIT, lambda x: x[1]]
    c = rule_to_phi(committed, LABELS)
    assert c["structure"] == "triadic" and abs(c["max_phi"] - 2.0) < 1e-9, c
    # one reading repeated -> degenerate (zero-width) CI
    ci = phi_ci([c["max_phi"], c["max_phi"], c["max_phi"]], rng=np.random.default_rng(0))
    assert ci["degenerate"] and (ci["ci_high"] - ci["ci_low"]) < 1e-9, ci

    print("CONTROL faithful-triad triadic@2.0, decoupled-relay dyadic, committed-account triadic w/ zero-width CI ... PASS")


# --------------------------------------------------------------------------------------
# H1 — pass-through flip rate
# --------------------------------------------------------------------------------------

def _src(i):
    return lambda x: x[i]


def h1_flip_rate():
    """Enumerate a basis family of accounts; the system rule is the manipulated bit.

    Worker and counterpart rules are drawn from a fixed basis of single-source and
    pairwise-coupling forms. An account is in scope when it reads triadic under commit.
    The flip rate is the fraction of in-scope accounts that read dyadic under relay.
    """
    w_basis = [_src(0), _src(1), _src(2), lambda x: x[1] & x[2], lambda x: x[1] | x[2]]
    w_names = ["W<-W", "W<-S", "W<-C", "W<-S&C", "W<-S|C"]
    c_basis = [_src(0), _src(1), _src(2), lambda x: x[0] & x[1], lambda x: x[0] | x[1]]
    c_names = ["C<-W", "C<-S", "C<-C", "C<-W&S", "C<-W|S"]

    rows = []
    in_scope = 0
    flipped = 0
    for wi, W in enumerate(w_basis):
        for ci, C in enumerate(c_basis):
            commit = [W, S_COMMIT, C]
            rc = rule_to_phi(commit, LABELS)
            if rc["structure"] != "triadic":
                continue
            in_scope += 1
            relay = [W, S_RELAY, C]
            rr = rule_to_phi(relay, LABELS)
            flips = rr["structure"] == "dyadic"
            if flips:
                flipped += 1
            rows.append((w_names[wi], c_names[ci], rc["max_phi"], rr["structure"], rr["max_phi"], flips))
    rate = flipped / in_scope if in_scope else 0.0
    return rows, in_scope, flipped, rate


# --------------------------------------------------------------------------------------
# H2 — per-rule CI-sensitivity decomposition
# --------------------------------------------------------------------------------------

def _account_family():
    """Synthetic accounts. Each names per-party plausible coder readings.

    The system always carries the commit / relay / store ambiguity (the commit-vs-convey
    bit). The worker and counterpart each carry a coupled reading and a decoupled-self
    reading, so a coder splitting on either could in principle swing the verdict.
    The first reading of each party is the consensus reading.
    """
    S_alts = [S_COMMIT, S_RELAY, S_STORE]
    return {
        "mutual": dict(
            W=[lambda x: x[1], lambda x: x[0]], S=S_alts, C=[lambda x: x[1], lambda x: x[2]]),
        "wfeedback": dict(
            W=[lambda x: x[1], lambda x: x[0]], S=S_alts, C=[lambda x: x[0], lambda x: x[2]]),
        "cfollows": dict(
            W=[lambda x: x[2], lambda x: x[0]], S=S_alts, C=[lambda x: x[1], lambda x: x[2]]),
        "sdriven": dict(
            W=[lambda x: x[1], lambda x: x[1] & x[2]], S=S_alts, C=[lambda x: x[1], lambda x: x[1] & x[0]]),
        "andmix": dict(
            W=[lambda x: x[1], lambda x: x[2]], S=S_alts, C=[lambda x: x[0] & x[1], lambda x: x[1]]),
    }


def _party_phis(account, party):
    """Phi readings when a coder panel splits across `party`'s plausible readings,
    holding the other two parties at their consensus (first) reading."""
    Wc, Sc, Cc = account["W"][0], account["S"][0], account["C"][0]
    out = []
    for alt in account[party]:
        rules = [
            alt if party == "W" else Wc,
            alt if party == "S" else Sc,
            alt if party == "C" else Cc,
        ]
        out.append(rule_to_phi(rules, LABELS)["max_phi"])
    return out


def h2_decomposition():
    fam = _account_family()
    rows = []
    s_shares = []
    for name, acct in fam.items():
        widths = {}
        for party in ("W", "S", "C"):
            rng = np.random.default_rng(0)  # fixed per-call for determinism
            widths[party] = ci_width(_party_phis(acct, party), rng)
        total = sum(widths.values())
        if total > 1e-12:
            shares = {p: widths[p] / total for p in ("W", "S", "C")}
            s_shares.append(shares["S"])
        else:
            shares = None
        rows.append((name, widths, shares))
    median_s = float(np.median(s_shares)) if s_shares else float("nan")
    return rows, s_shares, median_s


# --------------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------------

def main():
    control()
    print()

    rows, in_scope, flipped, rate = h1_flip_rate()
    print("H1  pass-through flip: commit (S=D&R) -> relay (S=D), over the basis account family")
    print(f"    {'worker':8} {'counterpart':12} {'commit':>7} {'relay':>8} {'relayphi':>9} {'flips':>6}")
    for wn, cn, cphi, rstruct, rphi, flips in rows:
        print(f"    {wn:8} {cn:12} {'triadic':>7} {rstruct:>8} {rphi:>9.3f} {str(flips):>6}")
    print(f"    in-scope (triadic under commit): {in_scope}   flipped to dyadic under relay: {flipped}")
    print(f"    flip rate: {rate:.3f}")
    print()

    h2_rows, s_shares, median_s = h2_decomposition()
    print("H2  per-rule CI-sensitivity decomposition (induced Phi-CI width by party, share of total)")
    print(f"    {'account':10} {'W width':>8} {'S width':>8} {'C width':>8}   {'W sh':>5} {'S sh':>5} {'C sh':>5}")
    for name, w, sh in h2_rows:
        if sh is None:
            print(f"    {name:10} {w['W']:8.3f} {w['S']:8.3f} {w['C']:8.3f}   {'--':>5} {'--':>5} {'--':>5}")
        else:
            print(f"    {name:10} {w['W']:8.3f} {w['S']:8.3f} {w['C']:8.3f}   "
                  f"{sh['W']:5.2f} {sh['S']:5.2f} {sh['C']:5.2f}")
    print(f"    accounts with nonzero induced width: {len(s_shares)} / {len(h2_rows)}")
    print(f"    median system (S) share of CI width: {median_s:.3f}")
    print()

    # H1 verdict: NULL holds if any in-scope account stays triadic under relay.
    h1_supported = abs(rate - 1.0) < 1e-9
    print(f"H1 pass-through flip is universal (100% flip rate): "
          f"{'SUPPORTED' if h1_supported else 'REFUTED'}")
    if not h1_supported:
        stayed = in_scope - flipped
        print(f"   NULL holds: {stayed} of {in_scope} triadic-under-commit accounts stay triadic "
              f"under pure relay, so relaying does not guarantee a literacy pipe.")

    # H2 verdict: median S share > 0.5.
    h2_supported = median_s > 0.5
    print(f"H2 commit-vs-convey bit is the dominant CI driver (median S share > 0.5): "
          f"{'SUPPORTED' if h2_supported else 'NOT SUPPORTED'}")


if __name__ == "__main__":
    main()
