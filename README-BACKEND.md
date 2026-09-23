# WishCraft — Backend storage setup

Photos, the song and the wish itself are now stored in **Vercel Blob** (your backend).
The link you share is short: `https://your-site.vercel.app/?w=Ab3xK9pQzM`

## How it works
1. **Photo / song chosen** → browser resizes photos, then uploads the file directly to Blob
   (`/api/upload-token` authorises it). Songs up to **25 MB**, photos compressed to ≤1600 px.
2. **Generate link** → `POST /api/wish` saves the wish JSON (text + media URLs) → returns a short id.
3. **Recipient opens `?w=id`** → `GET /api/wish?id=…` loads the wish, photos and song play.

Old `#wish=` / `#wishurl=` links still open.

## Deploy
1. Vercel → Project → **Storage → Create/Connect Blob store** (Production + Preview).
2. Deploy this folder (root has `index.html`, `api/`, `package.json`).
3. Redeploy after connecting the store.

## Files
- `api/upload-token.js` – token for direct browser → Blob uploads (large files)
- `api/wish.js` – save (POST) / load (GET) a wish; only accepts media hosted in your Blob store
- `api/upload-image.js`, `api/upload-audio.js` – ≤4 MB fallback if direct upload is unavailable

Note: the browser loads the Blob client from `esm.sh`; if it is blocked, files ≤4 MB still use the fallback.

## Poster → Video / GIF
Poster tab → **Download Video** (6‑second looping MP4, or WebM on browsers without MP4 recording)
or **Download GIF** (480 px wide, loops forever). Runs entirely in the browser; the GIF encoder
loads from cdnjs on first use.

## Poster effects
Effects: Balloons, Confetti, Sparkles, Hearts, None (slow zoom). Use **▶ Preview Animation** to watch the
looping animation full-screen before exporting it as Video or GIF.
