---
citekey: baum2026constitutive
title: "Constitutive vs. Corrective: A Causal Taxonomy of Human Runtime Involvement in AI Systems"
authors: "Baum, Kevin and Laux, Johann"
year: 2026
doi: 10.1007/978-3-032-41269-0_8
venue: "Lecture Notes in Computer Science, Bridging the Gap Between AI and Reality (Springer), pp. 115-130"
cluster: mediation-sovereignty
status: held
role: evidence
used_by_sections: [5, 7, 9]
claims: [limits-and-agenda, institutional-not-trainable]
read_depth: full-text
verified: crossref-verified
verified_date: 2026-11-10
source_basis: "Crossref record 10.1007/978-3-032-41269-0_8 fetched 2026-11-10 (LNCS chapter, pp. 115-130, published online 13 Oct 2026, CC BY 4.0; Crossref gives the print date as 2027, so decide which year to cite). The Springer PDF returned a bot challenge, so the full text was read from arXiv 2603.19213v2 (20 Aug 2026, 15 pp.), the version OpenAlex links to the chapter. Locators are arXiv v2 PDF pages and section numbers; the version of record was not compared, so pagination and wording may differ. Copy at manuscript/revision_2026-11/research/sources/baum2026constitutive/."
generated_run: rr-2026-11-h
flags: []
hold_rationale: "Proposed as the one H5 entry (cap 1). It supplies the criterion R2.5a asks for: whether a human can intervene before a decision takes effect, rather than how fast review comes. The authors decide admission."
---

Section numbers are the outline numbering (rr-2026-11-h): §5 test, §7 interruptibility, §9 boundary conditions.

## Summary

A conceptual taxonomy of human involvement at runtime. Human-in-the-loop (HITL) is *constitutive*: no
output without the human. Human-on-the-loop (HOTL) is *corrective*: the system runs by default and the
human can prevent, modify or override. HOTL has three temporal modes (synchronous, asynchronous,
anticipatory), and only the synchronous mode can change the individual decision at runtime ("can become
outcome-HITL for a given deployer-runtime decision", p. 6). "The decision a person is subject to" is
H5's gloss; the taxonomy does not discuss the person affected.
"Human oversight" in the EU AI Act is read as a normative form of HOTL that needs preparation, capacity
and authority, not mere presence.

## Key facts / verified quotes with loci

- Gate against switch: "an approval requirement is a gate (HITL), a veto window is a switch (HOTL)" (p. 3, §2) [full-text]
- HITL definition: a human is HITL "if and only if—and if, then because—without H’s contribution, no causal chain manifestation of P can effectively generate a decision output." (p. 4, Def. 1) [full-text]
- Synchronous mode: "A human monitors operations in real-time and can intervene immediately." (p. 6, §2.3) [full-text]
- The criterion is timing relative to effect, not elapsed time: periodic review before outputs take effect is "synchronous with latency: the distinguishing feature is not elapsed time but whether intervention can occur before the token output becomes effective." (p. 6, §2.3) [full-text]
- "Only synchronous HOTL can become outcome-HITL for a given deployer-runtime decision" (p. 6, §2.3); "asynchronous HOTL intervenes after the decision has been made, shaping future iterations; anticipatory HOTL shapes the decision space before deployment." (p. 7, §2.3) [full-text]
- Decisions too fast for a person: the vehicle "executes emergency braking autonomously; here, the human is not meaningfully a synchronous HOTL: the intervention happens too fast for real-time correction"; adjusting the braking parameters in advance "constitutes anticipatory HOTL" (p. 8, §2.3, "Boundary Cases and Process Individuation"; the paragraph opens on p. 7, the quoted words are all on p. 8) [full-text]
- Asynchronous review does not reach the decision at hand: "the intervention targets future system behavior (e.g., by adjusting parameters or triggering retraining) rather than the decision currently being made" (p. 6, §2.3) (added by Fable, rr-2026-11-h) [full-text]
- Advance rules count as oversight only if they can be revised: "A choice that is not revisitable within the system's life-cycle is design, not corrective involvement." (p. 6, n. 9) (added by Fable, rr-2026-11-h) [full-text]
- A present human is not thereby an overseer: "A human who must click 'approve' for every decision (HITL) but rubberstamps without genuine judgment does not thereby become an overseer." (p. 12, §4.1) (added by Fable, rr-2026-11-h) [full-text]
- Presence is not oversight: "Satisfying the descriptive conditions (e.g., being in a HOTL configuration) is typically necessary but not sufficient for meeting normative demands"; humans need "the capacities, information, and authority to make that position meaningful and effective" (p. 2, §1) [full-text]
- GDPR against AI Act: a HOTL configuration under Art. 14 AI Act "may thus provide stronger protection than the HITL configuration that the wording in Article 22 GDPR prima facie seems to demand" (p. 11, §4.1) [full-text]
- Human overseer: "systematically prepared for and is in a position to consciously monitor operations and intervene, if necessary, in order to substantially reduce AI-induced risks" (p. 12, Def. 3) [full-text]
- Cites Parasuraman et al. (2000) and Sterz et al. (2024), both already cards (pp. 3, 14-15) [full-text]

## Critical notes & threats

- Conceptual, with no data; it is about system architecture, not about the person affected. The paper's move from "the deployer can intervene" to "the guest can reach someone who will" is the authors' own.
- Examples are vehicles, surgery, ICU, warehouses and criminal justice. Nothing on hospitality or commercial service.
- arXiv v2 read, not the LNCS version of record; check pages and quotes before citing.
- The taxonomy has no slot for a later appeal that reverses the same person's outcome (a refund, a re-admission). Its asynchronous mode shapes "future iterations" (p. 7). Mapping "a guest's later appeal" onto asynchronous HOTL is H5's analogy, not the source's. [added by Fable, rr-2026-11-h]
- Its normative layer rests on Sterz et al. (2024); the two can be cited together, and Sterz already carries the "authority to influence" definition (card `sterz2024effectiveness`).

## Where it enters the manuscript

§5 and §9 (boundary conditions, R2.5a): the test for which decisions need immediate interruptibility
becomes, in H5's formulation (not a quotation), whether a person with authority can intervene before the decision takes effect on the guest; the source's own criterion is "whether intervention can occur before the token output becomes effective" (p. 6).
§7: separates three things the outline runs together, a reachable person at the moment (synchronous), a
later appeal that changes future practice (asynchronous), and rules the host sets in advance for decisions
too fast for anyone (anticipatory, pp. 6, 8; revisable rules only, p. 6 n. 9). That last class answers R3.9 (authority is constrained) without
dropping accountability.

## Which reviewer point(s) it answers

R2.5a (which decisions need immediate interruptibility); R3.7 (technology takes many forms: the
taxonomy distinguishes configurations); in part R3.9.

New card in rr-2026-11-h (2026-11-10): full text read from arXiv v2.
Corrected in rr-2026-11-h after VERIFY_H_v1/v2 (2026-11-10): recorded the 2027 print date beside the 2026 online date; all quotations remain verified against arXiv v2 only.

Fable-checked rr-2026-11-h (2026-11-10): verifier notes accepted; the applied fix (2027 print date recorded) confirmed against the saved Crossref record; all quotations re-matched to arXiv v2 and read in context (pp. 2-8, 11-12). Changed: braking quotation relocated from pp. 7-8 to p. 8; the proposed test in Where-it-enters was set in quotation marks with a page locator and is now marked as H5's wording; "the decision a person is subject to" marked as H5's gloss; three located quotations added (p. 6, p. 6 n. 9, p. 12) and a note that a guest's later appeal is not the source's asynchronous mode. LNCS version of record still unread.

Upgraded in rr-2026-11-h (debts), 2026-11-10: version of record still unread; recorded as blocked. Unpaywall lists the Springer chapter PDF as open (hybrid, publishedVersion), but both the chapter page and the PDF returned a 'Client Challenge' bot page to curl, WebFetch was redirected to idp.springer.com, and the PhilPapers copy (BAUCVC-2) returned 403. The Chrome browser route was unavailable (no connected browser). Locators remain arXiv v2 pages; pagination and wording against LNCS pp. 115-130 are unchecked. Cite the chapter's pages only after someone opens the Springer PDF in a browser.
