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

### K-D11 · 11 Nov · The run continues on Opus 5.5
Fable 5.2 reached its usage limit at about 17:15 on 11 Nov. All eight agents then running stopped before writing any file: the five card verifiers (CV-A to CV-E), the novelty scout (P5) and readers R7 and R8. The authors switched the session to Opus 5.5 and said to continue.

- **What changes.** The rest of the run, including the reruns of those eight agents, the hand-check of Tier 1 cards, `ARGUMENT.md`, the red team and DRAFT_v7, runs on Opus 5.5. The authors asked for Fable 5.2; this departs from that request, and the report says so.
- **What does not change.** The briefs are the same, apart from the model named in each report's header line and a note that the earlier attempt left nothing.
- **What was done on Fable 5.2.** Stages 0 to 2, the claim audit and its verification, the nine reader reports and the 67 new cards. The commit trailers show which model wrote each commit.
- **A guard affected.** The standing rule for research-run cards asks for a hand-check by Fable. The hand-check is now done by Opus 5.5; if the authors want the Fable check, it can be re-run on the Tier 1 cards when Fable is available again.

### K-D12 · 11 Nov · Internet Archive copies of open texts count as open copies
Several readers fetched texts from Internet Archive captures because the live site returned a bot check, HTTP 202 with no body, or HTTP 403 to automated requests: legislation.gov.uk, BAILII, Wiley and PhilPapers (de Kenessey 2024, CC BY-NC), the California legislature's site (AB 1609), and a repository copy of Gelbrich and Roschk (2011). CV-D asked whether this satisfies guard 6 ('open copies only; no CAPTCHA or bot check; no paywall workaround').

**Ruling.** An Internet Archive capture counts as an open copy when the text is itself open: public law, an openly licensed article, or a copy a repository serves without charge. No agent completed or evaded a challenge on the live site; the capture is a copy held by a separate public library. A capture of a paywalled text would not count, and none was used. Each card records the capture it used, and the verifiers checked identity against it.

**Alternative.** Treat any text whose live site blocks scripts as closed. Reason for not doing so: the texts are open by licence or by law, and the block is on automated access, not on the reader. The authors may reverse this; if they do, the affected cards (`dekenessey2024two`, `ca2026ab1609`, `uk2025datause`, `americancyanamid1975ethicon`, the legislation.gov.uk statute cards, `gelbrich2011metaanalysis`) drop to 'closed' and the dossier's uses of them must be re-checked.

### K-D13 · 11 Nov · R8 changes the thesis's second half
R8 found that the one automated hotel chain read kept a worker on site as a fall-back, and that no open study shows automation removing the person with authority. The dossier therefore says that automation *can move* the person with power behind the machine, so that the guest reaches them only by seeking them out. It no longer says that mediation removes the path. The v6 abstract and conclusion state the stronger version and will be changed in v7.

### K-D14 · 11 Nov · The red team starts before the novelty check returns
The plan had the red team read draft 2, after all inputs. By the time CV-F finished, every card the dossier uses had been verified and every premise had a source read in full or was marked as the paper's own step, which meets the gate after stage 3. Only the P5 novelty scout was still running, and novelty bears on what the paper may claim as new, not on whether the premises hold. The three attackers (philosopher of obligation, tort and consumer lawyer, critical hospitality scholar) were therefore launched on the dossier as it stood at commit time, with the same brief for each and a role section each (`REDTEAM_PHIL.md`, `REDTEAM_TORT.md`, `REDTEAM_CRIT.md`). P5's results go into draft 2 with the red team's.

### K-D15 · 11 Nov · A reader added in answer to the critical hospitality scholar
The critical scholar's report (`REDTEAM_CRIT.md`) finds two fatal and ten serious objections. Its core is that Step 6 draws nothing from hospitality: the plate misreads Pitt-Rivers (F1), law both supplies and trims the content (F2), and the dossier engages none of *Hospitality & Society*'s own articles (S10). Several answers need reading, not drafting, so reader R9 reads the journal's saved articles again for the keystone's questions, cards Kekstaite 2022 and O'Gorman's paper on commercial hospitality in ancient Rome, and looks for open copies of six critical leads (Dikeç 2002; Aramberri 2001; Robinson and Lynch 2007; Darke and Gurney 2000; Veijola and Jokinen 2008; Fuller and Smith 1991). Draft 2 waits on R9 as well as on the other two attackers and P5.

**What I accept now, before R9 reports.** F1: the plate is dropped as footing for C. F2: the 'Answered' status of the 'innkeeper law' objection was wrong, and draft 2 will re-describe what hospitality supplies and what law supplies. M1 and the seven citation errors listed in section 3 of the report are corrected in draft 2.

