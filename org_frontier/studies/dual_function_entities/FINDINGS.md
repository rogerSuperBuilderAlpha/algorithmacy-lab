# dual_function_entities — findings

Seven platforms decomposed into 16 functions, each classified by the bypass-counterfactual (q213). Every
entity bundles an integrating function with a contingent gate; Amazon spans all four cells. n=3 per form,
exact Φ.

| entity | profile |
|---|---|
| Visa | necessary (authorization) + contingent (network gate) |
| Amazon | necessary (fulfillment) + partial (matching) + contingent (Buy Box) + reducible (1P reselling) |
| Apple App Store | partial (distribution) + contingent (payment gate) |
| Google | necessary (organic matching) + contingent (ad-auction gate) |
| Uber | necessary (real-time matching) + contingent (rider-driver gate) |
| Ticketmaster | partial (distribution/anti-fraud) + contingent (exclusive-venue gate) |
| GDS / Sabre | necessary (inventory aggregation) + contingent (booking gate) |

## The entity does not classify; the function does

A platform's class is not a single label. Run the bypass-counterfactual on Visa as a whole and there is no
answer, because Visa is not one triad. Run it on the authorization function and the answer is necessary: an
approval needs the merchant's request and the issuer's response jointly, and two parties clearing bilaterally
do not reproduce it. Run it on network acceptance and the answer is contingent: the merchant and the
cardholder's bank could clear another way, and the only thing stopping them is that the network's rails are the
rails both sides share. Same company, two functions, opposite cells. The unit that classifies is the (entity,
function) pair.

## Every powerful platform is a bundle

The seven entities share a shape: an integrating function the direct tie cannot reproduce, beside a contingent
gate held shut by a constraint. Visa integrates authorization and gates the network. Google integrates the
ranking of the whole web and gates attention with the ad auction. Uber integrates real-time matching and gates
the rider-driver relationship. The integrating function is why the platform exists; the gate is where the rent
sits. The bypass-counterfactual separates them with a margin: the integrating function carries margin 0 (the
bypass takes nothing), the gate carries margin 2.0 (the bypass takes everything). A platform's power is the sum
of work it earns and a toll it holds, and the two have opposite signatures under the test.

## Amazon is the whole taxonomy

Amazon occupies all four cells at once. Fulfillment integrates a logistics joint condition — necessary.
Marketplace matching integrates demand and supply but a buyer can go direct for a known brand — partial. The
Buy Box gates which seller a buyer sees, and sellers pay to pass — contingent. First-party reselling is a plain
conduit that a brand able to go direct-to-consumer routes around — reducible. The same company is, function by
function, necessary, partial, contingent, and reducible. There is no single thing Amazon is to its sellers; the
question only has an answer once the function is named.

## What the decomposition is for

The verbal version of this is the antitrust question: how much of a platform's position is earned by the
service it provides and how much is a toll on a chokepoint. The bypass-counterfactual answers it function by
function. The integrating functions are necessary or partial and survive the direct tie; the gates are
contingent and dissolve under it, which is to say a remedy that opens the gate — sideloading, interoperability,
breaking an exclusive — removes the contingent function without touching the necessary one. The decomposition
says which remedies hit rent and which would hit the service.

## Caveats

Stylized n=3 Boolean models, one per function, classified by exact Φ; worked illustrations of each role's
structure, not fitted models of the businesses. Which functions a platform has, and which template each maps
to, is a reading of its causal structure stated in `entities.py`; a different reading of a borderline function
(is organic search necessary or partial?) could move it one cell. The decomposition is the contribution: an
entity is a portfolio of (function, class) pairs, and the powerful ones pair earned integration with a held
gate. In-silico; not a measurement of any company.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python org_frontier/studies/dual_function_entities/analyze_dual.py`
