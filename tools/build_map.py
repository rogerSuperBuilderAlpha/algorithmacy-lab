"""Generate MAP.md — a one-screen index of the repository for agents and humans.

MAP.md is fully generated: a compact map of the entry documents, the lab's programs and arms, the
machinery that keeps the repo current, and the live counts (questions, probes, studies, watch entries).
It is the cheap-to-load companion to README.md's full directory and AGENTS.md's operating manual.

    python tools/build_map.py            # rewrite MAP.md in place
    python tools/build_map.py --check    # exit non-zero if MAP.md is stale (CI gate)

Deterministic and standard-library only: every list is sorted or curated, and the derived rows and
counts depend only on the files on disk. Run after adding or removing a program, arm, study, or probe.
"""

import argparse
import glob
import os
import re
import sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_MAP = os.path.join(_ROOT, "MAP.md")


# ---------------------------------------------------------------------------------------------
# Small helpers (mirrors tools/build_index.py conventions)
# ---------------------------------------------------------------------------------------------

def _first_heading(path: str) -> str:
    """The first markdown H1, or "" if none."""
    try:
        with open(path) as fh:
            for line in fh:
                if line.startswith("# "):
                    return line[2:].strip()
    except OSError:
        pass
    return ""


def _clip(text: str, n: int = 90) -> str:
    """One-line clip: collapse whitespace, cut at a word boundary near n chars."""
    text = re.sub(r"\s+", " ", text).strip().rstrip(".")
    if len(text) <= n:
        return text
    cut = text[:n]
    sp = cut.rfind(" ")
    return (cut[:sp] if sp > 0 else cut).rstrip(",;:—-") + "…"


def _link(path: str) -> str:
    """Repo-relative POSIX path for a markdown link."""
    return os.path.relpath(path, _ROOT).replace(os.sep, "/")


def _exists(rel: str) -> bool:
    return os.path.exists(os.path.join(_ROOT, rel))


def _count_dirs(pattern: str, marker: str = None) -> int:
    """Count directories matching the glob, skipping dunder dirs. With a marker filename, count only
    the directories that contain it — the repo's definition of a real experiment or study."""
    n = 0
    for d in glob.glob(os.path.join(_ROOT, pattern)):
        if not os.path.isdir(d) or os.path.basename(d).startswith("__") \
                or os.path.basename(d) == "template":
            continue
        if marker and not os.path.exists(os.path.join(d, marker)):
            continue
        n += 1
    return n


def _count_files(pattern: str) -> int:
    return len(glob.glob(os.path.join(_ROOT, pattern)))


def _count_bib(pattern: str) -> int:
    total = 0
    for path in glob.glob(os.path.join(_ROOT, pattern)):
        try:
            with open(path) as fh:
                total += len(re.findall(r"^@\w+\s*\{", fh.read(), re.M))
        except OSError:
            pass
    return total


def _row(label_link: str, gloss: str) -> str:
    return f"| {label_link} | {gloss} |"


# ---------------------------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------------------------

# Curated entry documents, in reading order. Each row is emitted only if the file exists, so a
# removed document drops out of the map.
_ENTRY_DOCS = [
    ("NOW.md", "This week's live deadlines and canonical drafts — read this first"),
    ("START_HERE.md", "Guided onboarding an AI assistant runs for a newcomer: from \"what is this?\" to a first computed verdict"),
    ("AGENTS.md", "Operating manual for agents: map, run/verify, git rule, land flow, done-checklist"),
    ("README.md", "What the lab is, the thesis, setup, and the full generated directory"),
    ("OVERVIEW.md", "Five-minute orientation: the argument, where it stands, where to contribute"),
    ("GETTING_STARTED.md", "Hands-on: environment → confirm the instrument → scaffold → register → PR"),
    ("CONTRIBUTING.md", "Code, probe, study, and house-style conventions a submission must meet"),
    ("REPO_LAYOUT.md", "The two-repo git trap: this repo vs the nested private dissertation"),
    ("PUBLISHING.md", "The reproducibility-first public review process for essays and studies"),
    ("MAINTAINERS.md", "The review board and how to apply"),
    ("CLAUDE.md", "House writing style, the dissertation spine, and git-push rules"),
    ("llms.txt", "Token-light brief for representing the project to outside agents and LLM tools"),
]

# Curated machinery: the generators and the gates that keep the repo current. Command, then what it
# keeps in sync. Emitted only when the script exists.
_MACHINERY = [
    ("tools/build_index.py", "python tools/build_index.py", "the generated directory in README.md"),
    ("tools/build_map.py", "python tools/build_map.py", "this file, MAP.md"),
    ("org_frontier/research/build_research_index.py",
     "python org_frontier/research/build_research_index.py", "the research watch INDEX.md"),
    ("ci/reproduce.py", "python ci/reproduce.py", "every registered number in ci/reproduce.json"),
]

# Grouped lab surface. Computational is the hub at org_frontier/ itself.
_INSTRUMENT = [
    ("foundations", "Instrument validation — what tracks exact IIT-4.0 Φ"),
]
_COMPUTATIONAL = [
    ("org_frontier", "Computational — exact Φ on Boolean models: the protocol, probes, questions, studies"),
]
_EMPIRICAL = [
    ("org_frontier/field", None),
    ("org_frontier/qualitative", None),
    ("org_frontier/recurrence", None),
    ("org_frontier/survey", None),
    ("org_frontier/cognition", None),
]
_COMPUTATIONAL_ARMS = ["classifier", "corpus", "multiparty", "principal", "proxy_bridge",
                       "landscape", "outreach", "protocol", "llm_variance", "research", "reviews"]
_SUBMISSIONS = [
    ("submissions", "Outward manuscripts — IGI, Hospitality & Society, Lima, Slacker, OT, Hegel"),
    ("submissions/coordinative_sovereignty", None),
    ("submissions/hospitality_phygital", None),
    ("submissions/lima_pdw", None),
    ("submissions/slacker_thirds", None),
    ("submissions/hegel_coordination", None),
    ("submissions/proposals", None),
]


def _entry_docs() -> list:
    out = ["## Entry documents", "",
           "Start here. The full directory lives in [`README.md`](README.md); the operating manual in "
           "[`AGENTS.md`](AGENTS.md).", "",
           "| file | what it is |", "|---|---|"]
    for rel, gloss in _ENTRY_DOCS:
        if _exists(rel):
            out.append(_row(f"[`{rel}`]({rel})", gloss))
    out.append("")
    return out


def _section(title: str, intro: str, rows: list) -> list:
    out = [f"## {title}", "", intro, "",
           "| path | what it is |", "|---|---|"]
    out += rows
    out.append("")
    return out


def _rows_from(pairs: list) -> list:
    rows = []
    for rel, override in pairs:
        readme = os.path.join(_ROOT, rel, "README.md")
        if not os.path.exists(readme):
            continue
        gloss = override or _clip(_first_heading(readme))
        rows.append(_row(f"[`{rel}/`]({rel}/)", gloss))
    return rows


def _programs() -> list:
    out = []
    out += _section(
        "Instrument",
        "Measure-validation: why exact Φ, not a cheap proxy.",
        _rows_from(_INSTRUMENT),
    )
    comp = _rows_from(_COMPUTATIONAL)
    for name in sorted(_COMPUTATIONAL_ARMS):
        readme = os.path.join(_ROOT, "org_frontier", name, "README.md")
        if not os.path.exists(readme):
            continue
        # Skip stub READMEs left at old writing-arm paths (they start with "# Moved").
        heading = _first_heading(readme)
        if heading == "Moved":
            continue
        comp.append(_row(f"[`org_frontier/{name}/`](org_frontier/{name}/)",
                         _clip(heading)))
    out += _section(
        "Computational lab",
        "Exact Φ on Boolean models. Import paths stay `org_frontier.*`. Hub: "
        "[`org_frontier/README.md`](org_frontier/README.md).",
        comp,
    )
    out += _section(
        "Empirical and bridge arms",
        "Field, qualitative, recurrence, survey, cognition — packets ready; most still pre-field.",
        _rows_from(_EMPIRICAL),
    )
    out += _section(
        "Submissions",
        "Outward manuscripts. Live dates in [`NOW.md`](NOW.md) and "
        "[`submissions/CALENDAR.md`](submissions/CALENDAR.md).",
        _rows_from(_SUBMISSIONS),
    )
    return out


def _machinery() -> list:
    out = ["## Machinery — generators and gates", "",
           "Run the relevant generator after adding content, then verify with its `--check`. CI "
           "regenerates on same-repo PRs and gates fork PRs.", "",
           "| script | command | keeps current |", "|---|---|---|"]
    for rel, cmd, keeps in _MACHINERY:
        if _exists(rel):
            out.append(f"| [`{rel}`]({rel}) | `{cmd}` | {keeps} |")
    out.append("")
    return out


def _at_a_glance() -> list:
    # (label, count, source) — the source names exactly what each count measures, so a reader cannot
    # mis-attribute it (e.g. studies counts org_frontier/studies/, not the survey arm).
    counts = [
        ("questions", _count_dirs("org_frontier/questions/q*_*"),
         "`org_frontier/questions/q*_*/`"),
        ("probes", _count_files("org_frontier/probes/probe_*.py"),
         "`org_frontier/probes/probe_*.py`"),
        ("studies", _count_dirs("org_frontier/studies/*"),
         "`org_frontier/studies/*/`"),
        ("essays", _count_files("org_frontier/essays/*.md"),
         "`org_frontier/essays/*.md`"),
        ("foundations experiments", _count_dirs("foundations/*", marker="FINDINGS.md"),
         "`foundations/*/` with a `FINDINGS.md`"),
        ("literature reviews", _count_dirs("org_frontier/reviews/*", marker="FINDINGS.md"),
         "`org_frontier/reviews/*/` with a `FINDINGS.md`"),
        ("watch entries (program-level)", _count_bib("org_frontier/research/*/literature/references.bib"),
         "`org_frontier/research/*/literature/references.bib`"),
    ]
    out = ["## At a glance", "", "| count | what | source |", "|---|---|---|"]
    for label, n, source in counts:
        if n:
            out.append(f"| {n} | {label} | {source} |")
    out.append("")
    return out


# ---------------------------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------------------------

def build() -> str:
    L = ["# Repository map", "",
         "*Generated by `tools/build_map.py`. Do not edit by hand — regenerated on every PR.*", "",
         "A one-screen index of the lab. For how to navigate, run, verify, and land a change, read "
         "[`AGENTS.md`](AGENTS.md); for the full per-experiment directory, read [`README.md`](README.md).",
         ""]
    L += _entry_docs()
    L += _programs()
    L += _machinery()
    L += _at_a_glance()
    return "\n".join(L).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if MAP.md is stale")
    args = ap.parse_args()

    new = build()
    current = open(_MAP).read() if os.path.exists(_MAP) else ""

    if args.check:
        if new == current:
            print("MAP.md is up to date.")
            return 0
        print("MAP.md is OUT OF DATE — run: python tools/build_map.py")
        return 1

    if new == current:
        print("MAP.md already current; unchanged.")
        return 0
    with open(_MAP, "w") as fh:
        fh.write(new)
    print(f"Wrote {_MAP}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
