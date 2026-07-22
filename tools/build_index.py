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


def _qualitative() -> list:
    """The qualitative-research arm under org_frontier/qualitative/, if present."""
    base = os.path.join(_ROOT, "org_frontier", "qualitative")
    readme = os.path.join(base, "README.md")
    if not os.path.exists(readme):
        return []
    title = _first_heading(readme) or "Qualitative research"
    summary = _clip(_first_paragraph(readme))
    out = [f"- **[{title}]({_link(readme)})** — {summary}"]
    links = []
    for fname, label in [("METHODS.md", "Methods"), ("TOPICS.md", "Topics"),
                         ("PUBLISHING.md", "Publishing")]:
        path = os.path.join(base, fname)
        if os.path.exists(path):
            links.append(f"[{label}]({_link(path)})")
    if links:
        out.append("  - " + " · ".join(links))
    for d in sorted(glob.glob(os.path.join(base, "*"))):
        name = os.path.basename(d)
        if not os.path.isdir(d) or name == "template" or name.startswith("__"):
            continue
        study = os.path.join(d, "STUDY.md")
        if not os.path.exists(study):
            continue
        s_title = _first_heading(study) or name.replace("_", " ")
        out.append(f"- [{s_title}]({_link(study)}) — {_clip(_first_paragraph(study))}")
    return out


def _survey() -> list:
    """The survey arm under org_frontier/survey/, if present."""
    base = os.path.join(_ROOT, "org_frontier", "survey")
    readme = os.path.join(base, "README.md")
    if not os.path.exists(readme):
        return []
    title = _first_heading(readme) or "Survey research"
    summary = _clip(_first_paragraph(readme))
    out = [f"- **[{title}]({_link(readme)})** — {summary}"]
    for d in sorted(glob.glob(os.path.join(base, "*"))):
        name = os.path.basename(d)
        if not os.path.isdir(d) or name == "template" or name.startswith("__"):
            continue
        study = os.path.join(d, "STUDY.md")
        if not os.path.exists(study):
            continue
        s_title = _first_heading(study) or name.replace("_", " ")
        out.append(f"- [{s_title}]({_link(study)}) — {_clip(_first_paragraph(study))}")
    return out


def _cognition() -> list:
    """The cognition arm under org_frontier/cognition/, if present."""
    base = os.path.join(_ROOT, "org_frontier", "cognition")
    readme = os.path.join(base, "README.md")
    if not os.path.exists(readme):
        return []
    title = _first_heading(readme) or "Cognition"
    summary = _clip(_first_paragraph(readme))
    out = [f"- **[{title}]({_link(readme)})** — {summary}"]
    links = []
    for fname, label in [("coordinating_through_the_opaque_third.md", "Paper"),
                         ("FINDINGS.md", "Findings"), ("THEORIES.md", "Theory batteries"),
                         ("PREDICTIVE_PROCESSING.md", "Predictive processing"),
                         ("survey_bridge.md", "Survey bridge")]:
        path = os.path.join(base, fname)
        if os.path.exists(path):
            links.append(f"[{label}]({_link(path)})")
    if links:
        out.append("  - " + " · ".join(links))
    return out


def _recurrence() -> list:
    """The recurrence arm under org_frontier/recurrence/, if present."""
    base = os.path.join(_ROOT, "org_frontier", "recurrence")
    readme = os.path.join(base, "README.md")
    if not os.path.exists(readme):
        return []
    title = _first_heading(readme) or "Recurrence"
    summary = _clip(_first_paragraph(readme))
    out = [f"- **[{title}]({_link(readme)})** — {summary}"]
    links = []
    for fname, label in [("CONCEPTS.md", "Concepts"), ("FINDINGS.md", "Bridge"),
                         ("SWEEP.md", "Sweep"), ("IIT_EXPERIMENTS.md", "Φ experiments"),
                         ("CRQA_EXPERIMENTS.md", "CRQA experiments"),
                         ("BRIDGE_FOUR.md", "Four-party")]:
        path = os.path.join(base, fname)
        if os.path.exists(path):
            links.append(f"[{label}]({_link(path)})")
    if links:
        out.append("  - " + " · ".join(links))
    return out


def _llm_variance() -> list:
    """The llm_variance program under org_frontier/llm_variance/, if present."""
    base = os.path.join(_ROOT, "org_frontier", "llm_variance")
    readme = os.path.join(base, "README.md")
    if not os.path.exists(readme):
        return []
    title = _first_heading(readme) or "LLM variance"
    summary = _clip(_first_paragraph(readme))
    out = [f"- **[{title}]({_link(readme)})** — {summary}"]
    for d in sorted(glob.glob(os.path.join(base, "*"))):
        if not os.path.isdir(d) or os.path.basename(d).startswith("__"):
            continue
        sreadme = os.path.join(d, "README.md")
        findings = os.path.join(d, "FINDINGS.md")
        if not os.path.exists(sreadme):
            continue
        stitle = _first_heading(sreadme) or os.path.basename(d).replace("_", " ")
        ssum = _clip(_first_paragraph(findings) or _finding_for(findings))
        link = f"  - **[{stitle}]({_link(sreadme)})**"
        out.append(f"{link} — {ssum}" if ssum else link)
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


def _reviews() -> list:
    """The literature-experiments arm under org_frontier/reviews/, if present."""
    base = os.path.join(_ROOT, "org_frontier", "reviews")
    readme = os.path.join(base, "README.md")
    if not os.path.exists(readme):
        return []
    title = _first_heading(readme) or "Reviews"
    summary = _clip(_first_paragraph(readme))
    out = [f"- **[{title}]({_link(readme)})** — {summary}"]
    links = []
    for fname, label in [("RESEARCH_PLAYBOOK.md", "Playbook"),
                         ("METHODS_FOUNDATIONS.md", "Methods foundations"),
                         ("template/README.md", "Template")]:
        path = os.path.join(base, fname)
        if os.path.exists(path):
            links.append(f"[{label}]({_link(path)})")
    if links:
        out.append("  - " + " · ".join(links))
    for d in sorted(glob.glob(os.path.join(base, "*"))):
        name = os.path.basename(d)
        if not os.path.isdir(d) or name in ("template", "lib") or name.startswith("__"):
            continue
        findings = os.path.join(d, "FINDINGS.md")
        if not os.path.exists(findings):
            continue
        readme_d = os.path.join(d, "README.md")
        r_title = _first_heading(readme_d) or name.replace("_", " ")
        summary = _clip(_finding_for(findings))
        link = readme_d if os.path.exists(readme_d) else d
        line = f"  - **[{r_title}]({_link(link)})**"
        out.append(f"{line} — {summary}" if summary else line)
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


def _handoff() -> list:
    """The cross-arm handoff-packet index under org_frontier/HANDOFF_PACKETS.md, if present."""
    path = os.path.join(_ROOT, "org_frontier", "HANDOFF_PACKETS.md")
    if not os.path.exists(path):
        return []
    title = _first_heading(path) or "Handoff packets"
    summary = _clip(_first_paragraph(path))
    out = [f"- **[{title}]({_link(path)})** — {summary}"]
    links = []
    for rel, label in [("survey/cohort_algorithmacy/README.md", "Survey"),
                       ("field/packets/gig_dispatch/README.md", "Field"),
                       ("recurrence/packets/template/README.md", "Recurrence"),
                       ("cognition/packets/template/README.md", "Cognition"),
                       ("qualitative/template/README.md", "Qualitative")]:
        p = os.path.join(_ROOT, "org_frontier", rel)
        if os.path.exists(p):
            links.append(f"[{label}]({_link(p)})")
    if links:
        out.append("  - " + " · ".join(links))
    return out


def _research() -> list:
    """The research-monitoring home under org_frontier/research/, if present."""
    base = os.path.join(_ROOT, "org_frontier", "research")
    readme = os.path.join(base, "README.md")
    if not os.path.exists(readme):
        return []
    title = _first_heading(readme) or "Research monitoring"
    summary = _clip(_first_paragraph(readme))
    out = [f"- **[{title}]({_link(readme)})** — {summary}"]
    links = []
    for fname, label in [("INDEX.md", "Master index"), ("CHANGELOG.md", "Changelog"),
                         ("DAILY_REFRESH.md", "Daily playbook")]:
        path = os.path.join(base, fname)
        if os.path.exists(path):
            links.append(f"[{label}]({_link(path)})")
    progs = []
    for p in ("computational", "field", "qualitative", "recurrence", "survey", "cognition"):
        pr = os.path.join(base, p, "README.md")
        if os.path.exists(pr):
            progs.append(f"[{p}]({_link(pr)})")
    if links:
        out.append("  - " + " · ".join(links))
    if progs:
        out.append("  - programs: " + " · ".join(progs))
    return out


# ---------------------------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------------------------

def build_directory() -> str:
    articles = _articles()
    syntheses = _syntheses()
    handoff = _handoff()
    research = _research()
    field = _field()
    qualitative = _qualitative()
    survey = _survey()
    recurrence = _recurrence()
    llm_variance = _llm_variance()
    cognition = _cognition()
    threads = _threads()
    studies = _studies()
    foundations = _foundations()
    reviews = _reviews()
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

    if handoff:
        L += ["### Handoff packets — pick one up and run it", "",
              "The five empirical and bridge arms, each packaged so a researcher can take a real "
              "input to a verdict: a front-door README, the pre-registration discipline, and a "
              "runnable scaffold.", ""]
        L += handoff
        L.append("")

    if research:
        L += ["### Research monitoring — a standing literature watch", "",
              "A live bibliography and review for each program, decomposed into ten topics and refreshed "
              "daily so new work is caught as it appears.", ""]
        L += research
        L.append("")

    if field:
        L += ["### Field — reading real organizations", "",
              "Bridging the in-silico work to real coordination arrangements: a field protocol "
              "and a worked demonstration.", ""]
        L += field
        L.append("")

    if qualitative:
        L += ["### Qualitative research", "",
              "The empirical arm: reading real coordination against the pre-disclosed priors, with "
              "methods and an open topic agenda for qualitative contributors.", ""]
        L += qualitative
        L.append("")

    if survey:
        L += ["### Survey — measuring algorithmacy in real workers", "",
              "The first human-subjects arm: self-report from people inside a real coordination "
              "arrangement, with the instrument and hypotheses committed before the data.", ""]
        L += survey
        L.append("")

    if recurrence:
        L += ["### Recurrence — coordination read off behavior", "",
              "Pairing exact Φ with cross-recurrence quantification: the structural measure on the "
              "model and the behavioral measure on a run of it.", ""]
        L += recurrence
        L.append("")

    if llm_variance:
        L += ["### LLM variance — how independent are model answers", "",
              "Measuring the variance problem: when N responses to one prompt look diverse but collapse to "
              "far fewer independent answers, read across lexical, structural, and semantic layers.", ""]
        L += llm_variance
        L.append("")

    if cognition:
        L += ["### Cognition — the formal bridge to cognitive science", "",
              "Where the formal apparatus meets the cognitive theories of coordination: the third "
              "party that two-party theories cannot represent, held as a member of the irreducible "
              "core.", ""]
        L += cognition
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

    if reviews:
        L += ["### Reviews — experiments on the literature", "",
              "Quantitative, systematic archival reviews: a body of scholarship treated as a dataset, "
              "with falsifiable claims about the field tested against a coded corpus and its citation "
              "graph, and intercoder reliability reported.", ""]
        L += reviews
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
