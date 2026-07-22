# Methods — corpus boundary, search, coder design, statistics

## Corpus boundary (the gates)

**Substantive.** A source is in-boundary if it concerns the algorithmic management of workers: the use of
algorithms to direct, allocate, evaluate, monitor, discipline, or otherwise coordinate and control human
labor, in platform/gig settings or conventional employment. Operationalized as one algorithm signal (an
algorithm word stem, covering algorithmic management/control/surveillance/governance and the Taylorism and
panopticon metaphors) AND one work signal (worker, gig, platform work, labor, employee, crowdwork,
ride-hail/delivery, workforce, workplace, employment, HRM, job design/quality, and cognates). The
conjunction excludes generic algorithm-in-finance, law-and-society, and firm-productivity hits with no
worker referent.

**Procedural.** English-language, 2019–2026 (the window the connectors returned), journal articles and
peer-reviewed conference/working papers indexed by the two search connectors. Gray literature is included
where the connectors surfaced it (e.g. working papers), excluded otherwise. Book reviews were screened out.

11 candidates were screened out on the boundary rule; the set is logged in `literature/screened_out.jsonl`.

## Search

Two academic semantic-search connectors, chosen over raw keyword search for cleaner recall.

- **Scholar Gateway** (full-text scholarly index): six queries — algorithmic management of workers on
  digital labor platforms; algorithmic control of gig workers in the platform economy; algorithmic
  management as a new form of control over workers; platform work algorithmic management systematic review;
  algorithmic management effects on productivity and firm performance; worker experience wellbeing and
  resistance under algorithmic management. Records matched to these six executed-query strings, so payloads
  from other concurrent reviews sharing the results directory are ignored.
- **Consensus** (peer-reviewed index over ~200M papers): three queries recovering canonical and empirical
  anchors — algorithmic management gig work control worker outcomes; algorithmic management platform work
  review research agenda; algorithmic surveillance monitoring control of workers. Transcribed into
  `literature/consensus_seed.jsonl` (title, abstract, year, DOI where known).

The two channels were merged and deduplicated by DOI and by normalized title. Yield: 146 raw records →
77 after dedupe → 66 in-boundary (41 Scholar Gateway, 25 Consensus). `build_corpus.py` is deterministic
given the saved payloads.

## Coder design

Three independent coders (LLM agents), each given the same fixed codebook (`coding_protocol.md`) and the
corpus, each writing to its own `coding/coder{A,B,C}.jsonl`, each blind to the others and to the
hypotheses' predicted direction. Coders read title + abstract only. Three categorical variables:
`claim_type` (stylized_fact / assumption / critique / omission / na), `evidence` (conceptual / qualitative
/ quantitative / mixed / na), `outcome` (control / worker_experience / performance / other / na).

## Statistics

`lib/reliability.py` computes Fleiss' κ and mean pairwise percent agreement per categorical variable, and
writes a majority-vote adjudicated dataset (`results/frozen.json`). `run.py` runs the three hypothesis
tests on the adjudicated data: the outcome distribution (H1), the evidence distribution and quantitative
share (H2), and the claim_type × evidence and outcome × evidence cross-tabulations that locate the
control claim's evidentiary footing (H3). Numbers are registered in `results/summary.json`.

## Threats to validity

Agent coders, not trained humans (high κ is not a substitute for human coding); title-and-abstract coding
(full-text method or secondary outcomes can be missed); SLRs coded as conceptual (raises the conceptual
share); connector coverage and English-language indexing bound the corpus and oversample HRM/OB venues.
The performance share is an estimate for this corpus, not a census.
