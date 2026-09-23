import { put } from '@vercel/blob';
import { randomUUID } from 'node:crypto';

export const config = { api: { bodyParser: false } };
const MAX_BYTES = 4 * 1024 * 1024; // fallback proxy only

function safeName(name) {
  const clean = String(name || 'photo.jpg').replace(/[^a-zA-Z0-9._-]/g, '_');
  return clean.slice(-120) || 'photo.jpg';
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }
  const contentType = String(req.headers['content-type'] || '').split(';')[0].toLowerCase();
  if (!contentType.startsWith('image/')) return res.status(415).json({ error: 'Please upload an image.' });
  const contentLength = Number(req.headers['content-length'] || 0);
  if (contentLength > MAX_BYTES) return res.status(413).json({ error: 'Photo must be 4 MB or smaller.' });
  try {
    const chunks = []; let total = 0;
    for await (const chunk of req) {
      total += chunk.length;
      if (total > MAX_BYTES) return res.status(413).json({ error: 'Photo must be 4 MB or smaller.' });
      chunks.push(Buffer.from(chunk));
    }
    if (!total) return res.status(400).json({ error: 'No image received.' });
    const filename = safeName(decodeURIComponent(req.headers['x-filename'] || 'photo.jpg'));
    const pathname = `wishcraft/images/${randomUUID()}-${filename}`;
    const blob = await put(pathname, Buffer.concat(chunks), {
      access: 'public',
      contentType,
      addRandomSuffix: false,
    });
    return res.status(200).json({ url: blob.url, pathname: blob.pathname, contentType: blob.contentType, size: total });
  } catch (error) {
    console.error('WishCraft image upload error:', error);
    return res.status(500).json({ error: 'Vercel Blob image upload failed. Make sure the Blob store is connected to this project and redeploy.' });
  }
}
