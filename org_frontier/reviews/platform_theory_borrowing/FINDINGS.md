# Findings — platform research borrows economics early and ecosystem theory late, and it more often claims to extend a parent theory than to apply it

Eighty platform-governance sources (2002–2026), three independent agent coders, coded for the parent
theory each imports, how it treats that theory, and whether it combines more than one. Two-sided-market
economics leads the early period; ecosystem theory rises in the later period while institutional theory
stays marginal; a third of the corpus imports a theory outside the seven-way scheme; single-theory
imports dominate; and, against prediction, most sources were coded as *extending* their parent theory
rather than applying it.

## Intercoder reliability
| variable | Fleiss' κ | mean agreement | interpretation |
|---|---|---|---|
| parent_theory | 0.872 | 90.4% | almost perfect |
| borrowing_mode | 0.678 | 85.8% | substantial |
| multi_theory | 0.760 | 95.8% | substantial |

Three agents applying the fixed codebook blind to one another converged; the parent-theory attribution
is almost-perfect, and the two mode/count variables are substantial. The κ answers the single-coder
objection.

## Results
| # | Hypothesis | Verdict | Statistic |
|---|---|---|---|
| H1 | economics theories lead early; institutional + ecosystem rise later | Supported (qualified) | pre-2015 economics 60% vs 13%; 2015+ economics 22%, inst+ecosystem 32%; ecosystem 2→18, institutional flat at 3 |
| H2 | most sources borrow-and-apply rather than extend or critique | Challenged | apply 29% (23/80); extend 70% (56/80); critique 1% |
| H3 | single-theory imports dominate | Supported | multi-theory 10% (8/80); single 90% |

## What the data show

**H1 — supported, with one leg qualified.** In the pre-2015 window, economics leads: two-sided-market
theory alone is 8 of 15 sources, and `tce` + `two_sided_market` together are 60%, against 13% for
institutional + ecosystem. In 2015-and-after the economics share falls to 22% and the
institutional-plus-ecosystem share rises to 32%. The rise is carried almost entirely by ecosystem
theory (2 sources pre-2015 → 18 after), not institutional theory, which stays at three sources across
the whole corpus. The predicted late-period rise of *institutional* theory does not appear in the
abstracts; the ecosystem/complementor turn is the real shift. The direction of H1 holds and its
economics-early claim is clean, but "institutional theory rises" is not supported.

**H2 — challenged.** The prediction was that platform research imports a theory as a ready lens and
applies it. The coders read the opposite: 70% of sources (56/80) were coded `extend` — they claim to
develop or modify the parent theory using the platform case — against 29% `apply` and a single
`critique`. Platform-governance research, as its abstracts present it, is a literature that advertises
theoretical extension far more than plain application. The caveat below bounds this.

**H3 — supported.** Multi-theory imports are rare: 10% of sources (8/80) braid two or more parent
theories; 90% run on a single lens. The field accumulates parallel single-theory studies, as
predicted.

**A side finding worth stating.** The largest single `parent_theory` value is `other` (28/80, 35%) —
sources whose primary theory sits outside the seven-way scheme, mostly labour-process theory in the
gig/algorithmic-management cluster, plus entrepreneurship, RBV, stakeholder, and structuration imports.
Platform-governance research borrows from a wider shelf than the canonical platform-economics and
platform-ecosystem theories; a third of it reaches past them.

## What the data revise

The pre-registered picture of the late period was "institutional and ecosystem theory rise." Only
ecosystem theory rises; institutional theory is near-absent throughout. And the field is not the
apply-a-borrowed-lens literature H2 assumed — coders overwhelmingly read platform papers as claiming to
extend their parent theory. The corrected statement: platform-governance research moves from
two-sided-market economics toward ecosystem/complementor theory as it matures, imports one theory at a
time, and routinely frames that import as an extension of the parent theory rather than a plain
application.

## Limitations
- **Agent coders.** The three coders are LLM agents applying a fixed codebook, not trained human
  raters. Agreement is high (κ = 0.87 on parent_theory) but is not a substitute for human coding.
- **The `extend` reading (H2).** Abstracts are where authors advertise novelty ("we extend X to
  platforms"). Coding borrowing_mode from the abstract likely inflates `extend` over what a full-text
  reading of the paper's actual theoretical contribution would show. The H2 challenge is a claim about
  how sources *present* their borrowing, and should be read as such.
- **Corpus bound and the labor cap.** The corpus is one semantic-search connector's neighborhood,
  English-language, screened to platform-as-organization sources. The platform-labor cluster was large
  and was capped (every governance/strategy/economics/ecosystem source and every pre-2015 source kept;
  the labor cluster filled the remaining slots in year order). A different cap would move the `other`
  share.
- **Small early cell.** The pre-2015 window is 15 sources; the economics-early result rests on a small
  n, though the effect (60% vs 13%) is large.
- **Single-theory attribution.** `parent_theory` records one primary theory; a secondary theory named
  only in the full text is not captured, which can understate multi-theory borrowing (H3).

## Reproduce
```bash
python3 -m org_frontier.reviews.lib.reliability org_frontier/reviews/platform_theory_borrowing/coding \
    --categorical parent_theory,borrowing_mode,multi_theory \
    --out org_frontier/reviews/platform_theory_borrowing/results/frozen.json
python3 -m org_frontier.reviews.platform_theory_borrowing.run
```
Registered numbers: `results/summary.json` (parent-theory distribution overall and by period,
borrowing-mode distribution, multi-theory rate); κ printed by the reliability step.
