import { put } from '@vercel/blob';

export const config = {
  api: {
    bodyParser: false,
  },
};

const MAX_BYTES = 4 * 1024 * 1024;
const ALLOWED_TYPES = new Set([
  'audio/mpeg', 'audio/mp3', 'audio/wav', 'audio/x-wav', 'audio/wave',
  'audio/mp4', 'audio/x-m4a', 'audio/ogg', 'audio/aac', 'audio/flac',
  'audio/webm', 'audio/*'
]);

function safeName(name) {
  const clean = String(name || 'song').replace(/[^a-zA-Z0-9._-]/g, '_');
  return clean.slice(-120) || 'song';
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const contentLength = Number(req.headers['content-length'] || 0);
  if (contentLength > MAX_BYTES) {
    return res.status(413).json({ error: 'Song must be 4 MB or smaller.' });
  }

  const contentType = String(req.headers['content-type'] || 'application/octet-stream').split(';')[0].toLowerCase();
  if (contentType !== 'application/octet-stream' && !contentType.startsWith('audio/')) {
    return res.status(415).json({ error: 'Please upload an audio file.' });
  }

  try {
    const chunks = [];
    let total = 0;
    for await (const chunk of req) {
      total += chunk.length;
      if (total > MAX_BYTES) {
        return res.status(413).json({ error: 'Song must be 4 MB or smaller.' });
      }
      chunks.push(Buffer.from(chunk));
    }

    if (!total) return res.status(400).json({ error: 'No audio file received.' });

    const filename = safeName(decodeURIComponent(req.headers['x-filename'] || 'song'));
    const ext = filename.includes('.') ? '' : '.mp3';
    const pathname = `wishcraft/audio/${crypto.randomUUID()}-${filename}${ext}`;

    const blob = await put(pathname, Buffer.concat(chunks), {
      access: 'public',
      contentType: contentType === 'application/octet-stream' ? 'audio/mpeg' : contentType,
      addRandomSuffix: false,
    });

    return res.status(200).json({
      url: blob.url,
      pathname: blob.pathname,
      contentType: blob.contentType,
      size: total,
    });
  } catch (error) {
    console.error('WishCraft audio upload error:', error);
    return res.status(500).json({
      error: 'Vercel Blob upload failed. Connect a Vercel Blob store to this project and redeploy.'
    });
  }
}
