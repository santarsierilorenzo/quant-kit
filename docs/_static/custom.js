(function () {
  const TITLES = new Set(["Parameters:", "Returns:", "Return type:", "Notes"]);

  document.addEventListener("DOMContentLoaded", function () {
    const spans = document.querySelectorAll("dl.field-list dt span.field-name");

    spans.forEach((sp) => {
      const txt = (sp.textContent || "").trim();
      if (TITLES.has(txt)) {
        sp.classList.add("qk-section-label");
      }
    });
  });
})();
