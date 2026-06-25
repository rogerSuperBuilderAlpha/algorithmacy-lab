---
citekey: casali2013theoretically
title: A Theoretically Based Index of Consciousness Independent of Sensory Processing and Behavior
authors: Casali, Adenauer G. and Gosseries, Olivia and Rosanova, Mario and Boly, Melanie and Sarasso, Simone and Casali, Karina R. and Casarotto, Silvia and Bruno, Marie-Aur{\'e}lie and Laureys, Steven and Tononi, Giulio and Massimini, Marcello
year: 2013
doi: 10.1126/scitranslmed.3006294
arxiv: null
journal: Science Translational Medicine
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://orbi.uliege.be/bitstream/2268/171542/1/A%20theoretically%20based%20index%20of%20consciousness%20independent%20of%20sensory%20processing%20and%20behavior.pdf
sha256: 732f3514eff4c2ad0dc27fdbb7dd0f422c5b3c593b096d42e7cf5a6b806c2626
pdf_path: literature/pdfs/casali2013theoretically.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses the lack of an objective measure of the level of consciousness that does not depend on a patient's ability to sense, move, or behaviorally respond. Motivated by the theoretical idea (drawn from integrated information / brain-complexity theory) that consciousness requires brain activity that is simultaneously integrated and differentiated, the authors introduce the perturbational complexity index (PCI). PCI is computed by perturbing the cortex with transcranial magnetic stimulation (TMS), recording the resulting electrocortical response with high-density EEG, reconstructing the spatiotemporal pattern of significant cortical sources, and then compressing that pattern (Lempel-Ziv complexity, normalized by source entropy) to measure its algorithmic complexity. Tested on a large dataset (208 TMS/EEG measurements in 52 subjects), PCI was high during wakefulness and low whenever consciousness was lost, in NREM sleep, and under three different anesthetics (midazolam, xenon, propofol). PCI reliably discriminated conscious from unconscious states in single individuals and tracked graded changes in the level of consciousness under propofol sedation. In brain-injured patients, PCI was low in vegetative/unresponsive patients, high in locked-in (conscious) patients, and intermediate in minimally conscious patients, suggesting it could provide an objective bedside measure of consciousness independent of sensory processing and behavior.

## Key facts it relies on
- PCI is operationally defined as the normalized Lempel-Ziv complexity of the spatiotemporal pattern of significant cortical activation (SS(x,t)) triggered by a direct TMS perturbation, recorded within the first 300 ms by high-density EEG (60 channels in the illustrated case).
- The full dataset comprised 208 TMS/EEG measurements in 52 subjects (overall); the healthy within-subject part used n = 32 subjects across N = 152 sessions, and the brain-injured cross-sectional part used n = 20 patients with N = 48 measurements.
- In awake healthy subjects, PCI ranged 0.44 to 0.67 (mean +/- SD 0.55 +/- 0.05; N = 110 measurements, n = 32 subjects), and did not significantly depend on TMS stimulation site (BA19, BA08, BA07, BA06, BA04) or intensity (induced field 80 to 160 V/m).
- When consciousness was lost (NREM sleep or anesthesia, n = 24), PCI fell to 0.12 to 0.31 (mean +/- SD 0.23 +/- 0.04; N = 42), giving a clear-cut separation from the conscious group (P = 10^-21).
- Condition-specific unconscious ranges: NREM sleep 0.18 to 0.28 (0.24 +/- 0.02; P = 10^-19); midazolam deep sedation 0.23 to 0.31 (0.28 +/- 0.03; P = 10^-19); propofol 0.13 to 0.30 (0.23 +/- 0.04; P = 10^-13); xenon 0.12 to 0.31 (0.23 +/- 0.06; P = 10^-22).
- Under intermediate propofol sedation (six subjects, MOAAS scores 2-3), PCI showed intermediate values 0.34 to 0.42 (0.39 +/- 0.03; N = 6), significantly higher than deep sedation (P = 0.0004) and lower than wakefulness (P = 0.001).
- In brain-injured patients, PCI was 0.19 to 0.31 in vegetative/unresponsive (VS/UWS) patients (0.24 +/- 0.04; N = 15), 0.32 to 0.49 in minimally conscious (MCS) patients (0.39 +/- 0.05; N = 15), 0.37 to 0.52 in emerged-from-MCS (EMCS) patients (0.43 +/- 0.05; N = 14), and 0.51 to 0.62 in two locked-in (LIS, conscious) patients, matching healthy awake values.
- A reference threshold emerges from healthy data: maximum complexity in unconsciousness was PCI = 0.31 and minimum complexity in alert wakefulness was PCI = 0.44; PCI in MCS/EMCS/LIS patients was always above the highest unconscious value (0.31).
- The TMS-evoked source pattern is extracted via a weighted minimum-norm inverse solution on a three-sphere BERG forward model, with significant sources identified by a nonparametric bootstrap statistical procedure; PCI worked across physiological (sleep), pharmacological, and pathological loss of consciousness.

## Critical notes from the literature
- The authors note the relatively small number of brain-injured patients (n = 20) tested, and call for further studies in larger independent samples of MCS, locked-in, dreaming, and ketamine-anesthesia (dissociated) subjects to confirm reliability.
- They flag an important caveat: although PCI does not depend on cortical stimulation site in healthy brains, it may be inaccurate in brain-injured patients if TMS is applied to a structurally damaged cortical region; PCI is reliable only if the TMS effectively elicits a significant cortical response, motivating imaging-guided TMS positioning.
- The paper contrasts PCI with prior empirical measures: spectral/entropy measures (e.g., the bispectral index) are unreliable across subjects and in brain-injured individuals, and event-related potentials (mismatch negativity, P300, P400) can be absent in conscious subjects and present in unconscious ones; TMS/EEG effective-connectivity measures were previously qualitative and insensitive to graded changes.
- The authors caution that high (spatially extended) neural activation alone does not imply consciousness, since hypersynchronous or widespread but undifferentiated/stereotypical activation can occur during anesthesia, NREM sleep, and generalized seizures.
- This is described as a hypothesis-generating study; validity for clinical application is stated to require assessment in prospective trials.

## Key topics covered
- Perturbational complexity index (PCI)
- Transcranial magnetic stimulation (TMS) with high-density EEG (TMS/EEG)
- Integrated information theory / integration-differentiation account of consciousness
- Lempel-Ziv complexity and algorithmic compressibility
- Source modeling (weighted minimum-norm inverse, BERG three-sphere model)
- Levels of consciousness: wakefulness, NREM sleep, REM/dreaming
- Anesthesia (midazolam, xenon, propofol) and graded sedation (MOAAS scale)
- Disorders of consciousness: vegetative/unresponsive (VS/UWS), minimally conscious (MCS), emerged from MCS (EMCS), locked-in syndrome (LIS)
- Coma Recovery Scale-Revised (CRS-R)
- Objective bedside measure of consciousness independent of sensory/motor function
