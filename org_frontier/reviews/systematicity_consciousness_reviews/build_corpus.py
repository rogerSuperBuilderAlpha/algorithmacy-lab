"""Build the corpus for the systematicity_consciousness_reviews review.

The candidate pool was harvested with two academic semantic-search connectors (Scholar Gateway and
Consensus) over eight review-oriented queries (see methods.md). Their raw returns are stored under
literature/ as raw_scholar_gateway.json (title, abstract, year, doi, article_type) and
raw_consensus.json (title, year, citationCount, journal). This script:

  1. merges and deduplicates the two pools by normalized title;
  2. applies the corpus boundary (a REVIEW/survey/overview of consciousness science, not a primary
     empirical study, a single-measure methods paper, a book review, or a bare adversarial-experiment
     report);
  3. enriches each kept source's citation count from Semantic Scholar by DOI (Consensus counts are the
     fallback where no DOI resolves);
  4. writes literature/corpus.jsonl, seeds.json, and literature/screened_out.jsonl.

    python -m org_frontier.reviews.systematicity_consciousness_reviews.build_corpus

Standard library only. The S2 enrichment is the only network step; it degrades gracefully to the
Consensus citation count when the API rate-limits.
"""

import json
import os
import re
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(__file__)
LIT = os.path.join(HERE, "literature")

# --- boundary regexes -------------------------------------------------------
REVIEW = re.compile(
    r"\breview\b|\bsurvey\b|\boverview\b|\bsynthes|\bscoping\b|\bsystematic\b|\btaxonom|"
    r"state[- ]of[- ]the[- ]art|\bwe review\b|\bwe compare\b|comparing theories|"
    r"theoretical landscape|\bmeta-analy|classification of|profiles of|commensurab|"
    r"perspectives?\b|\bframework\b", re.I)
PRIMARY = re.compile(
    r"\bwe recorded\b|\bparticipants\b|\bn ?= ?\d|\bsubjects (viewed|were|underwent)\b|"
    r"fmri data (were|was) acquired|\bwe measured\b|\bpreregist|\bhealthy (subjects|volunteers)\b|"
    r"\beeg data\b|we present (an|a) (implementation|model|measure)|we propose a (new |novel )?measure|"
    r"\bsimulation(s)? (demonstrate|show|analysis)|were acquired from|\bpropofol\b|"
    r"study protocol|will (view|follow|test)|\bwe derive\b|electrodes", re.I)
CONSCIOUSNESS = re.compile(
    r"conscious|awareness|integrated information|\bIIT\b|global (neuronal )?workspace|"
    r"neural correlate|phenomen|qualia|sentien|\bphi\b|\bNCC\b", re.I)
# off-domain semantic-search false positives (incidental "conscious" mention in another field)
OFF_DOMAIN = re.compile(
    r"chemical engineering|critical race|policy design|artificial intelligence in education|"
    r"australopithecus|\bimagination\b|mathematics in|introspection\"|50 year|"
    r"sensory expectation|hedonic|packaging|advertising", re.I)
# titles we screen out by hand: bare adversarial-experiment reports / single-measure methods papers
HARD_DROP = re.compile(
    r"adversarial testing of global neuronal workspace|adversarial collaboration protocol|"
    r"an implementation of integrated information theory in resting-state|"
    r"a practical measure of integrated information reveals|"
    r"measuring integrated information from the decoding|"
    r"practical measures of integrated information for time-series|"
    r"measuring integrated information: comparison of candidate|"
    r"protocol for testing global neuronal workspace|"
    r"the predictive global neuronal workspace: a formal|"
    r"a synergistic workspace for human consciousness|"
    r"development of a model for the study and measurement|"
    r"mechanism integrated information$|an adversarial collaboration to critically evaluate|"
    r"two books on the representation", re.I)


def norm(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())


def get(url):
    try:
        req = urllib.request.Request(url, headers={})
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except Exception as e:
        return {"_err": str(e)}


def s2_cites(doi):
    if not doi:
        return None
    d = get("https://api.semanticscholar.org/graph/v1/paper/DOI:" +
            urllib.parse.quote(doi) + "?fields=citationCount")
    return d.get("citationCount") if isinstance(d, dict) and "citationCount" in d else None


def in_boundary(rec):
    t = (rec.get("title") or "") + " " + (rec.get("abstract") or "")
    if HARD_DROP.search(rec.get("title") or "") or OFF_DOMAIN.search(t):
        return False
    if rec.get("atype") in ("bookReview", "letter", "caseStudy", "researchArticle"):
        # research/case/book-review/letter are not literature reviews
        if rec.get("atype") == "researchArticle":
            return False
        return False
    if not CONSCIOUSNESS.search(t):
        return False
    if not REVIEW.search(t):
        return False
    if PRIMARY.search(t) and rec.get("atype") != "reviewArticle":
        return False
    return True


def slugify(title, year, taken):
    base = re.sub(r"[^a-z0-9]+", "", (title or "").lower())[:26] or "src"
    slug = f"{base}{year or ''}"
    n, out = 1, slug
    while out in taken:
        n += 1
        out = f"{slug}_{n}"
    taken.add(out)
    return out


def main():
    sg = json.load(open(os.path.join(LIT, "raw_scholar_gateway.json")))
    cons = json.load(open(os.path.join(LIT, "raw_consensus.json")))
    cons_cites = {norm(c["title"]): c for c in cons}

    merged = {}
    for r in sg:
        k = norm(r["title"])
        merged[k] = {"title": r["title"], "abstract": r.get("abstract") or "",
                     "year": r.get("year"), "doi": r.get("doi"),
                     "atype": r.get("atype"), "journal": r.get("journal"),
                     "src": "scholar_gateway", "cites": None}
    for c in cons:
        k = norm(c["title"])
        if k in merged:
            merged[k]["cites"] = c.get("cites")  # trust Consensus count
            merged[k]["src"] = "both"
            if not merged[k]["abstract"] and c.get("abstract"):
                merged[k]["abstract"] = c["abstract"]
        else:
            merged[k] = {"title": c["title"], "abstract": c.get("abstract") or "",
                         "year": c.get("year"), "doi": None, "atype": "reviewArticle",
                         "journal": c.get("journal"), "src": "consensus",
                         "cites": c.get("cites")}

    kept, dropped, taken = [], [], set()
    for k, r in merged.items():
        (kept if in_boundary(r) else dropped).append(r)

    # enrich citation counts: S2 by DOI, else Consensus count already on record, else 0
    for r in kept:
        cc = cons_cites.get(norm(r["title"]))
        if r["cites"] is None and cc:
            r["cites"] = cc.get("cites")
        if r["doi"]:
            s2 = s2_cites(r["doi"])
            time.sleep(1.1)
            if s2 is not None:
                r["cites"] = s2
        if r["cites"] is None:
            r["cites"] = 0

    for r in kept:
        r["slug"] = slugify(r["title"], r["year"], taken)

    os.makedirs(LIT, exist_ok=True)
    with open(os.path.join(LIT, "corpus.jsonl"), "w") as fh:
        for r in sorted(kept, key=lambda x: (x.get("year") or 0)):
            fh.write(json.dumps({"slug": r["slug"], "title": r["title"],
                                 "abstract": r["abstract"], "year": r["year"],
                                 "doi": r["doi"], "cites": r["cites"],
                                 "journal": r.get("journal"), "source": r["src"]}) + "\n")
    with open(os.path.join(LIT, "screened_out.jsonl"), "w") as fh:
        for r in dropped:
            fh.write(json.dumps(r) + "\n")
    seeds = [{"slug": r["slug"], "doi": r["doi"]} if r["doi"]
             else {"slug": r["slug"], "title": r["title"]} for r in kept]
    json.dump(seeds, open(os.path.join(HERE, "seeds.json"), "w"), indent=1)

    print(f"merged candidates: {len(merged)}")
    print(f"kept (in-boundary reviews): {len(kept)}   screened out: {len(dropped)}")
    print(f"wrote literature/corpus.jsonl, seeds.json ({len(seeds)}), literature/screened_out.jsonl")


if __name__ == "__main__":
    main()
