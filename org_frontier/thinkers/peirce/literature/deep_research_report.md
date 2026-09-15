# Peirce — Stage 2 literature

## Primary texts

Peirce's account of the triad is the **reduction thesis** of his logic of relations, and it has two clauses.
The negative clause — some triadic relations cannot be built from monadic and dyadic ones — appears first
without argument in the 1870 "Description of a Notation for the Logic of Relatives" (CP 3.144), receives
its valency argument in "A Guess at the Riddle" (c. 1887–88, CP 1.363), is defended against Kempe in "The
Critic of Arguments" (1892, CP 3.423–424), and is worked into the *Monist* article "The Logic of Relatives"
(1897, 7(2): 161–217) and the existential graphs. The positive clause — every relation of adicity four or
more is a compound of triads — is argued in the same places, with "A sells C to B for the price D" as the
worked tetrad (CP 1.363). Koshkin's statement of the two clauses is the one used in `exegesis.md`.

The classification of triads into monadically degenerate, dyadically degenerate, and genuine is from "The
Logic of Mathematics: An Attempt to Develop My Categories from Within" (c. 1896, CP 1.473), which supplies
the father-of / mother-and-wife exemplars. Giving as the type case of a genuine triad is in the 1903 Lowell
Lectures (CP 1.345–347) and the 1904 letter to Lady Welby (CP 8.331), which also gives the aphorism "no
branching of a line can result from putting one line on the end of another." The sign definition with the
"genuine triadic relation" clause is in the 1903 *Syllabus* (CP 2.274; EP2: 272–273); the 1907 "Pragmatism"
manuscript gives semiosis as a "tri-relative influence not being in any way resolvable into actions between
pairs" (CP 5.484).

## What the secondary literature did with the reduction thesis

**Formalization and proof.** The thesis was widely dismissed after Löwenheim (1915) and Quine (1954) showed
that set-theoretic pairing reduces every relation to dyads. Skidmore (1971) named it "Peirce's thesis" and
raised the worry that any proof would have to restrict the allowed operations until the result came out —
gerrymandering. Herzberger (1981) proved a version in a "bonding algebra" whose valency rule forbids triple
junctions; Burch (1991) built Peircean Algebraic Logic (PAL), in which the teridentity predicate carries the
genuinely triadic content and the thesis is a theorem. Kerr-Lawson (1992) simplified Burch. Hereth and
Pöschel (2011) gave the mathematically strongest formulation and proof. Koshkin's preprint argues that all
of these tie the thesis to privileged operations, proposes an invariant formulation, and — the point of
contact with this paper — sketches an *informational* reading in which a relation is degenerate when its
places can be filled independently and genuine when fixing one place constrains the others, citing
"information integration" measures in biology as the analogous quantity.

**Semiotics.** The genuine-triad clause in the sign definition anchors the whole later literature on the
sign's correlates (object, interpretant, and the hexadic and decadic typologies). The literature reads the
clause logically: the sign relation is genuine because the interpretant is determined *with respect to* the
object, not merely by the sign. No semiotic treatment renders the relation as a dynamical system and asks
whether the object, which "determines and is not determined," would be inside or outside the causal whole.

**Sociology.** Peirce's triad entered organization studies through Bateson and through second-order
cybernetics rather than through the logic of relations, and the reduction thesis itself is absent from the
coordination literature. The lab's borrowing runs the other way: its criterion — a form is irreducible when
no partition reproduces its cause-effect structure — is a reduction test, and Peirce's thesis is the
earliest general claim about which relations pass such a test.

## The open gap

Every formal treatment of the reduction thesis works on **extensional relations**: sets of tuples, with
composition by relative product, junction, and identity. None asks the thesis's question of a **dynamical
system**: given elements that determine one another by rules, which arrangements contain a fact irreducibly
about three of them? IIT 4.0 computes exactly that — the irreducible distinctions of a system's cause-effect
structure, each with a mechanism and a purview — and the number of parties a distinction spans is the
adicity of the relation it asserts. The gap is a computation: read the adicity of every irreducible
distinction in small forms built from one-input rules (dyads), two-input rules (triads), and Peirce's own
exemplars, and see whether the genuine/degenerate line falls where he drew it. Koshkin's informational
reading predicts that it does; the lab's standing results on rings (whole-irreducible from copy rules) and
on emit-only sources (never in the core) predict that Peirce's line and the lab's Φ > 0 line will not
coincide, and say where.

## Sources

- Primary: `references.bib` — `peirce1897relatives`, `peirce1867categories`, `peirce_cp`, `peirce_ep2`.
- Secondary: `skidmore1971triads`, `herzberger1981remarkable`, `burch1991reduction`, `kerrlawson1992burch`,
  `hereth2011pal`, `koshkin_gerrymandered`.
- Instrument: `albantakis2023iit4`, `mayner2018pyphi`.
- Quotations were checked against the Commens Digital Companion and the textlog.de CP transcription; CP
  paragraph numbers are as given there. The Monist DOI resolves.
