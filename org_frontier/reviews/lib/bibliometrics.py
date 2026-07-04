"""Citation-network analysis for a systematic literature review.

Operates on a harvested citation graph (see harvest.py): one edge file per seed source, each holding
the seed's outbound references and inbound citers. Given a cluster map (source id -> cluster label),
it answers the structural questions a review asks about a body of literature:

  * cluster_matrix   — how often does one cluster cite another? A block-diagonal matrix is the
    signature of sub-literatures that developed in isolation.
  * spanning         — how many external papers cite sources from >= k clusters? Tests whether any
    prior work already assembled the sub-literatures (a low ceiling means the assembly is open).
  * mutual_density   — among a named set of sources, what fraction of possible pairs are linked? A
    proxy for whether a set of rival readings engages each other at all.

Each edge file is JSON: {"handle": "<paperId or DOI:...>", "doi": "...", "title": "...",
"refs": [{"id","doi","t"}...], "citers": [{"id","doi","t"}...]}. A candidate is matched to a seed by
paperId, then DOI, then a normalized-title fallback. References are elided by some publishers, so the
outbound signal is partial; inbound citers are the more complete channel. Report both.

Run (example):

    python -m org_frontier.reviews.lib.bibliometrics edges/ --clusters clusters.json --seeds seeds.json

Standard library only.
"""

import argparse
import glob
import json
import os
import re
from collections import Counter, defaultdict
from itertools import combinations


def _norm(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())[:40]


def load_edges(path):
    """Return {seed_slug: edge_record} from a directory of per-seed JSON files."""
    edges = {}
    for f in glob.glob(os.path.join(path, "*.json")):
        slug = os.path.splitext(os.path.basename(f))[0]
        try:
            edges[slug] = json.load(open(f))
        except (OSError, json.JSONDecodeError):
            continue
    return edges


def _seed_lookup(edges, seeds):
    """Build id/doi/title -> seed_slug maps so an edge target can be matched to one of our seeds.
    `seeds` is optional {slug: {"doi":..., "title":...}} to enrich matching."""
    by_id, by_doi, by_title = {}, {}, {}
    for slug, e in edges.items():
        h = (e.get("handle") or "").replace("DOI:", "").lower()
        if h:
            by_id[h] = slug
        meta = (seeds or {}).get(slug, {})
        doi = (e.get("doi") or meta.get("doi") or "").lower()
        if doi:
            by_doi[doi] = slug
        title = e.get("title") or meta.get("title") or ""
        if title:
            by_title[_norm(title)] = slug
    return by_id, by_doi, by_title


def _match(rec, by_id, by_doi, by_title):
    return (by_id.get((rec.get("id") or "").lower())
            or by_doi.get((rec.get("doi") or "").lower())
            or by_title.get(_norm(rec.get("t") or rec.get("title"))))


def cluster_matrix(edges, cluster_of, seeds=None):
    """Undirected cluster-to-cluster link counts among seed sources (deduped seed pairs)."""
    by_id, by_doi, by_title = _seed_lookup(edges, seeds)
    links = Counter()
    seen_pairs = set()
    for slug, e in edges.items():
        ca = cluster_of.get(slug)
        if not ca or "error" in e:
            continue
        for rec in (e.get("refs") or []) + (e.get("citers") or []):
            tgt = _match(rec, by_id, by_doi, by_title)
            if not tgt or tgt == slug:
                continue
            cb = cluster_of.get(tgt)
            if not cb:
                continue
            key = (min(slug, tgt), max(slug, tgt))
            if key in seen_pairs:
                continue
            seen_pairs.add(key)
            links[tuple(sorted((ca, cb)))] += 1
    return links


def spanning(edges, cluster_of, seeds=None):
    """{k: number of external citers that cite seeds from exactly k clusters}."""
    by_id, by_doi, by_title = _seed_lookup(edges, seeds)
    citer_clusters = defaultdict(set)
    for slug, e in edges.items():
        c = cluster_of.get(slug)
        if not c or "error" in e:
            continue
        for rec in e.get("citers") or []:
            cid = rec.get("id")
            if cid:
                citer_clusters[cid].add(c)
    return Counter(len(v) for v in citer_clusters.values())


def mutual_density(edges, members, seeds=None):
    """Fraction of possible undirected pairs, among `members` with edge data, that are linked."""
    sub = {m: edges[m] for m in members if m in edges and "error" not in edges.get(m, {})}
    by_id, by_doi, by_title = _seed_lookup(sub, seeds)
    linked = set()
    for slug, e in sub.items():
        for rec in (e.get("refs") or []) + (e.get("citers") or []):
            tgt = _match(rec, by_id, by_doi, by_title)
            if tgt and tgt != slug and tgt in sub:
                linked.add((min(slug, tgt), max(slug, tgt)))
    n = len(sub)
    possible = n * (n - 1) // 2
    return (len(linked) / possible if possible else 0.0), len(linked), possible, sorted(linked)


def print_matrix(links, clusters):
    print("cluster-to-cluster citation links (undirected, deduped seed pairs)")
    print(f"  {'':14}" + "".join(f"{c[:10]:>12}" for c in clusters))
    for a in clusters:
        row = f"  {a:14}"
        for b in clusters:
            row += f"{links.get(tuple(sorted((a, b))), 0):>12}"
        print(row)
    within = sum(v for k, v in links.items() if k[0] == k[1])
    cross = sum(v for k, v in links.items() if k[0] != k[1])
    print(f"  within-cluster: {within}   cross-cluster: {cross}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("edges", help="directory of per-seed edge JSON files")
    ap.add_argument("--clusters", required=True, help="JSON {slug: cluster_label}")
    ap.add_argument("--seeds", default=None, help="optional JSON {slug: {doi,title}} to enrich matching")
    ap.add_argument("--members", default=None, help="comma-separated slugs for a mutual-density test")
    a = ap.parse_args()
    edges = load_edges(a.edges)
    cluster_of = json.load(open(a.clusters))
    seeds = json.load(open(a.seeds)) if a.seeds else None
    clusters = sorted(set(cluster_of.values()))
    print(f"edges: {len(edges)} seeds | clusters: {clusters}\n")
    print_matrix(cluster_matrix(edges, cluster_of, seeds), clusters)
    print("\nassembly-spanning citers (how many clusters each external citer spans)")
    for k, n in sorted(spanning(edges, cluster_of, seeds).items(), reverse=True):
        print(f"  spans {k}: {n} external papers")
    if a.members:
        d, obs, poss, pairs = mutual_density(edges, a.members.split(","), seeds)
        print(f"\nmutual-citation density among {a.members.count(',')+1} members: "
              f"{d:.2f} ({obs}/{poss} pairs)")


if __name__ == "__main__":
    main()
