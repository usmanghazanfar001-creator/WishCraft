import { put, head } from '@vercel/blob';
import { randomBytes } from 'node:crypto';

export const config = { api: { bodyParser: false } };

/**
 * POST /api/wish        -> saves the complete wish JSON in Blob storage, returns { id }
 * GET  /api/wish?id=XXX -> returns the saved wish JSON
 *
 * Photos and the song are uploaded separately (see upload-token.js / upload-image.js /
 * upload-audio.js); the wish JSON only stores their public URLs, so the shared
 * link is just  https://your-site/?w=<id>
 */
const MAX_JSON_BYTES = 200 * 1024;            // text + URLs only; media never goes through here
const ID_RE = /^[A-Za-z0-9_-]{6,40}$/;
const ALPHABET = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789';

function newId(len = 10) {
  const bytes = randomBytes(len);
  let s = '';
  for (let i = 0; i < len; i++) s += ALPHABET[bytes[i] % ALPHABET.length];
  return s;
}

function isBlobUrl(u) {
  try {
    const url = new URL(u);
    return url.protocol === 'https:' && url.hostname.endsWith('.public.blob.vercel-storage.com');
  } catch { return false; }
}

// Only allow media that lives in our own Blob store (no data: URIs, no random hosts).
function validateMedia(wish) {
  if (wish.mainPhoto && !isBlobUrl(wish.mainPhoto)) return 'Main photo is not uploaded yet.';
  if (Array.isArray(wish.photos)) {
    for (const p of wish.photos) if (!p || !isBlobUrl(p.url)) return 'A memory photo is not uploaded yet.';
    if (wish.photos.length > 10) return 'Maximum 10 memory photos.';
  }
  if (wish.audio && !isBlobUrl(wish.audio.data)) return 'Song is not uploaded yet.';
  return null;
}

export default async function handler(req, res) {
  if (req.method === 'GET') {
    const id = String(req.query?.id || new URL(req.url, 'http://x').searchParams.get('id') || '');
    if (!ID_RE.test(id)) return res.status(400).json({ error: 'Invalid wish id.' });
    try {
      const meta = await head(`wishcraft/wishes/${id}.json`);
      const r = await fetch(meta.url);
      if (!r.ok) throw new Error('fetch failed');
      res.setHeader('Cache-Control', 'public, s-maxage=3600, stale-while-revalidate=86400');
      return res.status(200).json(await r.json());
    } catch (e) {
      return res.status(404).json({ error: 'This birthday wish was not found.' });
    }
  }

  if (req.method !== 'POST') {
    res.setHeader('Allow', 'GET, POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const chunks = [];
    let total = 0;
    for await (const c of req) {
      total += c.length;
      if (total > MAX_JSON_BYTES) return res.status(413).json({ error: 'Wish text is too large.' });
      chunks.push(Buffer.from(c));
    }
    const wish = JSON.parse(Buffer.concat(chunks).toString('utf8') || 'null');

    if (!wish || typeof wish !== 'object' || typeof wish.name !== 'string' || !wish.name.trim()) {
      return res.status(400).json({ error: 'A birthday name is required.' });
    }
    const mediaError = validateMedia(wish);
    if (mediaError) return res.status(400).json({ error: mediaError });

    const id = newId();
    await put(`wishcraft/wishes/${id}.json`, JSON.stringify(wish), {
      access: 'public',
      contentType: 'application/json',
      addRandomSuffix: false,
    });

    return res.status(200).json({ id });
  } catch (error) {
    console.error('Wish storage error:', error);
    return res.status(500).json({ error: 'Could not save the birthday wish. Is the Blob store connected?' });
  }
}
