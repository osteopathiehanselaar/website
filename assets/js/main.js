(function () {
  "use strict";

  // Footer year
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Scroll-reveal animations
  var revealEls = document.querySelectorAll(".reveal, .reveal-scale");
  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  } else {
    var observer = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            obs.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -60px 0px" }
    );
    revealEls.forEach(function (el) { observer.observe(el); });
  }

  // Sticky header style on scroll
  var header = document.querySelector("[data-header]");
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 12) {
        header.classList.add("bg-cream/90", "backdrop-blur-md", "shadow-sm", "shadow-sage-900/[0.04]");
      } else {
        header.classList.remove("bg-cream/90", "backdrop-blur-md", "shadow-sm", "shadow-sage-900/[0.04]");
      }
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Mobile menu toggle
  var menuToggle = document.getElementById("menu-toggle");
  var mobileMenu = document.getElementById("mobile-menu");
  var iconOpen = document.getElementById("icon-open");
  var iconClose = document.getElementById("icon-close");

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener("click", function () {
      var isOpen = mobileMenu.classList.toggle("hidden") === false;
      menuToggle.setAttribute("aria-expanded", String(isOpen));
      iconOpen.classList.toggle("hidden", isOpen);
      iconClose.classList.toggle("hidden", !isOpen);
      document.body.classList.toggle("overflow-hidden", isOpen);
    });

    // Close mobile menu when a link is clicked
    mobileMenu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        mobileMenu.classList.add("hidden");
        menuToggle.setAttribute("aria-expanded", "false");
        iconOpen.classList.remove("hidden");
        iconClose.classList.add("hidden");
        document.body.classList.remove("overflow-hidden");
      });
    });
  }

  // Subtle parallax for hero decorative shapes (transform/opacity only)
  if (!prefersReducedMotion) {
    var parallaxEls = document.querySelectorAll("[data-parallax]");
    if (parallaxEls.length) {
      var ticking = false;
      var updateParallax = function () {
        var scrollY = window.scrollY;
        parallaxEls.forEach(function (el) {
          var speed = parseFloat(el.getAttribute("data-parallax")) || 0.15;
          var offset = scrollY * speed;
          el.style.transform = "translate3d(0, " + offset + "px, 0)";
        });
        ticking = false;
      };
      window.addEventListener(
        "scroll",
        function () {
          if (!ticking) {
            window.requestAnimationFrame(updateParallax);
            ticking = true;
          }
        },
        { passive: true }
      );
      updateParallax();
    }
  }

  // FAQ accordions
  document.querySelectorAll("[data-accordion-trigger]").forEach(function (trigger) {
    trigger.addEventListener("click", function () {
      var panel = document.getElementById(trigger.getAttribute("aria-controls"));
      var expanded = trigger.getAttribute("aria-expanded") === "true";
      trigger.setAttribute("aria-expanded", String(!expanded));
      if (panel) {
        if (expanded) {
          panel.style.maxHeight = "0px";
        } else {
          panel.style.maxHeight = panel.scrollHeight + "px";
        }
      }
      var icon = trigger.querySelector("[data-accordion-icon]");
      if (icon) icon.style.transform = expanded ? "rotate(0deg)" : "rotate(45deg)";
    });
  });

  // Basic client-side form handling (no backend configured)
  document.querySelectorAll("[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector("[data-form-status]");
      if (status) {
        status.classList.remove("hidden");
        status.focus({ preventScroll: true });
      }
      form.reset();
    });
  });
})();
