# Intake setup

## Done already

The bucket exists, created 18 August 2026 with the `pitch-rise` admin service account:

```
gs://pitch-rise-interview-intake
  location                     US-CENTRAL1
  public_access_prevention     enforced
  uniform_bucket_level_access  true
```

Nothing can read it without project credentials, and nothing on the public internet can list it.

**Note the project.** This is `pitch-rise`, not the algorithmacy/cohorts project. Functionally fine;
worth a deliberate decision, since interview material for the dissertation will live there
indefinitely alongside whatever else that project is for.

## How a person submits — the two designs

Both keep responses out of git and out of any public repo. They differ in whether you run a public
endpoint.

### Blocked on one IAM grant — do this first

The `firebase-adminsdk-fbsvc@pitch-rise` key can create buckets but **cannot deploy functions.** It
lacks `iam.serviceAccounts.actAs`, and it cannot grant itself the role either (no
`iam.serviceAccounts.getIamPolicy`). Both failures are reproducible; the bucket above was created with
the same key, so this is a permissions boundary, not a broken key.

Signed in as yourself — `gcloud auth login` — either run the deploy in Option A directly, or grant the
key what it needs and let it deploy:

```
gcloud iam service-accounts add-iam-policy-binding \
  299206296414-compute@developer.gserviceaccount.com \
  --member="serviceAccount:firebase-adminsdk-fbsvc@pitch-rise.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser" --project=pitch-rise
```

Deploying as yourself is the better option. A key that can mint functions is a key you have to guard
more carefully than one that can only write to a bucket.

### Option A — direct POST to a Cloud Function *(built and unit-tested; deploy blocked above)*

Nothing on the client holds a credential. The participant's own agent — or the upload page — POSTs the
markdown straight to one endpoint, which validates it and writes it to the bucket under a random name.

```
agent (or page) ──POST markdown──▶ intake ──▶ gs://pitch-rise-interview-intake/<uuid>.md
                ◀── 201 {reference} ─┘
```

**The endpoint enforces the review gate**, which a client cannot be trusted to do. The harness writes
`reviewed_by_human: false` and is forbidden from changing it; only the person sets it true, after
reading the file. A submission still marked false gets a `422` and a message telling them what to do.
Seven cases of that logic are unit-tested, including the obvious dodge — writing
`reviewed_by_human: true` into the body rather than the front matter, which is refused.

Files: `functions/index.js`, `functions/package.json`, `upload.html`.

Deploy (as yourself, per the grant note above):

```
gcloud functions deploy intake \
  --gen2 --runtime=nodejs22 --region=us-central1 \
  --source=submissions/lima_pdw/interview/firebase/functions \
  --entry-point=intake --trigger-http --allow-unauthenticated \
  --set-env-vars=INTAKE_BUCKET=pitch-rise-interview-intake \
  --memory=256Mi --timeout=60s --project=pitch-rise
```

Then put the printed URL into **two** places: `INTAKE_URL` in `../AGENT.md`, so an agent can send
directly, and `MINT_URL` in `upload.html` for people who would rather do it in a browser. The hosted
page's own URL goes into `[UPLOAD_URL]` in `../AGENT.md`.

Smoke-test it before anyone gets the link — the second call must be refused:

```
printf -- '---\nrole: operations\nreviewed_by_human: true\n---\n\n# Interview\n\n**Q:** test\n\n**A:** test\n' \
  | curl -s -X POST "$URL" -H 'Content-Type: text/markdown' --data-binary @-

printf -- '---\nrole: operations\nreviewed_by_human: false\n---\n\n# Interview\n\n**Q:** test\n\n**A:** test\n' \
  | curl -s -X POST "$URL" -H 'Content-Type: text/markdown' --data-binary @-
```

**What you are accepting.** `--allow-unauthenticated` is a public endpoint. Anyone who finds it can
mint an upload URL and drop a ≤512 KB markdown file in the bucket. They cannot read, list, overwrite,
or delete anything. The realistic worst case is junk you delete, not exposure. Reduce it if you like
with a shared secret header the page sends, Cloud Armor, or App Check — none of which are anonymity
problems, since they identify the *page*, not the person.

**Cost.** Negligible at this volume, but it is a billable resource that stays up until you remove it:

```
gcloud functions delete mintUpload --gen2 --region=us-central1 --project=pitch-rise
```

### Option B — Firebase Storage rules and anonymous auth *(no public endpoint)*

Uses the project's default Firebase bucket instead, with `storage.rules` enforcing create-and-nothing-
else. Needs Anonymous sign-in enabled in the console, and the client carries the public Firebase web
config.

1. Console → Authentication → Sign-in method → **Anonymous** → enable.
2. `firebase deploy --only storage` with `storage.rules`.
3. **Verify from a signed-out browser that you cannot read an object.** If you can, stop.
4. Restore the Firebase-SDK version of `upload.html` from git history (commit `d472d3f`).

Slightly weaker: the client holds a real (if public) API key, and anonymous auth mints a UID per
uploader. Simpler in that nothing is deployed and nothing bills.

## Hosting the page

Wherever you like, at an unguessable path — `cohorts.algorithmacy.org/i/<random>`. The page is
`noindex`, but a tidy URL attracts traffic you do not want.

## Reading what arrives

```
gcloud storage ls gs://pitch-rise-interview-intake/
gcloud storage cp gs://pitch-rise-interview-intake/<uuid>.md .
```

Filenames are random UUIDs and carry nothing; sort by creation time if you need order. **Move them
into the private dissertation repo's `paper3/corpus/` for analysis — never into `algorithmacy-lab`,
which is public.**

## Two things to know before promising anonymity

**Google logs request metadata, including IP.** The consent text says no name, no email, no account,
which is true. It does not claim no server logs, because that would be false. Immaterial for staff
and partners. If the participant version needs a stronger guarantee later, the Bentley IRB will
likely want institutional Qualtrics or an explicit line about cloud logging in the consent form.

**Anonymity forecloses withdrawal.** No link exists between a file and a person, so a withdrawal
request cannot be honoured. `../CONSENT.md` says this outright, which is why the review-before-upload
step is load-bearing rather than a courtesy.

## The service account key

It is at `~/Downloads/pitch-rise-firebase-adminsdk-fbsvc-d506f82e6a.json`. It is a live credential
with broad project rights.

- Move it out of `Downloads` and `chmod 600` it.
- Never let it into a repo. `algorithmacy-lab` is public, so a committed key is a disclosed key.
- Rotate it in the Firebase console if it has ever been in a shared folder, a chat, or a public path.

## Not cleared yet

**The participant path.** The harness refuses it, and `../CONSENT.md` explains why. Enabling it needs
the `paper3/irb/` determination — and that protocol still describes a gate that stopped running
(private votes; the Hult gate publishes reviews and upvotes and withholds only the tally). Correct the
site description before filing, or the site-fit argument arrives already refuted by your own
governance doc.
