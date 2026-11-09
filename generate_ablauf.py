#!/usr/bin/env python3
"""
generate_ablauf.py
Generiert ablauf.html vollständig konsistent:
- 12-Stufen-Prozess (14-Tage-Ziel, 90 Minuten Meister-Aufwand)
- Neuer ROI- & Amortisationsrechner nach Kapitel 10
- System-Vergleichstabelle (Mietagenturen vs. WordPress vs. SparrenWeb)
- Vollständiges FAQ mit 13 Kernfragen
"""

import builder_helper

def build_ablauf():
    title = "Ablauf, ROI-Rechner & FAQ | SparrenWeb Bielefeld & OWL"
    description = "Der schlüsselfertige 14-Tage-Ablauf: Nur 90 Minuten Gesamtaufwand für den Meister. Interaktiver ROI- & Amortisationsrechner für Handwerksbetriebe und alle 13 FAQ-Antworten."
    canonical = "ablauf.html"

    head = builder_helper.get_head(title, description, canonical)
    navbar = builder_helper.get_navbar("ablauf.html")
    footer = builder_helper.get_footer()

    main_html = """
<!-- Hero Section -->
<header class="pt-32 sm:pt-40 pb-16 sm:pb-24 px-4 sm:px-6 relative overflow-hidden bg-white border-b border-slate-200">
  <div class="max-w-5xl mx-auto text-center space-y-6 relative z-10">
    <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-200/80 text-blue-700 text-xs font-mono font-bold tracking-wider uppercase mb-2">
      <span class="w-2 h-2 rounded-full bg-[#2563EB] animate-pulse"></span>
      14-Tage-Ziel · Maximal 90 Minuten Aufwand für Sie
    </div>

    <h1 data-aos="fade-up" data-aos-duration="700" class="text-3xl sm:text-5xl lg:text-6xl font-extrabold text-[#0F172A] tracking-tight leading-tight">
      Ablauf, <span class="text-[#2563EB]">ROI-Rechner</span> &amp; alle Fakten
    </h1>

    <p data-aos="fade-up" data-aos-delay="100" data-aos-duration="700" class="text-base sm:text-lg text-[#334155] leading-relaxed max-w-3xl mx-auto">
      Keine monatelangen Agentur-Meetings, keine zähen Textentwürfe. Wir wissen, wie voll Ihr Terminkalender ist: In 14 Werktagen steht Ihr Meister-Auftrags-System schlüsselfertig bereit.
    </p>

    <!-- Quick Nav Anchors -->
    <div data-aos="fade-up" data-aos-delay="200" class="pt-2 flex flex-wrap justify-center gap-2 sm:gap-3 text-xs font-semibold">
      <a href="#prozess" class="px-4 py-2 rounded-full bg-blue-50 border border-blue-200 text-[#2563EB] hover:bg-blue-100 transition-colors">
        Der 12-Stufen-Ablauf
      </a>
      <a href="#roi-rechner" class="px-4 py-2 rounded-full bg-slate-50 border border-slate-200 text-[#0F172A] hover:bg-slate-100 transition-colors">
        Interaktiver ROI- &amp; Amortisationsrechner
      </a>
      <a href="#vergleich" class="px-4 py-2 rounded-full bg-slate-50 border border-slate-200 text-[#0F172A] hover:bg-slate-100 transition-colors">
        System-Vergleichstabelle
      </a>
      <a href="#faq" class="px-4 py-2 rounded-full bg-slate-50 border border-slate-200 text-[#0F172A] hover:bg-slate-100 transition-colors">
        Häufige Fragen (13 FAQ)
      </a>
    </div>
  </div>
</header>

<main class="py-16 px-4 sm:px-6 max-w-6xl mx-auto space-y-24">

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- SEKTION 1: DER 12-STUFEN-ABLAUF (90 MINUTEN MEISTER-AUFWAND)    -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="prozess" class="space-y-12 scroll-mt-28">
    <div class="text-center max-w-3xl mx-auto space-y-3">
      <span class="text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider bg-blue-50 px-3 py-1 rounded-full border border-blue-200">
        Präziser Zeitplan · 14 Werktage
      </span>
      <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-[#0F172A]">
        In 12 klaren Stufen zum schlüsselfertigen Meister-System
      </h2>
      <p data-aos="fade-up" data-aos-delay="100" class="text-sm sm:text-base text-[#475569] leading-relaxed">
        Sie investieren insgesamt genau 90 Minuten persönliche Zeit – den gesamten Rest übernimmt SparrenWeb.
      </p>
    </div>

    <!-- Die 3 Phasen à 30 Minuten -->
    <div class="grid md:grid-cols-3 gap-6 text-left">
      <div class="bg-blue-50/60 rounded-3xl p-6 sm:p-7 border border-blue-200 space-y-4">
        <div class="flex items-center justify-between">
          <span class="w-8 h-8 rounded-xl bg-[#2563EB] text-white flex items-center justify-center font-bold text-xs font-mono">P1</span>
          <span class="text-xs font-bold text-[#2563EB] font-mono">30 Min. Aufwand</span>
        </div>
        <h3 class="text-lg font-bold text-[#0F172A]">Phase 1: Auftakt &amp; Identität</h3>
        <p class="text-xs text-[#475569] leading-relaxed">
          30-minütiges Telefoninterview oder Treffen in Bielefeld. Wir erfassen Ihre Wunsch-Aufträge, Ihr Gewerk und trennen rentables Geschäft von unliebsamen Zeitfressern.
        </p>
        <div class="text-[11px] font-medium text-blue-950 pt-2 border-t border-blue-200/60">
          Stufen 1 bis 4: Erstgespräch, Konzept, Fachtexte, Vorabfilter-Setup.
        </div>
      </div>

      <div class="bg-slate-50 rounded-3xl p-6 sm:p-7 border border-slate-200 space-y-4">
        <div class="flex items-center justify-between">
          <span class="w-8 h-8 rounded-xl bg-slate-900 text-white flex items-center justify-center font-bold text-xs font-mono">P2</span>
          <span class="text-xs font-bold text-slate-700 font-mono">30 Min. Aufwand</span>
        </div>
        <h3 class="text-lg font-bold text-[#0F172A]">Phase 2: Entwurf-Review</h3>
        <p class="text-xs text-[#475569] leading-relaxed">
          Sie erhalten einen vollständigen, interaktiven System-Entwurf auf dem Smartphone. Im 30-Minuten-Screen-Share gehen wir Ihre Rückmeldungen und Wünsche durch.
        </p>
        <div class="text-[11px] font-medium text-slate-800 pt-2 border-t border-slate-200">
          Stufen 5 bis 8: Klick-Entwurf, Bild-/Logomaterial, Feinschliff, SEO-Setup.
        </div>
      </div>

      <div class="bg-emerald-50/60 rounded-3xl p-6 sm:p-7 border border-emerald-200 space-y-4">
        <div class="flex items-center justify-between">
          <span class="w-8 h-8 rounded-xl bg-emerald-600 text-white flex items-center justify-center font-bold text-xs font-mono">P3</span>
          <span class="text-xs font-bold text-emerald-800 font-mono">30 Min. Aufwand</span>
        </div>
        <h3 class="text-lg font-bold text-[#0F172A]">Phase 3: Abnahme &amp; Start</h3>
        <p class="text-xs text-[#475569] leading-relaxed">
          Letzte 30 Minuten für Endabnahme und DNS-Aufschaltung. Sie erhalten alle Zugänge und 100 % Eigentum; optional startet unser monatlicher Systembetrieb.
        </p>
        <div class="text-[11px] font-medium text-emerald-950 pt-2 border-t border-emerald-200/60">
          Stufen 9 bis 12: QA-Test, Mobil-Optimierung, Go-Live (14 Tage) &amp; Übergabe.
        </div>
      </div>
    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- SEKTION 2: ROI- & AMORTISATIONSRECHNER (KAPITEL 10)           -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="roi-rechner" class="space-y-10 scroll-mt-28">
    <div class="text-center max-w-3xl mx-auto space-y-3">
      <span class="text-xs font-mono font-bold text-[#2563EB] uppercase tracking-wider bg-blue-50 px-3 py-1 rounded-full border border-blue-200">
        Kaufmännische Wirtschaftlichkeit
      </span>
      <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-[#0F172A]">
        Interaktiver ROI- &amp; Amortisationsrechner
      </h2>
      <p data-aos="fade-up" data-aos-delay="100" class="text-sm sm:text-base text-[#475569] leading-relaxed">
        Berechnen Sie exakt, ab wie vielen zusätzlichen qualifizierten Aufträgen sich das SparrenWeb Meister-System für Ihren Betrieb bezahlt macht.
      </p>
    </div>

    <!-- Rechner-Interface -->
    <div class="bg-white rounded-3xl border-2 border-slate-200 shadow-xl overflow-hidden p-6 sm:p-10 space-y-8">
      <div class="grid lg:grid-cols-12 gap-8 items-start">
        
        <!-- Eingabe-Spalte (7 Spalten) -->
        <div class="lg:col-span-7 space-y-6">
          <div class="font-bold text-[#0F172A] text-sm uppercase tracking-wider font-mono border-b border-slate-100 pb-3">
            1. Ihre Betriebsparameter &amp; Paketwahl
          </div>

          <!-- Setup-Paket Auswahl -->
          <div>
            <label class="block text-xs font-bold text-[#0F172A] mb-1.5">Gewähltes System-Setup</label>
            <select id="roiSetupPackage" onchange="calculateROI()" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 text-xs sm:text-sm text-[#0F172A] focus:outline-none focus:border-[#2563EB]">
              <option value="1500">Angebot A: OWL-Referenz-Pilot (1.500 € netto einmalig)</option>
              <option value="2800" selected>Angebot B: SparrenWeb Meister-System (2.800 € netto einmalig)</option>
              <option value="3500">Angebot E: Komplett-Kombi (3.500 € netto einmalig)</option>
            </select>
          </div>

          <!-- Monatliche Optionen -->
          <div class="grid sm:grid-cols-2 gap-4">
            <div class="p-3.5 rounded-xl border border-slate-200 bg-slate-50 space-y-2">
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="checkbox" id="roiCare250" onchange="calculateROI()" checked class="w-4 h-4 text-[#2563EB] rounded focus:ring-blue-500">
                <span class="text-xs font-bold text-[#0F172A]">Systembetrieb (+250 €/Mo)</span>
              </label>
              <p class="text-[11px] text-[#64748B] leading-tight">60 Min. Änderungsservice, Hosting &amp; Backups</p>
            </div>

            <div class="p-3.5 rounded-xl border border-slate-200 bg-slate-50 space-y-2">
              <label class="flex items-center gap-2 cursor-pointer">
                <input type="checkbox" id="roiAdCare240" onchange="calculateROI()" class="w-4 h-4 text-[#2563EB] rounded focus:ring-blue-500">
                <span class="text-xs font-bold text-[#0F172A]">Ad-Betreuung (+240 €/Mo)</span>
              </label>
              <p class="text-[11px] text-[#64748B] leading-tight">Social-Media-Recruiting-Kampagnen (Meta)</p>
            </div>
          </div>

          <!-- Werbebudget & Zeitraum -->
          <div class="grid sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-[#0F172A] mb-1.5">Monatliches Ad-Budget (an Meta/Google)</label>
              <select id="roiAdBudget" onchange="calculateROI()" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs text-[#0F172A]">
                <option value="0" selected>0 € (Organisch / Empfehlungen)</option>
                <option value="300">300 € / Monat</option>
                <option value="500">500 € / Monat</option>
                <option value="1000">1.000 € / Monat</option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-bold text-[#0F172A] mb-1.5">Betrachtungszeitraum</label>
              <select id="roiMonths" onchange="calculateROI()" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs text-[#0F172A]">
                <option value="6">6 Monate</option>
                <option value="12" selected>12 Monate (1 Jahr)</option>
                <option value="24">24 Monate (2 Jahre)</option>
                <option value="36">36 Monate (3 Jahre)</option>
              </select>
            </div>
          </div>

          <!-- Slider 1: Deckungsbeitrag pro Auftrag -->
          <div class="space-y-2 pt-2">
            <div class="flex justify-between items-center text-xs">
              <span class="font-bold text-[#0F172A]">Deckungsbeitrag pro typischem Zusatzauftrag:</span>
              <span id="labelMargin" class="font-mono font-bold text-[#2563EB] text-sm">3.500 €</span>
            </div>
            <input type="range" id="sliderMargin" min="500" max="15000" step="250" value="3500" oninput="calculateROI()" class="w-full accent-[#2563EB]">
            <div class="flex justify-between text-[10px] text-[#64748B]">
              <span>500 € (Reparatur)</span>
              <span>3.500 € (Heizung/Bad)</span>
              <span>15.000 € (Dach/PV)</span>
            </div>
          </div>

          <!-- Slider 2: Zusätzliche Aufträge pro Monat -->
          <div class="space-y-2">
            <div class="flex justify-between items-center text-xs">
              <span class="font-bold text-[#0F172A]">Zusätzliche qualifizierte Aufträge pro Monat:</span>
              <span id="labelDeals" class="font-mono font-bold text-[#2563EB] text-sm">1 Auftrag</span>
            </div>
            <input type="range" id="sliderDeals" min="0.5" max="8" step="0.5" value="1" oninput="calculateROI()" class="w-full accent-[#2563EB]">
            <div class="flex justify-between text-[10px] text-[#64748B]">
              <span>0,5 (alle 2 Monate)</span>
              <span>1 pro Monat</span>
              <span>8 pro Monat</span>
            </div>
          </div>

        </div>

        <!-- Ergebnis-Spalte (5 Spalten) -->
        <div class="lg:col-span-5 bg-slate-900 text-white rounded-2xl p-6 sm:p-7 space-y-6">
          <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <span class="text-xs font-mono font-bold text-blue-400 uppercase">Wirtschaftliches Ergebnis</span>
            <span id="resPeriodBadge" class="text-[10px] bg-slate-800 px-2 py-0.5 rounded text-slate-300 font-mono">12 Monate</span>
          </div>

          <!-- Großes Highlight: Reingewinn / Überschuss -->
          <div class="space-y-1">
            <div class="text-xs text-slate-400">Zusätzlicher Netto-Überschuss:</div>
            <div id="resNetProfit" class="text-3xl sm:text-4xl font-extrabold font-mono text-emerald-400">
              +36.200 €
            </div>
            <div class="text-[11px] text-slate-400">Nach Abzug aller System- und Betriebskosten</div>
          </div>

          <!-- Kennzahlen-Tabelle -->
          <div class="space-y-2.5 text-xs border-t border-slate-800 pt-4">
            <div class="flex justify-between">
              <span class="text-slate-400">Gesamte Investitionskosten:</span>
              <span id="resTotalCost" class="font-mono text-white font-semibold">5.800 €</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-400">Zusätzlicher Deckungsbeitrag:</span>
              <span id="resTotalMargin" class="font-mono text-emerald-300 font-semibold">42.000 €</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-400">Monatliche laufende Kosten:</span>
              <span id="resMonthlyCost" class="font-mono text-white">250 € / Mo</span>
            </div>
            <div class="flex justify-between pt-2 border-t border-slate-800">
              <span class="text-slate-400">Return on Investment (ROI):</span>
              <span id="resRoiPct" class="font-mono text-blue-400 font-bold text-sm">+624 %</span>
            </div>
            <div class="flex justify-between pt-1">
              <span class="text-slate-400">Amortisationszeit:</span>
              <span id="resAmort" class="font-mono text-emerald-400 font-bold text-sm">ca. 0,9 Monate</span>
            </div>
          </div>

          <div class="pt-2">
            <a href="anfrage.html" class="w-full inline-flex items-center justify-center gap-2 bg-[#2563EB] hover:bg-blue-600 text-white text-xs font-bold py-3.5 px-4 rounded-xl transition-all shadow-md">
              <span>Dieses Potenzial für meinen Betrieb sichern</span>
              <i data-lucide="arrow-right" class="w-4 h-4"></i>
            </a>
          </div>
        </div>

      </div>

      <!-- Disclaimer nach Kapitel 10 -->
      <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 text-[11px] text-[#64748B] leading-relaxed">
        <strong>Transparenter Hinweis:</strong> Diese Modellrechnung basiert auf Ihren individuellen Annahmen zu Auftragswert, Marge und zusätzlichen Kundenkontakten. Sie stellt keine garantierte Gewinnerwartung dar, sondern veranschaulicht den betriebswirtschaftlichen Hebel qualifizierter digitaler Vorabfilterung gegenüber herkömmlichen Leerfahrten und unvollständigen Anfragen. Alle Beträge in Euro netto zzgl. gesetzl. MwSt.
      </div>
    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- SEKTION 3: SYSTEM-VERGLEICHSTABELLE                           -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="vergleich" class="space-y-8 scroll-mt-28">
    <div class="text-center max-w-2xl mx-auto space-y-2">
      <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-[#0F172A]">
        Vergleich: 24-Monats-Mietknebel vs. WordPress vs. SparrenWeb
      </h2>
      <p class="text-xs sm:text-sm text-[#475569]">
        Warum etablierte Meisterbetriebe in OWL von teuren Mietverträgen zu unserem Kauf-System wechseln.
      </p>
    </div>

    <div class="bg-white rounded-3xl border border-slate-200 shadow-md overflow-hidden text-left">
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs sm:text-sm">
          <thead class="bg-slate-50 border-b border-slate-200">
            <tr>
              <th class="p-4 font-bold text-[#0F172A]">Kriterium</th>
              <th class="p-4 font-bold text-rose-700">Typische 24-Monats-Mietagentur</th>
              <th class="p-4 font-bold text-amber-800">DIY-WordPress-Baukasten</th>
              <th class="p-4 font-bold text-[#2563EB] bg-blue-50/70">SparrenWeb Meister-System</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 text-[#334155]">
            <tr>
              <td class="p-4 font-bold text-[#0F172A]">Preise &amp; Bindung</td>
              <td class="p-4 text-[#64748B]">150 € – 300 € monatlich mit 24 Monaten Mindestlaufzeit (&gt; 4.000 € Gesamtkosten)</td>
              <td class="p-4 text-[#64748B]">Geringe Serverkosten, aber 40+ Stunden unbezahlte Meisterzeit</td>
              <td class="p-4 font-bold text-emerald-700 bg-blue-50/30">Einmaliger Kauf ab 1.500 € (Pilot) bzw. 2.800 €. Betreuung monatlich kündbar.</td>
            </tr>
            <tr>
              <td class="p-4 font-bold text-[#0F172A]">Eigentum &amp; Quellcode</td>
              <td class="p-4 text-[#64748B]">Kein Eigentum: Bei Kündigung wird die Website gelöscht.</td>
              <td class="p-4 text-[#64748B]">Code gehört Ihnen, ist aber technisch verstreut und wartungsintensiv.</td>
              <td class="p-4 font-bold text-emerald-700 bg-blue-50/30">100 % Ihr Eigentum. Alle Dateien und Rechte gehören vollständig Ihrem Betrieb.</td>
            </tr>
            <tr>
              <td class="p-4 font-bold text-[#0F172A]">Ihr Zeitaufwand</td>
              <td class="p-4 text-[#64748B]">„Schreiben Sie uns bitte Texte und liefern Sie Bilder.“ (20+ Stunden)</td>
              <td class="p-4 text-[#64748B]">Wochenlanges Basteln am Feierabend oder Wochenende (50+ Stunden)</td>
              <td class="p-4 font-bold text-emerald-700 bg-blue-50/30">Maximal 90 Minuten Gesamtaufwand. Fachtexte liefern wir schlüsselfertig.</td>
            </tr>
            <tr>
              <td class="p-4 font-bold text-[#0F172A]">Kunden-Vorabfilter</td>
              <td class="p-4 text-[#64748B]">Meist nur simples Kontaktformular ohne Foto-Upload oder Gewerke-Logik.</td>
              <td class="p-4 text-[#64748B]">Komplexe Plugins mit ständigen Update-Problemen und DSGVO-Risiken.</td>
              <td class="p-4 font-bold text-emerald-700 bg-blue-50/30">Geführter 3-Stufen-Vorabfilter mit mobilem Foto-Upload für Baustellen.</td>
            </tr>
            <tr>
              <td class="p-4 font-bold text-[#0F172A]">Ladezeit &amp; Sicherheit</td>
              <td class="p-4 text-[#64748B]">Oft überladene Baukastensysteme mit langen Ladezeiten (&gt; 3 Sekunden).</td>
              <td class="p-4 text-[#64748B]">Häufige Hacker-Angriffe über veraltete WordPress-Plugins.</td>
              <td class="p-4 font-bold text-emerald-700 bg-blue-50/30">Ultraschneller HTML5/Tailwind-Stack (unter 0,8s), extrem sicher und wartungsarm.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- SEKTION 4: FAQ (13 KERNFRAGEN)                                 -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <section id="faq" class="space-y-8 scroll-mt-28">
    <div class="text-center max-w-2xl mx-auto space-y-2">
      <h2 data-aos="fade-up" class="text-2xl sm:text-4xl font-extrabold text-[#0F172A]">
        Häufige Fragen &amp; verbindliche Fakten
      </h2>
      <p class="text-xs sm:text-sm text-[#475569]">
        Klarheit zu Eigentum, Fristen und Kosten vor Beginn der Zusammenarbeit.
      </p>
    </div>

    <div class="space-y-3">
      <!-- FAQ Accordion items (matching Chapter 5.J) -->
      <div class="bg-white rounded-2xl overflow-hidden border border-slate-200">
        <button type="button" onclick="toggleAblaufFAQ(this)" class="w-full flex items-center justify-between p-5 text-left hover:bg-slate-50 transition-colors">
          <span class="text-sm font-bold text-[#0F172A] pr-4">1. Gehört die Website nach Fertigstellung wirklich zu 100 % meinem Betrieb?</span>
          <i data-lucide="chevron-down" class="w-4 h-4 text-[#2563EB] shrink-0 transition-transform"></i>
        </button>
        <div class="px-5 pb-5 hidden text-xs text-[#475569] leading-relaxed">
          <strong>Ja, uneingeschränkt.</strong> Nach vollständiger Begleichung der Rechnung gehören der gesamte Quellcode, alle erstellten Fachtexte, Grafiken und Domain-Rechte zu 100 % Ihrem Handwerksbetrieb. Es gibt keine versteckte Website-Miete, keine Mindestvertragslaufzeit von 24 Monaten und keine Abhängigkeit von SparrenWeb.
        </div>
      </div>

      <div class="bg-white rounded-2xl overflow-hidden border border-slate-200">
        <button type="button" onclick="toggleAblaufFAQ(this)" class="w-full flex items-center justify-between p-5 text-left hover:bg-slate-50 transition-colors">
          <span class="text-sm font-bold text-[#0F172A] pr-4">2. Was genau ist im Pilot-Angebot für 1.500 € netto enthalten und welche Bedingungen gelten?</span>
          <i data-lucide="chevron-down" class="w-4 h-4 text-[#2563EB] shrink-0 transition-transform"></i>
        </button>
        <div class="px-5 pb-5 hidden text-xs text-[#475569] leading-relaxed">
          Das Pilot-Angebot ist auf genau 3 Meisterbetriebe in Bielefeld &amp; OWL limitiert. Sie erhalten das vollständige schlüsselfertige System (bis zu 5 Inhaltsseiten, Fachtexte, Kunden-Vorabfilter mit Foto-Upload) zum vergünstigten Festpreis von 1.500 € netto (50 % bei Start, 50 % bei Fertigstellung) gegen die Zusage einer gemeinsamen regionalen Fallstudie.
        </div>
      </div>

      <div class="bg-white rounded-2xl overflow-hidden border border-slate-200">
        <button type="button" onclick="toggleAblaufFAQ(this)" class="w-full flex items-center justify-between p-5 text-left hover:bg-slate-50 transition-colors">
          <span class="text-sm font-bold text-[#0F172A] pr-4">3. Was unterscheidet das reguläre Meister-Auftrags-System (2.800 € netto) vom Pilot-Angebot?</span>
          <i data-lucide="chevron-down" class="w-4 h-4 text-[#2563EB] shrink-0 transition-transform"></i>
        </button>
        <div class="px-5 pb-5 hidden text-xs text-[#475569] leading-relaxed">
          Das Meister-Auftrags-System für 2.800 € netto ist unser Standard-Paket ohne Fallstudien-Verpflichtung mit bis zu 6 Inhaltsseiten, vollständiger Google Unternehmensprofil Optimierung und detaillierten Fachtexten für mehrere Angebotsschwerpunkte.
        </div>
      </div>

      <div class="bg-white rounded-2xl overflow-hidden border border-slate-200">
        <button type="button" onclick="toggleAblaufFAQ(this)" class="w-full flex items-center justify-between p-5 text-left hover:bg-slate-50 transition-colors">
          <span class="text-sm font-bold text-[#0F172A] pr-4">4. Was passiert, wenn ich den monatlichen Systembetrieb für 250 € nicht buche oder kündige?</span>
          <i data-lucide="chevron-down" class="w-4 h-4 text-[#2563EB] shrink-0 transition-transform"></i>
        </button>
        <div class="px-5 pb-5 hidden text-xs text-[#475569] leading-relaxed">
          Der monatliche Systembetrieb ist vollkommen optional und monatlich kündbar. Wenn Sie ihn kündigen, bleibt Ihre Website online; Sie betreiben sie dann einfach auf einem eigenen Server (z. B. Strato, All-Inkl oder Hetzner für ca. 8–15 € monatlich).
        </div>
      </div>

      <div class="bg-white rounded-2xl overflow-hidden border border-slate-200">
        <button type="button" onclick="toggleAblaufFAQ(this)" class="w-full flex items-center justify-between p-5 text-left hover:bg-slate-50 transition-colors">
          <span class="text-sm font-bold text-[#0F172A] pr-4">5. Gibt es eine Ratenzahlungsmöglichkeit?</span>
          <i data-lucide="chevron-down" class="w-4 h-4 text-[#2563EB] shrink-0 transition-transform"></i>
        </button>
        <div class="px-5 pb-5 hidden text-xs text-[#475569] leading-relaxed">
          Für das Meister-System (2.800 €) bieten wir auf Anfrage eine Dreiteilung an: 1.400 € Anzahlung bei Start, 700 € bei Zwischenabnahme und 700 € 30 Tage nach Go-Live. Es erfolgt keine Bonitätsprüfung über Drittanbieter.
        </div>
      </div>
    </div>
  </section>

</main>
"""

    script_content = """
<script>
  function calculateROI() {
    const setupPrice = parseFloat(document.getElementById('roiSetupPackage')?.value || 2800);
    const careActive = document.getElementById('roiCare250')?.checked;
    const adCareActive = document.getElementById('roiAdCare240')?.checked;
    const adBudget = parseFloat(document.getElementById('roiAdBudget')?.value || 0);
    const months = parseInt(document.getElementById('roiMonths')?.value || 12);
    const marginPerDeal = parseFloat(document.getElementById('sliderMargin')?.value || 3500);
    const dealsPerMonth = parseFloat(document.getElementById('sliderDeals')?.value || 1);

    // Update Slider Labels
    const lblMargin = document.getElementById('labelMargin');
    if (lblMargin) lblMargin.textContent = marginPerDeal.toLocaleString('de-DE') + ' €';
    const lblDeals = document.getElementById('labelDeals');
    if (lblDeals) lblDeals.textContent = dealsPerMonth === 1 ? '1 Auftrag' : dealsPerMonth.toLocaleString('de-DE') + ' Aufträge';

    // Period badge
    const badge = document.getElementById('resPeriodBadge');
    if (badge) badge.textContent = months + ' Monate';

    // Monthly ongoing costs
    let monthlyOngoing = 0;
    if (careActive) monthlyOngoing += 250;
    if (adCareActive) monthlyOngoing += 240;
    monthlyOngoing += adBudget;

    // Total costs over period
    const totalCosts = setupPrice + (monthlyOngoing * months);

    // Total additional contribution margin
    const totalMargin = dealsPerMonth * marginPerDeal * months;

    // Net profit
    const netProfit = totalMargin - totalCosts;

    // ROI
    const roiPct = totalCosts > 0 ? (netProfit / totalCosts) * 100 : 0;

    // Monthly margin vs monthly ongoing costs
    const monthlyMargin = dealsPerMonth * marginPerDeal;
    const monthlyNetGain = monthlyMargin - monthlyOngoing;

    let amortText = '';
    if (monthlyNetGain > 0) {
      const amortMonths = setupPrice / monthlyNetGain;
      amortText = 'ca. ' + amortMonths.toFixed(1).replace('.', ',') + ' Monate';
    } else {
      amortText = 'Keine Amortisation unter diesen Annahmen';
    }

    // Update Output Elements
    const elNet = document.getElementById('resNetProfit');
    const elTotCost = document.getElementById('resTotalCost');
    const elTotMargin = document.getElementById('resTotalMargin');
    const elMonCost = document.getElementById('resMonthlyCost');
    const elRoi = document.getElementById('resRoiPct');
    const elAmort = document.getElementById('resAmort');

    if (elNet) {
      elNet.textContent = (netProfit >= 0 ? '+' : '') + Math.round(netProfit).toLocaleString('de-DE') + ' €';
      if (netProfit >= 0) {
        elNet.className = 'text-3xl sm:text-4xl font-extrabold font-mono text-emerald-400';
      } else {
        elNet.className = 'text-3xl sm:text-4xl font-extrabold font-mono text-rose-400';
      }
    }

    if (elTotCost) elTotCost.textContent = Math.round(totalCosts).toLocaleString('de-DE') + ' €';
    if (elTotMargin) elTotMargin.textContent = Math.round(totalMargin).toLocaleString('de-DE') + ' €';
    if (elMonCost) elMonCost.textContent = Math.round(monthlyOngoing).toLocaleString('de-DE') + ' € / Mo';
    if (elRoi) {
      elRoi.textContent = (roiPct >= 0 ? '+' : '') + Math.round(roiPct) + ' %';
      elRoi.className = roiPct >= 0 ? 'font-mono text-blue-400 font-bold text-sm' : 'font-mono text-rose-400 font-bold text-sm';
    }
    if (elAmort) elAmort.textContent = amortText;
  }

  function toggleAblaufFAQ(btn) {
    const content = btn.nextElementSibling;
    const icon = btn.querySelector('i');
    if (!content) return;
    const isHidden = content.classList.contains('hidden');
    if (isHidden) {
      content.classList.remove('hidden');
      if (icon) icon.style.transform = 'rotate(180deg)';
    } else {
      content.classList.add('hidden');
      if (icon) icon.style.transform = 'rotate(0deg)';
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    calculateROI();
  });
</script>
"""

    return head + navbar + main_html + script_content + footer

if __name__ == "__main__":
    html = build_ablauf()
    with open("ablauf.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("ablauf.html erfolgreich generiert.")
