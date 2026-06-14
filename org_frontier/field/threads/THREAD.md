# Thread — is the mediator in the irreducible core?

A single question, dug twenty steps deep from one anomaly in the field mocks: when is a mediating
system a member of the irreducible coordination, and when is it a bypassable side-channel? The
verdicts are in-silico, on small Boolean models; the value is the structure that emerges, not a
measurement of any organization. Reproduce the headline numbers with
`python -m org_frontier.field.threads.mediator_in_core`.

## The seed

Mock M4, the CI code-review gate, reads triadic — the coordination is irreducible — yet its major
complex is author–maintainer, and the gate, the thing that "commits the pass/fail," sits outside the
core. Mock M9's arbitrator, by contrast, is in its core. Same shape, opposite membership. The thread
chases that contradiction.

## The arc, with its turns

**Q1–Q2.** The gate leaves the core only when two things hold at once: it senses just one party, and
the two parties have a direct mutual channel. Sensing both keeps it in; sensing one with no direct
channel collapses the form to dyadic. The bypass needs the parties' direct tie to be *reciprocal* —
a one-way link either leaves the form dyadic or ejects the counterpart instead.

**Q3 (a refutation).** The natural guess — the mediator must sense two parties — is wrong. `S=W|C`
reads both and is still bypassed; `S=W&C` stays. Membership is not about fan-in. It is a
Φ-competition: the mediator is in the core only when the whole system is more integrated than the
parties' own coalition. The major complex is just the argmax coalition.

**Q4–Q5.** Mapping mediator logic against the direct channel, the conjunctive bottleneck `S=W&C`
keeps the full triad in the core in every condition; one-sided and disjunctive mediators lose to a
mutual channel. Charting all sixteen mediator logics shows a third regime as well: biased,
negation-bearing mediators (`¬W`, `XNOR`) survive only by forming an exclusive pair with one party
and ejecting the other — platform capture.

**Q6.** The mediator must be embedded both ways. A platform that only observes two reciprocating
parties, or that broadcasts a constant they read, is excluded. Acting-on and being-acted-on are both
required.

**Q7 (grounding).** In the ride-hail frame: a two-sided conjunctive match (`P=D&R`) survives drivers
and riders adding a direct off-platform tie; a one-sided platform (`P=D`) is disintermediated the
moment they connect.

**Q9 (the crux).** What bypasses a platform is not that a direct channel exists, but that it makes
the platform *optional*. A substitute tie (parties can use platform or direct, `W=S|C`) ejects the
platform; a complement tie (parties need both, `W=S&C`) keeps it. Disintermediation is the
substitutability law turned on the platform itself.

**Q10.** The law scales to more parties, and two redundant platforms (parties read either) make each
non-pivotal — the platform layer self-collapses. That is multi-homing dissolving structural
necessity.

**Q11.** The strategic inverse: a bypassed platform regains the core by sensing both sides, or by
becoming a required step. Both are routes to being a bidirectional conjunctive complement.

**Q12.** The account predicts the mediator's membership across all ten mocks. Among the triadic
mocks, only the CI gate is excluded — the lone one-sided sensor with a direct human channel.

**Q13 (the reshaping).** Lesioning the mediator — freezing it and asking whether the parties still
coordinate — splits "in the core" into two. A mediator with no party fallback breaks coordination
when lesioned; a conjunctive mediator that sits alongside a direct tie is in the core yet survives
lesioning. Being in the irreducible core is not the same as being indispensable.

**Q14–Q15.** The trichotomy. **Bottleneck**: no party fallback, the sole integrator, in the core and
indispensable. **Enricher**: a fallback exists, but the mediator (a conjunctive complement) still
deepens integration enough to join the core — in the core, dispensable. **Bypassed**: a party
coalition out-integrates the mediator. Of the triadic mocks, the platforms are bottlenecks except
the bypassed CI gate; none are enrichers, because the mocks were built without fallback channels.

**Q16.** Over five hundred random mediated forms: bottlenecks are the rarest regime (13.6%), bypassed
mediators are common among triadic forms (about a third), and enrichers are the most common in-core
regime (23.2%). The hand-built mocks, lacking fallbacks, over-represent bottlenecks — a modeling bias
real organizations, which have fallbacks, would correct.

**Q17.** The missing regime in a real shape: a freelance escrow, where client and freelancer work
directly and the escrow conjunctively gates payment, is an enricher — in the core, but the parties
survive its removal. The platform that adds value yet faces leakage.

**Q18 (the correction).** "One-sided implies bypassed" is false in general. A one-sided mediator is
in the core in 73% of triadic random forms. One-sidedness bypasses the mediator only when the parties
happen to form a competing coalition. There is no structural shortcut; the membership is a genuine
Φ-competition.

**Q19–Q20.** The same one-sided mediator rule yields four different regimes as only the parties'
coupling changes. And the ride-hail platform walks bottleneck → enricher → bypassed as off-platform
contact goes from absent to complementary to substitutable. Disintermediation is that walk.

## What the thread found

A mediating system's place in the irreducible coordination is not a property of the system. It is a
property of the whole arrangement — a competition between the system-inclusive whole and the parties'
own coalitions, won or lost on integrated information. Three regimes follow, and one transition:

- **Bottleneck** — the parties have no path to each other except through the system. The system is in
  the core and indispensable.
- **Enricher** — the parties have a direct fallback, but the system, as a conjunctive complement,
  still deepens the coordination enough to belong to the core. In the core, dispensable.
- **Bypassed** — a party coalition is more integrated than the whole. The system is causally present
  and outside the irreducible core: a side-channel.
- **Disintermediation** is the move from bottleneck or enricher to bypassed, driven by the parties
  acquiring a substitute path. **Re-intermediation** is the reverse, by the system becoming a
  bidirectional conjunctive complement — sensing both sides and making itself a required step.

For the algorithmacy thesis the payoff is sharp: a platform "doing irreducible work" is not settled
by the platform's design. The same matching rule is indispensable, merely enriching, or bypassed
depending on whether the parties can reach each other another way. Algorithmacy is a position a
platform can hold and lose.

## Limits

All of this is in-silico, on three- to four-node Boolean models, and the magnitude of Φ is not read
beyond the binary verdict and the membership. The lesion test asks whether the parties coordinate
under *some* frozen mediator value, which can credit a fallback the live dynamics never reach; a
sharper test would weight by reachability. The random battery samples one encoding family. And the
whole thread inherits the field protocol's gap: these are stipulated models, and which regime a real
platform occupies is an empirical question the computation cannot answer. What the thread offers a
field study is the question to ask — bottleneck, enricher, or bypassed — and a way to model it.
