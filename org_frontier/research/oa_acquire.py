#!/usr/bin/env python3
"""Open-access PDF acquisition chain for the research-watch reference cards. Stdlib only.

Resolves a free, legal full-text PDF for a bibliography entry, in order: arXiv, Unpaywall,
Europe PMC, DOI content-negotiation, and a landing-page citation_pdf_url scrape. Open-access
sources only — paywalls, cookie/captcha walls, Sci-Hub, ResearchGate caches, and the like are
never used. A candidate is accepted only after a %PDF magic-byte check.

This is the engine behind the per-paper cards under `*/literature/cards/`. See `card_backfill.py`
for the on-demand pass that retries acquisition over uncarded references and surfaces any that
have become open-access.

    acquire(entry) -> {"status": "ACQUIRED"|"NOT_FREE", "oa_source", "source_url", "sha256", "_data"}
    where entry is a dict with any of: doi, eprint (arXiv id), url.
"""
import hashlib
import json
import re
import urllib.parse
import urllib.request

EMAIL = "rhunt@bentley.edu"
UA = "algorithmacy-lab-refcards/1.0 (mailto:%s)" % EMAIL


def _get(url, accept=None, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    if accept:
        req.add_header("Accept", accept)
    return urllib.request.urlopen(req, timeout=timeout)


def _try_pdf(url, timeout=40):
    try:
        data = _get(url, accept="application/pdf", timeout=timeout).read()
        if data[:5] == b"%PDF-" and len(data) > 15000:
            return data
    except Exception:
        return None
    return None


def _pdf_from_landing(url, timeout=30):
    """Fetch an HTML landing page and try its citation_pdf_url meta tag and any .pdf links."""
    try:
        html = _get(url, timeout=timeout).read(600000).decode("utf-8", "ignore")
    except Exception:
        return None
    cands = []
    for pat in (r'<meta[^>]+name=["\']citation_pdf_url["\'][^>]+content=["\']([^"\']+)',
                r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']citation_pdf_url["\']'):
        m = re.search(pat, html, re.I)
        if m:
            cands.append(m.group(1))
    for mm in re.finditer(r'href=["\']([^"\']+\.pdf(?:\?[^"\']*)?)["\']', html, re.I):
        cands.append(urllib.parse.urljoin(url, mm.group(1)))
    seen = set()
    for u in cands:
        u = urllib.parse.urljoin(url, u)
        if u in seen:
            continue
        seen.add(u)
        data = _try_pdf(u)
        if data:
            return data, u
    return None


def _ok(data, source, url):
    return {"status": "ACQUIRED", "oa_source": source, "source_url": url,
            "sha256": hashlib.sha256(data).hexdigest(), "_data": data, "_size": len(data)}


def acquire(entry):
    doi = (entry.get("doi") or "").strip()
    eprint = (entry.get("eprint") or "").strip()
    am = re.match(r"10\.48550/arXiv\.(.+)", doi)
    arxiv_id = eprint or (am.group(1) if am else None)
    if arxiv_id:
        data = _try_pdf("https://arxiv.org/pdf/%s" % arxiv_id)
        if data:
            return _ok(data, "arxiv", "https://arxiv.org/pdf/%s" % arxiv_id)
    if doi:
        try:
            j = json.load(_get("https://api.unpaywall.org/v2/%s?email=%s" % (urllib.parse.quote(doi), EMAIL)))
            locs = ([j["best_oa_location"]] if j.get("best_oa_location") else []) + (j.get("oa_locations") or [])
            for loc in locs:
                u = loc.get("url_for_pdf")
                if u:
                    data = _try_pdf(u)
                    if data:
                        return _ok(data, "unpaywall:" + (loc.get("host_type") or "?"), u)
                land = loc.get("url") or loc.get("url_for_landing_page")
                if land:
                    got = _pdf_from_landing(land)
                    if got:
                        return _ok(got[0], "landing:" + (loc.get("host_type") or "?"), got[1])
        except Exception:
            pass
    if doi:
        try:
            q = urllib.parse.quote('DOI:"%s"' % doi)
            j = json.load(_get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%s&format=json" % q))
            for r0 in (j.get("resultList", {}).get("result") or []):
                pmcid = r0.get("pmcid")
                if pmcid:
                    u = "https://www.ebi.ac.uk/europepmc/webservices/rest/%s/%s/fullTextPDF" % (r0.get("source", "PMC"), pmcid)
                    data = _try_pdf(u)
                    if data:
                        return _ok(data, "europepmc", u)
        except Exception:
            pass
    if doi.startswith("10.1371/"):
        u = "https://journals.plos.org/plosone/article/file?id=%s&type=printable" % doi
        data = _try_pdf(u)
        if data:
            return _ok(data, "plos-template", u)
    if doi:
        got = _pdf_from_landing("https://doi.org/%s" % doi)
        if got:
            return _ok(got[0], "doi-landing", got[1])
    return {"status": "NOT_FREE", "oa_source": None, "source_url": None, "sha256": None, "_data": None}
