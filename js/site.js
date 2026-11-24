// Mobile menu toggle + footer year
(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('site-nav');
  if (btn && nav) btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open);
  });
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();

// Quote carousel: rotates every 7s, pauses on hover, dots to jump
(function () {
  var slides = document.querySelectorAll('.q-slide');
  var dots = document.querySelectorAll('.q-dot');
  if (!slides.length) return;
  var i = 0, timer;
  function show(n) {
    slides[i].classList.remove('is-active'); slides[i].setAttribute('aria-hidden', 'true'); dots[i].classList.remove('is-active');
    i = (n + slides.length) % slides.length;
    slides[i].classList.add('is-active'); slides[i].setAttribute('aria-hidden', 'false'); dots[i].classList.add('is-active');
  }
  function start() { stop(); timer = setInterval(function () { show(i + 1); }, 7000); }
  function stop() { clearInterval(timer); }
  dots.forEach(function (d, n) { d.addEventListener('click', function () { show(n); start(); }); });
  var stage = document.querySelector('.q-stage');
  stage.addEventListener('mouseenter', stop); stage.addEventListener('mouseleave', start);
  start();
})();

// Next Literary Circle date: second Saturday of the month (10 AM–12 PM)
(function () {
  var el = document.querySelector('[data-next-meet]');
  if (!el) return;
  function secondSat(y, m) { var d = new Date(y, m, 1); var first = (6 - d.getDay() + 7) % 7 + 1; return new Date(y, m, first + 7, 12, 0); }
  var now = new Date(), d = secondSat(now.getFullYear(), now.getMonth());
  if (now > d) d = secondSat(now.getFullYear(), now.getMonth() + 1);
  el.textContent = d.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' }) + ', 10 AM';
})();

