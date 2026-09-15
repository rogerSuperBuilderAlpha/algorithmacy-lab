# Davis — Stage 2 literature

## Primary text

Davis (1967) is seven pages in *Human Relations* and turns on one substitution. Harary (1953) and Cartwright
and Harary (1956) had formalized Heider's balance as a property of signed graphs — a graph is balanced iff
every cycle has an even number of negative lines — and proved the structure theorem: a balanced graph
partitions into at most two plus-sets with all positive lines within and all negative lines between. Davis
observes that groups often have more than two cliques, defines a graph as *clusterable* when its points
partition into any number of such sets, and proves that a signed graph is clusterable iff it contains no
cycle with exactly one negative line (181). The proof, he notes, was supplied by Cartwright and Harary in
place of his own longer one (182 n. 2). Balance becomes the two-set special case. For complete graphs the
condition reduces to triangles (183): a complete signed graph is clusterable iff no triangle has exactly one
negative line, and its clustering is unique. The sociology behind the formalism is Davis (1963) on
mechanical solidarity and the "crosspressure hypothesis" (184 n. 3): the friend of two enemies is the one
position the structure cannot place.

The consequence for the triad is the paper's point. Balance forbids two of the four signed triangles —
++− and −−−. Clustering forbids only ++−. The all-negative triangle, which Heider (1958) had called
"too indetermined" and Cartwright–Harary had called unbalanced, is clusterable with three plus-sets.

## What the literature did with it

**Signed-graph theory.** Doreian and Mrvar (1996) build the partitioning approach on Davis: *k*-balance
subsumes balance (k = 2) and clustering (k > 2), and the line index of imbalance counts the lines whose
sign must change to reach a k-balanced structure. Zaslavsky's later work characterizes k-clusterability
through the chromatic number of the graph obtained by contracting the positive components; for k > 2 the
decision problem is NP-complete.

**Triad census.** Davis and Leinhardt (1972) carry clustering into the ranked-clusters model and the
sixteen-type triad census, and find that empirical sociograms violate the forbidden triad less than chance
would predict. The all-negative triad, in that program, is a structural fact about groups with several
cliques rather than a case of tension.

**Organization studies.** Faction and coalition models in organizations rest on clusterability in Davis's
sense whenever they allow more than two camps; the formal condition is rarely cited.

## The open gap

The lab's Heider paper found ++− and −−− indistinguishable: Φ = 6, all three persons in the core, no rest
state, the same attractors. That finding was computed with one bit per person, and one bit is two camps.
Two camps is Cartwright–Harary's two-plus-set restriction built into the instrument, and under it the
all-negative triangle cannot rest for the same reason it is unbalanced: three mutually different persons
need three values. Davis's paper is a direct contest of the lab's result, and the contest can be run: give
each person an alphabet of k camps, encode the camp in two bits, let each person move to the camp of least
strain, and ask whether the all-negative triangle's verdict changes with k while the forbidden triangle's
does not. If it does, the Heider paper's H3 refutation was an artifact of the alphabet, and the instrument
sides with Davis. If the classes under Φ then follow clusterability — the forbidden pattern alone, the
three clusterable patterns together — the substitution of "exactly one" for "odd" is visible in the
structure and not only in the combinatorics.

## Sources

- Primary: `references.bib` — `davis1967clustering` (pp. 181–184), `davis1963structural`, `davis1972structure`.
- The line: `harary1953notion`, `cartwright1956structural`, `doreian1996partitioning`, `heider1958psychology`.
- Instrument: `albantakis2023iit4`, `mayner2018pyphi`.
- Davis 1967, Davis 1963, Cartwright–Harary 1956, Doreian–Mrvar 1996, and Harary 1953 DOIs checked against
  Crossref.
