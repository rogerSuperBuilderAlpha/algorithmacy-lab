"""The compact bounded-search record must decompress to the original JSON bytes and recompress byte-identically."""
import hashlib

from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search_data as d


def test_pair_search_gz_roundtrip_and_counts():
    raw = d.raw_bytes()
    assert hashlib.sha256(raw).hexdigest() == d.RAW_SHA256
    assert d.compress(raw) == open(d.GZ, "rb").read()
    obj = d.load()
    assert len(obj["all_candidates"]) == 7488 and len(obj["verified"]) == 20
