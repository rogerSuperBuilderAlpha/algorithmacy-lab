"""Generate catalog.json — a machine-readable index of what the lab has already asked — and search it.

The README directory is for people. This catalog is for the assistant that has to answer "has this
question been asked here?" before a newcomer scaffolds a new one (START_HERE.md, Phase 3.5; the
protocol's Stage 1). One row per question, probe, study, foundations experiment, and open thread,
with the one-line finding, the reproduce commands registered in ci/reproduce.json, and a runtime
class, so the nearest prior work can be found without crawling the tree.

    python tools/build_catalog.py                     # rewrite catalog.json in place
    python tools/build_catalog.py --check             # exit non-zero if catalog.json is stale (CI gate)
    python tools/build_catalog.py --find "k-of-n quorum majority"   # nearest rows to a question

Deterministic and standard-library only: every list is sorted, so the output depends only on the
content. Run after adding a question, probe, or study, or editing OPEN_QUESTIONS.md.
"""

import argparse
import glob
import json
import os
import re
import signal
import sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_OUT = os.path.join(_ROOT, "catalog.json")
_MANIFEST = os.path.join(_ROOT, "ci", "reproduce.json")
_PROBES_MD = os.path.join(_ROOT, "org_frontier", "probes", "PROBES.md")
_OPEN = os.path.join(_ROOT, "OPEN_QUESTIONS.md")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_index import _first_heading, _first_paragraph, _finding_for, _clip, _strip_q_prefix  # noqa: E402


# ---------------------------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------------------------

def _rel(path: str) -> str:
    return os.path.relpath(path, _ROOT).replace(os.sep, "/")


def _checks_by_dir() -> dict:
    """Map a study directory to the reproduce checks whose command runs from it."""
    try:
        with open(_MANIFEST, encoding="utf-8") as fh:
            checks = json.load(fh)["checks"]
    except (OSError, ValueError, KeyError):
        return {}
    out = {}
    for c in checks:
        toks = c["cmd"].split()
        d = None
        if "-m" in toks:
            d = "/".join(toks[toks.index("-m") + 1].split(".")[:-1])
        else:
            for t in toks[1:]:
                if t.endswith(".py") and "/" in t:
                    d = "/".join(t.split("/")[:-1])
                    break
        if d:
            out.setdefault(d, []).append(c)
    return out


def _runtime(checks: list) -> str:
    """fast: every registered check is per-PR; slow: at least one is nightly-only; unregistered."""
    if not checks:
        return "unregistered"
    return "slow" if any(c.get("slow") for c in checks) else "fast"


def _strip_md(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\*\*([^*]*)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]*)\*", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


# ---------------------------------------------------------------------------------------------
# Row builders
# ---------------------------------------------------------------------------------------------

def _questions(by_dir: dict) -> list:
    rows = []
    for d in glob.glob(os.path.join(_ROOT, "org_frontier", "questions", "q*_*")):
        m = re.match(r"q(\d+)_(.+)", os.path.basename(d))
        if not m or not os.path.isdir(d):
            continue
        num, slug = int(m.group(1)), m.group(2)
        paper = os.path.join(d, "paper.md")
        findings = os.path.join(d, "FINDINGS.md")
        hyps = os.path.join(d, "hypotheses.md")
        title = _strip_q_prefix(_first_heading(paper)) or slug.replace("_", " ")
        question = ""
        review = os.path.join(d, "review.md")
        if os.path.exists(review):
            with open(review, encoding="utf-8") as fh:
                mq = re.search(r"\*\*Question\.\*\*\s*(.+?)(?:\n\n|\Z)", fh.read(), re.S)
                if mq:
                    question = _clip(_strip_md(mq.group(1)), 400)
        checks = by_dir.get(_rel(d), [])
        rows.append({
            "kind": "question",
            "id": f"Q{num}",
            "slug": slug,
            "title": title,
            "question": question,
            "finding": _finding_for(findings),
            "path": _rel(d),
            "artifacts": {
                "review": os.path.exists(review),
                "hypotheses": os.path.exists(hyps),
                "literature": os.path.isdir(os.path.join(d, "literature")),
                "paper": os.path.exists(paper),
                "findings": os.path.exists(findings),
            },
            "reproduce": sorted(c["cmd"] for c in checks),
            "runtime": _runtime(checks),
        })
    rows.sort(key=lambda r: int(r["id"][1:]))
    return rows


def _cmd_module(cmd: str) -> str:
    """The module token after `-m` in a check command, or "" if there is none."""
    m = re.search(r"(?:^|\s)-m\s+(\S+)", cmd)
    return m.group(1) if m else ""


def _probes(by_dir: dict) -> list:
    """Every `| n | concept | hypothesis | verdict | result |` row of PROBES.md, by number."""
    rows = {}
    try:
        with open(_PROBES_MD, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
    except OSError:
        return []
    probe_checks = by_dir.get("org_frontier/probes", [])
    for line in lines:
        m = re.match(r"^\|\s*(\d+)\s*\|(.*)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        if len(cells) < 4:
            continue
        num = int(m.group(1))
        script = re.search(r"`(probe_[a-z0-9_]+)\.py`", cells[-1])
        module = f"org_frontier.probes.{script.group(1)}" if script else ""
        checks = [c for c in probe_checks if module and _cmd_module(c["cmd"]) == module]
        rows[num] = {
            "kind": "probe",
            "id": f"#{num}",
            "concept": _strip_md(cells[0]),
            "hypothesis": _strip_md(cells[1]),
            "verdict": _strip_md(cells[2]),
            "result": _clip(_strip_md(cells[3]), 400),
            "path": f"org_frontier/probes/{script.group(1)}.py" if script else "org_frontier/probes/PROBES.md",
            "reproduce": sorted(c["cmd"] for c in checks) or ([f"python -m {module}"] if module else []),
            "runtime": _runtime(checks),
        }
    return [rows[k] for k in sorted(rows)]


def _dir_rows(kind: str, pattern: str, by_dir: dict) -> list:
    rows = []
    for d in sorted(glob.glob(os.path.join(_ROOT, pattern))):
        base = os.path.basename(d)
        if not os.path.isdir(d) or base.startswith("__") or base == "template":
            continue
        findings = os.path.join(d, "FINDINGS.md")
        if not os.path.exists(findings):
            continue
        readme = os.path.join(d, "README.md")
        checks = by_dir.get(_rel(d), [])
        rows.append({
            "kind": kind,
            "id": base,
            "title": _first_heading(readme) or base.replace("_", " "),
            "finding": _clip(_first_paragraph(findings) or _finding_for(findings), 400),
            "path": _rel(d),
            "reproduce": sorted(c["cmd"] for c in checks),
            "runtime": _runtime(checks),
        })
    return rows


def _open_threads() -> list:
    """The rows of the table in OPEN_QUESTIONS.md: id, question, status, kind, where, first command."""
    rows = []
    try:
        with open(_OPEN, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return rows
    for line in text.splitlines():
        m = re.match(r"^\|\s*(O\d+)\s*\|(.*)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        if len(cells) < 5:
            continue
        rows.append({
            "kind": "open",
            "id": m.group(1),
            "question": _strip_md(cells[0]),
            "status": _strip_md(cells[1]).lower(),
            "needs": _strip_md(cells[2]),
            "where": _strip_md(cells[3]),
            "first_command": _strip_md(cells[4]),
            "path": "OPEN_QUESTIONS.md",
        })
    return rows


def build() -> dict:
    by_dir = _checks_by_dir()
    rows = []
    rows += _questions(by_dir)
    rows += _probes(by_dir)
    rows += _dir_rows("study", "org_frontier/studies/*", by_dir)
    rows += _dir_rows("foundations", "foundations/*", by_dir)
    rows += _open_threads()
    counts = {}
    for r in rows:
        counts[r["kind"]] = counts.get(r["kind"], 0) + 1
    return {
        "_help": "Generated by tools/build_catalog.py; do not edit by hand. One row per question, probe, "
                 "study, foundations experiment, and open thread. Search it with "
                 "`python tools/build_catalog.py --find \"<keywords>\"` before scaffolding a new question.",
        "counts": counts,
        "rows": rows,
    }


# ---------------------------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------------------------

_STOP = set("a an the of to in on for and or is are does do can with by from as at it its this that "
            "than into when what which who how not no any one two three vs versus under over".split())


def _tokens(text: str) -> set:
    return {t for t in re.findall(r"[a-z0-9φ]+", text.lower()) if t not in _STOP and len(t) > 1}


def _row_text(r: dict) -> str:
    return " ".join(str(r.get(k, "")) for k in ("id", "slug", "title", "question", "finding", "concept",
                                                 "hypothesis", "result", "needs", "where"))


def find(query: str, catalog: dict, limit: int = 12) -> list:
    q = _tokens(query)
    scored = []
    for r in catalog["rows"]:
        toks = _tokens(_row_text(r))
        hit = q & toks
        if hit:
            # Weight by distinct matched terms, then by how much of the query matched.
            scored.append((len(hit), len(hit) / len(q), r, sorted(hit)))
    scored.sort(key=lambda t: (-t[0], -t[1], t[2]["kind"], t[2]["id"]))
    return scored[:limit]


def _print_find(query: str, catalog: dict) -> None:
    hits = find(query, catalog)
    if not hits:
        print(f"No catalog row shares a term with {query!r}. The question looks open; place it against "
              f"org_frontier/STRUCTURAL_FINDINGS.md by hand, then scaffold it.")
        return
    print(f"Nearest catalog rows to {query!r} ({len(hits)} shown; matched terms in brackets):")
    for n, frac, r, hit in hits:
        label = r.get("title") or r.get("concept") or r.get("question") or r["id"]
        gist = r.get("finding") or r.get("result") or r.get("status") or ""
        line = f"  {r['kind']:<11} {r['id']:<8} {_clip(label, 70)}"
        if gist:
            line += f" — {_clip(gist, 110)}"
        print(line + f"  [{', '.join(hit)}]")
        print(f"              {r['path']}" + (f"  ({r['runtime']})" if r.get("runtime") else ""))
    print("Read the closest rows before writing review.md. An open-thread row (kind `open`) is a "
          "contribution waiting for someone; a question or probe row that already answers you is a "
          "result to cite, stress, or extend.")


# ---------------------------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------------------------

def render() -> str:
    return json.dumps(build(), indent=1, ensure_ascii=False, sort_keys=False) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit non-zero if catalog.json is stale")
    ap.add_argument("--find", metavar="QUERY", help="print the catalog rows nearest to a question")
    args = ap.parse_args()

    if args.find:
        if hasattr(signal, "SIGPIPE"):  # absent on Windows
            signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # `| head` must not traceback
        _print_find(args.find, build())
        return 0

    new = render()
    current = open(_OUT, encoding="utf-8").read() if os.path.exists(_OUT) else ""
    if args.check:
        if new == current:
            print("catalog.json is up to date.")
            return 0
        print("catalog.json is OUT OF DATE — run: python tools/build_catalog.py")
        return 1
    if new == current:
        print("catalog.json already current; unchanged.")
        return 0
    with open(_OUT, "w", encoding="utf-8") as fh:
        fh.write(new)
    print(f"Wrote {_OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
