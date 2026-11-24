/* =========================================================
   Reading Archive – automatic updates from YouTube
   ---------------------------------------------------------
   Each time someone opens readings.html, this asks the org's
   "Living Tamil YouTube Feed" Apps Script (no API key needed)
   for the channel's 15 latest uploads, and adds any video not
   already on the page to a "Newly added" section at the top.
   ========================================================= */
(function () {
  var FEED_URL = 'https://script.google.com/macros/s/AKfycbzAvA_OBwL2nxq05pFQOo5Yjf7WYENBoIFghtZ7rMdS5csiFJhqlTlSL-QJBSkKFQbpiA/exec';
  if (!/^https:\/\/script\.google\.com\//.test(FEED_URL)) return;
  var anchor = document.querySelector('.r-talks') || document.querySelector('.r-session');
  if (!anchor) return;

  var known = {};
  document.querySelectorAll('img[src*="/vi/"]').forEach(function (img) {
    var m = img.src.match(/\/vi\/([^/]+)\//); if (m) known[m[1]] = true;
  });

  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); }
  function okId(id) { return /^[A-Za-z0-9_-]{6,20}$/.test(id); }

  function parse(t) {
    t = String(t).replace(/[’']/g, "’");
    var m;
    if ((m = t.match(/^(.+?)\s+introduces\s+(.+)$/i))) return { kind: 'intro', title: 'Introducing ' + m[2], author: m[2], speaker: m[1] };
    if ((m = t.match(/^Introducing\s+(.+?)(?:\s+by\s+(.+))?$/i))) return { kind: 'intro', title: t.replace(/\s+by\s+.+$/i, ''), author: m[1], speaker: m[2] || '' };
    if ((m = t.match(/^(.+?)\s+on\s+(.+?)’s?\s+(.+)$/i))) return { kind: 'story', title: m[3].replace(/^[‘“"]|[’”"]$/g, ''), author: m[2], speaker: m[1] };
    if ((m = t.match(/^(.+?)\s+[-–]\s+(.+)$/))) {
      if (/அறிமுகம்/.test(m[2])) return { kind: 'intro', title: t, author: m[1].replace(/^எழுத்தாளர்\s*/, ''), speaker: '' };
      return { kind: 'story', title: m[1], author: m[2], speaker: '' };
    }
    return { kind: 'talk', title: t, author: '', speaker: '' };
  }

  function card(v) {
    var p = parse(v.title), id = v.id, yt = 'https://www.youtube.com/watch?v=' + id;
    var tag = { intro: 'Introduction', story: 'Story', talk: 'Talk' }[p.kind];
    var find = p.kind === 'story'
      ? ' <a href="https://www.google.com/search?q=' + encodeURIComponent(p.title + ' ' + p.author + ' சிறுகதை') + '" target="_blank" rel="noopener noreferrer">Find the text ↗</a>' : '';
    return '<li class="r-item r-' + p.kind + '">' +
      '<a class="r-thumb" href="' + yt + '" target="_blank" rel="noopener noreferrer"><img src="https://i.ytimg.com/vi/' + id + '/mqdefault.jpg" alt="" loading="lazy"><span class="r-tag">' + tag + '</span></a>' +
      '<div class="r-body"><h4>' + esc(p.title) + '</h4>' +
      (p.author ? '<p class="r-author">' + esc(p.author) + '</p>' : '') +
      (p.speaker ? '<span class="r-spk">Presented by ' + esc(p.speaker) + '</span>' : '') +
      '<p class="r-links"><a href="' + yt + '" target="_blank" rel="noopener noreferrer">▶ Watch</a>' + find + '</p></div></li>';
  }

  fetch(FEED_URL, { credentials: 'omit', referrerPolicy: 'no-referrer' })
    .then(function (r) { return r.json(); })
    .then(function (d) {
      var fresh = (d.videos || []).filter(function (v) { return okId(v.id) && !known[v.id]; });
      if (!fresh.length) return;
      var html = '<section class="r-session r-new"><div class="wrap">' +
        '<div class="r-head"><span class="r-when">New</span><div><p class="card-ta" lang="ta">புதிய பதிவுகள்</p><h2>Newly added</h2></div></div>' +
        '<ul class="r-list">' + fresh.map(card).join('') + '</ul></div></section>';
      anchor.insertAdjacentHTML('beforebegin', html);
    })
    .catch(function () { /* feed unavailable: the archive simply shows as is */ });
})();

