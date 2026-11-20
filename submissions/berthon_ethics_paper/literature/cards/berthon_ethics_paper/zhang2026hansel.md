---
citekey: zhang2026hansel
title: "HANSEL: Extracting Breadcrumbs from Web Agent Trajectories for Interactive Verification"
authors: Zhang, Yujin; Nam, Daye
year: 2026
type: article
doi: null
venue: arXiv preprint arXiv:2606.18671v1 (June 2026)
source_basis: partial-text
pages_read: "p. 1 (abstract, introduction opening) and p. 9 (RQ1 accuracy, RQ2 effort, RQ3 usefulness); study design located but not read in full"
source_url: https://arxiv.org/pdf/2606.18671v1
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/arx_hansel2026/page.pdf
sha256: c668a64e39b8d86cb06861b29fe7339ade0285dd0e96d462a8756b5078b35541
manuscript_lines: []
ledger_rows: [H07, D04]
premises: [A4, A5]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
A system that turns a web agent's full trajectory into marked evidence: the pages and snippets the answer rests on,
with a flag where the answer traces to no visited page. In a within-subjects study (14 participants, 8 tasks) it cut
completion time and effort against a standard agent interface, and every participant preferred it. Accuracy did not
differ significantly (75.0% baseline, 82.14% HANSEL). When the agent was wrong, participants caught it 60.7% of the time
with the standard interface and 67.9% with HANSEL; HANSEL users accepted the wrong answer in 32.1% of such cases.
Baseline users re-did parts of the task themselves in 66% of tasks, against 9% with HANSEL.

## Key facts it relies on
- "Existing transparency mechanisms — full trajectory logs, source links, screenshots, and LLM-generated summaries —
  treat verification as a passive reading task, leaving users to sift through overwhelming logs or trust potentially
  unfaithful explanations" (abstract, p. 1).
- "we found no significant difference between conditions across all tasks (β = 0.71, SE = 0.67, z = 1.06, p = .29)"
  (p. 9; the PDF sets the symbols in math italics).
- "on tasks where the agent’s answer was incorrect, accuracy was 60.7% for the baseline and 67.9% for HANSEL" (p. 9).
- "Participants using the baseline frequently re-executed parts of the task themselves (e.g., reopening webpages,
  rerunning searches, and manually applying filters) in 66% of tasks, whereas participants using HANSEL did so in only
  9% of tasks" (p. 9).
- "HANSEL users accepted the wrong answer in 32.1% of cases when the agent’s answer was incorrect" (p. 9).

## Critical notes from the literature
- Preprint; 14 university participants; the agent tasks are web search and shopping questions, not consequential
  actions.

## Where the argument uses it
- M4(b) (refutation sought): narrows it. Marking the evidence points in a trajectory, the analogue of word spacing for a
  log, saves time and effort and is preferred. It does not, in this study, make people significantly better at
  catching wrong agent answers, and one wrong answer in three still passed.
- M4 (reconstruction from complete logs): with the full log, people caught wrong answers about 61% of the time, mostly
  by redoing the work. That is evidence that a complete record does not by itself let a reader check the outcome.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
