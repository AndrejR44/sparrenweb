# builder_helper.py
# Shared navigation, head, and footer markup for all subpages and site generators

def get_head(title, description, canonical_page):
    return f"""<!DOCTYPE html>
<html lang="de" class="scroll-smooth overflow-x-hidden">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://sparrenweb.de/{canonical_page}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  
  <!-- Open Graph -->
  <meta property="og:locale" content="de_DE">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="SparrenWeb">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://sparrenweb.de/{canonical_page}">
  <meta property="og:image" content="https://sparrenweb.de/og-cover.jpg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
  <meta name="theme-color" content="#2563EB">

  <!-- Tailwind CSS & Shared Config -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="tailwind-shared-config.js"></script>

  <!-- Central Pricing Data -->
  <script src="pricing-data.js"></script>

  <!-- Lucide & AOS -->
  <script src="assets/lucide.js"></script>
  <script>
    if (typeof lucide === 'undefined') {{
      document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/lucide/0.344.0/umd/lucide.min.js"><\\/script>');
    }}
  </script>
  <link rel="stylesheet" href="assets/aos.css">
  <script src="assets/aos.js"></script>
  <script>
    if (typeof AOS === 'undefined') {{
      document.write('<link rel="stylesheet" href="https://unpkg.com/aos@2.3.4/dist/aos.css">');
      document.write('<script src="https://unpkg.com/aos@2.3.4/dist/aos.js"><\\/script>');
    }}
  </script>

  <!-- Fonts & Shared CSS -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="site-common.css">
</head>
<body class="bg-palette-canvas text-palette-primary font-sans antialiased selection:bg-blue-600 selection:text-white">
"""

def get_navbar(active_page):
    links = [
        ("index.html", "Startseite"),
        ("gewerke.html", "Gewerke"),
        ("leistungen.html", "Leistungen"),
        ("referenzen.html", "System-Demos"),
        ("ablauf.html", "Ablauf &amp; FAQ"),
    ]
    
    desktop_links_html = []
    for href, label in links:
        is_active = (href == active_page)
        if is_active:
            desktop_links_html.append(f'<a href="{href}" class="text-xs xl:text-[13px] text-[#2563EB] bg-blue-50/80 px-2.5 xl:px-3.5 py-1.5 rounded-full font-bold whitespace-nowrap">{label}</a>')
        else:
            desktop_links_html.append(f'<a href="{href}" class="text-xs xl:text-[13px] text-slate-700 hover:text-slate-950 hover:bg-slate-100 px-2.5 xl:px-3.5 py-1.5 rounded-full transition-all font-medium whitespace-nowrap">{label}</a>')
    
    mobile_links_html = []
    for href, label in links:
        is_active = (href == active_page)
        if is_active:
            mobile_links_html.append(f'<a href="{href}" class="block text-sm text-[#2563EB] bg-blue-50/80 py-2.5 px-3 rounded-lg font-bold transition-colors">{label}</a>')
        else:
            mobile_links_html.append(f'<a href="{href}" class="block text-sm text-slate-800 hover:text-[#2563EB] py-2.5 px-3 rounded-lg hover:bg-slate-50 font-semibold transition-colors">{label}</a>')

    d_html = "\n        ".join(desktop_links_html)
    m_html = "\n        ".join(mobile_links_html)

    return f"""  <!-- Navigation Bar -->
  <nav id="navbar" class="fixed top-0 left-0 right-0 z-50 transition-all duration-300" style="background: transparent;">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-20 flex items-center justify-between gap-2 sm:gap-4">
      
      <!-- Brand Logo + Region Badge -->
      <a href="index.html" class="flex items-center gap-2.5 group shrink-0 whitespace-nowrap" aria-label="SparrenWeb Startseite">
        <picture class="flex items-center shrink-0">
          <source srcset="logo.webp" type="image/webp">
          <img src="logo.png" alt="SparrenWeb" class="h-7 sm:h-8 md:h-8.5 w-auto object-contain transition-transform duration-200 group-hover:scale-[1.02]" width="217" height="36">
        </picture>
        <span class="hidden 2xl:inline-flex items-center gap-1.5 text-[10px] font-semibold text-slate-500 tracking-wider uppercase pl-3 border-l border-slate-200/80 py-0.5 whitespace-nowrap shrink-0">
          <span class="w-1.5 h-1.5 rounded-full bg-[#2563EB]"></span>
          Bielefeld &amp; OWL
        </span>
      </a>

      <!-- Central Nav Links -->
      <div class="hidden lg:flex items-center gap-0.5 xl:gap-1 bg-white/90 backdrop-blur-md px-2.5 xl:px-3.5 py-1.5 rounded-full border border-slate-200/80 shadow-xs shrink-0 whitespace-nowrap">
        {d_html}
      </div>

      <!-- Action Button & Trust Access -->
      <div class="flex items-center gap-2 xl:gap-3 shrink-0 whitespace-nowrap">
        <a href="anfrage.html" class="hidden sm:inline-flex items-center gap-2 bg-[#2563EB] hover:bg-blue-700 text-white text-xs xl:text-[13px] font-semibold px-4 xl:px-5 py-2 xl:py-2.5 rounded-full transition-all shadow-sm shadow-blue-600/25 hover:shadow-md hover:-translate-y-0.5 whitespace-nowrap shrink-0">
          <span class="whitespace-nowrap">System-Entwurf anfordern</span>
          <i data-lucide="arrow-right" class="w-3.5 h-3.5 shrink-0"></i>
        </a>

        <!-- Mobile menu toggle -->
        <button id="mobile-menu-btn" class="lg:hidden text-slate-800 p-2 sm:p-2.5 rounded-xl bg-slate-100 border border-slate-200 focus:outline-none focus:ring-2 focus:ring-[#2563EB] shrink-0" aria-label="Menü öffnen" aria-expanded="false" aria-controls="mobile-menu">
          <i data-lucide="menu" id="mobile-menu-icon" class="w-5 h-5"></i>
        </button>
      </div>
    </div>

    <!-- Mobile menu -->
    <div id="mobile-menu" class="hidden lg:hidden bg-white border-b border-slate-200 px-5 pt-3 pb-6 space-y-2.5 shadow-2xl transition-all relative z-50" style="background-color: #FFFFFF;" role="region" aria-label="Mobiles Navigationsmenü">
      <div class="space-y-1 pb-2 border-b border-slate-100">
        {m_html}
      </div>
      <div class="pt-1 space-y-2">
        <a href="anfrage.html" class="block bg-[#2563EB] hover:bg-blue-700 text-white text-xs font-bold px-4 py-3 rounded-xl text-center shadow-md shadow-blue-500/20 transition-all">
          Kostenlosen System-Entwurf anfordern →
        </a>
      </div>
    </div>

    <!-- Mobile menu backdrop overlay -->
    <div id="mobile-menu-backdrop" class="fixed inset-0 top-20 bg-slate-950/60 backdrop-blur-xs z-40 hidden lg:hidden" aria-hidden="true"></div>
  </nav>
"""

def get_footer():
    return """  <!-- Footer -->
  <footer class="border-t border-slate-200/80 py-12 px-6 bg-slate-50/60">
    <div class="max-w-5xl mx-auto space-y-6">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 border-b border-slate-200/60 pb-6">
        <div class="flex items-center gap-3">
          <picture class="flex items-center">
            <source srcset="logo.webp" type="image/webp">
            <img src="logo.png" alt="SparrenWeb" class="h-6 md:h-7 w-auto object-contain opacity-95" width="169" height="28">
          </picture>
          <span class="text-xs text-slate-600 font-medium pl-3 border-l border-slate-300">Bielefeld &amp; Ostwestfalen-Lippe</span>
        </div>
        <div class="flex flex-wrap items-center gap-4 text-xs text-slate-600 font-medium">
          <a href="gewerke.html" class="hover:text-slate-950 transition-colors">Gewerke</a>
          <a href="leistungen.html" class="hover:text-slate-950 transition-colors">Leistungen</a>
          <a href="referenzen.html" class="hover:text-slate-950 transition-colors">System-Demos</a>
          <a href="ablauf.html" class="hover:text-slate-950 transition-colors">Ablauf &amp; FAQ</a>
          <a href="anfrage.html" class="hover:text-slate-950 transition-colors">System anfragen</a>
          <a href="impressum.html" class="hover:text-slate-950 transition-colors">Impressum</a>
          <a href="datenschutz.html" class="hover:text-slate-950 transition-colors">Datenschutz</a>
        </div>
      </div>
      <div class="flex flex-col sm:flex-row items-center justify-between gap-3 text-[11px] text-slate-500 font-medium">
        <div>
          © 2026 SparrenWeb. Alle Preise verstehen sich netto zzgl. gesetzlicher Mehrwertsteuer.
        </div>
        <div class="flex items-center gap-3">
          <span>Website-Kauf statt Website-Miete</span>
          <span>•</span>
          <span>Optionale Betreuung monatlich kündbar</span>
          <span>•</span>
          <span>Bielefeld &amp; OWL</span>
        </div>
      </div>
    </div>
  </footer>

  <script src="site-nav.js"></script>
</body>
</html>
"""
