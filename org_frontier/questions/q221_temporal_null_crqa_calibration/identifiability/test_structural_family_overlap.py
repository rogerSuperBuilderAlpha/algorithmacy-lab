"""Fast guard against canonical-form leakage in the held-out-family pilot.

Uses the committed form-selection receipts, without rerunning slow PyPhi.
Run: python -m org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.test_structural_family_overlap
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "results" / "structural_baselines.json"


def canonical_truth_table(fid):
    family, *codes = fid
    outputs = []
    for j, c in enumerate(codes):
        bits = []
        for state in range(8):
            if family == "aff":
                value = ((state & (c >> 1)).bit_count() & 1) ^ (c & 1)
            elif family == "nsi":
                others = [k for k in range(3) if k != j]
                input_state = ((state >> others[0]) & 1) + 2 * ((state >> others[1]) & 1)
                value = (c >> input_state) & 1
            else:
                raise ValueError("unknown form family " + str(family))
            bits.append(value)
        outputs.append(tuple(bits))
    return tuple(outputs)


def split_counts():
    record = json.loads(RECEIPT.read_text(encoding="utf-8"))
    forms = record["forms"]
    nsi = [canonical_truth_table(x["fid"]) for x in forms["nsi"]]
    aff = [canonical_truth_table(x["fid"]) for x in forms["aff"]]
    return len(nsi), len(aff), len(set(nsi)), len(set(aff)), len(set(nsi) & set(aff))


def test_families_can_overlap_as_model_classes():
    assert canonical_truth_table(("nsi", 0, 0, 0)) == canonical_truth_table(("aff", 0, 0, 0))


def test_actual_selected_forms_are_nonoverlapping():
    nsi, aff, unique_nsi, unique_aff, shared = split_counts()
    assert (nsi, aff, unique_nsi, unique_aff, shared) == (80, 80, 80, 80, 0)


def main():
    test_families_can_overlap_as_model_classes()
    test_actual_selected_forms_are_nonoverlapping()
    nsi, aff, unique_nsi, unique_aff, shared = split_counts()
    print(f"q221 split identity: nsi {nsi}/{unique_nsi} unique; aff {aff}/{unique_aff} unique; shared {shared}")


if __name__ == "__main__":
    main()
