---
citekey: bertschinger2014quantifying
title: Quantifying Unique Information
authors: Bertschinger, Nils and Rauh, Johannes and Olbrich, Eckehard and Jost, Jürgen and Ay, Nihat
year: 2014
doi: 10.3390/e16042161
arxiv: null
journal: Entropy
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1311.2852
sha256: d9d90da2a964039588b1eed45458b02b197e6d5605964b14e0eb048ce557e0ac
pdf_path: literature/pdfs/bertschinger2014quantifying.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses the open problem of decomposing the mutual information MI(X:(Y,Z)) that a pair of variables (Y,Z) carries about a target X into four non-negative terms: shared information SI, two unique-information terms UI(X:Y\Z) and UI(X:Z\Y), and synergistic (complementary) information CI. Motivated by an operational, decision-theoretic interpretation, the authors argue that unique and shared information should depend only on the pair marginals of (X,Y) and (X,Z) — an invariance property they call (∗). They define new measures by optimizing over the polytope ΔP of all joint distributions sharing those two pair marginals: UĨ(X:Y\Z) = min over Q∈ΔP of MI_Q(X:Y|Z), with SĨ and CĨ derived correspondingly. They prove these four functions are non-negative, that the defining optimization problems are equivalent convex problems with a unique solution, and that the measures bound any other decomposition satisfying (∗). The construction is shown to be consistent with the operational idea via Blackwell's theorem, to satisfy the bivariate PI axioms and the identity axiom, and to agree with the prior redundancy measure I_red of Harder/Salge/Polani in many paradigmatic examples, while differing in a dice example. The authors note that, as shown elsewhere, SĨ cannot be extended to three input variables within the PI-lattice framework because the identity axiom is incompatible with a non-negative PI-lattice decomposition for n=3.

## Key facts it relies on
- The decomposition uses four terms satisfying MI(X:(Y,Z)) = SI + UI(X:Y\Z) + UI(X:Z\Y) + CI, plus the consistency identities MI(X:Y) = SI + UI(X:Y\Z) and MI(X:Z) = SI + UI(X:Z\Y) (a "binary information decomposition").
- The co-information CoI(X;Y;Z) = MI(X:Y) − MI(X:Y|Z) equals SI − CI (Eq. 3); positive co-information signals redundancy, negative signals synergy (cited from interaction information, ref [8]).
- Core definition: UĨ(X:Y\Z) = min_{Q∈ΔP} MI_Q(X:Y|Z), SĨ(X:Y;Z) = max_{Q∈ΔP} CoI_Q(X;Y;Z), CĨ(X:Y;Z) = MI(X:(Y,Z)) − min_{Q∈ΔP} MI_Q(X:(Y,Z)), where ΔP fixes the (X,Y) and (X,Z) pair marginals.
- Lemma 4: the five optimization problems (minimizing MI_Q(X:Y|Z), MI_Q(X:Z|Y), MI_Q(X:(Y,Z)); maximizing CoI_Q and H_Q(X|Y,Z)) are equivalent; MI quantities are convex on ΔP and CoI/conditional entropy concave, so the optimum set is convex and the solution unique.
- Lemma 5: all four functions UĨ, SĨ, CĨ are non-negative; Lemma 3: they bound any other non-negative continuous decomposition satisfying (∗).
- Operational interpretation via decision problems (p, A, u): Y has unique information about X iff there is a reward function with R(κ,p,u) > R(µ,p,u); Corollary 7 shows UĨ(X:Z\Y)=0 iff Z has no unique information, proved via Blackwell's theorem (ref [3], also [1]).
- Proposition 18 (identity property): for X=(Y,Z), ΔP={P} and SĨ((Y,Z):Y;Z) = MI(Y:Z), CĨ=0, UĨ((Y,Z):Y\Z)=H(Y|Z) — matching the identity axiom of ref [5].
- Worked examples (Table 1) give SĨ values: Rdn (SĨ=1, CĨ=0), Unq (SĨ=0, CĨ=1), Xor (SĨ=0, CĨ=1), And (SĨ=0.311, CĨ=1/2, matching I_min=0.311); SĨ agrees with I_red in all these examples.
- Comparison: both I_red [5] and I_min [10] satisfy (∗), so I_red ≥ SĨ and I_min ≥ SĨ; Theorem 20 shows I_red=0 iff SĨ=0; Lemma 26 gives dim(ker A) = |X|(|Y|−1)(|Z|−1) for the marginal polytope ΔP.
- Lemma 25: unique information is monotone — UĨ(X:Y\(Z1,...,Zk)) ≥ UĨ(X:Y\(Z1,...,Zk+1)) — so it cannot grow as more conditioning variables are added.

## Critical notes from the literature
- The authors state the invariance property (∗) does not uniquely determine the measures; it only implies their functions are bounds (SĨ a lower bound, CĨ a lower bound, UĨ an upper bound) for any decomposition satisfying (∗). The stronger uniqueness comes only under the additional postulate (∗∗) that synergy cannot be detected from the two pair marginals alone.
- The operational criterion (Definition 1) distinguishes when unique information vanishes but, as the paper explicitly notes, "does not allow to quantify the unique information" — quantification requires the extra modeling assumption (∗).
- Scope is fundamentally bivariate: the paper shows (citing ref [2]) that SĨ cannot be generalized to three input variables within the Williams–Beer PI-lattice, because the identity axiom is incompatible with a non-negative PI-lattice decomposition for n=3.
- The measures agree with the earlier redundancy measure I_red [5] in many cases but are genuinely different functions; in the dice example (X=Y+αZ, correlation λ) SĨ ≤ I_red with SĨ depending only weakly on α for small λ, and the authors admit they "do not have an argument" for which behaviour is more intuitive.
- Computing the measures requires solving a convex optimization over the polytope ΔP; the authors caution (Example 31, appendix) that this is harder in practice than in theory.

## Key topics covered
Partial information decomposition; shared / unique / synergistic (complementary) information; mutual information and co-information (interaction information); operational decision-theoretic interpretation; Blackwell's theorem and channel garbling; invariance to pair marginals (assumption ∗); convex optimization over the marginal polytope ΔP; bivariate PI axioms (Williams–Beer) and the identity axiom; comparison with I_min and I_red; non-extendability to n=3; XOR/AND/copy example systems; dice example.
