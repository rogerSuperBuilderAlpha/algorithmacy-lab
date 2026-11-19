# Insurance claim adjudication: who decides a claim?

A stipulated description of five routing designs an insurer could use, adapted from a question a
contributor ran through the lab's protocol. It is not field data. Paragraph numbers are locators.

**¶1.** A claimant files a claim. An auto-adjudication engine screens it. A human adjuster may review
it. Each party's state is one bit: the claimant is pursuing or paid (C), the engine approves or flags
(E), the adjuster acts or does not (A).

**¶2.** Design 1, the pipe. "The engine forwards every claim to the adjuster; the adjuster's decision
goes back to the claimant." The engine reads the claimant, the adjuster reads the engine, and the
claimant reads the adjuster.

**¶3.** Design 2, threshold auto-approval. "Small claims are approved automatically; the adjuster
reviews only claims the engine flags." The claimant is paid when the engine approves and the adjuster
has not intervened; the adjuster acts when the engine flags a claim the claimant is pursuing.

**¶4.** Design 3, the fraud-flag loop with override learning. "The engine flags claims for the adjuster
and retrains on the adjuster's overrides." The engine's flag reads both the claim and the adjuster.

**¶5.** Design 4, the same loop without learning. "The engine no longer retrains on overrides."

**¶6.** Design 5, the frozen claimant. "The claimant is not told the outcome until the file closes."
The claimant's state no longer reads the decision.
