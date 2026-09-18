# Hub floor uniqueness — proofs (agenda #48)

Claims fixed in `hypotheses.md`. Builds on #47/#49 and Q45 / #30 /
#116. Exact IIT-4.0 Φ; in-silico.

---

## U0 — floor universality (confirmed)

**Theorem (n=3 strict mediation).** Every triadic form in the
256-form strict-mediation family has exactly $2(n-1)=4$ edges.

*Proof.* Exhaustion of `enumerate_family()` (Probe #30; Q45 H1).
Reproduced in `verify_uniqueness.py`. No analytic derivation beyond
the bidirectional joint-determination wiring that defines the family:
each triadic form uses S←W, S←C, W←S, C←S and no more.

---

## U1 — AND not unique in mediation (refuted uniqueness)

**Refutation.** At n=3, 16 triadic forms achieve Φ = 2 at 4 edges; only
2 have S-index AND (Q45 H2). Counterexamples include OR, NOR, NAND,
and implication variants. Reproduced count in the smoke.

---

## Lemma I — De Morgan / bit-flip orbit

**Theorem.** Let $H_{\mathrm{AND}}(n)$ be the conjunctive hub. Define
\[
\begin{align*}
H_{\mathrm{OR}}(n):&\quad S'=\bigvee_i X_i,\ X_i'=S,\\
H_{\mathrm{NAND}}(n):&\quad S'=\neg\bigwedge_i X_i,\ X_i'=S,\\
H_{\mathrm{NOR}}(n):&\quad S'=\neg\bigvee_i X_i,\ X_i'=S.
\end{align*}
\]
Each has the same connectivity matrix as $H_{\mathrm{AND}}$ (every party
feeds S and reads S), hence $2(n-1)$ edges whenever every party is
pivotal to $S'$.

Bit-flip isomorphisms of the state space map these four TPMs onto each
other (De Morgan: $\vee=\neg\wedge\neg$, and output flip on $S$).
IIT-4.0 Φ is invariant under state relabeling of this kind (Probe #14:
0 verdict flips / Φ-range 0 on the isomorphism battery). Therefore
\[
\Phi(H_{\mathrm{AND}})=\Phi(H_{\mathrm{OR}})=\Phi(H_{\mathrm{NAND}})=\Phi(H_{\mathrm{NOR}}).
\]
Combined with #47/#49 ($\Phi(H_{\mathrm{AND}})=n-1$), all four achieve
Φ★ = n−1 at the edge floor.

*Status:* invariance cited from #14; equality of edge counts by CM
identity; Φ★ transferred from #47. Direct exact-Φ verification for
all four through n=6 in the smoke.

---

## U2 — dual orbit at the floor (proved on checked range)

**Theorem (verified $n\le 6$).** Each of AND / OR / NAND / NOR hubs
has major-complex Φ = n−1, full core, and exactly $2(n-1)$ edges.

*Proof.* Lemma I + direct computation (`verify_uniqueness.py`).

---

## U3 — hub-topology class equals the orbit (proved $n\le 4$)

**Theorem.** Fix hub topology: $S'=f(X_1,\ldots,X_{n-1})$, $X_i'=S$.
Among all $2^{2^{n-1}}$ Boolean commits $f$:

- at $n=3$: exactly 4 of 16 achieve Φ = 2 with full core —
  {AND, OR, NAND, NOR};
- at $n=4$: exactly 4 of 256 achieve Φ = 3 with full core —
  the same four.

*Proof.* Exhaustion of the commit table (smoke). No other $f$ hits
Φ★.

**Conjecture (all $n$).** On hub topology, the Φ = n−1 achievers are
exactly the De Morgan orbit of AND-all. Supporting reason: #47’s GID
evaluation at the all-1s (AND) / all-0s (OR) / flipped peaks requires
the commit to be a pure conjunction or disjunction (or their
negations) so that selectivity = 1 and $p_{\mathrm{part}}=2^{1-n}$
under $H$; other $f$ either drop selectivity, raise $p_{\mathrm{part}}$,
or shrink the major complex. Named gap: no general classification of
all $2^{2^{n-1}}$ commits for $n\ge 5$ (enumeration infeasible).

---

## U4 — uniqueness verdict

**Not unique.** The conjunctive hub is one of four hub-topology
commits achieving Φ★ at the 2(n−1) floor (U2–U3), and one of many
strict-mediation forms achieving Φ = 2 at the n=3 floor (U1). What
*is* unique is the **De Morgan orbit as a class** on the hub wiring
(through n=4 by exhaustion; conjectured for all n), and the
**monotone-versus-parity split** of ceilings at the floor (Q45).

---

## Best next

**#50** — lattice of coordination kinds (verdict + Φ magnitude as a
partial order; extremes).
