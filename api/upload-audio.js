import { put } from '@vercel/blob';

export const config = {
  api: { bodyParser: false },
};

const MAX_BYTES = 4 * 1024 * 1024;

function cleanName(value = 'birthday-song') {
  let name = decodeURIComponent(value).replace(/[^a-zA-Z0-9._-]/g, '-');
  if (!name || name === '.' || name === '..') name = 'birthday-song';
  return name.slice(-120);
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const contentLength = Number(req.headers['content-length'] || 0);
  if (contentLength > MAX_BYTES) {
    return res.status(413).json({ error: 'Song is too large. Please choose an audio file under 4 MB.' });
  }

  try {
    const chunks = [];
    let total = 0;

    for await (const chunk of req) {
      const part = Buffer.from(chunk);
      total += part.length;
      if (total > MAX_BYTES) {
        return res.status(413).json({ error: 'Song is too large. Please choose an audio file under 4 MB.' });
      }
      chunks.push(part);
    }

    if (!total) {
      return res.status(400).json({ error: 'No audio file was received.' });
    }

    const contentType = String(req.headers['content-type'] || 'application/octet-stream');
    if (!contentType.startsWith('audio/')) {
      return res.status(400).json({ error: 'Only audio files can be uploaded.' });
    }

    const originalName = cleanName(req.headers['x-filename'] || 'birthday-song');
    const id = crypto.randomUUID();
    const blob = await put(`wishcraft/audio/${id}-${originalName}`, Buffer.concat(chunks), {
      access: 'public',
      contentType,
      addRandomSuffix: false,
    });

    return res.status(200).json({
      url: blob.url,
      pathname: blob.pathname,
    });
  } catch (error) {
    console.error('WishCraft audio upload error:', error);
    return res.status(500).json({ error: 'Could not upload the song. Make sure Vercel Blob is connected to this project.' });
  }
}
