/* WishCraft analytics — OFF until you paste an ID below.
 *
 * Privacy rules built in:
 *  - Never loads on shared-wish pages (/?w=…, #wish=…), which contain private names, photos and messages.
 *  - Never sends names, messages, photos, links or any text typed by users. Events carry only a fixed
 *    event name plus (for templates) the public template name, e.g. "Elegant Gold".
 *  - Respects Do Not Track / Global Privacy Control.
 *  - Loads only after the first user interaction, so it never slows the first paint.
 *
 * Event naming convention: <object>_<action>, lowercase snake_case
 *   wish_create        – "Create Wish & Generate Link" pressed
 *   wish_preview       – "Preview Birthday Experience" pressed
 *   poster_download    – "Download Poster" pressed
 *   video_export       – "Download Video" pressed
 *   gif_export         – "Download GIF" pressed
 *   share_whatsapp     – any WhatsApp share button pressed (param: source = creator | poster | recipient)
 *   template_select    – poster template or wish theme picked (param: template_name, kind = poster | wish)
 *   cta_click          – a landing-page button into the tool (param: cta = text of the CTA, fixed strings only)
 * These fire when the button is pressed, not when the action is confirmed successful.
 */
(function () {
  var CONFIG = {
    GA4_ID: '',          // e.g. 'G-XXXXXXXXXX'
    CLARITY_ID: '',      // optional. Turn on strict text masking in Clarity settings first: the creator contains typed messages.
    BING_UET_ID: ''      // optional Bing Ads UET tag; Bing Webmaster verification is a meta tag, not this.
  };
  var loc = location;
  if (/[?&]w=/.test(loc.search) || /^#wish(url)?=/.test(loc.hash)) return;
  if (navigator.doNotTrack === '1' || navigator.globalPrivacyControl) return;
  if (!CONFIG.GA4_ID && !CONFIG.CLARITY_ID) { window.wcTrack = function () { }; return; }

  var queue = []; var ready = false;
  window.wcTrack = function (name, params) { if (ready && window.gtag) window.gtag('event', name, params || {}); else queue.push([name, params]); };

  function load() {
    if (ready || window.__wcAnalytics) return; window.__wcAnalytics = true;
    if (CONFIG.GA4_ID) {
      var s = document.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + CONFIG.GA4_ID; document.head.appendChild(s);
      window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); };
      gtag('js', new Date()); gtag('config', CONFIG.GA4_ID, { anonymize_ip: true, allow_google_signals: false, allow_ad_personalization_signals: false });
    }
    if (CONFIG.CLARITY_ID) {
      (function (c, l, a, r, i, t, y) { c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments) }; t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i; y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y); })(window, document, 'clarity', 'script', CONFIG.CLARITY_ID);
    }
    ready = true; queue.splice(0).forEach(function (q) { window.wcTrack(q[0], q[1]); });
  }
  ['scroll', 'pointerdown', 'keydown', 'touchstart'].forEach(function (e) { addEventListener(e, load, { once: true, passive: true }); });

  var BTN = { wGenerateBtn: 'wish_create', wPreviewBtn: 'wish_preview', downloadBtn: 'poster_download', videoBtn: 'video_export', gifBtn: 'gif_export' };
  var WA = { wShareWA: 'creator', waBtn: 'poster', finalWA: 'recipient' };
  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('button,a,.tpl-card'); if (!t) return;
    if (BTN[t.id]) return wcTrack(BTN[t.id]);
    if (WA[t.id]) return wcTrack('share_whatsapp', { source: WA[t.id] });
    if (t.classList.contains('tpl-card')) {
      var kind = t.closest('#tplGrid') ? 'poster' : (t.closest('#wThemeGrid') ? 'wish' : '');
      if (kind) return wcTrack('template_select', { kind: kind, template_name: (t.textContent || '').trim().slice(0, 40) });
    }
    if (t.tagName === 'A' && t.classList.contains('btn') && /^\/create/.test(t.getAttribute('href') || '')) wcTrack('cta_click', { cta: (t.textContent || '').trim().slice(0, 40) });
  }, true);
})();

/* cta_click: landing-page buttons that lead into the tool. Sends only the button's fixed label and the page path. */
(function () {
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a.btn[href^="/create"]');
    if (a && window.wcTrack) window.wcTrack('cta_click', { cta: (a.textContent || '').trim().slice(0, 40), page: location.pathname });
  }, true);
})();
