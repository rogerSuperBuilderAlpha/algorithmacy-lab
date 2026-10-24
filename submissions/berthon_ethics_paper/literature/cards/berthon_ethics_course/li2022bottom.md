---
citekey: li2022bottom
title: "A Bottom-Up End-User Intelligent Assistant Approach to Empower Gig Workers against AI Inequality"
authors: Li, Toby Jia-Jun and Lu, Yuwen and Clark, Jaylexia and Chen, Meng and Cox, Victor and Jiang, Meng and Yang, Yang and Kay, Tamara and Wood, Danielle and Brockman, Jay
year: 2022
type: article
doi: 10.1145/3533406.3533418
venue: "2022 Symposium on Human-Computer Interaction for Work (CHIWORK), Durham NH, ACM, 10 pp."
source_basis: full-text
pages_read: "arXiv 2204.13842v1 PDF pp. 1-8 (all text before the references)"
source_url: https://arxiv.org/abs/2204.13842
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/M2/li2022.txt
sha256: 256a1292f54e357e8c5fa04965cb5a7525b67e6ee87d64b7998e5568827dbfc6
manuscript_lines: [223, 337]
ledger_rows: [P6-016]
verified: true
written: 2026-10-14
---

## Summary
Li and colleagues, HCI and sociology researchers at Notre Dame and Syracuse, write a position paper on "AI
inequality" in gig work. It has two sources: a technology divide over who can use AI, and a data divide over
who owns the data (p. 1). Platforms collect data from all drivers and customers and run matching and pricing
algorithms "designed to optimize for platforms' best interests", while each worker can at most self-track
(p. 2). The authors propose a bottom-up network of end-user-programmable intelligent assistants. Each worker
runs an assistant on the phone used for the platform app. It records the time, distance and proposed pay of
every task offered, and the worker's accept or decline. It shares those data in real time across the network,
models the market, and recommends tasks according to the worker's own goals (pp. 4-5). A prototype crawler,
Crepe, reads task data from platform app screens without platform cooperation (p. 5). The network could
estimate pay bias and support collective action (pp. 5, 7). Because the approach needs no platform data
access, it can be deployed now, while platform cooperation "contradicts directly their interests" (p. 7). The
paper reports formative interviews and studies but no evaluation of the assistant.

## Key facts it relies on
- AI inequality stems from "the technology divide" and "the data divide" (abstract, p. 1).
- A "network of end-user-programmable intelligent assistants" lets workers "share data among a group of
  workers" (abstract, p. 1).
- The approach requires no "cooperation, access to additional data, or software access from the platform",
  since platforms may resist "because it might work against their financial interests" (p. 2).
- Platforms hold a "monopoly on data and algorithms"; neither rider nor driver knows the other's price (p. 2).
- Formative work: six semi-structured interviews with rideshare drivers and two sessions with labour
  organisers at Chicago Rideshare Advocates (p. 3).
- The assistant collects each task's "time needed, distance, proposed pay" and shares it "with the assistants
  of other workers in the same network in real-time" (p. 4).
- The Crepe crawler extracts on-screen task data and "listens to the worker's input into the platform app
  (e.g., accepting a task)" (p. 5).
- The assistant "is owned by an individual worker, is programmed by an individual worker" (p. 5).
- Platform-cooperative alternatives are harder because reducing AI inequality "contradicts directly their
  interests" (p. 7).

## Critical notes from the literature
- Facet M2 (`literature/facets/M2_algorithm_studies.md:134, 170`): the closest existing counter-delegation
  proposal; "a position paper, with no evaluation".
- Facet M2 (`:153`): Li et al. pool data across workers, so the paper should say whether its user-side agents
  are individual or networked.
- Facet N5 (`literature/facets/N5_prior_work_gap.md:187`): each half of the paper's proposal exists separately
  (the user-side record here; contestation elsewhere), and no searched work pairs it with a binding
  independent adjudicator.
- The authors flag their own risks: worker-side optimisation may worsen service for "undesirable" customers,
  and demographics can be proxied by geography (p. 7). GUI crawling cannot see the customer's price (p. 5).
  The assistant is a new party in the transaction whose design choices affect third parties, which bears on
  the manuscript's point about Kolt at line 225.
- AUDIT_05 M2-33 (`literature/audit/AUDIT_05.md:262`) confirmed the facet's quotations against the preprint.

## Key topics covered
gig work, AI inequality, data divide, end-user programming, intelligent assistants, rideshare drivers, data
sharing, GUI crawling, worker collective action, platform power

## Where the manuscript uses it
- **Line 223**, "Li and colleagues (2022) outline assistants that would run on a gig worker's side, logging
  offers and pay and pooling the data across workers." Source: pp. 1, 4-5. **holds.** "Outline" fits a
  position paper. Offers and proposed pay are logged (p. 4), accept/decline input is captured (p. 5), and data
  are shared across the network (pp. 1, 4).
- **Line 337, reference entry**: Li et al. (2022), *2022 Symposium on Human-Computer Interaction for Work*
  (pp. 1-10), ACM, DOI 10.1145/3533406.3533418. **holds**: the arXiv copy prints the ACM reference format with
  CHIWORK 2022, "10 pages" and this DOI (p. 1). The ten authors and their order match.

## Verifier notes
- Recomputed sha256 of `li2022.txt`: matches. Crossref (10.1145/3533406.3533418): ten authors in the card's order, *2022 Symposium on Human-Computer Interaction for Work*, pp. 1-10, ACM, 8 Jun. 2022. The bib booktitle adds "(CHIWORK)" and its note ("read in part") is stale; otherwise no disagreement.
- The two-column layer interleaves; I checked each fact by page and line. Confirmed: technology and data divides, "network of end-user-programmable intelligent assistants" (p. 1); no platform "cooperation, access to additional data, or software access", "against their financial interests", "monopoly on data and algorithms", neither party knows the other's price, "optimize for platforms' best interests" (p. 2); six interviews and Chicago Rideshare Advocates (p. 3); "time needed, distance, proposed pay" shared "in real-time" (p. 4); Crepe, "listens to the worker's input", "owned by an individual worker" (p. 5); "contradicts directly their interests" and the "undesirable" customers risk (p. 7).
- L223 and L337 verdicts confirmed (**hold**).
- Verified 2026-10-14.
