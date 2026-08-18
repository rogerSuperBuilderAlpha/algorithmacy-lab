# Standing up the intake — Roger's steps

Fifteen minutes. Four of them matter.

## 1. Enable anonymous auth

Firebase console → Authentication → Sign-in method → **Anonymous** → enable.

The rules require `request.auth != null`, so uploads fail without this. Anonymous auth mints a
throwaway UID with no email, name, or persistent identity attached. It exists to stop the bucket
being an open drop box for the whole internet, not to identify anyone.

## 2. Deploy the rules

Copy `storage.rules` into your Firebase project and:

```
firebase deploy --only storage
```

Then check it: open the bucket path in a browser. You should get a permission error. If you can read
a file from a signed-out browser, the rules did not deploy and nothing should go out until they have.

## 3. Fill in the config and host the page

Firebase console → Project settings → Your apps → Web → copy the config object into the
`firebaseConfig` block in `upload.html`. Those values are public by design; the rules are the
protection, not the key.

```
firebase deploy --only hosting
```

Put it somewhere unguessable rather than at `/`. Something like
`cohorts.algorithmacy.org/i/<random>` — the page is `noindex`, but a tidy URL invites traffic you
don't want.

## 4. Put the URL in the harness

`AGENT.md` closes on `[UPLOAD_URL]`. Replace it with the real one. That placeholder is deliberate —
the harness should not ship with a live endpoint before the rules are verified.

## Reading what comes in

Console → Storage → `interview-intake/`, or pull them with a service account. Filenames are random
UUIDs and carry nothing. Sort by upload time if you need order.

**Move them out of the bucket and into the private dissertation repo's `paper3/corpus/` for
analysis** — never into `algorithmacy-lab`, which is public.

## Two things to know before you promise anonymity

**Google logs request metadata, including IP addresses.** The consent text says no name, no email, no
account, which is true. It does not say no server logs, because that would be false. For staff and
partners this is a non-issue. If the participant version later needs a stronger guarantee, the
Bentley IRB will likely want either institutional Qualtrics or an explicit statement about GCP
logging in the consent form.

**Anonymity makes withdrawal impossible.** There is no link between a file and a person, so a request
to withdraw cannot be honoured — there is nothing to find. `CONSENT.md` says this outright. It is why
the review-before-upload step is load-bearing rather than a courtesy.

## What this is not yet cleared for

**Participants.** The harness refuses that path in `AGENT.md` and `CONSENT.md` says why. Turning it on
needs the `paper3/irb/` determination — and that protocol still describes a gate that no longer runs
(private votes; the Hult gate publishes reviews and upvotes and withholds only the tally). Correct
that before filing, or the site-fit argument arrives refuted by your own governance doc.
