# A code-review gate

A stipulated description of a software team's merge process. It is not field data. Paragraph numbers
are locators.

**¶1.** An author opens a change. A continuous-integration gate runs the tests on it. A maintainer
decides whether to approve the merge.

**¶2.** The repository's branch-protection rule says: "The CI check runs on every push to the change."

**¶3.** The contributing guide says: "Maintainers approve only changes whose CI check is green."

**¶4.** Authors revise in response to both: "I push a fix when CI fails or when the maintainer asks
for changes, and I stop when both are satisfied."

**¶5.** Some maintainers admit: "On small changes I just read the diff and approve; I don't wait for
CI."
