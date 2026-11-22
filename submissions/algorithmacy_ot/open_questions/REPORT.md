# Where algorithmacy can enter *Organization Theory*: report of run `ot-oq-2026-11`

> **[Written by Claude, the run's lead, 22 Nov 2026.]** This is the checkpoint for Gate 1. Read it before
> anything touches the manuscript. Fable traced every quotation and number in it to a run file; the trace
> is at the end. The plan is at `~/.claude/plans/ok-i-want-you-curried-pumpkin-of-5549facb-8130-42d5-8697-8054667dfe73.md`.

## The answer in brief

*Organization Theory* has one place where the algorithmacy paper answers a question its authors are asking
and keeps its definition intact: **Stark and Vanden Broeck's closing call, in "Principles of Algorithmic
Management" (2024), to study the communication field that goes with the platform form.** The paper enters
there in two moves. It supplies the participant's part of that field. It also amends the authors' claim
that the technologies "themselves become communication partners", using the triangle the authors draw
themselves. Two more entries hold, each at a cost: Hinds and von Krogh's question on team members who
"blindly follow guidance from the AI" (2024), and Justesen and Plesner's call to account for the
"unintended tasks" of digitalization (2024). All three critics ruled that each of the three holds only with
reframing, and none holds as written. No open question in the journal scores the top fit of 4.

The coordination frame explains the weak response. Coordination theory as such is nearly absent from the
journal: two articles in one volume ask about it, they do not cite each other, and nobody has asked about it
for two years. The coordination *problem*, though, is where the best-fitting question sits. Hinds and von
Krogh ask it about generative AI, not about coordination theory.

## What the run did

| Stage | What | Result |
|---|---|---|
| Corpus | Every item OT published, 4(1) 2023 to 7(3) 2026, of all types | 66 items, all read in full from the publisher's version |
| Records | 15 reader batches (Opus for Tier A, Sonnet for Tier B), 13 verifier batches (Opus), Fable's hand-check of all 66 | 684 entries: **605 open questions**, plus 79 the papers answer themselves |
| The compilation you asked for | `QUESTIONS.md` (by article) and `QUESTIONS.tsv` (table) | every question verbatim with its page; 637 of 684 quotations match the text exactly, and the other 47 differ only where the extraction broke a line or a page |
| Conversations | Two blind clusterings (Fable, Opus), reconciled by Fable | 54 conversations, 17 singletons (`synthesis/CONVERSATIONS.md`) |
| Fit | Two blind Opus scorers against `ALGORITHMACY_BRIEF.md`; Fable adjudicated every score of 2 or more | agreement κw = 0.878; final scores: 4 = none, 3 = 2, 2 = 25, 1 = 94, 0 = 484 |
| Pick-up | Forward citations of the asking articles (OpenAlex, OpenCitations); triage; full reads; gap search | 272 citing works triaged, 19 read and carded, 43 gap-search queries |
| Critics | Three Opus seats (the asker, a hostile OT reviewer, a rival-answer seat) plus a decoy question; Fable ruled | all three seats rejected the decoy; rulings in `critic/CRITIC.md` |

Every record, quotation and verdict is in `open_questions/`. Start with `INDEX.md`.

## Entry 1 (recommended): Stark and Vanden Broeck, "Out of Bounds", pp. 14–16

**The question.** "Also like them, further research should study the corresponding field of communication.
But whereas Merton and Lazarsfeld analyzed mass communication as the related, yet separate, field
corresponding to bureaucratic organization, in our case, organizational form and communication field are
conjoined." (OQ-stark2024-06, p. 15). The next paragraph sets an agenda of "genre forms, for example, the
genre forms of ratings and rankings" (OQ-stark2024-09, p. 16). It ends on the sentence the paper must
dispute: "This new sociality—when the partner with which we are communicating is an algorithm— will be a
critical component of further research on algorithmic management." (OQ-stark2024-07, p. 16).

**How algorithmacy answers.** The authors ground their call in Yates, who studied bureaucracy through its
written genres. The paper does for the platform form what Yates did for bureaucracy, from the person's
side. It classifies communicative capacities by what stands between two people: oracy for direct dyads,
literacy for dyads moderated by a text (Yates's orders and reports are such texts), and algorithmacy for
triads. It then says what a co-opted person must be able to do with a rating. In the same section the paper
contests the partner premise. It uses the authors' own triangle, "with the platform operator at the apex and
producers and users at the other corners" (p. 14), and their own case of colleagues behind the system
(p. 9).

**What the critics required.**
- Claim one component of the field, not the field. The askers "operate at the organizational level" (p. 2).
- Present the sequence as a classification by the form of the relation, not as a history laid over their
  Table 1.
- Restrict the setting to cases with a person on the far side. Most of the askers' p. 16 examples have none.
- Concede two things to others. The field-level joining of organization and communication belongs to the
  CCO school (Dion et al., 2025, in the corpus). The position between partner and channel is already taken:
  by the askers' triangle, and by Bujold et al. (2026), whose "technological intermediary" acts "on behalf of
  one party".

**Pick-up and gap.** This is the least taken-up question on the shortlist: 3 of 127 works citing Stark and
Vanden Broeck touched it, and none answered it. The gap search found no classification of capacities by the
form of the relation. It did find sequences by medium: Emigh (2024) gives orality, literacy, "digitality";
Heyd (2021) gives "tertiary orality". A book by Gloy (2025) is known only through a review. The paper's
claim is therefore its *criterion*, not the three-step sequence.

**What would move in each version** (moves only; the wording stays yours):
- *ASM* moves least. Open the introduction on Stark and Vanden Broeck's call, so that oracy → literacy →
  algorithmacy arrives as the answer to it. Move "the co-opted person's side" to the front of the
  contributions. ASM's "dyad dilemma" becomes the amendment of the partner premise.
- *GDOC.* Move the Okhuysen and Bechky frame out of the introduction and into the section that grounds the
  three parts. Set the gap sentence (§2 ¶3) against this call. Lead with the first contribution (linking
  platform co-optation to everyday practice).
- *PAPER.* Replace the opening on displacement with the platform form and its communication field. The gap
  in §2 ¶1 already has this shape.

**Risk.** It rests on one article, a call rather than a question, 29 months old. Three of the October
panel's objections land hardest here: the lopsided triad (1), Simmel's profiting third (3), and the name
(6), because under a relation-form criterion the third member needs no algorithm. One likely engagement,
Hall and Kuhn (2025), is unread.

## Entry 2: Hinds and von Krogh, "Team coordination", pp. 7–8

**The question.** "With the introduction of GenAI, might emergent interdependence be disrupted because team
members blindly follow guidance from the AI?" (OQ-hinds2024-04, p. 7), joined to "We need theorizing that
captures what shapes team participants' dynamic relations with AI to coordinate their work." (OQ-hinds2024-25,
p. 8). It is the only explicit question among the three entries, and one of the run's two questions at fit 3.

**How algorithmacy answers.** Blind following is the first failure mode: the member treats the system as the
counterpart, and the colleague drops from view. The three parts describe the member who does not collapse the
triad. Keeping track matches the authors' own "progressive encapsulation" (pp. 5–6).

**What the critics required.** The paper answers only the first horn of the question. The second, that
emergent interdependence becomes "less necessary", lies outside a construct that presupposes interdependent
work. It must state the step from members' abilities to the team's property. It must specify the ability by
what a member does, not by its outcome, because "disrupted where members lack the ability" is circular. And
it must pay one of two costs openly. Either it widens "binding" to guidance members come to follow, or it
anchors in the authors' evaluating cases: GenAI "determining job assignments or pay increases" (p. 4), and
brokerage under surveillance (p. 9).

**Pick-up and gap.** 8 triage rows and 4 cards. Rivals work at team level, not the individual's: Steiger et
al.'s "delegation calibration" and Yuh et al.'s team competence. The gap search found no individual capacity
that keeps the AI-mediated colleague in view as the remedy.

**What would move.** *GDOC* is closest in vocabulary. Its setting moves from platform work to teams inside
organizations, and its agenda item on generative AI moves into the argument. *ASM* makes generative AI a main
setting, and the scope change lands on "bindingness". *PAPER* already opens on generative AI; it would move
from displaced institutions to absorbed coordination among colleagues.

**Risk.** One calibrated critic (the hostile reviewer) called it shoehorned. Fable did not follow that verdict,
with reasons in `critic/CRITIC.md`. The cost to the definition is real.

## Entry 3: Justesen and Plesner, "Future research", p. 22

**The question.** "Finally, we could account more fully for the emotional costs, mental loads and unintended
tasks associated with digitalization." (OQ-justesen2024-13, p. 22). The same paragraph says this work is
"neither systematically analysed nor theorized".

**How algorithmacy answers.** It treats the three parts as tasks the arrangement imposes without
acknowledging them, a case of the authors' "compensating work" in settings that have a counterpart.

**What the critics required.** A claim the brief does not hold: that exercising the ability is unrecognized
work. A reversal on "pacifying the algorithm". The authors file it as invisible emotional labour (p. 15, citing
Bucher et al.), and the brief files it as a failure mode. The Hinds leg of this candidate is shoehorned.

**Risk.** The askers want empirical accounts. Algorithmacy offers a capacity and "measures no one".

## The coordination finding

The cluster on coordination (R49 in `synthesis/CONVERSATIONS.md`) has 2 theory articles and 1 commentary
question, all in volume 5. It has no citation edges between askers, no editorial signal, and no ask since
29 Oct 2024. Its one coordination theorist, Räcker et al. (2024), theorizes physical space only and names no
algorithm. Of the 66 records, one names Okhuysen and Bechky (2009) as an interlocutor. Yet the same cluster
holds the run's other fit-3 question and six questions at fit 2, mostly Hinds and von Krogh's. So **keep
coordination as the problem, and drop coordination theory as the audience.**

## What algorithmacy can claim, and what it cannot

**What it can claim.** I found no work that names an individual's ability to do interdependent work with
another person through an intermediary that evaluates both, or that classifies communicative capacities by
the form of the relation. Sources searched: the 66 OT items; the 19 carded citing works; and OpenAlex and
Consensus searches for shortlist candidates 1–3 on 22 Nov 2026 (Scholar Gateway was unavailable).
Specifying intent so that it survives the intermediary and reaches the counterpart has no neighbour in the
carded works. Its older name outside them is audience design.

**What it cannot claim.** On this evidence the paper cannot claim:
- the triad, which belongs to Stark and Vanden Broeck, and to Pfadenhauer and Kirschner (2017);
- the third position between partner and channel (Bujold et al., 2026);
- that the parts are unnamed. Interpreting and keeping track appear as conditions in Bujold et al. (pp. 11,
  15) and as "interpreters" in Choroszewicz (2026);
- that the intermediary *binds* both parties. No text read shows it. Evaluation of both appears in Stark
  and Vanden Broeck (pp. 4, 14). Binding runs one way in Zelles et al. (2026): "We can rate the riders, and
  they can rate the drivers", yet only the driver is suspended.

## Flags for you (reported, not fixed)

1. **"Evaluates and binds them both."** This phrase is in all three versions. The run found evaluation of
   both parties in the sources, and binding of one only.
2. **"Pacifying the algorithm."** GDOC §4.3 pairs it with ignoring the counterpart. In Justesen and Plesner's
   report of Bucher et al. (2021), the client is part of the effort. Check the pairing against Bucher et al.
3. **Emigh (2024) and Heyd (2021)** already run an orality → literacy → digital sequence by medium. Cite and
   distinguish them.
4. **APC.** `JOURNAL_SPEC.md` gives US$1,000. OpenAlex lists OT with an APC of 0 and DOAJ status. Check the
   SAGE page before budgeting.
5. **Age of the fit.** All 27 questions at fit 2 or 3 come from articles published Oct 2023 – Oct 2024.
   Nothing in volumes 6–7 reaches 2. The conversation the paper joins is about two years old.

## Reads owed before any of this enters a draft

Hall and Kuhn (2025, QROM; closed); Gloy (2025); Curchod et al. (2020) and S.G. and Lyytinen (2026) in full;
Snyder (2025); Zientara (2026, SAGE 403). Two pick-up cards rest on abstracts (akhil2026, ivarsson2026).

## Deviations from the plan

- **Corpus.** The plan expected 51–57 items. The author's Gate 0 ruling added 4(1)–(3), so the corpus became
  66, with no OnlineFirst items after 21 Sep 2026.
- **Pilot rule.** The rule "Ernst must state none" over-read the structure map. Ernst's eight closing calls
  are genuine.
- **Text layers.** The first extraction set columns side by side. All layers were regenerated in reading
  order before the main reading.
- **Fable's clustering.** It saw 12 lines of hand-check fit notes after its clustering was fixed (logged in
  `DECISIONS.md`). Fable's reconciliation was made with the brief and fit scores open.
- **Unread works.** Four pick-up works could not be fetched (bot-checks, closed access).
- **Approvals.** The author was away. The brief was treated as approved under the author's instruction, and
  the lead ruled every stage query in `DECISIONS.md`.

## Gate 1: your decision

Choose one: Entry 1, Entry 2, Entry 3, a combination (Entries 1 and 2 can share a paper: the field call frames
it, and the team case supplies a setting outside gig work), none, or a deeper read. Nothing in `manuscript/`
has been touched.

## Trace

[Filled by Fable's trace pass: each quotation and number above, with the run file and locator that supports
it.]
