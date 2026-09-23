import { handleUpload } from '@vercel/blob/client';

/**
 * Issues short-lived tokens so the BROWSER uploads photos / songs straight to
 * Vercel Blob storage. This bypasses the ~4.5 MB Vercel Function body limit,
 * so songs up to 25 MB and full-quality photos work.
 */
const IMAGE_MAX = 8 * 1024 * 1024;
const AUDIO_MAX = 25 * 1024 * 1024;

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const chunks = [];
    for await (const c of req) chunks.push(Buffer.from(c));
    const body = JSON.parse(Buffer.concat(chunks).toString('utf8') || '{}');

    const json = await handleUpload({
      body,
      request: req,
      onBeforeGenerateToken: async (pathname) => {
        const isImage = pathname.startsWith('wishcraft/images/');
        const isAudio = pathname.startsWith('wishcraft/audio/');
        if (!isImage && !isAudio) throw new Error('Invalid upload path.');
        return {
          allowedContentTypes: isImage
            ? ['image/jpeg', 'image/png', 'image/webp']
            : ['audio/*', 'application/octet-stream'],
          maximumSizeInBytes: isImage ? IMAGE_MAX : AUDIO_MAX,
          addRandomSuffix: true,
        };
      },
      // Nothing to record here: the wish JSON (saved via /api/wish) keeps the URLs.
      onUploadCompleted: async () => {},
    });

    return res.status(200).json(json);
  } catch (error) {
    console.error('WishCraft upload-token error:', error);
    return res.status(400).json({ error: error.message || 'Could not authorize upload.' });
  }
}
