// one-click copy for the BibTeX box on publication pages
(function () {
  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    // fallback for older / non-secure-context browsers
    return new Promise(function (resolve, reject) {
      try {
        var ta = document.createElement("textarea");
        ta.value = text;
        ta.style.position = "fixed";
        ta.style.opacity = "0";
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
        resolve();
      } catch (err) {
        reject(err);
      }
    });
  }

  function init() {
    document.querySelectorAll(".bibtex_copy").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var wrap = btn.closest(".publication_bibtex_wrap");
        var code = wrap ? wrap.querySelector("code") : null;
        if (!code) return;
        copyText(code.innerText).then(function () {
          var original = btn.innerHTML;
          btn.innerHTML = '<i class="fas fa-check"></i> Copied';
          btn.classList.add("copied");
          setTimeout(function () {
            btn.innerHTML = original;
            btn.classList.remove("copied");
          }, 2000);
        });
      });
    });
  }

  // scripts.html is loaded in <head>, so wait for the DOM before wiring buttons
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
