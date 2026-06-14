# Q106 findings — the design vocabulary is the law's three conditions, read as moves

All four hypotheses confirmed. Six named operations on three levers (binding, liveness, requirement) each
move the verdict in a stated direction, each build paired with an inverse break. The design vocabulary a
coordination engineer needs is the law's conditions turned into operations.

| operation | lever | direction | before → after |
|---|---|---|---|
| add_binding | binding | build | dyadic → triadic |
| remove_binding | binding | break | triadic → dyadic |
| restore_liveness | liveness | build | dyadic → triadic |
| break_liveness | liveness | break | triadic → dyadic |
| require_all | requirement | build | dyadic → triadic |
| substitute | requirement | break | triadic → dyadic |

| H | Result | Verdict |
|---|--------|---------|
| H1 | every build operation: dyadic → triadic | confirmed |
| H2 | every break operation: triadic → dyadic | confirmed |
| H3 | build and break are inverse pairs per lever | confirmed |
| H4 | three levers, each one build and one break | confirmed |

From `probe_design_operations.py`.

## What it says

The design operations are the law's conditions, read as moves. The law makes a coordination triadic when
the mediator binds every party into one joint determination, when each party keeps itself live to the
commit, and when the parties are jointly required rather than substitutable. Each of those three conditions
is a lever, and each lever carries a build operation that supplies the condition and a break operation that
removes it. Add the mediator's read of a party and a dyad becomes a triad; remove it and the triad becomes a
dyad. Close a party's loop to the mediator and the form builds; open it and the form breaks. Make optional
parties all-required and the form builds; make a required party optional and it breaks. Six operations, and
every one is the law turned into an edit.

The operations come in inverse pairs. For each lever the build and the break are exact inverses: the build
takes the dyadic form to the triadic one, and the break takes that triadic form back to the dyadic one (H3).
The catalog is therefore not six independent moves but three reversible levers, each switchable in either
direction. A coordination engineer has three knobs (binding, liveness, requirement), and turning any one
moves the verdict.

The vocabulary is complete in the sense that matters for design. Q105 found that building a triad usually
restores liveness, and Q107 will show repair is lever-specific; both presuppose a vocabulary of named
operations, and this is that vocabulary. The descriptive program read whether a form is triadic; the design
operations say how to make it so, or unmake it, and they are exactly the conditions the law already named.
The bridge from the verdict to the design-operations account is that the operations are the conditions, and
the conditions are the operations.

## Caveats

- **Confirmatory.** All four predictions held; the catalog is the law restated as moves.
- **Keystone forms.** The operations are demonstrated on keystone before-and-after forms (broadcast,
  read_recipient, one_shot, the k=2 market), not as transforms over the whole family. They move the verdict
  on these forms; that they move it on every form is Q105's construction-distance result, not claimed here.
- **Three levers.** Binding, liveness, requirement match the law's conditions; a richer form family could
  expose a lever the three-node forms do not, and is untested. In-silico, exact verdict.
