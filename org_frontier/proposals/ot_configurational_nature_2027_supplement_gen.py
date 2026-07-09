"""Generate the OT-manuscript online supplement from lab sources (no hand-transcription)."""
import csv
import os
import sys

REPO = "/Users/ludwitt/iit-playground/pyphi-experiments"
sys.path.insert(0, REPO)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q215_phi_family_robustness.probe_phi_family_robustness import FORMS
from org_frontier.classifier.classifier import tpm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.studies.irreducibility_catalog.catalog_entries import ENTRIES

RULE_STRINGS = {
    "CTRL+": "E′ = M;  M′ = E ∧ R;  R′ = M",
    "CTRL-": "A′ = B;  B′ = A;  C′ = D;  D′ = C",
    "E1": "P0′ = P1′ = P2′ = S;  S′ = [P0+P1+P2 ≥ 1]",
    "E2": "P0′ = P1′ = P2′ = S;  S′ = [P0+P1+P2 ≥ 2]",
    "E3": "P0′ = P1′ = P2′ = S;  S′ = [P0+P1+P2 ≥ 3]",
    "E4": "A′ = D;  B′ = A;  C′ = B;  D′ = C",
    "E5": "W′ = S;  S′ = W ∧ ¬C;  C′ = S",
    "E6": "W′ = ¬S;  S′ = W ∧ C;  C′ = C ∧ ¬S",
    "E7": "W′ = ¬S;  S′ = W;  C′ = C ∧ ¬S",
    "E8": "W′ = ¬(S ∨ C);  S′ = ¬W ∧ C;  C′ = ¬(W ∧ S)",
}

# per-state Φ from the Q215 run
phi = {}  # (form_id, state_str) -> (phi40, phi30)
with open(os.path.join(REPO, "org_frontier/questions/q215_phi_family_robustness/results/phi_family.csv")) as fh:
    for row in csv.DictReader(fh):
        phi[(row["form"], row["state"])] = (float(row["phi_iit40"]), float(row["phi_iit30"]))

# catalog class/margin from the study's committed output
klass = {}  # name -> (class, margin)
with open(os.path.join(REPO, "org_frontier/studies/irreducibility_catalog/results/output.txt")) as fh:
    for line in fh:
        t = line.split()
        if len(t) >= 3 and any(e["name"] == t[0] for e in ENTRIES):
            klass[t[0]] = (t[-2], t[-1])

out = []
w = out.append
w("# Online supplement — When is a combination a configuration?\n")
w("*Companion to `ot_configurational_nature_2027_manuscript.md`. Every table below is generated from the")
w("lab's committed sources (question q215 and the irreducibility-catalog study), not transcribed by hand.")
w("Reproduction: the q215 probe re-derives every Φ value in Part A (`python -m")
w("org_frontier.questions.q215_phi_family_robustness.probe_phi_family_robustness`; registered as CI check")
w("`q215-phi-family-robustness`); the catalog study re-derives Part B (`python -m")
w("org_frontier.studies.irreducibility_catalog.build_catalog`).*\n")

w("## Part A — the manuscript's model forms: rules, transitions, and Φ under two measures\n")
w("Rules are synchronous Boolean updates; a state lists node values in label order. Φ is whole-system")
w("integrated information at that state: IIT 4.0 (`pyphi.new_big_phi`) and IIT 3.0 (`pyphi.compute`,")
w("`DIRECTED_BI` partitions). Only reachable states carry Φ values; verdicts in the manuscript are the")
w("sign of the maximum over reachable states.\n")

for fid, name, rules, labels in FORMS:
    n = len(rules)
    tpm = tpm_from_rules(rules)
    reach = set(reachable_states(tpm, n))
    w(f"### {fid} — {name}\n")
    w(f"Rules: {RULE_STRINGS[fid]}\n")
    w(f"| state ({','.join(labels)}) | next state | reachable | Φ (IIT 4.0) | Φ (IIT 3.0) |")
    w("|---|---|---|---|---|")
    for s in range(2 ** n):
        x = [(s >> i) & 1 for i in range(n)]
        nxt = [int(bool(r(x))) for r in rules]
        st = "".join(map(str, x))
        key = (fid, st)
        if s in reach and key in phi:
            p40, p30 = phi[key]
            w(f"| {st} | {''.join(map(str, nxt))} | yes | {p40:.4f} | {p30:.4f} |")
        else:
            w(f"| {st} | {''.join(map(str, nxt))} | {'yes' if s in reach else 'no'} | — | — |")
    w("")

w("## Part B — the intermediary catalog: entries, coding, and classification\n")
w("Each entry is a real or stylized coordination arrangement with a mediating third, coded to one of four")
w("structural templates and classified by the bypass-counterfactual (restore the forbidden direct tie,")
w("recompute, read whether the mediator stays in the core). The `expected` column records the coding;")
w("`class` and `margin` (whole-system Φ lost when the bypass opens) are the computed result. Because the")
w("computed class follows the structural template by construction — margin is constant within a template —")
w("agreement between coding and classification checks the pipeline's consistency, not a prediction. The")
w("catalog's contribution is the coding itself: which real constraint holds which arrangement in which")
w("template. Coding rule for `expected`: an entry is coded *contingent* when an")
w("identifiable external constraint (statute, license, exclusive contract, standard, friction) is the only")
w("stated reason the parties cannot transact directly; *necessary* when the mediator computes a joint")
w("condition the direct tie cannot reproduce; *partial* when a direct channel already runs alongside the")
w("mediated one; *reducible* when the direct tie is already open and unconstrained. As the manuscript")
w("notes, outcomes were known to the coders; the exercise disciplines the distinction rather than tests")
w("it.\n")
keys_present = sorted({k for e in ENTRIES for k in e.keys()})
w(f"Fields coded per entry: `{'`, `'.join(keys_present)}`.\n")
w("| # | entry | domain | template | constraint type | expected | class | margin |")
w("|---|---|---|---|---|---|---|---|")
# the classifier's vocabulary calls the necessary class "intrinsic"; normalize for display/compare
NORM = {"intrinsic": "necessary"}
for i, e in enumerate(ENTRIES, 1):
    cls, mar = klass.get(e["name"], ("?", "?"))
    exp = NORM.get(e.get("expected", ""), e.get("expected", ""))
    w(f"| {i} | {e['name']} | {e.get('domain','')} | {e.get('template', e.get('form',''))} | "
      f"{e.get('constraint_type','')} | {exp} | {cls} | {mar} |")
tally = {}
for e in ENTRIES:
    c = klass.get(e["name"], ("?",))[0]
    tally[c] = tally.get(c, 0) + 1
w("")
w(f"Class tally: {', '.join(f'{k}={v}' for k, v in sorted(tally.items()))} (n = {len(ENTRIES)}).")
mism = [e['name'] for e in ENTRIES if e.get('expected')
        and klass.get(e['name'], ('?',))[0] != NORM.get(e['expected'], e['expected'])]
w(f"Entries whose computed class differs from the coded expectation: "
  f"{', '.join(mism) if mism else 'none'} (a pipeline-consistency check; see the note above on why "
  f"agreement is expected by construction).\n")

w("## Part C — the ten-case encoding-sensitivity demonstration\n")
w("The four-of-ten verdict-flip figure cited in sections 2 and 7 comes from the lab's encoding-sensitivity")
w("demonstration on ten stylized organizational cases, each modeled twice under defensible alternative")
w("rule encodings; the demonstration and per-case rules are maintained with the field-reading program's")
w("records and will be included in the submission package.\n")

text = "\n".join(out) + "\n"
dest = os.path.join(REPO, "org_frontier/proposals/ot_configurational_nature_2027_supplement.md")
with open(dest, "w") as fh:
    fh.write(text)
print("wrote", dest, len(text.split()), "words,", len([l for l in out if l.startswith('|')]), "table rows")
print("catalog classes:", tally, "| expectation mismatches:", mism if mism else "none")
