# Maintainers

Maintainers are this project's review board. They are its reviewers and editors: the people who run the
review in [`PUBLISHING.md`](PUBLISHING.md) on incoming submissions, approve pull requests, and sign off in
public under their own names. A submission becomes part of the record when a maintainer has reproduced its
numbers, audited its pre-commitment, judged its argument, and approved it. The role carries the authority
to admit work and the obligation to hold it to the standard.

## What a maintainer does

- **Reviews submissions** in their area, working the four passes in order: reproduce the numbers, audit
  the pre-commitment, judge the argument, check the prose. The first two are mechanical and gate the rest.
- **Approves or requests changes** as a signed GitHub review on the pull request. An approval is a public
  vouch that the work meets the standard.
- **Upholds the three commitments** every submission owes: every number reproduces from a committed
  script, claims are fixed before computing, and scope is stated. A maintainer who would not stake their
  name on a result does not approve it.
- **Files corrections** when a published result stops reproducing, and reviews others' corrections fairly.
- **Discloses conflicts.** A maintainer who authored or has a stake in a submission does not review it.

## The standard a maintainer upholds

The full standard and the four-pass review are in [`PUBLISHING.md`](PUBLISHING.md). The house style for all
prose is in [`CLAUDE.md`](CLAUDE.md). A maintainer reviews against these, not against taste.

## Current maintainers

- **rogerSuperBuilderAlpha** — founding maintainer and repository owner.

## How authority grows

While the board has one maintainer, that maintainer merges as a repository admin, because GitHub does not
let an author approve their own pull request. When a second maintainer is admitted, admin exemption is
turned off, so every pull request, the owner's included, needs an approving review. The number of required
approvals rises as the board grows. The aim is a review process that belongs to a community rather than to
one person.

## How to apply

Applying is itself a pull request, reviewed in the open like any other contribution.

1. **Fork** the repository and create a branch off `maintainer-applications`.
2. **Copy** [`applications/TEMPLATE.md`](applications/TEMPLATE.md) to `applications/<your-github-handle>.md`
   and fill it in.
3. **Open a pull request into the `maintainer-applications` branch.**
4. The current maintainers review the application and decide. A merge accepts it: the applicant is added
   to the roster above, granted review access, and folded into the authority ramp.

## What an application shows

An application is judged on whether the person can run the review to the standard. Two things establish
that, and an application leads with whichever it has.

- **A track record here.** Merged submissions, careful reviews left on other people's pull requests, and
  corrections filed honestly. Link them.
- **A sample review.** An applicant new to the project picks an existing paper or probe — the Thompson
  study under [`org_frontier/questions/q43_thompson_interdependence/`](org_frontier/questions/q43_thompson_interdependence/)
  is a good target — and writes the four-pass review of it: reproduce the numbers, audit the
  pre-commitment, judge the argument, check the prose. The sample review shows the work better than a
  résumé does.

Relevant expertise helps and is worth stating: integrated information and PyPhi, organization and
coordination theory, research design and statistics, or editing prose to the house style. Expertise is not
a substitute for showing the review.
