# WishCraft — Photo Storage Fix

This version stores the main photo and memory photos in Vercel Blob instead of embedding their Base64 data inside the WhatsApp/share URL.

The browser compresses photos first, then uploads them to `/api/upload-image`. The wish link contains only short public image URLs.

Keep the existing Vercel Blob store connected to both Production and Preview, then redeploy.
