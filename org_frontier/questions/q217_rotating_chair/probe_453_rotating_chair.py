"""Q217 probe 453: rotating chair. Run from repo root:
    PYPHI_WELCOME_OFF=true python -m org_frontier.questions.q217_rotating_chair.probe_453_rotating_chair
"""
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set

# x = (A, B, C, T...) ; parties 0..2
F_fixed = ([lambda x: x[1] & x[2], lambda x: x[0], lambda x: x[0], lambda x: 1 - x[3]], tuple("ABCT"))


def rot2():
    def a(x): return (x[1] & x[2]) if x[3] == 0 else x[1]
    def b(x): return x[0] if x[3] == 0 else (x[0] & x[2])
    def c(x): return x[0] if x[3] == 0 else x[1]
    return [a, b, c, lambda x: 1 - x[3]], tuple("ABCT")


def rot3():
    def phase(x):
        p = x[3] + 2 * x[4]
        return p if p < 3 else 0  # unreachable state 11 treated as phase 0

    def party(i):
        def f(x):
            p = phase(x)
            if p == i:
                o = [j for j in range(3) if j != i]
                return x[o[0]] & x[o[1]]
            return x[p]
        return f

    def nxt(x):
        return (phase(x) + 1) % 3
    return [party(0), party(1), party(2), lambda x: nxt(x) & 1, lambda x: (nxt(x) >> 1) & 1], tuple("ABCTU")


if __name__ == "__main__":
    for name, (rules, L) in [("F_fixed", F_fixed), ("F_rot2", rot2()), ("F_rot3", rot3())]:
        v = verdict(rules, L)
        core, phi = major_complex(rules, L)
        net, tpm = network(rules, L)
        W = integrating_coalitions(net, tpm, len(L))
        vs = sorted(L[i] for i in veto_set(W))
        print(f"{name:8s} structure={v.structure} maxPhi={v.max_phi:.4f} irreducible_states={v.n_states_irreducible}/{v.n_states_evaluated} "
              f"core={core} corePhi={phi:.4f} n_integrating={len(W)} veto={vs}", flush=True)
