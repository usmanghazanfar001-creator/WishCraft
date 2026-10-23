"# WishCraft" 


## What's new (WishCraft+)
All new options are **off by default** — existing wishes and old share links play exactly as before.

**New scenes** (Step "✦ Bonus Scenes & Extras")
- 🕯️ *Blow the Candles* cake ceremony (alternative to Cut the Cake; tap the button or a candle)
- ⏱️ 3·2·1 countdown before the reveal
- 🎂 Age counter scene (counts up to the age)
- 💛 "Reasons you're special" cards (up to 6 lines, custom title)
- 🎟️ Scratch-card surprise (hidden message / gift idea)

**New tools**
- 🔒 Lock-until date/time (recipients see a live countdown)
- 🎼 Music-box "Happy Birthday" melody when no song is uploaded
- Quick message styles (heartfelt, funny, short, formal, blessing, Urdu)
- Draft auto-save on the creator's device ("Start fresh" clears it)
- ✕ Exit button / Esc to close the preview, ↻ Watch Again, 💌 Say Thanks (recipients)

**New looks**: 6 themes (22 total), 2 frames (11 total), 3 effects (Petals, Bubbles, Shooting Stars), 4 poster templates, 2 poster message styles.

**Fixes**: the memory-photo story now continues to the reveal (it looped on the last photo); effect pieces no longer squash the hero photo; "Create Your Own" works for recipients; captions/sender are HTML-escaped.

No backend changes: new fields are plain JSON stored by the existing `/api/wish`.


## Site structure (SEO / AdSense update)
- `index.html` – content landing page (ads allowed here). Old `#wish=` / `?w=` links opened here redirect to the viewer.
- `create.html` – wish creator + poster tool and the recipient viewer (served at `/create`; `/?w=ID` is rewritten to it by `vercel.json`). No ads here.
- `guides/*.html`, `faq.html`, `about.html`, `contact.html`, `privacy.html`, `terms.html` – content pages.
- Content pages are generated: edit `_src/*.py`, then run `WISHCRAFT_CONTACT_EMAIL=you@example.com python3 _src/build.py` (also regenerates `sitemap.xml` and `robots.txt`).
