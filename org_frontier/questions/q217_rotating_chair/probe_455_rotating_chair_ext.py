"""Q217 probe 455: non-conjunctive chairs (H7) and an earned, endogenous rotation (H8)."""
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set

OPS = {"AND": lambda a, b: a & b, "OR": lambda a, b: a | b, "XOR": lambda a, b: a ^ b}


def rot3(op, earned=False):
    g = OPS[op]

    def phase(x):
        p = x[3] + 2 * x[4]
        return p if p < 3 else 0

    def party(i):
        def f(x):
            p = phase(x)
            if p == i:
                o = [j for j in range(3) if j != i]
                return g(x[o[0]], x[o[1]])
            return x[p]
        return f

    def nxt(x):
        p = phase(x)
        if earned and not x[p]:
            return p          # chair holds the gavel until it acts
        return (p + 1) % 3
    return [party(0), party(1), party(2), lambda x: nxt(x) & 1, lambda x: (nxt(x) >> 1) & 1], tuple("ABCTU")


if __name__ == "__main__":
    for name, (rules, L) in [("F_rot3_OR", rot3("OR")), ("F_rot3_XOR", rot3("XOR")), ("F_earned3", rot3("AND", True)),
                             ("F_earned3_XOR", rot3("XOR", True))]:
        v = verdict(rules, L)
        core, phi = major_complex(rules, L)
        net, tpm = network(rules, L)
        W = integrating_coalitions(net, tpm, len(L))
        vs = sorted(L[i] for i in veto_set(W))
        print(f"{name:14s} structure={v.structure} maxPhi={v.max_phi:.4f} irreducible={v.n_states_irreducible}/{v.n_states_evaluated} "
              f"core={core} corePhi={phi:.4f} n_integrating={len(W)} veto={vs}", flush=True)
