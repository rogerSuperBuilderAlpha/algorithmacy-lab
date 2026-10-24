#!/usr/bin/env python3
"""Collect the lab's earlier work on Nadella's posts into nadella/sources/, and the cards it cites into
literature/cards/, as byte-identical copies. Writes nadella/CARDS.md and records every copy in
literature/card_sources.json ("nadella_sources") so build_provenance.py checks it.

    python3 -I nadella/collect.py          # copy, write CARDS.md, update card_sources.json
    python3 -I nadella/collect.py --check  # exit 1 if a copy is missing or differs, or CARDS.md is stale

The full texts of the posts are NOT copied here: the repo is public and the X capture is marked for local
use only. They live in ~/iit-playground/berthon_ethics_local/nadella/ (see nadella/CORPUS.md).
"""
import glob
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARM = os.path.dirname(HERE)
SUB = os.path.dirname(ARM)
sys.path.insert(0, os.path.join(ARM, "literature"))
import cardlib as cl  # noqa: E402

DXF = "submissions/dxd_foundation"
BEC = "submissions/berthon_ethics_course"
FILES = {}
for f in ["ABSTRACT_v4", "ARGUMENT_MAP", "CLAIM", "DRAFT", "DRAFT_v2", "DRAFT_v3", "DRAFT_v4", "OUTLINE",
          "README", "RESEARCH_PLAN", "REVIEW_v2_2026-10-13", "SOURCE"]:
    FILES[f"nadella/sources/dxf_{f}.md"] = f"{DXF}/{f}.md"
for f in ["E_human_factors_frame", "G_nadella_lineage", "H_candidate_moves", "L_disclosure_and_choice",
          "S_hmi_read_to_check", "T_adjudication", "X_counter_case", "Z_gap_search"]:
    FILES[f"nadella/sources/dxf_facet_{f}.md"] = f"{DXF}/literature/facets/{f}.md"
FILES["nadella/sources/dxf_facet_G_nadella_lineage.bib"] = f"{DXF}/literature/facets/G_nadella_lineage.bib"
# The two historical transitions: scriptio continua to word spacing (dxd_foundation) and print (berthon facet B).
HISTORY = ["A_the_record", "B_the_dispute", "C_spacing_to_literacy", "D_reading_science", "F_parallel_moves",
           "J_who_holds_the_convention", "K_training_and_cause", "O_custody_of_conventions", "W_spacing_oracy_literacy"]
for f in HISTORY:
    FILES[f"nadella/sources/dxf_facet_{f}.md"] = f"{DXF}/literature/facets/{f}.md"
    FILES[f"nadella/sources/dxf_facet_{f}.bib"] = f"{DXF}/literature/facets/{f}.bib"
FILES["nadella/sources/bec_facet_B_print_1450_1800.md"] = f"{BEC}/literature/facets/B_print_1450_1800.md"
FILES["nadella/sources/bec_facet_B_print_1450_1800.bib"] = f"{BEC}/literature/facets/B_print_1450_1800.bib"
for f in ["V1_nadella_disclosure_paradigm", "V2_oracy_to_literacy", "V4_disclosure_and_burden",
          "V5_scaffolding", "V6_prior_work_and_objections"]:
    FILES[f"nadella/sources/bec_facet_{f}.md"] = f"{BEC}/literature/facets/{f}.md"
FILES["nadella/sources/bec_facet_V1_nadella_disclosure_paradigm.bib"] = f"{BEC}/literature/facets/V1_nadella_disclosure_paradigm.bib"
for f in ["RESEARCH_BRIEF", "V4_CHECK_BRIEF"]:
    FILES[f"nadella/sources/bec_v4_{f}.md"] = f"{BEC}/v4/{f}.md"

LIBS = {"dxd_foundation": f"{DXF}/literature/library", "berthon_ethics_course": f"{BEC}/literature/cards",
        "algorithmacy_design_ethics": "submissions/algorithmacy_design_ethics/literature/library"}


def library_index():
    """(sub, path) for every card in LIBS, keyed by filename, DOI and title+year."""
    by = {}
    for sub, lib in LIBS.items():
        for p in sorted(glob.glob(os.path.join(origin(lib), "*.md"))):
            if os.path.basename(p) in cl.NONCARDS:
                continue
            r = cl.parse_card(p, sub)
            for k in (("key", os.path.basename(p)[:-3]), ("doi", r["doi"]),
                      ("title", cl.norm_title(r["title"], r["year"]) if r["year"] else "")):
                if k[1]:
                    by.setdefault(k, (sub, p))
    return by
BIBS = ["nadella/sources/dxf_facet_G_nadella_lineage.bib", "nadella/sources/bec_facet_V1_nadella_disclosure_paradigm.bib"] + \
    [f"nadella/sources/dxf_facet_{f}.bib" for f in HISTORY] + ["nadella/sources/bec_facet_B_print_1450_1800.bib"]


def origin(rel):
    return os.path.join(os.path.dirname(SUB), rel)


def main(check):
    ok = True
    for dest, src in FILES.items():
        d = os.path.join(ARM, dest)
        if check:
            ok &= os.path.exists(d) and cl.sha256(d) == cl.sha256(origin(src))
        else:
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copy2(origin(src), d)
    rows, missing = [], []
    idx = library_index()
    for bib in BIBS:
        entries = cl.parse_bib(os.path.join(ARM, bib)) if os.path.exists(os.path.join(ARM, bib)) else {}
        for key in sorted(entries):
            e = entries[key]
            t = cl.norm_title(re.sub(r"[{}\\]", "", e.get("title", "")), e.get("year", ""))
            hit = idx.get(("key", key)) or idx.get(("doi", cl.norm_doi(e.get("doi", "")))) or idx.get(("title", t))
            if not hit:
                missing.append((os.path.basename(bib), key))
                continue
            sub, p = hit
            dest = os.path.join(cl.CARDS, sub, os.path.basename(p))
            if check:
                ok &= os.path.exists(dest) and cl.sha256(dest) == cl.sha256(p)
            elif not os.path.exists(dest):
                shutil.copy2(p, dest)
            r = cl.parse_card(p, sub)
            rows.append(f"| `{sub}/{os.path.basename(p)}` | {cl.md_cell(r['authors'][:50])} | {r['year']} | "
                        f"{cl.md_cell(r['title'][:80])} | {r['basis']} | {os.path.basename(bib)} |")
    lines = ["# Cards behind the earlier Nadella and transition research", "",
             "Generated by `nadella/collect.py`; do not edit by hand. Every key in the two Nadella facet bibs",
             "(`sources/*.bib`: facets G and V1 on the post; A-D, F, J, K, O, W on word spacing; B on print),",
             "with the card now in `../literature/cards/`. Paths are relative to that directory.", "",
             f"Cards: {len(rows)}. Bib keys with no card: {len(missing)}.", "",
             "| card | authors | year | title | basis | facet bib |", "|---|---|---|---|---|---|"] + sorted(set(rows)) + \
            ["", "## Keys with no card", ""] + [f"- `{k}` ({b})" for b, k in missing]
    ok &= cl.write_or_check(os.path.join(HERE, "CARDS.md"), "\n".join(lines) + "\n", check)
    if not check:
        jp = os.path.join(cl.HERE, "card_sources.json")
        meta = json.load(open(jp, encoding="utf-8"))
        meta["nadella_sources"] = FILES
        with open(jp, "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2, ensure_ascii=False)
            f.write("\n")
    print(f"{len(FILES)} files; {len(rows)} cards; {len(missing)} keys without card" + ("" if ok else " — STALE"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
