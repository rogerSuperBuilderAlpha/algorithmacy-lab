# Prompt: promote `algorithmacy-lab` on algorithmacy.com

A copy-pasteable prompt for a Claude session working on the algorithmacy.com website. It adds a Research/Lab
page and a homepage callout that promote this repository, leading with the method, in an academic register.
The only optional fill-in is a Substack URL if those essays get posted there.

---

**Task: add a Research / Lab section to algorithmacy.com promoting the `algorithmacy-lab` repository.**

You are working on the algorithmacy.com website. Add a dedicated **Research** (or "Lab") page plus a short
**homepage callout** that points to it, promoting an open computational research program. Lead with the
*method* as the novelty; treat the algorithmacy thesis as the domain the method is applied to. Audience:
researchers and serious readers. Register: precise, credible, honest about scope. Do not overclaim.

**First, before writing anything:** inspect this site's stack, file structure, navigation, and existing
voice/CSS. Match them. Identify where a new page and a homepage callout should live. Propose the placement
and a draft before publishing or deploying — do not push live without confirmation.

**What the program is (use these facts; do not invent results or numbers):**
- A public research repository, **`algorithmacy-lab`**, applying *exact integrated information* (Φ, from
  IIT 4.0, computed with the PyPhi library) to organizational coordination theory. The lab lives in the
  `org_frontier/` directory; a `foundations/` directory holds the measure-validation experiments that
  established the instrument.
- **The thesis it tests:** a coordination form is either *dyadic* (it factors into independent pieces — it
  demands literacy) or *triadic* (it is structurally irreducible — it demands algorithmacy). This is made
  computable: model a worker–system–counterpart arrangement as a small Boolean dynamical system and read
  whether its most-integrated state factors (dyadic) or stays bound (triadic). The verdict is exact, not a
  proxy.
- **The method (lead with this):** a six-stage, AI-assisted research protocol that takes one question to a
  finished quantitative paper — (1) review prior work, (2) deep literature research, (3) fix five
  falsifiable hypotheses *before* computing, (4) specify methods, (5) run the tests against the exact-Φ
  ground-truth instrument, (6) write a full paper, reporting nulls and refutations as first-class results.
  It is grounded in established norms (Platt's strong inference, Chamberlin's multiple working hypotheses,
  pre-registration) and is made *runnable* end to end.
- **The track record:** 134+ logged experiments ("probes"), each with question / hypothesis / method /
  result; six iterative research programs; a standing agenda of 50 open questions. About a third of the
  results are nulls or refinements, logged as such — that honesty is part of the point.
- **The worked example:** the first question taken fully through the automated pipeline tested whether the
  dyadic/triadic verdict reproduces Thompson's (1967) pooled/sequential/reciprocal interdependence
  ordering. It does not: four of five hypotheses confirmed, one refuted, and the headline is a negative
  result about a classic typology. Present it as a worked example of the method, not a settled claim.

**Links to feature (verify each resolves before publishing):**
- The repository: **https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab**
- The method write-up: `org_frontier/essays/studying_algorithmacy.md`
- The protocol spec: `org_frontier/protocol/RESEARCH_PROTOCOL.md`
- The experiment catalog: `org_frontier/essays/pyphi_org_theory_catalog.md`
- The logbook: `org_frontier/probes/PROBES.md`
- The pilot paper: `org_frontier/questions/q43_thompson_interdependence/paper.md`
- The foundations arc: `foundations/README.md`
- [OPTIONAL: if these essays are posted on Substack, link those URLs too — otherwise link the GitHub
  markdown above, which renders on GitHub.]

**Hard constraints:**
- **Accuracy.** Every claim and number must come from the facts above (or from the linked files if you can
  fetch them). Invent nothing. If unsure, link rather than summarize.
- **Honest scope.** State plainly that these are *in-silico* results on small Boolean models, computed
  exactly, and that a validation gap separates them from empirical claims about real organizations —
  cross-model agreement is internal validity, not external validity. The program is a proof-of-method and a
  research agenda, not peer-reviewed findings about real firms. Do not let the page imply the thesis is
  empirically proven.
- **Privacy.** Promote only the public `algorithmacy-lab` repository. Do **not** reference, link, or
  describe any private dissertation repository.
- **Link, don't copy.** Drive readers to the repo and essays; don't paste large excerpts.
- **Voice.** Match algorithmacy.com's existing tone. Plain, declarative, no hype adjectives, no
  "revolutionary/groundbreaking." Let the rigor show through specifics (exact Φ, 134 probes, honest nulls),
  not superlatives.

**Deliverables:**
1. A new **Research / Lab page** with: a one-paragraph lead on the method; a short "the thesis it's applied
   to" section; "the track record" (the numbers above); the worked example as an honest mini-case; a
   clearly-labeled scope/limitations note; and a tidy link list to the repo and key documents.
2. A **homepage callout** (a heading, two or three sentences, and a link to the Research page) placed where
   it fits the existing layout.
3. A note to me listing the exact files you changed, the links you verified, and anything you were unsure
   about — before any deploy.
