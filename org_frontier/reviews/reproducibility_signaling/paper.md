# Reproducibility Signaling in Management Research: A Lower-Bound Estimate from 88 Abstracts, 2015–2025

## Research Summary

Management journals have spent a decade adding open-science policies: data-availability statements,
badge programs, registered-report tracks, and repository mandates. This study asks a narrower question
than whether those policies work. It asks whether authors *say* they follow the practices where a
reader first looks — in the title and abstract. Three independent coders read 88 empirical management
and organization papers published between 2015 and 2025, evenly spread across the eleven years, and
recorded whether each abstract signaled open data, available code, or pre-registration, along with the
paper's method type. One paper of the 88 signaled anything. That paper is a registered-report survey
whose topic is open research practice. Open data and shared code appear in zero abstracts. Intercoder
reliability is perfect (Fleiss' κ = 1.000 on every variable), which is less a coding achievement than a
symptom of how little there was to code. Signaling in management abstracts is a floor, and the one-word
verdict on the field's headline claim is that reproducibility signaling is not merely uncommon; in this
channel it is nearly absent. The rates are lower bounds, because most data-availability statements live
in a paper's back matter, and the size of the gap between this lower bound and true practice is the
next thing worth measuring.

## Introduction

The credibility movement arrived in management research after it reshaped psychology. Replication
failures, concerns about questionable research practices, and the spread of pre-registration pushed
several management and organization journals to adopt open-science infrastructure over the 2015–2025
window. *Strategic Management Journal*, *Journal of Business and Psychology*, *The Leadership
Quarterly*, and others introduced open-science badges, data and code availability policies, or
registered-report formats during this period. The Center for Open Science's Transparency and Openness
Promotion guidelines gave journals a menu of standards to adopt. Editorials in the field's methods
outlets called for data sharing and pre-registration as routine.

Policy adoption and author behavior are different measurements. A journal can require a data-
availability statement without any author depositing data; an author can pre-register without saying so
where a casual reader would notice. This study measures one visible slice of author behavior: the
signal a paper sends in its title and abstract. The abstract is what a reader, a search engine, and an
automated screening tool encounter first, and what a paper chooses to foreground there is a reasonable
proxy for what its authors treat as salient. If open data, shared code, and pre-registration had become
normal and prized, some fraction of abstracts would advertise them, the way abstracts already advertise
sample size, effect direction, and theoretical contribution.

The question is descriptive, in the systematicity typology of Simsek, Fox, and Heavey (2023): how often
does the signal appear, and does its frequency move over time. Three claims about the literature are
testable against a coded corpus. The first is a stylized fact the field half-believes about itself:
that open-science practice remains a minority behavior. The second is an assumption baked into the
optimistic reading of the past decade: that signaling has risen as norms diffused. The third is an
enduring methodological critique: that the open-science apparatus was built for quantitative work and
fits qualitative traditions poorly, so quantitative papers should signal more. Each becomes a
hypothesis with a predicted proportion, pre-registered before any coding, and each is reported below
with its number and a verdict.

## Framework

Reproducibility signaling, as measured here, is the presence in a paper's abstract of a statement that
the study followed one of three practices. Open data is a statement that the study's own data are
deposited or shared — an OSF or Dryad link, a named repository, a sentence that data are publicly
available. Code availability is a statement that analysis scripts, syntax, or a computational model are
shared. Pre-registration is a statement that hypotheses or the design were registered in advance, or
that the paper is a registered report. The measurement is deliberately literal. A statement present in
the abstract is a signal; silence is coded as no signal. Using a pre-existing public dataset such as
Compustat or the World Values Survey does not count, because it says nothing about the authors' own
transparency; only a statement that the authors deposited or shared their own data or extract counts.

This literalness sets the quantity the study estimates: the visible signal, and a lower bound on true
practice. A paper can deposit data and never mention it in the abstract; that paper is coded as no
signal and is a false negative against real practice, by design. The coding recovers what is
advertised, not what is done. The value of the lower bound is that it is honest and reproducible — any
reader of the same abstract reaches the same code — and that its distance from true practice names a
concrete follow-up.

Method type is coded alongside the signals to test the third hypothesis. A paper is quantitative when
it analyzes numeric data statistically (surveys, panels, archival data, experiments, simulations with
statistics), qualitative when its evidence is interviews, ethnography, case study, or grounded theory,
mixed when it balances both, and conceptual when its abstract shows no primary empirical data. The
distinction matters because the three signaling practices carry different costs across method types.
Depositing survey data or a panel extract is routine; depositing interview transcripts raises
confidentiality problems and often cannot be done at all. Pre-registration presumes hypotheses fixed
before data collection, which fits confirmatory quantitative designs and sits awkwardly with the
emergent logic of qualitative inquiry. The apparatus, in short, was built around one kind of study, and
the third hypothesis asks whether the signaling follows the apparatus.

## Method

The corpus boundary, fixed in `methods.md` before coding, admits empirical papers in management and
organization research — organizational behavior, human resources, strategy, entrepreneurship, corporate
governance, operations, and adjacent subfields — published in English between 2015 and 2025 and indexed
in the Scholar Gateway academic corpus. Twelve semantic-search queries crossed subfields with
open-science topics and were windowed across the decade so the corpus would spread over the eleven
years rather than pile into recent ones. A title-cue screen dropped reviews, editorials, research
agendas, and framework papers. A build script deduplicated the returned records by DOI and then by
normalized title, applied the screen, and capped the corpus at eight papers per publication year to
hold an even spread for the trend test. The result is 88 sources, eight per year from 2015 through 2025.

Three independent coders — LLM agents, each blind to the others, each given the same codebook —
read every source's title and abstract and wrote a JSON record per paper: open_data, code_available,
and preregistered as yes or no, method_type as one of the four values, and the year. The three coder
files were scored with the arm's reliability tool, which reports Fleiss' κ per variable and builds a
majority-vote adjudicated dataset. All analyses run on the adjudicated dataset, joined to the
authoritative publication year from the corpus metadata.

The three hypotheses map to three tests. H1 is the any-signal rate: the share of papers coded yes on at
least one of the three signaling variables, predicted to be a minority. H2 is the any-signal rate by
period, 2015–2019 against 2020–2025, predicted to rise, with a by-year breakdown for the trend. H3 is
the any-signal rate for quantitative against qualitative papers, predicted higher for quantitative.
Each hypothesis is reported with its statistic and a supported, qualified, or challenged verdict.

## Results

The three coders agreed completely. Fleiss' κ is 1.000 for open_data, code_available, preregistered,
and method_type, with 100% pairwise agreement on all four. Agreement this total is unusual and demands
an explanation, which the signal itself supplies: with the signaling variables almost always zero,
there was little for coders to weigh. The reliability answers the objection that a single reader's
judgment drove the result — three readers produced the same dataset — but the κ is as much a
description of the finding as a warrant for it.

**Table 1. Reproducibility signaling rates (adjudicated; each a lower bound).**

| Signal | Papers coded "yes" | Rate |
|---|---|---|
| Open data | 0 / 88 | 0.0% |
| Code available | 0 / 88 | 0.0% |
| Pre-registration | 1 / 88 | 1.1% |
| **Any of the three** | **1 / 88** | **1.1%** |

One abstract in 88 signals any reproducibility practice. That single paper is a 2024 registered-report
survey of open research practices in psychology departments, coded quantitative — a paper whose subject
is open science and which is a registered report by its own title. No abstract in the corpus states that
its authors deposited their own data, and none states that analysis code is available. H1 predicted a
minority; the data return one paper, and even that one is atypical of the empirical management work the
corpus was built to sample. **H1 is supported**, and more strongly than the hypothesis claimed:
in-abstract signaling is not a minority behavior but a near-absent one.

**Table 2. Any-signal rate by year.**

| Year | Any-signal | Rate |
|---|---|---|
| 2015 | 0 / 8 | 0.0% |
| 2016 | 0 / 8 | 0.0% |
| 2017 | 0 / 8 | 0.0% |
| 2018 | 0 / 8 | 0.0% |
| 2019 | 0 / 8 | 0.0% |
| 2020 | 0 / 8 | 0.0% |
| 2021 | 0 / 8 | 0.0% |
| 2022 | 0 / 8 | 0.0% |
| 2023 | 0 / 8 | 0.0% |
| 2024 | 1 / 8 | 12.5% |
| 2025 | 0 / 8 | 0.0% |

Grouped into periods, the earlier window 2015–2019 shows 0 of 40 (0.0%) and the later window 2020–2025
shows 1 of 48 (2.1%). The later rate exceeds the earlier one, so the comparison points the way H2
predicted. The weight it can bear is another matter. The entire difference is one paper in 2024; every
other year-cell is zero. Delete that paper and the trend is 0.0% against 0.0%. A rise built on a single
observation is not a rise a reader should trust, and the honest verdict is that the corpus carries too
little signal to test the trend. **H2 is qualified**: the direction is nominally consistent with the
hypothesis, and the data cannot distinguish it from a flat floor.

The same single paper governs the method comparison. Quantitative papers signal at 1 of 64 (1.6%),
qualitative at 0 of 8 (0.0%), mixed at 0 of 7 (0.0%), and conceptual at 0 of 9 (0.0%). Quantitative
exceeds qualitative, as H3 predicted, but the quantitative rate is one paper — the same registered
report — and the qualitative cell is a floor of zero over a small denominator. **H3 is qualified** for
the same reason as H2: a directional result resting entirely on one observation, against zeros
everywhere else. The corpus does not contain enough signaling to separate quantitative from qualitative
behavior in this channel.

The method distribution is a finding in its own right. Of the 88 papers, 64 are quantitative, 9
conceptual, 8 qualitative, and 7 mixed. The nine conceptual sources slipped a screen built to catch
reviews; they are open-science topical papers — pieces discussing data sharing, pre-registration, and
credibility reform. They talk about the practices at length and do not signal that the article in hand
does any of them. The literature about reproducibility is visible in abstracts; the practice of
reproducibility is not.

## Discussion

The headline result is stark and one-directional: management abstracts almost never advertise open
data, shared code, or pre-registration, and this holds flat across the entire 2015–2025 window. If the
open-science movement changed what management authors do, it did not change what they say in the one
place a reader looks first. The gap between a decade of policy adoption and a near-zero signaling rate
is the interesting quantity, and there are two readings of it.

The first reading is that practice itself remains rare, and the abstracts are telling the truth.
Adoption of journal policy does not compel author behavior, and if few management authors deposit data
or pre-register, few abstracts would mention it. Under this reading the 1.1% is close to real practice
and the field's credibility reforms have not yet reached the median paper.

The second reading is that practice has grown but lives out of sight. Data-availability statements are
increasingly generated from submission metadata and printed in back matter that never touches the
abstract; OSF links sit in a footnote or a method section; a registered-report designation appears on
the first page but not in the 200-word summary. Under this reading the abstract is simply the wrong
place to look, and the true rate is materially higher than 1.1%.

This study cannot adjudicate between the two readings, and saying so is the point of calling every rate
a lower bound. What it establishes is the lower bound itself and its flatness: whatever is happening to
practice, the abstract channel carries essentially none of it, in any year, for any method. That is
useful in two ways. It sets a floor that a full-text audit must beat to demonstrate growth, and it
identifies where signaling is not happening — the front matter — which matters for anyone who relies on
abstracts to screen literature at scale, including automated meta-science and evidence-synthesis tools.
A screening pipeline that keys on abstract text will find almost no reproducibility signal in management
research, not because the practice is absent but because the abstract is not where the field records it.

The qualified verdicts on H2 and H3 carry a methodological lesson for this kind of review. When the
base rate of a coded feature is near zero, hypotheses about its distribution — over time, across
groups — cannot be tested at corpus sizes in the tens, because a single observation swings every
comparison. The direction of both tests matched the prediction, and neither is worth defending, because
each rides on the same lone paper. A study designed to test H2 and H3 seriously would need either a much
larger corpus or a full-text protocol that lifts the base rate off the floor, and probably both.

The finding also relocates the phenomenon. The most reproducibility-conscious documents in the corpus
are the ones about reproducibility. The nine conceptual, open-science topical papers foreground the
practices they study; the 64 ordinary empirical papers, the actual objects of a data-sharing norm, do
not. A movement can generate a visible literature about itself while leaving little trace on the routine
output it means to change. Measuring the second, not the first, is the harder task, and the abstract
channel understates it by construction.

## Limitations

Abstract-only coding is the limitation that bounds every number here. Data-availability statements,
open-materials notes, and repository links overwhelmingly appear in a paper's back matter, and journals
increasingly render them from structured submission fields rather than author prose. Coding from the
abstract therefore undercounts real practice, and every rate reported is a lower bound. The gap between
this lower bound and true practice is unmeasured, and closing it requires the full text.

The corpus is a bounded sample, not a census. It is drawn from one semantic-search connector's
coverage, restricted to English-language indexing, and capped at eight papers per year to hold an even
trend spread. A different connector, a different subfield mix, or an uncapped draw could move the rates,
though a signal this close to zero leaves little room to move downward. Eleven year-cells of eight
papers is a thin base for a trend test, as the qualified H2 verdict reflects.

The coders are LLM agents applying a fixed codebook, not trained human raters. Their agreement was
perfect, which reflects the near-constant signal more than it certifies human-grade judgment;
independent human coding on a full-text corpus would be a stronger design, and the perfect κ here should
not be read as evidence that agent coders match human ones on harder distinctions. Finally, the
conceptual-paper contamination — nine topical open-science pieces that passed a review screen tuned for
a different genre — is a reminder that a title-cue boundary is porous; those papers were coded on their
merits and left in, and they do not carry signaling, so they do not inflate the rates.

## References

Full bibliographic entries for the 88-paper corpus and the two method papers are in
`literature/references.bib`. The method sources are:

Simsek, Z., Fox, B. C., & Heavey, C. (2023). Systematicity in organizational research literature
reviews: A framework and assessment. *Organizational Research Methods, 26*(2), 292–321.
https://doi.org/10.1177/10944281211008652

Simsek, Z., Heavey, C., Fox, B. C., & Yu, T. (2022). Compelling questions in research: Seeing what
everybody has seen and thinking what nobody has thought. *Journal of Management.*
https://doi.org/10.1177/01492063211073068
