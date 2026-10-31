#!/usr/bin/env python3
"""Static site generator for WishCraft content pages. Run from the project root:  python3 _src/build.py
Set WISHCRAFT_CONTACT_EMAIL to your public contact address before building."""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import *
from guides_a import G as GA
from guides_b import G as GB
from wishes_a import W as WA
from wishes_b import W as WB
from wishes_c import W as WC

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUIDES = {}; GUIDES.update(GA); GUIDES.update(GB)
ORDER = ["how-to-create-a-birthday-surprise-link", "birthday-wishes-messages", "how-to-write-a-heartfelt-birthday-message",
         "birthday-photo-tips-for-memory-stories", "birthday-poster-design-guide", "long-distance-birthday-surprise-ideas",
         "share-birthday-wishes-on-whatsapp"]
assert set(ORDER) == set(GUIDES)
urls = []

def write(path, content, sitemap=True, prio="0.6"):
    fn = os.path.join(ROOT, path.strip("/") + ".html") if path != "/" else os.path.join(ROOT, "index.html")
    if path == "/guides": fn = os.path.join(ROOT, "guides", "index.html")
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    open(fn, "w", encoding="utf8").write(content)
    if sitemap: urls.append((path, prio))

def related(slug):
    items = [s for s in ORDER if s != slug][:3]
    cards = "".join('<a class="card" href="/guides/%s"><h3>%s</h3><p>%s</p></a>' % (s, esc(GUIDES[s]["title"]), esc(GUIDES[s]["desc"])) for s in items)
    return '<div class="related"><h2>Keep reading</h2><div class="grid">%s</div></div>' % cards

# ---------------- guides
for slug, g in GUIDES.items():
    path = "/guides/" + slug
    body = f'''<article class="narrow">
<p class="kicker">{esc(g["cat"])} · {g["read"]}</p>
<h1>{esc(g["title"])}</h1>
<p class="meta">By WishCraft · Updated October 23, 2026</p>
{g["body"]()}
{related(slug)}
</article>'''
    write(path, page(path, g["meta_title"], g["desc"], body,
        trail=[("/", "Home"), ("/guides", "Guides"), (path, g["title"])],
        schema=[article_schema(path, g["title"], g["desc"])], og_type="article", current="/guides"), prio="0.8")

# ---------------- guides index
cards = "".join('<a class="card" href="/guides/%s"><p class="kicker">%s</p><h2>%s</h2><p>%s</p></a>' % (s, esc(GUIDES[s]["cat"]), esc(GUIDES[s]["title"]), esc(GUIDES[s]["desc"])) for s in ORDER)
body = f'''<div class="narrow"><h1>Birthday Guides, Ideas &amp; Message Help</h1>
<p>Practical guides from WishCraft: how to write a message that sounds like you, how to choose photos, how to design a poster and how to surprise someone who lives far away. Every guide is free to read and written to be useful with or without our tools.</p></div>
<div class="wrap"><div class="grid">{cards}</div></div>
<div class="narrow"><div class="callout"><p>Want to put the advice to work? <a href="/create">Open the WishCraft creator</a> and build an animated birthday wish or a poster in minutes.</p></div></div>'''
write("/guides", page("/guides", "Birthday Guides, Message Ideas & Surprise Tips | WishCraft",
    "Free guides on writing birthday messages, choosing photos, designing posters, sharing on WhatsApp and planning long-distance surprises.",
    body, trail=[("/", "Home"), ("/guides", "Guides")], current="/guides",
    schema=[{"@context": "https://schema.org", "@type": "CollectionPage", "name": "WishCraft Birthday Guides", "url": SITE + "/guides",
             "hasPart": [{"@type": "Article", "headline": GUIDES[s]["title"], "url": SITE + "/guides/" + s} for s in ORDER]}]), prio="0.8")

# ---------------- FAQ
FAQ = [
 ("What is WishCraft?", "WishCraft is a free web tool for creating animated birthday wishes and birthday posters. You add a name, photos, a message and optional music, preview the result, and share it with a single link. You can also make a poster image, a short video or a GIF."),
 ("Is WishCraft really free?", "Yes. You can create wishes and posters without paying and without creating an account. The site shows advertising on its guide and information pages to cover running costs."),
 ("Do I need to sign up or install anything?", "No. WishCraft runs in your browser on phones, tablets and computers. Recipients just open the link."),
 ("What do I need to make a wish?", "Only the birthday person's name is required. Photos, a song, a message, themes, animations and bonus scenes are all optional."),
 ("How many photos can I add?", "One main photo and up to ten memory photos. Photos are resized and compressed automatically so the wish loads quickly on mobile data."),
 ("Can I add my own music?", "Yes. You can upload an audio file up to 25 MB and choose the start and end points. If you don't add a song you can turn on a built-in music-box version of Happy Birthday. Only upload music you have the right to share."),
 ("Why doesn't the music start automatically for the recipient?", "Most phones and browsers block sound until the person taps the screen. WishCraft starts with an Open button so the music can begin right after the first tap."),
 ("How long does a shared link last?", "Wishes are stored so the link keeps working. We may remove old or reported content. If you want your wish removed, contact us with the link and we will delete it."),
 ("Who can see my wish?", "Anyone who has the link can open it, so share it only with the people you intend. Links are randomly generated and are not listed anywhere, and shared wishes are asked not to be indexed by search engines."),
 ("Can I schedule a wish for the birthday itself?", "Yes. Use the lock option to choose a date and time. If someone opens the link early they will see a countdown instead of the surprise."),
 ("Does the poster generator work on a phone?", "Yes. You can design the poster on your phone and download it as a 1080 × 1350 image. Video and GIF export run in your browser and may take a few seconds, depending on your device."),
 ("I lost my half-finished wish. Can I get it back?", "The creator auto-saves a draft on the device and browser you were using. Open the creator again on the same browser and use the draft bar at the top to continue."),
 ("What languages are supported?", "The interface is in English, and your message can be in any language your device can type. There is also an Urdu quick-message style to help you get started."),
 ("How do I report a problem or request removal?", "Visit the contact page and include the link. We review requests as quickly as we can."),
]
body = '<div class="narrow"><h1>Frequently Asked Questions</h1><p>Short answers about how WishCraft works. If you can\'t find yours, <a href="/contact">get in touch</a>.</p>' + \
       "".join("<details><summary>%s</summary><p>%s</p></details>" % (esc(q), esc(a)) for q, a in FAQ) + \
       '<div class="callout"><p>Ready to try it? <a href="/create">Create a birthday wish</a> or read the <a href="/guides/how-to-create-a-birthday-surprise-link">step-by-step tutorial</a>.</p></div></div>'
write("/faq", page("/faq", "WishCraft FAQ: Questions About Birthday Wishes, Links & Privacy",
    "Answers about how WishCraft works: cost, photos, music, link privacy, scheduling, posters, video and GIF export.",
    body, trail=[("/", "Home"), ("/faq", "FAQ")], current="/faq", schema=[faq_schema(FAQ)]), prio="0.7")

# ---------------- About
body = '''<div class="narrow"><h1>About WishCraft</h1>
<p>WishCraft started with a simple observation: most birthday messages are forgettable not because people don't care, but because the tools for sending something more personal are either complicated or expensive. We wanted to make it easy to turn a few photos, a song and a few honest sentences into a small moment someone will remember.</p>
<h2>What we make</h2>
<ul>
<li><strong>The wish creator:</strong> an animated, shareable birthday experience with a gift box, a cake ceremony, a photo memory story and a personal message.</li>
<li><strong>The poster generator:</strong> a quick way to design a birthday poster and export it as an image, short video or GIF.</li>
<li><strong>The guides:</strong> free articles on writing messages, choosing photos, designing posters and planning surprises.</li>
</ul>
<h2>What we believe</h2>
<ul>
<li><strong>Personal beats polished.</strong> A sincere line with a real memory is better than a perfect template.</li>
<li><strong>No barriers.</strong> No sign-up, no app to install, nothing for the recipient to download.</li>
<li><strong>Respect for privacy.</strong> We only store what is needed to make your link work, and we explain it plainly in our <a href="/privacy">privacy policy</a>.</li>
<li><strong>Honest content.</strong> Our guides are written to help, not to stuff keywords.</li>
</ul>
<h2>How we make money</h2>
<p>WishCraft is free to use. We show advertising on our guides and information pages. The wish creator and recipient experience are kept free of ads so the moment stays about the person being celebrated.</p>
<h2>Who we are</h2>
<p>WishCraft is an independent project that loves celebrations and simple, well-made web tools. Feedback from the people who use it decides what gets built next.</p>
<h2>Get in touch</h2>
<p>Questions, ideas or problems? Visit our <a href="/contact">contact page</a>.</p></div>'''
write("/about", page("/about", "About WishCraft: A Free, Personal Birthday Wish Maker",
    "Learn who makes WishCraft, what the tools do, how we handle privacy and how the site is funded.", body,
    trail=[("/", "Home"), ("/about", "About")], current="/about"), prio="0.5")

# ---------------- Contact
body = f'''<div class="narrow"><h1>Contact WishCraft</h1>
<p>We'd love to hear from you. Use the address below for questions, bug reports, feature ideas, partnership enquiries and content-removal requests.</p>
<div class="card"><h3>Email</h3><p><a href="mailto:{esc(CONTACT_EMAIL)}">{esc(CONTACT_EMAIL)}</a></p><p>We usually reply within a few days.</p></div>
<h2>Requesting removal of a wish</h2>
<p>If a wish contains your photo or information and you want it removed, email us the full link (for example <code>https://wishcrafting.vercel.app/?w=…</code>) and we will delete it. If the wish is yours, tell us you are its creator; if you are in the photos but did not create it, tell us that instead.</p>
<h2>Reporting a problem</h2>
<p>For bugs, please tell us your device, browser, what you were doing and what happened. A screenshot helps.</p>
<h2>Before you write</h2>
<p>Your question may already be answered in our <a href="/faq">FAQ</a> or in the <a href="/guides/how-to-create-a-birthday-surprise-link">step-by-step tutorial</a>.</p></div>'''
write("/contact", page("/contact", "Contact WishCraft: Support, Feedback & Removal Requests",
    "Get in touch with the WishCraft team for support, feedback, bug reports or to request removal of a shared wish.", body,
    trail=[("/", "Home"), ("/contact", "Contact")], current="/contact", ads=False), prio="0.4")

# ---------------- Privacy
body = f'''<div class="narrow"><h1>Privacy Policy</h1>
<p class="meta">Last updated: October 23, 2026</p>
<p>This policy explains what information WishCraft ("we", "us") handles when you use <strong>wishcrafting.vercel.app</strong>, why we handle it and what choices you have.</p>
<h2>1. Information you provide</h2>
<p>When you create a birthday wish, you may enter a name, age, relationship, text messages, photos, an audio file and settings such as theme and unlock time. When you press <em>Create Wish &amp; Generate Link</em>, this content is uploaded and stored so that the link you share can display it. Your photos and audio are stored as files and the text and settings are stored as a small data file that is retrieved using a randomly generated identifier.</p>
<p>The poster generator runs in your browser. Poster images, videos and GIFs are generated on your device and are not uploaded unless you use another tool to share them.</p>
<h2>2. Who can see your content</h2>
<p>Anyone who has your wish link can open it and see the photos, message and audio. Only share the link with people you trust, and do not upload photos or information you would not want a recipient to forward. We do not publish a directory of wishes and we ask search engines not to index shared wishes.</p>
<h2>3. Information stored on your device</h2>
<p>The creator saves a draft of your work in your browser's local storage so you can come back to it. It stays on your device and can be cleared at any time with the "Start fresh" button or by clearing your browser data.</p>
<h2>4. Information collected automatically</h2>
<p>Like most websites, our hosting provider, Vercel, and our storage provider process technical information such as IP address, browser type, pages requested and timestamps to deliver the site, keep it secure and diagnose errors.</p>
<h2>5. Advertising and cookies</h2>
<p>We use Google AdSense to show advertising on our guides and information pages. Google and its partners may use cookies and similar technologies to serve and measure ads, including ads based on your prior visits to this or other websites. Google's use of advertising cookies enables it and its partners to serve ads to you based on your visit to our site and other sites on the internet.</p>
<ul>
<li>You can opt out of personalized advertising at <a href="https://adssettings.google.com" rel="noopener">Google Ads Settings</a>.</li>
<li>You can learn how Google uses data from sites that use its services at <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">policies.google.com/technologies/partner-sites</a>.</li>
<li>You can also opt out of some third-party vendors' use of cookies for personalized advertising at <a href="https://www.aboutads.info" rel="noopener">aboutads.info</a>.</li>
</ul>
<p>Visitors in the European Economic Area, the United Kingdom and Switzerland may be shown a consent message so they can choose whether to allow advertising cookies. We do not display ads inside the wish creator or on shared wish pages.</p>
<h2>6. Third-party services</h2>
<p>The site uses services including Vercel (hosting and file storage), Google AdSense (advertising) and content delivery networks that supply open-source code libraries used for image and GIF export. These services have their own privacy policies.</p>
<h2>7. How we use information</h2>
<ul>
<li>To create, store and display the wishes you make</li>
<li>To operate, secure and improve the site</li>
<li>To respond to messages you send us</li>
<li>To show advertising that supports the free service</li>
</ul>
<p>We do not sell personal information and we do not use your photos or messages for advertising.</p>
<h2>8. Retention and removal</h2>
<p>Wishes remain available so that links keep working. You can ask us to delete a wish at any time by emailing us the link; see our <a href="/contact">contact page</a>. We may also remove content that is reported or that violates our <a href="/terms">terms</a>.</p>
<h2>9. Children</h2>
<p>WishCraft is not directed at children under 13 and we do not knowingly collect personal information from them. If you share photos of a child, make sure you are their parent or guardian or have the guardian's permission. If you believe a child's information has been uploaded without permission, contact us and we will remove it.</p>
<h2>10. Your rights</h2>
<p>Depending on where you live, you may have the right to access, correct or delete your information, or object to certain processing. To exercise these rights, contact us at <a href="mailto:{esc(CONTACT_EMAIL)}">{esc(CONTACT_EMAIL)}</a>.</p>
<h2>11. Changes</h2>
<p>We may update this policy and will change the date above when we do. Continued use of the site after a change means you accept the updated policy.</p>
<h2>12. Contact</h2>
<p>Questions about this policy? Email <a href="mailto:{esc(CONTACT_EMAIL)}">{esc(CONTACT_EMAIL)}</a>.</p></div>'''
write("/privacy", page("/privacy", "Privacy Policy | WishCraft",
    "How WishCraft handles your photos, messages, cookies and advertising, who can see shared wishes and how to request removal.", body,
    trail=[("/", "Home"), ("/privacy", "Privacy Policy")], ads=False), prio="0.3")

# ---------------- Terms
body = '''<div class="narrow"><h1>Terms of Use</h1>
<p class="meta">Last updated: October 23, 2026</p>
<p>By using WishCraft you agree to these terms. If you don't agree, please don't use the site.</p>
<h2>1. The service</h2>
<p>WishCraft provides free tools for creating birthday wishes and posters, plus informational articles. We may change, suspend or discontinue any part of the service at any time.</p>
<h2>2. Your content</h2>
<p>You keep ownership of the photos, audio and text you upload. You give us permission to store, process and display that content so that your wish and link work. You are responsible for your content and promise that you have the right to upload and share it.</p>
<h2>3. What you must not upload</h2>
<ul>
<li>Content that is unlawful, hateful, harassing, threatening or sexually explicit</li>
<li>Photos of other people, especially children, without the permission needed to share them</li>
<li>Music, images or other material you do not have the right to share</li>
<li>Malware or anything intended to harm devices or the service</li>
<li>Content designed to deceive, impersonate or defraud others</li>
</ul>
<p>We may remove content and disable links that break these rules or that are reported to us, without notice.</p>
<h2>4. Copyrighted music</h2>
<p>You are responsible for making sure you have the right to share any audio you upload. If you are a rights holder and believe content on the site infringes your rights, contact us with the link and details and we will review it promptly.</p>
<h2>5. Sharing and privacy</h2>
<p>Anyone with a link can open the wish it points to. Share links carefully. See our <a href="/privacy">privacy policy</a> for details.</p>
<h2>6. Acceptable use</h2>
<p>Don't attempt to disrupt the service, overload it with automated requests, access data that isn't yours or circumvent technical limits.</p>
<h2>7. No warranty</h2>
<p>The service is provided "as is" and "as available". We try to keep it reliable but cannot promise that it will always be available, error-free or that content will be stored forever. Keep your own copies of photos and music you care about.</p>
<h2>8. Limitation of liability</h2>
<p>To the extent permitted by law, we are not liable for indirect or consequential losses arising from your use of the service.</p>
<h2>9. Advertising and third-party links</h2>
<p>Our information pages show advertising and may link to other sites. We are not responsible for third-party content or services.</p>
<h2>10. Changes</h2>
<p>We may update these terms and will change the date above when we do. Continued use after a change means you accept the new terms.</p>
<h2>11. Contact</h2>
<p>Questions about these terms? See our <a href="/contact">contact page</a>.</p></div>'''
write("/terms", page("/terms", "Terms of Use | WishCraft",
    "The rules for using WishCraft: your content, acceptable use, copyrighted music, sharing and liability.", body,
    trail=[("/", "Home"), ("/terms", "Terms of Use")], ads=False), prio="0.3")


# ---------------- Wish pages (/wishes/<slug>) and hub
WISH = {}; WISH.update(WA); WISH.update(WB); WISH.update(WC)
WORDER = ["birthday-wishes-for-friend","birthday-wishes-for-best-friend","birthday-wishes-for-brother","birthday-wishes-for-sister",
          "birthday-wishes-for-mother","birthday-wishes-for-father","birthday-wishes-for-husband","birthday-wishes-for-wife",
          "birthday-wishes-for-son-and-daughter","birthday-wishes-for-boss-and-colleague","funny-birthday-wishes",
          "short-birthday-wishes-and-captions","birthday-wishes-in-urdu","islamic-birthday-wishes-and-duas","belated-birthday-wishes"]
assert set(WORDER) == set(WISH), set(WORDER) ^ set(WISH)

def wish_li(w, kind):
    if "||" in w:
        a, b = w.split("||", 1)
        if not b: return "<li>%s</li>" % esc(a)
        lang = "ur" if kind == "ur" else "ar"
        return '<li><span lang="%s" dir="rtl" style="display:block;font-size:1.25em;line-height:2;text-align:right">%s</span><span>%s</span></li>' % (lang, esc(a), esc(b))
    return "<li>%s</li>" % esc(w)

def wish_count(d): return sum(len(x[2]) for x in d["sections"])

for slug, d in WISH.items():
    path = "/wishes/" + slug
    kind = "ur" if d.get("urdu") else "ar"
    n = wish_count(d)
    secs = ""; toc = ""
    for i, (h, lead, items) in enumerate(d["sections"]):
        sid = "s%d" % (i + 1)
        toc += '<li><a href="#%s">%s</a></li>' % (sid, esc(h))
        secs += '<h2 id="%s">%s</h2>%s<ul class="wish-list">%s</ul>' % (sid, esc(h), ("<p>%s</p>" % esc(lead)) if lead else "", "".join(wish_li(w, "ur" if d.get("urdu") else "ar") for w in items))
    tips = "".join("<li>%s</li>" % esc(t) for t in d["tips"])
    rel = "".join('<a class="card" href="/wishes/%s"><h3>%s</h3><p>%s</p></a>' % (r, esc(WISH[r]["label"]) + " wishes", esc(WISH[r]["desc"])) for r in d["related"])
    body = f'''<article class="narrow">
<p class="kicker">Birthday wishes · {n} messages</p>
<h1>{esc(d["title"])}</h1>
<p class="meta">By WishCraft · Updated October 31, 2026 · Tap and hold any message to copy it</p>
{"".join("<p>%s</p>" % esc(x) for x in d["intro"])}
<div class="toc"><strong>On this page</strong><ul>{toc}</ul></div>
{secs}
<h2>Tips to make your message more personal</h2>
<ul>{tips}</ul>
<div class="callout"><p><strong>Make it a surprise, not just a text.</strong> Paste your favorite message into the <a href="/create">WishCraft birthday wish creator</a>, add a photo and a song, and send a private animated link, or turn it into a <a href="/create">birthday poster</a>. See the <a href="/guides/how-to-create-a-birthday-surprise-link">step-by-step tutorial</a>.</p></div>
<div class="related"><h2>More birthday wishes</h2><div class="grid">{rel}</div><p><a href="/wishes">Browse all birthday wishes →</a></p></div>
</article>'''
    write(path, page(path, d["meta"], d["desc"], body,
        trail=[("/", "Home"), ("/wishes", "Birthday wishes"), (path, d["label"] + " wishes")],
        schema=[article_schema(path, d["title"], d["desc"])], og_type="article", current="/wishes"), prio="0.8")

hub_cards = "".join('<a class="card" href="/wishes/%s"><p class="kicker">%d messages</p><h2>%s</h2><p>%s</p></a>' % (s_, wish_count(WISH[s_]), esc(WISH[s_]["meta"]), esc(WISH[s_]["desc"])) for s_ in WORDER)
total = sum(wish_count(WISH[s_]) for s_ in WORDER)
body = f'''<div class="narrow"><h1>Birthday Wishes &amp; Messages for Everyone</h1>
<p>Find the right words fast. We've written {total}+ original birthday wishes, sorted by who you're writing to: friends, family, partners, colleagues and more. There are funny, short and heartfelt versions, plus wishes in Urdu and Islamic duas. Every message is meant to be edited, so add a name and a memory and make it yours.</p>
<p>Not sure where to start? Read <a href="/guides/how-to-write-a-heartfelt-birthday-message">how to write a heartfelt birthday message</a> first.</p></div>
<div class="wrap"><div class="grid">{hub_cards}</div></div>
<div class="narrow"><div class="callout"><p>Want to go beyond a text? <a href="/create">Create a free animated birthday wish</a> with photos, music and your message, then share it with one link.</p></div></div>'''
write("/wishes", page("/wishes", "Birthday Wishes & Messages for Friends, Family & More | WishCraft",
    "Hundreds of original birthday wishes for friends, brothers, sisters, parents, partners, colleagues, in Urdu and more: heartfelt, funny and short.",
    body, trail=[("/", "Home"), ("/wishes", "Birthday wishes")], current="/wishes",
    schema=[{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Birthday Wishes", "url": SITE + "/wishes",
             "hasPart": [{"@type": "Article", "headline": WISH[s_]["title"], "url": SITE + "/wishes/" + s_} for s_ in WORDER]}]), prio="0.9")

# ---------------- Landing page
HOME_FAQ = FAQ[:5]
feat = [
 ("🎁", "Gift box &amp; cake ceremony", "A cinematic opening: tap to open a gift, make a wish, then cut the cake or blow out the candles."),
 ("📸", "Photo memory story", "Add up to ten photos and choose fade, zoom, slide or cinematic transitions for a slideshow with feeling."),
 ("🎵", "Your song, your moment", "Upload a track and pick the exact part that plays, or use a built-in music-box Happy Birthday."),
 ("💌", "A message in your words", "Heartfelt, funny, short, formal, blessing or Urdu starters, then edit them until they sound like you."),
 ("🔒", "Time-locked surprises", "Send the link early. If it's opened before the date, they see a live countdown instead."),
 ("🖼️", "Posters, video &amp; GIF", "Design a birthday poster and export it as a 1080 × 1350 image, a short looping video or a GIF."),
 ("🎟️", "Scratch cards &amp; reasons", "Hide a gift idea under a scratch-off or show six cards of reasons they're special."),
 ("🎨", "22 themes, 9 effects", "Match the look to the person with confetti, balloons, petals, fireworks, shooting stars and more."),
]
fcards = "".join('<div class="card"><h3>%s %s</h3><p>%s</p></div>' % (i, t, d) for i, t, d in feat)
uses = [("For friends and family", "Surprise a best friend, sibling or cousin with a photo story and an inside joke.", "/guides/birthday-wishes-messages"),
        ("For parents", "Say thank you with childhood photos and a message that mentions specific things they did for you.", "/guides/how-to-write-a-heartfelt-birthday-message"),
        ("For partners", "Combine your favorite photos, a song that matters to you both and a scratch-card date idea.", "/guides/how-to-create-a-birthday-surprise-link"),
        ("When you're far away", "Time-lock a surprise to arrive on their birthday morning, wherever they are.", "/guides/long-distance-birthday-surprise-ideas")]
ucards = "".join('<a class="card" href="%s"><h3>%s</h3><p>%s</p></a>' % (l, t, d) for t, d, l in uses)
gcards = "".join('<a class="card" href="/guides/%s"><p class="kicker">%s</p><h3>%s</h3><p>%s</p></a>' % (s, esc(GUIDES[s]["cat"]), esc(GUIDES[s]["title"]), esc(GUIDES[s]["desc"])) for s in ORDER[:3])
wcards = "".join('<a class="card" href="/wishes/%s"><h3>%s</h3><p>%s</p></a>' % (s_, esc(WISH[s_]["label"]) + " wishes", esc(WISH[s_]["desc"])) for s_ in ["birthday-wishes-for-friend","birthday-wishes-for-mother","birthday-wishes-for-brother","birthday-wishes-for-sister","birthday-wishes-in-urdu","funny-birthday-wishes"])
hfaq = "".join("<details><summary>%s</summary><p>%s</p></details>" % (esc(q), esc(a)) for q, a in HOME_FAQ)
body = f'''<script>
/* Old shared links (#wish=, #wishurl=) and ?w= links opened on the home page go straight to the viewer. */
(function(){{var l=location;if(/^#wish(url)?=/.test(l.hash)||/[?&]w=/.test(l.search)){{l.replace('/create'+l.search+l.hash);}}}})();
</script>
<section class="hero"><div class="wrap">
<p class="kicker">Free · No sign-up · Works on any phone</p>
<h1>Turn a Birthday Wish Into a Memory They Keep</h1>
<p class="lead">Create an animated birthday surprise with photos, music, a cake ceremony and a heartfelt message, then send it as one private link. Or design a birthday poster in minutes.</p>
<div class="cta-row"><a class="btn" href="/create">Create a birthday wish</a><a class="btn ghost" href="/guides/how-to-create-a-birthday-surprise-link">See how it works</a></div>
</div></section>

<div class="wrap"><section>
<h2>What you can make with WishCraft</h2>
<div class="grid">{fcards}</div></section></div>

<div class="band"><div class="narrow">
<h2 style="margin-top:0">How it works</h2>
<ol class="steps">
<li><strong>Add the details.</strong> Enter the name, upload a main photo and up to ten memory photos.</li>
<li><strong>Write and choose.</strong> Add your message, pick a song, a theme and the animations you like.</li>
<li><strong>Preview it.</strong> Watch the whole experience on your own screen before anyone else sees it.</li>
<li><strong>Share one link.</strong> Send it on WhatsApp or anywhere else. Nothing to install for the recipient.</li>
</ol>
<p><a class="btn" href="/create">Start now, it's free</a></p>
</div></div>

<div class="wrap"><section>
<h2>Made for every kind of birthday</h2>
<div class="grid">{ucards}</div></section></div>

<div class="narrow"><section>
<h2>Why personal wishes matter</h2>
<p>A text that says "Happy birthday" takes two seconds to send and two seconds to forget. A wish with a photo from a trip you took together, a song they love and a message that mentions something only you two know takes a few minutes to make, and people tend to remember it, replay it and show it to others.</p>
<p>WishCraft is built to make that effort small. You don't need design skills or editing software, and the person receiving it doesn't need an account or an app. The animations, cake ceremony and photo story give your words a moment to land, rather than burying them in a chat thread.</p>
<p>If you're not sure what to write, our guides help: start with <a href="/guides/how-to-write-a-heartfelt-birthday-message">how to write a heartfelt birthday message</a> or browse more than a hundred <a href="/guides/birthday-wishes-messages">birthday wishes</a> for friends, family, partners and colleagues.</p>
</section></div>

<div class="wrap"><section>
<h2>Birthday wishes by person</h2>
<p>Need the right words? Browse original messages for every relationship.</p>
<div class="grid">{wcards}</div>
<p><a href="/wishes">Browse all birthday wishes →</a></p></section></div>

<div class="wrap"><section>
<h2>Latest guides</h2>
<div class="grid">{gcards}</div>
<p><a href="/guides">Browse all guides →</a></p></section></div>

<div class="narrow"><section>
<h2>Common questions</h2>
{hfaq}
<p><a href="/faq">Read the full FAQ →</a></p></section></div>'''
home_schema = [
 {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE + "/"},
 {"@context": "https://schema.org", "@type": "WebApplication", "name": NAME, "url": SITE + "/create", "applicationCategory": "MultimediaApplication",
  "operatingSystem": "Any (web browser)", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
  "description": "Free web app for creating animated birthday wishes with photos, music and a shareable link, and for designing birthday posters, videos and GIFs."},
 faq_schema(HOME_FAQ)]
write("/", page("/", "WishCraft: Free Animated Birthday Wishes & Poster Maker",
    "Create a free animated birthday wish with photos, music and a cake ceremony and share it with one link. Or design a birthday poster, video or GIF. No sign-up.",
    body, schema=home_schema, current="/"), prio="1.0")

# ---------------- 404
open(os.path.join(ROOT, "404.html"), "w", encoding="utf8").write(page("/404", "Page not found | WishCraft", "That page doesn't exist.",
    '<div class="narrow" style="text-align:center;padding:70px 0"><h1>Page not found</h1><p>We couldn\'t find that page. Try the <a href="/">home page</a>, our <a href="/guides">guides</a> or the <a href="/create">wish creator</a>.</p></div>', ads=False).replace('content="index,follow,max-image-preview:large"', 'content="noindex"').replace('<link rel="canonical" href="%s/404">\n' % SITE, ''))

# ---------------- /create entry (the app) goes in sitemap; sitemap + robots + vercel
urls.insert(1, ("/create", "0.9"))
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p, pr in urls:
    sm.append("  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>" % (SITE, p, TODAY, pr))
sm.append("</urlset>\n")
open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm))
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {SITE}/sitemap.xml\n")
print("built", len(urls), "pages; contact email =", CONTACT_EMAIL)
