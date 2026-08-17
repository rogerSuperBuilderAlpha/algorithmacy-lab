#!/usr/bin/env python3
"""Pre-submission check for the Hospitality & Society manuscript.

Every requirement in JOURNAL_SPEC.md that a machine can decide, decided. Things a machine
cannot decide are listed at the end as author checks rather than silently passed, because a
checklist that reports only what it can test reads as a clean bill of health.

    python3 preflight.py            # DRAFT.md and the submission front matter
    python3 preflight.py FILE.md    # some other draft

Exit status is 1 if any hard requirement fails.
"""
import io
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRAFT = HERE / "DRAFT.md"
FRONT = HERE / "submission" / "FRONT_MATTER.md"

# Names and affiliations that must not appear anywhere in an anonymized manuscript.
IDENTIFYING = ["Hunt", "Berthon", "Bentley", "Pierre", "Roger", "Youse"]
VENUE = "Hospitality & Society"

results = []


def check(ok, label, detail=""):
    results.append((bool(ok), label, detail))


def words(text):
    return [t for t in text.split() if any(c.isalnum() for c in t)]


def main():
    draft = Path(sys.argv[1]) if len(sys.argv) > 1 else DRAFT
    s = io.open(draft, encoding="utf-8").read()
    body = "## 1." + s.split("## 1.", 1)[1].split("## References", 1)[0]
    refs = s.split("## References", 1)[1]
    entries = [b.strip() for b in refs.split("### Cases")[0].strip().split("\n\n") if b.strip()]

    # --- length ---------------------------------------------------------------
    n = len(words(body))
    check(n >= 6000, "body reaches the 6,000 floor", f"{n:,} words")
    check(n <= 7000, "body is not far past the floor", f"{n:,} words; author's target was 6,000 and not much over")

    # --- anonymity ------------------------------------------------------------
    hits = [w for w in IDENTIFYING if re.search(rf"\b{w}\b", body)]
    check(not hits, "no contributor name or affiliation in the body", ", ".join(hits) or "clean")
    check(VENUE not in body, "the venue is not named in the body", "found" if VENUE in body else "clean")
    check("BUILDOUT" not in s and "governing voice" not in s, "no drafting notes left in the file")

    # --- citations, both directions -------------------------------------------
    surnames = set()
    for e in entries:
        m = re.match(r"([^(]+)\(", e)
        if m:
            surnames.update(re.findall(r"[A-Z][\w’'\-]+", m.group(1)))
    cited = set(re.findall(r"([A-Z][\w’'\-]+)(?:\s+et\s+al\.)?\s+\d{4}[a-z]?", body))
    unresolved = sorted(c for c in cited if c not in surnames and c not in {"Table", "Section"})
    check(not unresolved, "every in-text citation resolves", ", ".join(unresolved[:6]) or "all resolve")

    uncited = []
    for e in entries:
        m = re.match(r"([A-Z][\w’'\-]+)", e)
        if m and m.group(1) not in body:
            uncited.append(m.group(1))
    check(not uncited, "every reference entry is cited", ", ".join(uncited[:6]) or "all cited")

    # Surname matching alone cannot see a year mismatch: a re-render can silently revert a
    # year fixed by hand in the rendered list while the in-text citation keeps the new one.
    listed = {}
    for e in entries:
        m = re.match(r"([A-Z][\w’'\-]+).*?\((\d{4}[a-z]?)\)", e)
        if m:
            listed.setdefault(m.group(1), set()).add(m.group(2))
    mismatched = sorted(
        f"{n} {y}" for n, y in re.findall(r"([A-Z][\w’'\-]+)(?:\s+(?:et\s+al\.|and\s+[A-Z][\w’'\-]+))?\s+(\d{4}[a-z]?)", body)
        if n in listed and y not in listed[n]
    )
    check(not mismatched, "in-text years match the reference list",
          ", ".join(mismatched[:6]) or "all match")

    # --- reference list form ---------------------------------------------------
    def fold(e):
        return "".join(c for c in unicodedata.normalize("NFKD", e) if not unicodedata.combining(c)).lower()

    breaks = [i for i in range(1, len(entries)) if fold(entries[i]) < fold(entries[i - 1])]
    check(not breaks, "reference list is alphabetical", f"{len(breaks)} break(s)")
    check(not re.search(r"pp\. \d+\.$", refs, re.M), "no 'pp.' before a bare article number")
    check("--" not in refs, "no LaTeX dash artifacts")
    check(not re.search(r"\d+:\d+-\d+", refs), "volume ranges use en dashes")
    check(len(entries) > 0, "reference list is present", f"{len(entries)} entries")

    # --- house style -----------------------------------------------------------
    check(body.count('"') == 0, "no double quote marks in the body", f"{body.count(chr(34))} found")
    bold = [b for b in re.findall(r"\*\*(.+?)\*\*", body, re.S) if not b.startswith("Table ")]
    check(not bold, "no bold in running text apart from table captions",
          "; ".join(b[:30] for b in bold[:3]) or "clean")
    ise = [w for w in re.findall(r"\b\w+is(?:e|ed|es|ing|ation)\b", body)
           if w.lower() not in {"raised", "praise", "precise", "revise", "revised", "arise", "arises",
                                "exercising", "improvised", "wise", "otherwise", "comprises", "promises",
                                "surprising", "advertise", "noise", "concise", "rise", "rises", "raises",
                                "raising", "rising", "raise", "arising", "praises", "praising",
                                "advise", "advised", "advises", "advising", "revise",
                                "exercise", "exercised", "exercises", "improvise", "improvised",
                                "improvises", "improvising", "revises", "revising", "devise", "devised",
                                "compromise", "compromised", "supervise", "supervised", "franchise",
                                "merchandise", "expertise", "enterprise", "premise", "premises"}]
    check(not ise, "no false '-ise' endings", ", ".join(sorted(set(ise))[:6]) or "clean")
    check("toward " not in body, "British 'towards'")

    # --- front matter ----------------------------------------------------------
    if FRONT.exists():
        fm = io.open(FRONT, encoding="utf-8").read()
        abs_txt = "Phygital hospitality scholarship" + fm.split("Phygital hospitality scholarship", 1)[1].split("## Keywords", 1)[0]
        a = len(words(abs_txt))
        check(100 <= a <= 200, "abstract within 100-200 words", f"{a} words")
        kw = fm.split("## Keywords", 1)[1].split("*", 1)[0]
        kw = "\n".join(l for l in kw.split("\n") if l.strip() and not l.strip().startswith("("))
        kws = [k.strip() for k in kw.replace("\n", " ").split(";") if k.strip()]
        check(len(kws) == 6, "exactly six keywords", f"{len(kws)}")
        check(all(len(k.split()) <= 2 for k in kws), "each keyword is one or two words",
              "; ".join(k for k in kws if len(k.split()) > 2) or "all compliant")
        hl = re.findall(r"^- (.+?) `\[(\d+)\]`", fm, re.M)
        check(3 <= len(hl) <= 5, "three to five highlights", f"{len(hl)}")
        check(all(len(h[0]) <= 85 for h in hl), "every highlight within 85 characters",
              f"longest {max((len(h[0]) for h in hl), default=0)}")
        check(all(int(h[1]) == len(h[0]) for h in hl), "highlight character counts are accurate")

    # --- report ----------------------------------------------------------------
    width = max(len(l) for _, l, _ in results)
    failed = 0
    for ok, label, detail in results:
        if not ok:
            failed += 1
        print(f"  {'PASS' if ok else 'FAIL'}  {label:<{width}}  {detail}")

    print("\n  Author checks a machine cannot make:")
    for item in [
        "page locators for the three direct quotations (the Notes require them)",
        "whether the Notes count references toward the 6,000-9,000 range",
        "ORCID for each contributor, and the two biographies",
        "the publishing agreement, postal address, ethical and conflict statements",
        "that the AI acknowledgment describes what actually happened",
        "a read-aloud pass, which no counter substitutes for",
    ]:
        print(f"    - {item}")

    print(f"\n  {len(results) - failed}/{len(results)} machine checks pass.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
