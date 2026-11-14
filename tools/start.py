#!/usr/bin/env python3
"""Start here: set up the lab and compute your first verdict.

Run from the repo root with any Python 3:

    python3 tools/start.py

It does four things, and prints what it is doing at each step:

1. Finds a Python the pinned PyPhi build installs on (3.10, 3.11 or 3.12), or uses `uv` to fetch 3.12.
2. Creates `venv/` and installs `requirements.txt` (needs network; about a minute with a prebuilt wheel).
3. Runs the instrument controls. A verdict means nothing until this prints "Instrument validated".
4. Computes two exact Φ verdicts: a three-party form that is triadic, and the same form with one
   dependency removed, which is dyadic.

Flags:
    --check    only report the environment (Python, compiler, uv, venv); install and run nothing
    --no-demo  stop after the instrument controls

This script uses only the standard library, so it runs before anything is installed.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VENV = os.path.join(ROOT, "venv")
SUPPORTED = ("python3.12", "python3.11", "python3.10")

DEMO = r"""
from org_frontier.probes.lib import verdict
# W' = S, S' = W AND C, C' = S: the mediator's next state depends on both others
triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
# the same form with one dependency removed: S' = W (S no longer reads C)
dyad = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]
print("  mediator reads worker AND counterpart ->", verdict(triad, ("W", "S", "C")).structure)
print("  mediator reads the worker only        ->", verdict(dyad, ("W", "S", "C")).structure)
"""


def say(msg: str = "") -> None:
    print(msg, flush=True)


def py_version(exe: str) -> tuple | None:
    try:
        out = subprocess.run([exe, "-c", "import sys; print(*sys.version_info[:2])"],
                             capture_output=True, text=True, timeout=20)
        major, minor = out.stdout.split()
        return int(major), int(minor)
    except Exception:
        return None


def has_cxx() -> bool:
    return any(shutil.which(c) for c in ("g++", "c++", "clang++"))


def find_python() -> tuple[str | None, str]:
    """Return (interpreter, note). None means no usable interpreter was found."""
    for name in SUPPORTED:
        exe = shutil.which(name)
        if exe:
            return exe, f"found {name}"
    here = sys.version_info[:2]
    if (3, 10) <= here <= (3, 12):
        return sys.executable, f"using the running Python {here[0]}.{here[1]}"
    if here >= (3, 13) and has_cxx():
        return sys.executable, (f"using Python {here[0]}.{here[1]}; "
                                "graphillion will compile from source with your C++ compiler")
    return None, f"no Python 3.10-3.12 found (this one is {here[0]}.{here[1]})"


def venv_python() -> str:
    sub = os.path.join("Scripts", "python.exe") if os.name == "nt" else os.path.join("bin", "python")
    return os.path.join(VENV, sub)


def run(cmd: list[str], echo: bool = True, **kw) -> int:
    if echo:
        say("  $ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=ROOT, **kw).returncode


def report_env() -> None:
    exe, note = find_python()
    say("Environment")
    say(f"  python on PATH   : {sys.version.split()[0]} ({sys.executable})")
    say(f"  usable interpreter: {exe or 'none'} ({note})")
    say(f"  C++ compiler     : {'yes' if has_cxx() else 'no'}")
    say(f"  uv               : {'yes' if shutil.which('uv') else 'no'}")
    say(f"  venv/            : {'present' if os.path.exists(venv_python()) else 'not created yet'}")


def create_venv() -> bool:
    if os.path.exists(venv_python()):
        say("venv/ already exists; reusing it.")
        return True
    exe, note = find_python()
    if exe:
        say(f"Creating venv/ ({note}).")
        return run([exe, "-m", "venv", VENV]) == 0
    uv = shutil.which("uv")
    if uv:
        say(f"{note}. Using uv to fetch Python 3.12.")
        return run([uv, "venv", "--python", "3.12", VENV]) == 0
    say(f"Stopping: {note}.")
    say("  PyPhi's pinned build needs Python 3.10, 3.11 or 3.12. Python 3.13 and newer also work, but only")
    say("  with a C++ compiler on the machine (graphillion has no prebuilt wheel there).")
    say("  Fix with one of:")
    say("    - install Python 3.12 (python.org, pyenv, or your package manager), then rerun this script;")
    say("    - install uv (https://docs.astral.sh/uv/), which fetches 3.12 itself, then rerun;")
    say("    - install a C++ compiler (Debian/Ubuntu: apt install g++; macOS: xcode-select --install).")
    return False


def install() -> bool:
    py = venv_python()
    uv = shutil.which("uv")
    say("Installing requirements.txt (needs network; PyPhi and phyid come from git).")
    # a venv made by `uv venv` has no pip, so install through uv when it is available
    has_pip = subprocess.run([py, "-m", "pip", "--version"], capture_output=True).returncode == 0
    if has_pip:
        return run([py, "-m", "pip", "install", "-q", "-r", "requirements.txt"]) == 0
    if uv:
        return run([uv, "pip", "install", "-q", "--python", py, "-r", "requirements.txt"]) == 0
    say("The venv has no pip and uv is not installed; delete venv/ and rerun.")
    return False


def validate() -> bool:
    say("Running the instrument controls (about five seconds).")
    out = subprocess.run([venv_python(), "-m", "org_frontier.classifier.validate"],
                         cwd=ROOT, capture_output=True, text=True)
    tail = [ln for ln in out.stdout.splitlines() if ln.strip()][-4:]
    for ln in tail:
        say("  " + ln.strip())
    if "Instrument validated" in out.stdout:
        return True
    say("The instrument did not validate. Do not trust any verdict. Output above; stderr follows.")
    say(out.stderr[-1500:])
    return False


def demo() -> bool:
    say("Computing two exact verdicts.")
    return run([venv_python(), "-c", DEMO], echo=False) == 0


NEXT = """
Next steps (from the repo root, with `source venv/bin/activate`; on Windows `venv\\Scripts\\activate`):

  See a full probe       python -m org_frontier.probes.probe_control            # Probe 7, about two seconds
  Test your own form     edit the rules in the snippet above, rerun it in `python`
  Ask whether the lab has already answered your question
                         python tools/build_catalog.py --find "your question keywords"
  Pick an open thread    OPEN_QUESTIONS.md  (rows marked `compute` run on a laptop today)
  Contribute a result    GETTING_STARTED.md, then open a pull request into the `contrib` branch

Scope: these are in-silico results on small Boolean models. They are evidence about the models, not
measurements of a real organization.
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="report the environment and stop")
    ap.add_argument("--no-demo", action="store_true", help="stop after the instrument controls")
    args = ap.parse_args()

    if not os.path.exists(os.path.join(ROOT, "requirements.txt")):
        say(f"Run this from a clone of algorithmacy-lab (no requirements.txt under {ROOT}).")
        return 2
    report_env()
    if args.check:
        return 0
    say()
    if not create_venv() or not install():
        return 1
    say()
    if not validate():
        return 1
    if not args.no_demo:
        say()
        if not demo():
            return 1
    say(NEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
