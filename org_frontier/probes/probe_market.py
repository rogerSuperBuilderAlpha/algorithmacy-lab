"""Probe 68 (#48) — is a market clearinghouse triadic?

Question: a clearinghouse matches buyers and sellers; is that structurally triadic, like the pool, or
dyadic, like a broadcast price-poster? Hypothesis: a clearinghouse that jointly matches supply and
demand is triadic; a pure price-poster (one-way broadcast) is dyadic. Method: model small market forms
and classify.

Nodes: 0=B (buyer), 1=S (clearinghouse), 2=Se (seller), and for the two-buyer case 3=B2.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_market
"""

from .lib import verdict, major_complex

FORMS = {
    # clearinghouse: matches iff a buyer AND a seller are present; both track the clearing
    ("clearinghouse", ("B", "S", "Se")):
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    # price-poster: clearinghouse broadcasts a price set by the seller; buyer reads it; no joint match
    ("price_poster", ("B", "S", "Se")):
        [lambda x: x[1], lambda x: x[2], lambda x: x[2]],
    # two-buyer clearinghouse, sided market: match needs the seller and at least one buyer
    ("two_buyer_either", ("B1", "S", "Se", "B2")):
        [lambda x: x[1], lambda x: (x[0] | x[3]) & x[2], lambda x: x[1], lambda x: x[1]],
    # two-buyer clearinghouse requiring both buyers and the seller (joint clear)
    ("two_buyer_all", ("B1", "S", "Se", "B2")):
        [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
}


def main():
    print("PROBE 68 (#48) — market clearinghouse forms")
    print("=" * 80)
    for (name, labels), rules in FORMS.items():
        v = verdict(rules, labels)
        core, phi = major_complex(rules, labels)
        print(f"  {name:<20} {v.structure:<8} Φ={v.max_phi:.3f}   core={core}")
    print("=" * 80)
    print("  Reading: a clearinghouse that jointly matches supply and demand is triadic; a one-way")
    print("  price-poster is a conveyor and factors; substitutable buyers (either clears) dilute it.")
    print("=" * 80)


if __name__ == "__main__":
    main()
