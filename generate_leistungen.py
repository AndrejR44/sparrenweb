#!/usr/bin/env python3
"""
generate_leistungen.py
Generiert eine architektonisch anspruchsvolle, hochgradig ästhetische und voll animierte
Angebots- & Leistungsarchitektur-Seite (leistungen.html) für SparrenWeb.

Enthält:
- Hero mit interaktivem Schnellwähler & Vertrauenspfeilern
- Angebot B: Meister-Auftrags-System (2.800 € netto einmalig) mit Zahlungsmodell-Rechner
- Angebot A: OWL-Referenz-Pilot (1.500 € netto einmalig, 3 Betriebe, 50/50 Split) mit dynamischem Kontingentbalken
- Angebot E: Komplett-Kombi (3.500 € netto einmalig, 500 € Vorteil) im edlen Dark-Blue Stage
- Angebot D: 60-Sekunden-Recruiting-Modul (1.200 € netto einmalig) mit interaktiver Smartphone-Bewerbungs-Simulation
- Interaktive Vorabfilter-Demo: Live-Split-Screen (Kunden-Eingabe vs. Meister-Cockpit)
- Angebot C: Regionaler Systembetrieb & Ad-Care mit interaktivem Monats-/Jahreszahler-Umschalter
- Vollständige Funktions- & Leistungs-Vergleichstabelle aller 5 Angebote
- 100 % Eigentumsgarantie & Transparente Leistungsgrenzen
- Interaktives FAQ-Accordion
- Finaler CTA-Banner mit Direktrückruf & Entwurfsanforderung
"""

import builder_helper

def build_leistungen():
    title = "Angebote & Leistungen im Festpreis-Überblick | SparrenWeb Bielefeld & OWL"
    description = "Volle Leistungstransparenz für Meisterbetriebe in Bielefeld & OWL: Meister-Auftrags-System (2.800 € netto), Pilot-Angebot (1.500 € netto), 60s-Recruiting (1.200 € netto) und optionaler Systembetrieb (250 €/Mo). Website-Kauf statt Miete."
    canonical = "leistungen.html"

    head = builder_helper.get_head(title, description, canonical)
    navbar = builder_helper.get_navbar("leistungen.html")
    footer = builder_helper.get_footer()

    main_html = """
<!-- ══════════════════════════════════════════════════════════════ -->
<!-- 1. HERO SECTION: TITEL & SCHNELLWÄHLER                         -->
<!-- ══════════════════════════════════════════════════════════════ -->
<header class="pt-32 sm:pt-40 pb-16 sm:pb-24 px-4 sm:px-6 relative overflow-hidden bg-white border-b border-slate-200 hero-bg">
  <div class="max-w-5xl mx-auto text-center space-y-6 relative z-10">
    
    <div data-aos="fade-down" data-aos-duration="600" class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-200/80 text-blue-700 text-xs font-mono font-bold tracking-wider uppercase mb-1 shadow-2xs">
      <span class="w-2 h-2 rounded-full bg-[#2563EB] animate-pulse"></span>
      Transparente Festpreis-Architektur · Bielefeld &amp; OWL
    </div>

    <h1 data-aos="fade-up" data-aos-duration="750" class="text-3xl sm:text-5xl lg:text-6xl font-extrabold text-[#0F172A] tracking-tight leading-tight">
      Schlüsselfertige Meister-Systeme <br class="hidden sm:inline">
      <span class="text-[#2563EB]">zum transparenten Festpreis</span>
    </h1>

    <p data-aos="fade-up" data-aos-delay="100" data-aos-duration="750" class="text-base sm:text-lg text-[#334155] leading-relaxed max-w-3xl mx-auto">
      Kein intransparentes Agentur-Kauderwelsch, keine monatliche Software-Miete: Bei SparrenWeb erwerben Sie Ihr System als echtes Betriebseigentum. Inklusive Fachtexten, Kunden-Vorabfilter mit Foto-Upload und 5 physischen Google-NFC-Karten.
    </p>

    <!-- Quick Navigation Anchors with Smooth Scroll & Visual Indicator -->
    <div data-aos="fade-up" data-aos-delay="200" data-aos-duration="750" class="pt-2 flex flex-wrap justify-center gap-2 sm:gap-3 text-xs font-semibold">
      <a href="#meister-system" class="px-4 py-2 rounded-full bg-blue-50 border border-blue-300 text-[#2563EB] hover:bg-blue-100 transition-all shadow-xs flex items-center gap-1.5 hover:-translate-y-0.5">
        <span class="w-1.5 h-1.5 rounded-full bg-[#2563EB]"></span>
        <span>Meister-System (2.800 €)</span>
      </a>
      <a href="#pilot" class="px-4 py-2 rounded-full bg-slate-50 border border-slate-200 text-[#0F172A] hover:bg-slate-100 hover:border-amber-300 transition-all shadow-xs flex items-center gap-1.5 hover:-translate-y-0.5">
        <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
        <span>OWL-Pilot (1.500 €)</span>
      </a>
      <a href="#kombi" class="px-4 py-2 rounded-full bg-slate-50 border border-slate-200 text-[#0F172A] hover:bg-slate-100 hover:border-blue-400 transition-all shadow-xs flex items-center gap-1.5 hover:-translate-y-0.5">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
        <span>Komplett-Kombi (3.500 €)</span>
      </a>
      <a href="#recruiting" class="px-4 py-2 rounded-full bg-slate-50 border border-slate-200 text-[#0F172A] hover:bg-slate-100 transition-all shadow-xs flex items-center gap-1.5 hover:-translate-y-0.5">
        <span>60s-Recruiting (1.200 €)</span>
      </a>
      <a href="#vorqualifizierung" class="px-4 py-2 rounded-full bg-slate-50 border border-slate-200 text-[#0F172A] hover:bg-slate-100 transition-all shadow-xs flex items-center gap-1.5 hover:-translate-y-0.5">
        <span>Vorabfilter &amp; Chef-Cockpit</span>
      </a>
      <a href="#systembetrieb" class="px-4 py-2 rounded-full bg-slate-50 border border-slate-200 text-[#0F172A] hover:bg-slate-100 transition-all shadow-xs flex items-center gap-1.5 hover:-translate-y-0.5">
        <span>Systembetrieb (250 €/Mo)</span>
      </a>
      <a href="#vergleich" class="px-4 py-2 rounded-full bg-slate-50 border border-slate-200 text-[#0F172A] hover:bg-slate-100 transition-all shadow-xs flex items-center gap-1.5 hover:-translate-y-0.5">
        <span>Funktions-Vergleich</span>
      </a>
    </div>

    <!-- 4 Concrete Trust Pillars -->
    <div data-aos="fade-up" data-aos-delay="300" data-aos-duration="750" class="pt-6 grid grid-cols-2 md:grid-cols-4 gap-3 text-left">
      <div class="p-4 rounded-2xl bg-white border border-slate-200/90 shadow-xs flex items-start gap-3">
        <div class="w-8 h-8 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center shrink-0 mt-0.5">
          <i data-lucide="shield-check" class="w-4 h-4"></i>
        </div>
        <div>
          <div class="text-xs font-bold text-[#0F172A]">100 % Ihr Eigentum</div>
          <div class="text-[11px] text-[#64748B] mt-0.5">Keine Softwaremiete, voller Quellcode</div>
        </div>
      </div>

      <div class="p-4 rounded-2xl bg-white border border-slate-200/90 shadow-xs flex items-start gap-3">
        <div class="w-8 h-8 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center shrink-0 mt-0.5">
          <i data-lucide="clock" class="w-4 h-4"></i>
        </div>
        <div>
          <div class="text-xs font-bold text-[#0F172A]">In 14 Tagen live</div>
          <div class="text-[11px] text-[#64748B] mt-0.5">Nur ca. 90 Min. Aufwand für den Meister</div>
        </div>
      </div>

      <div class="p-4 rounded-2xl bg-white border border-slate-200/90 shadow-xs flex items-start gap-3">
        <div class="w-8 h-8 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center shrink-0 mt-0.5">
          <i data-lucide="calculator" class="w-4 h-4"></i>
        </div>
        <div>
          <div class="text-xs font-bold text-[#0F172A]">Echte B2B-Festpreise</div>
          <div class="text-[11px] text-[#64748B] mt-0.5">Netto zzgl. MwSt., 0 € Überraschungen</div>
        </div>
      </div>

      <div class="p-4 rounded-2xl bg-white border border-slate-200/90 shadow-xs flex items-start gap-3">
        <div class="w-8 h-8 rounded-xl bg-blue-50 text-[#2563EB] flex items-center justify-center shrink-0 mt-0.5">
          <i data-lucide="map-pin" class="w-4 h-4"></i>
        </div>
        <div>
          <div class="text-xs font-bold text-[#0F172A]">Regionale Betreuung</div>
          <div class="text-[11px] text-[#64748B] mt-0.5">Direkter Ansprechpartner in Bielefeld</div>
        </div>
      </div>
    </div>

  </div>
</header>

<main class="py-16 px-4 sm:px-6 max-w-6xl mx-auto space-y-28">

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- 2. HAUPTANGEBOT: MEISTER-AUFTRAGS-SYSTEM (2.800 €)             -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="meister-system" class="space-y-10 scroll-mt-28">
    <div class="text-center max-w-3xl mx-auto space-y-3">
      <div class="inline-flex items-center gap-1.5 text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider bg-blue-50 px-3 py-1 rounded-full border border-blue-200 shadow-2xs">
        <i data-lucide="star" class="w-3.5 h-3.5 fill-[#2563EB]"></i>
        <span>Hauptangebot · Regulärer Standard für Meisterbetriebe</span>
      </div>
      <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-[#0F172A]">
        SparrenWeb Meister-Auftrags-System (2.800 € netto einmalig)
      </h2>
      <p data-aos="fade-up" data-aos-delay="100" class="text-sm sm:text-base text-[#475569] leading-relaxed">
        Das schlüsselfertige Gesamtsystem für etablierte Handwerksbetriebe mit 4 bis 20 Mitarbeitern in Bielefeld &amp; OWL. Konzipiert, um Pfennigfuchser auszusortieren und ertragsstarke 5-stellige Premium-Aufträge planbar zu gewinnen.
      </p>
    </div>

    <!-- Große Paketkarte mit Blue Glow & Tiefenstruktur -->
    <div data-aos="fade-up" data-aos-duration="700" class="bg-white rounded-3xl border-2 border-[#2563EB] p-6 sm:p-10 lg:p-12 shadow-xl relative overflow-hidden card-lift">
      
      <!-- Top Accent Bar -->
      <div class="absolute top-0 left-0 right-0 h-1.5 bg-gradient-to-r from-blue-500 via-[#2563EB] to-blue-700"></div>

      <div class="grid lg:grid-cols-3 gap-8 items-start">
        
        <!-- Left 2 Cols: Details, Preissplit & 6 Module -->
        <div class="lg:col-span-2 space-y-6">
          
          <div class="flex flex-wrap items-baseline justify-between gap-4 border-b border-slate-100 pb-5">
            <div>
              <div class="flex items-baseline gap-2">
                <span class="text-3xl sm:text-4xl lg:text-5xl font-extrabold font-mono text-[#0F172A]">2.800 €</span>
                <span class="text-xs font-semibold text-[#64748B]">netto einmalig · zzgl. MwSt.</span>
              </div>
              <div class="text-xs text-[#2563EB] font-bold mt-1">
                Website-Kauf statt Miete · 100 % Ihr uneingeschränktes Betriebseigentum
              </div>
            </div>

            <!-- Interactive Payment Milestone Selector -->
            <div class="bg-slate-50 border border-slate-200 p-1 rounded-xl text-xs font-semibold flex items-center">
              <button id="payModelSplit" onclick="setPayModel('split')" class="px-3 py-1.5 rounded-lg bg-white text-[#2563EB] shadow-2xs border border-slate-200 transition-all font-bold">
                50/50 Split (1.400 € / 1.400 €)
              </button>
              <button id="payModelThree" onclick="setPayModel('three')" class="px-3 py-1.5 rounded-lg text-slate-600 hover:text-[#0F172A] transition-all">
                3 Raten (1.400 € / 700 € / 700 €)
              </button>
            </div>
          </div>

          <!-- Dynamic Payment Explanation Box -->
          <div id="payExplBox" class="p-3.5 rounded-xl bg-blue-50/70 border border-blue-200 text-xs text-blue-950 leading-relaxed">
            <strong>Faires Zahlungsmodell 50/50:</strong> Sie zahlen 50 % bei Projektstart (1.400 € netto) zur Deckung der Konzeption &amp; Textarbeit. Die zweiten 50 % (1.400 € netto) werden <em>erst nach vollständiger Funktionsprüfung, Ihrer persönlichen Freigabe und erfolgreichem Go-Live</em> fällig.
          </div>

          <!-- 6 Structured Scope Cards -->
          <div class="grid sm:grid-cols-2 gap-3.5 text-xs text-[#334155] pt-1">
            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80 hover:border-blue-300 transition-colors flex items-start gap-3">
              <div class="w-7 h-7 rounded-lg bg-blue-100 text-[#2563EB] flex items-center justify-center shrink-0 mt-0.5">
                <i data-lucide="layout" class="w-3.5 h-3.5"></i>
              </div>
              <div>
                <strong class="text-[#0F172A] block text-[13px] mb-0.5">Bis zu 6 individuelle Inhaltsseiten</strong>
                Startseite, Leistungs-Spezialisierungen, Referenz-Architekturen, Über den Meisterbetrieb, Kontakt &amp; Impressum.
              </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80 hover:border-blue-300 transition-colors flex items-start gap-3">
              <div class="w-7 h-7 rounded-lg bg-blue-100 text-[#2563EB] flex items-center justify-center shrink-0 mt-0.5">
                <i data-lucide="filter" class="w-3.5 h-3.5"></i>
              </div>
              <div>
                <strong class="text-[#0F172A] block text-[13px] mb-0.5">Branchen-Vorabfilter mit Foto-Upload</strong>
                Interessenten übermitteln Maße, Fotos und Zeitplan direkt vom Smartphone. Sortiert Kleinkram vorab aus.
              </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80 hover:border-blue-300 transition-colors flex items-start gap-3">
              <div class="w-7 h-7 rounded-lg bg-blue-100 text-[#2563EB] flex items-center justify-center shrink-0 mt-0.5">
                <i data-lucide="file-text" class="w-3.5 h-3.5"></i>
              </div>
              <div>
                <strong class="text-[#0F172A] block text-[13px] mb-0.5">Schlüsselfertige Meister-Fachtexte</strong>
                Exakt formuliert für SHK, Dach, Elektro, Tischler oder GaLaBau. 0 Minuten Schreibarbeit für Sie.
              </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80 hover:border-blue-300 transition-colors flex items-start gap-3">
              <div class="w-7 h-7 rounded-lg bg-blue-100 text-[#2563EB] flex items-center justify-center shrink-0 mt-0.5">
                <i data-lucide="map-pin" class="w-3.5 h-3.5"></i>
              </div>
              <div>
                <strong class="text-[#0F172A] block text-[13px] mb-0.5">Google Profil &amp; Local SEO OWL</strong>
                Optimierung Ihres Google-Unternehmensprofils, Schema.org LocalBusiness-Markup und Keyword-Fundament.
              </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80 hover:border-blue-300 transition-colors flex items-start gap-3">
              <div class="w-7 h-7 rounded-lg bg-blue-100 text-[#2563EB] flex items-center justify-center shrink-0 mt-0.5">
                <i data-lucide="smartphone-nfc" class="w-3.5 h-3.5"></i>
              </div>
              <div>
                <strong class="text-[#0F172A] block text-[13px] mb-0.5">5 physische Baustellen-NFC-Karten</strong>
                Ihre Monteure halten die Karte an das Kunden-Smartphone: 5-Sterne-Google-Bewertungen direkt bei Abnahme vor Ort.
              </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80 hover:border-blue-300 transition-colors flex items-start gap-3">
              <div class="w-7 h-7 rounded-lg bg-blue-100 text-[#2563EB] flex items-center justify-center shrink-0 mt-0.5">
                <i data-lucide="code" class="w-3.5 h-3.5"></i>
              </div>
              <div>
                <strong class="text-[#0F172A] block text-[13px] mb-0.5">100 % Eigentum &amp; Quellcode</strong>
                HTML5, CSS, Vanilla JS. Kein Mietvertrag, keine Agentur-Abhängigkeit. Sie können jederzeit frei hosten.
              </div>
            </div>
          </div>

        </div>

        <!-- Right Col: Wirtschaftlichkeit, Zielgruppe & Direkter CTA -->
        <div class="lg:border-l lg:border-slate-100 lg:pl-8 flex flex-col justify-between space-y-6">
          <div class="space-y-4">
            <h3 class="text-xs font-bold text-[#0F172A] uppercase tracking-wider font-mono flex items-center gap-2">
              <i data-lucide="target" class="w-4 h-4 text-[#2563EB]"></i>
              <span>Für wen konzipiert?</span>
            </h3>
            <p class="text-xs text-[#475569] leading-relaxed">
              Für etablierte Meisterbetriebe, die genug von unvollständigen Anrufen, zeitraubenden Leerfahrten und Preisfüchsen haben und ihren Betrieb regional als erstklassige Qualitätsmarke etablieren möchten.
            </p>

            <div class="p-4 bg-emerald-50 rounded-2xl border border-emerald-200 text-xs text-emerald-950 space-y-2">
              <div class="font-bold flex items-center gap-1.5 text-emerald-900">
                <i data-lucide="trending-up" class="w-4 h-4 text-emerald-600"></i>
                <span>Kaufmännische Meister-Rechnung:</span>
              </div>
              <p class="text-[11px] leading-relaxed">
                Ein einziger gewonnener Qualitätsauftrag (z. B. Badsanierung 18.000 €, Wärmepumpen-Tausch 22.000 € oder PV-Anlage 16.000 €) amortisiert die gesamte 2.800 € Investition bereits beim ersten Projekt vollständig.
              </p>
            </div>

            <div class="space-y-1.5 text-xs text-[#64748B]">
              <div class="flex items-center gap-2">
                <i data-lucide="check" class="w-3.5 h-3.5 text-emerald-600"></i>
                <span>Lieferzeit: 14 Werktage nach Telefonat</span>
              </div>
              <div class="flex items-center gap-2">
                <i data-lucide="check" class="w-3.5 h-3.5 text-emerald-600"></i>
                <span>Persönliche Betreuung in Bielefeld &amp; OWL</span>
              </div>
            </div>
          </div>

          <div class="pt-2">
            <a href="anfrage.html" class="w-full inline-flex items-center justify-center gap-2 bg-[#2563EB] hover:bg-blue-700 text-white text-sm font-bold py-4 px-6 rounded-2xl transition-all shadow-md shadow-blue-500/25 hover:-translate-y-0.5">
              <span>System-Entwurf anfordern</span>
              <i data-lucide="arrow-right" class="w-4 h-4"></i>
            </a>
            <div class="text-[11px] text-center text-[#64748B] mt-2">
              100 % unverbindlich · Vorab-Entwurf zur Ansicht
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- 3. PILOT-ANGEBOT: OWL-REFERENZ-PILOT (1.500 €)                 -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="pilot" class="space-y-6 scroll-mt-28">
    <div data-aos="fade-up" class="bg-gradient-to-br from-amber-50/80 via-white to-amber-50/40 rounded-3xl border-2 border-amber-300/80 p-6 sm:p-10 shadow-lg space-y-6 card-lift">
      
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-amber-200/60 pb-5">
        <div>
          <span class="text-[11px] font-mono font-bold text-amber-900 uppercase tracking-wider bg-amber-100 px-3 py-1 rounded-full border border-amber-300">
            Angebot A · Streng limitiertes Kontingent
          </span>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-[#0F172A] mt-2">
            OWL-Referenz-Pilot (1.500 € netto einmalig)
          </h2>
          <p class="text-xs sm:text-sm text-amber-950 mt-1">
            Maximal 3 Meisterbetriebe in Bielefeld &amp; OWL zu stark vergünstigten Vorzugskonditionen.
          </p>
        </div>

        <div class="sm:text-right shrink-0">
          <div class="flex items-baseline gap-1 sm:justify-end">
            <span class="text-3xl sm:text-4xl font-extrabold font-mono text-[#0F172A]">1.500 €</span>
            <span class="text-xs text-[#64748B]">netto einmalig</span>
          </div>
          <span class="text-[11px] text-amber-900 font-bold block mt-0.5">50 % Start (750 €) · 50 % Abnahme (750 €)</span>
        </div>
      </div>

      <!-- Live Dynamic Allocation Bar -->
      <div class="p-4 rounded-2xl bg-amber-100/60 border border-amber-200/80 space-y-2">
        <div class="flex justify-between items-center text-xs font-bold text-amber-950">
          <span class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-amber-600 animate-ping"></span>
            <span>Verfügbarkeit für Bielefeld &amp; OWL (Q1/Q2):</span>
          </span>
          <span class="font-mono text-amber-900">Noch 2 von 3 Plätzen frei</span>
        </div>
        <div class="w-full bg-white h-3 rounded-full overflow-hidden p-0.5 border border-amber-200">
          <div class="bg-amber-600 h-full rounded-full transition-all duration-500" style="width: 33%;"></div>
        </div>
        <div class="text-[11px] text-amber-900/90 leading-tight">
          Wir vergeben die Pilotkonditionen pro Gewerk in OWL genau einmal, um gegenseitige Konkurrenz auszuschließen.
        </div>
      </div>

      <div class="grid md:grid-cols-2 gap-6 text-xs text-[#334155] pt-1">
        <div class="space-y-3">
          <h3 class="font-bold text-[#0F172A] text-sm flex items-center gap-1.5">
            <i data-lucide="check-circle" class="w-4 h-4 text-amber-700"></i>
            <span>Was im Pilot-Paket vollständig enthalten ist:</span>
          </h3>
          <ul class="space-y-2">
            <li class="flex items-start gap-2">
              <i data-lucide="check" class="w-4 h-4 text-amber-700 shrink-0 mt-0.5"></i>
              <span>Vollständiges schlüsselfertiges Website-System (bis zu 5 Inhaltsseiten)</span>
            </li>
            <li class="flex items-start gap-2">
              <i data-lucide="check" class="w-4 h-4 text-amber-700 shrink-0 mt-0.5"></i>
              <span>Branchenspezifischer Kunden-Vorabfilter mit mobilem Foto-Upload</span>
            </li>
            <li class="flex items-start gap-2">
              <i data-lucide="check" class="w-4 h-4 text-amber-700 shrink-0 mt-0.5"></i>
              <span>Schlüsselfertige Fachtexte für Ihr Hauptgewerk (0 Minuten Schreibaufwand)</span>
            </li>
            <li class="flex items-start gap-2">
              <i data-lucide="check" class="w-4 h-4 text-amber-700 shrink-0 mt-0.5"></i>
              <span>Rechtssichere DSGVO-Basis &amp; Impressumsstruktur</span>
            </li>
            <li class="flex items-start gap-2">
              <i data-lucide="check" class="w-4 h-4 text-amber-700 shrink-0 mt-0.5"></i>
              <span>100 % Quellcode-Eigentum nach Begleichung der Schlussrechnung</span>
            </li>
          </ul>
        </div>

        <div class="space-y-3 bg-white p-5 rounded-2xl border border-amber-200/80">
          <h3 class="font-bold text-amber-950 text-sm flex items-center gap-1.5">
            <i data-lucide="handshake" class="w-4 h-4 text-amber-700"></i>
            <span>Die verbindlichen Pilot-Bedingungen (Ehrliche Partnerschaft):</span>
          </h3>
          <p class="text-[#475569] leading-relaxed text-xs">
            Als Pilotbetrieb erhalten Sie das vollständige System mit <strong>1.300 € Preisnachlass</strong> gegenüber dem regulären Meister-System. Im Gegenzug verpflichten Sie sich zu folgenden 2 fairen Punkten:
          </p>
          <ol class="space-y-1.5 text-xs text-[#334155] list-decimal list-inside pl-1">
            <li>Ein 15-minütiges Feedback-Gespräch 60 Tage nach Go-Live.</li>
            <li>Freigabe von Logo und einem kurzen Zitat für eine regionale Fallstudie.</li>
          </ol>
          <div class="pt-2">
            <a href="anfrage.html" class="inline-flex items-center gap-2 bg-amber-600 hover:bg-amber-700 text-white font-bold px-5 py-2.5 rounded-xl transition-all shadow-xs hover:-translate-y-0.5">
              <span>Pilot-Verfügbarkeit anfragen →</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- 4. DIE KOMPLETT-KOMBI (ANGEBOT E – 3.500 €)                    -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="kombi" class="space-y-8 scroll-mt-28">
    <div data-aos="fade-up" class="bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 text-white rounded-3xl p-6 sm:p-10 lg:p-12 shadow-2xl relative overflow-hidden border border-blue-500/30 card-lift">
      
      <!-- Subtle Ambient Glow Accent -->
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-blue-600/15 rounded-full blur-2xl pointer-events-none"></div>

      <div class="relative z-10 space-y-6">
        
        <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-800 pb-5">
          <div class="space-y-1">
            <span class="inline-block text-[11px] font-mono font-bold uppercase tracking-wider px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-400/40">
              Angebot E · 500 € Kombi-Vorteil
            </span>
            <h2 class="text-2xl sm:text-4xl font-extrabold tracking-tight text-white mt-1">
              Komplett-Kombi: Meister-System + 60s-Recruiting
            </h2>
          </div>

          <div class="text-left sm:text-right">
            <div class="flex items-baseline gap-2">
              <span class="text-3xl sm:text-5xl font-extrabold font-mono text-white">3.500 €</span>
              <span class="text-xs text-slate-400 line-through">4.000 €</span>
            </div>
            <div class="text-xs text-emerald-400 font-semibold mt-0.5">
              Sie sparen sofort 500 € netto gegenüber der Einzelbuchung
            </div>
          </div>
        </div>

        <p class="text-xs sm:text-base text-slate-300 leading-relaxed max-w-3xl">
          Die schlüsselfertige Maximallösung für vorausschauende Handwerksunternehmer: Lösen Sie das Neukunden- und das Fachkräfteproblem mit einem einzigen, perfekt aufeinander abgestimmten System.
        </p>

        <!-- 3 Synergie-Säulen -->
        <div class="grid md:grid-cols-3 gap-4 pt-2 text-xs">
          <div class="p-4 rounded-2xl bg-slate-800/60 border border-slate-700/80 space-y-2">
            <div class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-400 flex items-center justify-center font-bold">1</div>
            <h3 class="font-bold text-white text-sm">Meister-System (2.800 €)</h3>
            <p class="text-slate-300 leading-relaxed text-[11px]">
              Bis zu 6 Seiten, digitaler Vorabfilter mit Foto-Upload, Fachtexte, Local SEO OWL und 5 Baustellen-NFC-Karten.
            </p>
          </div>

          <div class="p-4 rounded-2xl bg-slate-800/60 border border-slate-700/80 space-y-2">
            <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold">2</div>
            <h3 class="font-bold text-white text-sm">60s-Recruiting (1.200 €)</h3>
            <p class="text-slate-300 leading-relaxed text-[11px]">
              Smartphone-Bewerbungs-Trichter ohne Lebenslaufzwang, Google Jobs Schema &amp; druckfertige Fahrzeug-QR-Codes.
            </p>
          </div>

          <div class="p-4 rounded-2xl bg-gradient-to-br from-blue-900/60 to-emerald-900/40 border border-emerald-500/40 space-y-2">
            <div class="w-8 h-8 rounded-xl bg-emerald-400 text-slate-950 flex items-center justify-center font-bold">✓</div>
            <h3 class="font-bold text-emerald-300 text-sm">Ihr doppelter Betriebsvorteil</h3>
            <p class="text-slate-200 leading-relaxed text-[11px]">
              Volle Auftragsbücher mit ertragsstarken Projekten und gleichzeitig kontinuierlicher Zufluss an wechselwilligen Gesellen.
            </p>
          </div>
        </div>

        <div class="pt-4 flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
          <a href="anfrage.html" class="inline-flex items-center justify-center gap-2 bg-[#2563EB] hover:bg-blue-600 text-white text-xs sm:text-sm font-bold px-7 py-4 rounded-2xl transition-all shadow-lg shadow-blue-500/30 hover:-translate-y-0.5">
            <span>Komplett-Kombi anfragen</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </a>
          <span class="text-xs text-slate-400">
            Optional mit Kombi-Betreuung (490 €/Mo inkl. Ads-Management) erweiterbar
          </span>
        </div>

      </div>
    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- 5. 60-SEKUNDEN-RECRUITING (1.200 €) MIT LIVE-SIMULATOR         -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="recruiting" class="space-y-8 scroll-mt-28">
    <div class="text-center max-w-3xl mx-auto space-y-3">
      <span class="text-xs font-mono font-bold text-slate-500 uppercase tracking-wider bg-slate-100 px-3 py-1 rounded-full border border-slate-200">
        Angebot D · Einzeln oder im Paket buchbar
      </span>
      <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-[#0F172A]">
        Das 60-Sekunden-Recruiting-Modul (1.200 € netto einmalig)
      </h2>
      <p data-aos="fade-up" data-aos-delay="100" class="text-sm sm:text-base text-[#475569] leading-relaxed">
        Gute Gesellen schreiben keine Anschreiben am PC. Gewinnen Sie wechselwillige Fachkräfte direkt über das Smartphone in unter 60 Sekunden – ohne Lebenslauf und ohne PDF-Zwang.
      </p>
    </div>

    <div data-aos="fade-up" class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-10 shadow-lg space-y-8">
      <div class="grid lg:grid-cols-2 gap-8 items-center">
        
        <!-- Left: Leistungsbeschreibung -->
        <div class="space-y-5 text-xs sm:text-sm text-[#334155]">
          <p class="leading-relaxed">
            Klassische Stellenanzeigen verlangen Anschreiben, Zeugnisse und Lebensläufe – die Hürde ist für gute, festangestellte Handwerker viel zu hoch. Unser Recruiting-Modul kehrt den Prozess um: Fachkräfte bewerben sich spielerisch in wenigen Daumen-Klicks auf der Baustelle oder abends auf dem Sofa.
          </p>

          <div class="space-y-3">
            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80 flex items-start gap-3">
              <i data-lucide="briefcase" class="w-4 h-4 text-[#2563EB] shrink-0 mt-0.5"></i>
              <div>
                <strong class="text-[#0F172A] block text-xs">Google-Jobs-Auszeichnung:</strong>
                <span class="text-[11px] text-[#64748B]">Ihre offenen Stellen erscheinen mit allen Gehalts- und Vorzugsinformationen direkt in den Google-Jobs-Suchergebnissen in OWL.</span>
              </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80 flex items-start gap-3">
              <i data-lucide="qr-code" class="w-4 h-4 text-[#2563EB] shrink-0 mt-0.5"></i>
              <div>
                <strong class="text-[#0F172A] block text-xs">Druckfertige Vektor-QR-Codes:</strong>
                <span class="text-[11px] text-[#64748B]">Für Firmenfahrzeuge, Heckscheiben und Baustellenschilder. Interessierte Gesellen scannen den Code an der Ampel und sind im Bewerbertrichter.</span>
              </div>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80 flex items-start gap-3">
              <i data-lucide="megaphone" class="w-4 h-4 text-[#2563EB] shrink-0 mt-0.5"></i>
              <div>
                <strong class="text-[#0F172A] block text-xs">Social-Media-Anzeigenvorlagen:</strong>
                <span class="text-[11px] text-[#64748B]">Fertige Text- und Layoutvorlagen für regionale Kampagnen auf Instagram &amp; Facebook (Bielefeld, Gütersloh, Herford).</span>
              </div>
            </div>
          </div>

          <div class="pt-2 flex items-baseline gap-3">
            <span class="text-2xl sm:text-3xl font-extrabold font-mono text-[#0F172A]">1.200 €</span>
            <span class="text-xs text-[#64748B]">netto einmalig · Einzelbuchung</span>
          </div>
        </div>

        <!-- Right: Interaktiver Smartphone-Simulator -->
        <div class="bg-slate-900 rounded-3xl p-5 sm:p-6 border-2 border-slate-800 shadow-2xl text-white space-y-4">
          <div class="flex items-center justify-between border-b border-slate-800 pb-3 text-xs">
            <span class="font-bold text-blue-400 font-mono flex items-center gap-1.5">
              <i data-lucide="smartphone" class="w-3.5 h-3.5"></i>
              <span>Live-Bewerber-Simulator</span>
            </span>
            <span class="text-[10px] bg-blue-950 text-blue-300 border border-blue-800 px-2 py-0.5 rounded font-mono">
              Interaktiv testen
            </span>
          </div>

          <!-- Simulator Box -->
          <div class="bg-slate-950 rounded-2xl p-4 sm:p-5 border border-slate-800 space-y-4 min-h-[300px] flex flex-col justify-between">
            
            <!-- Sim Step 1 -->
            <div id="recSimStep1" class="space-y-3">
              <div class="text-xs text-slate-400 font-semibold">Schritt 1: Welches Gewerk beherrschen Sie?</div>
              <div class="grid grid-cols-2 gap-2 text-xs">
                <button type="button" onclick="setRecRole('Anlagenmechaniker SHK', this)" class="rec-role-btn active p-2.5 rounded-xl border border-[#2563EB] bg-blue-950/50 text-left hover:border-blue-400 transition-colors font-bold text-white">
                  SHK / Heizungsbau
                </button>
                <button type="button" onclick="setRecRole('Elektroniker Energie/Gebäude', this)" class="rec-role-btn p-2.5 rounded-xl border border-slate-800 bg-slate-900/60 text-left hover:border-slate-700 transition-colors font-bold text-white">
                  Elektro / PV
                </button>
                <button type="button" onclick="setRecRole('Dachdecker / Zimmerer', this)" class="rec-role-btn p-2.5 rounded-xl border border-slate-800 bg-slate-900/60 text-left hover:border-slate-700 transition-colors font-bold text-white">
                  Dach &amp; Holz
                </button>
                <button type="button" onclick="setRecRole('Tischler / Innenausbau', this)" class="rec-role-btn p-2.5 rounded-xl border border-slate-800 bg-slate-900/60 text-left hover:border-slate-700 transition-colors font-bold text-white">
                  Tischlerei &amp; Raum
                </button>
              </div>
              <button type="button" onclick="goRecStep(2)" class="w-full mt-2 py-2.5 bg-[#2563EB] hover:bg-blue-600 rounded-xl font-bold text-xs transition-colors flex items-center justify-center gap-1.5">
                <span>Weiter zur Qualifikation</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>

            <!-- Sim Step 2 -->
            <div id="recSimStep2" class="space-y-3 hidden">
              <div class="text-xs text-slate-400 font-semibold">Schritt 2: Qualifikation &amp; Wunsch-Bedingungen</div>
              <div class="space-y-2 text-xs">
                <label class="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900 border border-slate-800 cursor-pointer">
                  <input type="checkbox" checked class="rounded text-[#2563EB] focus:ring-0">
                  <span>Abgeschlossene Gesellenprüfung vorhanden</span>
                </label>
                <label class="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900 border border-slate-800 cursor-pointer">
                  <input type="checkbox" checked class="rounded text-[#2563EB] focus:ring-0">
                  <span>Führerschein Klasse B vorhanden</span>
                </label>
                <label class="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900 border border-slate-800 cursor-pointer">
                  <input type="checkbox" class="rounded text-[#2563EB] focus:ring-0">
                  <span>Interesse an 4-Tage-Woche</span>
                </label>
              </div>
              <div class="flex items-center justify-between pt-1">
                <button type="button" onclick="goRecStep(1)" class="text-xs text-slate-400 hover:text-white">← Zurück</button>
                <button type="button" onclick="goRecStep(3)" class="py-2 px-4 bg-[#2563EB] hover:bg-blue-600 rounded-xl font-bold text-xs transition-colors flex items-center gap-1">
                  <span>Weiter</span>
                  <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                </button>
              </div>
            </div>

            <!-- Sim Step 3 -->
            <div id="recSimStep3" class="space-y-3 hidden">
              <div class="text-xs text-slate-400 font-semibold">Schritt 3: Wie soll der Meister Sie kontaktieren?</div>
              <div class="space-y-2 text-xs">
                <div>
                  <label class="block text-[11px] text-slate-400 mb-1">Vorname &amp; Telefonnummer (für WhatsApp/Rückruf)</label>
                  <input type="text" id="recSimPhone" value="Dennis (Geselle) · 0176 98765432" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white text-xs">
                </div>
                <div>
                  <label class="block text-[11px] text-slate-400 mb-1">Bester Zeitpunkt für kurzen Anruf</label>
                  <select class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white text-xs">
                    <option>Nach Feierabend (ab 16:30 Uhr)</option>
                    <option>In der Mittagspause</option>
                    <option>Am Samstag Vormittag</option>
                  </select>
                </div>
              </div>
              <div class="flex items-center justify-between pt-1">
                <button type="button" onclick="goRecStep(2)" class="text-xs text-slate-400 hover:text-white">← Zurück</button>
                <button type="button" onclick="finishRecSim()" class="py-2.5 px-4 bg-emerald-600 hover:bg-emerald-500 rounded-xl font-bold text-xs transition-colors flex items-center gap-1.5 text-white">
                  <i data-lucide="send" class="w-3.5 h-3.5"></i>
                  <span>Bewerbung absenden</span>
                </button>
              </div>
            </div>

            <!-- Sim Success Screen -->
            <div id="recSimSuccess" class="space-y-3 hidden text-center py-4">
              <div class="w-10 h-10 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center mx-auto">
                <i data-lucide="check" class="w-6 h-6"></i>
              </div>
              <h4 class="font-bold text-white text-sm">Bewerbung in 42 Sekunden übermittelt!</h4>
              <p class="text-[11px] text-slate-300 leading-relaxed max-w-xs mx-auto">
                Der Meister erhält sofort eine strukturierte WhatsApp/E-Mail-Benachrichtigung mit Telefonnummer und Wunschzeit. 0 Bürokratie für beide Seiten.
              </p>
              <button type="button" onclick="goRecStep(1)" class="mt-2 text-[11px] text-blue-400 hover:underline">
                Simulator zurücksetzen ↺
              </button>
            </div>

          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- 6. VORQUALIFIZIERUNG: KUNDE VS. CHEF-COCKPIT                   -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="vorqualifizierung" class="space-y-10 scroll-mt-28">
    <div class="text-center max-w-3xl mx-auto space-y-3">
      <span class="text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider bg-blue-50 px-3 py-1 rounded-full border border-blue-200">
        Kernmodul im Meister-System
      </span>
      <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-[#0F172A]">
        Der digitale Kunden-Vorabfilter mit „Chef-Cockpit“
      </h2>
      <p data-aos="fade-up" data-aos-delay="100" class="text-sm sm:text-base text-[#475569] leading-relaxed">
        Erleben Sie live, wie ein Interessent auf dem Smartphone ein Projekt konfiguriert und welche glasklare Vorkalkulationsmappe zeitgleich im Büro des Meisters landet.
      </p>
    </div>

    <!-- Live Interaktiver Split-Screen Stage -->
    <div data-aos="fade-up" class="bg-slate-900 text-white rounded-3xl p-6 sm:p-10 shadow-2xl space-y-8 border border-slate-800">
      
      <!-- Stage Header & Tab Buttons -->
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 border-b border-slate-800 pb-6">
        <div>
          <span class="text-xs font-mono text-blue-400 font-bold uppercase tracking-wider flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span>
            <span>Interaktive Funktions-Demo</span>
          </span>
          <h3 class="text-lg sm:text-xl font-bold text-white mt-1">1. Kunden-Ansicht vs. 2. Was im Meister-Büro ankommt</h3>
        </div>

        <div class="flex items-center bg-slate-800/90 p-1.5 rounded-2xl border border-slate-700 text-xs font-bold">
          <button id="btnViewCustomer" onclick="switchDemoTab('customer')" class="px-4 py-2 rounded-xl bg-[#2563EB] text-white transition-all shadow-xs flex items-center gap-1.5">
            <i data-lucide="smartphone" class="w-3.5 h-3.5"></i>
            <span>1. Kunden-Smartphone</span>
          </button>
          <button id="btnViewMaster" onclick="switchDemoTab('master')" class="px-4 py-2 rounded-xl text-slate-300 hover:text-white transition-all flex items-center gap-1.5">
            <i data-lucide="monitor" class="w-3.5 h-3.5"></i>
            <span>2. Chef-Cockpit (Büro)</span>
          </button>
        </div>
      </div>

      <!-- Tab 1: Kunden-Ansicht -->
      <div id="tabContentCustomer" class="space-y-6">
        <div class="max-w-xl mx-auto bg-slate-950 rounded-2xl border border-slate-800 p-5 sm:p-7 space-y-5 shadow-inner">
          
          <div class="flex items-center justify-between text-xs text-slate-400 border-b border-slate-800/80 pb-3">
            <span id="demoStepIndicator" class="font-bold text-blue-400 font-mono">Schritt 1 von 3: Projekt auswählen</span>
            <span class="text-[10px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded font-mono">Simulierte Mobilansicht</span>
          </div>

          <!-- Step 1 Container -->
          <div id="demoStep1" class="space-y-3">
            <p class="text-sm font-semibold text-white">Welches Vorhaben planen Sie für Ihre Immobilie?</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
              <button type="button" onclick="setDemoOption('proj', 'Komplettbad-Sanierung', 'ca. 14 m², Bj. 1982', '~68 %', this)" class="demo-opt-btn active p-3 rounded-xl border border-[#2563EB] bg-blue-950/40 text-left hover:border-blue-400 transition-colors">
                <div class="font-bold text-white">Komplettbad-Sanierung</div>
                <div class="text-[11px] text-slate-400 mt-0.5">Neuplanung barrierefrei &amp; Fliesen</div>
              </button>
              <button type="button" onclick="setDemoOption('proj', 'Wärmepumpen-Installation', 'Altbau 160 m², Bj. 1974', '~65 %', this)" class="demo-opt-btn p-3 rounded-xl border border-slate-800 bg-slate-900/60 text-left hover:border-slate-700 transition-colors">
                <div class="font-bold text-white">Wärmepumpen-Tausch</div>
                <div class="text-[11px] text-slate-400 mt-0.5">KfW-Förderung &amp; Heizkörpertausch</div>
              </button>
              <button type="button" onclick="setDemoOption('proj', 'Energetische Dachsanierung', 'Satteldach 180 m², Ziegel', '~72 %', this)" class="demo-opt-btn p-3 rounded-xl border border-slate-800 bg-slate-900/60 text-left hover:border-slate-700 transition-colors">
                <div class="font-bold text-white">Dachsanierung &amp; Dämmung</div>
                <div class="text-[11px] text-slate-400 mt-0.5">Aufdachdämmung &amp; Eindeckung</div>
              </button>
              <button type="button" onclick="setDemoOption('proj', 'Photovoltaik & Speicher', '12 kWp Dachanlage, Süd', '~64 %', this)" class="demo-opt-btn p-3 rounded-xl border border-slate-800 bg-slate-900/60 text-left hover:border-slate-700 transition-colors">
                <div class="font-bold text-white">PV-Anlage mit Speicher</div>
                <div class="text-[11px] text-slate-400 mt-0.5">Notstrom &amp; Wallbox-Integration</div>
              </button>
            </div>
            <div class="pt-2 flex justify-end">
              <button type="button" onclick="goDemoStep(2)" class="px-5 py-2.5 rounded-xl bg-[#2563EB] hover:bg-blue-600 text-white font-bold text-xs transition-colors flex items-center gap-1.5">
                <span>Weiter zu Fotos &amp; Maßen</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>

          <!-- Step 2 Container -->
          <div id="demoStep2" class="space-y-3 hidden">
            <p class="text-sm font-semibold text-white">Fotos vom Bestand &amp; Maße</p>
            <div class="space-y-3 text-xs">
              <div class="p-4 rounded-xl border-2 border-dashed border-slate-700 bg-slate-900/60 text-center space-y-2">
                <i data-lucide="camera" class="w-6 h-6 text-blue-400 mx-auto"></i>
                <div class="text-slate-300 font-medium">Fotos vom Altbestand hochladen</div>
                <div class="text-[10px] text-slate-500">JPG, PNG bis 15 MB · Direkt mit Smartphone-Kamera aufgenommen</div>
                <div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-blue-900/40 border border-blue-700/60 text-[11px] text-blue-300">
                  <i data-lucide="check" class="w-3 h-3 text-blue-400"></i>
                  <span>2 Fotos simuliert angehängt (Bestand_1.jpg, Grundriss.png)</span>
                </div>
              </div>
              <div>
                <label class="block text-[11px] text-slate-400 mb-1">Ungefähre Maße oder Raumgröße</label>
                <input type="text" id="demoInputDim" value="ca. 14 m², Bj. 1982" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white text-xs">
              </div>
            </div>
            <div class="pt-2 flex items-center justify-between">
              <button type="button" onclick="goDemoStep(1)" class="text-xs text-slate-400 hover:text-white transition-colors">← Zurück</button>
              <button type="button" onclick="goDemoStep(3)" class="px-5 py-2.5 rounded-xl bg-[#2563EB] hover:bg-blue-600 text-white font-bold text-xs transition-colors flex items-center gap-1.5">
                <span>Weiter zu Zeitplan &amp; Ort</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>

          <!-- Step 3 Container -->
          <div id="demoStep3" class="space-y-3 hidden">
            <p class="text-sm font-semibold text-white">Standort, Zeitplan &amp; Kontaktdaten</p>
            <div class="space-y-3 text-xs">
              <div class="grid grid-cols-2 gap-2">
                <div>
                  <label class="block text-[11px] text-slate-400 mb-1">PLZ &amp; Ort</label>
                  <input type="text" id="demoInputLoc" value="33615 Bielefeld" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white text-xs">
                </div>
                <div>
                  <label class="block text-[11px] text-slate-400 mb-1">Wunschzeitraum</label>
                  <select id="demoInputTime" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white text-xs">
                    <option>In den nächsten 2–4 Monaten</option>
                    <option>Zeitnah (nächste 4–6 Wochen)</option>
                    <option>Im 2. Halbjahr</option>
                  </select>
                </div>
              </div>
              <div>
                <label class="block text-[11px] text-slate-400 mb-1">Name &amp; Telefonnummer für Rücksprache</label>
                <input type="text" id="demoInputContact" value="Familie Schulze · 0521 987654" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-white text-xs">
              </div>
            </div>
            <div class="pt-2 flex items-center justify-between">
              <button type="button" onclick="goDemoStep(2)" class="text-xs text-slate-400 hover:text-white transition-colors">← Zurück</button>
              <button type="button" onclick="switchDemoTab('master')" class="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition-colors flex items-center gap-1.5 shadow-md">
                <i data-lucide="check" class="w-3.5 h-3.5"></i>
                <span>Anfrage absenden &amp; Chef-Cockpit öffnen</span>
              </button>
            </div>
          </div>

        </div>
      </div>

      <!-- Tab 2: Chef-Cockpit -->
      <div id="tabContentMaster" class="hidden space-y-6">
        <div class="max-w-xl mx-auto bg-slate-950 rounded-2xl border-2 border-emerald-500/60 p-6 space-y-5 shadow-2xl">
          
          <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-ping"></span>
              <span class="text-xs font-bold text-white font-mono uppercase tracking-wide">Neue qualifizierte Anfrage eingegangen</span>
            </div>
            <span id="masterResMargin" class="text-[11px] text-emerald-400 font-mono font-bold bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-700/60">
              Deckungsbeitrag ~68 %
            </span>
          </div>

          <div class="space-y-3 text-xs">
            <div class="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-2.5">
              <div class="flex items-center justify-between">
                <span class="text-slate-400">Projekt:</span>
                <span id="masterResProj" class="text-white font-bold text-sm">Komplettbad-Sanierung</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">Standort:</span>
                <span id="masterResLoc" class="text-white font-bold">33615 Bielefeld</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">Eckdaten &amp; Maße:</span>
                <span id="masterResDim" class="text-white">ca. 14 m², Bj. 1982</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">Wunschzeitraum:</span>
                <span id="masterResTime" class="text-white">In den nächsten 2–4 Monaten</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-400">Kontakt:</span>
                <span id="masterResContact" class="text-white font-bold">Familie Schulze · 0521 987654</span>
              </div>
              <div class="flex items-center justify-between pt-2 border-t border-slate-800 text-blue-300">
                <span class="flex items-center gap-1.5"><i data-lucide="image" class="w-3.5 h-3.5"></i> Fotos:</span>
                <span class="font-bold underline cursor-pointer">2 Anhänge verfügbar (Bestand_1.jpg, Grundriss.png)</span>
              </div>
            </div>

            <div class="p-3.5 bg-emerald-950/50 rounded-xl border border-emerald-800/80 text-[11px] text-emerald-200 leading-snug">
              <strong>Entlastung für den Meister:</strong> Sie fahren nie wieder für eine vage Vor-Ort-Begutachtung ins Blaue. Mit Maßen, Bestandsfotos und Zeitrahmen erstellen Sie in 5 Minuten am Schreibtisch ein fundiertes Erstangebot oder rufen den Kunden gezielt vorbereitet an.
            </div>

            <div class="pt-1 flex justify-between items-center text-xs">
              <button type="button" onclick="switchDemoTab('customer')" class="text-slate-400 hover:text-white flex items-center gap-1">
                ← Zurück zur Kunden-Ansicht
              </button>
              <a href="anfrage.html" class="px-4 py-2 bg-[#2563EB] hover:bg-blue-600 rounded-xl text-white font-bold flex items-center gap-1.5">
                <span>Dieses System anfragen</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </a>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- 7. SYSTEMBETRIEB & AD-CARE (ANGEBOT C)                         -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="systembetrieb" class="space-y-10 scroll-mt-28">
    <div class="text-center max-w-3xl mx-auto space-y-3">
      <span class="text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider bg-blue-50 px-3 py-1 rounded-full border border-blue-200">
        Laufende Entlastung auf Wunsch
      </span>
      <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-[#0F172A]">
        Regionaler Sichtbarkeits- &amp; Systembetrieb
      </h2>
      <p data-aos="fade-up" data-aos-delay="100" class="text-sm sm:text-base text-[#475569] leading-relaxed">
        Freiwillig, transparent und jederzeit monatlich kündbar. Bei SparrenWeb gibt es keinen Zwang zum Monatsabo – Sie entscheiden, ob Sie die Pflege selbst übernehmen oder an uns abgeben.
      </p>

      <!-- Interactive Billing Toggle: Monthly vs. Yearly -->
      <div data-aos="fade-up" data-aos-delay="150" class="pt-2 flex justify-center">
        <div class="inline-flex items-center p-1 rounded-2xl bg-slate-100 border border-slate-200 text-xs font-bold">
          <button id="billToggleMonth" onclick="setBillingCycle('month')" class="px-4 py-2 rounded-xl bg-white text-[#2563EB] shadow-xs border border-slate-200 transition-all">
            Monatliche Zahlung (Kündbar)
          </button>
          <button id="billToggleYear" onclick="setBillingCycle('year')" class="px-4 py-2 rounded-xl text-slate-600 hover:text-[#0F172A] transition-all flex items-center gap-1.5">
            <span>Jährliche Zahlung</span>
            <span class="text-[10px] bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full font-bold">10 % Rabatt</span>
          </button>
        </div>
      </div>
    </div>

    <div class="grid md:grid-cols-2 gap-8">
      
      <!-- Option C1: Systembetrieb -->
      <div data-aos="fade-up" class="bg-white rounded-3xl border border-slate-200 p-8 shadow-md space-y-6 card-lift">
        <div class="flex items-center justify-between">
          <span class="text-xs font-mono font-bold text-[#2563EB] uppercase">Angebot C · Systembetrieb</span>
          <span class="text-xs bg-slate-100 text-slate-700 px-2.5 py-0.5 rounded-full font-semibold">Monatlich kündbar</span>
        </div>
        <div>
          <h3 class="text-xl font-bold text-[#0F172A]">Regionaler Systembetrieb</h3>
          <div class="flex items-baseline gap-1 mt-2">
            <span id="priceSysOp" class="text-3xl sm:text-4xl font-extrabold font-mono text-[#0F172A]">250 €</span>
            <span id="priceSysOpSuffix" class="text-xs text-[#64748B]">netto / Monat</span>
          </div>
          <div id="priceSysOpNote" class="text-[11px] text-[#2563EB] font-bold mt-1">
            Flexibel monatlich kündbar · Keine Mindestlaufzeit
          </div>
        </div>

        <p class="text-xs text-[#475569] leading-relaxed">
          Wir halten Ihr Web-System technisch auf Höchstleistung, sichern Daten täglich auf deutschen Servern und übernehmen Änderungen auf Zuruf.
        </p>

        <ul class="space-y-2.5 text-xs text-[#334155] border-t border-slate-100 pt-4">
          <li class="flex items-start gap-2">
            <i data-lucide="check" class="w-4 h-4 text-[#2563EB] shrink-0 mt-0.5"></i>
            <span><strong>60 Min. monatliches Änderungsservice-Kontingent:</strong> Anpassung von Öffnungszeiten, Notdienst-Hinweisen, Texten, Bildern oder neuen Gesuchten.</span>
          </li>
          <li class="flex items-start gap-2">
            <i data-lucide="check" class="w-4 h-4 text-[#2563EB] shrink-0 mt-0.5"></i>
            <span><strong>High-Performance-Hosting in Deutschland:</strong> Ladezeiten unter 1 Sekunde, SSL-Zertifikat, HTTP/3 und tägliche Backups.</span>
          </li>
          <li class="flex items-start gap-2">
            <i data-lucide="check" class="w-4 h-4 text-[#2563EB] shrink-0 mt-0.5"></i>
            <span><strong>DSGVO- &amp; Sicherheits-Wartung:</strong> Kontinuierliche Überwachung von Impressumspflichten, Cookie-freier Architektur und PHP/Server-Updates.</span>
          </li>
        </ul>

        <div class="pt-2">
          <a href="anfrage.html" class="w-full inline-flex items-center justify-center gap-2 bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold py-3.5 rounded-xl transition-all">
            <span>Systembetrieb anfragen</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </a>
        </div>
      </div>

      <!-- Option C2: Kombi-Betreuung mit Ads -->
      <div data-aos="fade-up" data-aos-delay="100" class="bg-white rounded-3xl border-2 border-emerald-500/50 p-8 shadow-md space-y-6 card-lift relative">
        <div class="flex items-center justify-between">
          <span class="text-xs font-mono font-bold text-emerald-600 uppercase">Kombi-Betreuung mit Recruiting-Ads</span>
          <span class="text-xs bg-emerald-50 text-emerald-700 px-2.5 py-0.5 rounded-full font-semibold border border-emerald-200">Für Kombi-Kunden</span>
        </div>
        <div>
          <h3 class="text-xl font-bold text-[#0F172A]">Systembetrieb + Meta-Ads-Betreuung</h3>
          <div class="flex items-baseline gap-1 mt-2">
            <span id="priceKombiOp" class="text-3xl sm:text-4xl font-extrabold font-mono text-[#0F172A]">490 €</span>
            <span id="priceKombiOpSuffix" class="text-xs text-[#64748B]">netto / Monat</span>
          </div>
          <div id="priceKombiOpNote" class="text-[11px] text-emerald-700 font-bold mt-1">
            250 € Systembetrieb + 240 € Social-Media-Betreuung
          </div>
        </div>

        <p class="text-xs text-[#475569] leading-relaxed">
          Für Betriebe, die kontinuierlich neue Gesellen gewinnen wollen: Vollständiger technischer Systembetrieb kombiniert mit aktiver Betreuung regionaler Werbekampagnen auf Instagram &amp; Facebook.
        </p>

        <ul class="space-y-2.5 text-xs text-[#334155] border-t border-slate-100 pt-4">
          <li class="flex items-start gap-2">
            <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
            <span>Alles aus dem regulären Systembetrieb inklusive (Hosting, 60 Min. Kontingent, SSL).</span>
          </li>
          <li class="flex items-start gap-2">
            <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
            <span>Laufende Betreuung, A/B-Tests und Auswertung Ihrer bezahlten Fachkräfte-Kampagnen in OWL.</span>
          </li>
          <li class="flex items-start gap-2">
            <i data-lucide="info" class="w-4 h-4 text-slate-400 shrink-0 mt-0.5"></i>
            <span class="text-[#64748B]">Reines Werbebudget (empfohlen: ca. 300–600 €/Mo) rechnet der Betrieb transparent direkt mit Meta ab.</span>
          </li>
        </ul>

        <div class="pt-2">
          <a href="anfrage.html" class="w-full inline-flex items-center justify-center gap-2 bg-[#2563EB] hover:bg-blue-700 text-white text-xs font-bold py-3.5 rounded-xl transition-all shadow-md">
            <span>Kombi-Betreuung anfragen</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- 8. VOLLSTÄNDIGER FUNKTIONS- & PAKET-VERGLEICH (TABELLE)        -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="vergleich" class="space-y-8 scroll-mt-28">
    <div class="text-center max-w-3xl mx-auto space-y-3">
      <span class="text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider bg-blue-50 px-3 py-1 rounded-full border border-blue-200">
        Maximale Transparenz
      </span>
      <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-[#0F172A]">
        Alle 5 Angebote im direkten Leistungsvergleich
      </h2>
      <p data-aos="fade-up" data-aos-delay="100" class="text-sm sm:text-base text-[#475569] leading-relaxed">
        Vergleichen Sie den genauen Leistungsumfang aller Pakete schwarz auf weiß. Keine versteckten Sternchen.
      </p>
    </div>

    <!-- Responsive Table Container -->
    <div data-aos="fade-up" class="bg-white rounded-3xl border border-slate-200 shadow-xl overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="bg-slate-50 border-b border-slate-200 text-[#0F172A]">
              <th class="p-4 sm:p-5 font-bold uppercase tracking-wider font-mono text-[11px] min-w-[200px]">Leistungsbereich</th>
              <th class="p-4 sm:p-5 font-bold text-center bg-blue-50/70 text-[#2563EB] min-w-[150px] border-x border-blue-200/60">
                <div class="text-[10px] uppercase font-mono tracking-wide text-blue-600">Bestseller</div>
                <div class="text-sm font-extrabold">Meister-System</div>
                <div class="text-xs font-mono font-normal text-blue-900 mt-0.5">2.800 € netto</div>
              </th>
              <th class="p-4 sm:p-5 font-bold text-center text-amber-900 min-w-[140px]">
                <div class="text-[10px] uppercase font-mono tracking-wide text-amber-700">Limitiert (3)</div>
                <div class="text-sm font-extrabold">OWL-Pilot</div>
                <div class="text-xs font-mono font-normal text-[#64748B] mt-0.5">1.500 € netto</div>
              </th>
              <th class="p-4 sm:p-5 font-bold text-center text-[#0F172A] min-w-[140px]">
                <div class="text-[10px] uppercase font-mono tracking-wide text-emerald-600">500 € Vorteil</div>
                <div class="text-sm font-extrabold">Komplett-Kombi</div>
                <div class="text-xs font-mono font-normal text-[#64748B] mt-0.5">3.500 € netto</div>
              </th>
              <th class="p-4 sm:p-5 font-bold text-center text-[#0F172A] min-w-[130px]">
                <div class="text-[10px] uppercase font-mono tracking-wide text-slate-500">Modul</div>
                <div class="text-sm font-extrabold">60s-Recruiting</div>
                <div class="text-xs font-mono font-normal text-[#64748B] mt-0.5">1.200 € netto</div>
              </th>
              <th class="p-4 sm:p-5 font-bold text-center text-[#0F172A] min-w-[130px]">
                <div class="text-[10px] uppercase font-mono tracking-wide text-slate-500">Optional</div>
                <div class="text-sm font-extrabold">Systembetrieb</div>
                <div class="text-xs font-mono font-normal text-[#64748B] mt-0.5">250 € / Mo</div>
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 text-[#334155]">
            <tr class="hover:bg-slate-50/80 transition-colors">
              <td class="p-4 font-semibold text-[#0F172A]">Umfang Inhaltsseiten</td>
              <td class="p-4 text-center font-bold text-[#2563EB] bg-blue-50/40 border-x border-blue-200/40">Bis zu 6 Seiten</td>
              <td class="p-4 text-center">Bis zu 5 Seiten</td>
              <td class="p-4 text-center font-bold">Bis zu 7 Seiten</td>
              <td class="p-4 text-center text-[#64748B]">Bewerber-Landingpage</td>
              <td class="p-4 text-center text-[#64748B]">— (Laufende Pflege)</td>
            </tr>

            <tr class="hover:bg-slate-50/80 transition-colors">
              <td class="p-4 font-semibold text-[#0F172A]">Kunden-Vorabfilter mit Foto-Upload</td>
              <td class="p-4 text-center font-bold text-emerald-600 bg-blue-50/40 border-x border-blue-200/40"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Inklusive</td>
              <td class="p-4 text-center text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Inklusive</td>
              <td class="p-4 text-center text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Inklusive</td>
              <td class="p-4 text-center text-slate-400">—</td>
              <td class="p-4 text-center text-[#64748B]">Wartung &amp; Pflege</td>
            </tr>

            <tr class="hover:bg-slate-50/80 transition-colors">
              <td class="p-4 font-semibold text-[#0F172A]">Schlüsselfertige Meister-Fachtexte</td>
              <td class="p-4 text-center font-bold text-emerald-600 bg-blue-50/40 border-x border-blue-200/40"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Alle Seiten</td>
              <td class="p-4 text-center text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Hauptgewerk</td>
              <td class="p-4 text-center text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Kunden + Recruiting</td>
              <td class="p-4 text-center text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Recruiting-Texte</td>
              <td class="p-4 text-center text-[#64748B]">Aktualisierung auf Zuruf</td>
            </tr>

            <tr class="hover:bg-slate-50/80 transition-colors">
              <td class="p-4 font-semibold text-[#0F172A]">60-Sekunden-Recruiting-Trichter</td>
              <td class="p-4 text-center text-slate-400 bg-blue-50/40 border-x border-blue-200/40">Optional (+1.200 €)</td>
              <td class="p-4 text-center text-slate-400">Optional</td>
              <td class="p-4 text-center font-bold text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Voll integriert</td>
              <td class="p-4 text-center font-bold text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Kernfunktion</td>
              <td class="p-4 text-center text-[#64748B]">Wartung &amp; Pflege</td>
            </tr>

            <tr class="hover:bg-slate-50/80 transition-colors">
              <td class="p-4 font-semibold text-[#0F172A]">5 Baustellen-NFC-Bewertungskarten</td>
              <td class="p-4 text-center font-bold text-emerald-600 bg-blue-50/40 border-x border-blue-200/40"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> 5 Karten inkl.</td>
              <td class="p-4 text-center text-slate-400">Optional nachrüstbar</td>
              <td class="p-4 text-center font-bold text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> 5 Karten inkl.</td>
              <td class="p-4 text-center text-slate-400">—</td>
              <td class="p-4 text-center text-[#64748B]">—</td>
            </tr>

            <tr class="hover:bg-slate-50/80 transition-colors">
              <td class="p-4 font-semibold text-[#0F172A]">Google Unternehmensprofil &amp; Local SEO OWL</td>
              <td class="p-4 text-center font-bold text-emerald-600 bg-blue-50/40 border-x border-blue-200/40"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Inklusive</td>
              <td class="p-4 text-center text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Basis-Setup</td>
              <td class="p-4 text-center font-bold text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Erweitert</td>
              <td class="p-4 text-center text-slate-400">—</td>
              <td class="p-4 text-center text-[#64748B]">Laufende Pflege</td>
            </tr>

            <tr class="hover:bg-slate-50/80 transition-colors">
              <td class="p-4 font-semibold text-[#0F172A]">Google Jobs Schema &amp; Vektor-QR-Codes</td>
              <td class="p-4 text-center text-slate-400 bg-blue-50/40 border-x border-blue-200/40">—</td>
              <td class="p-4 text-center text-slate-400">—</td>
              <td class="p-4 text-center font-bold text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Inklusive</td>
              <td class="p-4 text-center font-bold text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> Inklusive</td>
              <td class="p-4 text-center text-[#64748B]">—</td>
            </tr>

            <tr class="hover:bg-slate-50/80 transition-colors">
              <td class="p-4 font-semibold text-[#0F172A]">Quellcode-Eigentum &amp; Freie Hoster-Wahl</td>
              <td class="p-4 text-center font-bold text-emerald-600 bg-blue-50/40 border-x border-blue-200/40"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> 100 % Eigentum</td>
              <td class="p-4 text-center text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> 100 % Eigentum</td>
              <td class="p-4 text-center font-bold text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> 100 % Eigentum</td>
              <td class="p-4 text-center text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> 100 % Eigentum</td>
              <td class="p-4 text-center text-slate-400">Jederzeit kündbar</td>
            </tr>

            <tr class="hover:bg-slate-50/80 transition-colors">
              <td class="p-4 font-semibold text-[#0F172A]">Monatliches Änderungsservice-Kontingent</td>
              <td class="p-4 text-center text-slate-400 bg-blue-50/40 border-x border-blue-200/40">Im Systembetrieb</td>
              <td class="p-4 text-center text-slate-400">Im Systembetrieb</td>
              <td class="p-4 text-center text-slate-400">Im Systembetrieb</td>
              <td class="p-4 text-center text-slate-400">—</td>
              <td class="p-4 text-center font-bold text-emerald-600"><i data-lucide="check" class="w-4 h-4 mx-auto"></i> 60 Min. / Monat</td>
            </tr>
          </tbody>
          <tfoot>
            <tr class="bg-slate-50 border-t border-slate-200">
              <td class="p-4 font-bold text-[#0F172A]">Aktion</td>
              <td class="p-4 text-center bg-blue-50/70 border-x border-blue-200/60">
                <a href="anfrage.html" class="inline-block bg-[#2563EB] hover:bg-blue-700 text-white font-bold px-4 py-2 rounded-xl text-xs transition-all shadow-xs">
                  Auswählen →
                </a>
              </td>
              <td class="p-4 text-center">
                <a href="anfrage.html" class="inline-block bg-amber-600 hover:bg-amber-700 text-white font-bold px-4 py-2 rounded-xl text-xs transition-all shadow-xs">
                  Prüfen →
                </a>
              </td>
              <td class="p-4 text-center">
                <a href="anfrage.html" class="inline-block bg-slate-900 hover:bg-slate-800 text-white font-bold px-4 py-2 rounded-xl text-xs transition-all shadow-xs">
                  Auswählen →
                </a>
              </td>
              <td class="p-4 text-center">
                <a href="anfrage.html" class="inline-block bg-slate-100 hover:bg-slate-200 text-[#0F172A] font-bold px-4 py-2 rounded-xl text-xs transition-all">
                  Anfragen →
                </a>
              </td>
              <td class="p-4 text-center">
                <a href="anfrage.html" class="inline-block bg-slate-100 hover:bg-slate-200 text-[#0F172A] font-bold px-4 py-2 rounded-xl text-xs transition-all">
                  Buchen →
                </a>
              </td>
            </tr>
          </tfoot>
        </table>
      </div>
    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- 9. EIGENTUMSRECHTE & FAIRE LEISTUNGSGRENZEN                    -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="leistungsgrenzen" class="space-y-10 scroll-mt-28">
    <div class="text-center max-w-3xl mx-auto space-y-3">
      <span class="text-xs font-mono font-bold text-slate-500 uppercase tracking-wider bg-slate-100 px-3 py-1 rounded-full border border-slate-200">
        Rechtliche Klarheit &amp; Sicherheit
      </span>
      <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-[#0F172A]">
        Eigentumsrechte &amp; faire Leistungsgrenzen
      </h2>
      <p data-aos="fade-up" data-aos-delay="100" class="text-sm sm:text-base text-[#475569] leading-relaxed">
        Wir sprechen Handwerker-Klartext: Was SparrenWeb liefert und was wir bewusst nicht versprechen.
      </p>
    </div>

    <div class="grid md:grid-cols-2 gap-8">
      
      <!-- Eigentum -->
      <div data-aos="fade-up" class="bg-white rounded-3xl border-2 border-emerald-500/40 p-8 space-y-4 shadow-sm card-lift">
        <div class="flex items-center gap-2.5 text-emerald-700 font-bold text-sm">
          <div class="w-8 h-8 rounded-xl bg-emerald-50 flex items-center justify-center text-emerald-600">
            <i data-lucide="shield-check" class="w-5 h-5"></i>
          </div>
          <span class="text-base text-[#0F172A]">100 % Eigentum &amp; volle Nutzungsrechte</span>
        </div>
        <p class="text-xs text-[#475569] leading-relaxed">
          Nach Begleichung des vereinbarten Festpreises gehört Ihnen die gesamte Website uneingeschränkt:
        </p>
        <ul class="space-y-2.5 text-xs text-[#334155]">
          <li class="flex items-start gap-2">
            <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
            <span><strong>Vollständiger Quellcode:</strong> HTML5, CSS und JavaScript ohne proprietäre Verschlüsselung oder Bindung an ein geschlossenes System.</span>
          </li>
          <li class="flex items-start gap-2">
            <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
            <span><strong>Freie Provider-Wahl:</strong> Sie können das System auf jedem Webhoster Ihrer Wahl betreiben oder auf unseren Servern belassen.</span>
          </li>
          <li class="flex items-start gap-2">
            <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
            <span><strong>Dauerhaftes Nutzungsrecht:</strong> Alle erstellten Fachtexte und grafischen Ausarbeitungen stehen Ihrem Handwerksbetrieb zeitlich unbegrenzt zu.</span>
          </li>
        </ul>
      </div>

      <!-- Leistungsgrenzen -->
      <div data-aos="fade-up" data-aos-delay="100" class="bg-white rounded-3xl border-2 border-slate-200 p-8 space-y-4 shadow-sm card-lift">
        <div class="flex items-center gap-2.5 text-slate-800 font-bold text-sm">
          <div class="w-8 h-8 rounded-xl bg-amber-50 flex items-center justify-center text-amber-600">
            <i data-lucide="alert-circle" class="w-5 h-5"></i>
          </div>
          <span class="text-base text-[#0F172A]">Was wir bewusst ausschließen (Ehrlichkeit vor Märchen)</span>
        </div>
        <p class="text-xs text-[#475569] leading-relaxed">
          Seriosität im Handwerk bedeutet, keine falschen Marketing-Märchen zu erzählen:
        </p>
        <ul class="space-y-2.5 text-xs text-[#334155]">
          <li class="flex items-start gap-2">
            <i data-lucide="x" class="w-4 h-4 text-amber-600 shrink-0 mt-0.5"></i>
            <span><strong>Keine unbegrenzte Flatrate:</strong> Das Änderungsservice-Kontingent im Systembetrieb umfasst 60 Min./Monat. Größere Neuentwicklungen werden fair nach Aufwand kalkuliert.</span>
          </li>
          <li class="flex items-start gap-2">
            <i data-lucide="x" class="w-4 h-4 text-amber-600 shrink-0 mt-0.5"></i>
            <span><strong>Keine Rechtsberatung:</strong> Wir setzen technische DSGVO-Standards sauber um, ersetzen aber keine individuelle Rechtsberatung durch einen Anwalt.</span>
          </li>
          <li class="flex items-start gap-2">
            <i data-lucide="x" class="w-4 h-4 text-amber-600 shrink-0 mt-0.5"></i>
            <span><strong>Keine Platz-1-Garantien:</strong> Wir optimieren alle OnPage- und Schema-Faktoren seriös, garantieren aber keine willkürlichen Google-Erstplatzierungen gegen den Algorithmus.</span>
          </li>
        </ul>
      </div>

    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- 10. INTERAKTIVES FAQ-ACCORDION                                -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="faq" class="space-y-8 scroll-mt-28">
    <div class="text-center max-w-3xl mx-auto space-y-3">
      <span class="text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider bg-blue-50 px-3 py-1 rounded-full border border-blue-200">
        Häufige Fragen
      </span>
      <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-[#0F172A]">
        Fragen zu Preisen, Ablauf &amp; Konditionen
      </h2>
      <p data-aos="fade-up" data-aos-delay="100" class="text-sm sm:text-base text-[#475569] leading-relaxed">
        Klartext-Antworten auf die wichtigsten Fragen von Handwerksmeistern aus OWL.
      </p>
    </div>

    <div data-aos="fade-up" class="max-w-3xl mx-auto space-y-3">
      
      <!-- FAQ 1 -->
      <div class="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-2xs">
        <button type="button" onclick="toggleFaq(1)" class="w-full text-left p-4 sm:p-5 flex items-center justify-between gap-4 font-bold text-xs sm:text-sm text-[#0F172A] hover:bg-slate-50 transition-colors">
          <span>Gibt es versteckte Folgekosten oder ein verpflichtendes Monatsabo?</span>
          <i id="faqIcon1" data-lucide="chevron-down" class="w-4 h-4 text-[#2563EB] shrink-0 transition-transform"></i>
        </button>
        <div id="faqContent1" class="hidden px-5 pb-5 pt-1 text-xs text-[#475569] leading-relaxed border-t border-slate-100">
          Nein. Der Website-Kauf (Meister-System für 2.800 € netto oder Pilot für 1.500 € netto) ist eine einmalige Festpreis-Investition. Nach der Schlusszahlung gehört Ihnen das gesamte System zu 100 %. Der regionale Systembetrieb (250 € netto/Monat) ist ein rein optionales Angebot und jederzeit monatlich kündbar.
        </div>
      </div>

      <!-- FAQ 2 -->
      <div class="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-2xs">
        <button type="button" onclick="toggleFaq(2)" class="w-full text-left p-4 sm:p-5 flex items-center justify-between gap-4 font-bold text-xs sm:text-sm text-[#0F172A] hover:bg-slate-50 transition-colors">
          <span>Wie funktioniert die Zahlung (50/50 Split oder Dreiteilung)?</span>
          <i id="faqIcon2" data-lucide="chevron-down" class="w-4 h-4 text-[#2563EB] shrink-0 transition-transform"></i>
        </button>
        <div id="faqContent2" class="hidden px-5 pb-5 pt-1 text-xs text-[#475569] leading-relaxed border-t border-slate-100">
          Als Standard gilt das faire 50/50-Modell: 50 % bei Auftragsstart, 50 % erst nach vollständiger Endabnahme und Go-Live. Auf Wunsch bieten wir etablierten Betrieben auch eine individuelle Dreiteilung an: 1.400 € bei Start, 700 € nach Vorab-Entwurf und 700 € bei Go-Live. Alle Preise verstehen sich netto zzgl. gesetzlicher MwSt.
        </div>
      </div>

      <!-- FAQ 3 -->
      <div class="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-2xs">
        <button type="button" onclick="toggleFaq(3)" class="w-full text-left p-4 sm:p-5 flex items-center justify-between gap-4 font-bold text-xs sm:text-sm text-[#0F172A] hover:bg-slate-50 transition-colors">
          <span>Wie viel Zeit muss ich als Meister tatsächlich investieren?</span>
          <i id="faqIcon3" data-lucide="chevron-down" class="w-4 h-4 text-[#2563EB] shrink-0 transition-transform"></i>
        </button>
        <div id="faqContent3" class="hidden px-5 pb-5 pt-1 text-xs text-[#475569] leading-relaxed border-t border-slate-100">
          Ihr Gesamtaufwand beträgt in der Regel ca. 90 Minuten: Ein 30-minütiges telefonisches Interview zu Ihren Schwerpunkten und Wunschkunden, das Zusenden Ihrer Firmenfotos und Logodateien per WhatsApp/E-Mail (ca. 15 Min.) und eine 45-minütige gemeinsame Endabnahme vor der Freischaltung. Sämtliche Fachtexte erstellen wir schlüsselfertig für Ihr Gewerk.
        </div>
      </div>

      <!-- FAQ 4 -->
      <div class="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-2xs">
        <button type="button" onclick="toggleFaq(4)" class="w-full text-left p-4 sm:p-5 flex items-center justify-between gap-4 font-bold text-xs sm:text-sm text-[#0F172A] hover:bg-slate-50 transition-colors">
          <span>Was unterscheidet den OWL-Pilot (1.500 €) vom Meister-System (2.800 €)?</span>
          <i id="faqIcon4" data-lucide="chevron-down" class="w-4 h-4 text-[#2563EB] shrink-0 transition-transform"></i>
        </button>
        <div id="faqContent4" class="hidden px-5 pb-5 pt-1 text-xs text-[#475569] leading-relaxed border-t border-slate-100">
          Der Pilot (Angebot A) ist auf genau 3 Handwerksbetriebe in Ostwestfalen-Lippe limitiert (maximal ein Betrieb pro Gewerk). Sie erhalten das vollständige System mit 1.300 € Preisnachlass und verpflichten sich im Gegenzug zu einem kurzen 15-Minuten-Feedbackgespräch nach 60 Tagen und der Freigabe als regionale Referenz. Das Meister-System (Angebot B) umfasst zusätzlich 6 Inhaltsseiten und 5 physische Baustellen-NFC-Karten.
        </div>
      </div>

      <!-- FAQ 5 -->
      <div class="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-2xs">
        <button type="button" onclick="toggleFaq(5)" class="w-full text-left p-4 sm:p-5 flex items-center justify-between gap-4 font-bold text-xs sm:text-sm text-[#0F172A] hover:bg-slate-50 transition-colors">
          <span>Was passiert, wenn ich nach 2 Jahren den Hosting-Provider wechseln will?</span>
          <i id="faqIcon5" data-lucide="chevron-down" class="w-4 h-4 text-[#2563EB] shrink-0 transition-transform"></i>
        </button>
        <div id="faqContent5" class="hidden px-5 pb-5 pt-1 text-xs text-[#475569] leading-relaxed border-t border-slate-100">
          Das System basiert auf standardkonformem HTML5, modernem CSS und JavaScript – ganz ohne proprietäre Plattform-Zwänge (kein Wix, kein Shopify, kein modifiziertes Theme). Sie können Ihre Website jederzeit zu Strato, Ionos, Hetzner oder jedem anderen Webhoster umziehen.
        </div>
      </div>

    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- 11. FINALER CALL TO ACTION BANNER                             -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section data-aos="fade-up" class="bg-gradient-to-br from-blue-900 via-[#2563EB] to-blue-800 text-white rounded-3xl p-8 sm:p-12 shadow-2xl relative overflow-hidden">
    <div class="max-w-3xl mx-auto text-center space-y-6 relative z-10">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/10 text-white text-xs font-mono font-bold border border-white/20">
        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
        <span>100 % unverbindlicher Vorab-Entwurf</span>
      </div>

      <h2 class="text-2xl sm:text-4xl font-extrabold tracking-tight">
        Bereit für planbare Premium-Aufträge und echte Entlastung?
      </h2>

      <p class="text-xs sm:text-base text-blue-100 leading-relaxed max-w-2xl mx-auto">
        Lassen Sie uns in einem kurzen 15-minütigen Gespräch über Ihren Betrieb sprechen. Wir erstellen Ihren unverbindlichen Vorab-Entwurf inklusive Fachtexten für Ihr Gewerk – erst ansehen, dann entscheiden.
      </p>

      <div class="pt-2 flex flex-col sm:flex-row items-center justify-center gap-3">
        <a href="anfrage.html" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-white hover:bg-slate-100 text-[#0F172A] font-bold text-sm px-8 py-4 rounded-2xl transition-all shadow-lg hover:-translate-y-0.5">
          <span>Kostenlosen Vorab-Entwurf anfordern</span>
          <i data-lucide="arrow-right" class="w-4 h-4 text-[#2563EB]"></i>
        </a>
      </div>

      <div class="text-[11px] text-blue-200 pt-2 flex flex-wrap items-center justify-center gap-4">
        <span>✓ Fester B2B-Festpreis</span>
        <span>✓ 0 Min. Schreibaufwand</span>
        <span>✓ In 14 Werktagen startklar</span>
      </div>
    </div>
  </section>

</main>
"""

    script_content = """
<script>
  // 1. Zahlungsmodell-Umschalter im Meister-System
  function setPayModel(model) {
    const btnSplit = document.getElementById('payModelSplit');
    const btnThree = document.getElementById('payModelThree');
    const explBox = document.getElementById('payExplBox');
    
    if (model === 'three') {
      if (btnSplit) {
        btnSplit.classList.remove('bg-white', 'text-[#2563EB]', 'font-bold', 'shadow-2xs', 'border');
        btnSplit.classList.add('text-slate-600');
      }
      if (btnThree) {
        btnThree.classList.add('bg-white', 'text-[#2563EB]', 'font-bold', 'shadow-2xs', 'border');
        btnThree.classList.remove('text-slate-600');
      }
      if (explBox) {
        explBox.innerHTML = '<strong>Individuelle 3-Raten-Vereinbarung:</strong> 1.400 € netto bei Auftragsstart, 700 € netto nach Fertigstellung und Prüfung des Vorab-Entwurfs sowie 700 € netto erst nach vollständiger Endabnahme und Go-Live.';
      }
    } else {
      if (btnSplit) {
        btnSplit.classList.add('bg-white', 'text-[#2563EB]', 'font-bold', 'shadow-2xs', 'border');
        btnSplit.classList.remove('text-slate-600');
      }
      if (btnThree) {
        btnThree.classList.remove('bg-white', 'text-[#2563EB]', 'font-bold', 'shadow-2xs', 'border');
        btnThree.classList.add('text-slate-600');
      }
      if (explBox) {
        explBox.innerHTML = '<strong>Faires Zahlungsmodell 50/50:</strong> Sie zahlen 50 % bei Projektstart (1.400 € netto) zur Deckung der Konzeption & Textarbeit. Die zweiten 50 % (1.400 € netto) werden <em>erst nach vollständiger Funktionsprüfung, Ihrer persönlichen Freigabe und erfolgreichem Go-Live</em> fällig.';
      }
    }
  }

  // 2. Recruiting Simulator Steuerung
  let recRole = 'Anlagenmechaniker SHK';

  function setRecRole(role, btn) {
    recRole = role;
    const parent = btn.parentElement;
    if (parent) {
      parent.querySelectorAll('.rec-role-btn').forEach(b => {
        b.classList.remove('active', 'border-[#2563EB]', 'bg-blue-950/50');
        b.classList.add('border-slate-800', 'bg-slate-900/60');
      });
      btn.classList.add('active', 'border-[#2563EB]', 'bg-blue-950/50');
      btn.classList.remove('border-slate-800', 'bg-slate-900/60');
    }
  }

  function goRecStep(step) {
    for (let i = 1; i <= 3; i++) {
      const el = document.getElementById(`recSimStep${i}`);
      if (el) el.classList.add('hidden');
    }
    const success = document.getElementById('recSimSuccess');
    if (success) success.classList.add('hidden');

    const target = document.getElementById(`recSimStep${step}`);
    if (target) target.classList.remove('hidden');
  }

  function finishRecSim() {
    for (let i = 1; i <= 3; i++) {
      const el = document.getElementById(`recSimStep${i}`);
      if (el) el.classList.add('hidden');
    }
    const success = document.getElementById('recSimSuccess');
    if (success) success.classList.remove('hidden');
  }

  // 3. Vorabfilter Demo Steuerung
  let currentDemoStep = 1;
  const demoData = {
    proj: 'Komplettbad-Sanierung',
    dim: 'ca. 14 m², Bj. 1982',
    loc: '33615 Bielefeld',
    time: 'In den nächsten 2–4 Monaten',
    contact: 'Familie Schulze · 0521 987654',
    margin: '~68 %'
  };

  function switchDemoTab(tab) {
    const tabCust = document.getElementById('tabContentCustomer');
    const tabMast = document.getElementById('tabContentMaster');
    const btnCust = document.getElementById('btnViewCustomer');
    const btnMast = document.getElementById('btnViewMaster');

    if (tab === 'master') {
      if (tabCust) tabCust.classList.add('hidden');
      if (tabMast) tabMast.classList.remove('hidden');
      if (btnCust) {
        btnCust.classList.remove('bg-[#2563EB]', 'text-white', 'shadow-xs');
        btnCust.classList.add('text-slate-300');
      }
      if (btnMast) {
        btnMast.classList.add('bg-[#2563EB]', 'text-white', 'shadow-xs');
        btnMast.classList.remove('text-slate-300');
      }
      // Update values
      const resProj = document.getElementById('masterResProj');
      const resLoc = document.getElementById('masterResLoc');
      const resDim = document.getElementById('masterResDim');
      const resTime = document.getElementById('masterResTime');
      const resContact = document.getElementById('masterResContact');
      const resMargin = document.getElementById('masterResMargin');

      if (resProj) resProj.textContent = demoData.proj;
      if (resLoc) resLoc.textContent = document.getElementById('demoInputLoc')?.value || demoData.loc;
      if (resDim) resDim.textContent = document.getElementById('demoInputDim')?.value || demoData.dim;
      if (resTime) resTime.textContent = document.getElementById('demoInputTime')?.value || demoData.time;
      if (resContact) resContact.textContent = document.getElementById('demoInputContact')?.value || demoData.contact;
      if (resMargin) resMargin.textContent = 'Deckungsbeitrag ' + demoData.margin;
    } else {
      if (tabCust) tabCust.classList.remove('hidden');
      if (tabMast) tabMast.classList.add('hidden');
      if (btnCust) {
        btnCust.classList.add('bg-[#2563EB]', 'text-white', 'shadow-xs');
        btnCust.classList.remove('text-slate-300');
      }
      if (btnMast) {
        btnMast.classList.remove('bg-[#2563EB]', 'text-white', 'shadow-xs');
        btnMast.classList.add('text-slate-300');
      }
    }
  }

  function goDemoStep(step) {
    currentDemoStep = step;
    for (let i = 1; i <= 3; i++) {
      const el = document.getElementById(`demoStep${i}`);
      if (el) {
        if (i === step) el.classList.remove('hidden');
        else el.classList.add('hidden');
      }
    }
    const indicator = document.getElementById('demoStepIndicator');
    if (indicator) {
      const labels = ['Projekt auswählen', 'Fotos & Maße', 'Zeitplan & Kontakt'];
      indicator.textContent = `Schritt ${step} von 3: ${labels[step - 1]}`;
    }
  }

  function setDemoOption(key, val, dimDef, marginDef, btn) {
    demoData[key] = val;
    demoData.dim = dimDef;
    demoData.margin = marginDef;
    const inputDim = document.getElementById('demoInputDim');
    if (inputDim) inputDim.value = dimDef;

    const parent = btn.parentElement;
    if (parent) {
      parent.querySelectorAll('.demo-opt-btn').forEach(b => {
        b.classList.remove('active', 'border-[#2563EB]', 'bg-blue-950/40');
        b.classList.add('border-slate-800', 'bg-slate-900/60');
      });
      btn.classList.add('active', 'border-[#2563EB]', 'bg-blue-950/40');
      btn.classList.remove('border-slate-800', 'bg-slate-900/60');
    }
  }

  // 4. Systembetrieb Billing Cycle Toggle
  function setBillingCycle(cycle) {
    const btnM = document.getElementById('billToggleMonth');
    const btnY = document.getElementById('billToggleYear');
    const priceSys = document.getElementById('priceSysOp');
    const priceSysSuffix = document.getElementById('priceSysOpSuffix');
    const priceSysNote = document.getElementById('priceSysOpNote');
    const priceKombi = document.getElementById('priceKombiOp');
    const priceKombiSuffix = document.getElementById('priceKombiOpSuffix');
    const priceKombiNote = document.getElementById('priceKombiOpNote');

    if (cycle === 'year') {
      if (btnM) {
        btnM.classList.remove('bg-white', 'text-[#2563EB]', 'shadow-xs', 'border');
        btnM.classList.add('text-slate-600');
      }
      if (btnY) {
        btnY.classList.add('bg-white', 'text-[#2563EB]', 'shadow-xs', 'border');
        btnY.classList.remove('text-slate-600');
      }
      if (priceSys) priceSys.textContent = '225 €';
      if (priceSysSuffix) priceSysSuffix.textContent = 'netto / Mo (2.700 € / Jahr)';
      if (priceSysNote) priceSysNote.textContent = '10 % Ersparnis (300 € gespart bei Vorauszahlung)';
      if (priceKombi) priceKombi.textContent = '440 €';
      if (priceKombiSuffix) priceKombiSuffix.textContent = 'netto / Mo (5.280 € / Jahr)';
      if (priceKombiNote) priceKombiNote.textContent = '10 % Ersparnis (600 € gespart bei Vorauszahlung)';
    } else {
      if (btnM) {
        btnM.classList.add('bg-white', 'text-[#2563EB]', 'shadow-xs', 'border');
        btnM.classList.remove('text-slate-600');
      }
      if (btnY) {
        btnY.classList.remove('bg-white', 'text-[#2563EB]', 'shadow-xs', 'border');
        btnY.classList.add('text-slate-600');
      }
      if (priceSys) priceSys.textContent = '250 €';
      if (priceSysSuffix) priceSysSuffix.textContent = 'netto / Monat';
      if (priceSysNote) priceSysNote.textContent = 'Flexibel monatlich kündbar · Keine Mindestlaufzeit';
      if (priceKombi) priceKombi.textContent = '490 €';
      if (priceKombiSuffix) priceKombiSuffix.textContent = 'netto / Monat';
      if (priceKombiNote) priceKombiNote.textContent = '250 € Systembetrieb + 240 € Social-Media-Betreuung';
    }
  }

  // 5. FAQ Accordion Toggle
  function toggleFaq(num) {
    const content = document.getElementById(`faqContent${num}`);
    const icon = document.getElementById(`faqIcon${num}`);
    if (content) {
      const isHidden = content.classList.contains('hidden');
      if (isHidden) {
        content.classList.remove('hidden');
        if (icon) icon.style.transform = 'rotate(180deg)';
      } else {
        content.classList.add('hidden');
        if (icon) icon.style.transform = 'rotate(0deg)';
      }
    }
  }
</script>
"""
    return head + navbar + main_html + script_content + footer

if __name__ == "__main__":
    html = build_leistungen()
    with open("leistungen.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("leistungen.html erfolgreich generiert.")
