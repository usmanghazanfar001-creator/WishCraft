import { put } from '@vercel/blob';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const contentLength = Number(req.headers['content-length'] || 0);
  if (contentLength && contentLength > 4_000_000) {
    return res.status(413).json({
      error: 'Wish payload is too large. Reduce photos or audio.'
    });
  }

  try {
    const chunks = [];
    for await (const chunk of req) chunks.push(Buffer.from(chunk));
    const body = Buffer.concat(chunks).toString('utf8');

    if (!body || Buffer.byteLength(body, 'utf8') > 3_900_000) {
      return res.status(413).json({
        error: 'Wish payload is too large. Reduce photos or audio.'
      });
    }

    const wish = JSON.parse(body);

    if (!wish || typeof wish !== 'object' || typeof wish.name !== 'string' || !wish.name.trim()) {
      return res.status(400).json({ error: 'A birthday name is required.' });
    }

    // Store the complete wish outside the URL. The public URL returned by
    // Vercel Blob is short enough to share through WhatsApp/social apps.
    const id = crypto.randomUUID();
    const blob = await put(`wishcraft/${id}.json`, JSON.stringify(wish), {
      access: 'public',
      contentType: 'application/json',
      addRandomSuffix: false,
    });

    return res.status(200).json({
      id,
      url: blob.url,
    });
  } catch (error) {
    console.error('Wish storage error:', error);
    return res.status(500).json({ error: 'Could not save the birthday wish.' });
  }
}
