"""Generate the navigable directory in README.md from the repository's content.

Scans the questions, studies, essays, synthesis/review articles, and foundations, and writes a
directory between the markers

    <!-- BEGIN GENERATED DIRECTORY (tools/build_index.py) -->
    ...
    <!-- END GENERATED DIRECTORY -->

in README.md. The text outside the markers — the central thesis, setup, contributing — is left
untouched. Run after adding or merging any experiment so the README stays a current map of the lab.

    python tools/build_index.py            # rewrite the directory in place
    python tools/build_index.py --check    # exit non-zero if the directory is stale (CI gate)

Deterministic: every list is sorted, so the output depends only on the content, not on filesystem
order.
"""

import argparse
import glob
import os
import re
import sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_README = os.path.join(_ROOT, "README.md")
_BEGIN = "<!-- BEGIN GENERATED DIRECTORY (tools/build_index.py) -->"
_END = "<!-- END GENERATED DIRECTORY -->"


# ---------------------------------------------------------------------------------------------
# Small text helpers
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


def _first_paragraph(path: str) -> str:
    """The first non-empty, non-heading, non-table paragraph line."""
    try:
        with open(path) as fh:
            for line in fh:
                s = line.strip()
                if s and not s.startswith(("#", "|", ">", "<", "-", "*", "```")):
                    return s
    except OSError:
        pass
    return ""


def _clip(text: str, n: int = 165) -> str:
    """One-line clip: collapse whitespace, cut at a sentence or word boundary near n chars."""
    text = re.sub(r"\s+", " ", text).strip().rstrip(".")
    if len(text) <= n:
        return text
    cut = text[:n]
    dot = cut.rfind(". ")
    if dot > n // 2:
        return cut[:dot]
    sp = cut.rfind(" ")
    return (cut[:sp] if sp > 0 else cut).rstrip(",;:") + "…"


def _strip_q_prefix(title: str) -> str:
    """Drop a leading 'Q123 — ' / 'Q123 -- ' / 'Q123 findings — ' style prefix."""
    return re.sub(r"^Q\d+\s*(findings)?\s*[—\-:]*\s*", "", title, flags=re.I).strip()


_METHODS_BOILERPLATE = ("Probe", "Form:", "Form ", "Exact ", "Setup", "Code")


def _clean_finding(text: str) -> str:
    """Reduce a heading/paragraph to a finding, or "" when it is only a generic label."""
    text = _strip_q_prefix(text)
    text = re.sub(r"\(findings?\)$", "", text, flags=re.I).strip(" —-:")
    text = re.sub(r"^findings?\b[ —\-:]*", "", text, flags=re.I).strip(" —-:")
    if text.lower() in ("", "findings", "finding"):
        return ""
    return text


def _finding_for(findings_path: str) -> str:
    """A one-line finding for a FINDINGS.md: its heading if substantive, else its summary
    paragraph, skipping methods boilerplate."""
    h = _clean_finding(_first_heading(findings_path))
    if h:
        return _clip(h, 150)
    p = _first_paragraph(findings_path)
    if p and not p.startswith(_METHODS_BOILERPLATE):
        return _clip(p, 150)
    return ""


def _link(path: str) -> str:
    """Repo-relative POSIX path for a markdown link."""
    return os.path.relpath(path, _ROOT).replace(os.sep, "/")


# ---------------------------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------------------------

def _articles() -> list:
    out = []
    for path in sorted(glob.glob(os.path.join(_ROOT, "org_frontier", "essays", "*.md"))):
        title = _first_heading(path) or os.path.basename(path)
        out.append(f"- [{title}]({_link(path)})")
    return out


def _syntheses() -> list:
    """Curated cross-program syntheses, reviews, programs, and the open agenda."""
    of = os.path.join(_ROOT, "org_frontier")
    picks = []
    programs = sorted(glob.glob(os.path.join(of, "RESEARCH_PROGRAM_V*.md")),
                      key=lambda p: int(re.search(r"_V(\d+)", p).group(1)))
    if programs:
        picks.append((programs[-1], "the current research program"))
    for name, gloss in [
        ("RESEARCH_NARRATIVE.md", "the narrative arc across questions"),
        ("STRUCTURAL_FINDINGS.md", "the standing structural findings"),
        ("CRITICAL_REVIEW_Q111_Q117.md", "a critical self-review"),
        ("PAPER_PIPELINE.md", "the plan to turn paper-less work into full papers"),
        ("RESEARCH_AGENDA_50_V2.md", "the open agenda — questions waiting for a contributor"),
    ]:
        path = os.path.join(of, name)
        if os.path.exists(path):
            picks.append((path, gloss))
    out = []
    for path, gloss in picks:
        title = _first_heading(path) or os.path.basename(path)
        out.append(f"- [{title}]({_link(path)}) — {gloss}")
    return out


def _threads() -> list:
    """Deep exploratory single-question threads under org_frontier/threads/."""
    out = []
    for d in sorted(glob.glob(os.path.join(_ROOT, "org_frontier", "threads", "*"))):
        thread = os.path.join(d, "THREAD.md")
        if not os.path.isdir(d) or not os.path.exists(thread):
            continue
        title = _first_heading(thread) or os.path.basename(d).replace("_", " ")
        summary = _clip(_first_paragraph(thread))
        out.append(f"- [{title}]({_link(thread)}) — {summary}")
    return out


def _field() -> list:
    """The real-organizations field program, if present."""
    base = os.path.join(_ROOT, "org_frontier", "field")
    readme = os.path.join(base, "README.md")
    if not os.path.exists(readme):
        return []
    title = _first_heading(readme) or "Field"
    summary = _clip(_first_paragraph(readme))
    out = [f"- **[{title}]({_link(readme)})** — {summary}"]
    links = []
    for fname, label in [("PROTOCOL.md", "Protocol"), ("FINDINGS.md", "Findings")]:
        path = os.path.join(base, fname)
        if os.path.exists(path):
            links.append(f"[{label}]({_link(path)})")
    if links:
        out.append("  - " + " · ".join(links))
    return out


def _studies() -> list:
    out = []
    for d in sorted(glob.glob(os.path.join(_ROOT, "org_frontier", "studies", "*"))):
        if not os.path.isdir(d) or os.path.basename(d).startswith("__"):
            continue
        readme = os.path.join(d, "README.md")
        findings = os.path.join(d, "FINDINGS.md")
        title = _first_heading(readme) or os.path.basename(d).replace("_", " ")
        summary = _clip(_first_paragraph(findings) or _finding_for(findings))
        link = readme if os.path.exists(readme) else d
        line = f"- **[{title}]({_link(link)})**"
        out.append(f"{line} — {summary}" if summary else line)
    return out


def _foundations() -> list:
    out = []
    skip = {"__pycache__", "paper"}
    for d in sorted(glob.glob(os.path.join(_ROOT, "foundations", "*"))):
        name = os.path.basename(d)
        if not os.path.isdir(d) or name in skip or name.startswith("__"):
            continue
        findings = os.path.join(d, "FINDINGS.md")
        if not os.path.exists(findings):
            continue
        heading = re.sub(r"^findings?\s*[:—\-]\s*", "", _first_heading(findings), flags=re.I)
        title = heading.strip() or name.replace("_", " ")
        out.append(f"- [`{name}`]({_link(d)}) — {_clip(title, 130)}")
    return out


def _question_rows() -> list:
    rows = []
    for d in glob.glob(os.path.join(_ROOT, "org_frontier", "questions", "q*")):
        m = re.match(r"q(\d+)_", os.path.basename(d))
        if not m or not os.path.isdir(d):
            continue
        num = int(m.group(1))
        paper = os.path.join(d, "paper.md")
        findings = os.path.join(d, "FINDINGS.md")
        title = _strip_q_prefix(_first_heading(paper)) or os.path.basename(d)[len(m.group(0)):].replace("_", " ")
        finding = _finding_for(findings)
        link = paper if os.path.exists(paper) else d
        title = title.replace("|", "\\|")
        finding = finding.replace("|", "\\|")
        rows.append((num, f"| [Q{num}]({_link(link)}) | {title} | {finding} |"))
    rows.sort()
    return [r for _, r in rows]


# ---------------------------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------------------------

def build_directory() -> str:
    articles = _articles()
    syntheses = _syntheses()
    field = _field()
    threads = _threads()
    studies = _studies()
    foundations = _foundations()
    qrows = _question_rows()

    L = [_BEGIN,
         "## Directory",
         "",
         "*A map of the lab, regenerated by `tools/build_index.py`. Do not edit this section by "
         "hand — edits are overwritten on the next build.*",
         ""]

    L += ["### Reviews & articles",
          "",
          "Cross-program essays and reviews — the best places to start window-shopping.",
          ""]
    L += articles
    L.append("")

    if syntheses:
        L += ["### Programs, syntheses & the open agenda", ""]
        L += syntheses
        L.append("")

    if field:
        L += ["### Field — reading real organizations", "",
              "Bridging the in-silico work to real coordination arrangements: a field protocol "
              "and a worked demonstration.", ""]
        L += field
        L.append("")

    if threads:
        L += ["### Threads", "",
              "Deep single-question dives, each driven by its own results.", ""]
        L += threads
        L.append("")

    if studies:
        L += ["### Studies", "",
              "Multi-experiment batteries on one theme.", ""]
        L += studies
        L.append("")

    if foundations:
        L += ["### Foundations — what tracks Φ", "",
              "The measure-validation arc that established exact Φ as the instrument.", ""]
        L += foundations
        L.append("")

    L += [f"### Questions — the logbook ({len(qrows)})",
          "",
          "Each question fixes five hypotheses, runs them against the exact-Φ instrument, and "
          "writes a paper. The full per-probe log is "
          "[`org_frontier/probes/PROBES.md`](org_frontier/probes/PROBES.md).",
          "",
          "<details>",
          f"<summary>Browse all {len(qrows)} questions</summary>",
          "",
          "| # | Question | Finding |",
          "|---|----------|---------|"]
    L += qrows
    L += ["",
          "</details>",
          "",
          _END]
    return "\n".join(L)


def render_readme() -> str:
    with open(_README) as fh:
        text = fh.read()
    block = build_directory()
    if _BEGIN in text and _END in text:
        pre = text[:text.index(_BEGIN)]
        post = text[text.index(_END) + len(_END):]
        return pre + block + post
    raise SystemExit(
        f"README.md is missing the markers {_BEGIN!r} / {_END!r}; add them where the directory "
        "should go.")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if the directory in README.md is stale")
    args = ap.parse_args()

    new = render_readme()
    with open(_README) as fh:
        current = fh.read()

    if args.check:
        if new == current:
            print("Directory is up to date.")
            return 0
        print("Directory is OUT OF DATE — run: python tools/build_index.py")
        return 1

    if new == current:
        print("Directory already current; README.md unchanged.")
        return 0
    with open(_README, "w") as fh:
        fh.write(new)
    print("Rewrote the directory in README.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
