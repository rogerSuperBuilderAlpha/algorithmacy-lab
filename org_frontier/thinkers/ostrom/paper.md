# Monitors who are the monitored: Ostrom's design principles under exact Φ

<code + data: org_frontier/thinkers/ostrom/ ; probes #434–#438 in probes/PROBES.md ; standard in
org_frontier/thinkers/PAPER_STANDARD.md>

## Abstract

Ostrom (1990) distilled the long-enduring commons into eight design principles, four of them structural:
defined boundaries, monitors who are the appropriators, graduated sanctions, and nested enterprises; the
mechanism beneath them is a contingent self-commitment — I comply if the rest of you do. The Coleman paper
in this series found that an effective norm drops the sanctioned party out of the complex. This paper asks
whether Ostrom's structures avoid that. They do. When each of three appropriators complies if the others
comply or if the other two jointly sanction, and sanctions when either other defects, the major complex is
the three compliance nodes at Φ = 2.862 with every appropriator in it (H1 confirmed), and the form rests at
all-comply with no sanction standing, each single lapse returning to rest in four steps (H4 confirmed) —
where Coleman's norm rests only with the sanction standing. A clique of contingent commitments is a whole of
three at 6.000 against the enforcer's star at 3.000, but the enforcer holds no edge over anyone (H2
partial). Nesting two cliques under a federation does not make the seven one: exclusion returns a single
clique at 6.000 and the federation is outside the core and indispensable (H3 refuted). A defined boundary
leaves the enterprise untouched by an outsider; a breach leaves the core untouched too and makes the
outsider indispensable (H5 partial). Ostrom's mutual monitoring keeps everyone in the structure, and the
lab's recurring figure — the party outside the complex that the complex cannot do without — returns as the
federation and the outsider. Results are about Boolean models.

## Introduction

Coleman argued that a norm needs closure: the parties a third can harm must be tied to each other so they
can combine to sanction him. The Coleman paper in this series confirmed the mechanism and priced it. When
the sanctioners close, compliance becomes a fixed point — and the two sanctioners become the complex, at
Φ = 0.369, with the sanctioned party outside it as a background condition. An effective norm, on that
rendering, is a structure in which the governed have left the whole.

Ostrom's cases describe something else. In the Alanya fishery, the Valencian *huertas*, the Swiss alpine
commons, the appropriators are the monitors: "Monitors, who actively audit CPR conditions and appropriator
behavior, are accountable to the appropriators or are the appropriators" (1990, p. 90). Monitoring is "a
by-product of their own strong motivations to use their water rotation turn to the fullest extent" (p. 95);
the sanctions actually imposed are "surprisingly low" (p. 94); and compliance rests on a "contingent
self-commitment": "I commit myself to follow the set of rules we have devised in all instances except dire
emergencies if the rest of those affected make a similar commitment and act accordingly" (p. 100). There is
no sanctioned party who does not also sanction. Whether that keeps everyone in the complex is the question
this paper puts to the same instrument the Coleman paper used.

Five hypotheses were fixed before computing. Whether mutual monitoring keeps every appropriator in the
structure (H1); whether self-governance is a tighter whole than the enforcer's star and division binds
nothing (H2); whether nested enterprises are one whole with each layer still a whole (H3); whether
compliance rests with the sanction retired (H4); and whether a defined boundary keeps an outsider out while
a breach changes the whole (H5). Two confirmed, two partial, one refuted.

## Ostrom's account

*Governing the Commons* opens with Hardin's (1968) tragedy and the two remedies attached to it: a central
authority that monitors and sanctions — "Leviathan" (pp. 8–12) — and the division of the commons into private
holdings (pp. 12–13). The book's cases are a third way: appropriators who devise, monitor, and enforce their
own rules, beginning with the Alanya fishers who rotate through named sites in a fixed order so that
"cheaters are observed at low cost by those who most want to deter another cheater at that particular time
and location" (p. 95; pp. 18–21).

Chapter 3 distills the long-enduring cases into eight design principles (Table 3.1, p. 90). Boundaries:
"Individuals or households who have rights to withdraw resource units from the CPR must be clearly defined."
Monitoring: the monitors "are accountable to the appropriators or are the appropriators." Graduated
sanctions, assessed "by other appropriators, by officials accountable to these appropriators, or by both."
Nested enterprises: "Appropriation, provision, monitoring, enforcement, conflict resolution, and governance
activities are organized in multiple layers of nested enterprises." The mechanism beneath them is the
contingent self-commitment quoted above, which makes compliance conditional on the others' compliance and
makes monitoring worth doing: "Once appropriators have made contingent self-commitments, they are then
motivated to monitor other people's behavior" (p. 100). Levi's term for the result is quasi-voluntary
compliance (p. 94).

Ostrom (2000) restates the argument as norm evolution; Ostrom (2009) generalizes it into a framework for
social-ecological systems; Cox, Arnold, and Villamayor Tomás (2010) review 91 cases and find the principles
broadly supported.

## From claims to forms

An **appropriator** i has a compliance bit c_i and, where sanctions are modeled, a sanction bit s_i.
**Contingent self-commitment**: c_i complies when the others comply, c_i' = c_j ∧ c_k. **Monitoring by the
monitored**: s_i sanctions when either other defects, s_i' = ¬c_j ∨ ¬c_k, and c_i also complies when
jointly sanctioned, c_i' = (c_j ∧ c_k) ∨ (s_j ∧ s_k) — the Coleman paper's "yields only to a joint
sanction," with every party now on both sides. The **structure** is the major complex; **value added** V
and **positional advantage** are the Coleman paper's quantities, and a deleted variable reads 0. The
**Coleman contrast** is that paper's closed norm: A' = B ∧ C; B' = ¬A ∨ C; C' = ¬A ∨ B.

Nine forms. **mutual** (six nodes, above). **coleman_closed**. **leviathan**: L' = ¬(c1 ∧ c2 ∧ c3), c_i' = L
— the enforcer sanctions when anyone defects and everyone complies when sanctioned. **private**: c_i' = c_i.
**self**: the clique of contingent commitments. **nested**: two cliques a and b whose delegates a1, b1 also
require the federation, a1' = a2 ∧ a3 ∧ F, with F' = a1 ∧ b1; **unnested**: the two cliques alone.
**bounded**: self plus an outsider O' = c1 who watches and is not read; **breached**: bounded with
c1' = c2 ∧ c3 ∧ O, a member whose compliance turns on the outsider.

The rendering's risk is the same as the Coleman paper's: sanctions respond by negation and lift at once, so
graduated sanctions — which need memory and a source of lapses — are not modeled.

## Hypotheses

Fixed in `hypotheses.md` before any form was run.

- **H1 (Ostrom) — the monitored are in the structure.** {c1, c2, c3} ⊆ core(mutual); A ∉ core(coleman_closed).
  *Prior:* open.
- **H2 (Ostrom) — self-governance against Leviathan and privatization.** self's core is all three at Φ above
  leviathan's; L has positive advantage; private has no complex. *Prior:* with on private; open otherwise.
- **H3 (Ostrom) — nested enterprises.** nested's core is all seven; each local triad irreducible inside it;
  unnested is two triads. *Prior:* open.
- **H4 (Ostrom) — quasi-voluntary compliance.** 111000 is fixed in mutual; each single lapse returns to it;
  coleman_closed rests at 111. *Prior:* with.
- **H5 (Ostrom) — boundaries.** bounded has self's core and Φ with V(O) = 0; breached differs in core or Φ.
  *Prior:* with on bounded; open on breached.

## Methods

**Instrument.** Exact IIT-4.0 Φ (Albantakis et al., 2023) via PyPhi (Mayner et al., 2018); expression
machinery from the Coleman paper's `forms.py`; subsystem Φ via `new_big_phi.sia` at a reachable state.

**Control.** Every probe first runs the conjunctive triad (Φ = 2.000000, core {A, M, B}). All passed.

**Procedure.** Five probes, one per hypothesis. Results in `results/`, registered in `ci/reproduce.json`
(#434–#438); the six- and seven-node probes take five and ten minutes.

**Scope.** Results are about Boolean models. No commons is measured.

## Results

| form | Φ_MIP | major complex | core Φ | V by party | fixed points |
|---|---|---|---|---|---|
| coleman_closed | 0 | {B, C} | 0.369 | all .369 | 111 |
| mutual | 0.830 | {c1, c2, c3} | 2.862 | all six .862 | 111000 |
| leviathan | 3.000 | {L, c1, c2, c3} | 3.000 | all 3 | none |
| private | 0 | {c3} | 1.000 | all 0 | all 8 |
| self | 6.000 | {c1, c2, c3} | 6.000 | all 6 | 000, 111 |
| unnested | 0 | {a1, a2, a3} | 6.000 | all 0 | 4 |
| nested | 2.000 | {a1, a2, a3} | 6.000 | F 6, a1 4, b1 4, others 0 | 0000000, 1111111 |
| bounded | 0 | {c1, c2, c3} | 6.000 | c 6, O 0 | 0000, 1111 |
| breached | 2.000 | {c1, c2, c3} | 6.000 | c 6, O 6 | 0000, 1111 |

*Table 1. All forms. In nested, both local triads have subsystem Φ = 6.000 at the all-on state (post hoc).*

### H1 — the monitored are in the structure: CONFIRMED

In mutual the major complex is {c1, c2, c3} at Φ = 2.862: the three appropriators' compliance, every one of
them in. The whole of six is irreducible at 0.830 but excluded by the tighter three. The sanction bits are
outside the core and each adds 0.862 — delete any one and the core's Φ falls from 2.862 to 2.000, the plain
conjunctive triad's value. Beside it, Coleman's closed norm has the two sanctioners as the core at 0.369 and
A outside. Both clauses held. Where the sanction runs one way, the sanctioned party leaves the complex;
where it runs every way, the sanctioned parties are the complex.

### H2 — self-governance against Leviathan and privatization: PARTIAL

The clique of contingent commitments is a whole of three at 6.000, each member adding 6.000. The enforcer's
star is a whole of four at 3.000 — half — with the enforcer and every appropriator adding 3.000 alike, so
the enforcer's positional advantage is 0. Privatization leaves three self-holding nodes, and PyPhi counts a
self-holding node as a complex of one at 1.000, so "no complex" failed on a singleton. Two of four clauses
held: self-governance is the tighter whole and all three are in it; the Leviathan has no edge over those it
governs, and division does not bind but does not read as nothing.

### H3 — nested enterprises: REFUTED

Two cliques alone are two complexes of three at 6.000, and the whole of six is reducible. Bind their
delegates to a federation and the whole of seven becomes irreducible at 2.000 — but exclusion returns a
single local clique at 6.000, not the seven. The federation F is outside the core and indispensable: delete
it and the delegate it fed reads 0, the clique collapses, and F's value added is 6.000. The delegates add
4.000; the rank and file 0. The pre-registered check of the local triads inside the nest evaluated them at
the state where the whole's major complex is maximal, at which group b is off; at the all-on state both
triads are irreducible at 6.000, {a1, a2, a3, F} at 2.000, and {a1, b1, F} at 2.000 (post hoc, disclosed).
One clause of three held. The layers stay wholes; the nest is not one.

### H4 — quasi-voluntary compliance: CONFIRMED

mutual has one fixed point, 111000: all comply, no sanction standing. From each single lapse — one
appropriator defects, no sanction up — the form returns to that rest in four steps: the other two sanction,
the defector complies under the joint sanction while the others' contingent compliance wavers, all three
sanction, all comply, the sanctions retire. Coleman's closed norm has one fixed point, 111, the sanction
standing. All three clauses held.

### H5 — boundaries: PARTIAL

An outsider who reads the commons and is not read changes nothing: bounded has self's core at 6.000 and
V(O) = 0, and the whole of four is reducible. Let a member's compliance turn on the outsider and the core is
still {c1, c2, c3} at 6.000 — but the whole of four is now irreducible at 2.000 and V(O) = 6.000: delete O and
c1 reads 0 and the clique collapses. The breach did not change the core or its Φ, which is what the
hypothesis asked; it made the outsider indispensable, which it did not. One clause of two held.

## Discussion

The contest with Coleman is decided on H1 and H4. Coleman's closed norm and Ostrom's mutual form have the
same sanction — a party yields only when two others jointly sanction — and differ in one thing: in Coleman's
form A never sanctions, and in Ostrom's everyone does. That difference moves the sanctioned parties from
outside the complex to being the complex. In Coleman's form the core is the two sanctioners at 0.369 and A is
a background condition; in Ostrom's the core is the three compliances at 2.862, and the sanction apparatus
is outside it, each bit adding 0.862 to a triad that would be the plain conjunctive triad at 2.000 without
it. The fixed points differ the same way. Coleman's norm rests with the sanction standing; Ostrom's rests
with it retired, and a lapse calls it up and puts it away in four steps. That is her "surprisingly low"
sanctioning as a dynamical property: the sanction is a transient, not a state.

What keeps everyone in is the contingent self-commitment, not the mutuality of the sanction alone. The c_i
rule has two disjuncts: comply if the others comply, or if jointly sanctioned. The first is the clique of
contingent commitments that is a whole of three at 6.000 on its own (H2). The second is Coleman's rule. Add
the sanction bits to the clique and its Φ falls to 2.862 — the sanction is a cost to integration here as it
was in the Coleman paper — but the appropriators stay in. Under Coleman's rule alone they did not.

The Leviathan is the second result. The star with the enforcer at the center is a whole of four at 3.000 in
which the enforcer adds exactly what each appropriator adds and holds no advantage. Ostrom's objection to
central enforcement was informational and fiscal; the instrument adds that it is not even hierarchical in
the sense of giving the center an edge. It is half as integrated as the clique it replaces and flat.

The nest is the Coleman parents result one level up. There, a tie between the parents made the parents the
core and dropped the children; here, a federation above two cliques does not become the core — a local
clique does — but the federation is outside and indispensable, the delegates add 4.000, and the rank and
file add 0. Ostrom's principle says the layers are semi-autonomous, and the instrument agrees to the extent
that each clique is irreducible at 6.000 inside the nest; it disagrees that the nest is one. The seven are
irreducible at 2.000 and excluded by the three. The federation has the structural position Serres's parasite
had: not in the complex, and the complex cannot do without it. The outsider in the breached boundary has it
too — V(O) = 6.000, outside the core. A boundary, on these forms, is what keeps that position from opening.

## Limitations

One rendering per claim. Sanctions lift on compliance without memory, so graduated sanctions — the
principle most specific to Ostrom — were not modeled; a stochastic counter is the natural next form. The
privatization clause of H2 was mis-specified: a self-holding node is a complex of one in PyPhi, and "no
complex" should have read "no complex above one." H5's breach clause asked for a change in core or Φ where
the change came in value added. H3's local-triad clause was evaluated at a state that turned one group off;
the post-hoc check at the all-on state is reported and does not alter the verdict. A deleted variable reads
0, so deleting F or O collapses any conjunction that read it — the indispensability numbers are partly this
convention. Forms are three to seven nodes.

Results are about Boolean models. No commons is measured.

## Conclusion

Ostrom's fourth principle, that the monitors are the appropriators, is what keeps the governed inside the
structure that governs them: under Coleman's one-way sanction the sanctioned party leaves the complex, and
under mutual sanction the sanctioned parties are the complex, resting at compliance with the sanction
retired. Self-governance is twice as integrated as the enforcer's star, and the enforcer has no edge. What
Ostrom's structures do not do is make a nest one whole; the layers stay wholes and the federation stands
where Serres's parasite stood — outside, and necessary.

## References

Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0. *PLoS Computational Biology*, 19(10),
e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Coleman, J. S. (1988). Social capital in the creation of human capital. *American Journal of Sociology*,
94(Supplement), S95–S120. https://doi.org/10.1086/228943

Cox, M., Arnold, G., & Villamayor Tomás, S. (2010). A review of design principles for community-based natural
resource management. *Ecology and Society*, 15(4), 38. https://doi.org/10.5751/ES-03704-150438

Hardin, G. (1968). The tragedy of the commons. *Science*, 162(3859), 1243–1248.
https://doi.org/10.1126/science.162.3859.1243

Mayner, W. G. P., et al. (2018). PyPhi: A toolbox for integrated information theory. *PLoS Computational
Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343

Ostrom, E. (1990). *Governing the commons: The evolution of institutions for collective action*. Cambridge
University Press. https://doi.org/10.1017/CBO9780511807763

Ostrom, E. (2000). Collective action and the evolution of social norms. *Journal of Economic Perspectives*,
14(3), 137–158. https://doi.org/10.1257/jep.14.3.137

Ostrom, E. (2009). A general framework for analyzing sustainability of social-ecological systems. *Science*,
325(5939), 419–422. https://doi.org/10.1126/science.1172133

## Appendix A — Forms

All in `forms.py`. `∧` AND, `∨` OR, `¬` NOT; a deleted variable reads 0; {j, k} are the other two of {1, 2, 3}.

- **mutual** c_i' = (c_j ∧ c_k) ∨ (s_j ∧ s_k); s_i' = ¬c_j ∨ ¬c_k.
- **coleman_closed** A' = B ∧ C; B' = ¬A ∨ C; C' = ¬A ∨ B.
- **leviathan** L' = ¬(c1 ∧ c2 ∧ c3); c_i' = L.
- **private** c_i' = c_i.
- **self** c_i' = c_j ∧ c_k.
- **nested** a1' = a2 ∧ a3 ∧ F; a2' = a1 ∧ a3; a3' = a1 ∧ a2; same for b; F' = a1 ∧ b1.
- **unnested** the two cliques without F.
- **bounded** self plus O' = c1.
- **breached** bounded with c1' = c2 ∧ c3 ∧ O.

## Appendix B — Reproduction

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_monitors     # ~5 min
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_solutions
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_nested       # ~10 min
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_compliance
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_boundary
```

Registered as `thinkers-ostrom-h1-monitors` … `thinkers-ostrom-h5-boundary` in `ci/reproduce.json`; H1 and
H3 are marked slow.
