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
        if not os.path.isdir(d) or os.path.basename(d).startswith("__"):
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

# The four programs of the lab, each rooted at a directory whose README carries its scope. Computational
# is the hub at org_frontier/ itself (the protocol, probes, questions, studies).
_PROGRAMS = [
    ("org_frontier", "Computational — exact Φ on Boolean models: the protocol, probes, questions, studies"),
    ("org_frontier/qualitative", None),
    ("org_frontier/recurrence", None),
    ("org_frontier/survey", None),
]

# Bridge and support arms under org_frontier/. Description derived from each README's H1.
_ARMS = ["field", "cognition", "research", "classifier", "corpus", "multiparty",
         "principal", "proxy_bridge", "landscape", "outreach", "protocol"]


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


def _programs() -> list:
    out = ["## The lab — programs and arms", "",
           "Four programs on one thesis, plus the bridge and support arms. Each directory's README "
           "carries its scope; see [`org_frontier/README.md`](org_frontier/README.md) for the hub.", "",
           "| path | program / arm |", "|---|---|"]
    for rel, override in _PROGRAMS:
        readme = os.path.join(_ROOT, rel, "README.md")
        if not os.path.exists(readme):
            continue
        gloss = override or _clip(_first_heading(readme))
        out.append(_row(f"[`{rel}/`]({rel}/)", gloss))
    for name in sorted(_ARMS):
        readme = os.path.join(_ROOT, "org_frontier", name, "README.md")
        if not os.path.exists(readme):
            continue
        out.append(_row(f"[`org_frontier/{name}/`](org_frontier/{name}/)",
                        _clip(_first_heading(readme))))
    out.append("")
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
    counts = [
        ("questions", _count_dirs("org_frontier/questions/q*_*")),
        ("probes", _count_files("org_frontier/probes/probe_*.py")),
        ("studies", _count_dirs("org_frontier/studies/*")),
        ("essays", _count_files("org_frontier/essays/*.md")),
        ("foundations experiments", _count_dirs("foundations/*", marker="FINDINGS.md")),
        ("watch entries (program-level)", _count_bib("org_frontier/research/*/literature/references.bib")),
    ]
    parts = ", ".join(f"{n} {label}" for label, n in counts if n)
    return ["## At a glance", "", parts + ".", ""]


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
