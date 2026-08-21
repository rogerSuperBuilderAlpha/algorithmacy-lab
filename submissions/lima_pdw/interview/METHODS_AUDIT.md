# Methods audit — the harness against the qualitative literature

Written 2026-08-19. The instrument was built on 18 August from practice and from what the first
interview got wrong, and it was never checked against the methods literature the paper cites for it.
`PAPER.md` §5 makes six claims about how this study is conducted and analysed. This memo asks, for each,
whether the artifact on disk does what the paper says.

Sources read for this audit: Pratt (2009), Pratt, Kaplan & Whittington (2020) and Timmermans & Tavory
(2012) from `../literature/pdfs/`; Tracy (2010), Gioia, Corley & Hamilton (2013) and Mees-Buss, Welch &
Piekkari (2022) from the same folder; Bowen (2006), Saunders et al. (2018) and Charmaz (2014) at card
depth only, which is flagged where it matters.

**Verdict: the collection instrument is strong and under-warranted; the analysis instrument does not
exist.** Those are different problems and the second is the one that bites before 10 September.

---

## Part 1 — What the harness already does, and what licenses it

Every rule below is in `AGENT.md` or a protocol, and each one turns out to have a warrant in the
literature the paper already cites. None of them says so. Adding the citation costs nothing and makes
§5's claims about the instrument inspectable rather than asserted.

| Harness rule | Where | Warrant |
|---|---|---|
| "One incident per block, minimum. This is a requirement, not advice." | `AGENT.md` | **Pratt (2009)** on the most common failure in qualitative write-ups: "Telling about data, not showing it… too much 'telling' and not enough 'showing'." The incident rule is that failure prevented at collection rather than repaired at write-up. |
| "Knock twice" — one reframe from a different angle | `AGENT.md` | **Charmaz (2014)** on intensive interviewing; card depth. The stronger warrant is the arm's own: the first run took five closing answers at face value and lost the richest material. |
| "Introduce no vocabulary of your own" | `AGENT.md`, protocols | **Bowen (2006)**: sensitizing concepts legitimately *start* inquiry; they must not *sort* it. Handing a participant the category makes the answer evidence of nothing. This is the single most important rule in the harness and the one with the clearest methodological standing. |
| Verbatim markers on the turning sentences | `AGENT.md` | **Gioia, Corley & Hamilton (2013)** on first-cycle coding in informant terms. The markers are the in-vivo discipline operationalised at collection. |
| "Transcribe, do not compose"; keep grammatical person theirs | `AGENT.md` | **Pratt (2009)** again — the shape of the answer is data, and improved phrasing is interpretation smuggled into the record. |
| "Do not contradict them… the divergence is itself the finding" | `AGENT.md` | **Tracy (2010)**, sincerity and credibility. Also the right analytic call: an account diverging from the record is data about how the arrangement is understood. |
| Anonymisation applied as writing proceeds, never as a cleanup pass | `AGENT.md`, `ANONYMIZATION.md` | **Tracy (2010)**, ethics — procedural and situational. Applied at the strongest point: the participant never sees a colleague's name in her own file. |
| `reviewed_by_human` gate; the agent may never set it | `AGENT.md`, `firebase/` | Ethics again, and better than most consent practice: the approval is a machine-checked precondition of submission, not a form signed in advance. |
| "Stop when they stop." No persuading. | `AGENT.md` | Tracy, ethics. Also protects against the role-duality problem the 19 August review raised in finding 7. |

Two things here deserve to be said in the paper rather than buried in a repository.

**The no-vocabulary rule is a methodological commitment, not politeness.** The paper enters with three
derived operations and claims to treat them as sensitizing concepts. The harness is what makes that
claim true — a participant who is never handed "interpret," "specify," or "keep track" cannot produce
them on cue. That is the difference between sensitizing concepts and leading, and §5 currently asserts
the former without pointing at the mechanism.

**The consent gate is unusual and defensible.** Pratt, Kaplan and Whittington (2020) spend their essay
separating transparency from replication and arguing that trustworthiness is inspectable inference
rather than deposited data. A submission pipeline that refuses anything a human has not approved is
exactly that: the trail is the gate, and it is inspectable in `firebase/functions/gate.test.mjs`.

---

## Part 2 — What is missing, in the order it will be missed

### 1. There is no analysis apparatus at all

`PAPER.md` §5 says: "Analysis is abductive (Timmermans & Tavory, 2012): we entered with a derived
construct, treat the three operations as sensitizing concepts, keep first-cycle coding in the
participant's words (Gioia, Corley, & Hamilton, 2013), decline the data-structure template (Mees-Buss,
Welch, & Piekkari, 2022), and treat the design as bricolage (Pratt, Sonenshein, & Feldman, 2022)."

Nothing on disk performs any of it. There is no codebook, no coding rule, no memo file, no discard log,
no negative-case register. `interview/` holds an instrument and a pipeline and stops there.

This matters most for the abduction claim, because abduction is the one that has machinery. Timmermans
and Tavory do not define it as "starting from theory." They define it as inference "aimed at producing
new hypotheses and theories based on **surprising** research evidence," and they name three formal
processes that make it work: **revisiting, defamiliarization, and alternative casing**. Their whole
argument is that "allowing for observational surprises or puzzles should be a central object for
qualitative research design."

**A design that never records what surprised the analyst cannot be abductive.** Right now nothing does.
That is not a citation problem; it is the claim's mechanism missing.

### 2. There is no sampling logic, and with one response that is conspicuous

Pratt (2009) is cited in §5 for exactly the proposition that "enough" is a function of the question
rather than a magic N. That argument works only if the question's demands are stated. Who should be
interviewed, and why those people? The harness is an open invitation across three programmes; anyone may
answer. That is recruitment, not sampling, and a reviewer who reads Pratt's sentence in our paper will
ask the next one.

The material for an answer exists: the paper argues site fit from the gate, the private vote and the
moving codebase. The sampling rule follows from it — people who submitted into a gate and received an
outcome they did not expect, across the arc of a course, plus the operations side that saw the gate from
behind. That belongs in a file, before the responses arrive rather than after.

### 3. Saturation has no rule, and the paper is currently safe by silence

`RESEARCH_PLAN.md` says not to write "saturation was reached" without Saunders et al.'s (2018) rule, and
§5 correctly claims neither saturation nor a completed analysis. Fine for now. But the plan's own
sequence anticipates fielding until the empty blocks fill, and the moment anyone says "enough," the rule
has to already be written. Saunders is at card depth in this arm.

### 4. Tracy (2010) is in the reference list and nowhere in the body

The 19 August review found this and it is still open. The audit above shows Tracy is doing real work in
the instrument — sincerity, ethics, credibility — so the cheapest repair is to cite her where the work
is happening rather than cut the entry.

### 5. The protocols do not enforce the rule the paper attributes to them

§5 says "one incident is required for each block of questions." `AGENT.md` states it as a requirement,
and `STUDENT.md` reinforces it in prose for block B — "follow the specific; 'I just figured it out' is
the start of an answer." But no block carries a completion check, and nothing in the file structure
records whether a block finished with an incident or with a characterisation. The first transcript's
thinness was discovered by reading it, not by the instrument noticing.

A one-line field per block in the response file — the incident, or a mark that the block did not
produce one — would make the paper's claim true at the level of the artifact and give the analysis its
first countable thing.

### 6. The role-duality answer lives in a clause, and the literature for it is uncited

The review's finding 7 said this about the manuscript. It is also true of the repository: `CONSENT.md`
and the protocols handle the mechanics well — consent outside the course, no interview about an open
project, no vote in the gate — but the arm has Brannick and Coghlan (2007), Anteby (2013), Ferguson,
Yonge and Myrick (2004) and Mercer (2007) carded and cites none of them anywhere. Cameron (2024) is the
model for what the passage should look like; `models/cameron2024.md` has the detail.

---

## Part 3 — The minimum apparatus, and what each piece is for

Four files, none long, each answering a question a methods reviewer will ask. Listed in the order they
pay off.

1. **`interview/analysis/SURPRISE_LOG.md`** — one line per response: what was expected, what the
   transcript did instead. This is the abduction claim's mechanism (Timmermans & Tavory's *revisiting*
   and *defamiliarization*), and it is the file that makes §5's first sentence true. The first response
   already has two entries in it: forbearance with no forum, and interpretation delegated to another
   system.
2. **`interview/analysis/CODING_RULE.md`** — what a first-cycle code may be (participant's words), what
   it may not be (the three operations), what happens to material that fits none of them, and the
   discard rule. Gioia for the in-vivo discipline; Mees-Buss for the explicit refusal of the ladder,
   which should be stated as a decision with a reason rather than as an omission.
3. **`interview/analysis/SAMPLING.md`** — who the question requires, why, and what would count as
   enough for *this* question. Pratt (2009). Written before the next response arrives, so it is a rule
   rather than a description.
4. **`interview/analysis/NEGATIVE_CASE.md`** — §5 already names the negative case: a participant who
   obtains an answer from the gate by individual skill alone, with no other party involved. Registering
   it in advance, with what would count as an instance, converts a rhetorical concession into a
   standing test the study can fail.

None of these touches `PAPER.md`, and none requires a response to exist. All four are the kind of thing
Pratt, Kaplan and Whittington mean by an audit trail held for a committee rather than deposited: they
make the inference inspectable without publishing anybody's interview.

## What this audit did not do

Bowen (2006), Saunders et al. (2018) and Charmaz (2014) are cited above from cards, not from the
articles. All three are load-bearing for claims the paper makes or will make — sensitizing concepts,
saturation, interview craft — and each should be read before its sentence is written. No participant
response was read for this memo; the harness was audited as an instrument, against its own files.
