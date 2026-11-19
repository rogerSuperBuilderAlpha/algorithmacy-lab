"""Fast guard against canonical-form leakage in the held-out-family pilot.

Uses the committed form-selection receipts, without rerunning slow PyPhi.
Run: python -m org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.test_structural_family_overlap
"""
import json
from itertools import permutations
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



def relabel(table, perm, mask):
    """Node permutation plus bit flips, acting on both inputs and outputs."""
    result = [[0] * 8 for _ in range(3)]
    for state in range(8):
        old = sum(((((state >> perm[j]) & 1) ^ ((mask >> j) & 1)) << j)
                  for j in range(3))
        for j in range(3):
            result[perm[j]][state] = table[j][old] ^ ((mask >> j) & 1)
    return tuple(tuple(row) for row in result)


def canonical_orbit(table):
    """Canonical truth table under the 48 allowed label and value transforms."""
    return min(relabel(table, perm, mask)
               for perm in permutations(range(3)) for mask in range(8))


def orbit_split_counts():
    record = json.loads(RECEIPT.read_text(encoding="utf-8"))
    forms = record["forms"]
    nsi = {canonical_orbit(canonical_truth_table(x["fid"])) for x in forms["nsi"]}
    aff = {canonical_orbit(canonical_truth_table(x["fid"])) for x in forms["aff"]}
    return len(nsi), len(aff), len(nsi & aff)

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



def test_actual_selected_orbits_are_nonoverlapping():
    assert orbit_split_counts() == (50, 43, 0)


def main():
    test_families_can_overlap_as_model_classes()
    test_actual_selected_forms_are_nonoverlapping()
    test_actual_selected_orbits_are_nonoverlapping()
    nsi, aff, unique_nsi, unique_aff, shared = split_counts()
    print(f"q221 split identity: nsi {nsi}/{unique_nsi} unique; aff {aff}/{unique_aff} unique; shared {shared}")
    nsi_orbits, aff_orbits, shared_orbits = orbit_split_counts()
    print(f"q221 split 48-group orbits: nsi {nsi_orbits}; aff {aff_orbits}; shared {shared_orbits}")


if __name__ == "__main__":
    main()
