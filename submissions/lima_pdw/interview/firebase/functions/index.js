/**
 * Interview intake — signed-URL minter.
 *
 * The browser never holds a credential. It asks this function for a one-shot
 * upload URL; the function signs one with the service account and returns it.
 * The URL is good for ten minutes, for exactly one object name it chooses, for
 * exactly one content type, within a size range it pins. Nothing else.
 *
 * Deliberately anonymous: no per-person links, no tokens tied to a recipient.
 * A unique URL per invitee would tell the author who responded, which is the
 * one thing the consent text promises it cannot.
 */

const { Storage } = require('@google-cloud/storage');
const crypto = require('crypto');

const BUCKET = process.env.INTAKE_BUCKET || 'pitch-rise-interview-intake';
const MAX_BYTES = 512 * 1024;
const URL_TTL_MS = 10 * 60 * 1000;

const storage = new Storage();

exports.mintUpload = async (req, res) => {
  res.set('Access-Control-Allow-Origin', '*');
  res.set('Vary', 'Origin');

  if (req.method === 'OPTIONS') {
    res.set('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.set('Access-Control-Allow-Headers', 'Content-Type');
    res.set('Access-Control-Max-Age', '3600');
    return res.status(204).send('');
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'POST only' });
  }

  try {
    // The function picks the name, not the client. A client-chosen name is a
    // place to hide identifying information.
    const objectName = `${crypto.randomUUID()}.md`;

    const [url] = await storage
      .bucket(BUCKET)
      .file(objectName)
      .getSignedUrl({
        version: 'v4',
        action: 'write',
        expires: Date.now() + URL_TTL_MS,
        contentType: 'text/markdown',
        // Signed into the URL: an upload outside this range is rejected by GCS,
        // not by us. The client must echo this header or the signature fails.
        extensionHeaders: {
          'x-goog-content-length-range': `1,${MAX_BYTES}`,
        },
      });

    return res.status(200).json({
      url,
      maxBytes: MAX_BYTES,
      lengthRangeHeader: `1,${MAX_BYTES}`,
    });
  } catch (err) {
    console.error('mint failed', err);
    return res.status(500).json({ error: 'could not mint an upload URL' });
  }
};
