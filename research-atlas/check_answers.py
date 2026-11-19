"""Check the atlas answer examples against their cited repo snapshots."""

import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures"
KINDS = {"model_result", "open_question", "research_target"}


def check_fixture(path):
    data = json.loads(path.read_text())
    assert data["question"] and data["answer"] and data["claims"], path
    kinds = set()
    for claim in data["claims"]:
        assert claim["kind"] in KINDS and claim["text"] and claim["evidence"], path
        kinds.add(claim["kind"])
        for evidence in claim["evidence"]:
            source = evidence["path"]
            snapshot = evidence["snapshot"]
            assert re.fullmatch(r"[0-9a-f]{40}", snapshot), (path, snapshot)
            assert not Path(source).is_absolute() and ".." not in Path(source).parts, source
            content = subprocess.check_output(
                ["git", "show", f"{snapshot}:{source}"], cwd=ROOT, text=True
            )
            assert evidence["quote"] in content, (path, source, evidence["quote"])
    answer = data["answer"].lower()
    if "open_question" in kinds:
        assert "open" in answer and "does not resolve" in answer, path
    if "research_target" in kinds:
        assert "target" in answer and "unmeasured" in answer, path
        assert not re.search(r"(?:observed|achieved|measured|reached)\s+[^.]*(?:0\.80|80%)", answer), path
    if "model_result" in kinds:
        assert any(word in answer for word in ("model", "synthetic", "in-silico")), path
        assert any(word in answer for word in ("real", "field")), path


def main():
    paths = sorted(FIXTURES.glob("*.json"))
    assert len(paths) == 3, f"Expected three fixtures, found {len(paths)}"
    for path in paths:
        check_fixture(path)
    print(f"Checked {len(paths)} atlas answers and their snapshot evidence.")


if __name__ == "__main__":
    main()
