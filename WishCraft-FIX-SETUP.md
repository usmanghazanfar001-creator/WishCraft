# WishCraft animation + share-link fix

## Files
- Replace your current `index.html` with `WishCraft-fixed.html`.
- Create `api/wish.js` and paste the supplied `api/wish.js` file there.
- Add `@vercel/blob` to your existing `package.json` dependencies (do not overwrite an existing package.json).

## Vercel
1. Open the Vercel project used by WishCraft.
2. Add/connect a Vercel Blob store to the project.
3. Deploy with the `api/wish.js` function.
4. The app will POST wishes with media to `/api/wish`; the response contains a short public Blob URL.

The old implementation put compressed photos and the uploaded audio directly inside `#wish=...`. That is why WhatsApp showed a huge green base64 string. The new implementation stores media-bearing wishes in Blob and puts only a short pointer in the shared URL.

## Important payload limit
The supplied function rejects a wish above about 3.9 MB. If a wish is too large, reduce the number/size of photos or the audio file. This keeps it below Vercel Function request limits.
