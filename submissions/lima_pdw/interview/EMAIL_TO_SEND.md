# Email to send — copy from the block below

## Before you send: three things

**1. The harness is not on `main` yet.** These files are written to disk but uncommitted — a safety
check blocked git partway through the session. Until you commit, push, and merge, the link in the
email either 404s or shows an older version of the consent text. Run:

```
cd /Users/ludwitt/iit-playground/pyphi-experiments/.claude/worktrees/lima-manuscript-review
git add submissions/lima_pdw/interview
git commit -m "Interview harness: formal invitation, participant information, response access"
git push origin worktree-lima-manuscript-review
```

Then merge to `main`, and confirm the link below actually loads before sending anything.

~~**2. Fill the IRB line.**~~ **Done, 18 August 2026**, from the determination letter: IRB #260511078,
exempt under 45 CFR 46.102(e)(2)(ii), 11 May 2026, Bentley University IRB#1 FWA00007335, Chair
Tony Kiszewski. Present in `CONSENT.md`, `INVITATION.md` and the email body below.

*One thing to check against your own records, not a blocker:* the letter grants exemption "unless
there is a substantial change to the documents specified above, or to your planned protocol," and
asks for a Research Progress & Review Form if the study changes. If the agent-run interviews were
part of what you submitted, nothing follows. If they postdate it, that form is the mechanism the
letter names.

~~**3. Deploy the intake endpoint.**~~ **Done, 18 August 2026.** Live at
`https://us-central1-pitch-rise.cloudfunctions.net/intake`, wired into `AGENT.md`, and smoke-tested
end to end: a file marked `reviewed_by_human: true` returned `201` and landed in the bucket; one
marked `false` was refused with `422`. The test object was deleted; the bucket is empty.

## Who to send it to

Everyone who was part of these programmes — participants, instructors, operations staff, and partner
organizations. The harness asks which they were at the start and runs the matching interview.

The email below is written for the operational side. For participants, swap the "Why you" paragraph
for something like: *"You took part in one of these programmes, and the study is about what the
review process was like from where you sat — which is the part no design document records."*

---

## The email

**Subject:** Invitation to participate in research on AI engineering cohort programs

---

Dear [name],

I am writing to invite you to take part in a research study. You are receiving this because you
helped run one of the cohort programs it concerns — GauntleTT in Trinidad and Tobago, the Cursor
Boston cohort, or the Hult cohort program.

**Who is conducting this.** Roger B. Hunt III, doctoral candidate in Organizational Theory at Bentley
University (rhunt@bentley.edu), under the supervision of the Bentley faculty named in the study
record. The work forms part of a doctoral dissertation and a paper prepared for a Paper Development
Workshop convened by *Organization Studies* and *Organization Theory* at Universidad de Piura, Lima,
in October 2026.

**What the study is about.** How coordination works in programs where participants submit work to a
review process — how people determine what a review expects of them, how they convey their intent
through the channels a system provides, and how they learn that expectations have changed. The study
examines the programs as organizational arrangements. It does not evaluate the performance of any
individual.

**Why you.** You saw these programs from the operational side. The published record documents how
they were designed; it does not document how they ran.

**What participation involves.** A structured interview of approximately twenty minutes, which you
complete on your own schedule. Rather than scheduling a call, the interview runs through a text-based
assistant in your own editor — you open a link, tell the assistant to begin, and answer in your own
words. Questions cover your role, how work was reviewed, how changes were communicated, what
participants asked about, and what happened when someone believed a decision was wrong.

**Voluntary participation.** Taking part is entirely voluntary. You may decline without giving a
reason, skip any question, and stop at any point. Because responses are submitted anonymously, no
record is kept of who was invited and who took part, and I will not know whether you participated.
Your decision has no bearing on your role, your standing, or any working relationship.

**Anonymity, and its limits.** The interview removes identifying information as it is written —
names, usernames, organizations, locations and exact dates are replaced before you see the text. You
then review the file and may edit or delete any part of it before submitting. Submission requires no
name, email or account.

You should know the limit of this. These are small programs, and a detail that would identify no one
in a large organization may identify a specific person in a cohort of thirty. The removal process is
careful; it is not a guarantee. You will be asked to review the file with that in mind before you
send it.

**How the material is used and stored.** Submitted files are held in access-controlled cloud storage
and, for analysis, in a private repository. They are not published, not shared outside the research
team, and not placed in any public repository. Findings appear as a written account of how these
programs operated. **No response is published as a quotation attributed to a person.** Files are
retained for the standard period following completion of the dissertation and then deleted.

**Risks and benefits.** The foreseeable risk is the residual identifiability described above. There is
no direct benefit to you. The study aims to produce a more accurate account of how programs of this
kind work than the design documents alone can support.

**Withdrawal.** You may withdraw at any point before submitting. After submission, withdrawal is not
possible: nothing links a file to the person who sent it, so there is no way to locate and remove it.
This is a consequence of the anonymity described above, and it is why the review step before
submission matters.

**Approval.** This study has been reviewed by the Bentley University Institutional Review Board and
determined exempt from further review under 45 CFR 46.102(e)(2)(ii) — IRB #260511078, 11 May 2026
(Bentley University IRB#1, FWA00007335).

**Questions.** About the study, write to me at rhunt@bentley.edu. About your rights as a research
participant, or anything you would rather not raise with me directly: Tony Kiszewski, Chair,
Institutional Review Board, Bentley University, 175 Forest Street, Waltham, Massachusetts 02452,
referencing IRB #260511078.

**To take part.** Open the following link and follow the instructions there:

https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/submissions/lima_pdw/interview

Open that folder in Cursor — or any editor with an AI assistant — and tell the assistant:

> Read AGENT.md and follow it.

The full participant information is repeated there, and you will be asked to confirm before any
questions begin.

If you would prefer to be interviewed in conversation rather than through the assistant, reply and I
will arrange a time.

With thanks for considering it,

Roger B. Hunt III
Doctoral Candidate, Organizational Theory
Bentley University
rhunt@bentley.edu

---

## Links used

| Purpose | Link |
|---|---|
| The harness, once merged to `main` | `https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/submissions/lima_pdw/interview` |
| The harness, on the working branch | `https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/worktree-lima-manuscript-review/submissions/lima_pdw/interview` |
| Clone URL, if someone prefers it | `https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab.git` |
| Intake bucket | `gs://pitch-rise-interview-intake` |
| Intake endpoint | `https://us-central1-pitch-rise.cloudfunctions.net/intake` — live |

## For a recipient who does not use an editor with an assistant

Some partners will not have Cursor. Offer them the conversation instead — the invitation already
does. Do not talk anyone into installing something to be interviewed; that converts a favour into an
imposition and will cost you the response.
