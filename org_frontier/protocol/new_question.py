"""Scaffold a new question directory from the protocol template.

A new contributor does not have to hand-copy the template or guess the next probe number.
This finds the highest probe number already logged in ``org_frontier/probes/PROBES.md``,
copies ``org_frontier/protocol/template/`` to ``org_frontier/questions/q<NN>_<slug>/``, and
substitutes the placeholders (`<NN>`, `<slug>`, the starting probe number) in each artifact.

It does not touch PROBES.md or ci/reproduce.json — you register your numbers there yourself
once the probes run, so the commit history shows hypotheses fixed before results.

Run from the repo root:
    python -m org_frontier.protocol.new_question --id 125 --slug quorum_coordination \
        --question "Does a k-of-n quorum mediator bind the parties?"

Omitting --id uses the next integer after the highest existing q<NN> directory.
"""

import argparse
import os
import re
import shutil
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
_TEMPLATE = os.path.join(_HERE, "template")
_QUESTIONS = os.path.join(_REPO_ROOT, "org_frontier", "questions")
_PROBES_MD = os.path.join(_REPO_ROOT, "org_frontier", "probes", "PROBES.md")


def next_probe_number() -> int:
    """One past the highest probe number in any leading ``| <n> |`` row of PROBES.md."""
    if not os.path.exists(_PROBES_MD):
        return 1
    with open(_PROBES_MD) as fh:
        nums = [int(m.group(1)) for m in re.finditer(r"^\|\s*(\d+)\s*\|", fh.read(), re.M)]
    return (max(nums) + 1) if nums else 1


def next_question_id() -> int:
    """One past the highest q<NN> directory under questions/."""
    if not os.path.isdir(_QUESTIONS):
        return 1
    ids = [int(m.group(1)) for d in os.listdir(_QUESTIONS)
           if (m := re.match(r"q(\d+)_", d))]
    return (max(ids) + 1) if ids else 1


def scaffold(qid: int, slug: str, question: str, start_probe: int) -> str:
    dest = os.path.join(_QUESTIONS, f"q{qid}_{slug}")
    if os.path.exists(dest):
        raise SystemExit(f"refusing to overwrite existing {dest}")
    shutil.copytree(_TEMPLATE, dest)
    open(os.path.join(dest, "__init__.py"), "w").close()

    subs = {"<NN>": str(qid), "<slug>": slug, "<N>": str(start_probe), "<question>": question}
    for name in os.listdir(dest):
        path = os.path.join(dest, name)
        if not os.path.isfile(path):
            continue
        with open(path) as fh:
            text = fh.read()
        for k, v in subs.items():
            text = text.replace(k, v)
        with open(path, "w") as fh:
            fh.write(text)
    return dest


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--id", type=int, default=None, help="question number (default: next free)")
    ap.add_argument("--slug", required=True, help="short_snake_case name, e.g. quorum_coordination")
    ap.add_argument("--question", default="<the full question text>", help="the question, in one line")
    ap.add_argument("--start-probe", type=int, default=None,
                    help="first probe number (default: next free in PROBES.md)")
    args = ap.parse_args()

    if not re.fullmatch(r"[a-z][a-z0-9_]*", args.slug):
        raise SystemExit(f"slug must be lower_snake_case: got {args.slug!r}")

    qid = args.id if args.id is not None else next_question_id()
    start = args.start_probe if args.start_probe is not None else next_probe_number()
    dest = scaffold(qid, args.slug, args.question, start)

    rel = os.path.relpath(dest, _REPO_ROOT)
    print(f"Scaffolded {rel} (probes start at {start}).")
    print("Next, following org_frontier/protocol/RESEARCH_PROTOCOL.md:")
    print(f"  1. fill review.md, then hypotheses.md, and commit BEFORE computing")
    print(f"  2. write methods.md and the probe_*.py scripts; run them from the repo root")
    print(f"  3. write FINDINGS.md and paper.md, then register numbers in ci/reproduce.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
