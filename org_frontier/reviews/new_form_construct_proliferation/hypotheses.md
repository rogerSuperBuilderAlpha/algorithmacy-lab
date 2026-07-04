# Hypotheses — construct proliferation in the "new organizational form"

*Committed before any corpus is harvested or coded. The question: how many distinct construct labels
does organization theory give the "new organizational form," and do the label-camps read each other or
grow in isolation? This is a jangle-fallacy metascience study — the jangle fallacy is the error of
treating one thing under many names as many things. Each hypothesis names the knowledge claim it tests
(in the knowledge-weaving typology), its operationalization, and the outcome that would support versus
challenge it.*

The question is descriptive-integrative: it counts a field's labels for one recurring object and asks
whether those labels form one conversation or several. It matters to the lab's program because the lab
proposes another construct — algorithmacy — for a coordination form that sits near this cluster. Before
adding a label, measure how crowded and how fragmented the label space already is.

## H1 — Many labels, one phenomenon
- **Knowledge claim (stylized fact):** the literature calls the post-bureaucratic / non-hierarchical
  coordination form by many different names — platform, meta-organization, ecosystem, community,
  bazaar, open collaboration, partial organization, network organization, and more — treating
  overlapping phenomena as distinct constructs (the jangle fallacy).
- **Operationalization:** the count of distinct construct labels coded across the corpus, from a closed
  label set plus `other`.
- **Predicts:** more than 8 distinct labels in active use.
- **Challenged if:** the field has consolidated on 8 or fewer labels.

## H2 — Defined by contrast, not by mechanism
- **Knowledge claim (key assumption):** the field defines the new form negatively — by what it is not
  (not a hierarchy, not a market) — rather than positively, by the coordination mechanism that makes it
  work.
- **Operationalization:** code each source's `differentia_mode` as `by_contrast` (differentiates the
  form from hierarchy/market/bureaucracy) or `positive_mechanism` (specifies an internal coordinating
  mechanism as the differentia).
- **Predicts:** `by_contrast` is the majority.
- **Challenged if:** `positive_mechanism` is a plurality or more.

## H3 — Label-camps cite within, not across
- **Knowledge claim (substantive omission / enduring critique):** the label-camps proliferate in
  isolation — each construct's literature cites its own camp and largely ignores the others, so the
  citation graph is block-diagonal by label.
- **Operationalization:** `lib/bibliometrics.py` cluster matrix over the coded `label` as the cluster
  key; within-label versus cross-label citation links among the corpus seeds.
- **Predicts:** within-label links ≫ cross-label links (a block-diagonal matrix).
- **Challenged if:** cross-label links are comparable to or exceed within-label links (the camps read
  each other).

## Method fixed in advance
- Corpus boundary and search: `methods.md` (substantive + procedural gates; semantic search + snowball
  harvest).
- Coders: three independent agents, blind to one another, on `coding_protocol.md`.
- Reliability reported (Fleiss' κ per categorical variable). Any hypothesis the data contradict is
  reported as challenged. If the citation harvest is rate-limited, H1 and H2 are reported from the
  coded corpus and H3 is marked partial.
