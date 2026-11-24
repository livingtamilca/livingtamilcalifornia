/* Website forms -> Google Sheet in the Living Tamil Drive (Apps Script web app).
   Sends over HTTPS straight to the org's own Google account; no third-party form service.
   Without JavaScript the form still posts to the same address. */
(function () {
  document.querySelectorAll('form[data-sheet]').forEach(function (f) {
    var msg = f.querySelector('.form-msg');
    f.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (f.elements._honey && f.elements._honey.value) return;          // spam bot
      if (!f.checkValidity()) { f.reportValidity(); return; }
      var btn = f.querySelector('button[type=submit]'), label = btn.textContent;
      btn.disabled = true; btn.textContent = 'Sending…'; if (msg) msg.textContent = '';
      var body = new URLSearchParams(new FormData(f));
      fetch(f.action, { method: 'POST', mode: 'no-cors', body: body, credentials: 'omit', referrerPolicy: 'no-referrer' })
        .then(function () { f.reset(); location.href = 'thanks.html'; })
        .catch(function () {
          btn.disabled = false; btn.textContent = label;
          if (msg) msg.textContent = 'Sorry, that did not go through. Please try again, or email livingtamilcalifornia@gmail.com.';
        });
    });
  });
})();

