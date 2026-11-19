# Technical Appendix: Computing the Triad

[DRAFTED by Claude, 26 Oct 2026, v3. Companion to the proposal. Every result below reproduces from the submission repository ([REPOSITORY URL]) with `python reproduce.py` (17 checks, about two minutes) and `pytest` (19 tests).]

[Current version: https://docs.google.com/document/d/1fhM_C7pz6e3sR7aXY3_89oys06B-UyK9Vyf93bt1zFA/edit — the author's Google Doc supersedes this draft.]

## A. Encoding a coordinative structure

A structure with *n* parties is a deterministic Boolean network on *n* nodes. Node *i* holds party *i*'s state, and a rule sets its next state from the current states of the parties it reads. Rules are written as expressions over party labels using `and`, `or`, `not`, `xor`, `0` and `1` (`irreducibility/rules.py`). The parser rejects anything else, so an encoding cannot execute code.

An encodings file (`encode/SCHEMA.json`) holds one structure and several encodings. Each encoding gives:
- **role:** `rival` for a competing reading of the same arrangement, `design` for a deliberate change to it;
- **rules:** one per party;
- **evidence:** for every rule, a source, a locator and a verbatim quotation;
- **alternative:** for the mediator's rule, the reading the evidence does not rule out, and why;
- **predicted:** the verdict and core, with a reason, fixed before computing;
- **bypass (optional):** a direct tie for the contingency test.

Strict mediation, for example:

| Party | Rule | Reading |
|---|---|---|
| Driver D | D′ = P | acts on the platform's signal |
| Platform P | P′ = D and R | commits only when both parties are in |
| Rider R | R′ = P | responds to what the platform shows |

## B. The computation (`irreducibility/core.py`)

1. **Transition matrix.** `tpm_from_rules` builds the 2ⁿ × n state-by-node matrix, little-endian (index 0 = first party), as PyPhi expects. `cm_from_rules` builds the connectivity matrix by a flip test: cm[i, j] = 1 iff flipping node *i* can change node *j*'s next state.
2. **Reachable states.** These are states with at least one predecessor under the dynamics; PyPhi analyzes only these.
3. **Φ over the MIP.** For each reachable state, `pyphi.new_big_phi.sia` returns system integrated information over the minimum-information partition (Albantakis et al., 2023), together with the partition itself.
4. **Verdict.** The structure is **triadic** iff Φ > 10⁻⁹ in at least one reachable state, read at the most-integrated state; otherwise it is **dyadic**. The test uses the MIP, not the complete cut. The complete cut severs any coupled pair and would call every coupled dyad a triad.
5. **Major complex.** `pyphi.new_big_phi.maximal_complex` is maximized over reachable states. It names the parties bound into the irreducible core.
6. **Interpretation.** Only the binary verdict and core membership are interpreted. Φ magnitude depends on the encoding and is at most ordinal.

**Environment.** PyPhi is pinned to commit `b78d0e342` of its IIT-4.0 line (`requirements.txt`), with Python 3.10 or later; the code is tested on 3.12.

## C. Controls (`python -m irreducibility.validate`; every script refuses to run if they fail)

| Control or form | Rules (W, S, C) | Expected | Observed |
|---|---|---|---|
| Factoring control | S, W, C | dyadic | dyadic, Φ = 0.000 |
| Irreducible control | S or C, W and C, W xor S | triadic | triadic, Φ = 0.830 |
| Strict-mediation triad | S, W and C, S | triadic | triadic, Φ = 2.000 |
| Chat dyad; dyadic gig model; feedback that breaks liveness | (see code) | dyadic | dyadic, Φ = 0.000 each |
| Gig "false dyad" | not S, W and C, C and not S | triadic | triadic, Φ = 2.000 |

## D. Structural readings

- **Mediator position** (`irreducibility/regime.py`):
  - *dyadic*: the structure factors.
  - *BYPASSED*: triadic, but the mediator is outside the core.
  - *CAPTURE*: the mediator is in the core and some party is not.
  - *BOTTLENECK*: all parties are in the core, and freezing the mediator at 0 or 1 leaves the others unable to coordinate.
  - *ENRICHER*: all parties are in the core, and the others still coordinate with the mediator frozen.
- **Intrinsic or contingent** (`irreducibility/contingency.py`). Restore the forbidden direct tie (the downstream party reads the upstream party) and recompute the core.
  - *Contingent*: the intermediary leaves the core.
  - *Intrinsic*: it stays, with no loss of Φ.
  - *Partial*: it stays, but Φ falls.
  - *Reducible*: it was never in the core.
- **Spread across rival encodings** (`irreducibility/spread.py`, `analyze.py`): verdict agreement, the Φ gap, and the Jaccard overlap of the cores. For every pair of rival encodings with different verdicts, the analysis names each single rule whose swap flips the verdict.

## E. The AI step

| Component | File | Function |
|---|---|---|
| Schema | `encode/SCHEMA.json` | the format a drafter must produce |
| Drafter | `encode/PROMPT_drafter.md` | rival encodings with verbatim evidence, an alternative and a fixed prediction; commit, convey or store decided from evidence; pools encoded with `or` |
| Adversary | `encode/PROMPT_adversary.md` | the most different readings the evidence still permits on three forces (commit vs convey, substitutability, spectators and outside options), or a statement of which passage rules each one out |
| Gate | `irreducibility/encode_check.py` | rejects a missing rule, a rule with no evidence, a quotation not found verbatim in the source, a mediator rule with no alternative, or a missing prediction; never computes Φ |

**Logged runs.** Claude Sonnet 5.5 ran on 26 Oct 2026 with the committed prompts and the case description only, with no tools and no access to the human encodings.

| Run | Output | Result |
|---|---|---|
| Gig dispatch, drafter | `examples/01_gig_dispatch/ai_draft.json` | admissible; two rival encodings identical to the human encodings A and B; both predictions held; the driver pool was missed |
| Gig dispatch, adversary | `examples/01_gig_dispatch/ai_draft_plus_adversary.json` | added the driver pool (computed dyadic, core {P,R}; predicted triadic, so the prediction **failed**) and the substitute direct tie (computed triadic, core {D,R}, platform bypassed; predicted dyadic, so it **failed**); declined a complementary tie as unsupported |
| Insurance claim, drafter | `examples/02_insurance_claim/ai_draft.json` | left rules unwritten for four of five designs and stated the missing evidence; the gate **rejected** the file (9 problems) |

## F. Worked examples (`examples/`; stipulated descriptions, not field data)

The lab's results for these structures were known when the examples were written, so their predictions record the naive reading, not a blind test.

| Example | Encodings | Results |
|---|---|---|
| 01 Gig dispatch | 3 rival, 5 design | Platform commits: triadic, Φ = 2.0, core {D,P,R}, bottleneck, intrinsic. Driver's relay: dyadic. Pooled drivers: dyadic, core {P,R}. Flip rule: P: `D and R` → `D`. Outside options O1–O5: bottleneck, enricher, capture {D,P}, capture {P,R}, bypassed {D,R}. |
| 02 Insurance claim | 5 design | Pipe: triadic, core {C,E,A}. Threshold auto-approval: core {C,E}, capture. Fraud loop with learning: core {E,A}. Loop without learning: core {C,A}, engine bypassed. Frozen claimant: dyadic. 2 of 5 naive predictions held. |
| 03 Code-review gate | 2 rival | Maintainers wait for CI: triadic, Φ = 1.0, core {A,M}, gate bypassed. Maintainers approve on the diff alone: core {A,G,M}, gate enricher. |
| 04 Dealer vs clearinghouse | 2 design | Dealer under a ban on direct sales: core {U,I,V}, contingent (Φ lost when bypassed: 2.0). Clearinghouse: intrinsic (Φ lost: 0.0). |

## G. Reference results (`studies/`)

| Check | Result |
|---|---|
| `census` | 256 strict-mediation structures (4 worker rules × 16 mediator rules × 4 counterpart rules). 24 are triadic; 24/160 where the mediator reads both parties and 0/96 otherwise. |
| `field-mocks` | Ten invented organizations: the verdict matched the reading fixed before computing in 9/10 (support-ticket triage read triadic against a dyadic prediction). 4 flip under a second defensible encoding. |
| `mediator-in-core`, `enricher-regime` | Over 500 random mediated forms: dyadic 44.4%, bypassed 18.8%, capture 28.2%, bottleneck 2.6%, enricher 6.0%. A platform's core is itself plus the parties without an outside option (60/60). |
| `contingent-irreducibility` | The bypass test realizes the intrinsic / contingent / partial / reducible taxonomy. |
| `design-operations` | Three levers (binding, liveness, requirement), each with a build operation and an exact inverse break. |
| `thompson-ordering` | Pooled Φ = 0, sequential Φ = 2.0, reciprocal Φ = 2.0: the top step of Thompson's ordering collapses. |
| `adversarial-coding` | An adversary limited to evidence-permitted readings flips the point verdict on 101/101 contested accounts; a coder-agreement interval brackets the adversarial reading in only 22. |
| `proxies` | ΦID Φ_R and whole-minus-sum Φ from simulated trajectories separate dyadic from triadic at rank-AUC 0.563 and 0.629. |

## H. Planned specifications (Stage 2)

- **Encoding module.**
  - Input: transcripts, documents and logs, with locators.
  - Process: drafter and adversary on an open-weight and a commercial model; a researcher's approval recorded per encoding.
  - Agreement: AI drafter against two human coders, Krippendorff's α per rule and per bit, target ≥ 0.80.
- **Strategic model.**
  - Rows: structural position (verdict, core, regime, intrinsic or contingent), indexed by actor (platform, worker, counterpart, regulator).
  - Columns: design levers (add or remove binding; break or restore liveness; require all parties or allow substitutes; open or close a bypass; change an outside option).
  - Cells: the computed consequence (who stays bound, who is freed, whether the mediator survives).
  - Scope: structural only, with no claims about economic value.
- **Validation.** 10–15 published platform and algorithmic-management cases encoded from their own text. For each case, the verdict under every defensible encoding and the detail that would decide between them. The gig-dispatch interview packet (`protocol/`) will be fielded under ethics approval.

## References

Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Mayner, W. G. P., Marshall, W., Albantakis, L., Findlay, G., Marchman, R., & Tononi, G. (2018). PyPhi: A toolbox for integrated information theory. *PLOS Computational Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343
