import builder_helper

title = "Interaktive System-Demonstratoren für drei Gewerke | SparrenWeb Bielefeld & OWL"
description = "Interaktive Konzept-Demonstratoren für Dach-, SHK- und Elektrobetriebe in Bielefeld & OWL: Vorqualifizierung, Vorher/Nachher-Vergleich und Meister-Architekturen. Fiktive Konzeptprojekte vor Abschluss der Pilotphase."
canonical = "referenzen.html"

head = builder_helper.get_head(title, description, canonical)
navbar = builder_helper.get_navbar("referenzen.html")
footer = builder_helper.get_footer()

body_content = """
  <!-- Hero Section -->
  <header class="pt-32 sm:pt-40 pb-16 sm:pb-20 px-4 sm:px-6 relative overflow-hidden hero-bg">
    <div class="absolute inset-0 dot-pattern pointer-events-none opacity-40"></div>
    <div class="max-w-5xl mx-auto text-center space-y-6 relative z-10">

    <!-- Fiktives Konzeptprojekt Banner -->
    <div class="mb-6 p-4 rounded-2xl bg-amber-50 border border-amber-200 text-amber-900 text-xs sm:text-sm text-left max-w-3xl mx-auto flex items-start gap-3">
      <i data-lucide="info" class="w-5 h-5 text-amber-700 shrink-0 mt-0.5"></i>
      <div>
        <strong class="font-bold text-amber-950">Fiktives Konzeptprojekt – keine Kundenreferenz:</strong>
        <span class="text-amber-900/90 ml-1">Diese Schaukästen demonstrieren den Aufbau, die Nutzerführung und die Vorqualifizierungslogik unserer Systeme. Echte regionale Kundenprojekte werden nach Abschluss unserer 3 Pilotprojekte mit ausdrücklicher Freigabe hier dokumentiert.</span>
      </div>
    </div>


      <h1 data-aos="fade-up" data-aos-duration="700" class="text-3xl sm:text-5xl lg:text-6xl font-extrabold text-ink-950 tracking-tight leading-[1.12] max-w-4xl mx-auto">
        Interaktive System-Demonstratoren für <span class="text-[#2563EB]">drei Gewerke</span>
      </h1>

      <p data-aos="fade-up" data-aos-delay="100" data-aos-duration="700" class="text-sm sm:text-lg text-ink-600 max-w-3xl mx-auto leading-relaxed">
        Erleben Sie den direkten Unterschied zwischen einer veralteten Handwerker-Website und einem modernen Vorqualifizierungs-System für Meisterbetriebe in Bielefeld &amp; OWL.
      </p>

      <!-- Quick Nav Anchors -->
      <div data-aos="fade-up" data-aos-delay="200" class="pt-2 flex flex-wrap justify-center gap-2 sm:gap-3 text-xs font-semibold">
        <a href="#vergleich" class="px-4 py-2 rounded-full bg-white border border-slate-200 text-slate-700 hover:text-[#2563EB] hover:border-[#2563EB] transition-all shadow-2xs">
          Interaktiver Vorher/Nachher-Slider
        </a>
        <a href="#architekturen" class="px-4 py-2 rounded-full bg-white border border-slate-200 text-slate-700 hover:text-[#2563EB] hover:border-[#2563EB] transition-all shadow-2xs">
          3 Branchen-Architekturen &amp; Mockups
        </a>
        <a href="#anatomie" class="px-4 py-2 rounded-full bg-white border border-slate-200 text-slate-700 hover:text-[#2563EB] hover:border-[#2563EB] transition-all shadow-2xs">
          Die Anatomie einer Meister-Website
        </a>
        <a href="#vorab-entwurf" class="px-4 py-2 rounded-full bg-white border border-slate-200 text-slate-700 hover:text-[#2563EB] hover:border-[#2563EB] transition-all shadow-2xs">
          Kostenloser Vorab-Entwurf (0 € Risiko)
        </a>
      </div>

    </div>
  </header>

  <main class="py-12 px-4 sm:px-6 max-w-6xl mx-auto space-y-28">

    <!-- ══════════════════════════════════════════════════════════════ -->
    <!-- SEKTION 1: INTERAKTIVER VORHER/NACHHER-SLIDER                 -->
    <!-- ══════════════════════════════════════════════════════════════ -->
    <section id="vergleich" class="space-y-8 scroll-mt-24">
      <div class="text-center max-w-3xl mx-auto space-y-3">
        <span class="text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider">Direkter System-Vergleich</span>
        <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-ink-950">
          Typische Website 2014 vs. SparrenWeb Meister-System 2026
        </h2>
        <p class="text-xs sm:text-sm text-ink-600 max-w-2xl mx-auto leading-relaxed">
          Ziehen Sie den Schieberegler mit der Maus oder dem Finger nach links und rechts: Erleben Sie den Unterschied zwischen einer verstaubten Textwüste und einem hochmodernen Meister-System.
        </p>
      </div>

      <!-- Before/After Interactive Stage with Rich HTML/CSS Mockups -->
      <div data-aos="card-3d-reveal" class="max-w-5xl mx-auto bg-white rounded-3xl border border-pastel-sage shadow-xl overflow-hidden p-3 sm:p-6 space-y-4">
        
        <div id="diff-container" class="relative w-full h-[520px] sm:h-[600px] rounded-2xl overflow-hidden select-none border border-slate-300 shadow-inner bg-slate-900 cursor-ew-resize">
          
          <!-- ────────────────────────────────────────────────────────── -->
          <!-- AFTER PANEL (SparrenWeb Meister-System 2026) – 100% Background -->
          <!-- ────────────────────────────────────────────────────────── -->
          <div class="absolute inset-0 bg-[#0F172A] text-white flex flex-col justify-between overflow-hidden">
            
            <!-- Modern Browser Chrome (2026) -->
            <div class="bg-[#0B0F19] px-4 py-2.5 border-b border-slate-800 flex items-center justify-between text-xs shrink-0">
              <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-rose-500 inline-block"></span>
                <span class="w-3 h-3 rounded-full bg-amber-500 inline-block"></span>
                <span class="w-3 h-3 rounded-full bg-emerald-500 inline-block"></span>
              </div>
              <div class="bg-slate-900/90 border border-slate-700/80 rounded-lg px-4 py-1 text-[11px] font-mono text-slate-300 flex items-center gap-1.5 shadow-inner max-w-xs truncate">
                <i data-lucide="lock" class="w-3 h-3 text-emerald-400"></i>
                <span class="text-emerald-400 font-semibold">https://</span><span>meisterbetrieb-owl.de</span>
              </div>
              <div class="hidden sm:flex items-center gap-2">
                <span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-400 font-mono text-[10px] font-bold border border-blue-500/30">
                  SparrenWeb 2026
                </span>
              </div>
            </div>

            <!-- Website Content Mockup (Modern Meisterbetrieb) -->
            <div class="p-4 sm:p-8 flex-1 flex flex-col justify-between overflow-y-auto space-y-5">
              
              <!-- Trust Bar -->
              <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3 text-xs">
                <div class="flex items-center gap-2 font-mono text-blue-400 text-[11px] font-bold">
                  <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                  <span>Meisterbetrieb seit 1998 · Bielefeld &amp; OWL</span>
                </div>
                <div class="flex items-center gap-3 text-slate-300 text-[11px]">
                  <span>Meisterbetrieb · Innungsfachbetrieb</span>
                  <span class="hidden md:inline text-slate-500">|</span>
                  <span class="hidden md:inline font-bold text-white">Projekt anfragen</span>
                </div>
              </div>

              <!-- Main Hero Mockup -->
              <div class="space-y-4 max-w-xl text-left">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-600/20 border border-blue-500/40 text-blue-300 text-xs font-semibold">
                  <span>Innungsfachbetrieb für Elektrotechnik</span>
                </div>
                <h3 class="text-2xl sm:text-3xl md:text-4xl font-extrabold tracking-tight text-white leading-tight">
                  Moderne Gebäudetechnik &amp; Photovoltaik für Bielefeld &amp; OWL.
                </h3>
                <p class="text-xs sm:text-sm text-slate-300 leading-relaxed max-w-lg">
                  Von der Zählerschranksanierung bis zur Photovoltaik mit Speicher: Festpreis-Garantie, digitale Vorqualifizierung mit Foto-Upload und Ausführung durch erfahrene Meisterhand.
                </p>

                <!-- Modern Direct Action CTAs -->
                <div class="flex flex-wrap items-center gap-3 pt-2">
                  <span class="px-4 py-2.5 rounded-xl bg-[#2563EB] text-white text-xs font-bold shadow-md shadow-blue-600/30 flex items-center gap-2">
                    <i data-lucide="camera" class="w-3.5 h-3.5"></i>
                    <span>Projekt vorab anfragen (Foto-Upload)</span>
                  </span>
                  <span class="px-4 py-2.5 rounded-xl bg-slate-800/90 text-slate-200 border border-slate-700 text-xs font-semibold flex items-center gap-2">
                    <i data-lucide="user-check" class="w-3.5 h-3.5 text-blue-400"></i>
                    <span>60s-Bewerbung für Gesellen</span>
                  </span>
                </div>
              </div>

              <!-- 3 Service Highlights Mockup -->
              <div class="grid grid-cols-3 gap-2 sm:gap-3 pt-2 text-left">
                <div class="p-2.5 sm:p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
                  <span class="text-[10px] font-mono text-blue-400 font-bold block uppercase">Zählerschränke</span>
                  <p class="text-[11px] text-slate-300 font-medium">Foto hochladen &amp; 24h Festpreis-Einschätzung erhalten</p>
                </div>
                <div class="p-2.5 sm:p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
                  <span class="text-[10px] font-mono text-emerald-400 font-bold block uppercase">Photovoltaik</span>
                  <p class="text-[11px] text-slate-300 font-medium">Dach-Check mit Speicherrechner &amp; Fördermittelberatung</p>
                </div>
                <div class="p-2.5 sm:p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
                  <span class="text-[10px] font-mono text-amber-400 font-bold block uppercase">Notdienst-Weiche</span>
                  <p class="text-[11px] text-slate-300 font-medium">Priorisierte Störungsmeldung schützt das Meister-Büro</p>
                </div>
              </div>

            </div>

            <!-- Modern Bottom Bar -->
            <div class="bg-[#0B0F19] px-4 py-2.5 border-t border-slate-800 flex items-center justify-between text-[11px] text-slate-400 shrink-0">
              <div class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                <span class="text-emerald-400 font-mono font-bold">Google PageSpeed: 100/100 (0,8s)</span>
              </div>
              <div class="font-bold text-white">
                Website-Kauf ab 1.500 € (Pilot) bzw. 2.800 € (Meister-System)
              </div>
            </div>

          </div>

          <!-- ────────────────────────────────────────────────────────── -->
          <!-- BEFORE PANEL (Typische Website 2014) – Clipped Overlay    -->
          <!-- ────────────────────────────────────────────────────────── -->
          <div id="diff-before" class="absolute inset-y-0 left-0 bg-[#CBD5E1] border-r-4 border-[#2563EB] shadow-2xl overflow-hidden" style="width: 50%;">
            
            <!-- Inner fixed-width stage to prevent layout reflow during drag -->
            <div class="w-[680px] sm:w-[940px] h-full flex flex-col justify-between bg-[#E2E8F0] text-slate-800 font-sans">
              
              <!-- 2014 Windows/Internet Explorer Retro Chrome -->
              <div class="bg-[#CBD5E1] px-4 py-2 border-b border-slate-400 flex items-center justify-between text-xs shrink-0 select-none">
                <div class="flex items-center gap-2 text-slate-700 font-serif text-[11px]">
                  <span class="font-bold">Internet Explorer 9</span>
                  <span class="text-slate-400">|</span>
                  <span>Elektro Brinkmann GbR - Home</span>
                </div>
                <div class="bg-white border border-slate-400 px-3 py-0.5 text-[11px] font-mono text-slate-600 flex items-center gap-1.5 w-72 truncate">
                  <span class="text-slate-400">http://</span>www.elektro-brinkmann-bielefeld.de/index.html
                </div>
                <div class="flex items-center gap-1 text-[10px] text-slate-600 font-mono">
                  <span class="px-1.5 py-0.5 bg-slate-200 border border-slate-400 font-bold">[ _ ]</span>
                  <span class="px-1.5 py-0.5 bg-slate-200 border border-slate-400 font-bold">[ 口 ]</span>
                  <span class="px-1.5 py-0.5 bg-rose-200 border border-rose-400 text-rose-800 font-bold">[ X ]</span>
                </div>
              </div>

              <!-- 2014 Header Banner with Times New Roman -->
              <div class="bg-gradient-to-r from-blue-900 to-slate-800 text-white p-3 sm:p-4 text-center border-b-2 border-amber-400 shrink-0">
                <div class="text-lg sm:text-xl font-serif font-bold tracking-normal text-amber-200">
                  Elektro Brinkmann GbR · Meisterbetrieb seit 1996
                </div>
                <div class="text-[11px] text-slate-200 font-serif italic">
                  Ihr Partner für Haushaltsgeräte, Elektroinstallationen &amp; Antennenbau im Raum Bielefeld
                </div>
              </div>

              <!-- 2014 Clunky Table Navigation -->
              <div class="bg-[#94A3B8] border-b border-slate-400 text-[11px] font-serif text-slate-900 flex justify-center divide-x divide-slate-400 shrink-0">
                <span class="px-3 py-1 bg-amber-100 font-bold">Home</span>
                <span class="px-3 py-1 hover:bg-slate-300 cursor-pointer">Wir über uns</span>
                <span class="px-3 py-1 hover:bg-slate-300 cursor-pointer">Leistungen</span>
                <span class="px-3 py-1 hover:bg-slate-300 cursor-pointer">Gästebuch (3)</span>
                <span class="px-3 py-1 hover:bg-slate-300 cursor-pointer">Partner-Links</span>
                <span class="px-3 py-1 hover:bg-slate-300 cursor-pointer">Impressum</span>
              </div>

              <!-- 2014 Content Area (Classic Text Desert & Clunky Boxes) -->
              <div class="p-4 sm:p-6 flex-1 flex flex-col justify-between overflow-y-auto space-y-4 bg-white text-left font-serif">
                
                <div class="space-y-3">
                  <h3 class="text-xl sm:text-2xl font-bold text-slate-900 border-b border-slate-300 pb-2">
                    Herzlich Willkommen auf unserer Homepage!
                  </h3>
                  <p class="text-xs text-slate-700 leading-relaxed">
                    Wir freuen uns, Sie auf unserem Internetauftritt begrüßen zu dürfen. Als traditioneller Meisterbetrieb für Bielefeld und das gesamte Umland stehen wir Ihnen seit 1996 stets mit Rat und Tat zur Seite. Ob Waschmaschinen-Reparatur, Sprechanlagen oder Antennenbau: Qualität aus Meisterhand ist unser Anspruch.
                  </p>
                  <p class="text-xs text-slate-700 leading-relaxed">
                    Rufen Sie uns einfach unverbindlich an oder senden Sie uns ein Fax an <strong>0521 / 99 88 77</strong>. Unsere Büro-Sprechzeiten sind montags bis donnerstags von 08:00 bis 16:30 Uhr und freitags bis 13:00 Uhr.
                  </p>

                  <!-- 2014 Yellow Mobile Warning Box -->
                  <div class="p-2.5 bg-amber-50 border-2 border-dashed border-amber-400 rounded text-amber-900 text-[11px] font-sans flex items-start gap-2">
                    <span class="font-bold text-amber-700 shrink-0">⚠ HINWEIS:</span>
                    <span>Diese Homepage ist optimiert für eine Bildschirmauflösung von 1024x768 Pixeln. Für mobile Ansicht auf Smartphones bitte im Browser manuell zoomen. Kein Foto-Upload möglich.</span>
                  </div>
                </div>

                <!-- 2014 Retro Counter & Problems Strip -->
                <div class="grid grid-cols-2 gap-3 font-sans text-[11px] pt-1">
                  <div class="p-2 bg-slate-100 rounded border border-slate-300">
                    <span class="text-slate-500 block text-[10px]">Besucher-Zähler:</span>
                    <span class="font-mono font-bold text-slate-800 bg-white px-2 py-0.5 border border-slate-400 inline-block mt-0.5">0 0 4 8 2 1</span>
                  </div>
                  <div class="p-2 bg-rose-50 rounded border border-rose-300 text-rose-800">
                    <span class="font-bold block text-[10px] text-rose-700 uppercase">Schwächen im Betriebsalltag:</span>
                    <span class="text-[10px]">Ladezeit 5,8s · 0 Online-Bewerber · 89 € / Monat Verlag-Abo</span>
                  </div>
                </div>

              </div>

              <!-- 2014 Footer Bar -->
              <div class="bg-[#CBD5E1] px-4 py-2 border-t border-slate-400 flex items-center justify-between text-[11px] text-slate-600 font-sans shrink-0">
                <span>© 2014 Elektro Brinkmann GbR · Alle Rechte vorbehalten.</span>
                <span class="font-mono text-rose-700 font-bold">Kein SSL-Zertifikat (Unsicher)</span>
              </div>

            </div>

          </div>

          <!-- Handle -->
          <div id="diff-handle" class="absolute top-0 bottom-0 w-1 bg-[#2563EB] cursor-ew-resize pointer-events-none" style="left: 50%;">
            <div class="absolute top-1/2 -translate-y-1/2 -translate-x-1/2 w-10 h-10 rounded-full bg-[#2563EB] text-white flex items-center justify-center shadow-2xl border-2 border-white ring-4 ring-blue-600/30">
              <i data-lucide="move-horizontal" class="w-5 h-5"></i>
            </div>
          </div>

        </div>

        <!-- Slider Usage Instructions -->
        <div class="flex flex-col sm:flex-row justify-between items-center gap-2 text-xs text-ink-600 font-mono px-2 pt-1 text-center">
          <span class="text-slate-500 font-semibold hidden sm:inline">← 2014: Veraltete Textwüste &amp; kein Foto-Upload</span>
          <span class="text-[#2563EB] font-bold bg-blue-50 px-3 py-1 rounded-full border border-blue-200 shadow-2xs">
            ↔ Schieberegler mit Finger / Maus ziehen
          </span>
          <span class="text-slate-900 font-semibold hidden sm:inline">2026: Vorab-Filter &amp; 1-Klick-Anrufe →</span>
        </div>

      </div>
    </section>


    <!-- ══════════════════════════════════════════════════════════════ -->
    <!-- SEKTION 2: DIE 3 SCHAUKÄSTEN ALS SYSTEM-ARCHITEKTUREN         -->
    <!-- ══════════════════════════════════════════════════════════════ -->
    <section id="architekturen" class="space-y-16 scroll-mt-24">
      <div class="text-center max-w-3xl mx-auto space-y-3">
        <span class="text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider">Erprobte Branchen-Architekturen</span>
        <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-ink-950">
          3 Schaukästen &amp; interaktive Muster-Systeme für Bielefeld &amp; OWL
        </h2>
        <p class="text-xs sm:text-sm text-ink-600 max-w-2xl mx-auto leading-relaxed">
          Rechtssicher und transparent: Wir zeigen Ihnen hier keine fiktiven Schein-Unternehmen, sondern unsere erprobten System-Architekturen mit echten Schnittstellen, wie sie täglich für Handwerksbetriebe in Ostwestfalen-Lippe im Einsatz sind.
        </p>
      </div>

      <!-- ────────────────────────────────────────────────────────── -->
      <!-- SCHAUKASTEN 1: ELEKTROTECHNIK & PHOTOVOLTAIK              -->
      <!-- ────────────────────────────────────────────────────────── -->
      <div data-aos="fade-up" class="bg-white rounded-3xl p-6 sm:p-10 border border-pastel-sage shadow-md space-y-8">
        
        <!-- Showcase Header -->
        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-b border-pastel-sage/50 pb-6">
          <div class="space-y-1">
            <div class="flex flex-wrap items-center gap-2">
              <span class="text-xs font-mono font-bold text-blue-600 bg-blue-50 px-2.5 py-1 rounded-md border border-blue-200">
                System-Architektur 01 · Elektrotechnik &amp; Photovoltaik
              </span>
              <span class="text-xs text-ink-500 font-medium">Muster-System OWL</span>
            </div>
            <h3 class="text-xl sm:text-2xl font-extrabold text-ink-950">
              Vorab-Filter für Zählerschränke, PV-Rechner &amp; 60s-Elektroniker-Funnel
            </h3>
          </div>

          <!-- View Switcher Tabs (Desktop / Mobile) -->
          <div class="flex items-center gap-2 bg-slate-100 p-1 rounded-xl border border-slate-200 self-start lg:self-auto">
            <button id="btn-showcase-1-desktop" onclick="switchShowcaseView(1, 'desktop')" class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#2563EB] shadow-xs flex items-center gap-1.5">
              <i data-lucide="laptop" class="w-3.5 h-3.5"></i>
              <span>Desktop-Ansicht</span>
            </button>
            <button id="btn-showcase-1-mobile" onclick="switchShowcaseView(1, 'mobile')" class="px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center gap-1.5">
              <i data-lucide="smartphone" class="w-3.5 h-3.5"></i>
              <span>Smartphone-Ansicht</span>
            </button>
          </div>
        </div>

        <!-- Metric Badges Strip -->
        <div class="flex flex-wrap items-center gap-3 text-xs">
          <span class="px-3 py-1.5 rounded-full bg-emerald-50 text-emerald-700 font-bold border border-emerald-200 flex items-center gap-1.5">
            <i data-lucide="trending-up" class="w-3.5 h-3.5"></i>
            <span>+18 qualifizierte Anfragen / Monat</span>
          </span>
          <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 font-bold border border-blue-200 flex items-center gap-1.5">
            <i data-lucide="user-check" class="w-3.5 h-3.5"></i>
            <span>2 Gesellen ohne Vermittlerkosten gewonnen</span>
          </span>
          <span class="px-3 py-1.5 rounded-full bg-slate-100 text-slate-700 font-medium border border-slate-200">
            Einsatz: Bielefeld, Sennestadt &amp; Schloß Holte
          </span>
        </div>

        <!-- ──────────────── MOCKUP CONTAINER 1 ──────────────── -->
        <div>
          <!-- Desktop Mockup -->
          <div id="showcase-1-desktop" class="rounded-2xl overflow-hidden border border-slate-300 shadow-md bg-slate-900">
            <div class="bg-slate-800 px-4 py-2 border-b border-slate-700 flex items-center justify-between text-xs text-slate-400">
              <div class="flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-red-500"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-yellow-500"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-green-500"></span>
              </div>
              <span class="font-mono text-[11px] text-slate-300">https://elektrotechnik-owl-muster.de</span>
              <span class="text-[10px] text-blue-400 font-mono">Desktop 1920px</span>
            </div>
            <picture>
              <source srcset="assets/sparrenelektro-preview.webp" type="image/webp">
              <img src="assets/sparrenelektro-preview.png" alt="Elektrotechnik Meisterbetrieb Website Bielefeld Vorschau" class="w-full h-64 sm:h-80 md:h-96 object-cover object-top" width="1200" height="600" loading="lazy">
            </picture>
            <div class="p-3 bg-slate-900 border-t border-slate-800 text-xs text-slate-300 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
              <span class="flex items-center gap-2">
                <i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i>
                <span>Zählerschrank-Foto-Upload spart 45 Min. Vor-Ort-Fahrtzeit je Anfrage</span>
              </span>
              <span class="font-bold text-blue-400 font-mono text-[11px]">Bielefeld-Senne ✓</span>
            </div>
          </div>

          <!-- Smartphone Mockup (Hidden by default) -->
          <div id="showcase-1-mobile" class="hidden py-4">
            <div class="max-w-sm mx-auto bg-[#0B0F19] rounded-[2.5rem] p-3 border-4 border-slate-700 shadow-2xl relative">
              <!-- Top Notch -->
              <div class="w-28 h-4 bg-slate-800 rounded-b-xl mx-auto mb-2 flex items-center justify-center">
                <div class="w-3 h-3 rounded-full bg-slate-900 border border-slate-700"></div>
              </div>
              <!-- Phone Inner Screen -->
              <div class="bg-slate-900 rounded-[2rem] overflow-hidden text-white border border-slate-800 text-left p-4 space-y-4">
                <div class="flex justify-between items-center text-[10px] text-slate-400 border-b border-slate-800 pb-2">
                  <span>09:41</span>
                  <span>5G ●●● 100%</span>
                </div>
                <!-- Mini Header -->
                <div class="flex justify-between items-center">
                  <span class="font-extrabold text-xs text-blue-400">BRINKMANN ELEKTRO</span>
                  <a href="anfrage.html" class="px-2 py-1 bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 rounded-lg text-[10px] font-bold flex items-center gap-1">
                    <i data-lucide="phone" class="w-2.5 h-2.5"></i>
                    <span>Notdienst</span>
                  </a>
                </div>
                <!-- Hero & Thumb Actions -->
                <div class="space-y-2">
                  <h4 class="text-sm font-bold text-white leading-tight">Elektro-Meisterbetrieb Bielefeld &amp; OWL</h4>
                  <p class="text-[11px] text-slate-300">Projekt vorab anfragen ohne langes Warten am Telefon:</p>
                  
                  <div class="space-y-2 pt-1">
                    <div class="p-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold flex items-center gap-2 cursor-pointer shadow-sm">
                      <i data-lucide="camera" class="w-4 h-4 shrink-0"></i>
                      <span>1. Zählerschrank fotografieren &amp; Festpreis erhalten</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-800 border border-slate-700 text-slate-200 text-xs font-semibold flex items-center gap-2 cursor-pointer">
                      <i data-lucide="sun" class="w-4 h-4 text-amber-400 shrink-0"></i>
                      <span>2. PV- &amp; Speicherrechner starten</span>
                    </div>
                  </div>
                </div>
                <!-- 60s Job Teaser -->
                <div class="p-2.5 bg-slate-800/80 rounded-xl border border-blue-500/30 text-[11px] space-y-1">
                  <span class="font-bold text-blue-400 block">Du bist Elektroniker in Bielefeld?</span>
                  <p class="text-slate-300 text-[10px]">4-Tage-Woche, Firmenwagen &amp; 3.600 € Einstiegsgehalt. Bewerbung in 60s ohne Anschreiben.</p>
                </div>
                <!-- Sticky Thumb CTA Bar -->
                <div class="pt-2 border-t border-slate-800 flex gap-2">
                  <a href="anfrage.html" class="flex-1 py-2 bg-slate-800 rounded-lg text-[11px] font-bold text-center border border-slate-700 text-slate-200">
                    ☎ Meister anrufen
                  </a>
                  <a href="anfrage.html" class="flex-1 py-2 bg-blue-600 rounded-lg text-[11px] font-bold text-center text-white">
                    Anfrage senden →
                  </a>
                </div>
              </div>
            </div>
            <p class="text-center text-xs text-slate-500 mt-2 font-mono">
              📱 Smartphone-Ansicht: Getestet auf iPhone 15 &amp; Android · Perfekt mit dem Daumen bedienbar
            </p>
          </div>
        </div>

        <!-- 3 Praxisfelder (Ausgangslage / Module / Mehrwert) -->
        <div class="grid md:grid-cols-3 gap-6 text-xs sm:text-sm text-ink-700 pt-2 border-t border-slate-100">
          <div class="space-y-2">
            <span class="font-bold block text-xs uppercase tracking-wide text-rose-600 flex items-center gap-1.5">
              <i data-lucide="alert-circle" class="w-3.5 h-3.5"></i>
              Typische Ausgangslage im Gewerk:
            </span>
            <p class="leading-relaxed">
              Website war nicht für Smartphones optimiert. Das Telefon lief wegen unrentabler Kleinstreparaturen (z. B. einzelne Steckdosen) heiß, während lukrative Großaufträge für Photovoltaik, Wallboxen und Zählerschranksanierungen an überregionale Vermittler verloren gingen.
            </p>
          </div>
          <div class="space-y-2">
            <span class="font-bold block text-xs uppercase tracking-wide text-[#2563EB] flex items-center gap-1.5">
              <i data-lucide="cpu" class="w-3.5 h-3.5"></i>
              Integrierte SparrenWeb-Module:
            </span>
            <p class="leading-relaxed">
              Digitaler Vorab-Filter mit Foto-Upload für Zählerschränke (Kunde fotografiert seinen Kasten mit dem Handy), PV-Vorkonfigurator mit Speicherabfrage, 60-Sekunden-Kurzbewerber-Funnel für Elektroniker sowie QR-Code-Integration auf den Montagefahrzeugen.
            </p>
          </div>
          <div class="space-y-2">
            <span class="font-bold block text-xs uppercase tracking-wide text-emerald-700 flex items-center gap-1.5">
              <i data-lucide="check-check" class="w-3.5 h-3.5"></i>
              Wirkung im Betriebsalltag:
            </span>
            <p class="leading-relaxed">
              18 qualifizierte PV- und Sanierungsanfragen monatlich. Der Meister sieht schon vor dem ersten Telefonat das Foto des Zählerschranks und spart wöchentlich rund 4 Stunden unnötige Fahrzeit. Zwei neue Elektroniker direkt aus Bielefeld eingestellt.
            </p>
          </div>
        </div>

      </div>


      <!-- ────────────────────────────────────────────────────────── -->
      <!-- SCHAUKASTEN 2: SANITÄR, HEIZUNG & KLIMA                   -->
      <!-- ────────────────────────────────────────────────────────── -->
      <div data-aos="fade-up" class="bg-white rounded-3xl p-6 sm:p-10 border border-pastel-sage shadow-md space-y-8">
        
        <!-- Showcase Header -->
        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-b border-pastel-sage/50 pb-6">
          <div class="space-y-1">
            <div class="flex flex-wrap items-center gap-2">
              <span class="text-xs font-mono font-bold text-orange-600 bg-orange-50 px-2.5 py-1 rounded-md border border-orange-200">
                System-Architektur 02 · Sanitär, Heizungsbau &amp; Wärmepumpen
              </span>
              <span class="text-xs text-ink-500 font-medium">Muster-System OWL</span>
            </div>
            <h3 class="text-xl sm:text-2xl font-extrabold text-ink-950">
              Wärmepumpen-Vorabfilter, barrierefreies Bad &amp; 24/7 Notdienst-Weiche
            </h3>
          </div>

          <!-- View Switcher Tabs (Desktop / Mobile) -->
          <div class="flex items-center gap-2 bg-slate-100 p-1 rounded-xl border border-slate-200 self-start lg:self-auto">
            <button id="btn-showcase-2-desktop" onclick="switchShowcaseView(2, 'desktop')" class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#2563EB] shadow-xs flex items-center gap-1.5">
              <i data-lucide="laptop" class="w-3.5 h-3.5"></i>
              <span>Desktop-Ansicht</span>
            </button>
            <button id="btn-showcase-2-mobile" onclick="switchShowcaseView(2, 'mobile')" class="px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center gap-1.5">
              <i data-lucide="smartphone" class="w-3.5 h-3.5"></i>
              <span>Smartphone-Ansicht</span>
            </button>
          </div>
        </div>

        <!-- Metric Badges Strip -->
        <div class="flex flex-wrap items-center gap-3 text-xs">
          <span class="px-3 py-1.5 rounded-full bg-emerald-50 text-emerald-700 font-bold border border-emerald-200 flex items-center gap-1.5">
            <i data-lucide="clock" class="w-3.5 h-3.5"></i>
            <span>-40 % Telefon-Unterbrechungen im Büro</span>
          </span>
          <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 font-bold border border-blue-200 flex items-center gap-1.5">
            <i data-lucide="award" class="w-3.5 h-3.5"></i>
            <span>35 % höhere Abschlussquote beim Ersttermin</span>
          </span>
          <span class="px-3 py-1.5 rounded-full bg-slate-100 text-slate-700 font-medium border border-slate-200">
            Einsatz: Herford, Bünde &amp; Enger
          </span>
        </div>

        <!-- ──────────────── MOCKUP CONTAINER 2 ──────────────── -->
        <div>
          <!-- Desktop Mockup -->
          <div id="showcase-2-desktop" class="rounded-2xl overflow-hidden border border-slate-300 shadow-md bg-slate-900">
            <div class="bg-slate-800 px-4 py-2 border-b border-slate-700 flex items-center justify-between text-xs text-slate-400">
              <div class="flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-red-500"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-yellow-500"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-green-500"></span>
              </div>
              <span class="font-mono text-[11px] text-slate-300">https://shk-meister-owl-muster.de</span>
              <span class="text-[10px] text-orange-400 font-mono">Desktop 1920px</span>
            </div>
            <picture>
              <source srcset="assets/projekt-shk.webp" type="image/webp">
              <img src="assets/projekt-shk.jpg" alt="SHK Meisterbetrieb Bad und Heizung Herford Website Vorschau" class="w-full h-64 sm:h-80 md:h-96 object-cover object-center" width="1200" height="600" loading="lazy">
            </picture>
            <div class="p-3 bg-slate-900 border-t border-slate-800 text-xs text-slate-300 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
              <span class="flex items-center gap-2">
                <i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i>
                <span>Geführter Badplaner mit Vorher-/Nachher-Galerie &amp; KfW-Förderungs-Hinweisen</span>
              </span>
              <span class="font-bold text-orange-400 font-mono text-[11px]">Herford &amp; Bünde ✓</span>
            </div>
          </div>

          <!-- Smartphone Mockup (Hidden by default) -->
          <div id="showcase-2-mobile" class="hidden py-4">
            <div class="max-w-sm mx-auto bg-[#0B0F19] rounded-[2.5rem] p-3 border-4 border-slate-700 shadow-2xl relative">
              <!-- Top Notch -->
              <div class="w-28 h-4 bg-slate-800 rounded-b-xl mx-auto mb-2 flex items-center justify-center">
                <div class="w-3 h-3 rounded-full bg-slate-900 border border-slate-700"></div>
              </div>
              <!-- Phone Inner Screen -->
              <div class="bg-slate-900 rounded-[2rem] overflow-hidden text-white border border-slate-800 text-left p-4 space-y-4">
                <div class="flex justify-between items-center text-[10px] text-slate-400 border-b border-slate-800 pb-2">
                  <span>09:41</span>
                  <span>5G ●●● 100%</span>
                </div>
                <!-- Notdienst-Schutzweiche oben -->
                <div class="p-2 bg-rose-500/20 border border-rose-500/40 rounded-xl text-[10px] text-rose-300 flex items-center justify-between gap-1">
                  <span class="font-bold">Heizung kalt oder Rohrbruch?</span>
                  <a href="anfrage.html" class="px-2 py-0.5 bg-rose-600 text-white rounded font-bold whitespace-nowrap">Notdienst</a>
                </div>
                <!-- Hero & Selector -->
                <div class="space-y-2">
                  <h4 class="text-sm font-bold text-white leading-tight">Muster-SHK: Moderne Bäder &amp; Wärmepumpen</h4>
                  <p class="text-[11px] text-slate-300">Wählen Sie Ihr geplantes Projekt in 3 Schritten:</p>
                  
                  <div class="space-y-2 pt-1">
                    <div class="p-2.5 rounded-xl bg-slate-800 border border-slate-700 hover:border-orange-500 text-xs flex items-center justify-between cursor-pointer">
                      <div class="flex items-center gap-2">
                        <i data-lucide="bath" class="w-4 h-4 text-blue-400"></i>
                        <span>Komplettbad-Sanierung</span>
                      </div>
                      <span class="text-[10px] text-emerald-400 font-mono">Inkl. 3D-Planung</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-800 border border-slate-700 hover:border-orange-500 text-xs flex items-center justify-between cursor-pointer">
                      <div class="flex items-center gap-2">
                        <i data-lucide="flame" class="w-4 h-4 text-orange-400"></i>
                        <span>Wärmepumpe / Heizungstausch</span>
                      </div>
                      <span class="text-[10px] text-emerald-400 font-mono">Bis zu 70 % KfW</span>
                    </div>
                  </div>
                </div>
                <!-- Trust strip -->
                <div class="p-2.5 bg-slate-800/80 rounded-xl border border-slate-700 text-[10px] text-slate-300 flex items-center justify-between">
                  <span>Innungsbetrieb · Notdienst für Bestandskunden</span>
                  <span class="text-emerald-400 font-bold">Innungsfachbetrieb</span>
                </div>
                <!-- Sticky Thumb CTA Bar -->
                <div class="pt-2 border-t border-slate-800 flex gap-2">
                  <a href="anfrage.html" class="flex-1 py-2 bg-slate-800 rounded-lg text-[11px] font-bold text-center border border-slate-700 text-slate-200">
                    ☎ Beratung anfragen
                  </a>
                  <a href="anfrage.html" class="flex-1 py-2 bg-[#2563EB] rounded-lg text-[11px] font-bold text-center text-white">
                    Badrechner starten
                  </a>
                </div>
              </div>
            </div>
            <p class="text-center text-xs text-slate-500 mt-2 font-mono">
              📱 Smartphone-Ansicht: Notdienst-Weiche trennt Notfälle von planbaren Bädern &amp; schont Ihr Büro
            </p>
          </div>
        </div>

        <!-- 3 Praxisfelder (Ausgangslage / Module / Mehrwert) -->
        <div class="grid md:grid-cols-3 gap-6 text-xs sm:text-sm text-ink-700 pt-2 border-t border-slate-100">
          <div class="space-y-2">
            <span class="font-bold block text-xs uppercase tracking-wide text-rose-600 flex items-center gap-1.5">
              <i data-lucide="alert-circle" class="w-3.5 h-3.5"></i>
              Typische Ausgangslage im Gewerk:
            </span>
            <p class="leading-relaxed">
              Heizungsnotdienst-Anrufe blockierten tagsüber die Bürokräfte und kamen am Wochenende für banale Kleinigkeiten. Bei Badsanierungen fehlten vor dem ersten Beratungsgespräch grundlegende Raummaße, Baujahr und Budgetvorstellungen der Kunden.
            </p>
          </div>
          <div class="space-y-2">
            <span class="font-bold block text-xs uppercase tracking-wide text-[#2563EB] flex items-center gap-1.5">
              <i data-lucide="cpu" class="w-3.5 h-3.5"></i>
              Integrierte SparrenWeb-Module:
            </span>
            <p class="leading-relaxed">
              Geführter Bad- und Heizungsrechner mit Raumgrößen-Erfassung und KfW-Förderhinweisen. Intelligente Notdienst-Weiche direkt im Kopfbereich mit klarer Vorab-Abgrenzung für Notfälle von Bestandskunden.
            </p>
          </div>
          <div class="space-y-2">
            <span class="font-bold block text-xs uppercase tracking-wide text-emerald-700 flex items-center gap-1.5">
              <i data-lucide="check-check" class="w-3.5 h-3.5"></i>
              Wirkung im Betriebsalltag:
            </span>
            <p class="leading-relaxed">
              Das Büro spart wöchentlich über 6 Stunden unproduktive Telefonzeit. Kunden für Badsanierungen kommen mit realistischen Vorstellungen und fertigen Maßen zum Bemusterungstermin. Die Abschlussquote stieg um 35 %.
            </p>
          </div>
        </div>

      </div>


      <!-- ────────────────────────────────────────────────────────── -->
      <!-- SCHAUKASTEN 3: TISCHLEREI & INNENAUSBAU                    -->
      <!-- ────────────────────────────────────────────────────────── -->
      <div data-aos="fade-up" class="bg-white rounded-3xl p-6 sm:p-10 border border-pastel-sage shadow-md space-y-8">
        
        <!-- Showcase Header -->
        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-b border-pastel-sage/50 pb-6">
          <div class="space-y-1">
            <div class="flex flex-wrap items-center gap-2">
              <span class="text-xs font-mono font-bold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-md border border-emerald-200">
                System-Architektur 03 · Tischlerei, Möbelbau &amp; Objektinnenausbau
              </span>
              <span class="text-xs text-ink-500 font-medium">Muster-System OWL</span>
            </div>
            <h3 class="text-xl sm:text-2xl font-extrabold text-ink-950">
              Edler Holzarten-Katalog, Raumskizzen-Upload &amp; 2.500 € Mindestvolumen-Filter
            </h3>
          </div>

          <!-- View Switcher Tabs (Desktop / Mobile) -->
          <div class="flex items-center gap-2 bg-slate-100 p-1 rounded-xl border border-slate-200 self-start lg:self-auto">
            <button id="btn-showcase-3-desktop" onclick="switchShowcaseView(3, 'desktop')" class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#2563EB] shadow-xs flex items-center gap-1.5">
              <i data-lucide="laptop" class="w-3.5 h-3.5"></i>
              <span>Desktop-Ansicht</span>
            </button>
            <button id="btn-showcase-3-mobile" onclick="switchShowcaseView(3, 'mobile')" class="px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center gap-1.5">
              <i data-lucide="smartphone" class="w-3.5 h-3.5"></i>
              <span>Smartphone-Ansicht</span>
            </button>
          </div>
        </div>

        <!-- Metric Badges Strip -->
        <div class="flex flex-wrap items-center gap-3 text-xs">
          <span class="px-3 py-1.5 rounded-full bg-emerald-50 text-emerald-700 font-bold border border-emerald-200 flex items-center gap-1.5">
            <i data-lucide="check-circle" class="w-3.5 h-3.5"></i>
            <span>80 % Vor-Ort-Abschlussquote beim Aufmaß</span>
          </span>
          <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 font-bold border border-blue-200 flex items-center gap-1.5">
            <i data-lucide="euro" class="w-3.5 h-3.5"></i>
            <span>+4.200 € durchschnittlicher Auftragswert</span>
          </span>
          <span class="px-3 py-1.5 rounded-full bg-slate-100 text-slate-700 font-medium border border-slate-200">
            Einsatz: Detmold, Lage &amp; Lemgo
          </span>
        </div>

        <!-- ──────────────── MOCKUP CONTAINER 3 ──────────────── -->
        <div>
          <!-- Desktop Mockup -->
          <div id="showcase-3-desktop" class="rounded-2xl overflow-hidden border border-slate-300 shadow-md bg-slate-900">
            <div class="bg-slate-800 px-4 py-2 border-b border-slate-700 flex items-center justify-between text-xs text-slate-400">
              <div class="flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-red-500"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-yellow-500"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-green-500"></span>
              </div>
              <span class="font-mono text-[11px] text-slate-300">https://tischlerei-innenausbau-muster.de</span>
              <span class="text-[10px] text-emerald-400 font-mono">Desktop 1920px</span>
            </div>
            <picture>
              <source srcset="assets/projekt-tischlerei-werkstatt.webp" type="image/webp">
              <img src="assets/projekt-tischlerei-werkstatt.jpg" alt="Tischlerei Meisterwerkstatt Detmold Website Vorschau" class="w-full h-64 sm:h-80 md:h-96 object-cover object-center" width="1200" height="600" loading="lazy">
            </picture>
            <div class="p-3 bg-slate-900 border-t border-slate-800 text-xs text-slate-300 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
              <span class="flex items-center gap-2">
                <i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i>
                <span>Edler Holzarten-Katalog, Raumskizzen-Upload &amp; Filter ab 2.500 € Mindestauftragswert</span>
              </span>
              <span class="font-bold text-emerald-400 font-mono text-[11px]">Detmold &amp; Lippe ✓</span>
            </div>
          </div>

          <!-- Smartphone Mockup (Hidden by default) -->
          <div id="showcase-3-mobile" class="hidden py-4">
            <div class="max-w-sm mx-auto bg-[#0B0F19] rounded-[2.5rem] p-3 border-4 border-slate-700 shadow-2xl relative">
              <!-- Top Notch -->
              <div class="w-28 h-4 bg-slate-800 rounded-b-xl mx-auto mb-2 flex items-center justify-center">
                <div class="w-3 h-3 rounded-full bg-slate-900 border border-slate-700"></div>
              </div>
              <!-- Phone Inner Screen -->
              <div class="bg-slate-900 rounded-[2rem] overflow-hidden text-white border border-slate-800 text-left p-4 space-y-4">
                <div class="flex justify-between items-center text-[10px] text-slate-400 border-b border-slate-800 pb-2">
                  <span>09:41</span>
                  <span>5G ●●● 100%</span>
                </div>
                <!-- Mini Header -->
                <div class="flex justify-between items-center">
                  <span class="font-extrabold text-xs text-emerald-400">TISCHLEREI MANUFAKTUR</span>
                  <span class="text-[10px] font-mono text-slate-400">Detmold</span>
                </div>
                <!-- Hero & Qualifizierung -->
                <div class="space-y-2">
                  <h4 class="text-sm font-bold text-white leading-tight">Echte Tischler-Maßarbeit für Ihr Zuhause</h4>
                  <p class="text-[11px] text-slate-300">Individuelle Einbaumöbel, Küchen &amp; Vollholz-Tische ab 2.500 € Projektvolumen.</p>
                  
                  <div class="space-y-2 pt-1">
                    <div class="p-2.5 rounded-xl bg-slate-800 border border-slate-700 hover:border-emerald-500 text-xs flex items-center justify-between cursor-pointer">
                      <div class="flex items-center gap-2">
                        <i data-lucide="layout-grid" class="w-4 h-4 text-emerald-400"></i>
                        <span>Einbauschränke &amp; Schrägen</span>
                      </div>
                      <span class="text-[10px] text-slate-400 font-mono">Nach Maß</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-800 border border-slate-700 hover:border-emerald-500 text-xs flex items-center justify-between cursor-pointer">
                      <div class="flex items-center gap-2">
                        <i data-lucide="upload" class="w-4 h-4 text-blue-400"></i>
                        <span>Raumskizze / Foto hochladen</span>
                      </div>
                      <span class="text-[10px] text-emerald-400 font-mono">Direkt-Upload</span>
                    </div>
                  </div>
                </div>
                <!-- Material Trust -->
                <div class="p-2.5 bg-slate-800/80 rounded-xl border border-slate-700 text-[10px] text-slate-300 space-y-1">
                  <span class="font-bold text-white block">Regionale Hölzer &amp; Handwerkskunst</span>
                  <p class="text-slate-400">Eiche, Nussbaum &amp; Esche aus nachhaltiger Forstwirtschaft in NRW.</p>
                </div>
                <!-- Sticky Thumb CTA Bar -->
                <div class="pt-2 border-t border-slate-800 flex gap-2">
                  <a href="anfrage.html" class="flex-1 py-2 bg-slate-800 rounded-lg text-[11px] font-bold text-center border border-slate-700 text-slate-200">
                    ☎ Werkstatt anrufen
                  </a>
                  <a href="anfrage.html" class="flex-1 py-2 bg-emerald-600 rounded-lg text-[11px] font-bold text-center text-white">
                    Skizze senden
                  </a>
                </div>
              </div>
            </div>
            <p class="text-center text-xs text-slate-500 mt-2 font-mono">
              📱 Smartphone-Ansicht: Transparente Mindestbudgets filtern Preisfüchse automatisch vor dem Aufmaß aus
            </p>
          </div>
        </div>

        <!-- 3 Praxisfelder (Ausgangslage / Module / Mehrwert) -->
        <div class="grid md:grid-cols-3 gap-6 text-xs sm:text-sm text-ink-700 pt-2 border-t border-slate-100">
          <div class="space-y-2">
            <span class="font-bold block text-xs uppercase tracking-wide text-rose-600 flex items-center gap-1.5">
              <i data-lucide="alert-circle" class="w-3.5 h-3.5"></i>
              Typische Ausgangslage im Gewerk:
            </span>
            <p class="leading-relaxed">
              Zu viele Anfragen von reinen Preissuchern, die individuelle Meister-Maßarbeit mit billiger Industrieware aus Möbelhäusern verglichen. Der Tischlermeister verbrachte Feierabende mit unverbindlichen Vor-Ort-Aufmaßen ohne Auftragserfolg.
            </p>
          </div>
          <div class="space-y-2">
            <span class="font-bold block text-xs uppercase tracking-wide text-[#2563EB] flex items-center gap-1.5">
              <i data-lucide="cpu" class="w-3.5 h-3.5"></i>
              Integrierte SparrenWeb-Module:
            </span>
            <p class="leading-relaxed">
              Visueller Holzarten- &amp; Beschläge-Katalog, geführter Raumskizzen-Upload und eine transparente Projekt-Qualifizierung ab 2.500 € Mindestauftragswert direkt auf der Startseite.
            </p>
          </div>
          <div class="space-y-2">
            <span class="font-bold block text-xs uppercase tracking-wide text-emerald-700 flex items-center gap-1.5">
              <i data-lucide="check-check" class="w-3.5 h-3.5"></i>
              Wirkung im Betriebsalltag:
            </span>
            <p class="leading-relaxed">
              Reine Preisvergleicher sortieren sich von selbst aus. Kunden, die anfragen, schätzen echtes Handwerk und bringen bereits Maße oder Grundrisse mit. Die Vor-Ort-Abschlussquote stieg auf 80 %, der durchschnittliche Auftragswert wuchs um 4.200 €.
            </p>
          </div>
        </div>

      </div>

    </section>


    <!-- ══════════════════════════════════════════════════════════════ -->
    <!-- SEKTION 3: DIE ANATOMIE EINER VERKAUFSSTARKEN WEBSITE          -->
    <!-- ══════════════════════════════════════════════════════════════ -->
    <section id="anatomie" class="space-y-12 scroll-mt-24">
      <div class="text-center max-w-3xl mx-auto space-y-3">
        <span class="text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider">Erfolgsfaktoren &amp; Blueprint</span>
        <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-ink-950">
          Die Anatomie einer verkaufsstarken Handwerker-Website
        </h2>
        <p class="text-xs sm:text-sm text-ink-600 max-w-2xl mx-auto leading-relaxed">
          Warum 90 % aller Handwerker-Websites kaum messbare Anfragen bringen – und welche 6 Bausteine den entscheidenden Unterschied zwischen einer toten Visitenkarte und einer echten Auftragsmaschine ausmachen.
        </p>
      </div>

      <!-- 6-Point Anatomy Grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- Baustein 1 -->
        <div data-aos="fade-up" data-aos-delay="50" class="bg-white rounded-3xl p-7 border border-pastel-sage shadow-xs space-y-4 text-left">
          <div class="w-12 h-12 rounded-2xl bg-blue-50 text-[#2563EB] flex items-center justify-center font-bold">
            <i data-lucide="map-pin" class="w-6 h-6"></i>
          </div>
          <span class="text-xs font-mono font-bold text-blue-600 block uppercase">Baustein 01</span>
          <h3 class="text-lg font-bold text-ink-950">Sofortige regionale Einordnung (Above the Fold)</h3>
          <p class="text-xs sm:text-sm text-ink-600 leading-relaxed">
            Der Besucher weiß in den ersten 2 Sekunden ohne zu scrollen: Welches Gewerk, Meisterqualifikation und das genaue Einsatzgebiet in Bielefeld und OWL. Kein Rätselraten, kein Suchen.
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-800 font-medium">
            💡 <strong>Praxisnutzen:</strong> Bauherren fassen sofort Vertrauen; Google belohnt die eindeutige regionale Relevanz mit Spitzenplatzierungen.
          </div>
        </div>

        <!-- Baustein 2 -->
        <div data-aos="fade-up" data-aos-delay="100" class="bg-white rounded-3xl p-7 border border-pastel-sage shadow-xs space-y-4 text-left">
          <div class="w-12 h-12 rounded-2xl bg-blue-50 text-[#2563EB] flex items-center justify-center font-bold">
            <i data-lucide="shield-alert" class="w-6 h-6"></i>
          </div>
          <span class="text-xs font-mono font-bold text-blue-600 block uppercase">Baustein 02</span>
          <h3 class="text-lg font-bold text-ink-950">Intelligente Notdienst- &amp; Kleinauftrags-Weiche</h3>
          <p class="text-xs sm:text-sm text-ink-600 leading-relaxed">
            Schützt Ihr Büro vor unrentablen Anrufen zur Unzeit. Trennt dringende Störungsnotfälle von planbaren Sanierungs- und Neubauprojekten mit lukrativem Deckungsbeitrag.
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-800 font-medium">
            💡 <strong>Praxisnutzen:</strong> Ihr Notdienst-Team wird nur für echte Einsätze alarmiert. Preissucher für 50-Euro-Reparaturen werden automatisch gefiltert.
          </div>
        </div>

        <!-- Baustein 3 -->
        <div data-aos="fade-up" data-aos-delay="150" class="bg-white rounded-3xl p-7 border border-pastel-sage shadow-xs space-y-4 text-left">
          <div class="w-12 h-12 rounded-2xl bg-blue-50 text-[#2563EB] flex items-center justify-center font-bold">
            <i data-lucide="sliders" class="w-6 h-6"></i>
          </div>
          <span class="text-xs font-mono font-bold text-blue-600 block uppercase">Baustein 03</span>
          <h3 class="text-lg font-bold text-ink-950">Geführte Projekt-Vorqualifizierung mit Foto-Upload</h3>
          <p class="text-xs sm:text-sm text-ink-600 leading-relaxed">
            Keine leere „Nachricht schreiben“-Textbox. Der Kunde wählt in 3 einfachen Schritten Leistung, Gebäudeart und lädt direkt vom Smartphone Fotos vom Zählerschrank oder Altheizung hoch.
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-800 font-medium">
            💡 <strong>Praxisnutzen:</strong> Sie wissen vor dem ersten Telefonat, ob der Auftrag passt, und sparen sich unverbindliche Leerfahrten durch OWL.
          </div>
        </div>

        <!-- Baustein 4 -->
        <div data-aos="fade-up" data-aos-delay="200" class="bg-white rounded-3xl p-7 border border-pastel-sage shadow-xs space-y-4 text-left">
          <div class="w-12 h-12 rounded-2xl bg-blue-50 text-[#2563EB] flex items-center justify-center font-bold">
            <i data-lucide="camera" class="w-6 h-6"></i>
          </div>
          <span class="text-xs font-mono font-bold text-blue-600 block uppercase">Baustein 04</span>
          <h3 class="text-lg font-bold text-ink-950">Echte Handwerks-Authentizität statt Katalog-Floskeln</h3>
          <p class="text-xs sm:text-sm text-ink-600 leading-relaxed">
            Keine gekauften Stockfotos von amerikanischen Fotomodellen mit sauberem Plastikhelm. Wir zeigen Ihre echten Projekte, Ihre Werkstatt, Ihre Fahrzeuge und Ihr tatsächliches Team.
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-800 font-medium">
            💡 <strong>Praxisnutzen:</strong> Bauherren vertrauen bodenständigen Meistern aus der Region – und qualifizierte Gesellen sehen sofort ein echtes Kollegenteam.
          </div>
        </div>

        <!-- Baustein 5 -->
        <div data-aos="fade-up" data-aos-delay="250" class="bg-white rounded-3xl p-7 border border-pastel-sage shadow-xs space-y-4 text-left">
          <div class="w-12 h-12 rounded-2xl bg-blue-50 text-[#2563EB] flex items-center justify-center font-bold">
            <i data-lucide="smartphone" class="w-6 h-6"></i>
          </div>
          <span class="text-xs font-mono font-bold text-blue-600 block uppercase">Baustein 05</span>
          <h3 class="text-lg font-bold text-ink-950">Ergonomische Smartphone-Bedienung (Daumenzone)</h3>
          <p class="text-xs sm:text-sm text-ink-600 leading-relaxed">
            Über 78 % der Kunden und über 90 % der Gesellen surfen mobil. Unsere Interfaces bieten ergonomische Touch-Targets in der Daumenzone, 1-Klick-Anrufe und kein fummeliges Zoomen.
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-800 font-medium">
            💡 <strong>Praxisnutzen:</strong> Der Kunde erreicht Sie mit einem Fingertipp direkt von der Baustelle oder vom Sofa – ohne Frust und ohne Hürden.
          </div>
        </div>

        <!-- Baustein 6 -->
        <div data-aos="fade-up" data-aos-delay="300" class="bg-white rounded-3xl p-7 border border-pastel-sage shadow-xs space-y-4 text-left">
          <div class="w-12 h-12 rounded-2xl bg-blue-50 text-[#2563EB] flex items-center justify-center font-bold">
            <i data-lucide="zap" class="w-6 h-6"></i>
          </div>
          <span class="text-xs font-mono font-bold text-blue-600 block uppercase">Baustein 06</span>
          <h3 class="text-lg font-bold text-ink-950">Ladezeit unter 1,0 Sekunde (Ohne Plugin-Ballast)</h3>
          <p class="text-xs sm:text-sm text-ink-600 leading-relaxed">
            Handgeschriebener, statisch optimierter Code ohne 30 überladene WordPress-Plugins, SQL-Datenbanken oder fremde Tracking-Fallen. Öffnet blitzschnell auch im schwachen LTE-Netz.
          </p>
          <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-800 font-medium">
            💡 <strong>Praxisnutzen:</strong> Google PageSpeed 98–100/100. Besucher springen nicht genervt ab und Sie sparen teure Server-Wartungskosten.
          </div>
        </div>

      </div>
    </section>


    <!-- ══════════════════════════════════════════════════════════════ -->
    <!-- SEKTION 4: WARUM EIN KOSTENLOSER VORAB-ENTWURF BESSER IST     -->
    <!-- ══════════════════════════════════════════════════════════════ -->
    <section id="vorab-entwurf" class="space-y-10 scroll-mt-24">
      <div class="bg-gradient-to-br from-slate-900 to-[#0F172A] rounded-3xl p-8 sm:p-12 text-white border border-slate-800 shadow-2xl space-y-10">
        
        <div class="text-center max-w-3xl mx-auto space-y-4">
          <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 text-xs font-mono font-bold border border-emerald-500/30">
            <i data-lucide="shield-check" class="w-3.5 h-3.5"></i>
            <span>100 % Risikofrei · Die SparrenWeb Vorleistung</span>
          </span>
          <h2 class="text-2xl sm:text-4xl font-extrabold tracking-tight text-white leading-tight">
            Sie kaufen bei uns keine Katze im Sack: Sehen Sie vorab kostenlos, wie die neue Website für IHREN Betrieb aussieht.
          </h2>
          <p class="text-xs sm:text-base text-slate-300 max-w-2xl mx-auto leading-relaxed">
            Fallstudien anderer Betriebe sind gut. Aber zu sehen, wie Ihr eigener Meisterbetrieb mit modernem Design, Ihren echten Leistungen und Vorab-Filtern wirkt, überzeugt sofort. Deshalb gestalten wir Ihren individuellen Entwurf unverbindlich vorab.
          </p>
        </div>

        <!-- 3 Simple Risk-Reversal Steps -->
        <div class="grid md:grid-cols-3 gap-6 text-left">
          
          <!-- Step 1 -->
          <div class="p-6 bg-slate-800/80 rounded-2xl border border-slate-700/80 space-y-3 relative">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-blue-600 text-white font-bold text-xs flex items-center justify-center">1</span>
              <span class="text-[11px] font-mono text-blue-400 font-bold">15 Minuten</span>
            </div>
            <h3 class="text-base font-bold text-white">Kurzes 15-Minuten-Erstgespräch</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Kein Verkaufsdruck. Wir klären telefonisch: Welche Aufträge wollen Sie forcieren (z. B. Wärmepumpen statt Notdienst)? Welche Gesellen fehlen Ihnen? In welchem Umkreis in OWL sind Sie unterwegs?
            </p>
            <div class="pt-2 text-[11px] text-emerald-400 font-mono flex items-center gap-1">
              <i data-lucide="check" class="w-3.5 h-3.5"></i>
              <span>Unverbindlich &amp; auf Augenhöhe</span>
            </div>
          </div>

          <!-- Step 2 -->
          <div class="p-6 bg-slate-800/80 rounded-2xl border border-blue-500/40 space-y-3 relative ring-2 ring-blue-500/20">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-blue-600 text-white font-bold text-xs flex items-center justify-center">2</span>
              <span class="text-[11px] font-mono text-emerald-400 font-bold">0 € Kosten</span>
            </div>
            <h3 class="text-base font-bold text-white">Wir gestalten Ihren individuellen Entwurf</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Innerhalb von 48 Stunden erstellen wir Ihnen einen klickbaren, maßgeschneiderten Website-Entwurf mit Ihrem Logo, Ihren Farben und handwerkergerechten Texten für Ihr Gewerk.
            </p>
            <div class="pt-2 text-[11px] text-emerald-400 font-mono flex items-center gap-1">
              <i data-lucide="check" class="w-3.5 h-3.5"></i>
              <span>Echte Website-Vorschau zum Ausprobieren</span>
            </div>
          </div>

          <!-- Step 3 -->
          <div class="p-6 bg-slate-800/80 rounded-2xl border border-slate-700/80 space-y-3 relative">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-full bg-blue-600 text-white font-bold text-xs flex items-center justify-center">3</span>
              <span class="text-[11px] font-mono text-blue-400 font-bold">Volle Kontrolle</span>
            </div>
            <h3 class="text-base font-bold text-white">Sie entscheiden in aller Ruhe</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Erst wenn Sie zu 100 % überzeugt sind, starten wir die Umsetzung zum garantierten Festpreis ab 1.500 € netto (Pilot) bzw. 2.800 € netto (Meister-System). Gefällt Ihnen der Entwurf nicht? Dann zahlen Sie genau 0 Euro. Ohne Wenn und Aber.
            </p>
            <div class="pt-2 text-[11px] text-emerald-400 font-mono flex items-center gap-1">
              <i data-lucide="check" class="w-3.5 h-3.5"></i>
              <span>Kein Abo · Kein Risiko für Sie</span>
            </div>
          </div>

        </div>

        <!-- Trust Callout -->
        <div class="p-4 bg-slate-800/50 rounded-2xl border border-slate-700 text-xs text-slate-300 text-center max-w-2xl mx-auto flex flex-col sm:flex-row items-center justify-center gap-3">
          <span class="font-bold text-white flex items-center gap-1.5">
            <i data-lucide="lock" class="w-4 h-4 text-emerald-400"></i>
            Handwerks-Ehrenwort:
          </span>
          <span>Keine Vorauskasse, keine versteckten Folgekosten und kein monatliches Agentur-Abo.</span>
        </div>

      </div>
    </section>


    <!-- ══════════════════════════════════════════════════════════════ -->
    <!-- SEKTION 5: ABSCHLUSS-CTA                                       -->
    <!-- ══════════════════════════════════════════════════════════════ -->
    <section data-aos="card-3d-reveal" class="bg-white rounded-3xl p-8 sm:p-12 border-2 border-[#2563EB]/20 shadow-xl text-center space-y-6 max-w-4xl mx-auto">
      
      <div class="space-y-3">
        <span class="text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider">Starten Sie jetzt</span>
        <h2 class="text-2xl sm:text-4xl font-extrabold text-ink-950">
          Bereit für ein Meister-System, das Ihren Betrieb spürbar entlastet?
        </h2>
        <p class="text-sm sm:text-base text-ink-600 max-w-2xl mx-auto leading-relaxed">
          Sichern Sie sich jetzt Ihren kostenlosen, unverbindlichen Vorab-Entwurf für Ihren Handwerksbetrieb in Bielefeld und OWL. Wir prüfen Ihre bestehende Präsenz und zeigen Ihnen, was möglich ist.
        </p>
      </div>

      <div class="flex flex-col sm:flex-row justify-center items-center gap-3 pt-2">
        <a href="anfrage.html" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-[#2563EB] hover:bg-blue-700 text-white font-semibold text-sm px-7 py-4 rounded-full transition-all shadow-md shadow-blue-600/25">
          <span>Kostenlosen Vorab-Entwurf anfordern</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
        <a href="anfrage.html" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-slate-100 hover:bg-slate-200 text-slate-800 font-semibold text-sm px-6 py-4 rounded-full transition-all border border-slate-200">
          <i data-lucide="phone" class="w-4 h-4 text-[#2563EB]"></i>
          <span>Projekt anfragen</span>
        </a>
      </div>

      <div class="flex flex-wrap items-center justify-center gap-4 text-xs text-ink-500 font-medium pt-3 border-t border-slate-100">
        <span class="flex items-center gap-1.5">
          <i data-lucide="check" class="w-3.5 h-3.5 text-emerald-600"></i>
          Festpreis ab 1.500 € (Pilot) / 2.800 € (Meister-System)
        </span>
        <span>•</span>
        <span class="flex items-center gap-1.5">
          <i data-lucide="check" class="w-3.5 h-3.5 text-emerald-600"></i>
          0 € monatliches Agenturabo
        </span>
        <span>•</span>
        <span class="flex items-center gap-1.5">
          <i data-lucide="check" class="w-3.5 h-3.5 text-emerald-600"></i>
          Schlüsselfertig in 7 Werktagen
        </span>
      </div>

    </section>

  </main>

  <script>
    // ══════════════════════════════════════════════════════════════
    // BEFORE / AFTER SLIDER DRAG LOGIC (MOUSE & TOUCH)
    // ══════════════════════════════════════════════════════════════
    (function initDiffSlider() {
      const container = document.getElementById('diff-container');
      const beforePanel = document.getElementById('diff-before');
      const handle = document.getElementById('diff-handle');
      if (!container || !beforePanel || !handle) return;

      let isDragging = false;

      function updatePosition(clientX) {
        const rect = container.getBoundingClientRect();
        let pos = (clientX - rect.left) / rect.width;
        if (pos < 0.05) pos = 0.05;
        if (pos > 0.95) pos = 0.95;
        const percentage = (pos * 100).toFixed(2);
        beforePanel.style.width = percentage + '%';
        handle.style.left = percentage + '%';
      }

      container.addEventListener('mousedown', (e) => {
        isDragging = true;
        updatePosition(e.clientX);
      });

      window.addEventListener('mouseup', () => { isDragging = false; });
      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        updatePosition(e.clientX);
      });

      // Touch events for smartphone & tablet
      container.addEventListener('touchstart', (e) => {
        isDragging = true;
        updatePosition(e.touches[0].clientX);
      }, { passive: true });

      window.addEventListener('touchend', () => { isDragging = false; });
      window.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        updatePosition(e.touches[0].clientX);
      }, { passive: true });
    })();

    // ══════════════════════════════════════════════════════════════
    // SHOWCASE DESKTOP / SMARTPHONE VIEW SWITCHER
    // ══════════════════════════════════════════════════════════════
    function switchShowcaseView(showcaseId, viewType) {
      const desktopView = document.getElementById(`showcase-${showcaseId}-desktop`);
      const mobileView = document.getElementById(`showcase-${showcaseId}-mobile`);
      const btnDesktop = document.getElementById(`btn-showcase-${showcaseId}-desktop`);
      const btnMobile = document.getElementById(`btn-showcase-${showcaseId}-mobile`);

      if (!desktopView || !mobileView || !btnDesktop || !btnMobile) return;

      if (viewType === 'mobile') {
        desktopView.classList.add('hidden');
        mobileView.classList.remove('hidden');

        // Button styles
        btnMobile.className = 'px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#2563EB] shadow-xs flex items-center gap-1.5';
        btnDesktop.className = 'px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center gap-1.5';
      } else {
        mobileView.classList.add('hidden');
        desktopView.classList.remove('hidden');

        // Button styles
        btnDesktop.className = 'px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#2563EB] shadow-xs flex items-center gap-1.5';
        btnMobile.className = 'px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center gap-1.5';
      }

      // Re-trigger lucide icons inside newly revealed elements if needed
      if (typeof lucide !== 'undefined' && lucide.createIcons) {
        lucide.createIcons();
      }
    }
  </script>
"""

with open('referenzen.html', 'w', encoding='utf-8') as f:
    f.write(head + navbar + body_content + footer)

print("Generated referenzen.html successfully.")
