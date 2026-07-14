# Formal Fidelity Review — Paper 5, "Interdependence Without Unity"

**Reviewer lens:** integrated-information formalism, computed-receipt fidelity, honest scope. The
critical probe: did this paper repeat the Papers-2/3 failure of asserting Φ verdicts on uncomputed
cases, or claim a computed market that does not exist?

---

## Verdict

**Accept with minor revisions.** On the one axis this review exists to police — fidelity to the quorum
receipt and honesty about what the corpus does and does not model — Paper 5 is the cleanest of the
series so far. Every number matches `run.txt` exactly. Both failure modes the probe was sent to hunt
are not merely avoided but explicitly named and closed in the body (lines 160–164 for the
overstatement, 174–179 for the phantom market). The guard against Φ-demotion holds; the guard against
"aggregate = disorder" holds and is argued well (134–139). This is what a corrected paper looks like.

**Single most important fix.** The numbers are right, so the top fix is a *mechanism-location* error,
not an arithmetic one. The paper repeatedly explains the majority result by "scalar-mediated coupling"
— a shared tally every party reads (163–164, 169–171). But all three thresholds read a tally; a
threshold of any kind is a count. Scalar-mediation cannot be what factors the interior threshold,
because the extremes are equally scalar-mediated and still bind at 3%. The receipt's actual
distinguishing feature — the one the program's own finding names — is that the majority gate goes
**insensitive to which particular parties** made the count (redundancy / substitutability), while the
all-or-any extremes hold each party to the firing. Relocate the gloss from "shared scalar" to
"indifferent to which party," and two things happen: the internal tension disappears, and the market
bridge gets *stronger*, because "the farmer needs shoes, not this shoemaker" (196–197) is exactly the
same insensitivity-to-which-party the majority gate exhibits. Right now the best mechanism in the paper
sits in the specialization section and never gets connected to the receipt that would ground it.

---

## Step 0

- Read the receipt (`run.txt`), `THREAD.md`, `quorum.py`, `STRUCTURAL_FINDINGS.md`, and Paper 4's
  apparatus paragraph; checked every quorum number and every scope caveat against source.
- The paper's factual reporting is accurate; the revisions below are precision, cross-paper
  consistency, and register — not correction of a false claim.

---

## Part 1 — Formal rigor (ranked)

### 1. The majority result is glossed as "scalar-mediation" when the receipt says "redundancy." (Most important.)

The receipt:

```
quorum k=1 (any     ): triadic=12/400 (3%)  S-veto|integrating=170/170
quorum k=2 (majority): triadic= 0/400 (0%)  S-veto|integrating=247/247
quorum k=3 (all     ): triadic=12/400 (3%)  S-veto|integrating=158/158
```

The paper reports these exactly (153–158, 166–167). No error there. The problem is the *why*. The paper
writes that k = 2 is "the paradigm case of scalar-mediated coupling, each party responding to a shared
tally rather than to any other party in particular" and that a partition "can route around" it because
"the tally was never anywhere in particular" (163–171). That explanation over-predicts: it applies word
for word to k = 1 and k = 3, which also relay a shared tally and whose halves could also "keep their own
tally and re-threshold." If scalar-mediation were the factoring mechanism, all three thresholds would
factor equally. They do not — the extremes bind at 3%.

`THREAD.md` states the real mechanism (lines 24–26): "a majority gate is insensitive to which particular
parties are active once enough are, so it does not hold each party to the determination the way the
all-or-any extremes do." `STRUCTURAL_FINDINGS.md` files it under substitutability — finding 5,
"Substitutability collapses irreducibility," and the one-line law the paper itself quotes:
"majority/redundant determinations factor entirely." The determination factors because it is
*redundant in which parties satisfy it*, not because it passes through a scalar.

This is the single load-bearing fidelity fix. It is not fatal — most scalar-mediated forms do factor
(97%+ at the extremes, 100% at the majority), so the market-as-aggregate reading survives — but the
paper attributes the result to the wrong feature of its own computation, and the correct feature is the
one that connects to the market. Exact rewrite in Part 3.

### 2. "Every market-clearing rule actually uses" the interior threshold — the interpretation leaks into the computed sentence. (Moderate.)

Line 158: "The interior threshold, the one every voting body and every market-clearing rule actually
uses, factors entirely." This sits inside the paragraph reporting the *computed* result, and it asserts
that market clearing *is* a k = 2 majority rule. It is not. Market clearing is scalar-mediated and
redundant-in-suppliers, but it is not a majority-of-three vote, and stating that it "actually uses" the
interior threshold reads as a computed identity rather than an interpretation. The paper's own honest
caveat at 174–179 ("No form in this corpus represents a price or a market scalar directly") contradicts
the confidence of line 158. Keep the market out of the computed sentence entirely and let it appear only
in the flagged-interpretation paragraph, where it belongs. This is the same discipline Paper 4 learned:
the run reports thresholds over three parties; the market is a reading laid over the run.

### 3. The k = 2 "integrate something" count (247, the highest) risks reading against "majority factors entirely." (Moderate — clarity.)

The paper reports 247/400 draws "integrate something" at k = 2 (166–167), then two sentences later
quotes "majority and redundant determinations factor entirely" (168). A careful reader notices that the
*majority* threshold has the **most** draws where something integrates (247, versus 170 and 158 at the
extremes) and yet **zero** three-way bindings. Unexplained, this looks like a contradiction. It is not:
`integrating_coalitions` counts any coalition that integrates, and at k = 2 the coalitions that integrate
are *sub-parts* (pairs, mediator-plus-subset), never the full triad — which is exactly what "factors
entirely" means for the whole. One clause closes the gap and actually sharpens the lesson (the majority
gate is the busiest at coordinating something short of the whole and the emptiest at binding the whole).
Rewrite in Part 3.

### 4. "As connected as a system gets" — verdict-not-scale watch. (Minor.)

Line 151: "By the crude measure of how connected the parts are, this is as connected as a system gets."
The framing "crude measure of how connected the parts are" correctly distances this from Φ, so it does
not violate verdict-not-scale outright — it is a connectivity/wiring claim, not a Φ-magnitude claim. But
"as connected as a system gets" flirts with a maximum on a scale, and this series has committed to Φ as
a verdict (does division destroy anything, yes/no), not a quantity with a ceiling. Tighten to a plain
wiring statement: every part depends on the mediator and the mediator on all three, nothing missing. No
"maximum" language. Minor, but it is the kind of phrase Paper 4's panel converted throughout.

### 5. Apparatus consistency with Paper 4: state partition ≠ removal. (Minor — cross-paper.)

Paper 4's apparatus paragraph says it outright: "A cut severs dependencies; every part stays exactly
where it is." Paper 5's apparatus (34–43) says only "whether any way of cutting the system leaves the
parts making the same differences," and never states that the parts remain in place. Given the two-rooms
framing (splitting a population, not deleting traders), a lay reader will probably read "cut" correctly —
but the series should not let one paper define partition-as-severing and the next leave it implicit. Add
the one clause for consistency. The formalism citation itself (Φ; Albantakis et al., 2023; Oizumi et al.,
2014) is correct and matches Paper 4.

### 6. "N = 4" is unglossed. (Trivial.)

Line 153: "over 400 random draws (seed 11, N = 4)." N = 4 is the node count (three parties plus the
mediator), matching `quorum.py`. A reader coming to it fresh may read N as a sample size against the 400.
One word ("four nodes") removes the ambiguity. Trivial, noted for completeness.

### Fidelity items that are CORRECT and should not be touched

- The 12/400, 12/400, 0/400 triadic rates: exact.
- The 170/247/158 integrating counts and the S-veto-in-every-one claim: exact against 170/170, 247/247,
  158/158.
- The "three percent, which is not nothing" refusal to overstate (160–164): this is precisely the
  correction Papers 2 and 3 failed to make. It closes failure mode (a). Keep verbatim.
- The phantom-market disclosure (174–179): "No form in this corpus represents a price or a market scalar
  directly… an interpretation of a computed result, not a computed model of a market… the two-rooms case
  is an illustration, not a run." This closes failure mode (b) cleanly. Keep.
- The redundant-determination finding is used *in scope*, quoted accurately from `STRUCTURAL_FINDINGS`.
- No Φ-demotion. Line 143 ("Here is where the criterion earns the comparison, because it explains why…")
  affirms the instrument's work. The concession that the market is "only" an aggregate never tips into
  "the test does no work" — it stays a scope statement (the test brackets distribution, 253–258), which
  is the correct modest-not-self-defeating posture the dissertation guard requires.
- No overclaim on what a low verdict means. The paper insists aggregate ≠ disorder (134–139) and
  aggregate ≠ no coordination ("the order is genuine and the order is external," 113). This is the exact
  guard the lens asked for, and it is argued, not merely asserted.
- The bacteria/quorum-sensing worry in the brief is a non-issue: the paper uses "quorum" in the
  voting/threshold sense only and never smuggles biological quorum sensing as a computed result.

---

## Part 2 — Register and slop

First, the register call: **first person is correct here and is not a violation.** The repo
`CLAUDE.md` bans "I/we," but that rule governs the lab and dissertation code-prose. This is the Substack
essay series, whose venue the global `writing-style.md` explicitly covers ("First person is required,
not banned"; the genre note licenses a more first-personal register for essays). The author should not
"fix" the first person. Flagging this so a later pass does not mistake it for a defect.

Now the genuine tics.

### A. Self-narrating care — the one register tic that recurs.

Both style files target this ("performed rigor," "self-narrating honesty… cut every instance"). Instances:

- 174: "**Say plainly** what this is not." — This is on the repo's banned-openers list verbatim
  ("Stated plainly," "To be clear"). Cut the frame; keep the content.
- 216: "so **I will not soften it**."
- 249: "and the mistake is **the one to guard against most carefully**."
- 313–314: "that is the thing worth ending on, because it is **easy to state loosely and important to
  state exactly**."
- 160: "and it **needs stating exactly rather than rounded up**." (This one is closer to load-bearing,
  because the failure mode is real — but it still announces care. Trim to the claim.)

None of these is fatal; together they are a drumbeat of the paper telling you how careful it is being.
State the limitation; delete the announcement.

### B. The last third re-argues one point across three sections.

"Fixing distribution does not fix externality; same boundary, two upgrade conditions" is the paper's
real payoff, and it is stated at full length **four times**:

- 248–258 (the general statement: "A market engineered to distribute perfectly would remain… exactly as
  external as before"),
- 277–287 (Kain's remedy: "A civil society with a strong welfare apparatus… reads, on my criterion,
  exactly as it read before"),
- 289–299 (the Nordic case: "A just distribution repairs the ethical deficiency and leaves the
  structural externality exactly where it was"),
- 301–309 (the summary: "Keep them apart and each stays true. Run them together and both go false").

This is the series thesis, and repetition across *nine* papers is fine — but four full restatements
inside *one* paper is the "verbatim repetition… restated across sections" tic both style files name. The
Nordic case (289–299) is the strongest because it is concrete; keep it as the load-bearing instance.
Compress 248–258 to the setup, let Kain's section make the *Kain-specific* point (his remedy is a fix in
the ethical register, which is his contribution, not a fourth statement of the thesis), and let the
"Same Boundary, Two Reasons" section do the *upgrade-condition* work (recognition vs. causal structure,
327–328) without re-running the distribution point a fourth time.

### C. Section-ending epigram uniformity.

Nearly every section lands on a polished antithetical epigram: "a whole that reads everyone can still be
an aggregate" (172), "Specialization made the members need each other more and did not make them members"
(202), "One country, one defect fixed, one defect untouched" (299), "Keep them apart and each stays true.
Run them together and both go false" (309), "that disagreement is small enough to see past and real
enough that seeing past it would be a mistake" (337). Individually good. As the shape of every section
close, it is the "every section ending on a polished epigram" tell the global file names. Let two or
three sections end plainly, on the claim, without the chiasmus. The cure is variance, not more polish.

### D. Antithesis density in the closing section.

The house style permits load-bearing antithesis (the whole paper is *about* two registers that agree on
placement and disagree on reason, so contrast is the argument's real shape — do not strip it). But
311–337 stacks it: "the roads do not merge," "not the external state made more tightly coupled but the
external state *raised*," "It is not higher integrated information," "agree on where the line falls and
disagree on what the line is," "a subject and not a resultant." Several of these say the same thing.
Keep the sharpest (the upgrade-condition contrast, 321–328) and thin the rest. One contrast per
paragraph, per the repo rule.

Agentless passive: clean. The paper is strongly agent-first (Hegel did, Smith's pin factory, Kain
states, García Mills, Waszek documented). This is a real strength and matches the house rule that
matters most.

---

## Part 3 — Exact rewrites (author's voice)

### Rewrite 1 — the mechanism fix (Part 1, item 1). Replace lines 160–164.

> That contrast is the finding, and it needs stating exactly. It is not that any count-reading system is
> an aggregate — the extremes can and occasionally do bind, at three percent, which is not nothing. And
> the majority does not factor because it reads a shared tally while the extremes do not: all three read
> a tally, a threshold of any kind is a count. What sets the majority apart is that it stops caring which
> parties made the count. At *k* = 1 any single party is enough to fire the mediator, so each party's
> flip can decide it; at *k* = 3 every party is needed, so each is held to the firing. At *k* = 2 the gate
> goes indifferent to which two — once enough are active it forgets the rest, and a determination that
> does not track which particular party is live is one no partition has to keep whole. That indifference,
> not the mere presence of a shared number, is what factors the interior threshold. It is why the program
> files this result under substitutability rather than under mediation: majority and redundant
> determinations factor entirely.

### Rewrite 2 — the 247 clarity fix (Part 1, item 3). Replace the veto sentence at 164–168.

> A separate structural fact sharpens the same lesson. Whenever some coalition inside the system
> integrates — even when the whole three-way form does not — the mediator sits at the bottleneck. 170 of
> 400 draws integrate some coalition at *k* = 1, 247 at *k* = 2, 158 at *k* = 3, and S is a veto player in
> every one of them. The majority threshold is the busiest here and the emptiest above it: more of its
> draws coordinate *something* than at either extreme, and none of them binds all three. A sub-part
> coordinates; the whole factors. That is the quorum.

(Then move directly to the flagged-interpretation paragraph — see Rewrite 3 — so the market never
appears inside a computed sentence.)

### Rewrite 3 — pull the market out of the computed claim (Part 1, item 2). Revise line 158 and the bridge at 169–172.

Line 158, drop the market from the computed sentence:

> The interior threshold — a majority, the rule a voting body reaches for — factors entirely.

Then let the market bridge carry the redundancy mechanism, tied to the shoemaker case it already has:

> Reading the market through this receipt is an interpretation, not a run, and the mechanism is the one
> the majority result just showed. A price is a shared number that summarizes the whole supply and forgets
> which supplier produced any unit of it — the farmer needs shoes, not this shoemaker. That is the
> majority gate's indifference to which party, at the scale of a thousand traders: a coupling redundant in
> who satisfies it, and redundancy is what a partition routes around. No form in this corpus represents a
> price or a market scalar directly; the quorum, three parties and a threshold, is the nearest in-silico
> case of the structure, and the two-rooms split from the first post illustrates it without computing it.
> The computed backbone of Hegel's finding is narrow and it is real: a determination that reads everyone
> but tracks no one in particular can still be an aggregate.

### Rewrite 4 — self-narration (Part 2, item A). Two examples.

Line 174, cut the banned frame:

> Be exact about what this is not. No form in this corpus represents a price or a market scalar directly…

Line 216:

> Now the guard, and it carries the whole ethical weight of the section. Hegel's verdict that civil
> society is the external state is a claim about its *form*…

### Rewrite 5 — apparatus consistency (Part 1, item 5). Add one clause at 36.

> …and asks whether any way of cutting the system — severing the dependencies while every part stays
> exactly where it is — leaves the parts making the same differences to each other that they made when
> intact.

### Rewrite 6 — "as connected as a system gets" (Part 1, item 4). Replace line 151.

> By the crude measure of how many wires run between the parts, nothing is missing: no party settles its
> next state without the mediator, and the mediator answers to all three.

---

## Closing note

**The strength.** This paper does the thing Papers 2 and 3 were caught not doing. It reports a computed
receipt at its exact numbers, it refuses the sweeping reading the data invites ("not that any
count-reading system is an aggregate… three percent, which is not nothing"), and it flags the market as
an interpretation laid over the quorum rather than a computed model. The sourcing note's "honest scope"
paragraph (414–420) is a model for the series. On the formal axis this review polices, the paper is
sound; every revision above is a tightening, not a repair.

**The one thing only the author can supply.** The mechanism fix (Rewrite 1/3) sharpens the bridge from
the quorum to the market, but it does not close the gap the paper honestly leaves open: the market
reading rides on a three-party threshold model, and the corpus contains no price scalar and no
thousand-trader system. The author has two defensible moves and must choose one, because the reviewer
cannot. Either (a) hold the market strictly as an interpretation of the quorum — which the paper now
does, and which is fully honest, at the cost of leaving "a shared scalar redundant in its suppliers"
computed only at n = 3 with a threshold gate; or (b) commission the owed toy, the way Paper 4 owes an
acid–base pair — a scalar-mediated form with many substitutable suppliers feeding one public number,
run at the sizes the program computes, to show the redundancy result survives past three parties. Option
(b) is an afternoon in the program's own formalism and would convert the market bridge from a reading of
a narrow receipt into a computed structural claim. Until then, the paper's honesty is intact and its
reach is exactly as long as three parties and a threshold — and the author is the only one who can
decide whether that reach is enough for the argument he wants civil society to carry.
