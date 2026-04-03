(function () {
  function bind(btn) {
    var row = btn.closest(".password-input-row");
    if (!row) return;
    var input = row.querySelector("input");
    if (!input) return;

    btn.addEventListener("click", function () {
      var show = input.type === "password";
      input.type = show ? "text" : "password";
      btn.setAttribute("aria-pressed", show ? "true" : "false");
      btn.setAttribute(
        "aria-label",
        show ? "Ocultar contraseña" : "Mostrar contraseña"
      );
    });
  }

  function init() {
    document.querySelectorAll("[data-password-toggle]").forEach(bind);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
