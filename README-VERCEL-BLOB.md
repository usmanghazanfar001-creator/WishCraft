# WishCraft — Vercel Blob song upload setup

This version includes the missing `/api/upload-audio` endpoint. Without that endpoint, the browser can preview a song locally but cannot upload it for sharing/export.

## 1. Deploy the project

Upload/deploy this folder as the Vercel project root. It contains:

- `index.html`
- `api/upload-audio.js`
- `package.json`

## 2. Connect Vercel Blob

In Vercel Dashboard:

Project → Storage → Create/Connect Blob → create a Blob store → connect it to this project.

New Blob stores can use Vercel OIDC authentication. Vercel Functions receive the authentication automatically when the store is connected to the project.

## 3. Redeploy

Redeploy after connecting the store so the Function can use the Blob store.

## 4. Test

Open the app → Generate Poster → Background Music → Add music.

You should see:

`Uploading music to Vercel Blob…`

then:

`✓ Music uploaded to Vercel Blob and ready for sharing.`

## Important

The current UI limits shareable audio to 4 MB because it sends the file through the `/api/upload-audio` Vercel Function. For larger songs, the next upgrade should use Vercel Blob direct browser uploads with a signed upload URL/multipart upload.
