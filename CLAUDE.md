# Writing style (applies to all prose in this repo)

Write like Thomas Nagel in "What Is It Like to Be a Bat?": plain, blunt, concrete. The
difficulty belongs in the ideas, not the sentences. State a claim; do not perform the act of
stating it.

The drafts have a recognizable machine cadence. Three constructions produce most of it, and
they are the priority. Cut them on sight.

## The three priority tics

**1. The antithesis machine.** The drafts define almost everything by what it is not, then
pivot. This is the dominant sentence engine and it must be cut by roughly two-thirds. The
forms it takes:
- `, not X` — "a property of the coding, not a discovery that a market and a platform are alike."
- `X rather than Y` — "reports what the model yields rather than asserting it."
- `It is not X. It is Y.` — "It is not, and the instrument is needed because it is not."
- `is not a / the / an …` — "This is not a thought experiment. It is the documented structure."

Default to stating the positive claim alone. Use a contrast only when the wrong alternative
is one a reader would actually reach for, and then at most once per paragraph. If a paragraph
has two of these, one is decoration — delete it.

**2. Self-narrating honesty and rigor.** The prose constantly announces its own care instead
of being careful. Cut every instance. Offenders seen in the drafts: "stated plainly," "said
plainly," "the blunt version belongs here," "not waved past," "names its load-bearing
decisions rather than hiding them," "one honest qualifier belongs here," "stating it honestly
matters more than stating it strongly," "the status is stated plainly," "and the dissertation
says so," "precision about what it can say marks the boundary." State the limitation. Do not
narrate the virtue of stating it.

**3. The mechanized punchy opener.** A short blunt opener is good once; as the shape of nearly
every paragraph it becomes a metronome ("The level is wrong." "Cost is not an issue." "The
exhibit is not a one-off."). Vary how paragraphs begin. Let some open on the long sentence
that carries the idea.

## Rules
1. **No first person.** No "I," no "we." The subject is the paper, the model, the section, or
   the thing itself, with an active verb: "Paper 2 shows," "The model classifies."
2. Plain, ordinary words. Concrete examples over abstract nouns.
3. Declarative sentences: subject, verb, object. Vary length. Keep long sentences clear by
   coordinating clauses, not by stacking subordinate clauses ahead of the verb. No periodic
   sentences that defer the verb behind several clauses.
4. Say each point once, in the place it belongs. Do not restate a conclusion in near-identical
   words across sections. The "seat-blind / property of the coding" point, the "program the
   dissertation opens," and the limitation recaps are the repeat offenders: one clean statement
   each, then refer back, do not re-argue.
5. Em-dashes rare: at most one per paragraph, usually none. No em-dash pile-ups. No semicolon
   splices.
6. State uncertainty flatly: "this is not yet shown," "the result is unclear."
7. Rhetorical triads ("a name, a procedure, and a placement"; "name, formalize, grade") only
   when each member carries distinct content. Not for cadence.
8. One idea per sentence where possible.

## Banned openers
"We want to," "The honest reader," "It is worth," "Crucially," "Precisely," "Importantly,"
"Note that," "Stated plainly," "To be clear."

## Before / after
- Mannered: "Reaching into another discipline for a formal model is not a novelty in
  organizational research; it is one of the field's recurring ways of building theory, and
  naming the tradition is the first step toward claiming a place in it."
- Plain: "Organization theory borrows formal models from other fields. It always has.
  Population biology gave it organizational ecology. Microeconomics gave it transaction-cost
  theory. Integrated information is the next thing it borrows, and this paper claims its
  place in that line."

## Self-check (run before showing prose)
Scan the new prose and count, per ~1,000 words:
- `, not` + ` rather than ` + `is not a/the/an` + `It is not/does not` → target well under 5
  combined (the drafts ran ~7). If a paragraph has more than one, cut to one.
- Self-honesty phrases (list above) → target zero.
- Paragraphs opening with a fragment under six words → at most one in three.
Fix violations before showing. Flag any you deliberately kept and why.

---

# Repository layout & git pushes (IMPORTANT — applies every session)

This tree holds **two separate git repositories**. See `REPO_LAYOUT.md` for the full
explanation. The short version, which must be respected on every git operation:

- **`dissertation/`** is its own **nested, private** repo (`dissertation/.git`) whose
  remote is `github.com/rogerSuperBuilderAlpha/algorithmacy-dissertation` (PRIVATE).
  It is gitignored by the outer repo.
- **Everything else** belongs to the outer repo `algorithmacy-lab`, remote
  `github.com/rogerSuperBuilderAlpha/algorithmacy-lab`.

Git uses the nearest enclosing `.git`, so **the directory a command runs from decides
the repo and remote** — not intent. Before any commit or push:

1. Run `git rev-parse --show-toplevel` and `git remote -v` to confirm which repo/remote.
2. Dissertation work pushes to `algorithmacy-dissertation`; PyPhi/code work pushes to
   `algorithmacy-lab`. Never mix them.
3. State the target remote to the user before pushing.
4. Never `git add -f dissertation/` in the outer repo, and never re-`git init` either tree.
