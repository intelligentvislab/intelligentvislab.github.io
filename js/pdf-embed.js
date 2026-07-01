// inline PDF viewer toggle on publication pages (lazy-loads the iframe on first open)
(function () {
  function init() {
    document.querySelectorAll(".pdf_toggle").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var wrap = btn.closest(".publication_pdf");
        var container = wrap ? wrap.querySelector(".pdf_embed") : null;
        if (!container) return;

        // first click: build the iframe
        if (!container.dataset.loaded) {
          var iframe = document.createElement("iframe");
          iframe.src = btn.dataset.src;
          iframe.title = "PDF preview";
          iframe.loading = "lazy";
          iframe.allow = "fullscreen";
          container.appendChild(iframe);
          container.dataset.loaded = "true";
        }

        var open = container.classList.toggle("open");
        btn.innerHTML = open
          ? '<i class="fas fa-times"></i> Hide PDF'
          : '<i class="fas fa-file-pdf"></i> View PDF';
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
