"""Encode the commit history into weekly party-activity series — the field protocol's bit calibration.

Each party is a contributor. Each time step is a calendar week. A party's state in a week is active
(1) when it made at least one commit that week, inactive (0) otherwise. This is the observation and
the bit calibration of the field protocol, applied to a real series: the encoding choice is the week
and the at-least-one-commit threshold, both stated so a reader can vary them.

Two arrangements come from the two eras where several contributors overlap (see HYPOTHESES.md):
  core   2014-2018, the maintainer wmayner with the major co-developer rlmv and the early contributor
         William Marshall — a three-party coordination matching the lab's worker-system-counterpart unit.
  recent 2022-2024, the maintainer wmayner with isacdaavid, dviggiano, and ajbailey4 — a four-party
         coordination for the multiparty tools.

Reads `commits_raw.csv`; writes `activity_core.csv` and `activity_recent.csv`. Deterministic.

Run from the repo root:
    python org_frontier/recurrence/real_series/encode.py
"""

import csv
import datetime as dt
import os

HERE = os.path.dirname(__file__)
RAW = os.path.join(HERE, "commits_raw.csv")

ARRANGEMENTS = {
    "core": {
        "start": "2014-01-01", "end": "2018-12-31",
        "parties": ["wmayner", "rlmv", "William Marshall"],
    },
    "recent": {
        "start": "2022-01-01", "end": "2024-12-31",
        "parties": ["wmayner", "isacdaavid", "dviggiano", "ajbailey4"],
    },
}


def load():
    rows = []
    with open(RAW) as f:
        for r in csv.DictReader(f):
            rows.append((dt.date.fromisoformat(r["date"]), r["author"]))
    return rows


def encode(name, spec, rows):
    start = dt.date.fromisoformat(spec["start"])
    end = dt.date.fromisoformat(spec["end"])
    parties = spec["parties"]
    nweeks = (end - start).days // 7 + 1
    grid = [[0] * len(parties) for _ in range(nweeks)]
    for d, a in rows:
        if a not in parties or not (start <= d <= end):
            continue
        w = (d - start).days // 7
        grid[w][parties.index(a)] = 1
    out = os.path.join(HERE, f"activity_{name}.csv")
    with open(out, "w", newline="") as f:
        wri = csv.writer(f)
        wri.writerow(["week"] + parties)
        for i, row in enumerate(grid):
            wri.writerow([i] + row)
    active = [sum(r[j] for r in grid) for j in range(len(parties))]
    print(f"{name}: {nweeks} weeks, active-weeks " +
          ", ".join(f"{p}={active[j]}" for j, p in enumerate(parties)) + f" -> {out}")


if __name__ == "__main__":
    rows = load()
    for name, spec in ARRANGEMENTS.items():
        encode(name, spec, rows)
