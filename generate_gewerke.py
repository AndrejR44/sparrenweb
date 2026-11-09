import builder_helper

title = "Lösungen nach Gewerk | SparrenWeb – Websites für Handwerksbetriebe"
description = "Keine Standard-Schablone: Schlüsselfertige Websites exakt zugeschnitten auf Dachdecker, SHK, Elektrotechnik, Tischler und weitere Gewerke in Bielefeld & OWL."
canonical = "gewerke.html"

head = builder_helper.get_head(title, description, canonical)
navbar = builder_helper.get_navbar("gewerke.html")
footer = builder_helper.get_footer()

body_content = """
  <style>
    @keyframes fadeInSlideUp {
      0% {
        opacity: 0;
        transform: translateY(10px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }
    @keyframes pulseGlow {
      0%, 100% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.2); }
      50% { box-shadow: 0 0 0 6px rgba(37, 99, 235, 0); }
    }
    .trade-pane {
      transition: opacity 0.25s ease-out;
    }
    .table-trade-row {
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .table-trade-row:hover {
      background-color: rgba(248, 250, 252, 0.95);
      transform: translateY(-1px);
    }
    .table-trade-btn {
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .rank-badge-glow:hover {
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.3);
    }
  </style>

  <!-- Hero Section -->
  <header class="pt-32 sm:pt-40 pb-16 sm:pb-24 px-4 sm:px-6 relative overflow-hidden hero-bg">
    <div class="absolute inset-0 dot-pattern pointer-events-none opacity-40"></div>
    <div class="max-w-5xl mx-auto text-center space-y-6 relative z-10">
      
      <h1 data-aos="fade-up" data-aos-duration="700" class="text-3xl sm:text-5xl lg:text-6xl font-extrabold text-ink-950 tracking-tight leading-[1.12] max-w-4xl mx-auto">
        Keine Standard-Schablone: Eine Website, die exakt auf Ihr Gewerk zugeschnitten ist.
      </h1>

      <p data-aos="fade-up" data-aos-delay="100" data-aos-duration="700" class="text-sm sm:text-lg text-ink-600 max-w-2xl mx-auto leading-relaxed">
        Ein Dachdecker braucht andere Anfrage-Formulare als ein Heizungsbauer oder Möbelschreiner. Sehen Sie, wie wir die typischen Herausforderungen Ihres Gewerks mit praxisnahen Modulen und echter Meister-Tonalität lösen.
      </p>

      <!-- Interactive Gewerke Tab Switcher Bar -->
      <div data-aos="fade-up" data-aos-delay="200" class="pt-4 flex justify-center">
        <div class="p-1.5 bg-slate-100/90 border border-slate-200/80 rounded-full inline-flex flex-wrap justify-center gap-1.5 shadow-xs backdrop-blur-md">
          <button type="button" onclick="switchTrade('dach')" id="tab-dach" class="trade-tab-btn active px-4 sm:px-6 py-2.5 rounded-full text-xs sm:text-sm font-bold transition-all shadow-sm flex items-center gap-2 bg-[#2563EB] text-white">
            <i data-lucide="hammer" class="w-4 h-4"></i>
            <span>Dach &amp; Zimmerei</span>
          </button>
          <button type="button" onclick="switchTrade('shk')" id="tab-shk" class="trade-tab-btn px-4 sm:px-6 py-2.5 rounded-full text-xs sm:text-sm font-semibold transition-all flex items-center gap-2 bg-transparent text-slate-700 hover:text-ink-950 hover:bg-white/80">
            <i data-lucide="flame" class="w-4 h-4 text-orange-500"></i>
            <span>SHK, Heizung &amp; Bad</span>
          </button>
          <button type="button" onclick="switchTrade('elektro')" id="tab-elektro" class="trade-tab-btn px-4 sm:px-6 py-2.5 rounded-full text-xs sm:text-sm font-semibold transition-all flex items-center gap-2 bg-transparent text-slate-700 hover:text-ink-950 hover:bg-white/80">
            <i data-lucide="zap" class="w-4 h-4 text-amber-500"></i>
            <span>Elektro &amp; Photovoltaik</span>
          </button>
          <button type="button" onclick="switchTrade('tischler')" id="tab-tischler" class="trade-tab-btn px-4 sm:px-6 py-2.5 rounded-full text-xs sm:text-sm font-semibold transition-all flex items-center gap-2 bg-transparent text-slate-700 hover:text-ink-950 hover:bg-white/80">
            <i data-lucide="ruler" class="w-4 h-4 text-emerald-500"></i>
            <span>Tischlerei &amp; Ausbau</span>
          </button>
        </div>
      </div>

    </div>
  </header>

  <!-- Main Container -->
  <main class="py-12 px-4 sm:px-6 max-w-6xl mx-auto space-y-24">

    <!-- ══════════════════════════════════════════════ -->
    <!-- 1. DIE 4 KERN-GEWERKE TABS MIT LIVE-MOCKUP     -->
    <!-- ══════════════════════════════════════════════ -->
    <div class="space-y-12">

      <!-- TAB 1: DACH & ZIMMEREI -->
      <section id="pane-dach" class="trade-pane space-y-12">
        <div class="grid lg:grid-cols-12 gap-8 items-center">
          
          <!-- Text & Structure -->
          <div data-aos="fade-right" class="lg:col-span-6 space-y-6 text-left">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-amber-50 text-amber-800 border border-amber-200">
              <i data-lucide="shield-check" class="w-3.5 h-3.5 text-amber-600"></i>
              <span>Dachdecker &amp; Zimmereibetriebe</span>
            </div>

            <h2 class="text-2xl sm:text-4xl font-extrabold text-ink-950 leading-tight">
              Hochwertige Dachsanierungen statt unbezahlter Kleinstreparaturen.
            </h2>

            <!-- Authentic Project Photography Card -->
            <div class="rounded-2xl overflow-hidden border border-slate-200 shadow-xs">
              <picture>
                <source srcset="assets/projekt-dach.webp" type="image/webp">
                <img src="assets/projekt-dach.jpg" alt="Energetische Dachsanierung Meisterbetrieb Bielefeld" class="w-full h-44 object-cover" width="600" height="176" loading="lazy">
              </picture>
              <div class="p-3 bg-slate-50 border-t border-slate-200 text-xs text-ink-700 flex justify-between items-center">
                <span>Echtes Meisterprojekt: Steildachsanierung &amp; Aufstockung in Bielefeld-Senne</span>
                <span class="font-bold text-[#2563EB] font-mono text-[11px]">KfW-gefördert <i data-lucide="check" class="w-3 h-3 text-blue-600 inline"></i></span>
              </div>
            </div>

            <p class="text-sm sm:text-base text-ink-600 leading-relaxed">
              Wenn nach dem Sturm das Telefon im Minutentakt klingelt, geht die Büroarbeit unter. Auf der anderen Seite wollen Sie planbare Großaufträge wie energetische Dachsanierungen und Aufstockungen gewinnen.
            </p>

            <div class="space-y-4 pt-2">
              <div class="p-4 rounded-2xl bg-white border border-pastel-sage shadow-xs space-y-2">
                <div class="flex items-center gap-2 text-xs font-bold text-red-600 uppercase tracking-wide">
                  <i data-lucide="alert-circle" class="w-4 h-4"></i>
                  <span>1. Das typische Problem im Alltag</span>
                </div>
                <p class="text-xs sm:text-sm text-ink-700">
                  Stundenlange Telefonate für drei verrutschte Dachziegel. Kunden erwarten sofortige Vor-Ort-Besichtigung, ohne dass klar ist, ob sich der Einsatz für Ihren Meisterbetrieb überhaupt lohnt.
                </p>
              </div>

              <div class="p-4 rounded-2xl bg-blue-50/60 border border-blue-200/60 shadow-xs space-y-2">
                <div class="flex items-center gap-2 text-xs font-bold text-[#2563EB] uppercase tracking-wide">
                  <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                  <span>2. Wie unsere Website-Struktur das löst</span>
                </div>
                <p class="text-xs sm:text-sm text-ink-800">
                  Ein <strong>digitaler Sturmschaden- &amp; Sanierungs-Filter</strong> fragt Dachart, ungefähre Quadratmeter und Schadensfotos vorab ab. Notfälle werden priorisiert, lukrative Dachsanierungen sofort kalkulierbar gemacht.
                </p>
              </div>
            </div>

            <div class="pt-2 flex flex-wrap gap-3">
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="camera" class="w-3.5 h-3.5 text-blue-600"></i> Drohnen-Referenzgalerie
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="hard-hat" class="w-3.5 h-3.5 text-blue-600"></i> Gesellen-Bewerbung in 60s
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="file-check" class="w-3.5 h-3.5 text-blue-600"></i> KfW-Förderungshinweis
              </span>
            </div>
          </div>

          <!-- Interactive UI Mockup (Dach) -->
          <div data-aos="flip-tilt-left" class="lg:col-span-6">
            <div class="bg-[#0F172A] rounded-3xl p-5 sm:p-6 border border-slate-800 shadow-2xl text-white space-y-4">
              
              <!-- Mockup Browser Bar -->
              <div class="flex items-center justify-between border-b border-slate-800/80 pb-3 text-xs font-mono select-none">
                <div class="flex items-center gap-1.5 sm:gap-2">
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#EF4444]/90 inline-block shadow-xs"></span>
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#F59E0B]/90 inline-block shadow-xs"></span>
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#10B981]/90 inline-block shadow-xs"></span>
                </div>
                <div class="bg-slate-800/90 px-3 sm:px-4 py-1 rounded-full border border-slate-700/70 text-slate-300 text-[10px] sm:text-[11px] font-medium shadow-inner flex items-center gap-1.5">
                  <i data-lucide="lock" class="w-3 h-3 text-emerald-400"></i>
                  <span class="text-white font-medium">westermann-bedachungen-owl.de</span>
                  <span class="hidden sm:inline-block text-[9px] bg-blue-500/20 text-blue-300 px-1.5 py-0.5 rounded font-mono font-bold ml-1">ONLINE</span>
                </div>
                <div class="inline-flex items-center gap-1.5 text-[10px] text-emerald-400 font-bold uppercase tracking-wider">
                  <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                  <span>Vorab-Filter</span>
                </div>
              </div>

              <!-- Converting Funnel Canvas (Matching Startseite #demo) -->
              <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-lg text-slate-900 transition-all">
                
                <!-- Funnel Progress Header -->
                <div class="border-b border-slate-100 pb-2.5">
                  <div class="flex items-center justify-between text-xs sm:text-sm font-bold text-slate-800">
                    <span id="mock-dach-step-label">Schritt 1 von 3: Vorhaben</span>
                    <div class="flex items-center gap-2">
                      <span class="text-emerald-700 font-bold text-xs flex items-center gap-1">
                        <i data-lucide="shield-check" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span>100% unverbindlich</span>
                      </span>
                      <span id="mock-dach-pct-label" class="bg-blue-50 text-[#2563EB] border border-blue-100 font-bold px-2.5 py-0.5 rounded-full text-xs font-mono">33%</span>
                    </div>
                  </div>
                  <!-- Progress Bar -->
                  <div class="w-full bg-slate-100 h-1.5 rounded-full overflow-hidden mt-2.5">
                    <div id="mock-dach-progress" class="sim-progress-bar h-full bg-[#2563EB] rounded-full" style="width: 33%;"></div>
                  </div>
                </div>

                <!-- STEP 1: DACH -->
                <div id="mock-dach-s1" class="space-y-3 pt-3 text-left">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">1. Worum geht es bei Ihrem Dachprojekt?</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Wählen Sie Ihr Anliegen für eine schnelle Meister-Einschätzung:</p>
                  </div>

                  <div class="space-y-2">
                    <button type="button" onclick="advanceMockup('dach', 2, 'Dachsanierung (Steildach)')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Dachsanierung (Steildach)</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Energetische Dämmung, Neueindeckung &amp; KfW-Zuschussprüfung in OWL.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-blue-50 text-[#2563EB] flex items-center justify-center shrink-0">
                        <i data-lucide="home" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('dach', 2, 'Sturmschaden & Akute Undichtigkeit')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Sturmschaden &amp; Akute Undichtigkeit</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Dringender Notfall: Schnelle Sicherung &amp; Schadensbehebung vor Ort.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-amber-50 text-amber-600 flex items-center justify-center shrink-0">
                        <i data-lucide="cloud-lightning" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('dach', 2, 'Dachfenster & Gaubenausbau')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Dachfenster &amp; Gaubenausbau</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Velux- / Roto-Austausch, moderne Beschattung &amp; lichte Räume.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-yellow-50 text-yellow-600 flex items-center justify-center shrink-0">
                        <i data-lucide="sun" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('dach', 2, 'Flachdach & Abdichtung')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Flachdach &amp; Abdichtung</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Bitumen-, EPDM-Bahnen, Garagen- oder Gewerbe-Flachdächer.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                        <i data-lucide="layers" class="w-4 h-4"></i>
                      </div>
                    </button>
                  </div>

                  <div class="pt-1.5 text-center text-[11px] text-slate-400 font-mono flex items-center justify-center gap-1.5">
                    <i data-lucide="mouse-pointer-click" class="w-3.5 h-3.5 text-[#2563EB]"></i>
                    <span>Tipp: Klicken Sie auf eine Kachel zum Ausprobieren</span>
                  </div>
                </div>

                <!-- STEP 2: DACH -->
                <div id="mock-dach-s2" class="space-y-3 pt-3 text-left hidden">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">2. Eckdaten &amp; optionales Foto</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Ein schnelles Handyfoto spart oft einen aufwendigen Vor-Ort-Besuch.</p>
                  </div>

                  <div class="p-2.5 rounded-xl bg-blue-50/80 border border-blue-200/80 text-xs text-blue-900 flex items-center justify-between">
                    <span class="text-slate-600">Ausgewählt:</span>
                    <strong id="mock-dach-selected-title" class="font-bold text-[#2563EB]">Dachsanierung (Steildach)</strong>
                  </div>

                  <!-- Simulated Photo Upload Area -->
                  <div class="border-2 border-dashed border-slate-200 hover:border-[#2563EB] rounded-xl p-3 text-center space-y-1.5 bg-slate-50/60 transition-all">
                    <div class="w-8 h-8 rounded-full bg-blue-50 text-[#2563EB] flex items-center justify-center mx-auto">
                      <i data-lucide="camera" class="w-4 h-4"></i>
                    </div>
                    <div>
                      <div class="text-xs font-bold text-slate-900">Foto oder Skizze anhängen (optional)</div>
                      <div class="text-[10px] text-slate-500">Smartphone-Foto vom Dach, Ziegeln oder Schadensstelle</div>
                    </div>
                    <div class="p-2 bg-white rounded-lg border border-slate-200 flex items-center justify-between text-xs max-w-xs mx-auto shadow-2xs">
                      <div class="flex items-center gap-2">
                        <i data-lucide="image" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span class="font-semibold text-slate-800 text-[11px]">dach-suedseite.jpg (3.2 MB)</span>
                      </div>
                      <span class="text-[10px] font-mono text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded font-bold">Upload bereit</span>
                    </div>
                  </div>

                  <div class="space-y-1.5 text-xs">
                    <div class="p-2 bg-slate-50 rounded-lg border border-slate-200/80 flex justify-between items-center">
                      <span class="text-slate-500 font-mono text-[11px]">Fläche &amp; Baujahr:</span>
                      <span class="font-bold text-slate-900">Satteldach ~160 m² (Bj. 1984)</span>
                    </div>
                    <div class="p-2 bg-slate-50 rounded-lg border border-slate-200/80 flex justify-between items-center">
                      <span class="text-slate-500 font-mono text-[11px]">Wunschtermin:</span>
                      <span class="font-bold text-emerald-700">In 1–3 Monaten geplant</span>
                    </div>
                  </div>

                  <!-- Navigation -->
                  <div class="pt-2 border-t border-slate-100 flex items-center justify-between">
                    <button type="button" onclick="advanceMockup('dach', 1)" class="inline-flex items-center gap-1 text-xs font-semibold text-slate-500 hover:text-slate-900 transition-colors cursor-pointer">
                      <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i>
                      <span>Zurück</span>
                    </button>
                    <button type="button" onclick="advanceMockup('dach', 3)" class="inline-flex items-center justify-center gap-2 bg-[#2563EB] hover:bg-blue-700 text-white font-bold px-4 py-2 rounded-lg text-xs transition-all shadow-sm hover:shadow-md hover:-translate-y-0.5 cursor-pointer">
                      <span>Weiter zu Schritt 3 (Meister-Übergabe) →</span>
                    </button>
                  </div>
                </div>

                <!-- STEP 3: DACH -->
                <div id="mock-dach-s3" class="space-y-3 pt-3 text-left hidden">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">3. So strukturiert landet die Anfrage beim Meister:</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Alle Maße, Fotos &amp; Kontaktdaten liegen sofort vor dem Erstkontakt vor.</p>
                  </div>

                  <!-- Live Ticket Preview -->
                  <div class="bg-white rounded-xl border border-emerald-500/30 p-3.5 shadow-sm space-y-2.5 relative overflow-hidden">
                    <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-emerald-500 to-[#2563EB]"></div>
                    
                    <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                      <span class="inline-flex items-center gap-1 bg-emerald-50 text-emerald-700 text-[10px] font-bold px-2 py-0.5 rounded-full border border-emerald-200">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                        Qualifizierte Kundenanfrage
                      </span>
                      <span class="text-[10px] text-slate-400 font-mono font-bold">Ticket: #DACH-4819</span>
                    </div>

                    <div class="grid grid-cols-2 gap-2 text-xs">
                      <div class="p-2.5 bg-slate-50 rounded-lg space-y-0.5">
                        <div class="text-[9px] font-mono uppercase text-slate-400 font-bold">Bauherr &amp; Ort</div>
                        <div class="font-extrabold text-slate-900 text-xs">Familie Brinkmann</div>
                        <div class="text-slate-600 font-mono text-[11px]"><i data-lucide="map-pin" class="w-3 h-3 text-slate-500 inline mr-1"></i>Bielefeld-Senne</div>
                      </div>
                      <div class="p-2.5 bg-slate-50 rounded-lg space-y-0.5">
                        <div class="text-[9px] font-mono uppercase text-slate-400 font-bold">Vorhaben</div>
                        <div class="font-bold text-[#2563EB] text-xs">Steildachsanierung</div>
                        <div class="text-slate-600 text-[11px]">160 m² · Start in 1–3 Mon.</div>
                      </div>
                    </div>

                    <div class="p-2 bg-slate-50 rounded-lg flex items-center justify-between text-xs">
                      <div class="flex items-center gap-2">
                        <i data-lucide="image" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span class="text-[11px] font-semibold text-slate-800">2 Fotos angehängt (Dach &amp; Giebel)</span>
                      </div>
                      <span class="text-[10px] font-mono font-bold text-blue-600 bg-white px-2 py-0.5 rounded border border-slate-200 shadow-2xs">Foto ansehen</span>
                    </div>

                    <div class="p-2.5 rounded-lg bg-emerald-50/70 border border-emerald-200 text-xs text-emerald-900 leading-snug flex items-start gap-2">
                      <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
                      <div class="text-[11px]">
                        <strong>Ihr Zeitvorteil:</strong> Angebot in 15 Min. kalkulierbar statt 3 Ortstermine zur Bestandsaufnahme.
                      </div>
                    </div>
                  </div>

                  <!-- Footer actions -->
                  <div class="pt-2 border-t border-slate-100 flex items-center justify-between gap-2">
                    <button type="button" onclick="resetMockup('dach')" class="inline-flex items-center gap-1 text-xs font-bold text-slate-600 hover:text-slate-900 px-3 py-2 rounded-lg border border-slate-200 hover:bg-slate-50 transition-all cursor-pointer">
                      <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i>
                      <span>Demo neu starten</span>
                    </button>
                    <a href="anfrage.html" class="inline-flex items-center gap-1.5 bg-[#2563EB] hover:bg-blue-700 text-white font-bold text-xs px-3.5 py-2 rounded-lg transition-all shadow-xs hover:-translate-y-0.5">
                      <span>Vorab-Entwurf anfordern</span>
                      <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                    </a>
                  </div>
                </div>

              </div>

              <!-- Mockup Footer Stats -->
              <div class="flex justify-between items-center text-xs text-slate-400 pt-1">
                <span>Ergebnis für den Meisterbetrieb:</span>
                <span class="text-white font-bold">Angebot in 15 Min. statt nach 3 Ortsterminen</span>
              </div>

            </div>
          </div>
        </div>
      </section>

      <!-- TAB 2: SHK, HEIZUNG & BAD -->
      <section id="pane-shk" class="trade-pane hidden space-y-12">
        <div class="grid lg:grid-cols-12 gap-8 items-center">
          
          <div data-aos="fade-right" class="lg:col-span-6 space-y-6 text-left">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-orange-50 text-orange-800 border border-orange-200">
              <i data-lucide="flame" class="w-3.5 h-3.5 text-orange-600"></i>
              <span>Sanitär, Heizung &amp; Klimatechnik</span>
            </div>

            <h2 class="text-2xl sm:text-4xl font-extrabold text-ink-950 leading-tight">
              Wärmepumpen &amp; Traumbäder planbar anfragen – Notdienst klar filtern.
            </h2>

            <!-- Authentic Project Photography Card -->
            <div class="rounded-2xl overflow-hidden border border-slate-200 shadow-xs">
              <picture>
                <source srcset="assets/projekt-shk.webp" type="image/webp">
                <img src="assets/projekt-shk.jpg" alt="Wärmepumpen- und Badsanierung Herford" class="w-full h-44 object-cover" width="600" height="176" loading="lazy">
              </picture>
              <div class="p-3 bg-slate-50 border-t border-slate-200 text-xs text-ink-700 flex justify-between items-center">
                <span>Echtes Meisterprojekt: Wärmepumpenanlage &amp; barrierefreies Bad in Herford</span>
                <span class="font-bold text-orange-600 font-mono text-[11px]">70 % Förderung <i data-lucide="check" class="w-3 h-3 text-orange-600 inline"></i></span>
              </div>
            </div>

            <p class="text-sm sm:text-base text-ink-600 leading-relaxed">
              Als SHK-Betrieb in Ostwestfalen möchten Sie lukrative Heizungstausche und Badsanierungen abschließen, anstatt nachts wegen tropfender Wasserhähne von Mietern geweckt zu werden.
            </p>

            <div class="space-y-4 pt-2">
              <div class="p-4 rounded-2xl bg-white border border-pastel-sage shadow-xs space-y-2">
                <div class="flex items-center gap-2 text-xs font-bold text-red-600 uppercase tracking-wide">
                  <i data-lucide="alert-circle" class="w-4 h-4"></i>
                  <span>1. Das typische Problem im Alltag</span>
                </div>
                <p class="text-xs sm:text-sm text-ink-700">
                  Endlose Beratungsgespräche am Telefon über Wärmepumpen-Preise, ohne Baujahr des Hauses, bisherigen Öl-/Gasverbrauch oder Heizkörperzustand zu kennen.
                </p>
              </div>

              <div class="p-4 rounded-2xl bg-blue-50/60 border border-blue-200/60 shadow-xs space-y-2">
                <div class="flex items-center gap-2 text-xs font-bold text-[#2563EB] uppercase tracking-wide">
                  <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                  <span>2. Wie unsere Website-Struktur das löst</span>
                </div>
                <p class="text-xs sm:text-sm text-ink-800">
                  Ein interaktiver <strong>Wärmepumpen- &amp; Bad-Konfigurator</strong> filtert die wichtigsten Eckdaten in 90 Sekunden. Reine Preisfüchse springen ab, echte Modernisierer liefern Ihnen alle Fakten auf den Schreibtisch.
                </p>
              </div>
            </div>

            <div class="pt-2 flex flex-wrap gap-3">
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="thermometer" class="w-3.5 h-3.5 text-blue-600"></i> Heizungs-Rechner
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="bath" class="w-3.5 h-3.5 text-blue-600"></i> 3D-Bad-Galerie
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="phone-call" class="w-3.5 h-3.5 text-blue-600"></i> Intelligenter Notdienst-Filter
              </span>
            </div>
          </div>

          <!-- Interactive UI Mockup (SHK) -->
          <div data-aos="flip-tilt-left" class="lg:col-span-6">
            <div class="bg-[#0F172A] rounded-3xl p-5 sm:p-6 border border-slate-800 shadow-2xl text-white space-y-4">
              
              <!-- Mockup Browser Bar -->
              <div class="flex items-center justify-between border-b border-slate-800/80 pb-3 text-xs font-mono select-none">
                <div class="flex items-center gap-1.5 sm:gap-2">
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#EF4444]/90 inline-block shadow-xs"></span>
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#F59E0B]/90 inline-block shadow-xs"></span>
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#10B981]/90 inline-block shadow-xs"></span>
                </div>
                <div class="bg-slate-800/90 px-3 sm:px-4 py-1 rounded-full border border-slate-700/70 text-slate-300 text-[10px] sm:text-[11px] font-medium shadow-inner flex items-center gap-1.5">
                  <i data-lucide="lock" class="w-3 h-3 text-emerald-400"></i>
                  <span class="text-white font-medium">kroeger-shk-owl.de</span>
                  <span class="hidden sm:inline-block text-[9px] bg-blue-500/20 text-blue-300 px-1.5 py-0.5 rounded font-mono font-bold ml-1">ONLINE</span>
                </div>
                <div class="inline-flex items-center gap-1.5 text-[10px] text-emerald-400 font-bold uppercase tracking-wider">
                  <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                  <span>Vorab-Filter</span>
                </div>
              </div>

              <!-- Converting Funnel Canvas (Matching Startseite #demo) -->
              <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-lg text-slate-900 transition-all">
                
                <!-- Funnel Progress Header -->
                <div class="border-b border-slate-100 pb-2.5">
                  <div class="flex items-center justify-between text-xs sm:text-sm font-bold text-slate-800">
                    <span id="mock-shk-step-label">Schritt 1 von 3: Vorhaben</span>
                    <div class="flex items-center gap-2">
                      <span class="text-emerald-700 font-bold text-xs flex items-center gap-1">
                        <i data-lucide="shield-check" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span>100% unverbindlich</span>
                      </span>
                      <span id="mock-shk-pct-label" class="bg-blue-50 text-[#2563EB] border border-blue-100 font-bold px-2.5 py-0.5 rounded-full text-xs font-mono">33%</span>
                    </div>
                  </div>
                  <!-- Progress Bar -->
                  <div class="w-full bg-slate-100 h-1.5 rounded-full overflow-hidden mt-2.5">
                    <div id="mock-shk-progress" class="sim-progress-bar h-full bg-[#2563EB] rounded-full" style="width: 33%;"></div>
                  </div>
                </div>

                <!-- STEP 1: SHK -->
                <div id="mock-shk-s1" class="space-y-3 pt-3 text-left">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">1. Welches SHK-Projekt planen Sie?</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Wählen Sie Ihre Maßnahme für Förder- &amp; Machbarkeitsprüfung:</p>
                  </div>

                  <div class="space-y-2">
                    <button type="button" onclick="advanceMockup('shk', 2, 'Wärmepumpe & Heizungstausch')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Wärmepumpe &amp; Heizungstausch</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Bis zu 70 % KfW-Zuschuss sichern, Gas-/Ölheizung modern ersetzen.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-orange-50 text-orange-600 flex items-center justify-center shrink-0">
                        <i data-lucide="flame" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('shk', 2, 'Komplettbad-Sanierung')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Komplettbad-Sanierung</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Barrierefreie Walk-In-Dusche, moderne Fliesen &amp; Wohlfühloase.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-blue-50 text-[#2563EB] flex items-center justify-center shrink-0">
                        <i data-lucide="droplets" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('shk', 2, 'Heizungswartung & Optimierung')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Heizungswartung &amp; Optimierung</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Hydraulischer Abgleich, Thermostat-Tausch &amp; regelmäßiger Werterhalt.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                        <i data-lucide="sliders" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('shk', 2, 'Akuter Rohrbruch / Notdienst')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Akuter Rohrbruch / Notdienst</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Notdienst-Priorisierung: Monteur gezielt mit passenden Teilen schicken.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-rose-50 text-rose-600 flex items-center justify-center shrink-0">
                        <i data-lucide="shield-alert" class="w-4 h-4"></i>
                      </div>
                    </button>
                  </div>

                  <div class="pt-1.5 text-center text-[11px] text-slate-400 font-mono flex items-center justify-center gap-1.5">
                    <i data-lucide="mouse-pointer-click" class="w-3.5 h-3.5 text-[#2563EB]"></i>
                    <span>Tipp: Klicken Sie auf eine Kachel zum Ausprobieren</span>
                  </div>
                </div>

                <!-- STEP 2: SHK -->
                <div id="mock-shk-s2" class="space-y-3 pt-3 text-left hidden">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">2. Heizungszustand &amp; Fotos</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Typenschild-Fotos ermöglichen sofortige Förderungs- &amp; Heizlastberechnung.</p>
                  </div>

                  <div class="p-2.5 rounded-xl bg-orange-50/80 border border-orange-200/80 text-xs text-orange-950 flex items-center justify-between">
                    <span class="text-slate-600">Ausgewählt:</span>
                    <strong id="mock-shk-selected-title" class="font-bold text-orange-700">Wärmepumpe &amp; Heizungstausch</strong>
                  </div>

                  <!-- Simulated Photo Upload Area -->
                  <div class="border-2 border-dashed border-slate-200 hover:border-[#2563EB] rounded-xl p-3 text-center space-y-1.5 bg-slate-50/60 transition-all">
                    <div class="w-8 h-8 rounded-full bg-orange-50 text-orange-600 flex items-center justify-center mx-auto">
                      <i data-lucide="camera" class="w-4 h-4"></i>
                    </div>
                    <div>
                      <div class="text-xs font-bold text-slate-900">Typenschild oder Heizraum-Foto (optional)</div>
                      <div class="text-[10px] text-slate-500">Handyfoto vom bestehenden Kessel &amp; Außenaufstellfläche</div>
                    </div>
                    <div class="p-2 bg-white rounded-lg border border-slate-200 flex items-center justify-between text-xs max-w-xs mx-auto shadow-2xs">
                      <div class="flex items-center gap-2">
                        <i data-lucide="image" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span class="font-semibold text-slate-800 text-[11px]">kessel-viessmann-typenschild.jpg</span>
                      </div>
                      <span class="text-[10px] font-mono text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded font-bold">Upload bereit</span>
                    </div>
                  </div>

                  <div class="space-y-1.5 text-xs">
                    <div class="p-2 bg-slate-50 rounded-lg border border-slate-200/80 flex justify-between items-center">
                      <span class="text-slate-500 font-mono text-[11px]">Bestand &amp; Fläche:</span>
                      <span class="font-bold text-slate-900">EFH Bj. 1992 · 140 m² Wohnfläche</span>
                    </div>
                    <div class="p-2 bg-slate-50 rounded-lg border border-slate-200/80 flex justify-between items-center">
                      <span class="text-slate-500 font-mono text-[11px]">Wärmeverteilung:</span>
                      <span class="font-bold text-emerald-700">Fußbodenheizung vorhanden (ideal für WP)</span>
                    </div>
                  </div>

                  <!-- Navigation -->
                  <div class="pt-2 border-t border-slate-100 flex items-center justify-between">
                    <button type="button" onclick="advanceMockup('shk', 1)" class="inline-flex items-center gap-1 text-xs font-semibold text-slate-500 hover:text-slate-900 transition-colors cursor-pointer">
                      <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i>
                      <span>Zurück</span>
                    </button>
                    <button type="button" onclick="advanceMockup('shk', 3)" class="inline-flex items-center justify-center gap-2 bg-orange-600 hover:bg-orange-700 text-white font-bold px-4 py-2 rounded-lg text-xs transition-all shadow-sm hover:shadow-md hover:-translate-y-0.5 cursor-pointer">
                      <span>Weiter zu Schritt 3 (Meister-Übergabe) →</span>
                    </button>
                  </div>
                </div>

                <!-- STEP 3: SHK -->
                <div id="mock-shk-s3" class="space-y-3 pt-3 text-left hidden">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">3. So strukturiert landet die Anfrage im SHK-Büro:</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Keine Leerläufe am Telefon: KfW-Förderfähigkeit direkt vorqualifiziert.</p>
                  </div>

                  <!-- Live Ticket Preview -->
                  <div class="bg-white rounded-xl border border-orange-500/30 p-3.5 shadow-sm space-y-2.5 relative overflow-hidden">
                    <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-orange-500 to-[#2563EB]"></div>
                    
                    <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                      <span class="inline-flex items-center gap-1 bg-emerald-50 text-emerald-700 text-[10px] font-bold px-2 py-0.5 rounded-full border border-emerald-200">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                        Qualifizierte SHK-Anfrage
                      </span>
                      <span class="text-[10px] text-slate-400 font-mono font-bold">Ticket: #SHK-7231</span>
                    </div>

                    <div class="grid grid-cols-2 gap-2 text-xs">
                      <div class="p-2.5 bg-slate-50 rounded-lg space-y-0.5">
                        <div class="text-[9px] font-mono uppercase text-slate-400 font-bold">Kunde &amp; Ort</div>
                        <div class="font-extrabold text-slate-900 text-xs">Familie Krüger</div>
                        <div class="text-slate-600 font-mono text-[11px]"><i data-lucide="map-pin" class="w-3 h-3 text-slate-500 inline mr-1"></i>Herford-Elverdissen</div>
                      </div>
                      <div class="p-2.5 bg-slate-50 rounded-lg space-y-0.5">
                        <div class="text-[9px] font-mono uppercase text-slate-400 font-bold">Maßnahme</div>
                        <div class="font-bold text-orange-600 text-xs">Wärmepumpentausch</div>
                        <div class="text-slate-600 text-[11px]">Bis zu 70 % KfW berechtigt</div>
                      </div>
                    </div>

                    <div class="p-2 bg-slate-50 rounded-lg flex items-center justify-between text-xs">
                      <div class="flex items-center gap-2">
                        <i data-lucide="image" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span class="text-[11px] font-semibold text-slate-800">2 Fotos angehängt (Kessel &amp; Stellplatz)</span>
                      </div>
                      <span class="text-[10px] font-mono font-bold text-blue-600 bg-white px-2 py-0.5 rounded border border-slate-200 shadow-2xs">Foto ansehen</span>
                    </div>

                    <div class="p-2.5 rounded-lg bg-orange-50/70 border border-orange-200 text-xs text-orange-950 leading-snug flex items-start gap-2">
                      <i data-lucide="check-circle-2" class="w-4 h-4 text-orange-600 shrink-0 mt-0.5"></i>
                      <div class="text-[11px]">
                        <strong>Ihr Zeitvorteil:</strong> Bis zu 45 Min. Telefonzeit pro Anfrage gespart – Angebote direkt am PC erstellen.
                      </div>
                    </div>
                  </div>

                  <!-- Footer actions -->
                  <div class="pt-2 border-t border-slate-100 flex items-center justify-between gap-2">
                    <button type="button" onclick="resetMockup('shk')" class="inline-flex items-center gap-1 text-xs font-bold text-slate-600 hover:text-slate-900 px-3 py-2 rounded-lg border border-slate-200 hover:bg-slate-50 transition-all cursor-pointer">
                      <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i>
                      <span>Demo neu starten</span>
                    </button>
                    <a href="anfrage.html" class="inline-flex items-center gap-1.5 bg-[#2563EB] hover:bg-blue-700 text-white font-bold text-xs px-3.5 py-2 rounded-lg transition-all shadow-xs hover:-translate-y-0.5">
                      <span>Vorab-Entwurf anfordern</span>
                      <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                    </a>
                  </div>
                </div>

              </div>

              <!-- Mockup Footer Stats -->
              <div class="flex justify-between items-center text-xs text-slate-400 pt-1">
                <span>Ergebnis für den Meisterbetrieb:</span>
                <span class="text-white font-bold">Bis zu 45 Min. Telefonzeit pro Anfrage gespart</span>
              </div>

            </div>
          </div>
        </div>
      </section>

      <!-- TAB 3: ELEKTROTECHNIK & PV -->
      <section id="pane-elektro" class="trade-pane hidden space-y-12">
        <div class="grid lg:grid-cols-12 gap-8 items-center">
          
          <div data-aos="fade-right" class="lg:col-span-6 space-y-6 text-left">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-blue-50 text-blue-800 border border-blue-200">
              <i data-lucide="zap" class="w-3.5 h-3.5 text-blue-600"></i>
              <span>Elektrotechnik &amp; Erneuerbare Energien</span>
            </div>

            <h2 class="text-2xl sm:text-4xl font-extrabold text-ink-950 leading-tight">
              PV-Anlagen, Wallboxen &amp; Smarthome mit klaren Eckdaten vorab.
            </h2>

            <!-- Authentic Project Photography Card -->
            <div class="rounded-2xl overflow-hidden border border-slate-200 shadow-xs">
              <picture>
                <source srcset="assets/projekt-elektro.webp" type="image/webp">
                <img src="assets/projekt-elektro.jpg" alt="PV-Anlage und Zählerschrank Bielefeld" class="w-full h-44 object-cover" width="600" height="176" loading="lazy">
              </picture>
              <div class="p-3 bg-slate-50 border-t border-slate-200 text-xs text-ink-700 flex justify-between items-center">
                <span>Echtes Meisterprojekt: 14,8 kWp Photovoltaik mit Speicher &amp; Wallbox in OWL</span>
                <span class="font-bold text-blue-600 font-mono text-[11px]">VDE-zertifiziert <i data-lucide="check" class="w-3 h-3 text-blue-600 inline"></i></span>
              </div>
            </div>

            <p class="text-sm sm:text-base text-ink-600 leading-relaxed">
              Elektromeister brauchen keine Anrufer, die nur wissen wollen, was ein Zählerkasten kostet. Sie brauchen Kunden mit echtem Kaufinteresse und Gesellen, die gerne für Ihren Betrieb arbeiten.
            </p>

            <div class="space-y-4 pt-2">
              <div class="p-4 rounded-2xl bg-white border border-pastel-sage shadow-xs space-y-2">
                <div class="flex items-center gap-2 text-xs font-bold text-red-600 uppercase tracking-wide">
                  <i data-lucide="alert-circle" class="w-4 h-4"></i>
                  <span>1. Das typische Problem im Alltag</span>
                </div>
                <p class="text-xs sm:text-sm text-ink-700">
                  PV-Anfragen ohne Angaben zu Dachausrichtung, Zählerschrank oder Speicherwunsch. Nach drei Telefonaten stellt sich heraus, dass das Dach asbestbelastet ist.
                </p>
              </div>

              <div class="p-4 rounded-2xl bg-blue-50/60 border border-blue-200/60 shadow-xs space-y-2">
                <div class="flex items-center gap-2 text-xs font-bold text-[#2563EB] uppercase tracking-wide">
                  <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                  <span>2. Wie unsere Website-Struktur das löst</span>
                </div>
                <p class="text-xs sm:text-sm text-ink-800">
                  Der <strong>Elektro-Vorabfilter</strong> fragt Zählerschrank-Foto, Stromverbrauch und Wunschtermin direkt ab. Gleichzeitig gewinnt Ihre Website neue Elektroniker über die 60-Sekunden-Bewerbung.
                </p>
              </div>
            </div>

            <div class="pt-2 flex flex-wrap gap-3">
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="sun" class="w-3.5 h-3.5 text-blue-600"></i> PV-Dach-Check
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="battery-charging" class="w-3.5 h-3.5 text-blue-600"></i> Wallbox-Vorprüfung
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="users" class="w-3.5 h-3.5 text-blue-600"></i> Fachkräfte-Funnel
              </span>
            </div>
          </div>

          <!-- Interactive UI Mockup (Elektro) -->
          <div data-aos="flip-tilt-left" class="lg:col-span-6">
            <div class="bg-[#0F172A] rounded-3xl p-5 sm:p-6 border border-slate-800 shadow-2xl text-white space-y-4">
              
              <!-- Mockup Browser Bar -->
              <div class="flex items-center justify-between border-b border-slate-800/80 pb-3 text-xs font-mono select-none">
                <div class="flex items-center gap-1.5 sm:gap-2">
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#EF4444]/90 inline-block shadow-xs"></span>
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#F59E0B]/90 inline-block shadow-xs"></span>
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#10B981]/90 inline-block shadow-xs"></span>
                </div>
                <div class="bg-slate-800/90 px-3 sm:px-4 py-1 rounded-full border border-slate-700/70 text-slate-300 text-[10px] sm:text-[11px] font-medium shadow-inner flex items-center gap-1.5">
                  <i data-lucide="lock" class="w-3 h-3 text-emerald-400"></i>
                  <span class="text-white font-medium">brinkmann-elektro-owl.de</span>
                  <span class="hidden sm:inline-block text-[9px] bg-blue-500/20 text-blue-300 px-1.5 py-0.5 rounded font-mono font-bold ml-1">ONLINE</span>
                </div>
                <div class="inline-flex items-center gap-1.5 text-[10px] text-emerald-400 font-bold uppercase tracking-wider">
                  <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                  <span>Vorab-Filter</span>
                </div>
              </div>

              <!-- Converting Funnel Canvas (Matching Startseite #demo) -->
              <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-lg text-slate-900 transition-all">
                
                <!-- Funnel Progress Header -->
                <div class="border-b border-slate-100 pb-2.5">
                  <div class="flex items-center justify-between text-xs sm:text-sm font-bold text-slate-800">
                    <span id="mock-elektro-step-label">Schritt 1 von 3: Vorhaben</span>
                    <div class="flex items-center gap-2">
                      <span class="text-emerald-700 font-bold text-xs flex items-center gap-1">
                        <i data-lucide="shield-check" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span>100% unverbindlich</span>
                      </span>
                      <span id="mock-elektro-pct-label" class="bg-blue-50 text-[#2563EB] border border-blue-100 font-bold px-2.5 py-0.5 rounded-full text-xs font-mono">33%</span>
                    </div>
                  </div>
                  <!-- Progress Bar -->
                  <div class="w-full bg-slate-100 h-1.5 rounded-full overflow-hidden mt-2.5">
                    <div id="mock-elektro-progress" class="sim-progress-bar h-full bg-[#2563EB] rounded-full" style="width: 33%;"></div>
                  </div>
                </div>

                <!-- STEP 1: ELEKTRO -->
                <div id="mock-elektro-s1" class="space-y-3 pt-3 text-left">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">1. Welches Elektroprojekt planen Sie?</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Wählen Sie Ihr Vorhaben für eine gezielte Vorab-Prüfung:</p>
                  </div>

                  <div class="space-y-2">
                    <button type="button" onclick="advanceMockup('elektro', 2, 'Photovoltaik & Stromspeicher')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Photovoltaik &amp; Stromspeicher</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Maximale Unabhängigkeit, Speicher &amp; Eigenverbrauch in Bielefeld &amp; OWL.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-blue-50 text-[#2563EB] flex items-center justify-center shrink-0">
                        <i data-lucide="sun" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('elektro', 2, 'Wallbox & Ladeinfrastruktur')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Wallbox &amp; Ladeinfrastruktur</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Privat- &amp; Firmenladestationen fachgerecht nach VDE-Standard installiert.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-amber-50 text-amber-600 flex items-center justify-center shrink-0">
                        <i data-lucide="zap" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('elektro', 2, 'Zählerschrank & Modernisierung')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Zählerschrank &amp; Modernisierung</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">TAB-konformer Umbau, Überspannungsschutz &amp; Kapazitätserweiterung.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                        <i data-lucide="cpu" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('elektro', 2, 'Smart Home & Gebäudetechnik')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Smart Home &amp; Gebäudetechnik</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">KNX-Automatisierung, intelligente Beleuchtung &amp; Netzwerkinfrastruktur.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-purple-50 text-purple-600 flex items-center justify-center shrink-0">
                        <i data-lucide="home" class="w-4 h-4"></i>
                      </div>
                    </button>
                  </div>

                  <div class="pt-1.5 text-center text-[11px] text-slate-400 font-mono flex items-center justify-center gap-1.5">
                    <i data-lucide="mouse-pointer-click" class="w-3.5 h-3.5 text-[#2563EB]"></i>
                    <span>Tipp: Klicken Sie auf eine Kachel zum Ausprobieren</span>
                  </div>
                </div>

                <!-- STEP 2: ELEKTRO -->
                <div id="mock-elektro-s2" class="space-y-3 pt-3 text-left hidden">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">2. Eckdaten &amp; Zählerfoto</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Ein Zählerkasten-Foto spart oft tagelange Wartezeit auf die Netzprüfung.</p>
                  </div>

                  <div class="p-2.5 rounded-xl bg-blue-50/80 border border-blue-200/80 text-xs text-blue-900 flex items-center justify-between">
                    <span class="text-slate-600">Ausgewählt:</span>
                    <strong id="mock-elektro-selected-title" class="font-bold text-[#2563EB]">Photovoltaik &amp; Stromspeicher</strong>
                  </div>

                  <!-- Simulated Photo Upload Area -->
                  <div class="border-2 border-dashed border-slate-200 hover:border-[#2563EB] rounded-xl p-3 text-center space-y-1.5 bg-slate-50/60 transition-all">
                    <div class="w-8 h-8 rounded-full bg-blue-50 text-[#2563EB] flex items-center justify-center mx-auto">
                      <i data-lucide="camera" class="w-4 h-4"></i>
                    </div>
                    <div>
                      <div class="text-xs font-bold text-slate-900">Foto vom Zählerkasten oder Dach (optional)</div>
                      <div class="text-[10px] text-slate-500">Zeigt dem Elektromeister sofort den Zustand der Hauptverteilung</div>
                    </div>
                    <div class="p-2 bg-white rounded-lg border border-slate-200 flex items-center justify-between text-xs max-w-xs mx-auto shadow-2xs">
                      <div class="flex items-center gap-2">
                        <i data-lucide="image" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span class="font-semibold text-slate-800 text-[11px]">zaehlerschrank-bestand.jpg</span>
                      </div>
                      <span class="text-[10px] font-mono text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded font-bold">Upload bereit</span>
                    </div>
                  </div>

                  <div class="space-y-1.5 text-xs">
                    <div class="p-2 bg-slate-50 rounded-lg border border-slate-200/80 flex justify-between items-center">
                      <span class="text-slate-500 font-mono text-[11px]">Dachausrichtung:</span>
                      <span class="font-bold text-slate-900">Süd ~45 m² Dachfläche (10–12 kWp)</span>
                    </div>
                    <div class="p-2 bg-slate-50 rounded-lg border border-slate-200/80 flex justify-between items-center">
                      <span class="text-slate-500 font-mono text-[11px]">Bestandsanlage:</span>
                      <span class="font-bold text-slate-900">Hager Zählerschrank (Bj. 1998)</span>
                    </div>
                  </div>

                  <!-- Navigation -->
                  <div class="pt-2 border-t border-slate-100 flex items-center justify-between">
                    <button type="button" onclick="advanceMockup('elektro', 1)" class="inline-flex items-center gap-1 text-xs font-semibold text-slate-500 hover:text-slate-900 transition-colors cursor-pointer">
                      <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i>
                      <span>Zurück</span>
                    </button>
                    <button type="button" onclick="advanceMockup('elektro', 3)" class="inline-flex items-center justify-center gap-2 bg-[#2563EB] hover:bg-blue-700 text-white font-bold px-4 py-2 rounded-lg text-xs transition-all shadow-sm hover:shadow-md hover:-translate-y-0.5 cursor-pointer">
                      <span>Weiter zu Schritt 3 (Meister-Übergabe) →</span>
                    </button>
                  </div>
                </div>

                <!-- STEP 3: ELEKTRO -->
                <div id="mock-elektro-s3" class="space-y-3 pt-3 text-left hidden">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">3. So strukturiert landet die Anfrage beim Meister:</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Alle technischen Parameter sofort parat für die Netzbetreiber-Prüfung.</p>
                  </div>

                  <!-- Live Ticket Preview -->
                  <div class="bg-white rounded-xl border border-blue-500/30 p-3.5 shadow-sm space-y-2.5 relative overflow-hidden">
                    <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 to-emerald-500"></div>
                    
                    <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                      <span class="inline-flex items-center gap-1 bg-emerald-50 text-emerald-700 text-[10px] font-bold px-2 py-0.5 rounded-full border border-emerald-200">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                        Qualifizierte PV-Anfrage
                      </span>
                      <span class="text-[10px] text-slate-400 font-mono font-bold">Ticket: #ELEK-9154</span>
                    </div>

                    <div class="grid grid-cols-2 gap-2 text-xs">
                      <div class="p-2.5 bg-slate-50 rounded-lg space-y-0.5">
                        <div class="text-[9px] font-mono uppercase text-slate-400 font-bold">Kunde &amp; Ort</div>
                        <div class="font-extrabold text-slate-900 text-xs">Dr. M. Schildesche</div>
                        <div class="text-slate-600 font-mono text-[11px]"><i data-lucide="map-pin" class="w-3 h-3 text-slate-500 inline mr-1"></i>Bielefeld · 0171 ...</div>
                      </div>
                      <div class="p-2.5 bg-slate-50 rounded-lg space-y-0.5">
                        <div class="text-[9px] font-mono uppercase text-slate-400 font-bold">Vorhaben</div>
                        <div class="font-bold text-[#2563EB] text-xs">10 kWp PV + Speicher</div>
                        <div class="text-slate-600 text-[11px]">Inkl. 11 kW Wallbox</div>
                      </div>
                    </div>

                    <div class="p-2 bg-slate-50 rounded-lg flex items-center justify-between text-xs">
                      <div class="flex items-center gap-2">
                        <i data-lucide="image" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span class="text-[11px] font-semibold text-slate-800">2 Fotos (Zählerschrank &amp; Dach)</span>
                      </div>
                      <span class="text-[10px] font-mono font-bold text-blue-600 bg-white px-2 py-0.5 rounded border border-slate-200 shadow-2xs">Foto ansehen</span>
                    </div>

                    <div class="p-2.5 rounded-lg bg-blue-50/70 border border-blue-200 text-xs text-blue-950 leading-snug flex items-start gap-2">
                      <i data-lucide="check-circle-2" class="w-4 h-4 text-[#2563EB] shrink-0 mt-0.5"></i>
                      <div class="text-[11px]">
                        <strong>Ihr Zeitvorteil:</strong> Kein unnötiger Vor-Ort-Check nötig: Zählerkasten-Zustand liegt digital vor.
                      </div>
                    </div>
                  </div>

                  <!-- Footer actions -->
                  <div class="pt-2 border-t border-slate-100 flex items-center justify-between gap-2">
                    <button type="button" onclick="resetMockup('elektro')" class="inline-flex items-center gap-1 text-xs font-bold text-slate-600 hover:text-slate-900 px-3 py-2 rounded-lg border border-slate-200 hover:bg-slate-50 transition-all cursor-pointer">
                      <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i>
                      <span>Demo neu starten</span>
                    </button>
                    <a href="anfrage.html" class="inline-flex items-center gap-1.5 bg-[#2563EB] hover:bg-blue-700 text-white font-bold text-xs px-3.5 py-2 rounded-lg transition-all shadow-xs hover:-translate-y-0.5">
                      <span>Vorab-Entwurf anfordern</span>
                      <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                    </a>
                  </div>
                </div>

              </div>

              <!-- Mockup Footer Stats -->
              <div class="flex justify-between items-center text-xs text-slate-400 pt-1">
                <span>Ergebnis für den Meisterbetrieb:</span>
                <span class="text-white font-bold">100 % passgenaue Netzanfragen ohne Nacharbeit</span>
              </div>

            </div>
          </div>
        </div>
      </section>

      <!-- TAB 4: TISCHLEREI & AUSBAU -->
      <section id="pane-tischler" class="trade-pane hidden space-y-12">
        <div class="grid lg:grid-cols-12 gap-8 items-center">
          
          <div data-aos="fade-right" class="lg:col-span-6 space-y-6 text-left">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-emerald-50 text-emerald-800 border border-emerald-200">
              <i data-lucide="ruler" class="w-3.5 h-3.5 text-emerald-600"></i>
              <span>Tischlerei, Metallbau &amp; Innenausbau</span>
            </div>

            <h2 class="text-2xl sm:text-4xl font-extrabold text-ink-950 leading-tight">
              Maßarbeit in Holz &amp; Raum – Reine Möbelhaus-Preissucher aussortieren.
            </h2>

            <!-- Authentic Project Photography Card -->
            <div class="rounded-2xl overflow-hidden border border-slate-200 shadow-xs">
              <picture>
                <source srcset="assets/projekt-tischlerei-werkstatt.webp" type="image/webp">
                <img src="assets/projekt-tischlerei-werkstatt.jpg" alt="Tischlerei Werkstatt und Maßanfertigung Detmold" class="w-full h-44 object-cover" width="600" height="176" loading="lazy">
              </picture>
              <div class="p-3 bg-slate-50 border-t border-slate-200 text-xs text-ink-700 flex justify-between items-center">
                <span>Echtes Meisterprojekt: Individuelle Massivholz-Möbelmanufaktur in Detmold</span>
                <span class="font-bold text-emerald-600 font-mono text-[11px]">Echtholz geölt <i data-lucide="check" class="w-3 h-3 text-emerald-600 inline"></i></span>
              </div>
            </div>

            <p class="text-sm sm:text-base text-ink-600 leading-relaxed">
              Individuelle Einbauschränke, Massivholztische und Treppen entstehen durch meisterhaftes Handwerk. Ihre Website muss sofort vermitteln, dass Qualität ihren berechtigten Wert hat.
            </p>

            <div class="space-y-4 pt-2">
              <div class="p-4 rounded-2xl bg-white border border-pastel-sage shadow-xs space-y-2">
                <div class="flex items-center gap-2 text-xs font-bold text-red-600 uppercase tracking-wide">
                  <i data-lucide="alert-circle" class="w-4 h-4"></i>
                  <span>1. Das typische Problem im Alltag</span>
                </div>
                <p class="text-xs sm:text-sm text-ink-700">
                  Kunden schicken Ikea-Links und fragen: „Können Sie mir das für 400 € bauen?“ Sie vergeuden Zeit mit Angebotserstellungen für Interessenten ohne Qualitätsbewusstsein.
                </p>
              </div>

              <div class="p-4 rounded-2xl bg-blue-50/60 border border-blue-200/60 shadow-xs space-y-2">
                <div class="flex items-center gap-2 text-xs font-bold text-[#2563EB] uppercase tracking-wide">
                  <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                  <span>2. Wie unsere Website-Struktur das löst</span>
                </div>
                <p class="text-xs sm:text-sm text-ink-800">
                  Hochauflösende <strong>Projekt-Schaukästen mit Detailaufnahmen</strong> und ein Budget-Korridor im Vorab-Filter zeigen von der ersten Sekunde an den Premium-Anspruch Ihres Betriebs.
                </p>
              </div>
            </div>

            <div class="pt-2 flex flex-wrap gap-3">
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="image" class="w-3.5 h-3.5 text-blue-600"></i> Detail-Fotogalerien
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="sliders" class="w-3.5 h-3.5 text-blue-600"></i> Budget-Vorfilter
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 text-xs font-semibold text-ink-800">
                <i data-lucide="sparkles" class="w-3.5 h-3.5 text-blue-600"></i> Material-Muster-Vorschau
              </span>
            </div>
          </div>

          <!-- Interactive UI Mockup (Tischler) -->
          <div data-aos="flip-tilt-left" class="lg:col-span-6">
            <div class="bg-[#0F172A] rounded-3xl p-5 sm:p-6 border border-slate-800 shadow-2xl text-white space-y-4">
              
              <!-- Mockup Browser Bar -->
              <div class="flex items-center justify-between border-b border-slate-800/80 pb-3 text-xs font-mono select-none">
                <div class="flex items-center gap-1.5 sm:gap-2">
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#EF4444]/90 inline-block shadow-xs"></span>
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#F59E0B]/90 inline-block shadow-xs"></span>
                  <span class="w-2.5 sm:w-3 h-2.5 sm:h-3 rounded-full bg-[#10B981]/90 inline-block shadow-xs"></span>
                </div>
                <div class="bg-slate-800/90 px-3 sm:px-4 py-1 rounded-full border border-slate-700/70 text-slate-300 text-[10px] sm:text-[11px] font-medium shadow-inner flex items-center gap-1.5">
                  <i data-lucide="lock" class="w-3 h-3 text-emerald-400"></i>
                  <span class="text-white font-medium">kramer-innenausbau-owl.de</span>
                  <span class="hidden sm:inline-block text-[9px] bg-blue-500/20 text-blue-300 px-1.5 py-0.5 rounded font-mono font-bold ml-1">ONLINE</span>
                </div>
                <div class="inline-flex items-center gap-1.5 text-[10px] text-emerald-400 font-bold uppercase tracking-wider">
                  <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                  <span>Vorab-Filter</span>
                </div>
              </div>

              <!-- Converting Funnel Canvas (Matching Startseite #demo) -->
              <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-lg text-slate-900 transition-all">
                
                <!-- Funnel Progress Header -->
                <div class="border-b border-slate-100 pb-2.5">
                  <div class="flex items-center justify-between text-xs sm:text-sm font-bold text-slate-800">
                    <span id="mock-tischler-step-label">Schritt 1 von 3: Vorhaben</span>
                    <div class="flex items-center gap-2">
                      <span class="text-emerald-700 font-bold text-xs flex items-center gap-1">
                        <i data-lucide="shield-check" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span>100% unverbindlich</span>
                      </span>
                      <span id="mock-tischler-pct-label" class="bg-blue-50 text-[#2563EB] border border-blue-100 font-bold px-2.5 py-0.5 rounded-full text-xs font-mono">33%</span>
                    </div>
                  </div>
                  <!-- Progress Bar -->
                  <div class="w-full bg-slate-100 h-1.5 rounded-full overflow-hidden mt-2.5">
                    <div id="mock-tischler-progress" class="sim-progress-bar h-full bg-[#2563EB] rounded-full" style="width: 33%;"></div>
                  </div>
                </div>

                <!-- STEP 1: TISCHLER -->
                <div id="mock-tischler-s1" class="space-y-3 pt-3 text-left">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">1. Welches Holz- &amp; Ausbauprojekt planen Sie?</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Wählen Sie Ihre Projektart für eine maßgenaue Vorab-Kalkulation:</p>
                  </div>

                  <div class="space-y-2">
                    <button type="button" onclick="advanceMockup('tischler', 2, 'Einbauschrank nach Maß (Dachschräge)')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Einbauschrank nach Maß (Dachschräge)</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Dachschrägen, Nischen &amp; Ankleidezimmer millimetergenau gefertigt.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0">
                        <i data-lucide="layers" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('tischler', 2, 'Massivholztisch & Unikatmöbel')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Massivholztisch &amp; Unikatmöbel</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Wildeiche, Nussbaum &amp; Altholz geölt aus regionaler Meister-Manufaktur.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-amber-50 text-amber-600 flex items-center justify-center shrink-0">
                        <i data-lucide="sparkles" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('tischler', 2, 'Treppenbau & Innentüren nach Maß')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Treppenbau &amp; Innentüren nach Maß</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Massivholztreppen, raumhohe Türen &amp; moderne Schiebeelemente.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-blue-50 text-[#2563EB] flex items-center justify-center shrink-0">
                        <i data-lucide="ruler" class="w-4 h-4"></i>
                      </div>
                    </button>

                    <button type="button" onclick="advanceMockup('tischler', 2, 'Kompletter Innenausbau (Praxis/Wohnen)')" class="sim-card-option w-full p-2.5 sm:p-3 rounded-xl border border-slate-200 flex items-start gap-3 text-left group">
                      <div class="sim-radio-circle mt-0.5"><div class="sim-radio-dot"></div></div>
                      <div class="flex-1">
                        <div class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-[#2563EB] transition-colors">Kompletter Innenausbau (Praxis/Wohnen)</div>
                        <div class="text-[11px] text-slate-500 mt-0.5 leading-snug">Praxen, Kanzleien, Empfangsbereiche &amp; hochwertiges Privatwohnen.</div>
                      </div>
                      <div class="w-7 h-7 rounded-lg bg-purple-50 text-purple-600 flex items-center justify-center shrink-0">
                        <i data-lucide="layout" class="w-4 h-4"></i>
                      </div>
                    </button>
                  </div>

                  <div class="pt-1.5 text-center text-[11px] text-slate-400 font-mono flex items-center justify-center gap-1.5">
                    <i data-lucide="mouse-pointer-click" class="w-3.5 h-3.5 text-[#2563EB]"></i>
                    <span>Tipp: Klicken Sie auf eine Kachel zum Ausprobieren</span>
                  </div>
                </div>

                <!-- STEP 2: TISCHLER -->
                <div id="mock-tischler-s2" class="space-y-3 pt-3 text-left hidden">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">2. Maße &amp; Raumskizze</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Eine grobe Skizze oder Handyfoto reicht für die erste Entwurfsplanung.</p>
                  </div>

                  <div class="p-2.5 rounded-xl bg-emerald-50/80 border border-emerald-200/80 text-xs text-emerald-950 flex items-center justify-between">
                    <span class="text-slate-600">Ausgewählt:</span>
                    <strong id="mock-tischler-selected-title" class="font-bold text-emerald-800">Einbauschrank nach Maß</strong>
                  </div>

                  <!-- Simulated Photo Upload Area -->
                  <div class="border-2 border-dashed border-slate-200 hover:border-[#2563EB] rounded-xl p-3 text-center space-y-1.5 bg-slate-50/60 transition-all">
                    <div class="w-8 h-8 rounded-full bg-emerald-50 text-emerald-700 flex items-center justify-center mx-auto">
                      <i data-lucide="camera" class="w-4 h-4"></i>
                    </div>
                    <div>
                      <div class="text-xs font-bold text-slate-900">Skizze oder Raumfoto anhängen (optional)</div>
                      <div class="text-[10px] text-slate-500">Handyfoto von der Nische, Dachschräge oder Grundriss</div>
                    </div>
                    <div class="p-2 bg-white rounded-lg border border-slate-200 flex items-center justify-between text-xs max-w-xs mx-auto shadow-2xs">
                      <div class="flex items-center gap-2">
                        <i data-lucide="image" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span class="font-semibold text-slate-800 text-[11px]">skizze-dachschraege-masse.pdf</span>
                      </div>
                      <span class="text-[10px] font-mono text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded font-bold">Upload bereit</span>
                    </div>
                  </div>

                  <div class="space-y-1.5 text-xs">
                    <div class="p-2 bg-slate-50 rounded-lg border border-slate-200/80 flex justify-between items-center">
                      <span class="text-slate-500 font-mono text-[11px]">Einbausituation:</span>
                      <span class="font-bold text-slate-900">Dachschräge Kniestock 85 cm · Breite 3,80 m</span>
                    </div>
                    <div class="p-2 bg-slate-50 rounded-lg border border-slate-200/80 flex justify-between items-center">
                      <span class="text-slate-500 font-mono text-[11px]">Material &amp; Holz:</span>
                      <span class="font-bold text-emerald-800">Wildeiche massiv mit mattschwarzen Griffen</span>
                    </div>
                  </div>

                  <!-- Navigation -->
                  <div class="pt-2 border-t border-slate-100 flex items-center justify-between">
                    <button type="button" onclick="advanceMockup('tischler', 1)" class="inline-flex items-center gap-1 text-xs font-semibold text-slate-500 hover:text-slate-900 transition-colors cursor-pointer">
                      <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i>
                      <span>Zurück</span>
                    </button>
                    <button type="button" onclick="advanceMockup('tischler', 3)" class="inline-flex items-center justify-center gap-2 bg-[#2563EB] hover:bg-blue-700 text-white font-bold px-4 py-2 rounded-lg text-xs transition-all shadow-sm hover:shadow-md hover:-translate-y-0.5 cursor-pointer">
                      <span>Weiter zu Schritt 3 (Meister-Übergabe) →</span>
                    </button>
                  </div>
                </div>

                <!-- STEP 3: TISCHLER -->
                <div id="mock-tischler-s3" class="space-y-3 pt-3 text-left hidden">
                  <div>
                    <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight">3. So strukturiert landet die Anfrage in der Werkstatt:</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Alle Maße und Materialwünsche liegen sofort für den Zuschnitt vor.</p>
                  </div>

                  <!-- Live Ticket Preview -->
                  <div class="bg-white rounded-xl border border-emerald-500/30 p-3.5 shadow-sm space-y-2.5 relative overflow-hidden">
                    <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-emerald-500 to-[#2563EB]"></div>
                    
                    <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                      <span class="inline-flex items-center gap-1 bg-emerald-50 text-emerald-700 text-[10px] font-bold px-2 py-0.5 rounded-full border border-emerald-200">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                        Qualifizierte Maßmöbel-Anfrage
                      </span>
                      <span class="text-[10px] text-slate-400 font-mono font-bold">Ticket: #TISCH-3412</span>
                    </div>

                    <div class="grid grid-cols-2 gap-2 text-xs">
                      <div class="p-2.5 bg-slate-50 rounded-lg space-y-0.5">
                        <div class="text-[9px] font-mono uppercase text-slate-400 font-bold">Auftraggeber &amp; Ort</div>
                        <div class="font-extrabold text-slate-900 text-xs">Familie Wehmeier</div>
                        <div class="text-slate-600 font-mono text-[11px]"><i data-lucide="map-pin" class="w-3 h-3 text-slate-500 inline mr-1"></i>Detmold · 05231 ...</div>
                      </div>
                      <div class="p-2.5 bg-slate-50 rounded-lg space-y-0.5">
                        <div class="text-[9px] font-mono uppercase text-slate-400 font-bold">Maßarbeit</div>
                        <div class="font-bold text-emerald-700 text-xs">Einbauschrank Schräge</div>
                        <div class="text-slate-600 text-[11px]">Wildeiche massiv geölt</div>
                      </div>
                    </div>

                    <div class="p-2 bg-slate-50 rounded-lg flex items-center justify-between text-xs">
                      <div class="flex items-center gap-2">
                        <i data-lucide="file-text" class="w-3.5 h-3.5 text-emerald-600"></i>
                        <span class="text-[11px] font-semibold text-slate-800">Skizze &amp; 1 Foto angehängt (3.1 MB)</span>
                      </div>
                      <span class="text-[10px] font-mono font-bold text-blue-600 bg-white px-2 py-0.5 rounded border border-slate-200 shadow-2xs">PDF ansehen</span>
                    </div>

                    <div class="p-2.5 rounded-lg bg-emerald-50/70 border border-emerald-200 text-xs text-emerald-900 leading-snug flex items-start gap-2">
                      <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
                      <div class="text-[11px]">
                        <strong>Ihr Zeitvorteil:</strong> 80 % Abschlussquote beim Erstgespräch dank klar definierter Budget- &amp; Materialwünsche.
                      </div>
                    </div>
                  </div>

                  <!-- Footer actions -->
                  <div class="pt-2 border-t border-slate-100 flex items-center justify-between gap-2">
                    <button type="button" onclick="resetMockup('tischler')" class="inline-flex items-center gap-1 text-xs font-bold text-slate-600 hover:text-slate-900 px-3 py-2 rounded-lg border border-slate-200 hover:bg-slate-50 transition-all cursor-pointer">
                      <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i>
                      <span>Demo neu starten</span>
                    </button>
                    <a href="anfrage.html" class="inline-flex items-center gap-1.5 bg-[#2563EB] hover:bg-blue-700 text-white font-bold text-xs px-3.5 py-2 rounded-lg transition-all shadow-xs hover:-translate-y-0.5">
                      <span>Vorab-Entwurf anfordern</span>
                      <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                    </a>
                  </div>
                </div>

              </div>

              <!-- Mockup Footer Stats -->
              <div class="flex justify-between items-center text-xs text-slate-400 pt-1">
                <span>Ergebnis für den Meisterbetrieb:</span>
                <span class="text-white font-bold">Wertschätzung für echtes Handwerk &amp; faire Preise</span>
              </div>

            </div>
          </div>
        </div>
      </section>

    </div>

    <!-- ══════════════════════════════════════════════ -->
    <!-- 2. NEUE SEKTION: WEITERE GEWERKE IN OWL (6ER)  -->
    <!-- ══════════════════════════════════════════════ -->
    <section data-aos="fade-up" class="space-y-10 pt-4">
      <div class="text-center max-w-3xl mx-auto space-y-3">
        <h2 class="text-2xl sm:text-4xl font-extrabold text-ink-950">
          Weitere Gewerke, die wir in Bielefeld &amp; OWL betreuen
        </h2>
        <p class="text-sm sm:text-base text-ink-600 leading-relaxed">
          Ihr Handwerk war oben noch nicht dabei? Unsere modulare System-Architektur ist flexibel und wird exakt auf die Besonderheiten und Abrechnungsmodelle Ihres Gewerks abgestimmt.
        </p>
      </div>

      <!-- 6-Karten-Grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 text-left">
        
        <!-- Gewerke-Karte 1: GaLaBau -->
        <div class="bg-white rounded-3xl p-6 sm:p-7 border border-pastel-sage shadow-xs hover:border-[#2563EB] transition-all space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center font-bold">
              <i data-lucide="trees" class="w-5 h-5"></i>
            </div>
            <div>
              <span class="text-[10px] font-mono font-bold uppercase tracking-wider text-emerald-600">Garten- &amp; Landschaftsbau</span>
              <h3 class="text-lg font-bold text-ink-950 mt-0.5">GaLaBau, Pflaster- &amp; Erdarbeiten</h3>
            </div>
            <p class="text-xs text-ink-600 leading-relaxed">
              <strong>Fokus:</strong> Komplette Garten-Neuanlagen, Hangabfangungen, Terrassen &amp; Baggerarbeiten statt unbezahlter Kleinstpflege.
            </p>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-ink-700 space-y-1 font-mono">
              <div class="text-ink-950 font-bold">Integrierte Vorab-Filter:</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Grundstücksgröße (m²) &amp; Hanglage</span></div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Bagger-Zufahrtsbreite vor Ort</span></div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Foto-Upload von Gelände &amp; Plänen</span></div>
            </div>
          </div>
          <div class="pt-2 text-xs font-bold text-[#2563EB] flex items-center gap-1">
            <span>5-stellige Gartenprojekte planbar machen</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </div>
        </div>

        <!-- Gewerke-Karte 2: Maler & Fassade -->
        <div class="bg-white rounded-3xl p-6 sm:p-7 border border-pastel-sage shadow-xs hover:border-[#2563EB] transition-all space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-700 flex items-center justify-center font-bold">
              <i data-lucide="paint-roller" class="w-5 h-5"></i>
            </div>
            <div>
              <span class="text-[10px] font-mono font-bold uppercase tracking-wider text-purple-600">Maler- &amp; Stuckateurbetrieb</span>
              <h3 class="text-lg font-bold text-ink-950 mt-0.5">Maler, Putz, WDVS &amp; Fassade</h3>
            </div>
            <p class="text-xs text-ink-600 leading-relaxed">
              <strong>Fokus:</strong> Energetische WDVS-Fassadensanierung, Schimmelbeseitigung &amp; anspruchsvolle Innenraumgestaltung.
            </p>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-ink-700 space-y-1 font-mono">
              <div class="text-ink-950 font-bold">Integrierte Vorab-Filter:</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Gebäudehöhe &amp; Gerüstbedarf</span></div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Wandflächen (m²) &amp; Risserkennung</span></div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Foto-Upload der Fassaden-Ansichten</span></div>
            </div>
          </div>
          <div class="pt-2 text-xs font-bold text-[#2563EB] flex items-center gap-1">
            <span>Seriöse Angebote ohne böse Überraschungen</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </div>
        </div>

        <!-- Gewerke-Karte 3: Fliesenleger -->
        <div class="bg-white rounded-3xl p-6 sm:p-7 border border-pastel-sage shadow-xs hover:border-[#2563EB] transition-all space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-10 h-10 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center font-bold">
              <i data-lucide="grid" class="w-5 h-5"></i>
            </div>
            <div>
              <span class="text-[10px] font-mono font-bold uppercase tracking-wider text-blue-600">Fliesen- &amp; Natursteinhandwerk</span>
              <h3 class="text-lg font-bold text-ink-950 mt-0.5">Fliesen-, Platten- &amp; Natursteinleger</h3>
            </div>
            <p class="text-xs text-ink-600 leading-relaxed">
              <strong>Fokus:</strong> Barrierefreie Walk-in-Bäder, fugenlose XXL-Großformate &amp; hochwertige Naturstein-Terrassen.
            </p>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-ink-700 space-y-1 font-mono">
              <div class="text-ink-950 font-bold">Integrierte Vorab-Filter:</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Quadratmeter &amp; Verlege-Muster</span></div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Untergrund (Estrich / Trockenbau / Altbau)</span></div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Materialmuster &amp; Vorab-Foto</span></div>
            </div>
          </div>
          <div class="pt-2 text-xs font-bold text-[#2563EB] flex items-center gap-1">
            <span>Kunden mit Sinn für Meisterpräzision anziehen</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </div>
        </div>

        <!-- Gewerke-Karte 4: Metallbau -->
        <div class="bg-white rounded-3xl p-6 sm:p-7 border border-pastel-sage shadow-xs hover:border-[#2563EB] transition-all space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-700 flex items-center justify-center font-bold">
              <i data-lucide="wrench" class="w-5 h-5"></i>
            </div>
            <div>
              <span class="text-[10px] font-mono font-bold uppercase tracking-wider text-amber-600">Metallbau &amp; Schlosserei</span>
              <h3 class="text-lg font-bold text-ink-950 mt-0.5">Metall-, Geländer- &amp; Stahlbau</h3>
            </div>
            <p class="text-xs text-ink-600 leading-relaxed">
              <strong>Fokus:</strong> Außentreppen, Balkonanlagen, Geländer, Zaun- &amp; Toranlagen sowie Vordächer nach Maß.
            </p>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-ink-700 space-y-1 font-mono">
              <div class="text-ink-950 font-bold">Integrierte Vorab-Filter:</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Material (Edelstahl / Verzinkt / Pulver)</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Statik- &amp; Bauantrags-Vorprüfung</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Skizzen- &amp; Bemaßungs-Upload</div>
            </div>
          </div>
          <div class="pt-2 text-xs font-bold text-[#2563EB] flex items-center gap-1">
            <span>Genaue technische Vorgaben vor erstem Aufmaß</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </div>
        </div>

        <!-- Gewerke-Karte 5: Maurer & Sanierungsbau -->
        <div class="bg-white rounded-3xl p-6 sm:p-7 border border-pastel-sage shadow-xs hover:border-[#2563EB] transition-all space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-10 h-10 rounded-xl bg-orange-50 text-orange-700 flex items-center justify-center font-bold">
              <i data-lucide="blocks" class="w-5 h-5"></i>
            </div>
            <div>
              <span class="text-[10px] font-mono font-bold uppercase tracking-wider text-orange-600">Bauunternehmen &amp; Altbausanierung</span>
              <h3 class="text-lg font-bold text-ink-950 mt-0.5">Maurer, Beton- &amp; Sanierungsbau</h3>
            </div>
            <p class="text-xs text-ink-600 leading-relaxed">
              <strong>Fokus:</strong> Wanddurchbrüche (Stahlträger), Umbau, Kernsanierungen, Kellerabdichtung &amp; Bautenschutz.
            </p>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-ink-700 space-y-1 font-mono">
              <div class="text-ink-950 font-bold">Integrierte Vorab-Filter:</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Baujahr &amp; Bausubstanz-Erfassung</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Statiker-Gutachten vorhanden (Ja/Nein)</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Rissverlauf- &amp; Feuchte-Foto-Upload</div>
            </div>
          </div>
          <div class="pt-2 text-xs font-bold text-[#2563EB] flex items-center gap-1">
            <span>Haftungsrisiken minimieren &amp; sauber planen</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </div>
        </div>

        <!-- Gewerke-Karte 6: Boden- & Parkettleger -->
        <div class="bg-white rounded-3xl p-6 sm:p-7 border border-pastel-sage shadow-xs hover:border-[#2563EB] transition-all space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-10 h-10 rounded-xl bg-indigo-50 text-indigo-700 flex items-center justify-center font-bold">
              <i data-lucide="layers" class="w-5 h-5"></i>
            </div>
            <div>
              <span class="text-[10px] font-mono font-bold uppercase tracking-wider text-indigo-600">Boden- &amp; Raumausstattung</span>
              <h3 class="text-lg font-bold text-ink-950 mt-0.5">Raumausstatter, Boden- &amp; Parkettleger</h3>
            </div>
            <p class="text-xs text-ink-600 leading-relaxed">
              <strong>Fokus:</strong> Hochwertiges Massivholzparkett, Fischgrät, Designbeläge &amp; anspruchsvoller Gewerbe-Objektboden.
            </p>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-ink-700 space-y-1 font-mono">
              <div class="text-ink-950 font-bold">Integrierte Vorab-Filter:</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Raumgröße (m²) &amp; Raumgeometrie</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Untergrund &amp; Fußbodenheizungs-Prüfung</div>
              <div class="flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-[#2563EB] shrink-0"></i><span>Sockelleisten &amp; Altboden-Entsorgung</div>
            </div>
          </div>
          <div class="pt-2 text-xs font-bold text-[#2563EB] flex items-center gap-1">
            <span>Höhere Margen durch Komplettleistung</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </div>
        </div>

      </div>

      <!-- Hint Banner -->
      <div class="bg-blue-50/80 rounded-2xl p-6 sm:p-8 border border-blue-200 flex flex-col sm:flex-row items-center justify-between gap-6 text-left">
        <div class="space-y-1 max-w-2xl">
          <h4 class="text-base sm:text-lg font-bold text-ink-950">
            Ihr Gewerk ist noch spezieller?
          </h4>
          <p class="text-xs sm:text-sm text-ink-700 leading-relaxed">
            Ob Kälte- &amp; Klimatechnik, Brunnenbau, Glaserei, Trockenbau, Gerüstbau oder Ofenbau: Wir passen jedes Anfrage-Modul individuell auf Ihre Leistungen an – inklusive aller regionalen Besonderheiten in Bielefeld &amp; OWL.
          </p>
        </div>
        <a href="anfrage.html" class="shrink-0 inline-flex items-center gap-2 bg-[#2563EB] hover:bg-blue-700 text-white font-bold text-xs sm:text-sm px-5 py-3 rounded-xl transition-all shadow-sm">
          <span>Individuelle Lösung anfragen</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════ -->
    <!-- 3. NEUE SEKTION: ZWEI PROBLEME, EINE LÖSUNG    -->
    <!-- ══════════════════════════════════════════════ -->
    <section data-aos="fade-up" class="space-y-8">
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <h2 class="text-2xl sm:text-4xl font-extrabold text-ink-950">
          Zwei Probleme, eine Lösung: Lukrative Aufträge &amp; gute Fachkräfte
        </h2>
        <p class="text-xs sm:text-sm text-ink-600">
          Eine SparrenWeb-Website erfüllt für Ihren Handwerksbetrieb zwei entscheidende Wachstumsaufgaben gleichzeitig.
        </p>
      </div>

      <!-- Zweispaltiger Dark/Light Kontrast-Block -->
      <div class="grid md:grid-cols-2 gap-8 items-stretch text-left">
        
        <!-- Spalte 1: Für Ihre Kunden (Light Canvas Card) -->
        <div class="bg-white rounded-3xl p-8 sm:p-10 border border-pastel-sage shadow-md space-y-6 flex flex-col justify-between">
          <div class="space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-blue-50 text-[#2563EB] border border-blue-200">
              <i data-lucide="target" class="w-3.5 h-3.5"></i>
              <span>Für Ihre Kunden &amp; Bauherren</span>
            </div>

            <h3 class="text-xl sm:text-2xl font-extrabold text-ink-950 leading-snug">
              Schluss mit Preisfüchsen: Ziehen Sie genau die Projekte an, an denen Ihr Betrieb wirklich verdient.
            </h3>

            <p class="text-xs sm:text-sm text-ink-600 leading-relaxed">
              Kunden ohne Budget, die drei Betriebe gegeneinander ausspielen, vergeuden wertvolle Arbeitsstunden. Unsere Website-Struktur trennt die Spreu vom Weizen.
            </p>

            <ul class="space-y-3 text-xs sm:text-sm text-ink-800">
              <li class="flex items-start gap-2.5">
                <i data-lucide="check" class="w-4 h-4 text-[#2563EB] shrink-0 mt-0.5"></i>
                <span><strong>Geführter Vorab-Filter:</strong> Fragt Budgetkorridor, Maße und Fotos ab – unqualifizierte Anrufe springen vorher ab.</span>
              </li>
              <li class="flex items-start gap-2.5">
                <i data-lucide="check" class="w-4 h-4 text-[#2563EB] shrink-0 mt-0.5"></i>
                <span><strong>Meister-Referenzgalerien:</strong> Bildgewaltige Präsentation Ihrer Qualitätsarbeit vor Ort in Bielefeld, Herford &amp; Gütersloh.</span>
              </li>
              <li class="flex items-start gap-2.5">
                <i data-lucide="check" class="w-4 h-4 text-[#2563EB] shrink-0 mt-0.5"></i>
                <span><strong>Keine Preiskämpfe:</strong> Vertrauens-Elemente begründen Ihren Meisterpreis, bevor der Kunde überhaupt ein Angebot sieht.</span>
              </li>
            </ul>
          </div>

          <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs font-bold">
            <span class="text-ink-500">Messbarer Effekt:</span>
            <span class="text-emerald-600">Bis zu 40 % weniger Zeitverlust im Büro</span>
          </div>
        </div>

        <!-- Spalte 2: Für Gesellen & Azubis (Dark Slate/Navy Card) -->
        <div class="bg-[#0F172A] rounded-3xl p-8 sm:p-10 border border-slate-800 shadow-xl space-y-6 flex flex-col justify-between text-white">
          <div class="space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-blue-950 text-blue-300 border border-blue-700/60">
              <i data-lucide="users" class="w-3.5 h-3.5 text-blue-400"></i>
              <span>Für Gesellen, Meister &amp; Azubis</span>
            </div>

            <h3 class="text-xl sm:text-2xl font-extrabold text-white leading-snug">
              60-Sekunden-Bewerbung am Smartphone: Gesellen ohne Lebenslauf-Hürde gewinnen.
            </h3>

            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              Gute Handwerker haben keine Zeit für Anschreiben und Lebensläufe. Unsere mobile Kurzbewerbung holt Fachkräfte genau da ab, wo sie sind: am Smartphone.
            </p>

            <ul class="space-y-3 text-xs sm:text-sm text-slate-300">
              <li class="flex items-start gap-2.5">
                <i data-lucide="check" class="w-4 h-4 text-emerald-400 shrink-0 mt-0.5"></i>
                <span><strong>Bewerbung in 4 Klicks:</strong> Führerschein, Gesellenbrief und Erfahrung direkt antippen – ganz ohne PDF-Upload.</span>
              </li>
              <li class="flex items-start gap-2.5">
                <i data-lucide="check" class="w-4 h-4 text-emerald-400 shrink-0 mt-0.5"></i>
                <span><strong>Werkzeug- &amp; Fuhrpark-Fokus:</strong> Zeigt Ihren modernen Fuhrpark, Markenwerkzeug und faire Arbeitsbedingungen in OWL.</span>
              </li>
              <li class="flex items-start gap-2.5">
                <i data-lucide="check" class="w-4 h-4 text-emerald-400 shrink-0 mt-0.5"></i>
                <span><strong>Fahrzeug-QR-Codes:</strong> Druckfertige Vorlagen für Ihre Firmenwagen – Gesellen anderer Firmen scannen an der Ampel.</span>
              </li>
            </ul>
          </div>

          <div class="pt-4 border-t border-slate-800 flex items-center justify-between text-xs font-bold">
            <span class="text-slate-400">Messbarer Effekt:</span>
            <span class="text-emerald-400 font-mono">Bewerbungseingang in unter 60 Sekunden</span>
          </div>
        </div>

      </div>
    </section>

                <!-- ══════════════════════════════════════════════ -->
    <!-- 4. DIE VERGLEICHSTABELLE: AUFTRAGS-MAGNET GOOGLE (COMPACT) -->
    <!-- ══════════════════════════════════════════════ -->
    <section id="google-magnet" data-aos="fade-up" class="space-y-6 scroll-mt-24">
      
      <!-- Section Header -->
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider block">Lokale Google-Suchanalyse für Bielefeld &amp; OWL</span>
        <h2 class="text-xl sm:text-3xl font-extrabold text-ink-950 tracking-tight">
          Auftrags-Magnet bei Google: Wonach Ihre Wunschkunden in OWL suchen
        </h2>
        <p class="text-xs sm:text-sm text-ink-600 leading-relaxed max-w-xl mx-auto">
          Es gibt Suchanfragen, die kosten Sie nur Zeit und Nerven – und es gibt lokale Suchbegriffe mit fünfstelligem Auftragswert. Im SparrenWeb Meister-System richten wir Ihre Website exakt auf die ertragreichen Aufträge aus.
        </p>
      </div>

      <!-- Interactive Table Filter & Control Bar -->
      <div class="max-w-4xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3 px-1">
        <!-- Trade Filter Tabs (Segmented Control Dock) -->
        <div class="p-1 bg-slate-100 rounded-xl border border-slate-200/80 inline-flex items-center gap-1 shadow-inner overflow-x-auto max-w-full">
          <button type="button" onclick="filterTableTrade('all')" class="table-trade-btn active px-3 py-1 rounded-lg text-xs font-bold bg-[#2563EB] text-white transition-all shadow-xs flex items-center gap-1.5 whitespace-nowrap cursor-pointer" data-target="all">
            <i data-lucide="layout-grid" class="w-3.5 h-3.5"></i>
            <span>Alle 4 Gewerke</span>
          </button>
          <button type="button" onclick="filterTableTrade('shk')" class="table-trade-btn px-3 py-1 rounded-lg text-xs font-semibold text-slate-600 hover:text-ink-950 hover:bg-white/80 transition-all flex items-center gap-1.5 whitespace-nowrap cursor-pointer" data-target="shk">
            <i data-lucide="flame" class="w-3.5 h-3.5 text-orange-500"></i>
            <span>SHK &amp; Bad</span>
          </button>
          <button type="button" onclick="filterTableTrade('dach')" class="table-trade-btn px-3 py-1 rounded-lg text-xs font-semibold text-slate-600 hover:text-ink-950 hover:bg-white/80 transition-all flex items-center gap-1.5 whitespace-nowrap cursor-pointer" data-target="dach">
            <i data-lucide="hammer" class="w-3.5 h-3.5 text-amber-500"></i>
            <span>Dach &amp; Holz</span>
          </button>
          <button type="button" onclick="filterTableTrade('elektro')" class="table-trade-btn px-3 py-1 rounded-lg text-xs font-semibold text-slate-600 hover:text-ink-950 hover:bg-white/80 transition-all flex items-center gap-1.5 whitespace-nowrap cursor-pointer" data-target="elektro">
            <i data-lucide="zap" class="w-3.5 h-3.5 text-blue-500"></i>
            <span>Elektro &amp; PV</span>
          </button>
          <button type="button" onclick="filterTableTrade('tischler')" class="table-trade-btn px-3 py-1 rounded-lg text-xs font-semibold text-slate-600 hover:text-ink-950 hover:bg-white/80 transition-all flex items-center gap-1.5 whitespace-nowrap cursor-pointer" data-target="tischler">
            <i data-lucide="ruler" class="w-3.5 h-3.5 text-emerald-500"></i>
            <span>Tischler &amp; Raum</span>
          </button>
        </div>

        <!-- Animated Physical Filter Simulation Switch -->
        <button type="button" onclick="toggleTableFilterSimulation()" id="table-filter-toggle-btn" class="group flex items-center gap-2 px-3 py-1 rounded-xl bg-emerald-50 border border-emerald-300 text-emerald-800 text-[11px] font-mono font-bold hover:bg-emerald-100 transition-all shadow-2xs cursor-pointer shrink-0">
          <span class="relative flex h-2 w-2">
            <span id="toggle-pulse" class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span id="toggle-dot" class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span id="table-filter-toggle-text">Vorab-Filter: Aktiv</span>
          <div id="toggle-switch-track" class="w-6 h-3 bg-emerald-500 rounded-full p-0.5 transition-colors duration-300 flex items-center justify-end">
            <div id="toggle-switch-thumb" class="w-2 h-2 bg-white rounded-full shadow-2xs transition-transform duration-300"></div>
          </div>
        </button>
      </div>

      <!-- COMPACT DESKTOP COMPARISON TABLE (Hidden on mobile < md) -->
      <div class="hidden md:block max-w-4xl mx-auto bg-white rounded-2xl border border-slate-200 shadow-md overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full table-fixed text-left border-collapse">
            <colgroup>
              <col class="w-[24%]">
              <col class="w-[28%]">
              <col class="w-[32%]">
              <col class="w-[16%]">
            </colgroup>
            <thead>
              <tr class="bg-slate-900 text-white text-[11px] uppercase font-mono tracking-wider border-b border-slate-800">
                <th class="py-2.5 px-4 font-semibold text-slate-300">
                  <div class="flex items-center gap-1.5">
                    <i data-lucide="briefcase" class="w-3.5 h-3.5 text-blue-400"></i>
                    <span>Gewerk &amp; Region</span>
                  </div>
                </th>
                <th class="py-2.5 px-4 font-semibold text-rose-300">
                  <div class="flex items-center gap-1.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
                    <span>Kleinstaufträge (Hoher Aufwand)</span>
                  </div>
                </th>
                <th class="py-2.5 px-4 font-semibold text-emerald-300">
                  <div class="flex items-center gap-1.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                    <span>Wunschkunden (Google Rang #1)</span>
                  </div>
                </th>
                <th class="py-2.5 px-4 font-semibold text-slate-200">
                  <div class="flex items-center gap-1.5 text-slate-300">
                    <i data-lucide="trending-up" class="w-3.5 h-3.5 text-emerald-400"></i>
                    <span>Auftragswert</span>
                  </div>
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 text-xs text-slate-800">
              
              <!-- ROW 1: SHK -->
              <tr id="row-shk" class="table-trade-row hover:bg-slate-50/80 transition-colors group">
                <td class="py-3 px-4 align-top">
                  <div class="flex items-start gap-2.5">
                    <div class="w-7 h-7 rounded-lg bg-orange-50 border border-orange-200/60 text-orange-600 flex items-center justify-center font-bold shrink-0 mt-0.5">
                      <i data-lucide="flame" class="w-3.5 h-3.5"></i>
                    </div>
                    <div>
                      <div class="font-bold text-slate-900 text-xs sm:text-[13px] leading-tight">Sanitär &amp; Heizung</div>
                      <div class="text-[10px] font-mono text-slate-400 mt-0.5">Bielefeld &amp; OWL</div>
                    </div>
                  </div>
                </td>
                <td class="py-3 px-4 align-top space-y-1.5">
                  <div class="space-y-0.5 text-xs text-slate-500">
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Wasserhahn tropft Bielefeld</span></div>
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Dichtung austauschen Kosten</span></div>
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Notdienst Sonntag billig</span></div>
                  </div>
                  <div>
                    <span class="table-filter-status inline-flex items-center gap-1 text-[10px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80" data-active-text="Automatisch ausgefiltert">
                      <i data-lucide="shield-check" class="w-3 h-3 text-emerald-600"></i>
                      <span>Automatisch ausgefiltert</span>
                    </span>
                  </div>
                </td>
                <td class="py-3 px-4 align-top">
                  <div class="space-y-1 text-xs">
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Wärmepumpe Altbau Bielefeld</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Badsanierung Fachbetrieb GT</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Heizungstausch KfW OWL</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                  </div>
                </td>
                <td class="py-3 px-4 align-top">
                  <div class="space-y-0.5">
                    <div class="font-extrabold text-xs sm:text-[13px] text-emerald-700 font-mono tracking-tight whitespace-nowrap">15k – 35k €</div>
                    <div class="text-[10px] text-slate-500 font-mono">DB ~68 %</div>
                    <div class="text-[9px] font-mono font-bold text-blue-600 pt-0.5">Refinanziert Website</div>
                  </div>
                </td>
              </tr>

              <!-- ROW 2: DACH -->
              <tr id="row-dach" class="table-trade-row hover:bg-slate-50/80 transition-colors group">
                <td class="py-3 px-4 align-top">
                  <div class="flex items-start gap-2.5">
                    <div class="w-7 h-7 rounded-lg bg-amber-50 border border-amber-200/60 text-amber-600 flex items-center justify-center font-bold shrink-0 mt-0.5">
                      <i data-lucide="hammer" class="w-3.5 h-3.5"></i>
                    </div>
                    <div>
                      <div class="font-bold text-slate-900 text-xs sm:text-[13px] leading-tight">Dach &amp; Zimmerei</div>
                      <div class="text-[10px] font-mono text-slate-400 mt-0.5">Herford &amp; Bünde</div>
                    </div>
                  </div>
                </td>
                <td class="py-3 px-4 align-top space-y-1.5">
                  <div class="space-y-0.5 text-xs text-slate-500">
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Einzelner Dachziegel locker</span></div>
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Dachrinne reinigen günstig</span></div>
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Dachpappe kleben Anleitung</span></div>
                  </div>
                  <div>
                    <span class="table-filter-status inline-flex items-center gap-1 text-[10px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80" data-active-text="Keine Leerfahrten unter 1.500 €">
                      <i data-lucide="shield-check" class="w-3 h-3 text-emerald-600"></i>
                      <span>Keine Leerfahrten &lt;1.500 €</span>
                    </span>
                  </div>
                </td>
                <td class="py-3 px-4 align-top">
                  <div class="space-y-1 text-xs">
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Energetische Dachsanierung BI</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Zimmerei Dachstuhl Neubau HF</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Flachdachabdichtung OWL</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                  </div>
                </td>
                <td class="py-3 px-4 align-top">
                  <div class="space-y-0.5">
                    <div class="font-extrabold text-xs sm:text-[13px] text-emerald-700 font-mono tracking-tight whitespace-nowrap">20k – 60k €</div>
                    <div class="text-[10px] text-slate-500 font-mono">DB ~72 %</div>
                    <div class="text-[9px] font-mono font-bold text-blue-600 pt-0.5">Großprojekte</div>
                  </div>
                </td>
              </tr>

              <!-- ROW 3: ELEKTRO -->
              <tr id="row-elektro" class="table-trade-row hover:bg-slate-50/80 transition-colors group">
                <td class="py-3 px-4 align-top">
                  <div class="flex items-start gap-2.5">
                    <div class="w-7 h-7 rounded-lg bg-blue-50 border border-blue-200/60 text-blue-600 flex items-center justify-center font-bold shrink-0 mt-0.5">
                      <i data-lucide="zap" class="w-3.5 h-3.5"></i>
                    </div>
                    <div>
                      <div class="font-bold text-slate-900 text-xs sm:text-[13px] leading-tight">Elektro &amp; PV</div>
                      <div class="text-[10px] font-mono text-slate-400 mt-0.5">Bielefeld &amp; Senne</div>
                    </div>
                  </div>
                </td>
                <td class="py-3 px-4 align-top space-y-1.5">
                  <div class="space-y-0.5 text-xs text-slate-500">
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Lichtschalter defekt Hilfe</span></div>
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Kabel verlegen Meterpreis</span></div>
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Elektriker sofort billig</span></div>
                  </div>
                  <div>
                    <span class="table-filter-status inline-flex items-center gap-1 text-[10px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80" data-active-text="Foto-Upload sortiert Kleinkram aus">
                      <i data-lucide="shield-check" class="w-3 h-3 text-emerald-600"></i>
                      <span>Filtert Kleinkram aus</span>
                    </span>
                  </div>
                </td>
                <td class="py-3 px-4 align-top">
                  <div class="space-y-1 text-xs">
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Photovoltaik Speicher Bielefeld</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Wallbox Installation Gewerbe OWL</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Zählerschrank Modernisierung</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                  </div>
                </td>
                <td class="py-3 px-4 align-top">
                  <div class="space-y-0.5">
                    <div class="font-extrabold text-xs sm:text-[13px] text-emerald-700 font-mono tracking-tight whitespace-nowrap">8k – 25k €</div>
                    <div class="text-[10px] text-slate-500 font-mono">DB ~65 %</div>
                    <div class="text-[9px] font-mono font-bold text-blue-600 pt-0.5">PV &amp; Zähler</div>
                  </div>
                </td>
              </tr>

              <!-- ROW 4: TISCHLER -->
              <tr id="row-tischler" class="table-trade-row hover:bg-slate-50/80 transition-colors group">
                <td class="py-3 px-4 align-top">
                  <div class="flex items-start gap-2.5">
                    <div class="w-7 h-7 rounded-lg bg-emerald-50 border border-emerald-200/60 text-emerald-600 flex items-center justify-center font-bold shrink-0 mt-0.5">
                      <i data-lucide="ruler" class="w-3.5 h-3.5"></i>
                    </div>
                    <div>
                      <div class="font-bold text-slate-900 text-xs sm:text-[13px] leading-tight">Tischlerei &amp; Möbel</div>
                      <div class="text-[10px] font-mono text-slate-400 mt-0.5">Detmold &amp; Lemgo</div>
                    </div>
                  </div>
                </td>
                <td class="py-3 px-4 align-top space-y-1.5">
                  <div class="space-y-0.5 text-xs text-slate-500">
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Ikea Schrank aufbauen Bielefeld</span></div>
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Holztür einstellen günstig</span></div>
                    <div class="table-red-keyword flex items-center gap-1.5"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span class="line-through">Möbel reparieren lassen</span></div>
                  </div>
                  <div>
                    <span class="table-filter-status inline-flex items-center gap-1 text-[10px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80" data-active-text="Mindestvolumen ab 2.500 € filtert Preisfüchse">
                      <i data-lucide="shield-check" class="w-3 h-3 text-emerald-600"></i>
                      <span>Volumen &gt;2.500 €</span>
                    </span>
                  </div>
                </td>
                <td class="py-3 px-4 align-top">
                  <div class="space-y-1 text-xs">
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Einbauschrank Maß Dachschräge</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Massivholz Manufaktur Detmold</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                    <div class="flex items-center justify-between gap-1.5 text-slate-900">
                      <span class="font-medium flex items-center gap-1.5 min-w-0"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i><span class="truncate">Objektausbau Praxis Bielefeld</span></span>
                      <span class="text-[9px] font-mono font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200/80 shrink-0">Rang #1</span>
                    </div>
                  </div>
                </td>
                <td class="py-3 px-4 align-top">
                  <div class="space-y-0.5">
                    <div class="font-extrabold text-xs sm:text-[13px] text-emerald-700 font-mono tracking-tight whitespace-nowrap">5k – 30k €</div>
                    <div class="text-[10px] text-slate-500 font-mono">DB ~75 %</div>
                    <div class="text-[9px] font-mono font-bold text-blue-600 pt-0.5">Maßkunden</div>
                  </div>
                </td>
              </tr>

            </tbody>
          </table>
        </div>
      </div>

      <!-- COMPACT MOBILE CARDS (Visible only on mobile < md) -->
      <div class="md:hidden space-y-3 max-w-lg mx-auto">
        
        <!-- Mobile Card 1: SHK -->
        <div id="mobile-card-shk" data-trade="shk" class="mobile-table-card bg-white rounded-xl p-3.5 border border-slate-200 shadow-xs space-y-2.5 text-left">
          <div class="flex items-center justify-between border-b border-slate-100 pb-2">
            <div class="flex items-center gap-2">
              <div class="w-7 h-7 rounded-lg bg-orange-50 border border-orange-200/60 text-orange-600 flex items-center justify-center font-bold shrink-0">
                <i data-lucide="flame" class="w-3.5 h-3.5"></i>
              </div>
              <div>
                <h3 class="font-bold text-slate-900 text-xs">Sanitär &amp; Heizung</h3>
                <span class="text-[10px] font-mono text-slate-400">Bielefeld &amp; OWL</span>
              </div>
            </div>
            <span class="text-[11px] font-mono font-extrabold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 shrink-0">
              15k–35k €
            </span>
          </div>

          <div class="space-y-1 text-[11px] text-slate-500 mobile-red-keyword">
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Wasserhahn tropft Bielefeld</span></div>
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Dichtung austauschen Kosten</span></div>
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Notdienst Sonntag billig</span></div>
          </div>

          <div class="space-y-1 text-xs text-slate-800 pt-1 border-t border-slate-100">
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Wärmepumpe Altbau Bielefeld</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Badsanierung Fachbetrieb GT</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Heizungstausch KfW OWL</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
          </div>

          <div class="pt-1.5 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-500 font-mono">
            <span>DB: <strong class="text-emerald-700">~68 %</strong></span>
            <span class="text-blue-600 font-bold">Refinanziert Website</span>
          </div>
        </div>

        <!-- Mobile Card 2: Dach -->
        <div id="mobile-card-dach" data-trade="dach" class="mobile-table-card bg-white rounded-xl p-3.5 border border-slate-200 shadow-xs space-y-2.5 text-left">
          <div class="flex items-center justify-between border-b border-slate-100 pb-2">
            <div class="flex items-center gap-2">
              <div class="w-7 h-7 rounded-lg bg-amber-50 border border-amber-200/60 text-amber-600 flex items-center justify-center font-bold shrink-0">
                <i data-lucide="hammer" class="w-3.5 h-3.5"></i>
              </div>
              <div>
                <h3 class="font-bold text-slate-900 text-xs">Dach &amp; Zimmerei</h3>
                <span class="text-[10px] font-mono text-slate-400">Herford &amp; Bünde</span>
              </div>
            </div>
            <span class="text-[11px] font-mono font-extrabold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 shrink-0">
              20k–60k €
            </span>
          </div>

          <div class="space-y-1 text-[11px] text-slate-500 mobile-red-keyword">
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Einzelner Dachziegel locker</span></div>
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Dachrinne reinigen günstig</span></div>
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Dachpappe kleben Anleitung</span></div>
          </div>

          <div class="space-y-1 text-xs text-slate-800 pt-1 border-t border-slate-100">
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Energetische Dachsanierung BI</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Zimmerei Dachstuhl Neubau HF</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Flachdachabdichtung OWL</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
          </div>

          <div class="pt-1.5 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-500 font-mono">
            <span>DB: <strong class="text-emerald-700">~72 %</strong></span>
            <span class="text-blue-600 font-bold">Großprojekte</span>
          </div>
        </div>

        <!-- Mobile Card 3: Elektro -->
        <div id="mobile-card-elektro" data-trade="elektro" class="mobile-table-card bg-white rounded-xl p-3.5 border border-slate-200 shadow-xs space-y-2.5 text-left">
          <div class="flex items-center justify-between border-b border-slate-100 pb-2">
            <div class="flex items-center gap-2">
              <div class="w-7 h-7 rounded-lg bg-blue-50 border border-blue-200/60 text-blue-600 flex items-center justify-center font-bold shrink-0">
                <i data-lucide="zap" class="w-3.5 h-3.5"></i>
              </div>
              <div>
                <h3 class="font-bold text-slate-900 text-xs">Elektro &amp; PV</h3>
                <span class="text-[10px] font-mono text-slate-400">Bielefeld &amp; Senne</span>
              </div>
            </div>
            <span class="text-[11px] font-mono font-extrabold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 shrink-0">
              8k–25k €
            </span>
          </div>

          <div class="space-y-1 text-[11px] text-slate-500 mobile-red-keyword">
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Lichtschalter defekt Hilfe</span></div>
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Kabel verlegen Meterpreis</span></div>
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Elektriker sofort billig</span></div>
          </div>

          <div class="space-y-1 text-xs text-slate-800 pt-1 border-t border-slate-100">
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Photovoltaik Speicher Bielefeld</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Wallbox Installation Gewerbe OWL</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Zählerschrank Modernisierung</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
          </div>

          <div class="pt-1.5 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-500 font-mono">
            <span>DB: <strong class="text-emerald-700">~65 %</strong></span>
            <span class="text-blue-600 font-bold">PV &amp; Zähler</span>
          </div>
        </div>

        <!-- Mobile Card 4: Tischler -->
        <div id="mobile-card-tischler" data-trade="tischler" class="mobile-table-card bg-white rounded-xl p-3.5 border border-slate-200 shadow-xs space-y-2.5 text-left">
          <div class="flex items-center justify-between border-b border-slate-100 pb-2">
            <div class="flex items-center gap-2">
              <div class="w-7 h-7 rounded-lg bg-emerald-50 border border-emerald-200/60 text-emerald-600 flex items-center justify-center font-bold shrink-0">
                <i data-lucide="ruler" class="w-3.5 h-3.5"></i>
              </div>
              <div>
                <h3 class="font-bold text-slate-900 text-xs">Tischlerei &amp; Möbel</h3>
                <span class="text-[10px] font-mono text-slate-400">Detmold &amp; Lemgo</span>
              </div>
            </div>
            <span class="text-[11px] font-mono font-extrabold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 shrink-0">
              5k–30k €
            </span>
          </div>

          <div class="space-y-1 text-[11px] text-slate-500 mobile-red-keyword">
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Ikea Schrank aufbauen Bielefeld</span></div>
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Holztür einstellen günstig</span></div>
            <div class="flex items-center gap-1.5 line-through"><i data-lucide="x" class="w-3 h-3 text-rose-500 shrink-0"></i><span>Möbel reparieren lassen</span></div>
          </div>

          <div class="space-y-1 text-xs text-slate-800 pt-1 border-t border-slate-100">
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Einbauschrank Maß Dachschräge</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Massivholz Manufaktur Detmold</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
            <div class="flex items-center justify-between gap-1 text-[11px]">
              <span class="font-medium flex items-center gap-1.5 truncate"><i data-lucide="search" class="w-3 h-3 text-emerald-600 shrink-0"></i>Objektausbau Praxis Bielefeld</span>
              <span class="text-[9px] font-mono text-emerald-700 font-bold bg-emerald-50 px-1 rounded border border-emerald-200 shrink-0">Rang #1</span>
            </div>
          </div>

          <div class="pt-1.5 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-500 font-mono">
            <span>DB: <strong class="text-emerald-700">~75 %</strong></span>
            <span class="text-blue-600 font-bold">Maßkunden</span>
          </div>
        </div>

      </div>

      <!-- Bottom Advantage Banner (Compact) -->
      <div class="p-4 sm:p-5 rounded-2xl bg-white border border-slate-200/90 shadow-2xs text-slate-800 space-y-2.5 max-w-4xl mx-auto text-center">
        <span class="text-[11px] font-mono font-bold text-[#2563EB] uppercase tracking-wider block">Fest integriert im SparrenWeb Meister-System</span>
        <p class="text-xs text-slate-600 leading-relaxed max-w-xl mx-auto">
          <strong>Ihr Vorteil bei SparrenWeb:</strong> Alle Fachtexte, Meta-Beschreibungen und Google-Strukturdaten (Schema.org) sind im Meister-System (2.800 € netto) sowie im Pilot-Paket (1.500 € netto) bereits auf diese ertragsstarken Suchbegriffe in Bielefeld &amp; OWL optimiert.
        </p>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 text-[11px] font-mono text-slate-700">
          <div class="p-2 rounded-lg bg-slate-50 border border-slate-200/80 flex items-center justify-center gap-1 font-bold">
            <i data-lucide="check" class="w-3 h-3 text-emerald-600"></i>
            <span>Schema.org Daten</span>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border border-slate-200/80 flex items-center justify-center gap-1 font-bold">
            <i data-lucide="check" class="w-3 h-3 text-emerald-600"></i>
            <span>Google Maps SEO</span>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border border-slate-200/80 flex items-center justify-center gap-1 font-bold">
            <i data-lucide="check" class="w-3 h-3 text-emerald-600"></i>
            <span>Fachtexte fertig</span>
          </div>
          <div class="p-2 rounded-lg bg-slate-50 border border-slate-200/80 flex items-center justify-center gap-1 font-bold">
            <i data-lucide="check" class="w-3 h-3 text-emerald-600"></i>
            <span>0 € laufendes Abo</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════ -->
    <!-- 5. NEUE SEKTION: 100 % SCHLÜSSELFERTIG         -->
    <!-- ══════════════════════════════════════════════ -->
    <section data-aos="fade-up" class="space-y-10">
      <div class="text-center max-w-3xl mx-auto space-y-3">
        <h2 class="text-2xl sm:text-4xl font-extrabold text-ink-950">
          100 % schlüsselfertig: Sie müssen keine einzige Zeile Fachtext selbst schreiben
        </h2>
        <p class="text-sm sm:text-base text-ink-600 leading-relaxed">
          Viele Handwerksmeister schieben eine neue Website vor sich her, weil Agenturen seitenlange Textentwürfe verlangen. Bei uns genügt ein kurzes Telefonat – den Rest erledigen wir.
        </p>
      </div>

      <!-- 3 Vertrauens-Boxen -->
      <div class="grid md:grid-cols-3 gap-6 text-left">
        
        <!-- Box 1 -->
        <div class="bg-white rounded-3xl p-7 border border-pastel-sage shadow-xs space-y-3 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-12 h-12 rounded-2xl bg-blue-50 text-[#2563EB] flex items-center justify-center font-bold">
              <i data-lucide="book-open-check" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-ink-950">Fertige Branchen-Vorlagen &amp; Fachbegriffe</h3>
            <p class="text-xs sm:text-sm text-ink-600 leading-relaxed">
              Ob KfW-Förderung, Vorlauftemperaturen, U-Werte, TAB-Zählerstandards oder Holzarten: Wir verwenden echte Handwerker-Sprache, die bei Ihren Kunden Vertrauen und Fachkompetenz stiftet.
            </p>
          </div>
          <div class="pt-2 text-xs font-bold text-emerald-600 flex items-center gap-1 font-mono">
            <i data-lucide="check" class="w-4 h-4"></i>
            <span>Fachlich präzise formuliert</span>
          </div>
        </div>

        <!-- Box 2 -->
        <div class="bg-white rounded-3xl p-7 border border-pastel-sage shadow-xs space-y-3 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-12 h-12 rounded-2xl bg-blue-50 text-[#2563EB] flex items-center justify-center font-bold">
              <i data-lucide="list-filter" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-ink-950">Vordefinierte Filter-Fragen nach Gewerk</h3>
            <p class="text-xs sm:text-sm text-ink-600 leading-relaxed">
              Sie müssen sich keine Gedanken über Formularfelder machen. Wir haben für jedes Gewerk erprobte Fragenkataloge (Fotos, Quadratmeter, Baujahr, Dringlichkeit), die unpassende Anfragen aussortieren.
            </p>
          </div>
          <div class="pt-2 text-xs font-bold text-emerald-600 flex items-center gap-1 font-mono">
            <i data-lucide="check" class="w-4 h-4"></i>
            <span>In der Praxis erprobt</span>
          </div>
        </div>

        <!-- Box 3 -->
        <div class="bg-white rounded-3xl p-7 border border-pastel-sage shadow-xs space-y-3 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-12 h-12 rounded-2xl bg-blue-50 text-[#2563EB] flex items-center justify-center font-bold">
              <i data-lucide="clock" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-ink-950">In 30 Minuten am Telefon abgestimmt</h3>
            <p class="text-xs sm:text-sm text-ink-600 leading-relaxed">
              Ein kurzes Gespräch zu Ihrem Betrieb reicht völlig aus. Wir übernehmen Struktur, Design, Texte und Technik – zum fairen Festpreis ab 1.500 € netto (Pilot) bzw. 2.800 € netto (Meister-System). Kein Mietknebel.
            </p>
          </div>
          <div class="pt-2 text-xs font-bold text-emerald-600 flex items-center gap-1 font-mono">
            <i data-lucide="check" class="w-4 h-4"></i>
            <span>14-Tage-Fertigstellungsziel</span>
          </div>
        </div>

      </div>
    </section>

    <!-- ══════════════════════════════════════════════ -->
    <!-- ABSCHLUSS-CTA-BOX                              -->
    <!-- ══════════════════════════════════════════════ -->
    <section data-aos="card-3d-reveal" class="bg-white rounded-3xl p-8 sm:p-12 border-2 border-[#2563EB]/20 shadow-xl text-center space-y-6 max-w-4xl mx-auto">
      <div class="inline-flex items-center gap-2 bg-blue-50 px-3.5 py-1 rounded-full text-xs font-mono font-bold text-[#2563EB]">
        <i data-lucide="check" class="w-3.5 h-3.5"></i>
        <span>Ihr Gewerk ist dabei</span>
      </div>

      <h2 class="text-2xl sm:text-4xl font-extrabold text-ink-950">
        Wir kennen Ihr Gewerk und Ihre Kunden in Bielefeld &amp; OWL.
      </h2>

      <p class="text-sm sm:text-base text-ink-600 max-w-2xl mx-auto leading-relaxed">
        Ob Dachdecker, SHK, Elektriker, Tischler, Maler oder Metallbauer: Wir texten und strukturieren Ihre Website so, dass Sie sich von der ersten Minute an verstanden fühlen – zum fairen Festpreis ab 1.500 € netto (Pilot) bzw. 2.800 € netto (Meister-System).
      </p>

      <div class="pt-2 flex flex-col sm:flex-row items-center justify-center gap-3">
        <a href="anfrage.html" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-[#2563EB] hover:bg-blue-700 text-white font-semibold text-sm px-6 py-3.5 rounded-full transition-all shadow-md shadow-blue-600/25">
          <span>Kostenlosen Vorab-Entwurf für Ihr Gewerk anfordern</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
        <a href="leistungen.html" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-slate-100 hover:bg-slate-200 text-ink-900 font-semibold text-sm px-6 py-3.5 rounded-full transition-all">
          <span>Alle System-Module im Detail</span>
        </a>
      </div>
    </section>

  </main>

  <script>
    // Tab switching logic for the 4 core trades with animation
    function switchTrade(tradeId) {
      document.querySelectorAll('.trade-pane').forEach(p => p.classList.add('hidden'));
      document.querySelectorAll('.trade-tab-btn').forEach(b => {
        b.className = 'trade-tab-btn px-4 sm:px-6 py-2.5 rounded-full text-xs sm:text-sm font-semibold transition-all flex items-center gap-2 bg-transparent text-slate-700 hover:text-ink-950 hover:bg-white/80';
      });

      const targetPane = document.getElementById('pane-' + tradeId);
      if (targetPane) {
        targetPane.classList.remove('hidden');
        targetPane.style.animation = 'none';
        targetPane.offsetHeight; /* trigger reflow */
        targetPane.style.animation = 'fadeInSlideUp 0.35s cubic-bezier(0.16, 1, 0.3, 1)';
      }

      const targetTab = document.getElementById('tab-' + tradeId);
      if (targetTab) {
        targetTab.className = 'trade-tab-btn active px-4 sm:px-6 py-2.5 rounded-full text-xs sm:text-sm font-bold transition-all shadow-sm flex items-center gap-2 bg-[#2563EB] text-white';
      }

      if (typeof lucide !== 'undefined') lucide.createIcons();
      if (typeof AOS !== 'undefined') AOS.refresh();
    }

    // Interactive 3-step mockup flow with Animated Progress Bar
    function advanceMockup(tradeId, targetStep, selectedOption) {
      const s1 = document.getElementById('mock-' + tradeId + '-s1');
      const s2 = document.getElementById('mock-' + tradeId + '-s2');
      const s3 = document.getElementById('mock-' + tradeId + '-s3');
      const titleEl = document.getElementById('mock-' + tradeId + '-selected-title');
      const progressEl = document.getElementById('mock-' + tradeId + '-progress');
      const stepLabel = document.getElementById('mock-' + tradeId + '-step-label');
      const pctLabel = document.getElementById('mock-' + tradeId + '-pct-label');

      if (selectedOption && titleEl) {
        titleEl.textContent = selectedOption;
      }

      if (s1) s1.classList.add('hidden');
      if (s2) s2.classList.add('hidden');
      if (s3) s3.classList.add('hidden');

      const targetEl = targetStep === 1 ? s1 : (targetStep === 2 ? s2 : s3);
      if (targetEl) {
        targetEl.classList.remove('hidden');
        targetEl.style.animation = 'none';
        targetEl.offsetHeight; /* trigger reflow */
        targetEl.style.animation = 'fadeInSlideUp 0.25s ease-out';
      }

      // Update Animated Progress Bar (Matching Startseite #demo)
      if (progressEl && stepLabel && pctLabel) {
        if (targetStep === 1) {
          progressEl.style.width = '33%';
          stepLabel.textContent = 'Schritt 1 von 3: Vorhaben';
          pctLabel.textContent = '33%';
        } else if (targetStep === 2) {
          progressEl.style.width = '66%';
          stepLabel.textContent = 'Schritt 2 von 3: Eckdaten & Fotos';
          pctLabel.textContent = '66%';
        } else if (targetStep === 3) {
          progressEl.style.width = '100%';
          stepLabel.textContent = 'Schritt 3 von 3: Qualifizierte Übergabe';
          pctLabel.textContent = '100%';
        }
      }

      if (typeof lucide !== 'undefined') lucide.createIcons();
    }

    function resetMockup(tradeId) {
      advanceMockup(tradeId, 1);
    }

            // Comparison Table Trade Filter
    function filterTableTrade(trade) {
      document.querySelectorAll('.table-trade-btn').forEach(btn => {
        if (btn.getAttribute('data-target') === trade) {
          btn.className = 'table-trade-btn active px-3 py-1 rounded-lg text-xs font-bold bg-[#2563EB] text-white transition-all shadow-xs flex items-center gap-1.5 whitespace-nowrap cursor-pointer';
        } else {
          btn.className = 'table-trade-btn px-3 py-1 rounded-lg text-xs font-semibold text-slate-600 hover:text-ink-950 hover:bg-white/80 transition-all flex items-center gap-1.5 whitespace-nowrap cursor-pointer';
        }
      });

      const trades = ['shk', 'dach', 'elektro', 'tischler'];
      trades.forEach(t => {
        const row = document.getElementById('row-' + t);
        if (row) {
          if (trade === 'all' || trade === t) {
            row.classList.remove('hidden');
            row.style.animation = 'none';
            row.offsetHeight; /* trigger reflow */
            row.style.animation = 'fadeInSlideUp 0.25s ease-out';
          } else {
            row.classList.add('hidden');
          }
        }

        const card = document.getElementById('mobile-card-' + t);
        if (card) {
          if (trade === 'all' || trade === t) {
            card.classList.remove('hidden');
            card.style.animation = 'none';
            card.offsetHeight; /* trigger reflow */
            card.style.animation = 'fadeInSlideUp 0.25s ease-out';
          } else {
            card.classList.add('hidden');
          }
        }
      });

      if (typeof lucide !== 'undefined') lucide.createIcons();
    }

    // Comparison Table Filter Simulation Toggle with Physical Switch Animation
    let isTableFilterActive = true;
    function toggleTableFilterSimulation() {
      isTableFilterActive = !isTableFilterActive;
      const toggleBtn = document.getElementById('table-filter-toggle-btn');
      const toggleTrack = document.getElementById('toggle-switch-track');
      const toggleThumb = document.getElementById('toggle-switch-thumb');
      const togglePulse = document.getElementById('toggle-pulse');
      const toggleDot = document.getElementById('toggle-dot');
      const toggleText = document.getElementById('table-filter-toggle-text');
      const redKeywords = document.querySelectorAll('.table-red-keyword span, .mobile-red-keyword span');
      const filterStatuses = document.querySelectorAll('.table-filter-status, .mobile-filter-status');

      if (isTableFilterActive) {
        if (toggleBtn) {
          toggleBtn.className = 'group flex items-center gap-2 px-3 py-1 rounded-xl bg-emerald-50 border border-emerald-300 text-emerald-800 text-[11px] font-mono font-bold hover:bg-emerald-100 transition-all shadow-2xs cursor-pointer shrink-0';
        }
        if (toggleTrack) toggleTrack.className = 'w-6 h-3 bg-emerald-500 rounded-full p-0.5 transition-colors duration-300 flex items-center justify-end';
        if (toggleThumb) toggleThumb.className = 'w-2 h-2 bg-white rounded-full shadow-2xs transition-transform duration-300';
        if (togglePulse) togglePulse.className = 'animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75';
        if (toggleDot) toggleDot.className = 'relative inline-flex rounded-full h-2 w-2 bg-emerald-500';
        if (toggleText) toggleText.textContent = 'Vorab-Filter: Aktiv';

        redKeywords.forEach(el => {
          el.classList.add('line-through');
          el.classList.remove('text-red-700', 'font-extrabold');
        });
        filterStatuses.forEach(el => {
          el.classList.remove('text-amber-800', 'bg-amber-100/80', 'border-amber-300');
          el.classList.add('text-emerald-700', 'bg-emerald-50', 'border-emerald-200');
          const customText = el.getAttribute('data-active-text') || 'Automatisch ausgefiltert';
          el.innerHTML = '<i data-lucide="shield-check" class="w-3 h-3 text-emerald-600 inline"></i> <span>' + customText + '</span>';
        });
      } else {
        if (toggleBtn) {
          toggleBtn.className = 'group flex items-center gap-2 px-3 py-1 rounded-xl bg-amber-50 border border-amber-300 text-amber-800 text-[11px] font-mono font-bold hover:bg-amber-100 transition-all shadow-2xs cursor-pointer shrink-0';
        }
        if (toggleTrack) toggleTrack.className = 'w-6 h-3 bg-amber-400 rounded-full p-0.5 transition-colors duration-300 flex items-center justify-start';
        if (toggleThumb) toggleThumb.className = 'w-2 h-2 bg-white rounded-full shadow-2xs transition-transform duration-300';
        if (togglePulse) togglePulse.className = 'animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75';
        if (toggleDot) toggleDot.className = 'relative inline-flex rounded-full h-2 w-2 bg-amber-500';
        if (toggleText) toggleText.textContent = 'Filter pausiert';

        redKeywords.forEach(el => {
          el.classList.remove('line-through');
          el.classList.add('text-red-700', 'font-extrabold');
        });
        filterStatuses.forEach(el => {
          el.classList.remove('text-emerald-700', 'bg-emerald-50', 'border-emerald-200');
          el.classList.add('text-amber-800', 'bg-amber-100/80', 'border-amber-300');
          el.innerHTML = '<i data-lucide="alert-triangle" class="w-3 h-3 text-amber-600 inline"></i> <span>Ungefiltert!</span>';
        });
      }

      if (typeof lucide !== 'undefined') lucide.createIcons();
    }

    document.addEventListener('DOMContentLoaded', () => {
      if (typeof lucide !== 'undefined') lucide.createIcons();
    });
  </script>
"""

with open('gewerke.html', 'w') as f:
    f.write(head + navbar + body_content + footer)

print("Generated gewerke.html successfully with all 5 new sections & interactive mockups.")
