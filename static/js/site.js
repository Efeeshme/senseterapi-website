(() => {
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Mobile nav toggle
  const btn = document.querySelector(".menu-btn");
  const nav = document.getElementById("primary-nav");
  if (btn && nav) {
    const closeNav = () => {
      btn.setAttribute("aria-expanded", "false");
      nav.classList.remove("is-open");
    };

    btn.addEventListener("click", () => {
      const expanded = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!expanded));
      nav.classList.toggle("is-open", !expanded);
    });

    // Close on Escape
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeNav();
    });

    // Close after clicking an anchor
    nav.addEventListener("click", (e) => {
      const a = e.target.closest("a");
      if (!a) return;
      if (a.getAttribute("href")?.startsWith("#")) closeNav();
    });

    // Close when clicking outside
    document.addEventListener("click", (e) => {
      if (nav.contains(e.target) || btn.contains(e.target)) return;
      closeNav();
    });
  }

  // Reveal on scroll
  if (!prefersReducedMotion && "IntersectionObserver" in window) {
    const items = document.querySelectorAll(".reveal");
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        });
      },
      { threshold: 0.12 }
    );
    items.forEach((el) => io.observe(el));
  } else {
    document.querySelectorAll(".reveal").forEach((el) => el.classList.add("is-visible"));
  }

  // Active nav highlight on scroll
  const sectionIds = ["services", "team", "branches", "contact"];
  const sections = sectionIds
    .map((id) => document.getElementById(id))
    .filter(Boolean);

  const navLinks = Array.from(document.querySelectorAll('#primary-nav a[href^="#"]'));

  const setActive = (id) => {
    navLinks.forEach((a) => {
      const href = a.getAttribute("href") || "";
      const isActive = href === `#${id}`;
      if (isActive) a.setAttribute("data-active", "true");
      else a.removeAttribute("data-active");
    });
  };

  const findCurrentSection = () => {
    const y = window.scrollY + 120; // header offset
    let current = null;
    for (const s of sections) {
      if (s.offsetTop <= y) current = s;
    }
    return current?.id || null;
  };

  const onScroll = () => {
    const id = findCurrentSection();
    if (id) setActive(id);
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
})();