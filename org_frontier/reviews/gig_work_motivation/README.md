# gig_work_motivation

**Question.** How do gig/platform-work review articles motivate themselves — by gap-spotting (a
literature gap / under-studied area) or by problematization (challenging an in-field assumption, in
the sense of Sandberg & Alvesson 2011) — and does one style draw more citations?

**Corpus.** 49 review, agenda-setting, and bibliometric-review articles on gig work, platform work,
on-demand labor, crowdwork, and the algorithmic management of platform workers (2017-2026), discovered
via the Consensus and Scholar Gateway semantic-search connectors and screened against a
review-vs-primary boundary. See `methods.md` and `literature/corpus.jsonl`.

**Result.** Gap-spotting motivates 90% of the corpus (44/49); problematization 8% (4); one is neither.
Problematization does not rise over time — it falls (13% -> 6%) as bibliometric/PRISMA reviews come to
dominate. The four problematizers are cited more per year (median 28.6 vs 3.7; Mann-Whitney p = 0.022),
on a fragile base. Fleiss' κ = 0.72 (motivation_mode), 0.92 (assumption_targeted).

- Pre-registration: `hypotheses.md` (committed before coding)
- Codebook: `coding_protocol.md` · Coders: `coding/coder{A,B,C}.jsonl`
- Analysis: `run.py` · Adjudicated data + summary: `results/`
- Write-up: `FINDINGS.md` (verdicts) and `paper.md` (ORM register)

**Reproduce.**
```bash
cd /Users/ludwitt/iit-playground/pyphi-experiments
python3 -m org_frontier.reviews.lib.reliability \
    org_frontier/reviews/gig_work_motivation/coding \
    --categorical motivation_mode,assumption_targeted \
    --out org_frontier/reviews/gig_work_motivation/results/frozen.json
python3 -m org_frontier.reviews.gig_work_motivation.run
```
