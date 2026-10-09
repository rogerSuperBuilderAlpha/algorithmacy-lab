# Q219 — findings: who decides an insurance claim?

Two hypotheses confirmed, three refuted. The instrument control passed in every probe (chat_dyad dyadic
Φ=0.000, ats_triad_mediator triadic Φ=2.000), and `python -m org_frontier.classifier.validate` printed
`Instrument validated` in the same environment. Numbers reproduce from the named probe; per-state
profiles are in `results/`.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 pass-through pipe is triadic through closure | **confirmed** | `pipe` triadic, max Φ_MIP = 2.000, MIP 3 parts {C,E,A}, core {C,E,A} 2.000, Φ = 2.000 in 8/8 states (`probe_457_pipe`) |
| H2 threshold auto-approval triadic only through flagged claims | **refuted** | `gated` triadic as a whole, max Φ_MIP = 0.415 at state 111 only (1/5); core {C,E} 2.000, adjuster outside. The flagged-only clause held: E=0 states 000 and 100 read Φ = 0 (`probe_458_gated`) |
| H3 fraud-flag loop with override learning is triadic | **refuted** | `loop` triadic as a whole, max Φ_MIP = 1.000 (110: 0.415, 111: 1.000; 2/5); core {E,A} 2.000, claimant outside, the outcome H3's null named (`probe_459_loop`) |
| H4 loop survives removing override learning | **refuted** | `loop_nolearn` triadic as a whole, max Φ_MIP = 2.000 (110: 0.415, 111: 2.000; 2/6); core {C,A} 2.000, engine outside (`probe_459_loop`) |
| H5 freezing the claimant collapses the loop | **confirmed** | `loop_frozen_claimant` dyadic, max Φ_MIP = 0.000 in 0/5 states; sub-complex {E,A} 2.000 remains (`probe_460_liveness`) |

**Through-line.** Only the plainest design binds all three parties. The pass-through pipe, in which the
engine forwards, the adjuster copies, and the claimant reads the decision, is one irreducible loop in
every state at Φ = 2.0, replicating Q11's three-node rotating ring under the claims labels. Every design
that gives a party a conjunctive gate keeps the whole system triadic, yet its strongest core shrinks to a
pair, and the pair depends on where the gate sits. Threshold auto-approval leaves claimant and engine as
the core and the adjuster outside it, the structural form of a rubber stamp that study #39 described.
The fraud-flag loop with override learning closes into a private engine–adjuster pair and pushes the
claimant out, the counterpart of #39's {H, S} override dyad. Removing the learning edge does not restore
the triad; it swaps the excluded party, so claimant and adjuster form the core and the engine falls out.
Freezing the claimant makes the whole loop factor, confirming the liveness condition from q63. In short,
the answer to "who decides" depends on the gate: the claimant and engine under auto-approval, the engine
and adjuster under a learning fraud loop, the claimant and adjuster when the engine stops learning.

**Caveats.**
- **Whole system versus core.** In `gated`, `loop`, and `loop_nolearn` the whole system is triadic
  (Φ_MIP > 0) while a two-node subset carries a larger Φ (2.0) and wins the major complex. The
  pre-registered rule required all three in the major complex, so these read as refuted; under a
  whole-system-only rule they would read triadic.
- **In-silico.** Three-node deterministic Boolean models. The verdicts are evidence about these models
  and say nothing measured about any insurer, claimant, or adjuster.
- **Encoding.** Each variant is one encoding among many. The bit meanings in `methods.md` are stylized,
  and other encodings of "auto-approve" or "learn from overrides" may read differently.
- **Φ magnitude is ordinal** in this program; the 0.415 / 1.0 / 2.0 values rank states but are not
  compared across forms.
- **Few reachable states.** `gated` and `loop` reach five of eight states, and the irreducibility sits
  in one or two of them.

**Reproduce.** From the repo root with the venv active:
`python -m org_frontier.questions.q219_insurance_claim_adjudication.probe_457_pipe` (and `probe_458_gated`,
`probe_459_loop`, `probe_460_liveness`); or `python ci/reproduce.py q219-h1-pipe q219-h2-gated
q219-h3-h4-loop q219-h5-liveness`.
