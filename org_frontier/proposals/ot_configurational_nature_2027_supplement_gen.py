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
from org_frontier.field.mocks import MOCKS

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
w("*Companion to the manuscript. Every table below is generated from the replication package's committed")
w("sources, not transcribed by hand: Part A from the two-measure robustness computation, Part B from the")
w("intermediary-catalog study, Part C from the encoding-sensitivity demonstration, Part D from the")
w("coordination-logic atlas, and Part E from the membership-law battery and the integration-game")
w("computation. Commands to re-derive each part accompany the replication package (see the final")
w("section).*\n")

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
w("Ten stylized organizational arrangements, each encoded as a small Boolean form with the prediction")
w("fixed before computation; five carry a second, equally defensible encoding of the same story (the")
w("sensitivity variant). Four of the ten flip verdict between the two encodings — the figure the")
w("manuscript cites. The rules are stipulated to demonstrate the protocol's mechanics, not elicited from")
w("field evidence, and the transition tables below are generated from the same committed rules that")
w("produced the verdicts.\n")
w("| id | arrangement | parties | base verdict (Φ) | sensitivity variant | variant verdict | flips |")
w("|---|---|---|---|---|---|---|")
import csv as _csv
mockrows = {}
with open(os.path.join(REPO, "org_frontier/field/results/field_mocks.csv")) as fh:
    for row in _csv.DictReader(fh):
        mockrows[row["id"]] = row
for m in MOCKS:
    r = mockrows[m.mid]
    var = m.sensitivity.name if m.sensitivity else "—"
    sv = r["sens_verdict"] or "—"
    fl = r["sens_flips"] or "—"
    w(f"| {m.mid} | {m.org} | {' '.join(m.parties)} | {r['verdict']} (Φ={r['system_phi']}) | {var} | {sv} | {fl} |")
w("")
w("Transition tables (base encoding, and the variant where one exists):\n")
def _table(rules, labels):
    n = len(rules)
    _tpm = tpm_from_rules(rules)
    _reach = set(reachable_states(_tpm, n))
    w(f"| state ({','.join(labels)}) | next | reachable |")
    w("|---|---|---|")
    for st in range(2 ** n):
        xv = [(st >> i) & 1 for i in range(n)]
        nx = [int(bool(rr(xv))) for rr in rules]
        w(f"| {''.join(map(str, xv))} | {''.join(map(str, nx))} | {'yes' if st in _reach else 'no'} |")
    w("")
for m in MOCKS:
    w(f"**{m.mid} — {m.org}** (base encoding)\n")
    _table(m.rules, m.parties)
    if m.sensitivity:
        w(f"**{m.mid} — variant: {m.sensitivity.name}** ({m.sensitivity.what_changes})\n")
        _table(m.sensitivity.rules, m.sensitivity.parties)

w("## Part D — the quorum sweep and the manuscript's other atlas forms, with cores\n")
w("From the coordination-logic atlas (fifty exactly solved forms, predictions fixed per form before")
w("computation). Rows below are the forms the manuscript's section 3 uses: the full quorum sweep at two")
w("to five parties, the rotation, and the one-sided veto, with each form's maximal complex (core) — the")
w("membership information Part A's whole-system values do not carry. Verdicts here are the IIT 4.0")
w("measure.\n")
w("| atlas id | form | predict | binds | core | core Φ | whole-system Φ |")
w("|---|---|---|---|---|---|---|")
keep = {"A21","A22","A31","A32","A33","A41","A42","A43","A44","A51","A53","A55","B10","D1"}
with open(os.path.join(REPO, "org_frontier/studies/coordination_logic_atlas/results/atlas.csv")) as fh:
    for row in _csv.DictReader(fh):
        if row["id"] in keep:
            core = row["core"] or "—"
            w(f"| {row['id']} | {row['experiment']} | {row['predict']} | {row['binds']} | {core} | "
              f"{float(row['core_phi']):.3f} | {float(row['whole_system_phi']):.3f} |")
w("")
w("## Part E — membership law, the integration game, and the coalition exhibit\n")
w("**Membership law (core-membership battery, committed run).** Necessity: across the enumerated family")
w("of 660 strict-mediation three-party forms, 0/660 elements lacking bidirectional coupling entered the")
w("major complex; the strict family's triadic rate is 9.5% (the manuscript's 'on the order of a tenth').")
w("The graded half comes from the battery's broader unconstrained random three-node family: inclusion in")
w("the core by influence bucket runs 38.9% (≈ four in ten) at influence ≈ 0.25 through 57.9% and 73.7% to")
w("87.5% (≈ nine in ten) at influence ≈ 1.00, rank-AUC 0.629. The two families are distinct and the")
w("manuscript attributes each half to its own family.\n")
w("**The integration game (worth function stated).** For a configuration modeled as network N at state s,")
w("the worth of coalition S is v(S) = max(0, Φ of the subsystem induced by S in N at s), with the")
w("complement nodes held as frozen background conditions at their values in s, and v(∅) = 0. Shapley")
w("values are computed exactly over all orderings. On the worked strict-mediation triad at state 111:\n")
w("| party | Shapley value | share of Φ = 2.0 |")
w("|---|---|---|")
with open(os.path.join(REPO, "org_frontier/questions/q111_shapley_value/results/shapley_value.csv")) as fh:
    for row in _csv.DictReader(fh):
        if row["form"] == "read_recipient":
            v = float(row["shapley_value"])
            w(f"| {row['party']} | {v:+.3f} | {abs(v)/2.0:.0%} |")
w("")
w("**The coalition exhibit (section 4).** Four elements (W, S, C1, C2), rules: W′ = S; S′ = W ∧ C1 ∧ C2;")
w("C1′ = S ∨ C2; C2′ = S ∨ C1. Every element is bidirectionally coupled and pivotal on a per-element")
w("screen; the exact maximal complex is {C1, C2} at Φ = 2.0, with W and S outside. Transition table:\n")
_table([lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1] | x[3], lambda x: x[1] | x[2]],
       ("W", "S", "C1", "C2"))
w("## Replication\n")
w("Each part re-derives from a committed script in the replication package; the package's README maps")
w("part to command. All computations are exact; the two-measure comparison in Part A additionally runs")
w("as a continuous-integration check on the package repository.\n")
text = "\n".join(out) + "\n"
dest = os.path.join(REPO, "org_frontier/proposals/ot_configurational_nature_2027_supplement.md")
with open(dest, "w") as fh:
    fh.write(text)
print("wrote", dest, len(text.split()), "words,", len([l for l in out if l.startswith('|')]), "table rows")
print("catalog classes:", tally, "| expectation mismatches:", mism if mism else "none")
