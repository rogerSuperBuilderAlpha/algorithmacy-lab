"""Integrity tests for the committed stage-2 per-run table (no simulation, about 2 s).

`ci/reproduce.py` verifies `results/stage2_runs.csv.gz` only by re-running the full probe. These tests
check the stored file directly: its uncompressed bytes carry the SHA-256 registered in `ci/reproduce.json`,
and `read_runs` followed by `runs_csv_bytes` reproduces those bytes exactly, so the reanalysis scripts
(`margin_audit.py`, `make_figure.py`) read the same table the probe wrote."""

import gzip
import hashlib
import json
import os
import re

from org_frontier.questions.q220_observation_process_robustness.stage2 import probe_stage2 as p

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
_GZ = os.path.join(p.RESULTS, p.RUNS_FILE)


def _registered_sha256():
    with open(os.path.join(_REPO_ROOT, "ci", "reproduce.json"), encoding="utf-8") as fh:
        manifest = json.load(fh)
    checks = manifest if isinstance(manifest, list) else manifest.get("checks", manifest)
    (check,) = [c for c in checks if c["name"] == "q220-stage2-gap-aware-crqa"]
    (line,) = [e for e in check["expect"] if e.startswith("stage2_runs.csv sha256 ")]
    return re.fullmatch(r"stage2_runs\.csv sha256 ([0-9a-f]{64})", line).group(1)


def _raw():
    with gzip.open(_GZ, "rb") as fh:
        return fh.read()


def test_stored_table_matches_registered_sha256():
    assert hashlib.sha256(_raw()).hexdigest() == _registered_sha256()


def test_read_runs_round_trips_byte_for_byte():
    rows = p.read_runs()
    assert list(rows[0].keys()) == p.FIELDS
    assert len(rows) == 55_680
    assert p.runs_csv_bytes(rows) == _raw()
