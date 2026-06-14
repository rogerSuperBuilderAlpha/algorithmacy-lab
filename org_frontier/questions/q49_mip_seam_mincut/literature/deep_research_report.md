# Q49 — Stage 2 deep research

The question asks what the minimum-information partition (MIP) of a triadic coordination form names: a
structural seam tied to a specific party, or a degenerate choice among tied partitions. It also asks
whether, once a seam is unique, it falls at a graph min-cut. The literature that bears on this divides
into the definition of the MIP and its ties, the computation that PyPhi performs, the graph-theoretic
min-cut it might reduce to, and the organization-theory reading of a coordination "weakest link." The
target range for a deep-research stage is roughly 15–30 sources; this question is narrow and formal, and
twelve sources cover it. The gap is stated at the end.

## The MIP and its ties

The minimum information partition originates in Balduzzi and Tononi (2008). They define it as the
"informational weakest link": the decomposition of a system into the parts that are most independent,
that is, least integrated, found by searching all partitions after normalization
(`balduzzi2008integrated`). The same paper states the tie rule that matters here: "If there is more than
one partition that attains the minimum normalized value, we select those partitions that generate the
lowest un-normalized quantity of effective information to be the minimum information partition(s)." The
plural is explicit. The MIP can be a set.

IIT 3.0 carried the MIP forward as the partition over which integrated information is evaluated
(`oizumi2014phenomenology`), descending from the original integration proposal in Tononi (2004)
(`tononi2004information`). IIT 4.0 fixes the normalization and the tie-break precisely
(`albantakis2023iit4`). The MIP is the partition minimizing integrated information relative to the maximum
possible value for arbitrary transition matrices of the same dimensions, so the measure reads a system's
fault lines rather than defaulting to cuts between single units and the rest. On ties IIT 4.0 is explicit:
"If two or more partitions minimize Eq (23), we select the partition with the largest unnormalized φs
value as θ′, applying the principle of maximal existence." A reported MIP is therefore one representative
of a possibly larger tie set, chosen by a fixed convention. The convention is a selection rule, not a
claim that the chosen partition is the unique fault line.

## The computation

PyPhi implements the IIT formalism for discrete dynamical systems of binary elements and is the reference
tool for exact Φ (`mayner2018pyphi`). It exposes the system irreducibility analysis, the chosen MIP, and
the set of tied partitions, which is what lets this question read the tie set directly rather than the
single representative the classifier prints.

## Min-cut and graph partitioning

A min-cut on an edge-weighted graph is the partition of the vertices into two sets that minimizes the
weight of crossing edges, computable without flow techniques (`stoer1997simple`). The MIP is a partition
of a system, so a natural hypothesis is that the MIP coincides with a min-cut of the connectivity graph —
the seam falls at the least-coupled boundary. IIT 4.0's own normalization gestures the same way: the
denominator counts the connections a partition severs, so cuts across few connections are favored
(`albantakis2023iit4`). Whether the cause-effect MIP actually reduces to a graph min-cut is an empirical
question for these forms, and the program's prior work warns against the reduction: connectivity predicts
the triadic verdict only to about 93% at n=3, with a holistic residual the graph cannot see.

## The coordination "weakest link"

Organization and economics theory has its own weakest-link idea. Hirshleifer (1983) models public goods
whose social provision is the minimum of individual contributions — the weakest-link rule — and notes it
arises "in linear situations, where each individual has a veto on the total to be provided (e.g., if each
is responsible for one link of a chain)" (`hirshleifer1983weakest`). Coordination theory frames
coordination as managing dependencies among activities, with the structure of the dependency setting which
coordination mechanism applies (`malone1994interdisciplinary`); Thompson (1967) supplies the interdependence
typology the program engaged in Q43 (`thompson1967organizations`). A coordination form's structural weakest
link, read off the MIP, is the formal analogue of the weakest-link party in these accounts. Identifying it
with the worker (probes #26, #33) is a substantive claim about where coordination most nearly factors, and
worth checking against the tie set.

## Method grounding

The protocol's commitment to fixing five hypotheses and their decision rules before computing descends
from Chamberlin's method of multiple working hypotheses (`chamberlin1890multiple`), and the evidence that a
complete pre-analysis plan, not the bare pre-commitment, is what reduces selective analysis
(`brodeur2024preregistration`). Reading the exact-Φ instrument as a ground truth against which a cheap or
structural account is checked is the docking standard, which also fixes the validation gap to real systems
(`axtell1996aligning`).

## The gap

The MIP is defined as a possibly-degenerate object with an explicit tie set and a fixed tie-break
(`balduzzi2008integrated`, `albantakis2023iit4`), and PyPhi exposes that tie set (`mayner2018pyphi`). The
program reported the worker as the MIP seam on a single representative per form (#26, #33) without reading
the tie set. No source, inside the program or out, has asked whether the worker-as-seam result survives
reading the ties, whether a verdict-preserving asymmetry makes the seam unique, or whether the unique seam
reduces to a connectivity min-cut (`stoer1997simple`) for a class of forms while failing on the
pure-higher-order forms the connectivity account already misses. The question is open, and the tools to
settle it exactly are in hand.
