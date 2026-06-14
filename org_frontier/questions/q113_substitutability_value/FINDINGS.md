# Q113 findings — substitutability destroys all value; a required set shares it equally

All four hypotheses confirmed. An all-required market distributes its value equally among the parties, in
contrast to the mediated triad where the mediator concentrated it. A substitutable market captures no value
at all: making the agents interchangeable does not lower their share, it zeroes the whole coordination's
worth.

| market | Φ | Shapley values | total |
|---|---|---|---|
| all-required (N=2) | 4.0 | E=1, M1=1, M2=1, C=1 | 4.0 |
| substitutable (N=2) | 0.0 | E=0, M1=0, M2=0, C=0 | 0.0 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | the all-required market captures positive value | confirmed (4.0) |
| H2 | the substitutable market captures zero value | confirmed |
| H3 | the required parties share value equally | confirmed |
| H4 | substitutability destroys the whole value (= Φ) | confirmed |

From `probe_substitutability_value.py`.

## What it says

A required set shares its value equally. In the all-required market, each of the four parties — the worker,
both agents, and the counterpart — has Shapley value 1.0, a quarter of the market's Φ of 4 (H1, H3). This is
the opposite of the mediated triad of Q111, where the mediator captured two-thirds. The difference is
essentiality. In the triad, one party was uniquely essential (the others produced nothing without it), so
it captured the most. In the all-required market every party is equally essential, each needed for the
coordination, so the value distributes equally. Value concentrates only when essentiality is asymmetric;
when all parties are equally required, the rent is shared.

Substitutability destroys the whole value, not a share. The substitutable market captures zero (H2): being
dyadic, it has no integrated information to distribute, so every party's value is zero. The value lost in
making the agents interchangeable is the entire market's Φ of 4 (H4), borne by all the parties, not just the
substitutable ones. Substitutability is not a discount on a replaceable agent's value; it is the destruction
of the coordination's value for everyone, including the parties who are not themselves substitutable. A
worker and a counterpart who could have shared in a market worth four capture nothing once the agents
between them become interchangeable.

The political-economy reading is that interchangeability is catastrophic, not merely disadvantageous to the
interchangeable. A platform that makes its agents substitutable, to discipline them or cut their rents,
does not transfer the agents' value to itself; it eliminates the coordination that produced any value, and
the platform's own share goes to zero with everyone else's. The threat of substitution is a threat to the
whole coordination, which is why a required set, where no party can be replaced, is the configuration that
sustains value, and why the value it sustains is shared among its equally-essential members.

## Caveats

- **Confirmatory.** All four predictions held; the contrast with Q111 follows from symmetric versus
  asymmetric essentiality.
- **Two market configurations.** The all-required and substitutable markets at N = 2; the mixed market and
  larger N are untested, though Finding 5 makes any substitutable pair dyadic.
- **Coalition value as subsystem Φ.** As in Q111, the value is the subsystem Φ at the all-ones state.
  In-silico, exact Φ.
