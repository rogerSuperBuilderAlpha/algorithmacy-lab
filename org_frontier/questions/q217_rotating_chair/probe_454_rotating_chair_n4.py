"""Q217 probe 454: rotating chair at four parties (n=6 with a 2-bit mod-4 clock)."""
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set

P = 4


def form(rotating):
    def phase(x):
        return (x[4] + 2 * x[5]) if rotating else 0

    def party(i):
        def f(x):
            p = phase(x)
            if p == i:
                o = [j for j in range(P) if j != i]
                return x[o[0]] & x[o[1]] & x[o[2]]
            return x[p]
        return f

    nxt = lambda x: (x[4] + 2 * x[5] + 1) % 4
    return [party(i) for i in range(P)] + [lambda x: nxt(x) & 1, lambda x: (nxt(x) >> 1) & 1], tuple("ABCDTU")


for name, rot in [("F4_fixed", False), ("F4_rot", True)]:
    rules, L = form(rot)
    v = verdict(rules, L)
    core, phi = major_complex(rules, L)
    net, tpm = network(rules, L)
    W = integrating_coalitions(net, tpm, len(L))
    vs = sorted(L[i] for i in veto_set(W))
    print(f"{name:8s} structure={v.structure} maxPhi={v.max_phi:.4f} core={core} corePhi={phi:.4f} "
          f"n_integrating={len(W)} veto={vs}", flush=True)
