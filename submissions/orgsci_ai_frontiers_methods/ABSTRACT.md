# ScholarOne fields: *Organization Science*, AI-Enabled Frontiers

[DRAFTED by Claude, 26 Oct 2026, v3. The abstract field allows 250 words.]

**Title:** Computing the Triad: An AI-and-PyPhi Pipeline for Testing Whether Coordinative Infrastructure Is Irreducible

**Running head:** Computing the Triad

## Abstract
Organizations increasingly coordinate through infrastructure that sits between parties: dispatch systems, claims engines, review gates, AI agents. Platform research calls these arrangements triadic but settles the claim by description. We present a pipeline that computes it. A language model reads case evidence and drafts rival Boolean encodings of who reads whom and what each party commits. Every rule must quote its evidence verbatim, and every encoding carries a prediction fixed in advance. A second, adversarial prompt searches for the most different readings the evidence permits. PyPhi's implementation of integrated information theory 4.0 then computes each encoding exactly. It returns whether any cut along party lines leaves the structure intact, which parties form the irreducible core, the mediator's position (bottleneck, enricher, capture or bypassed), and the single rule on which rival readings diverge. The surface does not decide the verdict: of 256 mediated three-party structures, 24 are irreducible, and time-series proxies separate the two classes barely above chance. In a worked gig-dispatch case, the AI drafter reproduced a human coder's readings, the adversary found two more, and PyPhi refuted both of its predictions. An open repository reproduces every result with one command. In the development stage we will build an encoding module for transcripts and documents, validated against human coders. We will also build a strategic model mapping structural positions and design levers to consequences for platforms, workers and regulators, and validate it on published cases.
