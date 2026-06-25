---
citekey: angus2019recurrence
title: Recurrence Methods for Communication Data, Reflecting on 20 Years of Progress
authors: Angus, Daniel
year: 2019
doi: 10.3389/fams.2019.00054
arxiv: null
journal: Frontiers in Applied Mathematics and Statistics
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.frontiersin.org/articles/10.3389/fams.2019.00054/pdf
sha256: 5441ee9b50b735fdc33b49c43bb2827685969fb06ecfe39e397a583f7ca34782
pdf_path: literature/pdfs/angus2019recurrence.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a review/position piece surveying how recurrence plotting and recurrence quantification analysis (RQA) have been applied to the study of human discourse and communication over roughly two decades, framed from a Communication Studies perspective. Angus traces the lineage from recurrence plots' origin as a tool for high-dimensional dynamical systems (Eckmann et al., 1987) through early language applications (orthographic analysis of poetry, schizophrenia monologs, child/caregiver conversation) to the author's own Conceptual Recurrence Plotting approach and its packaging in the Discursis software toolkit. The review organizes its positions along three key dimensions: discourse type (the need for context sensitivity and theory, e.g., Communication Accommodation Theory), the role of time in encoding input data (uniform vs. non-uniform/turn-based sampling), and the challenges multi-modality places on recurrence-based methods. It introduces specific recurrence machinery including 12 Multiple Participant Recurrence primitives, eight derived metrics, and a "pyramid of conceptual recurrence" for multi-party discourse. The central argument is that recurrence analysis holds much promise for discourse study but that its full potential has yet to be realized in this domain, and that bridging modalities and handling non-uniform time remain significant open challenges.

## Key facts it relies on
- Recurrence plotting was originally invented to display and identify patterns from time series of high-dimensional dynamical systems (Eckmann et al., 1987 [5]); a recurrence plot is a 2D plot whose axes represent time-series time points and whose elements mark where the phase space trajectory satisfies x(i) ≈ x(j).
- For n points in a time series there are n^2 - n recurrence values, or n(n-1)/2 if only one half of the diagonal is used (the latter being the case for conceptual recurrence plots).
- Conceptual Recurrence Plots (Angus, Smith, Wiles 2012 [12,13]) used a Bayes-inspired NLP engine that tags each turn/paragraph along roughly ~100 unique conceptual dimensions, then applies cosine similarity between concept vectors of all segment pairs; no threshold is applied, recurrences are retained as floating-point values between 0.0 and 1.0 and shown by visual intensity.
- Angus et al. [13] designed 12 primitives for conceptual recurrence from all combinations of three dimensions — time scale (short/medium/long), direction (forward/backward), and type (self/other) — and combined selections of these into eight metrics (topic repetition, introduction, reiteration, consistency, novelty), introduced as Multiple Participant Recurrence (MPR) metrics, used mostly in health communication [16-18].
- The "pyramid of conceptual recurrence" (Angus and Wiles 2018 [20]) defines RQA-inspired metrics across whole-conversation, group-group (G2G), person-person (P2P), and turn-turn scales; Conceptual Recurrence Rate (CRR) = (2/(N(N-1))) · sum over i, j>i of R_{i,j}, where N is total turns; analyses included large panel talk shows with up to 30 participants interacting over 1 h.
- Early language applications cited: Orsucci et al. (1999 [8]) plotting recurrence of three-letter word stems in poems across languages; Webber and Zbilut [9] comparing schizophrenia monologs vs. control (scientist) transcripts; Dale and Spivey (2005/2006 [10,11]) analyzing child/care-provider conversation and grammatical coordination via Recurrence Rate.
- The Discursis software packages conceptual recurrence plotting plus bespoke RQA metrics; it accepts CSV-formatted transcripts (one line per turn), builds a bag-of-words statistical language model from the input text (with optional pre-seeding), and is positioned as a CAQDAS system alongside NVivo [36], ATLAS.ti [37], and MAXQDA [38]; an unpublished prototype uses the Paraphrase model [39].
- Multi-modal recurrence challenges: cross recurrence methods require time series sampled at the same (or at least regular) rate, but social processes operate on different time scales; Fusaroli and Tylén [25] developed a multi-modal RQA approach modeling pause/speech, prosody, and lexical choice; PauseCode [51] is an open-source speech/pause coding toolkit; Czyzewski et al. [57] released a corpus of 31 h of high-resolution stereoscopic video, multi-channel audio, and annotated lexical transcripts.
- Applied case studies cited: Angus et al. [44] analyzed 101 "Andrew Denton's Enough Rope" TV talk-show interviews, using recurrence plots (rather than RQA) as salient visual evidence; doctor/patient consultations [15]; and dementia care-provider conversations [48] where apparently "low" recurrence was, per domain experts, very high given dementia's impact.

## Critical notes from the literature
- Self-described scope: the paper is a "position piece"/review (not new empirical work), and the author is the sole contributor; it explicitly builds on and responds to Fusaroli et al.'s [6] earlier comprehensive review rather than rehashing it.
- The paper stresses that recurrence/computational methods do not replace human analysts ("rather they are tools to help analysts ... draw greater insight from their data" [14]) and acknowledges a key methodological friction: Conversation Analysis adherents are skeptical of computational methods that move analysts "away from the data."
- Context-sensitivity is a recurring caution: results can be badly misread without domain expertise (the dementia case, where computer scientists initially saw recurrence as "low" but specialists judged it high), and the most informative features differ by genre (word order matters for poetry but perhaps not for doctor/patient talk).
- Non-uniform time and encoding choices are flagged as unresolved limitations: turn-based sampling makes long turns more likely to recur (denser concept vectors), so element sizing/sampling strategy materially affects visible patterns; cross-recurrence's requirement of regular sampling clashes with the non-uniform timescales of social/multimodal processes.
- The author warns that adding modalities as extra abstraction layers before similarity computation risks reducing system complexity and "missing critical non-linearity," and concedes recurrence analysis's full potential in this domain "has yet to be realized."

## Key topics covered
Recurrence plots; Recurrence Quantification Analysis (RQA); Conceptual Recurrence Plotting; Discursis software; Multiple Participant Recurrence (MPR) metrics; 12 primitives (time scale / direction / type); pyramid of conceptual recurrence; Conceptual Recurrence Rate (CRR), G2G and P2P metrics; social semantic networks; cross-recurrence quantification analysis (CRQA); Communication Accommodation Theory (CAT); Conversation Analysis (CA); CAQDAS tools (NVivo, ATLAS.ti, MAXQDA, Leximancer); discourse type / context sensitivity; time and encoding (uniform vs. turn-based sampling); PauseCode; multi-modality (gaze, gesture, prosody, speech acoustics); dyads vs. multi-party conversation; health and dementia communication; TV talk-show interviews; phase space trajectory; dynamical systems.
