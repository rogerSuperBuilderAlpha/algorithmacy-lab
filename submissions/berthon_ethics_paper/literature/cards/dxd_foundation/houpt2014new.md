# Houpt, J. W., Townsend, J. T., & Donkin, C. (2014). A new perspective on visual word processing efficiency. *Acta Psychologica, 145*, 118–127.

**Identifier:** doi:10.1016/j.actpsy.2013.10.013 · **Read depth:** full_text (PMC author manuscript, PMC3877166, Europe PMC XML; no journal page numbers, so locators are section names; Appendix A and B tables were not read in detail) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** two response-time experiments on four-letter strings; Experiment 1: 10 Indiana University students (8 women, 2 men; aged 19–34), five string types (words, pseudowords, unpronounceable nonwords, upside-down nonwords, Katakana), 10 sessions of 45–60 minutes each, 240 trials per block, 80 ms exposure with no mask; Experiment 2: 12 different students (10 women, 2 men), words, pseudowords and random consonant strings, upper case, with a mask, 100 ms exposure · **Parties modeled:** person–artefact (reader and letter string) · **Facets:** D · **Read:** 2026-10-13

## What it argues
Houpt, Townsend and Donkin ask whether a word context makes letters easier to perceive when the measure is response time and not accuracy. The classic word superiority effect (Reicher, 1969; Wheeler, 1970) shows in accuracy and needs a post-stimulus mask; a matching effect in response times "has been elusive" (Introduction). The authors apply the capacity coefficient, C(t), a response-time measure that compares the time for a whole string with the time predicted if each letter were processed in parallel at its isolated speed (Introduction, "The Capacity Coefficient"; Eq. 1). C(t) above 1 is super-capacity, below 1 limited capacity.

The Introduction retells the history: Cattell (1886) found letters held up at faster rates when they formed words, a result confounded by the way words constrain their letters; Reicher (1969) removed the confound with a two-alternative design in which both choices were words; Wheeler (1970) ruled out several alternative accounts. Pelli et al. (2003) argued that letters are detected independently, and the authors present their own data as a test of that claim.

Results:
- Experiment 1 (no mask): raw string response times separated words and pseudowords from upside-down and Katakana strings (for example, Word against Upside-Down, F(1,9) = 50.85, p < .0025). Words did not differ reliably from pseudowords or random letters in raw times. The capacity coefficient did separate them: word capacity exceeded pseudoword capacity (z = 7.27), random letters (z = 22.9), upside-down letters (z = 36.7) and Katakana (z = 45.9), all p < .0025. Words and pseudowords were super-capacity for nearly all participants; upside-down and Katakana strings were limited capacity.
- Experiment 2 (masked, capitals): the same order held. Words and pseudowords were super-capacity for nearly all 12 participants. For random letters, half the participants had accuracy too low for C(t) to be computed. Word and pseudoword capacity did not differ reliably (t(10) = 0.773, p = .458).
- General Discussion: the data reject an independent, unlimited-capacity parallel model, "the models presented in Massaro (1973) and Pelli et al. (2003) are not consistent with the findings". The authors list facilitation between letters, a phonological route, and coactive pooling as candidate accounts and do not choose among them. They add that perceptual learning probably contributes, citing Blaha (2010), where about a week of training moved squiggle-stimulus capacity from very limited to high.

## Relation to the argument
The paper bears on facet D only through the history it retells. The project cites it "only for its account of Cattell," and that account is accurate: the Introduction credits Cattell (1886) with the first demonstration that letters in words survive faster presentation than letters in random strings, and names the confound. It gives nothing about word spacing, unspaced text or sentence reading, and no premise in ARGUMENT_MAP.md or ruling D1 to D10 depends on its results.

Facet check: the facet's "read in part" status is consistent with what the paper contains. The one use is the Cattell sentence; the experiments are about single four-letter words in isolation, so the paper must not be cited for word-level processing in running text. It does support one narrow point for D6: word-level units are processed more efficiently than letter-by-letter, and the authors tie this to perceptual learning, not to any property of spacing.

## In conversation with
- `cattell1886time` — the first superiority demonstration and its decision-confound (Introduction).
- `reicher1969perceptual` — the two-alternative forced choice design that removes the confound.
- `wheeler1970processes` — follow-up that rules out alternative accounts and finds slower response times for words than for letters.
- `pelli2008uncrowded` — a different Pelli paper (the 2008 uncrowded-window article); the paper in this text is Pelli, Farell & Moore (2003), "The remarkable inefficiency of word recognition," which is not in the bib.
- `jordan2024reicher` — later critique of the Reicher-Wheeler paradigm; it postdates this paper.
- Leads not in the bib: Pelli, Farell & Moore (2003, *Nature*); Townsend & Nozawa (1995); Houpt & Townsend (2012); McClelland & Rumelhart (1981); Blaha (2010) thesis.

## Caution
Small samples (10 and 12), a student population, Courier or capital strings of four letters, no sentences or eye movements. Experiment 2's random-letter results rest on half the participants. The paper tests word versus letter efficiency, not spaces. This is the PMC author manuscript, not the typeset article, and page numbers of the journal are not given.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the PMC author-manuscript XML (PMC3877166, cards/houpt2014new.xml), stripped the tags, and matched the one in-source quotation (Massaro / Pelli sentence) exactly. Checked the numbers: 10 and 12 participants (8 F / 2 M and 10 F / 2 M, ages 19-34), 10 sessions of 45-60 min, 240 trials (after 40 practice), 80 ms and 100 ms exposures, Courier font, F(1,9) = 50.85, z = 7.27 / 22.9 / 36.7 / 45.9, p < .0025 (Bonferroni), t(10) = 0.773, p = .458, half of the Experiment 2 participants with too-low random-letter accuracy, and the Blaha (2010) one-week training remark. Also confirmed the Introduction's accounts of Cattell (1886), Reicher (1969), Wheeler (1970) and Pelli et al. (2003). Not checked: Appendix A and B tables.

**Findings:** No issues found. The two unmatched strings are the facet file's wording. The bib relation that pelli2008uncrowded is a different Pelli paper is consistent with the reference list (Pelli, Farell & Moore 2003 is the one cited).
