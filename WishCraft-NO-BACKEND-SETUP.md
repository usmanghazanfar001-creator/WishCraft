# WishCraft — no-backend share fix

## What changed
- The uploaded song is still available in the creator's in-app preview.
- The song is **not included in the generated share URL**.
- Photos and wish text remain self-contained in the URL.
- A live share-size warning appears while editing.
- Very large photo-heavy links are blocked with a clear message instead of producing a broken WhatsApp share.
- Confetti, balloons, sparkles, fireworks, hearts, and golden particles use CSS/drawn shapes and motion rather than floating emoji.

## Deploy
1. Replace your current `index.html` with `index.html` from this package.
2. No API route or database is required for this version.
3. Deploy normally to Vercel, Netlify, GitHub Pages, or another static host.

## Important sharing behavior
The creator can upload a song and hear it in Preview. When the share link is generated, WishCraft removes only the audio field from the shared copy. The original editor state is untouched, so the song remains available locally.

Photos are compressed before being placed in the link. If the resulting URL becomes very large, WishCraft shows a warning and blocks generation above the safety threshold.
