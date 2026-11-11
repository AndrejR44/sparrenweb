#!/usr/bin/env python3
"""
generate_anfrage.py
Generiert anfrage.html vollständig konsistent zur neuen Preis- und Angebotsstruktur:
- 4-Stufen-Funnel mit den neuen Paketen:
  * Angebot A: OWL-Referenz-Pilot (1.500 € netto · 3 Plätze)
  * Angebot B: SparrenWeb Meister-System (2.800 € netto · Bestseller)
  * Angebot E: Komplett-Kombi (3.500 € netto · 500 € Vorteil)
  * Angebot D: 60-Sek.-Recruiting-Modul (1.200 € netto)
  * Unverbindliche Beratung
- Neue Betriebs-Felder: Mitarbeiteranzahl, Website-Status, URL optional
- Keine vorausgewählte Monatsbetreuung
- Saubere Validierung & animierte Schrittwechsel
"""

import builder_helper

def build_anfrage():
    title = "System-Entwurf anfordern | SparrenWeb Bielefeld & OWL"
    description = "In 4 Schritten zum unverbindlichen System-Entwurf für Ihren Handwerksbetrieb in Bielefeld & OWL. 100 % risikofrei ohne Kaufverpflichtung."
    canonical = "anfrage.html"

    head = builder_helper.get_head(title, description, canonical)
    navbar = builder_helper.get_navbar("anfrage.html")
    footer = builder_helper.get_footer()

    main_html = """
  <!-- Hero Section -->
  <header class="pt-32 sm:pt-40 pb-12 sm:pb-16 px-4 sm:px-6 relative overflow-hidden bg-white border-b border-slate-200 hero-bg">
    <div class="max-w-4xl mx-auto text-center space-y-4 relative z-10">
      <div data-aos="fade-down" class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-200/80 text-blue-700 text-xs font-mono font-bold tracking-wider uppercase mb-1 shadow-2xs">
        <span class="w-2 h-2 rounded-full bg-[#2563EB] animate-pulse"></span>
        100 % unverbindlich · Vorab-Entwurf zur Ansicht
      </div>

      <h1 data-aos="fade-up" data-aos-duration="700" class="text-3xl sm:text-5xl font-extrabold text-[#0F172A] tracking-tight leading-tight">
        In 4 Schritten zu Ihrem <span class="text-[#2563EB]">System-Entwurf</span>
      </h1>

      <p data-aos="fade-up" data-aos-delay="100" data-aos-duration="700" class="text-sm sm:text-base text-[#475569] max-w-xl mx-auto leading-relaxed">
        Beantworten Sie uns 4 kurze Fragen zu Ihrem Handwerksbetrieb. Wir erstellen Ihnen einen individuellen Website-Entwurf mit Vorabfilter – ohne Kaufverpflichtung.
      </p>
    </div>
  </header>

  <main class="py-12 px-4 sm:px-6 max-w-3xl mx-auto space-y-12">

    <!-- Interactive 4-Step Funnel Card -->
    <div data-aos="fade-up" class="bg-white rounded-3xl border border-slate-200 shadow-xl p-6 sm:p-10 space-y-8 relative overflow-hidden card-lift">
      
      <!-- Progress Bar & Step Counter -->
      <div class="space-y-3">
        <div class="flex justify-between items-center text-xs font-mono font-bold">
          <span id="funnel-step-name" class="text-[#0F172A] uppercase tracking-wide flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-[#2563EB]"></span>
            <span>Schritt 1: Ihr Gewerk</span>
          </span>
          <span id="funnel-step-num" class="text-[#2563EB] bg-blue-50 px-2.5 py-0.5 rounded-full border border-blue-200">1 von 4</span>
        </div>
        <div class="w-full bg-slate-100 h-2.5 rounded-full overflow-hidden p-0.5 border border-slate-200/60">
          <div id="funnel-bar" class="bg-gradient-to-r from-blue-600 to-[#2563EB] h-full rounded-full transition-all duration-400 ease-out" style="width: 25%;"></div>
        </div>
      </div>

      <form id="funnelForm" onsubmit="submitFunnel(event)">
        
        <!-- SCHRITT 1: GEWERK AUSWÄHLEN -->
        <div id="step-1" class="funnel-step space-y-5 animate-step">
          <div class="space-y-1">
            <h2 class="text-lg sm:text-xl font-bold text-[#0F172A]">1. Welchem Gewerk gehört Ihr Betrieb an?</h2>
            <p class="text-xs text-[#475569]">Wir passen Struktur und Fachtexte exakt an Ihre Branche in Bielefeld &amp; OWL an.</p>
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-[#2563EB] has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/50 transition-all flex flex-col items-center text-center space-y-2 group shadow-2xs">
              <input type="radio" name="trade" value="Dachdecker & Zimmerei" class="hidden" onchange="enableNext(1)">
              <div class="w-10 h-10 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center group-hover:scale-110 transition-transform">
                <i data-lucide="hammer" class="w-5 h-5"></i>
              </div>
              <span class="text-xs font-bold text-[#0F172A]">Dach &amp; Zimmerei</span>
            </label>

            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-[#2563EB] has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/50 transition-all flex flex-col items-center text-center space-y-2 group shadow-2xs">
              <input type="radio" name="trade" value="Sanitär, Heizung & Klima (SHK)" class="hidden" onchange="enableNext(1)">
              <div class="w-10 h-10 rounded-xl bg-orange-50 text-orange-600 flex items-center justify-center group-hover:scale-110 transition-transform">
                <i data-lucide="flame" class="w-5 h-5"></i>
              </div>
              <span class="text-xs font-bold text-[#0F172A]">SHK &amp; Bad</span>
            </label>

            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-[#2563EB] has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/50 transition-all flex flex-col items-center text-center space-y-2 group shadow-2xs">
              <input type="radio" name="trade" value="Elektrotechnik & PV" class="hidden" onchange="enableNext(1)">
              <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center group-hover:scale-110 transition-transform">
                <i data-lucide="zap" class="w-5 h-5"></i>
              </div>
              <span class="text-xs font-bold text-[#0F172A]">Elektro &amp; PV</span>
            </label>

            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-[#2563EB] has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/50 transition-all flex flex-col items-center text-center space-y-2 group shadow-2xs">
              <input type="radio" name="trade" value="Tischlerei & Innenausbau" class="hidden" onchange="enableNext(1)">
              <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center group-hover:scale-110 transition-transform">
                <i data-lucide="ruler" class="w-5 h-5"></i>
              </div>
              <span class="text-xs font-bold text-[#0F172A]">Tischler &amp; Möbel</span>
            </label>

            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-[#2563EB] has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/50 transition-all flex flex-col items-center text-center space-y-2 group shadow-2xs">
              <input type="radio" name="trade" value="Garten- & Landschaftsbau" class="hidden" onchange="enableNext(1)">
              <div class="w-10 h-10 rounded-xl bg-lime-50 text-lime-600 flex items-center justify-center group-hover:scale-110 transition-transform">
                <i data-lucide="trees" class="w-5 h-5"></i>
              </div>
              <span class="text-xs font-bold text-[#0F172A]">GaLaBau</span>
            </label>

            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-[#2563EB] has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/50 transition-all flex flex-col items-center text-center space-y-2 group shadow-2xs">
              <input type="radio" name="trade" value="Metallbau & Schlosserei" class="hidden" onchange="enableNext(1)">
              <div class="w-10 h-10 rounded-xl bg-slate-100 text-slate-700 flex items-center justify-center group-hover:scale-110 transition-transform">
                <i data-lucide="shield" class="w-5 h-5"></i>
              </div>
              <span class="text-xs font-bold text-[#0F172A]">Metallbau</span>
            </label>

            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-[#2563EB] has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/50 transition-all flex flex-col items-center text-center space-y-2 group shadow-2xs">
              <input type="radio" name="trade" value="Maler & Stuckateur" class="hidden" onchange="enableNext(1)">
              <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center group-hover:scale-110 transition-transform">
                <i data-lucide="paint-roller" class="w-5 h-5"></i>
              </div>
              <span class="text-xs font-bold text-[#0F172A]">Maler &amp; Ausbau</span>
            </label>

            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-[#2563EB] has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/50 transition-all flex flex-col items-center text-center space-y-2 group col-span-2 sm:col-span-1 shadow-2xs">
              <input type="radio" name="trade" value="Anderes Gewerk" class="hidden" onchange="enableNext(1)">
              <div class="w-10 h-10 rounded-xl bg-slate-100 text-slate-700 flex items-center justify-center group-hover:scale-110 transition-transform">
                <i data-lucide="wrench" class="w-5 h-5"></i>
              </div>
              <span class="text-xs font-bold text-[#0F172A]">Anderes Gewerk</span>
            </label>
          </div>
        </div>

        <!-- SCHRITT 2: BETRIEBS-ECKDATEN -->
        <div id="step-2" class="funnel-step hidden space-y-5 animate-step">
          <div class="space-y-1">
            <h2 class="text-lg sm:text-xl font-bold text-[#0F172A]">2. Wie ist Ihr Handwerksbetrieb aufgestellt?</h2>
            <p class="text-xs text-[#475569]">Damit passen wir die Vorqualifizierungslogik und Kapazitäten genau an Ihre Betriebsgröße an.</p>
          </div>

          <!-- Mitarbeiterzahl -->
          <div class="space-y-2">
            <label class="block text-xs font-bold text-[#0F172A]">Mitarbeiteranzahl in Ihrem Betrieb:</label>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
              <label class="cursor-pointer p-3 rounded-xl border border-slate-200 text-center hover:border-blue-400 has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/70 transition-all shadow-2xs">
                <input type="radio" name="employees" value="1-3 Mitarbeiter" class="hidden" onchange="checkStep2Complete()">
                <span class="text-xs font-bold text-[#0F172A] block">1–3</span>
                <span class="text-[10px] text-[#64748B]">Mitarbeiter</span>
              </label>
              <label class="cursor-pointer p-3 rounded-xl border border-slate-200 text-center hover:border-blue-400 has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/70 transition-all shadow-2xs">
                <input type="radio" name="employees" value="4-10 Mitarbeiter" checked class="hidden" onchange="checkStep2Complete()">
                <span class="text-xs font-bold text-[#0F172A] block">4–10</span>
                <span class="text-[10px] text-[#64748B]">Mitarbeiter</span>
              </label>
              <label class="cursor-pointer p-3 rounded-xl border border-slate-200 text-center hover:border-blue-400 has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/70 transition-all shadow-2xs">
                <input type="radio" name="employees" value="11-20 Mitarbeiter" class="hidden" onchange="checkStep2Complete()">
                <span class="text-xs font-bold text-[#0F172A] block">11–20</span>
                <span class="text-[10px] text-[#64748B]">Mitarbeiter</span>
              </label>
              <label class="cursor-pointer p-3 rounded-xl border border-slate-200 text-center hover:border-blue-400 has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/70 transition-all shadow-2xs">
                <input type="radio" name="employees" value="20+ Mitarbeiter" class="hidden" onchange="checkStep2Complete()">
                <span class="text-xs font-bold text-[#0F172A] block">20+</span>
                <span class="text-[10px] text-[#64748B]">Mitarbeiter</span>
              </label>
            </div>
          </div>

          <!-- Status der bestehenden Website -->
          <div class="space-y-2">
            <label class="block text-xs font-bold text-[#0F172A]">Status Ihrer aktuellen Webpräsenz:</label>
            <div class="space-y-2">
              <label class="funnel-card cursor-pointer p-3.5 rounded-xl border border-slate-200 hover:border-blue-400 has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/50 flex items-center gap-3 transition-all shadow-2xs">
                <input type="radio" name="webstatus" value="Veraltet / Liefert kaum passende Anfragen" checked class="hidden" onchange="checkStep2Complete()">
                <div class="w-7 h-7 rounded-lg bg-slate-100 flex items-center justify-center text-slate-700 shrink-0">
                  <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                </div>
                <div class="text-xs text-left">
                  <strong class="text-[#0F172A]">Bestehende Website ist veraltet</strong> – liefert zu wenig rentables Geschäft
                </div>
              </label>

              <label class="funnel-card cursor-pointer p-3.5 rounded-xl border border-slate-200 hover:border-blue-400 has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/50 flex items-center gap-3 transition-all shadow-2xs">
                <input type="radio" name="webstatus" value="Nicht mobilfähig / Kein Vorabfilter" class="hidden" onchange="checkStep2Complete()">
                <div class="w-7 h-7 rounded-lg bg-slate-100 flex items-center justify-center text-slate-700 shrink-0">
                  <i data-lucide="smartphone" class="w-3.5 h-3.5"></i>
                </div>
                <div class="text-xs text-left">
                  <strong class="text-[#0F172A]">Schlechte Mobilansicht &amp; kein Foto-Upload</strong> – zu viele Telefonate für Kleinkram
                </div>
              </label>

              <label class="funnel-card cursor-pointer p-3.5 rounded-xl border border-slate-200 hover:border-blue-400 has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/50 flex items-center gap-3 transition-all shadow-2xs">
                <input type="radio" name="webstatus" value="Noch keine eigene Website vorhanden" class="hidden" onchange="checkStep2Complete()">
                <div class="w-7 h-7 rounded-lg bg-slate-100 flex items-center justify-center text-slate-700 shrink-0">
                  <i data-lucide="globe" class="w-3.5 h-3.5"></i>
                </div>
                <div class="text-xs text-left">
                  <strong class="text-[#0F172A]">Noch gar keine Website vorhanden</strong> – schlüsselfertiger Neubeginn
                </div>
              </label>
            </div>
          </div>

          <!-- Optionale Website-URL -->
          <div>
            <label for="existingUrl" class="block text-xs font-bold text-[#0F172A] mb-1">Aktuelle Internetadresse (falls vorhanden):</label>
            <input type="text" id="existingUrl" name="existingUrl" placeholder="z. B. www.meisterbetrieb-owl.de" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs text-[#0F172A] focus:outline-none focus:border-[#2563EB]">
          </div>
        </div>

        <!-- SCHRITT 3: PAKETWAHL -->
        <div id="step-3" class="funnel-step hidden space-y-4 animate-step">
          <div class="space-y-1">
            <h2 class="text-lg sm:text-xl font-bold text-[#0F172A]">3. Welches System-Paket interessiert Sie?</h2>
            <p class="text-xs text-[#475569]">Feste B2B-Nettopreise. Sie entscheiden erst nach Ansicht Ihres unverbindlichen Entwurfs.</p>
          </div>

          <div class="space-y-3">
            
            <!-- Angebot B: Meister-System (Standard) -->
            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-[#2563EB] has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/40 transition-all flex items-center justify-between gap-3 shadow-2xs">
              <div class="flex items-center gap-3">
                <input type="radio" name="package" value="Angebot B: SparrenWeb Meister-System (2.800 € netto)" checked class="hidden" onchange="enableNext(3)">
                <div class="w-10 h-10 rounded-xl bg-blue-100 text-[#2563EB] flex items-center justify-center shrink-0 font-bold font-mono text-xs">
                  2.800
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#0F172A]">SparrenWeb Meister-System (2.800 € netto einmalig)</div>
                  <div class="text-[11px] text-[#475569]">Bis zu 6 Seiten, Fachtexte, Vorabfilter mit Foto-Upload &amp; Google Profil</div>
                </div>
              </div>
              <span class="text-xs font-bold text-[#2563EB] font-mono shrink-0 hidden sm:inline bg-blue-50 px-2 py-0.5 rounded border border-blue-200">Bestseller</span>
            </label>

            <!-- Angebot A: Pilot -->
            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-amber-400 has-[:checked]:border-amber-500 has-[:checked]:bg-amber-50/40 transition-all flex items-center justify-between gap-3 shadow-2xs">
              <div class="flex items-center gap-3">
                <input type="radio" name="package" value="Angebot A: OWL-Referenz-Pilot (1.500 € netto · 3 Plätze)" class="hidden" onchange="enableNext(3)">
                <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center shrink-0 font-bold font-mono text-xs">
                  1.500
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#0F172A]">OWL-Referenz-Pilot (1.500 € netto einmalig)</div>
                  <div class="text-[11px] text-[#475569]">Streng auf 3 Betriebe limitiert gegen gemeinsame Fallstudie</div>
                </div>
              </div>
              <span class="text-xs font-bold text-amber-800 font-mono shrink-0 hidden sm:inline bg-amber-100 px-2 py-0.5 rounded border border-amber-300">3 Plätze</span>
            </label>

            <!-- Angebot E: Komplett-Kombi -->
            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-emerald-400 has-[:checked]:border-emerald-500 has-[:checked]:bg-emerald-50/40 transition-all flex items-center justify-between gap-3 shadow-2xs">
              <div class="flex items-center gap-3">
                <input type="radio" name="package" value="Angebot E: Komplett-Kombi (3.500 € netto · Meister + Recruiting)" class="hidden" onchange="enableNext(3)">
                <div class="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-800 flex items-center justify-center shrink-0 font-bold font-mono text-xs">
                  3.500
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#0F172A]">Komplett-Kombi (3.500 € netto einmalig)</div>
                  <div class="text-[11px] text-[#475569]">Meister-System + 60-Sek.-Recruiting (500 € Nachlass)</div>
                </div>
              </div>
              <span class="text-xs font-bold text-emerald-700 font-mono shrink-0 hidden sm:inline bg-emerald-100 px-2 py-0.5 rounded border border-emerald-300">500 € Vorteil</span>
            </label>

            <!-- Angebot D: Recruiting Einzelmodul -->
            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-blue-400 has-[:checked]:border-[#2563EB] has-[:checked]:bg-blue-50/40 transition-all flex items-center justify-between gap-3 shadow-2xs">
              <div class="flex items-center gap-3">
                <input type="radio" name="package" value="Angebot D: 60-Sek.-Recruiting-Modul (1.200 € netto)" class="hidden" onchange="enableNext(3)">
                <div class="w-10 h-10 rounded-xl bg-slate-100 text-[#0F172A] flex items-center justify-center shrink-0 font-bold font-mono text-xs">
                  1.200
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#0F172A]">60-Sekunden-Recruiting-Modul (1.200 € netto)</div>
                  <div class="text-[11px] text-[#475569]">Mobiles Bewerber-System ohne Lebenslauf + Google Jobs</div>
                </div>
              </div>
            </label>

            <!-- Beratung -->
            <label class="funnel-card cursor-pointer p-4 rounded-2xl border-2 border-slate-200 hover:border-slate-400 has-[:checked]:border-slate-600 has-[:checked]:bg-slate-50 transition-all flex items-center justify-between gap-3 shadow-2xs">
              <div class="flex items-center gap-3">
                <input type="radio" name="package" value="Unverbindlicher Entwurf & individuelle Beratung" class="hidden" onchange="enableNext(3)">
                <div class="w-10 h-10 rounded-xl bg-slate-100 text-slate-700 flex items-center justify-center shrink-0 font-bold font-mono text-xs">
                  Info
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#0F172A]">Erst unverbindlich beraten lassen</div>
                  <div class="text-[11px] text-[#475569]">Im 15-Minuten-Gespräch gemeinsam das ideale Setup finden</div>
                </div>
              </div>
            </label>

          </div>
        </div>

        <!-- SCHRITT 4: KONTAKTDATEN & ABSENDEN -->
        <div id="step-4" class="funnel-step hidden space-y-6 animate-step">
          <div class="space-y-1">
            <h2 class="text-lg sm:text-xl font-bold text-[#0F172A]">4. Wohin dürfen wir Ihren Entwurf senden?</h2>
            <p class="text-xs text-[#475569]">Wir melden uns telefonisch bei Ihnen für eine kurze 15-minütige Abstimmung.</p>
          </div>

          <div class="space-y-3.5 text-left text-xs">
            <div>
              <label for="f-name" class="block font-bold text-[#0F172A] mb-1">Ihr Name &amp; Handwerksbetrieb *</label>
              <input type="text" id="f-name" name="name" required placeholder="z. B. Thomas Meier, Meier Bedachungen e.K." class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-xs text-[#0F172A] focus:outline-none focus:border-[#2563EB]">
            </div>

            <div class="grid sm:grid-cols-2 gap-3.5">
              <div>
                <label for="f-phone" class="block font-bold text-[#0F172A] mb-1">Telefonnummer für Rückruf *</label>
                <input type="tel" id="f-phone" name="phone" required placeholder="z. B. 0521 1234567 oder Mobil" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-xs text-[#0F172A] focus:outline-none focus:border-[#2563EB]">
              </div>
              <div>
                <label for="f-email" class="block font-bold text-[#0F172A] mb-1">E-Mail-Adresse *</label>
                <input type="email" id="f-email" name="email" required placeholder="info@betrieb-owl.de" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-xs text-[#0F172A] focus:outline-none focus:border-[#2563EB]">
              </div>
            </div>

            <div>
              <label for="f-location" class="block font-bold text-[#0F172A] mb-1">PLZ &amp; Ort in Bielefeld / OWL *</label>
              <input type="text" id="f-location" name="location" required placeholder="z. B. 33602 Bielefeld" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-xs text-[#0F172A] focus:outline-none focus:border-[#2563EB]">
            </div>

            <div>
              <label for="f-notes" class="block font-bold text-[#0F172A] mb-1">Zusätzliche Wünsche oder Anmerkungen (optional):</label>
              <textarea id="f-notes" name="notes" rows="2" placeholder="z. B. Wir möchten vor allem Aufträge im Bereich Badsanierung / Wärmepumpe / Steildach vorfiltern..." class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-xs text-[#0F172A] focus:outline-none focus:border-[#2563EB]"></textarea>
            </div>
          </div>

          <!-- Hinweis & Datenschutz -->
          <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 text-[11px] text-[#64748B] leading-relaxed">
            Ihre Angaben werden streng vertraulich ausschließlich zur Kontaktaufnahme und Erstellung Ihres unverbindlichen System-Entwurfs verwendet (keine Werbeanrufe Dritter, kein Spam).
          </div>
        </div>

        <!-- Navigation Buttons -->
        <div class="pt-6 border-t border-slate-200 flex items-center justify-between gap-3">
          <button type="button" id="prevBtn" onclick="prevStep()" class="hidden px-5 py-2.5 rounded-xl border border-slate-300 text-xs font-bold text-[#0F172A] hover:bg-slate-50 transition-all">
            ← Zurück
          </button>
          
          <button type="button" id="nextBtn" onclick="nextStep()" class="ml-auto px-6 py-3 rounded-xl bg-[#2563EB] hover:bg-blue-700 text-white text-xs sm:text-sm font-bold transition-all shadow-md flex items-center gap-2">
            <span>Weiter</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </button>

          <button type="submit" id="submitBtn" class="hidden ml-auto px-6 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs sm:text-sm font-bold transition-all shadow-md flex items-center gap-2">
            <i data-lucide="check" class="w-4 h-4"></i>
            <span>Kostenlosen System-Entwurf anfordern</span>
          </button>
        </div>

      </form>

      <!-- Feedback Confirmation Screen -->
      <div id="funnelFeedback" class="hidden p-6 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-950 space-y-3 text-left">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-full bg-emerald-600 text-white flex items-center justify-center font-bold">
            ✓
          </div>
          <h3 class="text-base font-bold">Vielen Dank für Ihre Anfrage!</h3>
        </div>
        <p class="text-xs text-emerald-900 leading-relaxed">
          Ihre Angaben wurden erfolgreich erfasst. Wir erstellen Ihren unverbindlichen System-Entwurf und melden uns innerhalb von 1–2 Werktagen telefonisch bei Ihnen für die kurze 15-minütige Abstimmung.
        </p>
      </div>

    </div>

  </main>
"""

    script_content = """
<style>
  @keyframes stepFadeIn {
    from {
      opacity: 0;
      transform: translateY(8px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  .animate-step {
    animation: stepFadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) both;
  }
</style>
<script>
  let currentStep = 1;

  function enableNext(step) {
    const nextBtn = document.getElementById('nextBtn');
    if (nextBtn) nextBtn.disabled = false;
  }

  function checkStep2Complete() {
    enableNext(2);
  }

  function nextStep() {
    if (currentStep === 1) {
      const trade = document.querySelector('input[name="trade"]:checked');
      if (!trade) {
        alert('Bitte wählen Sie Ihr Gewerk aus.');
        return;
      }
    }
    
    if (currentStep < 4) {
      document.getElementById(`step-${currentStep}`).classList.add('hidden');
      currentStep++;
      const nextEl = document.getElementById(`step-${currentStep}`);
      nextEl.classList.remove('hidden');
      nextEl.classList.remove('animate-step');
      void nextEl.offsetWidth; // trigger reflow
      nextEl.classList.add('animate-step');
      updateProgress();
    }
  }

  function prevStep() {
    if (currentStep > 1) {
      document.getElementById(`step-${currentStep}`).classList.add('hidden');
      currentStep--;
      const prevEl = document.getElementById(`step-${currentStep}`);
      prevEl.classList.remove('hidden');
      prevEl.classList.remove('animate-step');
      void prevEl.offsetWidth; // trigger reflow
      prevEl.classList.add('animate-step');
      updateProgress();
    }
  }

  function updateProgress() {
    const bar = document.getElementById('funnel-bar');
    const num = document.getElementById('funnel-step-num');
    const name = document.getElementById('funnel-step-name');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.getElementById('submitBtn');

    const pct = (currentStep / 4) * 100;
    if (bar) bar.style.width = pct + '%';
    if (num) num.textContent = `${currentStep} von 4`;

    const stepTitles = [
      'Schritt 1: Ihr Gewerk',
      'Schritt 2: Betriebs-Eckdaten',
      'Schritt 3: Paket-Auswahl',
      'Schritt 4: Kontaktdaten'
    ];
    if (name) {
      name.innerHTML = `<span class="w-2 h-2 rounded-full bg-[#2563EB]"></span><span>${stepTitles[currentStep - 1]}</span>`;
    }

    if (prevBtn) {
      if (currentStep > 1) prevBtn.classList.remove('hidden');
      else prevBtn.classList.add('hidden');
    }

    if (currentStep === 4) {
      if (nextBtn) nextBtn.classList.add('hidden');
      if (submitBtn) submitBtn.classList.remove('hidden');
    } else {
      if (nextBtn) nextBtn.classList.remove('hidden');
      if (submitBtn) submitBtn.classList.add('hidden');
    }

    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }
  }

  async function submitFunnel(e) {
    e.preventDefault();
    const form = document.getElementById('funnelForm');
    const feedback = document.getElementById('funnelFeedback');
    const submitBtn = document.getElementById('submitBtn');

    if (!form) return;

    const origBtnHtml = submitBtn ? submitBtn.innerHTML : '';
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = `
        <span class="inline-block animate-spin mr-1.5">⟳</span>
        <span>Übertrage an CRM...</span>
      `;
    }

    try {
      const formData = new FormData(form);
      const payload = {
        trade: formData.get('trade') || '',
        employees: formData.get('employees') || '',
        webstatus: formData.get('webstatus') || '',
        existingUrl: formData.get('existingUrl') || '',
        package: formData.get('package') || '',
        name: formData.get('name') || '',
        phone: formData.get('phone') || '',
        email: formData.get('email') || '',
        location: formData.get('location') || '',
        notes: formData.get('notes') || '',
        source: 'anfrage.html Funnel'
      };

      const crmApiUrl = window.SPARRENWEB_CRM_URL || 'http://localhost:3000/api/leads';

      const response = await fetch(crmApiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (!response.ok) {
        console.warn('CRM API Status:', response.status);
      } else {
        const result = await response.json();
        console.log('CRM Lead erfolgreich erfasst:', result);
      }
    } catch (err) {
      console.warn('Lokaler CRM-Server pausiert oder nicht erreichbar. Speichere lokal als Fallback:', err);
      try {
        const formData = new FormData(form);
        const offlineQueue = JSON.parse(localStorage.getItem('sparrenweb_offline_leads') || '[]');
        offlineQueue.push({
          timestamp: new Date().toISOString(),
          data: Object.fromEntries(formData.entries())
        });
        localStorage.setItem('sparrenweb_offline_leads', JSON.stringify(offlineQueue));
      } catch (localErr) {
        console.warn('Fallback-Speicherung:', localErr);
      }
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = origBtnHtml;
      }
      if (form) form.classList.add('hidden');
      if (feedback) feedback.classList.remove('hidden');
      window.scrollTo({ top: 200, behavior: 'smooth' });
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    updateProgress();
  });
</script>
"""

    return head + navbar + main_html + script_content + footer

if __name__ == "__main__":
    html = build_anfrage()
    with open("anfrage.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("anfrage.html erfolgreich generiert.")
