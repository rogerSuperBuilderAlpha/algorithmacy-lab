# Update order on quorum hubs: members act one after another in a fixed order

Fixed before this study's computation.

## Gap

#62 (sequential update) found 6/6 update orders dyadic on the three-node conjunctive form, and
`continuous_time_invariance` found 0/24 corpus forms triadic under sequential update; both on n = 3
forms. The four-node counting quorum hubs (OR3, MAJ3, AND3) used by the noise and timing studies
(`lazy_update`, `memory_rules`, `delay_quorum`) have not been run under a fixed update order. Every
noisy-quorum backlog lists "asynchronous update".

## Model

Mediator S over three parties; S commits OR3, MAJ3 or AND3 over the parties' bits; each party copies S.
No noise (a noisy sequential composition is not conditionally independent and is out of scope). One
time step = the four nodes update one after another in a fixed order, each reading the current
(already partly updated) state. All 4! = 24 orders × 3 forms = 72 cases.

For each reachable state, φ of every subset from `new_big_phi.reachable_subsystems`; whole Φ = maximum
full-system φ over states; top tie set = subsets within 1e-9 of the largest subset φ.

Controls: the composed TPM is deterministic (0/1 entries); the synchronous hub reproduces the known
whole Φ (OR3 3.0, MAJ3 0, AND3 3.0); the #62 sequential construction (`timescale_separation`
`sequential_tpm`) gives the same TPM as this study's composition for one order.

## Outcomes (threshold 1e-9)

- H1: for OR3 and for AND3, at least one of the 24 orders gives whole Φ > 1e-9.
- H2: the order S first, then P1, P2, P3 gives whole Φ > 1e-9 for OR3 and AND3.
- H3: every order in which all three parties update before S gives whole Φ ≤ 1e-9, for every form.
- H4: MAJ3 gives whole Φ ≤ 1e-9 under every order.
- H5: OR3 and AND3 have the same number of orders with whole Φ > 1e-9.
