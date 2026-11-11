<!-- DRAFTED BY CLAUDE (Fable 5.2), from 11 Nov 2026. The log of calls made in run rr-2026-11-k under the authors' 'no stop' instruction: each with the alternative and the reason. The approved plan is at ~/.claude/plans/crystalline-tickling-reef.md. -->

# Decisions, run rr-2026-11-k

## What the authors decided (11 Nov)

- The run uses Fable 5.2 throughout, audits every claim in the paper, and widens the research beyond the existing package.
- Deliverables: an argument dossier, then DRAFT_v7, with no stop between them.
- Build the strongest argument for the host's duty and show where it departs from the 10 Nov 'middle position'.
- Open copies only; no library sign-in.

## Decisions I made

### K-D1 · 11 Nov · The design critique is adopted, and the claims were revised before the search
An independent agent critiqued the plan's argument and method while I wrote the set-up files. I adopted its main points and rewrote `CLAIMS_FIXED.md` as version 2 before any workstream search:

- **K7 is rebuilt.** Version 1 derived the reachable person from the guest's standing. A standing to demand creates no duty in the host to be reachable, so the inference failed in the same way the reviewers found v6's did. Version 2 derives it from the holder's own duty of oversight (P1–P4 to C), keeps the standing route as support only, and names a fallback.
- **K6 is weakened on purpose.** It no longer says a claim includes standing to demand 'by definition', since theories of directed duty disagree.
- **K3 concedes that the role does not bind by itself.** The role specifies content, trigger and holder; three external grounds bind. The run must produce a table of ground by hard case.
- **K8 is stated per duty.** The Occupiers' Liability Act 1957, s. 2(4)(b), already carded, lets an occupier discharge a duty by reasonable entrustment to a contractor, so 'the duty cannot be delegated' is false as a general statement of English law.
- **Three registers** (customary, moral, legal) are kept apart throughout.
- **K9** separates decisions before reception from decisions after it.

Alternative: keep version 1 and let the red team at stage 4 find these faults. Reason for changing now: an objection raised after the search can no longer direct the search.

This changes the argument and not the scope or the deliverables, so I did not stop to ask.

### K-D2 · 11 Nov · No separate red team at stage 0
The critique recommended one. The 11 Nov reviewer pack (eleven reports) and the critique itself already supply the objections, which are filed in `CLAIMS_FIXED.md`. The three-agent red team stays at stage 4, on the dossier.

### K-D3 · 11 Nov · The audit method is tested before it is used
`claims/CALIBRATION_SET.md` holds 24 sentences: 12 whose errors were confirmed and corrected on 11 Nov (in their uncorrected form) and 12 that the reviewer pack found sound. One auditor works through them blind, from the saved source texts only. **Thresholds, fixed before the result:** it must fault at least 10 of the 12 known-bad sentences for the right reason, and fault no more than 2 of the 12 known-good ones without a reason I accept on reading the source. If it fails, the brief is revised and the test repeated before the audit runs.

### K-D4 · 11 Nov · The law workstream is split in two
P4a covers the duties themselves (admission, reception, civil-law counterparts; K4, K5). P4b covers who holds them and what a channel requires (delegation, several firms, platforms, automated decisions, traders' reachability; K7, K8).

### K-D5 · 11 Nov · v6 is frozen for the audit
SHA-256 of `manuscript/DRAFT_v6.md` at the start of the audit: `8951cadf1fe32184a38a5b709a934bda06e3cf92d81bba449e876891d4b537e7`. v6 is not edited during this run; v7 is a new file.

### K-D6 · 11 Nov · Claim slugs
Eleven slugs for this run were added to `library/CLAIMS.md` (`k1-…` to `k9-…`, `novelty-neighbour`, `touchpoint-evidence`), so that new cards validate.

### K-D7 · 11 Nov · Depth of the audit follows what survives
The two theory sections will be rewritten, so their sources and inferences are audited in full and their wording is not. The other sections get the full row-by-row audit. v7's new sentences are audited afterwards by an agent that did not write them.

**K-D3, result (11 Nov).** The auditor's register is `claims/CALIBRATION_RESULT.md` (60 rows; about 440,000 tokens and 26 minutes). Scored against the key:

- **Known-bad, 12:** 10 faulted, each for the reason confirmed on 11 Nov. That meets the threshold.
  - Missed: the Thompson sentence, where two quoted formulas were each exact and together swap who owes whom.
  - Passed with a caution only: the Sandoval-Strausz sentence, whose fault lies in what the sentence before it implies. The test withheld the draft, so the item was not a fair one; the auditor did note that the liability is for goods.
  - Inside a faulted sentence, the Martin and Waldman clause was passed on the authors' summary line.
- **Known-good, 12:** none faulted; one marked unverifiable because the test did not supply the text for one of its two citations.

The brief is revised (version 1.1) for the three blind spots: a ninth mismatch class (combination), a rule to find empirical results in the results section, a rule to read each sentence in its paragraph, and a rule that a caution which changes the reader's understanding is a `partial`. It also gains a `not in source` verdict and a severity scale, which the auditor asked for. I did not repeat the test after these changes; the full audit's independent verifier re-checks every legal and theoretical row and a sample of the rest.

### K-D8 · 11 Nov · Ten auditors, not five
The calibration cost about 18,000 tokens a sentence. At that rate a batch of 60 sentences would exhaust one agent. The audit runs in ten batches of at most 34 sentences: the abstract and Introduction; 'The host's power' in two; 'Delegation and standing' in two; the opening of 'Assembled hosts' with 'The authority–answerability split'; 'Three conditions and six questions'; 'When a person must be reachable' with Table 1; 'Designing for interruptible hospitality' with Table 2; the Conclusion. The sections that survive into v7 go first.

### K-D9 · 11 Nov · Two readers added after the gate
The Tier 1 list is extended by two small reading tasks, each tied to one premise of K7.

- **R7, on knowledge.** The reader of the English delegation cases found that the occupier's and contractor-employer's duties turn on what the holder 'knows or has reason to suspect' (*Ferguson*; *Naylor*; *Maguire*), and suggested the form the paper's step should take: a host that removes every route by which a guest could tell it has put itself where the law's own trigger cannot operate. R7 tests whether the principle behind that (a duty that turns on knowledge cannot be met by arranging not to know) is in print, in philosophy (culpable ignorance, duties to inquire) and in law (wilful blindness, blind-eye knowledge), and how far it reaches. It also cards *Page v. Sloan*.
- **R8, on the empirical premise.** P4 says the guest's report is often the only timely signal and that correction needs a person with power in the single case. The planned evidence workstream (P6) had not run; R8 reads the open studies on complaint handling, forced self-service and frontline authority, and reports contrary evidence first.

P6 and P7 are not run as full workstreams. The claim audit showed that the paper's four cases are its weakest evidence, and the law reports carded in this run supply documented cases that can replace them (*Rasnick*, *Groh*, *R (DMA)*, with Xiang et al. and Petie et al.).

### K-D10 · 11 Nov · A wrong number in a commit message
The message of commit 7ad42b93 says the run produced 76 new cards. The count is **67 new cards and 6 upgraded** (332 cards in the library, 265 before the run). The message cannot be changed without rewriting pushed history, so the correction is recorded here.

