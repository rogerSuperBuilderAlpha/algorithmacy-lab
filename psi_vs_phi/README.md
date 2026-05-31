# psi_vs_phi — does the MaxCal information ψ track exact IIT‑4.0 Φ?

A research project extending Kearney (2026), *Information as Maximum‑Caliber Deviation: A bridge
between Integrated Information Theory and the Free Energy Principle* (arXiv:2605.12536).

Kearney defines an information measure **ψ** as the deviation of a system's dynamics from a
maximum‑caliber path ensemble, re‑derives IIT 3.0's repertoires from it, and links it to the Free
Energy Principle — but **never tests ψ against actual IIT Φ**, explicitly calling for that work.
We hold the missing instrument: an exact **IIT‑4.0** Φ oracle and a candidate‑measure validation
framework (see the sibling `proxy_audit/`, `candidate_audit/`, `phiid_vs_phi/`).

**Research question (Tier A):** does ψ(π) = log κ − H(π) − h(π) track exact IIT‑4.0 Φ?
See [`research_question.md`](research_question.md).

## Status

This folder currently holds the **literature foundation** for the study:

| File | Contents |
|------|----------|
| [`concepts.md`](concepts.md) | the theories/concepts the Kearney paper bridges (concept map) |
| [`research_question.md`](research_question.md) | Tier A RQ, hypotheses, design sketch, caveats |
| [`literature_review.md`](literature_review.md) | the written literature review |
| `literature/references.bib` | bibliography (BibTeX) |
| `literature/notes/` | per‑paper ingestion notes |
| `literature/pdfs/` | open‑access PDFs only |
| `literature/deep_research_report.md` | output of the deep‑research scan |

The ψ measure implementation and the ψ‑vs‑Φ experiment (`psi.py`, `run.py`, `analyze.py`,
`results/`, `FINDINGS.md`) are a **later phase**, deferred so the exact definition of the MaxCal
partition constant κ gets proper care before any numbers are trusted.

## Copyright note
`literature/pdfs/` contains **only open‑access** PDFs (arXiv, PLOS, Frontiers, MDPI/Entropy,
eLife). For paywalled sources we store a note + DOI link, not the PDF.
