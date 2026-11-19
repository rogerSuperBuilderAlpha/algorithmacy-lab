"""Check an encodings file before anything is computed.

    python -m irreducibility.encode_check examples/01_gig_dispatch/encodings.json

Three gates, in order:
  1. admissibility: every rule parses, cites evidence, the mediator names an alternative, and every
     encoding carries a prediction (irreducibility.encoding.validate);
  2. evidence is real: every quoted passage occurs verbatim in the cited source file (resolved
     relative to the encodings file), so a drafter, human or model, cannot cite a passage that is not
     there;
  3. nothing else: this script never computes Φ, so a prediction cannot be adjusted after seeing it.

Exit code 0 if all gates pass.
"""

import os
import re
import sys

from .encoding import load, validate


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("“", '"').replace("”", '"')).strip()


def check_quotes(doc: dict, base_dir: str):
    problems, cache = [], {}
    for enc in doc.get("encodings", []):
        for party, items in enc.get("evidence", {}).items():
            for item in items:
                src = item.get("source", "")
                path = os.path.join(base_dir, src)
                if path not in cache:
                    try:
                        with open(path, encoding="utf-8") as f:
                            cache[path] = _norm(f.read())
                    except OSError:
                        cache[path] = None
                text = cache[path]
                if text is None:
                    problems.append(f"[{enc.get('id')}] {party}: source {src!r} not found")
                elif _norm(item.get("quote", "")) not in text:
                    problems.append(f"[{enc.get('id')}] {party}: quote not found verbatim in {src}: "
                                    f"{item.get('quote', '')[:70]!r}")
    return problems


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__)
        return 2
    path = argv[0]
    doc = load(path)
    problems = validate(doc) + check_quotes(doc, os.path.dirname(os.path.abspath(path)))
    n = len(doc.get("encodings", []))
    if problems:
        print(f"REJECTED: {len(problems)} problem(s) in {n} encoding(s)")
        for p in problems:
            print("  - " + p)
        return 1
    print(f"ADMISSIBLE: {n} encoding(s); every rule has evidence found verbatim in its source; "
          f"every encoding carries a prediction.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
