# Coding protocol (codebook) — construct proliferation in the "new organizational form"

Code each source from its title + abstract. Code what the SOURCE does — the construct it proposes or
adopts, and how it defines that construct — not what this review predicts. You are one of several
independent coders; do not consult another coder's output. When unsure between two values, pick the
better fit — disagreement is expected and measured.

## Variables (one JSON object per source → your JSONL file)

- **slug** — the source id.
- **label** — the construct term the source proposes or centrally uses for the new/alternative
  organizational form. Closed set (pick the one the source foregrounds):
  - `platform` — platform organization, platform firm, platform-based organizing.
  - `ecosystem` — business/innovation/organizational ecosystem.
  - `meta_organization` — meta-organization (an organization whose members are organizations).
  - `community` — community form, community-based organizing, online community.
  - `network_organization` — network organization, network form, interfirm network.
  - `partial_organization` — partial organization / partial organizing (Ahrne & Brunsson).
  - `open_collaboration` — open collaboration, open-source / peer production, bazaar, commons-based
    peer production.
  - `field_or_institution` — organizational field / institutional field as the form.
  - `hybrid` — hybrid organization / hybrid form as the named construct.
  - `other` — a distinct label not in the list (e.g. holacracy, adhocracy, heterarchy, post-bureaucratic
    form, temporary organization, project network). Use when the source's central label is none of the
    above.
- **differentia_mode** — how the source establishes what the form IS (tests H2):
  - `by_contrast` — the form is defined chiefly by contrast to hierarchy, market, bureaucracy, or "the
    firm" (what it is not).
  - `positive_mechanism` — the form is defined chiefly by a positive internal coordination mechanism
    (e.g. modular interfaces, membership rules, generativity, shared identity, mutual adjustment).
- **parent_form** — the baseline against which the source positions the new form:
  `hierarchy` | `market` | `network` | `none` (no explicit baseline invoked).
- **claim_type** — the knowledge-weaving type of the source's central claim about the form:
  - `stylized_fact` — asserts the form exists / is prevalent / behaves a certain way as established.
  - `assumption` — takes the form's coherence for granted to build other analysis on it.
  - `critique` — disputes, bounds, or problematizes the construct or a rival construct.
  - `omission` — notes a gap the construct is meant to fill / calls for the new label.

## Output

Write JSONL to `coding/coder<yourname>.jsonl`, one line per source:
`{"slug":"smith2020","label":"platform","differentia_mode":"by_contrast","parent_form":"hierarchy","claim_type":"stylized_fact"}`

Code every source in the corpus (`literature/corpus.jsonl`). If capacity runs low, code in list order
and report how far you got.

## What the hypotheses predict (do NOT let this bias a call — code the source, not the prediction)

- H1 predicts many distinct `label` values. Do not spread calls to inflate the count; assign the label
  the source actually foregrounds, even if that concentrates the distribution.
- H2 predicts `differentia_mode=by_contrast` dominates. A source that specifies a positive coordinating
  mechanism as its differentia is a real disconfirming datum — record it as `positive_mechanism`.
