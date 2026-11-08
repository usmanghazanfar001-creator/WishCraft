# Guides part A
def lst(items):
    return '<ul class="wish-list">' + "".join("<li>%s</li>" % i for i in items) + "</ul>"

G = {}

# ---------------------------------------------------------------- 1
G["birthday-wishes-messages"] = dict(
 title="100+ Birthday Wishes & Messages for Every Person in Your Life",
 meta_title="100+ Birthday Wishes & Messages for Friends & Family",
 desc="100+ original birthday wishes for friends, family, partners and colleagues, plus funny, short and Roman Urdu messages to copy and personalize.",
 cat="Message ideas", read="9 min read",
 body=lambda: f'''
<p>A birthday message is the one thing almost everyone sends and very few people remember. The ones that stick are not the longest or the fanciest. They are the ones that sound like the sender and mention something only the two of you know.</p>
<p>Below you will find more than a hundred original birthday wishes, grouped by who you are writing to. Treat them as starting points. Swap in a name, a shared memory or an inside joke and a generic line becomes a message that person will actually keep. If you want a method for writing your own from scratch, read our guide to <a href="/guides/how-to-write-a-heartfelt-birthday-message">writing a heartfelt birthday message</a>.</p>
<div class="callout"><p><strong>Looking for someone specific?</strong> We have dedicated collections: <a href="/wishes/birthday-wishes-for-friend">friend</a>, <a href="/wishes/birthday-wishes-for-brother">brother</a>, <a href="/wishes/birthday-wishes-for-sister">sister</a>, <a href="/wishes/birthday-wishes-for-mother">mother</a>, <a href="/wishes/birthday-wishes-for-father">father</a>, <a href="/wishes/birthday-wishes-for-husband">husband</a>, <a href="/wishes/birthday-wishes-for-wife">wife</a>, <a href="/wishes/birthday-wishes-for-boss-and-colleague">boss &amp; colleague</a>, <a href="/wishes/birthday-wishes-in-urdu">Urdu</a> and <a href="/wishes">all wish collections</a>.</p></div>
<div class="toc"><strong>Jump to</strong><ul>
<li><a href="#friends">Friends and best friends</a></li><li><a href="#brother">Brothers</a></li><li><a href="#sister">Sisters</a></li><li><a href="#mother">Mothers</a></li><li><a href="#father">Fathers</a></li><li><a href="#partner">Husbands, wives and partners</a></li><li><a href="#colleague">Colleagues and bosses</a></li><li><a href="#funny">Funny wishes</a></li><li><a href="#short">Short wishes for cards and captions</a></li><li><a href="#urdu">Roman Urdu wishes</a></li><li><a href="#milestone">Milestone birthdays</a></li><li><a href="#grandparents">Grandparents</a></li><li><a href="#kids">Kids and teens</a></li><li><a href="#belated">Belated birthday wishes</a></li></ul></div>

<h2 id="friends">Birthday wishes for friends and best friends</h2>
<p>Friendship messages work best when they name what the person has actually done for you: the late-night calls, the honest advice, the way they show up.</p>
{lst([
"Happy birthday! Thank you for being the friend who answers on the first ring. May this year be as generous to you as you have always been to me.",
"Another year older and somehow still the person I want to tell everything to first. Happy birthday, my friend.",
"You make ordinary days feel like events. I hope your birthday is full of the same joy you hand out so easily.",
"Wishing you a year of good news, long laughs and no awkward group-chat silences. Happy birthday!",
"Some people are lucky to have one great friend. I got you. Happy birthday, and thank you for every memory so far.",
"I hope today brings everything you have been quietly hoping for. You deserve all of it.",
"Cheers to the person who knows my worst stories and still sits next to me. Happy birthday!",
"May your year be full of small wins, big adventures and your favorite people. I plan to be one of them.",
"Happy birthday to someone who makes every room warmer just by walking in.",
"Distance, schedules and busy weeks never changed us. I'm proud to be your friend. Have the best day.",
"You have been my safe place and my loudest cheerleader. Today, let everyone cheer for you.",
"Here's to another trip around the sun with you in my corner. Happy birthday, best friend!",
])}
<h2 id="brother">Birthday wishes for a brother</h2>
{lst([
"Happy birthday, bro. We have argued over everything, but I would still pick you as my brother every single time.",
"Thanks for being my first friend, my toughest critic and my biggest supporter. Wishing you a brilliant year.",
"To the one who always has my back, even when I don't deserve it: happy birthday!",
"May your year be as steady and strong as you are. I'm proud to be your sibling.",
"You taught me how to take a joke, how to stand up for myself and how to share the last slice. Happy birthday, brother!",
"I hope this year gives you everything you have worked so hard for. Enjoy your day, you've earned it.",
"Happy birthday to a brother who is also a best friend. Dinner is on me, as usual (only today).",
])}
<h2 id="sister">Birthday wishes for a sister</h2>
{lst([
"Happy birthday to my sister, my confidante and the keeper of all my secrets.",
"Growing up with you was the best part of my childhood. Growing older with you is the best part of now. Love you!",
"You are the person who understands my silence as well as my words. Wishing you a beautiful year ahead.",
"May your birthday feel as warm and comforting as your hugs. I'm so lucky to be your sister.",
"Thank you for every borrowed outfit, every pep talk and every laugh that left us out of breath. Happy birthday!",
"Whatever you dream of this year, I'll be cheering from the front row. Happy birthday, sis.",
"Some sisters share clothes. Ours share a whole lifetime. Happy birthday to my forever friend.",
])}
<h2 id="mother">Birthday wishes for a mother</h2>
<p>For parents, gratitude is the strongest message. Be specific about what they taught you.</p>
{lst([
"Happy birthday, Mom. Everything good in me started with you. I hope today is gentle, calm and full of the love you give away every day.",
"Thank you for the sacrifices you never mentioned and the comfort you never stopped giving. I love you more than I can say.",
"You taught me to be kind, to be brave and to keep trying. I'm trying to be a little more like you each year. Happy birthday!",
"Your prayers have carried me further than you know. May every one of them come back to you as blessings.",
"Today is your day to rest and be looked after. You have looked after all of us for so long.",
"A home is not a house. It's you. Happy birthday to the heart of our family.",
"May your health stay strong, your heart stay light and your family stay close. Happy birthday, Ammi.",
"No gift can match what you have given me, but I hope this day makes you feel as loved as you deserve to be.",
])}
<h2 id="father">Birthday wishes for a father</h2>
{lst([
"Happy birthday, Dad. You never said much about being proud of me, but you showed it in a thousand ways. Thank you.",
"You taught me that strength is quiet and that work done with honesty is never wasted. Wishing you a wonderful year.",
"Thank you for being my safety net and my example. May your day be as steady and generous as you are.",
"Dad, you are the reason I believe in myself. Happy birthday to my hero.",
"May this year bring you rest, good health and time with the people who love you. Happy birthday, Abu.",
"Every lesson I wish I'd listened to sooner came from you. Happy birthday, and thank you for your patience.",
"To the first man I ever looked up to: I still do. Have a beautiful birthday.",
])}
<h2 id="partner">Birthday wishes for a husband, wife or partner</h2>
<p>Keep romantic messages honest rather than dramatic. Naming one small habit you love will land harder than any big declaration.</p>
{lst([
"Happy birthday to the person who makes ordinary mornings feel like a gift. I love building this life with you.",
"Another year of you is the best present I could ask for. Happy birthday, my love.",
"You are my calm in a busy world and my favorite person to laugh with. May this year be gentle with you.",
"Thank you for choosing me every day, even on the difficult ones. I hope your birthday feels as special as you make me feel.",
"I fall for you a little more with every year. Happy birthday to my best friend and my home.",
"To my husband: you work so hard for all of us. Today, let us work hard for you. Happy birthday.",
"To my wife: you turn a house into a home and a day into a memory. I hope you feel loved today and always.",
"Whatever the year brings, I want to face it with you. Happy birthday, my partner in everything.",
])}
<h2 id="colleague">Birthday wishes for colleagues and bosses</h2>
<p>At work, warm and brief is better than overly personal. Mention something genuine about working with them.</p>
{lst([
"Happy birthday! Thank you for being a colleague who makes the team better. Enjoy your day.",
"Wishing you a year of success, good health and projects that go exactly to plan. Happy birthday!",
"Happy birthday! It's a pleasure working with someone so dependable and kind.",
"Thank you for your guidance and example. Wishing you a wonderful birthday and a rewarding year.",
"Happy birthday to the person who keeps the team calm in every deadline storm.",
"May the year ahead bring new opportunities and plenty of reasons to celebrate. Happy birthday!",
"Best wishes on your birthday. We are lucky to have you on the team.",
])}
<h2 id="funny">Funny birthday wishes</h2>
<p>Humor is great when you know the person well. Make the joke about yourself or the shared experience, never about something that could hurt.</p>
{lst([
"Happy birthday! You're not old, you're a limited edition.",
"I'd say you're aging like fine wine, but let's be honest, you're aging like a very good cheese. Happy birthday!",
"Another year older, but your sense of humor is still stuck at the same age as mine. Perfect.",
"Happy birthday! Please accept this message in place of the expensive gift you were expecting.",
"They say age is just a number. Yours is just a slightly bigger number this year. Congratulations!",
"Eat the cake. Calories don't count on birthdays. That's science. Happy birthday!",
"May your coffee be strong, your Wi-Fi be fast and your age be a secret you happily share. Happy birthday!",
"You are one year closer to your senior-citizen discount. Happy birthday!",
])}
<h2 id="short">Short birthday wishes for cards, captions and status</h2>
{lst([
"Happy birthday! Here's to you.",
"Wishing you joy today and all year long.",
"Many happy returns of the day!",
"Cheers to another great year.",
"Have a day as wonderful as you are.",
"Big hugs and bigger cake. Happy birthday!",
"May all your wishes come true.",
"Celebrate big today. You've earned it.",
])}
<h2 id="urdu">Roman Urdu birthday wishes</h2>
<p>Many families prefer to send wishes in Urdu written in Latin script. These are warm, simple and easy to adapt. WishCraft's message tool also includes an Urdu quick-message style you can start from.</p>
{lst([
"Salgirah mubarak ho! Allah aap ko hamesha khush aur salamat rakhe.",
"Aap ki zindagi mein khushiyan, sehat aur kamyabi hamesha rahein. Janam din mubarak!",
"Aap meri zindagi ka bohat khoobsurat hissa hain. Allah aap ko lambi umar aur sukoon de. Salgirah mubarak!",
"Dua hai ke aap ka aanay wala saal pichlay saal se bhi behtar ho. Janam din mubarak ho!",
"Meray pyare dost, aap jaisa dost naseeb walon ko milta hai. Salgirah mubarak!",
"Ammi, aap ki duaon ki wajah se hi main yahan hoon. Allah aap ko sehat aur khushi de. Salgirah mubarak!",
"Abu jaan, aap meri himmat hain. Allah aap ka saya hamesha salamat rakhe. Janam din mubarak!",
])}
<h2 id="milestone">Milestone birthday wishes (18th, 30th, 40th, 50th and beyond)</h2>
{lst([
"Happy 18th! Today the world opens up. Choose bravely, stay curious and remember that we're always here.",
"Happy 21st! May the next chapter be braver, funnier and kinder than the last.",
"Happy 30th! You walked into this decade with experience, and you walk out with plenty of room to dream. Enjoy it.",
"Forty looks great on you. Here's to wisdom, good friends and many more years of both.",
"Happy 50th! Half a century of stories, and you're still the best storyteller I know.",
"Sixty years of kindness and strength. Thank you for everything you've built and everyone you've lifted along the way.",
"At 70, you are proof that the best years aren't behind us. Happy birthday, and thank you for showing us how.",
"Happy 1st birthday to the little one who turned our lives upside down in the best way possible!",
])}
<h2 id="grandparents">Birthday wishes for grandparents</h2>
{lst([
"Happy birthday, Grandma. Your kitchen, your stories and your hugs are the warmest memories I have.",
"Grandpa, thank you for every lesson you taught me without ever making it feel like a lesson. Happy birthday!",
"Wishing the wisest, kindest person I know a day full of family, laughter and your favorite sweet.",
"Dadi, Nani, Dada, Nana: you are the roots of our family, and we are grateful for every year with you. Happy birthday!",
])}
<h2 id="kids">Birthday wishes for kids and teens</h2>
{lst([
"Happy birthday to our little superstar! May your day be full of cake, games and giggles.",
"You make us proud every single day. Happy birthday, and keep being exactly who you are.",
"Another year older, another year more amazing. Happy birthday, champ!",
"Happy birthday! I hope this year brings new friends, big adventures and zero homework on your birthday.",
"To our favorite niece/nephew: you make our family brighter. Happy birthday!",
"May you always chase your dreams, even the silly ones. Happy birthday, kiddo!",
])}
<h2 id="belated">Belated birthday wishes</h2>
<p>Forgot? It happens. A short, honest apology plus a real wish is far better than silence or a long excuse.</p>
{lst([
"I'm late, but my wishes are not. Happy belated birthday! I hope it was wonderful.",
"I missed the day but not the thought. Happy belated birthday, and let's celebrate properly soon.",
"Sorry for the delay. A good birthday deserves a good message, and I wanted to get this one right. Happy belated birthday!",
"Better late than never: happy birthday! Cake is on me whenever you are free.",
])}
<h2>How to make any wish more personal in 30 seconds</h2>
<ol>
<li><strong>Add a name.</strong> "Happy birthday, Sara" beats "Happy birthday."</li>
<li><strong>Add one specific memory.</strong> A trip, a joke or a favor you still remember.</li>
<li><strong>Add one wish for their year.</strong> Link it to something real in their life, such as a new job, an exam or a move.</li>
<li><strong>Cut anything you wouldn't say out loud.</strong> If a line sounds like a greeting card, rewrite it in your own words.</li>
</ol>
<div class="callout"><p><strong>Turn your message into a surprise.</strong> Paste any of these into the message box in the <a href="/create">WishCraft wish creator</a>, add a photo and a song, and send the recipient a private animated link instead of a plain text message.</p></div>
''')

# ---------------------------------------------------------------- 2
G["how-to-create-a-birthday-surprise-link"] = dict(
 title="How to Create a Birthday Surprise Link With Photos and Music",
 meta_title="How to Create a Birthday Surprise Link (Step-by-Step)",
 desc="Step-by-step tutorial: build an animated birthday wish with photos, music, a cake ceremony and a private link you can send on WhatsApp. Free, no sign-up.",
 cat="Tutorials", read="8 min read",
 body=lambda: '''
<p>A birthday surprise link is a single web address that opens a short animated experience for the person you are celebrating: a gift box, a cake ceremony, a story built from your photos, a message in your words and, if you like, music. It works on any phone with a browser, so there is nothing for the recipient to install.</p>
<p>This tutorial walks through each step of the <a href="/create">WishCraft wish creator</a> and explains what each option does, so the final result feels intentional rather than assembled.</p>
<div class="toc"><strong>What you will need</strong><ul><li>The birthday person's name (the only required field)</li><li>One clear photo of them, ideally a portrait</li><li>Optional: up to 10 more photos, a song, and a message in your own words</li><li>About ten minutes</li></ul></div>

<h2>Step 1: Enter the birthday details</h2>
<p>Type the name exactly as you want it to appear on the reveal screen. You can add their age and your relationship to them; the age is used for the optional age-counter scene. Two toggles are worth knowing about:</p>
<ul>
<li><strong>Surprise Mode</strong> hides the name until the recipient opens the wish, which keeps the preview screen mysterious.</li>
<li><strong>Gift box opening</strong> adds an animated gift they tap to open before the main experience begins.</li>
</ul>

<h2>Step 2: Add the main photo</h2>
<p>This is the photo shown on the hero screen. Choose a sharp, well-lit picture where the face is clearly visible. WishCraft compresses the photo automatically so it loads quickly on mobile data. You can pick a circle, rounded, square or soft-frame shape, and one of eleven frame styles. If you are unsure, start with the circle and a simple gold frame; it suits almost every photo. For more guidance see our <a href="/guides/birthday-photo-tips-for-memory-stories">photo selection tips</a>.</p>

<h2>Step 3: Build the memory story</h2>
<p>Add up to ten photos to create a short slideshow that plays before the reveal. Pick a transition (fade, Ken Burns zoom, slide or cinematic) and a duration per photo from three to ten seconds. Five seconds is a good default; shorter feels rushed and longer loses attention. A preview in the editor lets you flip through the photos before you commit.</p>

<h2>Step 4: Write the message</h2>
<p>The message box holds up to 260 characters, which is intentionally short so it stays readable on a phone screen. You can start from a quick style (heartfelt, funny, short, formal, blessing or Urdu) and edit it. Add a heading such as "To the best sister in the world" and sign with your name in the From field. Our guide to <a href="/guides/how-to-write-a-heartfelt-birthday-message">writing a heartfelt message</a> shows how to fit a lot of feeling into a few lines.</p>

<h2>Step 5: Add music</h2>
<p>Upload a song (up to 25 MB) and drag the start and end sliders to choose the exact part that plays, for example the chorus. If you don't upload a song, you can switch on the music-box "Happy Birthday" melody. Only use music you have the right to share; see our <a href="/terms">terms of use</a> for details.</p>

<h2>Step 6: Pick a theme and animations</h2>
<p>There are 22 themes. Choose one that matches the person: a warm gold for a parent, a bold color for a teenager, a soft pastel for a sibling. Then select animations such as confetti, balloons, sparkles, fireworks, hearts, golden particles, petals, bubbles or shooting stars, and set the intensity. Medium is best for most devices; choose low if the recipient may use an older phone.</p>

<h2>Step 7: Try the bonus scenes</h2>
<p>All bonus scenes are optional and off by default:</p>
<ul>
<li><strong>Blow the candles</strong> replaces the cake-cutting scene with a candle ceremony.</li>
<li><strong>Countdown</strong> adds a 3-2-1 before the reveal.</li>
<li><strong>Age counter</strong> counts up to the person's age.</li>
<li><strong>Reasons you're special</strong> shows up to six short lines as cards.</li>
<li><strong>Scratch card</strong> hides a message or gift idea under a surface they scratch away.</li>
<li><strong>Lock until a date and time</strong> shows a live countdown if they open the link early, so you can send it ahead of the day.</li>
</ul>

<h2>Step 8: Preview, then generate the link</h2>
<p>Always press <em>Preview Birthday Experience</em> and watch it from start to finish, ideally on your phone. Check that the name is spelled correctly, the music starts where you want and the photos are in the right order. When you are happy, press <em>Create Wish &amp; Generate Link</em>. Your photos, song and text are saved and you receive a short link that looks like <code>wishcrafting.vercel.app/?w=Ab3xK9pQzM</code>.</p>

<h2>Step 9: Share it</h2>
<p>Use the WhatsApp button, the native Share sheet or copy the link. When the recipient finishes, they can watch again, send you a thank-you message or create a wish of their own. Read <a href="/guides/share-birthday-wishes-on-whatsapp">how to share birthday wishes on WhatsApp</a> for timing and etiquette tips.</p>

<h2>Troubleshooting</h2>
<table>
<tr><th>Problem</th><th>What to try</th></tr>
<tr><td>Photo won't upload</td><td>Use a JPG, PNG or WebP file. Very large photos are resized automatically, but a poor connection can still interrupt the upload; try again on Wi-Fi.</td></tr>
<tr><td>Song is too large</td><td>The limit is 25 MB. Trim the file or export it at a lower bitrate first.</td></tr>
<tr><td>No sound for the recipient</td><td>Phones often block autoplay until the screen is tapped. The wish starts with an "Open" button for that reason, so the music begins after their first tap.</td></tr>
<tr><td>Link says wish not found</td><td>Check that the whole link was copied, including the part after <code>?w=</code>.</td></tr>
<tr><td>Lost your half-finished wish</td><td>Drafts auto-save on the device you were using. Reopen the creator on the same browser and use the draft bar at the top.</td></tr>
</table>
<div class="callout"><p>Ready to try it? <a href="/create">Open the WishCraft creator</a>. It is free and needs no account.</p></div>
''')

# ---------------------------------------------------------------- 3
G["how-to-write-a-heartfelt-birthday-message"] = dict(
 title="How to Write a Heartfelt Birthday Message (With Fill-in Templates)",
 meta_title="How to Write a Heartfelt Birthday Message + Templates",
 desc="A simple four-part formula for writing a sincere birthday message in under five minutes, with examples, templates and common mistakes to avoid.",
 cat="Writing", read="7 min read",
 body=lambda: '''
<p>Most of us know what we feel when someone we love has a birthday. The hard part is turning that feeling into a few sentences that don't sound like a greeting card. The good news is that a sincere message follows a simple shape, and anyone can learn it.</p>

<h2>Why generic messages fall flat</h2>
<p>"Happy birthday! Wishing you all the best" is polite, but it could be sent to anyone, so it tells the reader nothing about how you see them. People remember messages that prove you were paying attention. The goal is not poetry. It is specificity.</p>

<h2>The four-part formula</h2>
<ol class="steps">
<li><strong>Greet them by name.</strong> Open warmly and directly: "Happy birthday, Hassan."</li>
<li><strong>Say what they mean to you.</strong> Use a concrete detail rather than an adjective. "You're always the first to check in when I'm stressed" says more than "you're so caring."</li>
<li><strong>Add a shared memory (optional but powerful).</strong> One sentence is enough: "I still laugh about the day we missed the last bus home."</li>
<li><strong>Close with a wish for their year.</strong> Make it specific to their life: "I hope this is the year the new business takes off."</li>
</ol>

<h2>The same message, before and after</h2>
<table>
<tr><th>Generic</th><th>Personal</th></tr>
<tr><td>Happy birthday! Hope you have a great day.</td><td>Happy birthday, Hira! Thank you for driving two hours to help me move last spring. I hope your day is as generous to you as you are to everyone else.</td></tr>
<tr><td>Wishing you the best on your special day.</td><td>Happy birthday, Dad. You taught me to fix a bike and, without noticing, how to fix most other things. I hope this year gives you rest.</td></tr>
<tr><td>Happy birthday, colleague!</td><td>Happy birthday, Ali! Our Monday meetings are better because you ask the questions nobody else dares to. Enjoy your day.</td></tr>
</table>

<h2>Fill-in-the-blank templates</h2>
<p>Use these as scaffolding and replace every bracket with something true:</p>
<blockquote>Happy birthday, [name]! The thing I appreciate most about you is [specific quality or action]. I'll never forget [shared memory]. This year, I hope [wish tied to their life].</blockquote>
<blockquote>[Name], another year older and you still [habit you love]. Thank you for [what they did for you]. Wishing you [wish] today and all year.</blockquote>
<blockquote>Dear [name], I don't say it enough, so today I will: [honest thank-you]. Happy birthday, and here's to [future plan or hope].</blockquote>

<h2>Adjust the tone to the relationship</h2>
<h3>Close friends</h3>
<p>Be informal. Inside jokes are welcome. A little teasing shows affection, as long as it's something they'd laugh at in person.</p>
<h3>Parents and grandparents</h3>
<p>Lead with gratitude and health wishes. Specific thanks ("for the sandwiches you packed every morning") are more moving than big statements ("for everything you've done").</p>
<h3>Partners</h3>
<p>Name something small and daily. Grand declarations can feel performed; tiny details feel true.</p>
<h3>Colleagues and managers</h3>
<p>Keep it warm but short. One sincere line about working together is enough.</p>
<h3>Someone you've drifted from</h3>
<p>Don't apologize for the silence in a birthday note. Keep it light: "Thinking of you today. I hope the year's been kind. Happy birthday." Often that is enough to restart the conversation.</p>

<h2>Common mistakes to avoid</h2>
<ul>
<li><strong>Making it about you.</strong> One line about how they've helped you is good; a whole paragraph about your own year isn't.</li>
<li><strong>Jokes about age, weight or appearance.</strong> What reads as funny to you can land badly. When in doubt, tease yourself instead.</li>
<li><strong>Copying a viral message word for word.</strong> Recipients often recognize them, and they lose meaning.</li>
<li><strong>Going too long.</strong> For a text or animated card, two to four sentences is the sweet spot. Save letters for letters.</li>
<li><strong>Waiting for the perfect words.</strong> A sincere imperfect message sent on time beats a polished one sent late.</li>
</ul>

<h2>Writing for a short card</h2>
<p>If your message will appear on a screen, like the 260-character message box in WishCraft or on a poster, trim aggressively. Keep one image, one thank-you and one wish. Read it aloud once; if you stumble, shorten the sentence. For ready-to-use lines, browse our <a href="/guides/birthday-wishes-messages">collection of birthday wishes</a>.</p>

<h2>A five-minute routine</h2>
<ol>
<li>Spend one minute listing three things you value about them.</li>
<li>Pick the one with a real memory attached.</li>
<li>Write it in plain words as if texting them.</li>
<li>Add a wish for their coming year.</li>
<li>Read it aloud and delete the first sentence that sounds fake.</li>
</ol>
<div class="callout"><p>Once your message is ready, put it somewhere special. In the <a href="/create">WishCraft creator</a> it appears on the reveal screen after a cake ceremony and a photo story, so the words get the moment they deserve.</p></div>
''')
