#!/usr/bin/env python3
"""
Series-wide edition reconcile for the Hegel/coordination Substack series.

Run before posting. Audits all nine posts in posts/postN_*.md for edition
consistency across the series. It does NOT check that suffix letters (1991a vs
1991b) match across posts — APA assigns those per-document, so they legitimately
differ. It checks the things that must hold:

  1. Per-post integrity: every in-text citation key resolves to a reference
     entry, and every reference entry is cited at least once (orphan detection).
  2. One edition per work, series-wide: wherever a given Hegel work (or a canon
     secondary source) appears, its reference string is identical modulo the
     suffix letter and whitespace. Divergent strings for the same work are the
     reconcile's main target.
  3. Edition pins: PR = Wood/Nisbet (CUP); PhG = Pinkard 2018 (CUP); EL main
     paragraphs = Brinkmann/Dahlstrom 2010 (CUP); EL Zusätze = Geraets/Suchting/
     Harris (Hackett); SL = di Giovanni 2010 (CUP). Banned markers (Knox, Dyde,
     Miller/Baillie for PhG, Wallace for EL, "MIT" for Honneth) are flagged.
  4. The EL split, per locus: a Zusatz locus must use the Hackett edition; a bare
     main-paragraph locus should use Brinkmann/Dahlstrom. Every EL in-text
     citation is listed with its edition and locus so a human can confirm.
  5. The Pippin split: 2008 (Practical Philosophy) vs 2011 (Self-Consciousness)
     are different books; each post's choice is reported for confirmation.

Exit code is nonzero if any hard error (dangling citation, divergent edition
string, banned marker, Zusatz/main mismatch) is found. WARN and INFO items do
not fail the run.
"""

import os
import re
import sys
from collections import defaultdict

POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")

# ---- canon -----------------------------------------------------------------
# For each work: a stable id, the required translation year, a regex that
# identifies the reference entry, and the required "signature" substrings that
# must be present. Suffix letters are stripped before comparison.

CANON = {
    "PR": dict(
        label="Philosophy of Right (Wood/Nisbet)",
        trans_year="1991",
        entry_re=re.compile(r"Elements of the philosophy of right", re.I),
        must_have=["A. W. Wood", "H. B. Nisbet", "Cambridge University Press",
                   "Original work published 1821"],
        banned=["Knox", "Dyde"],
    ),
    "PhG": dict(
        label="Phenomenology of Spirit (Pinkard 2018)",
        trans_year="2018",
        entry_re=re.compile(r"phenomenology of spirit.*Pinkard", re.I | re.S),
        must_have=["T. Pinkard", "Cambridge University Press",
                   "Original work published 1807"],
        banned=[],
    ),
    "EL_MAIN": dict(
        label="Encyclopaedia Logic, main paragraphs (Brinkmann/Dahlstrom 2010)",
        trans_year="2010",
        entry_re=re.compile(r"Encyclopedia of the philosophical sciences", re.I),
        must_have=["K. Brinkmann", "D. O. Dahlstrom", "Cambridge University Press",
                   "Original work published 1830"],
        banned=["Wallace"],
    ),
    "EL_ZUSATZE": dict(
        label="Encyclopaedia Logic, Zusätze (Geraets/Suchting/Harris, Hackett)",
        trans_year="1991",
        entry_re=re.compile(r"encyclopaedia logic", re.I),
        must_have=["T. F. Geraets", "W. A. Suchting", "H. S. Harris", "Hackett",
                   "Original work published 1830"],
        banned=["Wallace"],
    ),
    "SL": dict(
        label="Science of Logic (di Giovanni 2010)",
        trans_year="2010",
        entry_re=re.compile(r"\*The science of logic\*", re.I),
        must_have=["di Giovanni", "Cambridge University Press"],
        banned=["Miller"],
    ),
    "BRANDOM": dict(
        label="Brandom, A Spirit of Trust (2019)",
        trans_year="2019",
        entry_re=re.compile(r"Brandom.*A spirit of trust", re.I | re.S),
        must_have=["A spirit of trust", "Belknap Press of Harvard University Press"],
        banned=[],
    ),
    "PINKARD94": dict(
        label="Pinkard, Hegel's Phenomenology: The Sociality of Reason (1994)",
        trans_year="1994",
        entry_re=re.compile(r"Pinkard.*sociality of reason", re.I | re.S),
        must_have=["sociality of reason", "Cambridge University Press"],
        banned=[],
    ),
    "HONNETH": dict(
        label="Honneth, The Struggle for Recognition (1995)",
        trans_year="1995",
        entry_re=re.compile(r"Honneth.*struggle for recognition", re.I | re.S),
        must_have=["struggle for recognition", "Polity", "J. Anderson",
                   "Original work published 1992"],
        banned=["MIT Press"],
    ),
    "OIZUMI": dict(
        label="Oizumi, Albantakis, & Tononi, IIT 3.0 (2014)",
        trans_year="2014",
        entry_re=re.compile(r"Oizumi.*mechanisms of consciousness", re.I | re.S),
        must_have=["e1003588", "PLOS Computational Biology"],
        banned=[],
    ),
    "ALBANTAKIS": dict(
        label="Albantakis et al., IIT 4.0 (2023)",
        trans_year="2023",
        entry_re=re.compile(r"Albantakis.*IIT.*4\.0", re.I | re.S),
        must_have=["e1011465", "PLOS Computational Biology"],
        banned=[],
    ),
}

# Non-canonical editions of pinned works: allowed only as a deliberate,
# in-text-cited contrast. Reported so a human confirms intent.
FLAG_ALT_EDITIONS = {
    "PhG-Miller": re.compile(r"Phenomenology of spirit.*A\. V\. Miller", re.I | re.S),
    "PhG-Baillie": re.compile(r"Phenomenology.*Baillie", re.I | re.S),
    "PR-Knox": re.compile(r"philosophy of right.*T\. M\. Knox", re.I | re.S),
    "Pippin-2011-SelfConsciousness": re.compile(r"Pippin.*self-consciousness", re.I | re.S),
    "Pippin-2008-Practical": re.compile(r"Pippin.*practical philosophy", re.I | re.S),
}

# A Zusatz (student-lecture Addition) is the reconcile concern: the series pins
# ALL Zusätze to the Hackett edition even though Brinkmann/Dahlstrom carry a
# selection. Remarks (Anmerkungen) are part of Hegel's own main text and belong
# with Brinkmann/Dahlstrom — they must NOT count here.
ZUSATZ_MARKERS = re.compile(r"\b(Zusatz|Zusätze|Addition|Additions)\b|§\s*\d+\s*Z\b|\bZ\d")

# Only these surnames are edition-relevant; restrict orphan/dangling reporting to
# them so the reconcile is not buried under ordinary bibliography bookkeeping.
# (Maybee/Fuchs/Günther are single-source, single-edition — no split risk — so
# they are deliberately out of scope here.)
TRACKED = {"Hegel", "Brandom", "Pinkard", "Pippin", "Honneth",
           "Oizumi", "Albantakis", "Tononi", "Anderson"}

# ---------------------------------------------------------------------------

class Report:
    def __init__(self):
        self.errors, self.warns, self.infos = [], [], []
    def err(self, m):  self.errors.append(m)
    def warn(self, m): self.warns.append(m)
    def info(self, m): self.infos.append(m)


def load_posts():
    posts = {}
    for fn in sorted(os.listdir(POSTS_DIR)):
        if not re.match(r"post[1-9]_.*\.md$", fn) or "SCAFFOLD" in fn:
            continue
        with open(os.path.join(POSTS_DIR, fn), encoding="utf-8") as fh:
            posts[fn] = fh.read()
    return posts


def references_block(text):
    """Return the References section as a list of unwrapped entries.

    Entries wrap across physical lines; a new entry starts at a line beginning
    with a capitalized surname. The block ends at the next heading."""
    m = re.search(r"^##+\s+References\s*$", text, re.M)
    if not m:
        return None
    tail = text[m.end():]
    end = re.search(r"^##+\s+\S", tail, re.M)
    block = tail[:end.start()] if end else tail
    # Entries are separated by blank lines; every non-blank line (including a
    # wrapped multi-author list) continues the current entry. Do NOT split on a
    # line that merely begins with "Surname, Initial." — long author lists wrap
    # onto such lines mid-entry.
    entries, cur = [], ""
    for line in block.splitlines():
        s = line.strip()
        if not s:
            if cur:
                entries.append(cur.strip()); cur = ""
            continue
        cur = (cur + " " + s).strip()
    if cur:
        entries.append(cur.strip())
    return entries


def strip_suffix(entry):
    """Normalize a reference entry for cross-post comparison: drop the a/b
    suffix on the translation year and collapse whitespace."""
    e = re.sub(r"\((\d{4})[a-z]\)", r"(\1)", entry)
    return re.sub(r"\s+", " ", e).strip()


def ref_key(entry):
    """(surname, year+suffix) key for a reference entry."""
    m = re.match(r"^([\wÀ-ÿ'’-]+),.*?\((\d{4}[a-z]?)\)", entry)
    return (m.group(1), m.group(2)) if m else None


def body_only(text):
    """The prose before the References section — so reference entries are not
    mistaken for in-text citations."""
    m = re.search(r"^##+\s+References\s*$", text, re.M)
    return text[:m.start()] if m else text


def intext_keys(text):
    """All in-text citation keys actually used, as (surname, trans-year+suffix).

    Hegel cites use original/translation double dates: (Hegel, 1821/1991a, ...).
    Others use a single year, either grouped — (Oizumi et al., 2014; Albantakis
    et al., 2023) — or narrative: Author (2019). Scanned on the body only."""
    text = body_only(text)
    def norm(surname):
        return re.sub(r"['’]s$", "", surname)  # drop possessive "Burt's" -> "Burt"

    keys = set()
    # Hegel double-date, both parenthetical and narrative
    for m in re.finditer(r"Hegel[,\s(]+\d{4}/(\d{4}[a-z]?)", text):
        keys.add(("Hegel", m.group(1)))
    # "Surname[, / 's] [et al.,] year" — no closing paren required, so grouped
    # and mid-sentence citations both match.
    for m in re.finditer(r"([A-ZÀ-Þ][\wÀ-ÿ'’-]+?)(?:'s|’s)?(?:\s+et al\.)?,\s(\d{4}[a-z]?)\b", text):
        s = norm(m.group(1))
        if s != "Hegel":
            keys.add((s, m.group(2)))
    # narrative: Surname (2019) / Surname's (2019) / Surname et al. (2019)
    for m in re.finditer(r"\b([A-ZÀ-Þ][\wÀ-ÿ'’-]+?)(?:'s|’s)?(?:\s+et al\.)?\s+\((\d{4}[a-z]?)\)", text):
        s = norm(m.group(1))
        if s != "Hegel":
            keys.add((s, m.group(2)))
    return {k for k in keys if k[0] in TRACKED}


def el_intext(text):
    """Every EL in-text citation: (edition-suffix, locus, is_zusatz)."""
    out = []
    for m in re.finditer(r"Hegel[,\s(]+1830/(\d{4}[a-z]?)(?:,\s*([^)]*))?\)", text):
        suffix = m.group(1)
        locus = re.sub(r"\s+", " ", (m.group(2) or "").strip())  # unwrap line breaks
        out.append((suffix, locus, bool(ZUSATZ_MARKERS.search(locus))))
    return out


def main():
    posts = load_posts()
    rep = Report()

    # Per-work collection for the cross-post edition-consistency check.
    work_strings = defaultdict(dict)   # work_id -> {post: normalized_entry}
    pippin_choice = {}                 # post -> set of pippin flags

    for post, text in sorted(posts.items()):
        entries = references_block(text)
        if entries is None:
            rep.err(f"[{post}] NO References section — cannot reconcile citations.")
            continue

        # ---- per-post orphan / dangling detection --------------------------
        ref_keys = {}
        for e in entries:
            k = ref_key(e)
            if k:
                ref_keys[k] = e
        used = intext_keys(text)
        # dangling: cited in text but not in the reference list
        for k in sorted(used):
            if k not in ref_keys:
                # tolerate secondary-author initials vs surname-only mismatch by surname+year
                if not any(rk[0] == k[0] and rk[1] == k[1] for rk in ref_keys):
                    rep.err(f"[{post}] in-text ({k[0]}, {k[1]}) has NO reference entry (dangling).")
        # orphan: listed but never cited (tracked, edition-relevant authors only)
        for k, e in sorted(ref_keys.items()):
            if k[0] not in TRACKED:
                continue
            if k not in used and not any(k[0] == u[0] and k[1] == u[1] for u in used):
                rep.warn(f"[{post}] reference '{k[0]} ({k[1]})' is never cited in text (orphan): "
                         f"{e[:70]}…")

        # ---- canon identification + edition-string collection --------------
        for wid, spec in CANON.items():
            for e in entries:
                if spec["entry_re"].search(e):
                    # verify required signature substrings
                    missing = [s for s in spec["must_have"] if s not in e]
                    if missing:
                        rep.err(f"[{post}] {spec['label']}: entry missing {missing}. "
                                f"Entry: {e[:90]}…")
                    for b in spec["banned"]:
                        if b in e:
                            rep.err(f"[{post}] {spec['label']}: BANNED marker '{b}' present.")
                    work_strings[wid][post] = strip_suffix(e)
                    break

        # ---- alternate / non-canonical editions ----------------------------
        for name, rx in FLAG_ALT_EDITIONS.items():
            for e in entries:
                if rx.search(e):
                    if name.startswith("Pippin"):
                        pippin_choice.setdefault(post, set()).add(name)
                    else:
                        rep.warn(f"[{post}] alternate edition present: {name}. "
                                 f"Confirm it is a deliberate contrast, not drift. "
                                 f"Entry: {e[:70]}…")

        # ---- EL split, per locus ------------------------------------------
        for suffix, locus, is_z in el_intext(text):
            entry = ref_keys.get(("Hegel", suffix), "")
            is_hackett = "Hackett" in entry or "encyclopaedia logic" in entry.lower()
            is_bd = "Brinkmann" in entry
            edn = "Hackett/Zusätze" if is_hackett else ("B&D/main" if is_bd else f"?({suffix})")
            shown = locus if locus else "(no locus)"
            rep.info(f"[{post}] EL {shown} → {edn}"
                     f"{'  [Zusatz]' if is_z else ''}")
            if is_z and is_bd:
                rep.warn(f"[{post}] EL locus '{locus}' is a Zusatz cited from "
                         f"Brinkmann/Dahlstrom. B&D carries a selection of Zusätze, so this "
                         f"may be accurate — but the series pins ALL Zusätze to Hackett for "
                         f"consistency. Re-cite from Hackett, or confirm the exception.")
            if not is_z and is_hackett and locus:
                rep.warn(f"[{post}] EL locus '{locus}' looks like a bare main paragraph "
                         f"but cites the Hackett Zusätze edition. Confirm it is a Zusatz; "
                         f"otherwise the series pins main paragraphs to Brinkmann/Dahlstrom.")

    # ---- cross-post: one edition string per work ---------------------------
    for wid, spec in CANON.items():
        variants = defaultdict(list)
        for post, s in work_strings[wid].items():
            variants[s].append(post)
        if len(variants) > 1:
            # name the likely axis of difference
            has_doi = {bool(re.search(r"https?://doi\.org|doi:", s)): ps
                       for s, ps in variants.items()}
            axis = "DOI present in some, absent in others" if len(has_doi) > 1 else "wording differs"
            rep.err(f"{spec['label']}: {len(variants)} DIFFERENT reference strings "
                    f"across posts ({axis}; pick one form):")
            for s, ps in variants.items():
                rep.errors.append(f"      · {', '.join(sorted(p.split('_')[0] for p in ps))}: {s}")

    # ---- Pippin split ------------------------------------------------------
    if pippin_choice:
        works = defaultdict(list)
        for post, flags in pippin_choice.items():
            for fl in flags:
                works[fl].append(post)
        if len(works) > 1:
            rep.warn("Pippin: the series cites TWO different Pippin books. Confirm each "
                     "post's choice is intentional (2011 is the PhG/self-consciousness book, "
                     "2008 is the practical-philosophy book):")
            for fl, ps in works.items():
                rep.warns.append(f"      · {fl}: {', '.join(sorted(ps))}")

    # ---- edition matrix (info) --------------------------------------------
    rep.info("── edition matrix (work × posts citing it) ──")
    for wid, spec in CANON.items():
        ps = sorted(work_strings[wid].keys())
        if ps:
            rep.info(f"  {wid:12s} {spec['trans_year']}: {', '.join(p.split('_')[0] for p in ps)}")

    # ---- output ------------------------------------------------------------
    def dump(title, items):
        print(f"\n{title} ({len(items)})")
        for m in items:
            print(f"  {m}")

    print("=" * 78)
    print("SERIES-WIDE EDITION RECONCILE —", len(posts), "posts")
    print("=" * 78)
    dump("ERRORS (must fix before posting)", rep.errors)
    dump("WARNINGS (confirm intentional)", rep.warns)
    dump("INFO", rep.infos)
    print("\n" + "-" * 78)
    print(f"RESULT: {len(rep.errors)} errors, {len(rep.warns)} warnings")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
