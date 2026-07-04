# Registry — ten experiments on the literature

Ten quantitative archival reviews in the style of Simsek, Fox & Heavey (2023) and Simsek, Heavey, Fox
& Yu (2022): each treats a body of scholarship as a dataset, codes a screened corpus on a fixed
framework with independent coders, reports the practice/claim distributions with intercoder
reliability, and (where applicable) relates them to a citation-graph structure or to impact. Each
review lives in its own `org_frontier/reviews/<slug>/` directory with a pre-registered `hypotheses.md`,
a `FINDINGS.md`, and a `paper.md` written in the register of *Organizational Research Methods*.

The method and tooling are shared: [`RESEARCH_PLAYBOOK.md`](RESEARCH_PLAYBOOK.md),
[`METHODS_FOUNDATIONS.md`](METHODS_FOUNDATIONS.md), and [`lib/`](lib/) (harvest, reliability,
bibliometrics). Corpora are built with the academic semantic-search connectors (cleaner than raw
keyword search) plus citation snowball.

| # | slug | question about the literature | coded on |
|---|---|---|---|
| 1 | `iit_beyond_consciousness` | has IIT/Φ been applied beyond consciousness, to organizations and collectives? | substrate, evidence, claim type |
| 2 | `systematicity_consciousness_reviews` | how systematic are review articles in consciousness science? (a Simsek-Fox replication) | the seven systematicity practices |
| 3 | `new_form_construct_proliferation` | how many distinct labels does the literature give the "new organizational form"? | construct label, differentia, parent form |
| 4 | `algorithmic_management_claims` | what does the algorithmic-management literature assert vs. test? | knowledge-claim type, evidence, outcome |
| 5 | `phi_measure_fragmentation` | are the proposed integrated-information / complexity measures validated and connected? | measure family, validation target, ground-truth use |
| 6 | `platform_theory_borrowing` | which parent theories does platform-governance research import, and how has the mix shifted? | parent theory, borrowing mode, year |
| 7 | `causal_emergence_evidence` | is the causal-emergence literature conceptual, formal, or empirical, and is it converging? | evidence type, formalism, claim direction |
| 8 | `gig_work_motivation` | how do gig/platform-work reviews motivate themselves — gap-spotting or problematization? | motivation mode, assumption targeted |
| 9 | `collective_intelligence_substrates` | what substrates does collective-intelligence research span, and does it cite across them? | substrate, method, cross-substrate citation |
| 10 | `reproducibility_signaling` | how often do recent management empirical papers signal open data, code, or pre-registration? | data/code/preregistration statements, year |

## Common protocol
1. **Envision** — the question above, with 3–4 falsifiable hypotheses in `hypotheses.md` (committed
   before results).
2. **Explicate** — a stated corpus boundary (substantive + procedural gates).
3. **Execute** — corpus via Scholar Gateway / Consensus semantic search + S2 citation snowball;
   screened against the boundary; the screened-out set logged.
4. **Encode** — three independent coder passes on a fixed `coding_protocol.md`; Fleiss' κ via
   `lib/reliability.py`.
5. **Evaluate** — the coded distributions and, where the hypothesis needs it, the citation graph via
   `lib/bibliometrics.py`.
6. **Exposit** — `FINDINGS.md` (verdicts + κ + limitations) and `paper.md` (~3,000 words, ORM register).

## Shared limitation, stated once
The coders are LLM agents applying a fixed codebook, not trained human raters; reliability among
agent passes is high but is not a substitute for independent human coding. Each paper states this.
Corpora are bounded by the search connectors' coverage and by English-language indexing.
