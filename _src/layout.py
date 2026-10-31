import json, html, os
SITE = "https://wishcrafting.vercel.app"
NAME = "WishCraft"
ADSENSE = "ca-pub-7402751690588915"
# Set this to the address visitors should write to (shown on /contact and in the privacy policy).
CONTACT_EMAIL = os.environ.get("WISHCRAFT_CONTACT_EMAIL", "YOUR-EMAIL@example.com")
TODAY = "2026-10-23"

NAV = [("/", "Home"), ("/wishes", "Wishes"), ("/guides", "Guides"), ("/faq", "FAQ"), ("/about", "About")]

CSS = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "site.css"), encoding="utf8").read()

def esc(s): return html.escape(s, quote=True)

def jsonld(objs):
    return "".join('<script type="application/ld+json">%s</script>\n' % json.dumps(o, ensure_ascii=False) for o in objs)

def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (p, n) in enumerate(trail)]}

def page(path, title, desc, body, *, trail=None, schema=None, ads=True, og_type="website", current=None, modified=TODAY):
    url = SITE + path
    nav = "".join('<a href="%s"%s>%s</a>' % (p, ' aria-current="page"' if p == current else "", n) for p, n in NAV)
    ld = [{"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": SITE + "/", "logo": SITE + "/favicon.png"}] if path == "/" else []
    if trail: ld.append(crumbs_ld(trail))
    ld += schema or []
    crumb_html = ""
    if trail and len(trail) > 1:
        parts = []
        for i, (p, n) in enumerate(trail):
            parts.append(esc(n) if i == len(trail) - 1 else '<a href="%s">%s</a>' % (p, esc(n)))
        crumb_html = '<nav class="crumbs" aria-label="Breadcrumb">%s</nav>' % " › ".join(parts)
    adsense = ("""<script>
/* Load AdSense on first interaction (scroll/tap/key) or after 8s, so ads never delay first paint or Core Web Vitals. */
(function(){var d=false;function go(){if(d)return;d=true;var s=document.createElement('script');s.async=true;s.crossOrigin='anonymous';s.src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=%s';document.head.appendChild(s);}
function later(){setTimeout(go,8000);}
if(document.readyState==='complete')later();else addEventListener('load',later);
['scroll','pointerdown','keydown','touchstart'].forEach(function(e){addEventListener(e,go,{once:true,passive:true});});})();
</script>
""" % ADSENSE) if ads else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0a0e1a">
<meta name="google-adsense-account" content="{ADSENSE}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/favicon.png">
<style>{CSS}</style>
{"<link rel=\"preconnect\" href=\"https://pagead2.googlesyndication.com\" crossorigin>" if ads else ""}
{jsonld(ld)}{adsense}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap">
<a class="brand" href="/">✦ WishCraft</a>
<nav class="main" aria-label="Main">{nav}<a class="btn" href="/create">Create a wish</a></nav>
</div></header>
<main id="main">
{crumb_html and '<div class="narrow">' + crumb_html + '</div>'}
{body}
</main>
<footer class="site"><div class="wrap">
<div class="cols">
<div><p class="fh">✦ WishCraft</p><p>A free birthday wish and poster maker. Add photos, music and a message, then share one private link.</p></div>
<div><p class="fh">Make something</p><ul><li><a href="/create">Birthday wish creator</a></li><li><a href="/create">Poster, video &amp; GIF maker</a></li><li><a href="/guides/how-to-create-a-birthday-surprise-link">How it works</a></li></ul></div>
<div><p class="fh">Birthday wishes</p><ul><li><a href="/wishes/birthday-wishes-for-friend">For a friend</a></li><li><a href="/wishes/birthday-wishes-for-mother">For a mother</a></li><li><a href="/wishes/birthday-wishes-in-urdu">In Urdu</a></li><li><a href="/wishes/funny-birthday-wishes">Funny wishes</a></li><li><a href="/wishes">All wishes</a></li></ul></div>
<div><p class="fh">Guides</p><ul><li><a href="/guides/how-to-write-a-heartfelt-birthday-message">Write a heartfelt message</a></li><li><a href="/guides/birthday-photo-tips-for-memory-stories">Photo tips</a></li><li><a href="/guides">All guides</a></li></ul></div>
<div><p class="fh">Company</p><ul><li><a href="/about">About</a></li><li><a href="/faq">FAQ</a></li><li><a href="/contact">Contact</a></li><li><a href="/privacy">Privacy policy</a></li><li><a href="/terms">Terms of use</a></li></ul></div>
</div>
<div class="copy">© 2026 WishCraft. All rights reserved.</div>
</div></footer>
</body>
</html>
'''

def article_schema(path, headline, desc):
    return {"@context": "https://schema.org", "@type": "Article", "headline": headline, "description": desc,
            "mainEntityOfPage": SITE + path, "image": SITE + "/og-image.png",
            "datePublished": TODAY, "dateModified": TODAY,
            "author": {"@type": "Organization", "name": NAME, "url": SITE + "/"},
            "publisher": {"@type": "Organization", "name": NAME, "logo": {"@type": "ImageObject", "url": SITE + "/favicon.png"}}}

def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
