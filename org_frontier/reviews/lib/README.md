# `reviews/lib/` — reusable tooling

Content-agnostic scripts for a systematic archival review. Standard library only; each runs as a
module from the repository root and prints a report. All three were validated on the lab's own first
review.

## `harvest.py` — build the citation graph

```bash
python -m org_frontier.reviews.lib.harvest <slug>/seeds.json --out <slug>/edges/
```

`seeds.json` is a list of `{"slug": "...", "doi": "..."}` or `{"slug": "...", "title": "..."}`. For
each seed it resolves a Semantic Scholar paperId, pulls backward references and forward citers, and
writes one edge file per seed. Checkpointed: a seed whose edge file exists is skipped, so a run killed
by a rate limit is simply restarted. Set `S2_API_KEY` in the environment to raise the rate limit.
Publishers elide references for many papers, so the `refs` list is often empty while `citers` is
populated — downstream code uses whichever is present.

## `reliability.py` — intercoder reliability

```bash
python -m org_frontier.reviews.lib.reliability <slug>/coding \
    --id slug --categorical substrate,claim_type --set cells --out <slug>/results/frozen.json
```

Reads N coder files (JSONL or JSON list) from a directory. Reports Fleiss' κ and mean pairwise
agreement for each categorical variable, mean pairwise Jaccard for each set-valued variable, and
writes a majority-vote adjudicated dataset. κ > 0.80 is "almost perfect" (Landis & Koch).

## `bibliometrics.py` — citation-network structure

```bash
python -m org_frontier.reviews.lib.bibliometrics <slug>/edges \
    --clusters <slug>/clusters.json --seeds <slug>/seeds.json --members a,b,c
```

From the harvested edges and a `{slug: cluster_label}` map, computes the cluster-to-cluster citation
matrix (a block-diagonal shape means sub-literatures developed in isolation), the assembly-spanning
count (how many clusters any external citer reaches), and, for a named `--members` set, the
mutual-citation density.

## The coder pattern (not a script)

The three-independent-coder step is run with agents, not code. Spawn one agent per coder in parallel,
each given the same `coding_protocol.md` and the corpus (the per-source notes or abstracts), each
writing to its own `coding/coder<X>.jsonl`, and each told it is one independent coder that must not
consult the others. Then run `reliability.py` over the `coding/` directory. Blindness plus a fixed
codebook is what makes the κ meaningful; do not let one agent see another's output, and do not code the
prediction — code the source.
