// Shared Navigation & Shell Controller
function initMobileMenu() {
  const navbar = document.getElementById('navbar');
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const backdrop = document.getElementById('mobile-menu-backdrop');
  const menuIcon = document.getElementById('mobile-menu-icon');
  if (!mobileMenuBtn || !mobileMenu) return;

  function openMenu() {
    mobileMenu.classList.remove('hidden');
    if (backdrop) backdrop.classList.remove('hidden');
    if (navbar) {
      navbar.style.backgroundColor = '#FFFFFF';
      navbar.classList.add('shadow-sm');
    }
    document.body.classList.add('overflow-hidden');
    mobileMenuBtn.setAttribute('aria-expanded', 'true');
    mobileMenuBtn.setAttribute('aria-label', 'Menü schließen');
    if (menuIcon) {
      menuIcon.setAttribute('data-lucide', 'x');
      if (typeof lucide !== 'undefined') lucide.createIcons();
    }
  }

  function closeMenu() {
    mobileMenu.classList.add('hidden');
    if (backdrop) backdrop.classList.add('hidden');
    if (navbar) {
      if (window.scrollY > 20) {
        navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
      } else {
        navbar.style.backgroundColor = 'transparent';
      }
      navbar.classList.remove('shadow-sm');
    }
    document.body.classList.remove('overflow-hidden');
    mobileMenuBtn.setAttribute('aria-expanded', 'false');
    mobileMenuBtn.setAttribute('aria-label', 'Menü öffnen');
    if (menuIcon) {
      menuIcon.setAttribute('data-lucide', 'menu');
      if (typeof lucide !== 'undefined') lucide.createIcons();
    }
  }

  mobileMenuBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
    if (isExpanded) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  if (backdrop) backdrop.addEventListener('click', closeMenu);

  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !mobileMenu.classList.contains('hidden')) {
      closeMenu();
      mobileMenuBtn.focus();
    }
  });

  document.addEventListener('click', (e) => {
    if (!mobileMenu.classList.contains('hidden') && !mobileMenu.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
      closeMenu();
    }
  });
}

function initNavbarScroll() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;
  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      navbar.classList.add('navbar-scrolled');
    } else {
      navbar.classList.remove('navbar-scrolled');
    }
  }, { passive: true });
}

function initAOSGlobal() {
  if (typeof AOS === 'undefined') return;
  AOS.init({
    duration: 750,
    easing: 'ease-out-cubic',
    once: false,
    offset: 50,
    mirror: true,
    disable: () => window.matchMedia('(prefers-reduced-motion: reduce)').matches
  });
}

function initCountersGlobal() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const counters = document.querySelectorAll('[data-counter-target]');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseFloat(el.getAttribute('data-counter-target'));
        const prefix = el.getAttribute('data-counter-prefix') || '';
        const suffix = el.getAttribute('data-counter-suffix') || '';
        const duration = 1400;
        const startTime = performance.now();

        function updateCounter(now) {
          const elapsed = now - startTime;
          const progress = Math.min(elapsed / duration, 1);
          const easeProgress = 1 - Math.pow(1 - progress, 3);
          const current = Math.round(target * easeProgress);
          el.textContent = prefix + current.toLocaleString('de-DE') + suffix;
          if (progress < 1) {
            requestAnimationFrame(updateCounter);
          } else {
            el.textContent = prefix + target.toLocaleString('de-DE') + suffix;
          }
        }
        requestAnimationFrame(updateCounter);
        obs.unobserve(el);
      }
    });
  }, { threshold: 0.2 });

  counters.forEach(c => observer.observe(c));
}

document.addEventListener('DOMContentLoaded', () => {
  if (typeof lucide !== 'undefined') lucide.createIcons();
  initAOSGlobal();
  initNavbarScroll();
  initMobileMenu();
  initCountersGlobal();
});
