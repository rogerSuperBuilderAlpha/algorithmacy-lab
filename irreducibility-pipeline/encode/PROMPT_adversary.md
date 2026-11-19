# Prompt: search for the defensible encodings that would change the answer

Run this after the drafter, on the same case material and the drafter's JSON. The adversary's job
is to stop a single convenient reading from standing as "the" verdict. A sampled sensitivity check
is not enough: in the lab's tests, an adversary limited to evidence-permitted readings could flip
the verdict on every contested account it was given.

---

You are given a coordinative structure's case material and a set of drafted encodings. Your task is to
find the **most different readings the evidence still permits**. You do not compute anything.

**Case material**

```
<<PASTE THE SAME CASE MATERIAL>>
```

**Drafted encodings**

```
<<PASTE THE DRAFTER'S JSON>>
```

For each of the three forces below, write at most one new encoding with role `"rival"`, each with
verbatim evidence for every rule. Write it only if the evidence actually permits the reading; if it does
not, say which passage rules it out.

1. **Commit versus convey.** If the drafts have the mediator committing on a joint condition, find the
   strongest evidence that it only relays one party's signal, or only stores inputs for a human. If
   the drafts have it relaying, find the strongest evidence that it commits.
2. **Substitutability.** If a party could be one of several interchangeable parties (drivers in a pool,
   sellers of the same item, reviewers on a rota), encode the pool with `or` and separate labels for
   the pool members.
3. **Spectators and outside options.** If a party watches but does not act, add it as a node. If a
   party can reach another without the mediator, encode the direct tie as a complement (`and`) or a
   substitute (`or`), according to what the evidence says about whether they need the mediator as
   well.

For each new encoding, state its prediction and reason before anything is computed, as the drafter did.

**Output:** the drafter's JSON with your encodings appended to `encodings`. No prose outside the JSON.
