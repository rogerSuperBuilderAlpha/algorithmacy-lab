# The thinker paper — a standard

One paper per thinker. Each takes a historical account of the third party — Simmel's *tertius*, Peirce's
genuine triad, Caplow's coalition, Latour's mediator — reads it from the primary texts, renders its claims as
small Boolean forms, tests them against exact IIT-4.0 Φ, and reports what survives. The paper reads as a
standard quantitative research paper: a theory section, pre-registered hypotheses, methods a reader can
reproduce, results in tables, a discussion, limitations. This file fixes the form so that the series is
comparable paper to paper. The six-stage protocol in
[`../protocol/RESEARCH_PROTOCOL.md`](../protocol/RESEARCH_PROTOCOL.md) governs the process; this standard
governs the artifact. Where they overlap, the protocol's gates apply unchanged.

## What a thinker paper is for

The lab has a criterion — a form is irreducible when Φ over the minimum-information partition is positive —
and a century of writing on the triad that draws its distinctions in words. A thinker paper puts one author's
distinctions through the criterion. Three outcomes are possible for each claim, and all three are results:
the criterion **recovers** the claim (the thinker's verdict and the instrument's agree), **refines** it (the
instrument splits a case the thinker treats as one, or grades what the thinker states flatly), or **refutes**
it (the thinker's verdict does not hold on the rendering, and no reasonable re-rendering rescues it). A paper
in which every claim is recovered has probably rendered the claims to fit. A paper in which every claim is
refuted has probably rendered them badly. The series is credible only if the mix is honest.

## Directory and artifacts

```
org_frontier/thinkers/<slug>/
  exegesis.md                 Stage 1: the claims, quoted and page-cited, labelled C1..Ck
  literature/
    deep_research_report.md   Stage 2: what the secondary literature did with the triad; the open gap
    references.bib            every citation, DOIs verified
  hypotheses.md               Stage 3: H1..Hk — one per claim; the thinker's prediction, the null, the lab prior
  methods.md                  Stage 4: forms as rules, controls, decision rules; reproducible without the code
  forms.py                    the forms, shared helpers, the instrument control
  probe_<slug>_<claim>.py     Stage 5: one probe per hypothesis; prints one line per form and one verdict line
  results/*.json              every number the paper reports
  paper.md                    Stage 6: the paper, in the section order below
  FINDINGS.md                 the compact version: numbers, verdicts, caveats
```

Stages 1–4 are committed before any probe runs. The commit that lands `hypotheses.md` and `methods.md` is the
pre-registration; `paper.md` cites its hash.

## The paper: section order and what each must contain

Section titles are short noun phrases. Length 3,500–6,000 words excluding references and appendices.

1. **Title.** A claim or a question, then the thinker: *The superindividual triad: Simmel's third party under
   exact Φ*.
2. **Abstract** (150–250 words). The thinker and the claims; the method in one sentence; the headline per
   hypothesis including every refutation; the one thing the instrument added that the words could not.
3. **Introduction.** Why this thinker's triad matters to coordination theory; that the claims are verbal and
   have never been computed; what the paper contributes; a closing sentence that names the sections to come.
4. **The thinker's account.** The exegesis, in the thinker's words. Quote before paraphrasing. Each claim
   gets a label **C1..Ck**, a verbatim quotation with a page or part citation, and a one-paragraph
   structural restatement — what the claim says about which parties are bound to which. Close with what the
   secondary literature did with these claims and why none of it computed irreducibility.
5. **From claims to forms.** The translation table: claim → structural restatement → Boolean form (rules
   written out) → what the rendering keeps and drops. State the alternative renderings considered and why
   the chosen one is the fairest to the text. This section carries the paper's main risk and says so
   once, flatly.
6. **Hypotheses.** One per claim. For each: the thinker's prediction as **Hk**, the null **H0**, and the
   **lab prior** from `probes/PROBES.md` where one exists — so the reader sees in advance where the thinker
   and the lab's standing results disagree. State that these were fixed before computing and cite the commit.
7. **Methods.** The instrument (exact IIT-4.0 Φ via PyPhi; verdict = Φ over the MIP, max over reachable
   states; the major complex for spectator-robust membership). The control form and its expected value. The
   forms, as rules. The decision rule per hypothesis. The reproduction command. A reader should be able to
   rerun every test from this section and `methods.md`.
8. **Results.** **Table 1** lists every form: verdict, Φ_MIP, major complex, core Φ. Then one subsection per
   hypothesis: the numbers, the verdict — **CONFIRMED**, **PARTIAL**, or **REFUTED** — and the decision rule
   it was read against. Anything observed after the fact is labelled *post hoc* and does not change a verdict.
9. **Discussion.** For each claim: recovered, refined, or refuted, and what that says about the thinker's
   construct. Then the through-line — what the results say together. Then what the instrument added:
   the case it split, the grade it put on a flat claim, the party it moved in or out of the core. Connect
   to the lab's standing results by probe number.
10. **Limitations.** Translation risk first: a Boolean rendering is one of several, and a borderline claim
    could move under another. Then the in-silico scope: evidence about models, not about any group of three
    people. Then what the rendering cannot carry — motive, affect, time, learning — and where that bit.
11. **Conclusion.** One paragraph. No new claims.
12. **References.** Every in-text key resolves to `literature/references.bib`. Primary texts carry a DOI or a
    stable public-domain location. Nothing enters on memory alone.
13. **Appendix A — Forms.** Every form with its full rules and node order, so a reader can rebuild the TPMs.
14. **Appendix B — Reproduction.** The commands, the Python, the expected output lines registered in
    `ci/reproduce.json`.

## Conventions

- **Claims** are C1..Ck; **hypotheses** H1..Hk, one per claim, same index. A claim with no testable rendering
  is listed under *Claims not carried to hypotheses* with the reason.
- **Verdict words.** *Triadic* / *dyadic* for the whole-system verdict; *in the core* / *out of the core* for
  membership; *irreducible* / *factors* for the structure. Do not call Φ a level, a score, or a strength;
  the magnitude is an ordinal hint at most (probe 14).
- **Numbers** are printed to six decimals by the probe and reported to the precision the claim needs. Every
  number in `paper.md` appears verbatim in a `results/*.json` and in a registered `expect` string.
- **Status words** for hypotheses are exactly CONFIRMED, PARTIAL, REFUTED, printed by the probe.
- **The thinker's voice.** Quote first; the structural restatement follows the quotation, never precedes it.
  Do not modernize a thinker's terms in the exegesis; do that in the translation section, where the move is
  visible.
- **Prose** follows [`../../CLAUDE.md`](../../CLAUDE.md): claim-first, named agents, tail-head linkage,
  paragraphs closing on a hook. First person marks authorial labour only.

## Gates before the paper is shown

1. The instrument control passed in every probe, and the paper says so.
2. `hypotheses.md` and `methods.md` predate `results/` in the git log.
3. Every number in `paper.md` traces to `results/*.json`; every probe is registered in `ci/reproduce.json`
   and `python ci/reproduce.py` passes.
4. Every hypothesis has a verdict; refutations are in the abstract.
5. Every citation resolves; DOIs checked; primary text located.
6. A row per probe in `probes/PROBES.md` under the global numbering; a row in the roster table in
   [`README.md`](README.md).
7. The de-slop self-check in `CLAUDE.md`, run on the paragraph, not the sentence.

## Choosing the next thinker

A thinker qualifies when the primary text makes at least three distinct claims about *which parties are
bound to which* in a three-party arrangement — claims about structure, not only about motive or feeling —
and when at least one of those claims disagrees with a standing lab result or with another thinker in the
series. The roster in `README.md` lists candidates and the claim each is expected to contest.
