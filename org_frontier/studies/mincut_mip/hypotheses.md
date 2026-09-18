# Min-cut MIP — claims (fixed before proving)

**Question (RESEARCH_AGENDA_50_V2 #49).** Is there a min-cut theorem
placing the MIP at the least-coupled node for a class of forms,
extending the worker-as-weakest-seam result (#26, #33)? In particular:
are the named cuts of #47 the MIP for all $n$ on conjunctive / pool /
parity?

**Already known (cited, not reopened).**
- #26 / #33: corpus/family MIP often reported as `{W,SC}`.
- Q49 (`q49_mip_seam_mincut`, probes #140–#144): worker-unique seam
  **refuted**; Φ-seam ≠ connectivity min-cut on the n=3 mediation
  family (H5). That answers the *graph* min-cut reading of agenda #49
  in the negative for that family.
- #47 `scaling_laws_closed_form/`: GID cut formulas proved; MIP
  identity left open (the gap this study closes).

**What is new.** A *normalized GID cut-weight* theorem for the three
#47 families under `SET_UNI/BI`, not a graph-edge min-cut.

## Instrument (fixed)

Same as #47: major-complex `sia.phi`; `GENERALIZED_INTRINSIC_DIFFERENCE`;
`SET_UNI/BI`; MIP minimizes $(\varphi_{\mathrm{norm}},-\varphi)$ with
$\varphi_{\mathrm{norm}}=\varphi/n_{\mathrm{cut}}$ and
$n_{\mathrm{cut}}=\sum C$ on the cut matrix. Exact Boolean; in-silico.

Named cuts from #47:
- $H$: hub-preserving atomic (row 0 zero; all other off-diagonal 1) —
  $n_{\mathrm{cut}}=(n-1)^2$.
- $H'$: dual (column 0 pattern / hub→party block with party CAUSE).
- $A$: complete atomic (all off-diagonal 1) — $n_{\mathrm{cut}}=n(n-1)$.

## Claims

### T0 — graph min-cut (scope lock)

There is **no** general theorem that the Φ-MIP equals the connectivity
min-cut singleton set for triadic mediation forms. (Q49 H5; cited.)

### T1 — pool

For every $n\ge 3$, at state $\mathbf{1}$, every `SET_UNI/BI` cut
satisfies $\varphi=n_{\mathrm{cut}}$, hence
$\varphi_{\mathrm{norm}}=1$, and the MIP is uniquely $A$ (max
$n_{\mathrm{cut}}$), with $\Phi=n(n-1)$.

### T2 — conjunctive hub

For every $n\ge 3$, at $\mathbf{1}$: $\varphi=p_{\to H}+p_{H\to}$
(star edges only); phantoms among parties obey
$\mathrm{phant}\le\varphi(n-2)$; hence
$\varphi_{\mathrm{norm}}\ge 1/(n-1)$, with equality on a nonempty
family whose maximum raw $\varphi$ is $n-1$, achieved at $H$ and
$H'$. MIP $\varphi=n-1$.

### T3 — parity hub

For every $n\ge 3$, at $\mathbf{1}$: with $\mathrm{sel}=2^{2-n}$,
$\varphi=\mathrm{sel}\cdot I$ for integer $I\ge 1$; every $I\ge 2$
has $\varphi_{\mathrm{norm}}>\mathrm{sel}/(n-1)^2=n\phi(H)$; among
$I=1$ cuts, $H$ uniquely maximizes $n_{\mathrm{cut}}$ at $(n-1)^2$.
MIP is uniquely $H$, with $\Phi=2^{2-n}$.

## Status targets

Each of T0–T3: proved / partial / refuted. #47 C1–C3 MIP gaps close
when T1–T3 are proved.
