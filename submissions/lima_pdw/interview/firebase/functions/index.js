/**
 * Interview intake endpoint.
 *
 * Accepts one anonymized markdown interview, validates it, and writes it to the
 * intake bucket under a random name. Callable two ways, both anonymous:
 *
 *   - the participant's own agent POSTs the file directly
 *   - the upload page POSTs it from a browser
 *
 * The endpoint enforces one thing the client cannot be trusted to enforce: a
 * submission whose front matter still says `reviewed_by_human: false` is
 * refused. The agent writes that field as false and is forbidden from changing
 * it; only the person can set it true, and only after reading the file. That
 * makes the review step a server-side gate rather than an honour system.
 *
 * Nothing about the request is recorded beyond what the object itself carries:
 * no IP in the object, no headers, no timestamp of the sender's choosing.
 */

const { Storage } = require('@google-cloud/storage');
const crypto = require('crypto');

const BUCKET = process.env.INTAKE_BUCKET || 'pitch-rise-interview-intake';
const MAX_BYTES = 512 * 1024;
const MIN_BYTES = 200;

const storage = new Storage();

function readBody(req) {
  if (req.rawBody) return req.rawBody.toString('utf8');
  if (typeof req.body === 'string') return req.body;
  if (req.body && typeof req.body.markdown === 'string') return req.body.markdown;
  return '';
}

/** Front matter must exist, and must declare a human read it. */
function checkReviewGate(text) {
  if (!text.startsWith('---')) {
    return 'That file has no front matter — it does not look like an interview the harness wrote.';
  }
  const end = text.indexOf('\n---', 3);
  if (end === -1) return 'The front matter block is not closed.';
  const front = text.slice(3, end);

  if (/^\s*reviewed_by_human\s*:\s*true\s*$/im.test(front)) return null;
  if (/^\s*reviewed_by_human\s*:\s*false\s*$/im.test(front)) {
    return 'This is still marked reviewed_by_human: false. Read the file, change anything you want to change, set that to true, and send it again.';
  }
  return 'The front matter has no reviewed_by_human field. Nothing is accepted without it.';
}

exports.intake = async (req, res) => {
  res.set('Access-Control-Allow-Origin', '*');
  res.set('Vary', 'Origin');

  if (req.method === 'OPTIONS') {
    res.set('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.set('Access-Control-Allow-Headers', 'Content-Type');
    res.set('Access-Control-Max-Age', '3600');
    return res.status(204).send('');
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ ok: false, error: 'POST the markdown file as the request body.' });
  }

  const text = readBody(req);
  const bytes = Buffer.byteLength(text, 'utf8');

  if (bytes < MIN_BYTES) {
    return res.status(400).json({ ok: false, error: 'That body is too short to be an interview.' });
  }
  if (bytes > MAX_BYTES) {
    return res.status(413).json({ ok: false, error: `Larger than the ${MAX_BYTES / 1024} KB limit.` });
  }

  const gate = checkReviewGate(text);
  if (gate) {
    return res.status(422).json({ ok: false, error: gate });
  }

  try {
    const name = `${crypto.randomUUID()}.md`;
    await storage.bucket(BUCKET).file(name).save(text, {
      contentType: 'text/markdown; charset=utf-8',
      resumable: false,
      metadata: { cacheControl: 'no-store' },
    });
    // The receipt names the object so a sender can mention it if something looks
    // wrong. It identifies the file, never the person.
    return res.status(201).json({ ok: true, received: bytes, reference: name });
  } catch (err) {
    console.error('write failed', err);
    return res.status(500).json({ ok: false, error: 'Could not store the file. Try again, or email it.' });
  }
};
