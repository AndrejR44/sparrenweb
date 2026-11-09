#!/usr/bin/env python3
"""
generate_legal.py
Generiert die rechtlichen Pflichtseiten impressum.html und datenschutz.html
unter Verwendung des gemeinsamen Layouts aus builder_helper.py.
Fehlende Betreiberdaten werden transparent als Launch-Blocker ausgewiesen.
"""

import os
from builder_helper import get_head, get_navbar, get_footer

def generate_impressum():
    head = get_head(
        title="Impressum · SparrenWeb Bielefeld",
        description="Impressum und Anbieterkennzeichnung nach § 5 DDG von SparrenWeb Bielefeld.",
        canonical_page="impressum.html"
    )
    navbar = get_navbar(active_page="impressum.html")
    footer = get_footer()
    
    content = f"""{head}
{navbar}
  <main class="min-h-screen pt-28 pb-20 px-6">
    <div class="max-w-4xl mx-auto">
      
      <!-- Launch Blocker Hinweisbox -->
      <div class="mb-10 p-5 rounded-2xl bg-amber-50 border border-amber-200 text-amber-900 text-sm">
        <div class="flex items-start gap-3">
          <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-600 shrink-0 mt-0.5"></i>
          <div>
            <h2 class="font-bold text-amber-950 text-base mb-1">Hinweis zur Test- und Bereitstellungsphase (Launch-Blocker)</h2>
            <p class="leading-relaxed text-amber-900/90 text-xs sm:text-sm">
              Diese Website befindet sich vor dem offiziellen Livegang. Die nachfolgende Anbieterkennzeichnung enthält Platzhalter für noch zu finalisierende Betreiberdaten (Gewerbeanmeldung, Steuernummer/USt-ID). Vor der Aufschaltung auf die öffentliche Live-Domain werden diese Daten verbindlich ergänzt (siehe <code class="bg-amber-100 px-1 py-0.5 rounded text-xs font-mono">docs/intern/09_launch_blocker_und_offene_freigaben.md</code>).
            </p>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-3xl border border-slate-200 shadow-sm p-8 sm:p-12 space-y-8">
        <div>
          <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-blue-50 text-blue-700 border border-blue-200/60 mb-4">
            Rechtliche Angaben
          </span>
          <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
            Impressum
          </h1>
          <p class="text-slate-600 text-sm mt-2">
            Angaben gemäß § 5 Digitale-Dienste-Gesetz (DDG)
          </p>
        </div>

        <section class="space-y-3 pt-6 border-t border-slate-100">
          <h2 class="text-lg font-bold text-slate-900">Anbieter</h2>
          <p class="text-slate-700 leading-relaxed text-sm">
            <strong>SparrenWeb</strong><br>
            Inhaber: [Vorname Nachname – Betreiberfreigabe ausstehend]<br>
            [Straße und Hausnummer – Betreiberfreigabe ausstehend]<br>
            33602 Bielefeld<br>
            Deutschland
          </p>
        </section>

        <section class="space-y-3 pt-6 border-t border-slate-100">
          <h2 class="text-lg font-bold text-slate-900">Kontakt</h2>
          <p class="text-slate-700 leading-relaxed text-sm">
            E-Mail: <a href="mailto:kontakt@sparrenweb.de" class="text-blue-600 hover:underline">kontakt@sparrenweb.de</a><br>
            Web: <a href="https://sparrenweb.de" class="text-blue-600 hover:underline">https://sparrenweb.de</a><br>
            Telefon: [Telefonnummer – Aktivierung bei Livegang]
          </p>
        </section>

        <section class="space-y-3 pt-6 border-t border-slate-100">
          <h2 class="text-lg font-bold text-slate-900">Umsatzsteuer-Identifikationsnummer</h2>
          <p class="text-slate-700 leading-relaxed text-sm">
            Umsatzsteuer-Identifikationsnummer gemäß § 27a Umsatzsteuergesetz:<br>
            <span class="text-slate-500 italic">[USt-ID beantragt / Erteilung durch Bundeszentralamt für Steuern ausstehend]</span>
          </p>
        </section>

        <section class="space-y-3 pt-6 border-t border-slate-100">
          <h2 class="text-lg font-bold text-slate-900">Angaben zur gewerblichen Tätigkeit</h2>
          <p class="text-slate-700 leading-relaxed text-sm">
            Gewerbeanmeldung nach § 14 GewO bei der Stadt Bielefeld (in Durchführung).<br>
            Zuständige Kammer: Industrie- und Handelskammer Ostwestfalen zu Bielefeld, Elsa-Brändström-Str. 1–3, 33602 Bielefeld.
          </p>
        </section>

        <section class="space-y-3 pt-6 border-t border-slate-100">
          <h2 class="text-lg font-bold text-slate-900">EU-Streitschlichtung &amp; Verbraucherstreitbeilegung</h2>
          <p class="text-slate-700 leading-relaxed text-sm">
            Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: <a href="https://ec.europa.eu/consumers/odr" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:underline">https://ec.europa.eu/consumers/odr</a>.<br>
            Unsere E-Mail-Adresse finden Sie oben im Impressum.<br>
            Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen, da sich unser Angebot ausschließlich an gewerbliche Kunden (B2B – Handwerks- und Meisterbetriebe) richtet.
          </p>
        </section>

        <section class="space-y-3 pt-6 border-t border-slate-100">
          <h2 class="text-lg font-bold text-slate-900">Haftung für Inhalte und Links</h2>
          <p class="text-slate-600 leading-relaxed text-xs">
            Als Diensteanbieter sind wir gemäß § 7 Abs. 1 DDG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 DDG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.
          </p>
          <p class="text-slate-600 leading-relaxed text-xs mt-2">
            Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich.
          </p>
        </section>
      </div>
    </div>
  </main>
{footer}"""
    return content

def generate_datenschutz():
    head = get_head(
        title="Datenschutzerklärung · SparrenWeb Bielefeld",
        description="Datenschutzerklärung nach der DSGVO für die Nutzung der Website von SparrenWeb Bielefeld.",
        canonical_page="datenschutz.html"
    )
    navbar = get_navbar(active_page="datenschutz.html")
    footer = get_footer()
    
    content = f"""{head}
{navbar}
  <main class="min-h-screen pt-28 pb-20 px-6">
    <div class="max-w-4xl mx-auto">
      
      <div class="bg-white rounded-3xl border border-slate-200 shadow-sm p-8 sm:p-12 space-y-8">
        <div>
          <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-blue-50 text-blue-700 border border-blue-200/60 mb-4">
            Datenschutz nach DSGVO
          </span>
          <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
            Datenschutzerklärung
          </h1>
          <p class="text-slate-600 text-sm mt-2">
            Information über die Verarbeitung Ihrer personenbezogenen Daten gemäß Art. 13 und 14 DSGVO
          </p>
        </div>

        <section class="space-y-3 pt-6 border-t border-slate-100">
          <h2 class="text-lg font-bold text-slate-900">1. Verantwortliche Stelle</h2>
          <p class="text-slate-700 leading-relaxed text-sm">
            Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) und anderer nationaler Datenschutzgesetze ist:<br><br>
            <strong>SparrenWeb</strong><br>
            [Vorname Nachname – Betreiberfreigabe ausstehend]<br>
            [Straße und Hausnummer – Betreiberfreigabe ausstehend]<br>
            33602 Bielefeld<br>
            Deutschland<br>
            E-Mail: <a href="mailto:kontakt@sparrenweb.de" class="text-blue-600 hover:underline">kontakt@sparrenweb.de</a>
          </p>
        </section>

        <section class="space-y-3 pt-6 border-t border-slate-100">
          <h2 class="text-lg font-bold text-slate-900">2. Datenschutzfreundliches Grundprinzip (Privacy by Design)</h2>
          <p class="text-slate-700 leading-relaxed text-sm">
            Wir legen größten Wert auf sparsame Datenverarbeitung:
          </p>
          <ul class="list-disc list-inside space-y-1.5 text-sm text-slate-700">
            <li><strong>Keine Tracking-Cookies:</strong> Wir setzen keine zustimmungspflichtigen Tracking-, Analyse- oder Marketing-Cookies (wie Google Analytics oder Meta-Pixel) auf dieser Website ein.</li>
            <li><strong>Lokale Einbindung:</strong> Schriften und Icons werden lokal ausgeliefert oder DSGVO-konform ohne Profilbildung geladen.</li>
            <li><strong>Keine Weitergabe an Dritte:</strong> Ihre Daten werden vertraulich behandelt und keinesfalls zu Werbezwecken an Dritte verkauft oder weitergegeben.</li>
          </ul>
        </section>

        <section class="space-y-3 pt-6 border-t border-slate-100">
          <h2 class="text-lg font-bold text-slate-900">3. Bereitstellung der Website und Logfiles</h2>
          <p class="text-slate-700 leading-relaxed text-sm">
            Bei jedem Aufruf unserer Website erfasst unser Webserver automatisch technische Daten, die Ihr Browser an unseren Server übermittelt:
          </p>
          <ul class="list-disc list-inside space-y-1 text-sm text-slate-700">
            <li>IP-Adresse des anfragenden Geräts (anonymisiert)</li>
            <li>Datum und Uhrzeit des Zugriffs</li>
            <li>Name und URL der abgerufenen Datei</li>
            <li>Übertragene Datenmenge und Zugriffsstatus (HTTP-Statuscode)</li>
            <li>Verwendeter Browser und Betriebssystem (User-Agent)</li>
          </ul>
          <p class="text-slate-700 leading-relaxed text-sm">
            <strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an der technischen Stabilität, Sicherheit und Fehleranalyse des Webservers). Die Server-Logfiles werden nach maximal 14 Tagen gelöscht.
          </p>
        </section>

        <section class="space-y-3 pt-6 border-t border-slate-100">
          <h2 class="text-lg font-bold text-slate-900">4. Kontaktaufnahme und Projektanfragen (Vorab-Entwurf)</h2>
          <p class="text-slate-700 leading-relaxed text-sm">
            Wenn Sie über unser Anfrageformular (<a href="anfrage.html" class="text-blue-600 hover:underline">anfrage.html</a>) oder per E-Mail Kontakt mit uns aufnehmen, verarbeiten wir die von Ihnen eingegebenen Daten (z. B. Betrieb/Firmenname, Name, Gewerk, E-Mail-Adresse, Telefonnummer, Angaben zum Vorhaben):
          </p>
          <p class="text-slate-700 leading-relaxed text-sm">
            <strong>Zweck:</strong> Bearbeitung Ihrer Anfrage, Erstellung des angeforderten individuellen System-Entwurfs und telefonische Rücksprache zur Projektbesprechung.<br>
            <strong>Rechtsgrundlage:</strong> Art. 6 Abs. 1 lit. b DSGVO (Durchführung vorvertraglicher Maßnahmen auf Anfrage der betroffenen Person).<br>
            <strong>Speicherdauer:</strong> Die Daten werden gelöscht, sobald sie für die Erreichung des Zweckes ihrer Erhebung nicht mehr erforderlich sind und keine gesetzlichen Aufbewahrungsfristen (z. B. nach HGB/AO bei Auftragserteilung) entgegenstehen.
          </p>
        </section>

        <section class="space-y-3 pt-6 border-t border-slate-100">
          <h2 class="text-lg font-bold text-slate-900">5. Ihre Rechte als betroffene Person</h2>
          <p class="text-slate-700 leading-relaxed text-sm">
            Sie haben nach der DSGVO jederzeit folgende Rechte gegenüber der verantwortlichen Stelle:
          </p>
          <ul class="list-disc list-inside space-y-1.5 text-sm text-slate-700">
            <li><strong>Recht auf Auskunft (Art. 15 DSGVO):</strong> Sie können Auskunft über Ihre von uns verarbeiteten personenbezogenen Daten verlangen.</li>
            <li><strong>Recht auf Berichtigung (Art. 16 DSGVO):</strong> Sie können unverzüglich die Berichtigung unrichtiger Daten verlangen.</li>
            <li><strong>Recht auf Löschung (Art. 17 DSGVO):</strong> Sie können die Löschung Ihrer bei uns gespeicherten Daten verlangen, sofern keine gesetzlichen Pflichten entgegenstehen.</li>
            <li><strong>Recht auf Einschränkung der Verarbeitung (Art. 18 DSGVO):</strong> Sie haben das Recht, eine Einschränkung der Verarbeitung zu verlangen.</li>
            <li><strong>Recht auf Datenübertragbarkeit (Art. 20 DSGVO):</strong> Sie können Ihre Daten in einem strukturierten, gängigen und maschinenlesbaren Format erhalten.</li>
            <li><strong>Widerspruchsrecht (Art. 21 DSGVO):</strong> Sie können der Verarbeitung widersprechen, wenn diese auf Art. 6 Abs. 1 lit. f DSGVO beruht.</li>
          </ul>
          <p class="text-slate-700 leading-relaxed text-sm">
            Zur Ausübung Ihrer Rechte genügt eine formlose E-Mail an <a href="mailto:kontakt@sparrenweb.de" class="text-blue-600 hover:underline">kontakt@sparrenweb.de</a>. Zudem haben Sie das Recht auf Beschwerde bei einer Datenschutz-Aufsichtsbehörde (z. B. der Landesbeauftragten für Datenschutz und Informationsfreiheit Nordrhein-Westfalen, LDI NRW in Düsseldorf).
          </p>
        </section>
      </div>
    </div>
  </main>
{footer}"""
    return content

if __name__ == "__main__":
    impressum_html = generate_impressum()
    datenschutz_html = generate_datenschutz()
    
    with open("impressum.html", "w", encoding="utf-8") as f:
        f.write(impressum_html)
    print("impressum.html erfolgreich generiert.")
    
    with open("datenschutz.html", "w", encoding="utf-8") as f:
        f.write(datenschutz_html)
    print("datenschutz.html erfolgreich generiert.")
