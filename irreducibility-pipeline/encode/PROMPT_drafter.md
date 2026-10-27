# Prompt: draft rival encodings of a coordinative structure

Model-agnostic. Paste the case material where marked. The output must validate against
`encode/SCHEMA.json` and pass `python -m irreducibility.encode_check <file>`, which rejects any rule
that lacks evidence, any mediator rule without an alternative, and any encoding without a
prediction.

---

You are encoding one coordinative structure as a small Boolean model so that its irreducibility can be
computed exactly. You draft; a researcher approves. Do not compute anything and do not guess what the
computation will return.

**Case material**

```
<<PASTE THE BOUNDED ACT, THE PARTY LIST, AND THE EVIDENCE: prose, interview excerpts, documents, logs.
Number the paragraphs or give each excerpt a locator.>>
```

**Steps**

1. **Parties.** Use the party list you are given. For each party, state what its bit = 1 means and what
   that binary collapses.
2. **Who reads whom.** A party reads another only if the evidence shows its action depends on the
   other's state. An edge needs a documented process, a log, or agreement among the parties. Record a
   single unsupported claim as an alternative, not an edge.
3. **The function.** Write each party's next state as a Boolean expression over the parties it reads,
   using `and`, `or`, `not`, `xor`, `0`, `1` and party labels only. For the mediating system, decide
   whether the evidence shows it **commits** on a joint condition (e.g. `D and R`), **conveys** a
   signal one party sets (e.g. `D`), or **stores** inputs for someone else to decide. Treat a pool of
   interchangeable parties as `or` over the pool.
4. **Evidence.** For every rule, quote the passage it rests on verbatim, with its source and locator.
   If no passage supports a rule, do not write the rule; say what evidence is missing.
5. **The alternative.** For the mediator's rule, and for any rule the evidence leaves open, give the
   alternative rule the evidence does not rule out and say why.
6. **Rival encodings.** Where the parties' accounts conflict (for example, the platform says it
   commits and the workers say it suggests), do not resolve the conflict by majority. Write one
   encoding per account, with role `"rival"`, and name whose account each one is.
7. **Prediction.** For each encoding, state the verdict you expect (`dyadic` or `triadic`), the parties
   you expect in the core, and a one-sentence structural reason. This prediction is fixed before
   anything is computed and is scored afterwards.

**Output:** one JSON object in the format of `encode/SCHEMA.json`. No prose outside the JSON.
