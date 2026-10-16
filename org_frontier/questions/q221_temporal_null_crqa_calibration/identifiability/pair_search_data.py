"""Compact storage for the bounded-search record (results/pair_search.json, 716 KB).

The committed artefact is results/pair_search.json.gz. It is written deterministically (gzip level 9,
mtime 0, no file name) from the exact bytes of the original JSON. RAW_SHA256 is the SHA-256 of those
original bytes, and load() checks it on every read.

- load(): returns the parsed dict straight from the .gz file. All q221 executor scripts use this.
- python -m org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.pair_search_data --restore
  writes results/pair_search.json byte-identically (git-ignored), for scripts that open that path directly,
  such as independent_audit/screen_all_candidates.py and screen_verified_marginals.py.
- python -m ...pair_search_data --check verifies the gz->raw checksum and that re-compressing the restored
  bytes reproduces the committed .gz exactly.
- Full regeneration from scratch is identifiability/pair_search.py (deterministic, about 290 s). It writes
  through save()."""
import gzip
import hashlib
import io
import json
import os
import sys

RES = os.path.join(os.path.dirname(__file__), "results")
GZ = os.path.join(RES, "pair_search.json.gz")
RAW = os.path.join(RES, "pair_search.json")
RAW_SHA256 = "7c54d45b690081003c836b696d6d63014aa5428a1d8221449a3ba2c75a58ba13"


def compress(raw: bytes) -> bytes:
    buf = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", compresslevel=9, fileobj=buf, mtime=0) as f:
        f.write(raw)
    return buf.getvalue()


def raw_bytes() -> bytes:
    raw = gzip.decompress(open(GZ, "rb").read())
    h = hashlib.sha256(raw).hexdigest()
    if h != RAW_SHA256:
        raise ValueError("pair_search.json.gz content checksum mismatch: %s" % h)
    return raw


def load():
    return json.loads(raw_bytes())


def save(obj):
    """Used by pair_search.py: same JSON formatting as the original (indent=1, default=str)."""
    raw = json.dumps(obj, indent=1, default=str).encode()
    open(GZ, "wb").write(compress(raw))
    return hashlib.sha256(raw).hexdigest()


def main(argv):
    raw = raw_bytes()
    if "--restore" in argv:
        open(RAW, "wb").write(raw)
        print("restored %s (%d bytes, sha256 %s)" % (RAW, len(raw), RAW_SHA256))
    if "--check" in argv or len(argv) == 0:
        assert compress(raw) == open(GZ, "rb").read(), "re-compression is not byte-identical"
        print("pair_search.json.gz OK: raw sha256 %s, %d raw bytes, %d gz bytes"
              % (RAW_SHA256, len(raw), os.path.getsize(GZ)))


if __name__ == "__main__":
    main(sys.argv[1:])
