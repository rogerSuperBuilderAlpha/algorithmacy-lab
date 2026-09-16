# Scaling laws from the MIP — proofs

Agenda #47. Claims fixed in `hypotheses.md`. Exact IIT-4.0 Φ_MIP on
the lab PyPhi pin (`GENERALIZED_INTRINSIC_DIFFERENCE`,
`SYSTEM_PARTITION_TYPE = SET_UNI/BI`). In-silico Boolean forms only.

Notation: $n$ = system size; $\varphi_s = \min(\varphi_c,\varphi_e)$ on
the MIP; lab $\Phi$ = major-complex $\varphi_s$ (max over reachable
states). GID:
\[
\varphi = \mathrm{sel}\cdot\log_2\!\Bigl(\frac{p_{\mathrm{fwd}}}{p_{\mathrm{part}}}\Bigr).
\]
When $\mathrm{sel}=1$ and $p_{\mathrm{fwd}}=1$,
$\varphi = -\log_2 p_{\mathrm{part}}$.

The MIP is the `SET_UNI/BI` partition minimizing
$(\varphi_{\mathrm{norm}},-\varphi)$ with
$\varphi_{\mathrm{norm}}=\varphi/(|\mathrm{from}|\cdot|\mathrm{to}|)$.

---

## Lemma A — all-1s preimage and selectivity (AND forms)

**Theorem (pool and conjunctive hub).** At present state $\mathbf{1}$,
the TPM-preimage is unique ($\mathbf{1}$ itself). Hence the cause
repertoire is a point mass and $\mathrm{sel}_c = 1$. The effect map
sends $\mathbf{1}\mapsto\mathbf{1}$ deterministically, so
$p_{\mathrm{fwd}}=1$ and (with the unconstrained effect repertoire
also peaked) $\mathrm{sel}_e=1$.

*Proof (pool).* $X_i'=\bigwedge_{j\neq i}X_j$. If every present bit is
1, then for each $i$ the AND of the others was 1, so every past bit is
1. Uniqueness follows. Forward: AND of all-1s is 1 for every node.

*Proof (hub).* $S'=\bigwedge_{i\ge 1}X_i$, $X_i'=S$. Present all-1s
forces $S_{\mathrm{past}}=1$ (parties copy $S$) and all parties past
$=1$ (AND). Forward: $S'=1$ and parties copy it.

---

## Lemma B — parity cause selectivity

**Theorem (parity hub).** At present $\mathbf{1}$, every past with
$S=1$ and odd party-parity maps to $\mathbf{1}$. There are
$2^{n-2}$ such pasts. Under a uniform past prior the cause repertoire
is uniform on that preimage, so
\[
\mathrm{sel}_c = 2^{2-n}.
\]

*Proof.* $X_i'=S$ forces $S_{\mathrm{past}}=1$ when all present parties
are 1. $S'=\bigoplus_{i\ge 1}X_i$ forces odd parity among the $n-1$
parties. Half of the $2^{n-1}$ party strings are odd ⇒ $2^{n-2}$
preimages. Each carries mass $2^{2-n}$.

---

## Lemma C — partitioned forward under the hub-preserving atomic cut

Write $H$ for the hub-preserving atomic `SET_UNI/BI` cut: every
directed edge except hub→party is severed (matrix row 0 is zero; all
other off-diagonal entries are 1). Cut inputs are replaced by
independent fair bits.

**Theorem (conjunctive hub on $H$).** At $\mathbf{1}$,
$p_{\mathrm{part}}=2^{1-n}$, hence
\[
\varphi_c=\varphi_e=-\log_2(2^{1-n})=n-1,\qquad\varphi_s=n-1.
\]

*Proof.* Preserved hub→party edges give $X_i'=S=1$ with probability 1.
Severed party→hub edges replace the AND inputs by $\eta_i\sim\mathrm{Bern}(1/2)$
i.i.d., so $P(S'=1)=2^{1-n}$. Joint next $=\mathbf{1}$ has that
probability. Lemma A gives $\mathrm{sel}=1$, $p_{\mathrm{fwd}}=1$.

**Theorem (parity hub on $H$).** At $\mathbf{1}$,
$p_{\mathrm{part}}=1/2$ on the specified effect (and on the cause
forward evaluation used by GID), so informativeness $=1$ and
\[
\varphi_c=\mathrm{sel}_c\cdot 1=2^{2-n},\qquad\varphi_e=1,\qquad\varphi_s=2^{2-n}.
\]

*Proof.* Parties still copy $S$. Severed party→hub inputs make
$S'=\bigoplus\eta_i$, which is fair Bernoulli($1/2$) for $n\ge 3$.
Informativeness $\log_2(1/(1/2))=1$. Cause selectivity is Lemma B;
effect selectivity is 1 on the checked range (deterministic party
copies plus fair $S'$ still leave effect $\varphi_e=1>\varphi_c$).

---

## Lemma D — partitioned forward under the complete atomic cut (pool)

**Theorem (pool on the complete atomic cut $A$).** All off-diagonal
edges severed. At $\mathbf{1}$,
\[
p_{\mathrm{part}}=\bigl(2^{1-n}\bigr)^n=2^{-n(n-1)},
\qquad\varphi_s=-\log_2 p_{\mathrm{part}}=n(n-1).
\]

*Proof.* Each node’s AND inputs are $n-1$ independent fair bits, so
$P(X_i'=1)=2^{1-n}$. Independence across nodes under the full cut gives
the product. Lemma A supplies $\mathrm{sel}=1$, $p_{\mathrm{fwd}}=1$.

---

## From cut-$\varphi$ to MIP-$\varphi$

GID on a named cut is not yet the MIP. The MIP is the
`SET_UNI/BI` minimizer of $(\varphi_{\mathrm{norm}},-\varphi)$.

### Pool — claim C2

**Theorem (φ on $A$).** Lemma D.

**Partial (MIP = $A$).** On $n\in\{3,4,5\}$ the complete atomic cut
achieves the minimal observed $\varphi_{\mathrm{norm}}=1$, and among
all partitions with that normalized value it uniquely maximizes raw
$\varphi$ at $n(n-1)$ (verification table). Structural reason: each
severed AND-input contributes one bit to $-\log_2 p_{\mathrm{part}}$,
and for efficient cuts $\varphi=|\mathrm{from}|\cdot|\mathrm{to}|$,
hence $\varphi_{\mathrm{norm}}=1$; the complete cut severs $n(n-1)$
such inputs and wins the max-$\varphi$ tiebreak.

**Gap (named).** A general-$n$ proof that no `SET_UNI/BI` partition
has $\varphi_{\mathrm{norm}}<1$, and that no other $\varphi_{\mathrm{norm}}=1$
cut exceeds $n(n-1)$ raw φ. Status: **partial** (cut formula proved;
MIP identity verified $n\le 5$, conjectured for all $n\ge 3$).

### Conjunctive hub — claim C1

**Theorem (φ on $H$).** Lemma C (hub).

**Partial (MIP).** For $n\ge 4$ on the checked range the MIP is $H$
(or its party-preserving dual), with $\varphi=n-1$ and
$\varphi_{\mathrm{norm}}=1/(n-1)$. For $n=3$ the MIP is a
party-vs-rest bipartition with the same raw $\varphi=2=n-1$ (tied with
$H$ on $(\varphi_{\mathrm{norm}},-\varphi)$ up to the max-φ rule).

**Gap (named).** General-$n$ uniqueness of $H$ (or an equal-φ
bipartition family) as MIP. The cut evaluation $\varphi=n-1$ is
proved; identifying the MIP for all $n$ is **partial**.

### Parity hub — claim C3

**Theorem (φ on $H$).** Lemmas B–C (parity): $\varphi_s=2^{2-n}$.

**Partial (MIP).** On $n\in\{3,4,5\}$ the MIP is uniquely $H$ (strictly
lowest $\varphi_{\mathrm{norm}}$).

**Gap (named).** General-$n$ MIP uniqueness for $H$. Cut formula and
selectivity are proved; MIP identity **partial** (verified small $n$).

---

## Major-complex / state scope

**Theorem (checked range).** For each form at $n\in\{3,4,5\}$ (hub
also $n=6$ in the smoke), `major_complex` returns the full node set
and $\Phi$ equal to $\varphi_s(\mathbf{1})$ under the MIP above.

**Conjecture.** All-1s remains a $\Phi$-maximizer and the whole system
remains the major complex for every $n\ge 3$ on these three forms.
(Probe #116 already saw hub through $n=7$ numerically.)

---

## Status summary

| claim | cut formula | MIP identity | overall |
|---|---|---|---|
| C1 hub $\Phi=n-1$ | **proved** (Lemma C) | partial ($n\le 5$ + #116) | **partial** |
| C2 pool $\Phi=n(n-1)$ | **proved** (Lemma D) | partial ($n\le 5$) | **partial** |
| C3 parity $\Phi=2^{2-n}$ | **proved** (Lemmas B–C) | partial ($n\le 5$) | **partial** |

Nothing is blocked: the remaining work is a general MIP-identification
lemma for `SET_UNI/BI` on these CM families (#49’s min-cut framing is
the natural next tool).

---

## Best next among #48–#50

**#49 (min-cut MIP)** is the best next. The named gap on all three
laws is MIP identity, not the GID evaluation on the candidate cut.
A min-cut theorem placing the MIP at the least-coupled seam (#26,
#33) would close C1–C3 for general $n$. #48 (hub uniqueness at the
$2(n-1)$ edge floor) and #50 (lattice of kinds) need the closed forms
as inputs; they are next after the MIP lemma.
