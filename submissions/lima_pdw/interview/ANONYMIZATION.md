# Anonymization rules

Apply these **while writing**, never as a pass at the end. The person reviewing the file should not
have to read a colleague's name in order to remove it.

## Substitutions

| What appears | Write instead |
|---|---|
| The speaker's own name | nothing — the file has no author field |
| Another person's name | `[STAFF-A]`, `[PARTICIPANT-B]`, `[PARTNER-C]` — consistent within the file, arbitrary across files |
| A GitHub handle, email, or username | `[HANDLE-1]` |
| A company or NGO by name | `[PARTNER-ORG]` |
| A government ministry or agency | `[MINISTRY]` |
| A police or security service | `[PUBLIC-AGENCY]` |
| An elected official, by name **or by constituency** | `[ELECTED-OFFICIAL]` |
| A university or school | `[INSTITUTION]` |
| A town, district or constituency | `[LOCALITY]` |
| An exact date | the month and year only |
| A project or repository name | `[PROJECT-1]` |
| A dollar figure tied to one person | a range, or cut it |

Keep the country and the program type. "An eight-week program in Trinidad" is context the account
needs and identifies nobody on its own.

## Constituency is a name

`[ELECTED-OFFICIAL]` covers the office as well as the person. "The MP for La Brea" names one living
individual exactly as surely as the surname does — there is one. The same holds for "the AI
Ministry" and for a national police service: in a country of 1.4 million, the role *is* the
identity. Substitute the role token and let the paper describe the relationship generically.

## Third-party speech

Do not record what someone else supposedly said, in quotation marks, attributed to a role. A quoted
line from `[STAFF-A]` is a statement by a person who never consented and never saw it. Paraphrase
what the speaker understood, in the speaker's voice: "the impression I got from the staff side was
that…"

## What not to strip

Do not anonymize away the substance. The following stay, always:

- What the rule was, and whether it changed
- What the speaker did, and what happened next
- What they got wrong, and how they found out
- Sequence and timing relative to the program — "week three," "after the second review"
- Their judgment of how it went, including if that judgment is unflattering

An anonymized file that has lost the incident has lost the point. Strip the identity, keep the event.

## The limit, stated plainly

This is **pseudonymization**, and pseudonymization is not anonymity in a cohort of thirty. Somebody
who was in the room can often reconstruct who `[STAFF-A]` is from a single detail — a role, a
sequence of events, a turn of phrase. In a small country the same is true of organizations.

So the rules above are a floor, not a guarantee, and the human review step is not a formality. Tell
the person that in the closing message, and mean it: they know their context and you do not.

## When in doubt

Generalize one level and note it inline: `[LOCALITY]` rather than the town, `[PARTNER-ORG]` rather
than the NGO. If a whole answer cannot be told without identifying someone, write:

> *(One answer here was withheld as unanonymizable.)*

and move on. A gap in the record is a smaller cost than an exposure.
