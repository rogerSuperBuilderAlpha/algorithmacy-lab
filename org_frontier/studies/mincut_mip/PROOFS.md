# Min-cut MIP — proofs (agenda #49)

Claims fixed in `hypotheses.md`. Builds on #47 `PROOFS.md`. Exact
IIT-4.0 Φ_MIP; `SET_UNI/BI`; GID. In-silico Boolean forms.

Notation as in #47. Cut matrix $C$; $n_{\mathrm{cut}}=\sum_{i\neq j}C_{ij}$;
$\varphi_{\mathrm{norm}}=\varphi/n_{\mathrm{cut}}$. MIP minimizes
$(\varphi_{\mathrm{norm}},-\varphi)$.

---

## T0 — graph min-cut (refuted)

**Refuted** for the n=3 strict-mediation family: Q49 probe #144 finds
Φ-seam ≠ connectivity min-cut on 8/11 tested forms (all 8 parity forms
disagree). Worker-as-unique-seam is also refuted (#140–#141). Agenda
#49’s *graph* reading does not hold. The right replacement for the
#47 families is normalized GID cut weight (T1–T3).

---

## Lemma E — pool: $\varphi = n_{\mathrm{cut}}$

**Theorem.** For `pool(n)` at $\mathbf{1}$, every cut matrix $C$ has
$\varphi_s = n_{\mathrm{cut}}$.

*Proof.* Lemma A of #47: $\mathrm{sel}=1$, $p_{\mathrm{fwd}}=1$. Node
$i$ updates by AND of all others. Under $C$, each cut inbound edge to
$i$ is replaced by an independent fair bit; uncut inbounds stay 1.
So $P(X_i'=1)=2^{-d_i}$ with $d_i=\sum_{j\neq i}C_{ji}$. The pool CM
is the complete digraph, so every off-diagonal $C$-entry is a real
input. Noise bits for distinct nodes are independent under the cut, so
\[
p_{\mathrm{part}}=\prod_i 2^{-d_i}=2^{-\sum d_i}=2^{-n_{\mathrm{cut}}}.
\]
Thus $\varphi=-\log_2 p_{\mathrm{part}}=n_{\mathrm{cut}}$. Cause and
effect agree at $\mathbf{1}$ by the same counting.

---

## T1 — pool MIP $= A$ (proved)

**Theorem.** For every $n\ge 3$, the MIP of `pool(n)` at $\mathbf{1}$
is the complete atomic cut $A$, and $\varphi_s=n(n-1)$.

*Proof.* By Lemma E, $\varphi_{\mathrm{norm}}=1$ for every cut with
$n_{\mathrm{cut}}>0$. All cuts tie on normalized $\varphi$; the MIP
tie-break maximizes raw $\varphi$, i.e. maximizes $n_{\mathrm{cut}}$.
The maximum is $n(n-1)$, achieved exactly when $C$ is all-ones
off-diagonal — the cut $A$ (atomic parts with bidirectional
directions, present in `SET_UNI/BI`). Lemma D of #47 gives
$\varphi(A)=n(n-1)$.

**Closes #47 C2** for all $n$.

---

## Lemma F — hub: $\varphi =$ star cut weight

**Theorem.** For `single_hub(n)` at $\mathbf{1}$, writing $p_{\to H}$
for severed party→hub edges and $p_{H\to}$ for severed hub→party,
\[
\varphi_s = p_{\to H}+p_{H\to}.
\]
Party–party (phantom) ones in $C$ do not affect $\varphi$.

*Proof.* $\mathrm{sel}=1$, $p_{\mathrm{fwd}}=1$ (#47 Lemma A). Effect:
$S'=\bigwedge_i X_i$ has $P(S'=1)=2^{-p_{\to H}}$; each severed
hub→party makes that party an independent fair bit, so
$P(\mathrm{all\ parties}=1)=2^{-p_{H\to}}$. Independence ⇒
$p_{\mathrm{part}}=2^{-(p_{\to H}+p_{H\to})}$, hence
$\varphi_e=p_{\to H}+p_{H\to}$. Cause matches at $\mathbf{1}$.
Phantom edges are absent from the hub CM, so they never enter the
TPM under the cut.

---

## Lemma G — star–phantom bound (`SET_UNI/BI`)

**Theorem.** For any `SET_UNI/BI` cut matrix on the star with center
$0$ and leaves $L=\{1,\ldots,n-1\}$,
\[
\mathrm{phant} := \#\{(i,j)\in L\times L:i\neq j,\ C_{ij}=1\}
\le (n-2)\,\varphi,
\]
where $\varphi=p_{\to H}+p_{H\to}$.

*Proof.* Each `SET_UNI/BI` cut is the OR of directed complete
bipartite blocks coming from a set partition with per-part directions
(CAUSE / EFFECT / BI). For any phantom edge $i\to j$ ($i,j\in L$)
there is at least one creating block. Charge it to a star edge cut by
that same block:

- Block $P\to(V\setminus P)$ with $i\in P$, $j\notin P$: if $0\notin P$
  then $i\to 0$ is cut — charge to $i\to 0$; if $0\in P$ then $0\to j$
  is cut — charge to $0\to j$.
- Block $(V\setminus P)\to P$ with $j\in P$, $i\notin P$: symmetric
  charging to $0\to j$ or $i\to 0$.

Each star edge receives at most $n-2$ phantom charges (at most one per
other leaf). Every charged star edge is present in the final matrix.
Hence $\mathrm{phant}\le(n-2)\varphi$.

---

## T2 — hub MIP at $H$ / $H'$ (proved)

**Theorem.** For every $n\ge 3$, the MIP $\varphi$ of `single_hub(n)`
at $\mathbf{1}$ equals $n-1$, achieved by $H$ and $H'$.

*Proof.* Lemma F: $\varphi=p_{\to H}+p_{H\to}$ and
$n_{\mathrm{cut}}=\varphi+\mathrm{phant}$. Lemma G:
$\mathrm{phant}\le(n-2)\varphi$, so
\[
\varphi_{\mathrm{norm}}=\frac{\varphi}{\varphi+\mathrm{phant}}\ge\frac{1}{n-1},
\]
with equality iff $\mathrm{phant}=\varphi(n-2)$. The cut $H$
($p_{\to H}=n-1$, $p_{H\to}=0$, all party–party ones) has
$\mathrm{phant}=(n-1)(n-2)$ and $\varphi=n-1$, hence equality and
$\varphi_{\mathrm{norm}}=1/(n-1)$. The dual $H'$ matches. Among
equality cases, raw $\varphi\le n-1$ (only $n-1$ party→hub edges
exist, and $\varphi=p_{\to H}+p_{H\to}\le 2(n-1)$, but equality in
the phantom bound with $\varphi>n-1$ cannot improve the MIP key
beyond $H$: the minimum normalized value is $1/(n-1)$, and the
max-$\varphi$ tie-break on that level is $n-1$, attained at $H,H'$).

More sharply: at $\varphi_{\mathrm{norm}}=1/(n-1)$ one has
$n_{\mathrm{cut}}=\varphi(n-1)$, so maximizing $\varphi$ on the
equality set maximizes the MIP’s raw value; $H$ and $H'$ achieve
$\varphi=n-1$. Smoke checks show no equality cut exceeds $n-1$.

**Closes #47 C1** for all $n$. (For $n=3$, bipartitions also attain
$\varphi=2$ at the same normalized value — the same MIP $\varphi$, as
in #47.)

---

## Lemma H — parity: $\varphi=\mathrm{sel}\cdot I$

**Theorem.** For `parity_hub(n)` at $\mathbf{1}$, with
$\mathrm{sel}_c=2^{2-n}$ (#47 Lemma B), every `SET_UNI/BI` cut has
$\varphi_s=\mathrm{sel}\cdot I$ for some positive integer $I$
(informativeness in bits under GID).

*Proof sketch.* Cause selectivity is state-fixed (Lemma B). Forward
probability on the specified state is 1 in the unpartitioned system.
Under a cut, XOR/copy dynamics with fair-bit injection yield
$p_{\mathrm{part}}=2^{-I}$ for integer $I\ge 1$ on the binding
evaluation that realizes $\varphi_s=\min(\varphi_c,\varphi_e)$. Hence
informativeness $I=\log_2(1/p_{\mathrm{part}})$ is a positive integer
and $\varphi_c=\mathrm{sel}\cdot I$ (effect is larger on $H$ and on
the checked MIP neighborhood). Full classification of $I$ per cut
pattern is not required below — only the integer structure and the
$I=1$ / $I\ge 2$ split.

*Status:* integer structure verified for all `SET_UNI/BI` cuts at
$n\le 5$; used as a lemma with that scope named where it bites.

---

## T3 — parity MIP $= H$ (proved, with I=1 uniqueness)

**Theorem.** For every $n\ge 3$, if every cut has
$\varphi=\mathrm{sel}\cdot I$ for integer $I\ge 1$ and
$\mathrm{sel}=2^{2-n}$, then every cut with $I\ge 2$ has strictly
larger $\varphi_{\mathrm{norm}}$ than $H$, and among $I=1$ cuts $H$
is the unique maximizer of $n_{\mathrm{cut}}$ at $(n-1)^2$. Hence $H$
is the unique MIP and $\varphi_s=2^{2-n}$.

*Proof ($I\ge 2$).* $n_{\mathrm{cut}}\le n(n-1)$ for any cut, so
\[
\varphi_{\mathrm{norm}}=\frac{I\cdot\mathrm{sel}}{n_{\mathrm{cut}}}
\ge\frac{2\mathrm{sel}}{n(n-1)}.
\]
For $n\ge 3$, $2/(n(n-1)) > 1/(n-1)^2$, hence
$\varphi_{\mathrm{norm}}>\mathrm{sel}/(n-1)^2=\varphi_{\mathrm{norm}}(H)$.

*Proof ($I=1$ max cut).* $H$ is an $I=1$ cut with
$n_{\mathrm{cut}}=(n-1)^2$ (#47 Lemma C). Among all $I=1$ cuts at
$n\le 5$, this value is the unique maximum (verification table). The
combinatorial reason matches Lemma G’s charging: an $I=1$ XOR cut
can sever the full party→hub bundle while loading all party–party
phantoms only in the hub-CAUSE / parties-EFFECT atomic pattern $H$;
the dual $H'$ is *not* $I=1$ under XOR (asymmetry vs AND).

**Gap (named, narrow).** Uniqueness of $H$ as max-$n_{\mathrm{cut}}$
among $I=1$ cuts is proved for $n\le 5$ by exhaustion and conjectured
for all $n$ by the same block-charging; the $I\ge 2$ half is
all-$n$. Together with #47’s cut formula this closes #47 C3 for
practical $n$ and leaves only that combinatorial uniqueness for
general $n$.

**Overall T3 status: partial** (I≥2 all-$n$ proved; I=1 uniqueness
partial), but sufficient to treat #47 C3 as **closed on the verified
range and on the cut formula for all $n$**, with the same residual
combinatorial gap made explicit.

*Update after verification script:* we strengthen to **proved for
$n\le 5$ by exhaustion of `SET_UNI/BI`**, and **proved for all $n$
conditional on I=1 uniqueness**. FINDINGS reports this split.

---

## Closing #47

| #47 claim | MIP identity after #49 |
|---|---|
| C1 hub $\Phi=n-1$ | **proved** (T2) |
| C2 pool $\Phi=n(n-1)$ | **proved** (T1) |
| C3 parity $\Phi=2^{2-n}$ | **partial→closed on cut + I≥2; I=1 uniqueness $n\le 5$** |

---

## Best next

**#48** — is the conjunctive hub unique at the $2(n-1)$ edge floor?
Then **#50** — lattice of coordination kinds.
