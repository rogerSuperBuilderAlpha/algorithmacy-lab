"""Paper 2 rebuild — worked applications (from scratch), cross-checked against ../results.md.

Cases:
  A. Dyadic limit — chat with a language model (the structure the dyadic constructs assume).
  B. Irreducible triad — résumé -> ATS -> hiring manager (sweep the committed determination).
  C. The false dyad — rideshare: presents as worker+app, is causally a triad (one edge S<-C).
  D. The false triad — a party-ignoring mediator: 3 visible parties, structure still factors.

Run: ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/rebuild/worked_examples.py
"""

import os, sys
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
sys.path.insert(0, os.path.dirname(__file__))

from instrument import classify, report


def case_A_dyadic_limit():
    print("\nA. DYADIC LIMIT — chat with a language model (the dyadic constructs' structure)")
    # Worker and model exchange; the model commits nothing that couples a third party.
    rules = [
        lambda s: s[1],   # W' = S   (worker reads the model)
        lambda s: s[0],   # S' = W   (model reads the worker)
        lambda s: s[2],   # C' = C   (no third party coupled)
    ]
    report(classify(rules, "chat dyad"))
    print("   expect: Φ=0 everywhere -> MODERATED DYAD  (../results.md §2.A)")


def case_B_ats_triad():
    print("\nB. IRREDUCIBLE TRIAD — résumé -> ATS -> hiring manager (sweep S'=f(W,C))")
    # Applicant reads the ATS determination (W'=S); manager reads it (C'=S);
    # the ATS commits a determination f(applicant, manager).
    fns = {
        "AND":  lambda w, c: w and c,
        "OR":   lambda w, c: w or c,
        "NAND": lambda w, c: not (w and c),
        "NOR":  lambda w, c: not (w or c),
        "XOR":  lambda w, c: bool(w ^ c),
        "XNOR": lambda w, c: not (w ^ c),
        "f=W (ignores manager)":   lambda w, c: w,
        "f=C (ignores applicant)": lambda w, c: c,
    }
    for label, f in fns.items():
        rules = [
            lambda s: s[1],                 # W' = S
            (lambda f: lambda s: f(s[0], s[2]))(f),  # S' = f(W, C)
            lambda s: s[1],                 # C' = S
        ]
        report(classify(rules, f"ATS S'={label}"))
    print("   expect: AND/OR/NAND/NOR -> maxΦ=2.0, MIP {W,SC}; XOR/XNOR -> Φ=0.5 tripartition;")
    print("           f=W, f=C -> Φ=0 (false triad)  (../results.md §2.B)")


def case_C_false_dyad():
    print("\nC. THE FALSE DYAD — rideshare (presents as worker+app; the edge S<-C decides)")
    # Common to both models: W' = ¬S (availability consumed by a dispatch);
    #                        C' = C ∧ ¬S (rider keeps waiting until served).
    triad = [
        lambda s: not s[1],            # W' = ¬S
        lambda s: s[0] and s[2],       # S' = W ∧ C   (dispatch reads BOTH sides)
        lambda s: s[2] and not s[1],   # C' = C ∧ ¬S
    ]
    dyad = [
        lambda s: not s[1],            # W' = ¬S
        lambda s: s[0],                # S' = W       (dispatch reads the driver only)
        lambda s: s[2] and not s[1],   # C' = C ∧ ¬S
    ]
    report(classify(triad, "full triad (S'=W∧C)"))
    report(classify(dyad,  "dyadic model (S'=W)"))
    print("   expect: full triad -> Φ=2.0 @ (1,1,1), MIP {W,SC}; dyadic model -> Φ=0")
    print("           the two differ by ONE edge (S<-C); that edge carries the verdict (../results.md §2.C)")


if __name__ == "__main__":
    case_A_dyadic_limit()
    case_B_ats_triad()
    case_C_false_dyad()
