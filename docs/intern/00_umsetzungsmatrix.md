# SparrenWeb – Vollständige Umsetzungsmatrix
**Stand:** 06. November 2026  
**Dokumenttyp:** Internes Steuerungsdokument (Nicht für die öffentliche Veröffentlichung)

---

## 1. Übersicht & Status-Legende
Die folgende Matrix erfasst alle strategischen, technischen, gestalterischen, preislichen und rechtlichen Anforderungen aus dem Briefing und der Analyse (`paste.txt`). Keine Anforderung wird stillschweigend weggelassen.

### Zulässige Statuswerte:
- `[IMPLEMENTIERT]` Implementiert und getestet
- `[KONFIG_FEHLT]` Implementiert, externe Konfiguration fehlt
- `[BETREIBER_FEHLT]` Betreiberinhalt fehlt (z. B. Name, Porträt, Registerdaten)
- `[EXTERN_OFFEN]` Externe Tätigkeit erforderlich (z. B. Gewerbeanmeldung, Konto, Kundenkontakt)
- `[PRUEFUNG_OFFEN]` Fachliche/rechtliche Prüfung erforderlich (z. B. USt-Status, AGB/Verträge)
- `[INTERN_GESCHUTZT]` Bewusst nicht öffentlich (in `docs/intern/` abgelegt)
- `[KORRIGIERT]` Widerspruch korrigiert
- `[NICHT_ZUTREFFEND]` Nicht zutreffend (mit Begründung)

---

## 2. Detaillierte Umsetzungsmatrix

| ID | Anforderung | Ursprung | Zielseite / Datei | Umsetzung | Test / Nachweis | Status | Offene Voraussetzung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **REQ-01** | Bestandsaufnahme Stack & keine unnötigen Frameworkwechsel | Kap. 1 | Projekt-Root | Bestehender Stack (HTML5, Tailwind, Vanilla JS, Python-Generatoren) beibehalten | `test_all_pages.py` | `[IMPLEMENTIERT]` | Keine |
| **REQ-02** | Positionierung für etablierte Meisterbetriebe (4–20 MA) in Bielefeld & OWL | Kap. 2 | Alle Seiten | Seröse Sie-Ansprache, Fokus auf Entlastung & qualifizierte Anfragen | Manuelle Prüfung, Content-Audit | `[IMPLEMENTIERT]` | Keine |
| **REQ-03** | Keine erfundenen Erfolgsnachweise, Garantien oder Fake-Rankings | Kap. 2, 4, 7 | `index.html`, `referenzen.html`, etc. | Entfernung aller erfundenen Kunden, Zitate, 4,9★-Ratings, AggregateRating-Schema | Scan auf Fake-Daten | `[IMPLEMENTIERT]` | Echte Referenzen nach Pilotphase |
| **REQ-04** | Primäre Gewerke (Dach, SHK, Elektro), sekundär (Tischler, GaLaBau, Metall), Maler ergänzend | Kap. 2, 8 | `gewerke.html`, `index.html` | Strukturierung & Priorisierung exakt nach Vorgabe | Gewerke-Tabs & Filtertests | `[IMPLEMENTIERT]` | Keine |
| **REQ-05** | Öffentliche Kernbotschaft & Nutzenhierarchie | Kap. 2, 5 | `index.html` (Hero & Value Props) | Exakte Kernbotschaft implementiert, Nutzen 1–6 strukturiert | Screenshot & Copy-Check | `[IMPLEMENTIERT]` | Keine |
| **REQ-06** | Zentrale Angebotsdaten definieren | Kap. 3 | `pricing_data.py`, `pricing-data.js` | Single Source of Truth für Python-Generatoren & Client-JS | Import & Konsistenztest | `[IMPLEMENTIERT]` | Keine |
| **REQ-07** | Alle Preise als B2B-Nettopreise mit „zzgl. gesetzl. MwSt.“ | Kap. 3 | Alle Seiten & Footer | Globaler Zusatz „zzgl. gesetzl. MwSt.“ in allen Preiskarten und Fußzeilen | Grep-Prüfung | `[IMPLEMENTIERT]` | Betreiber-USt-Status |
| **REQ-08** | Angebot A: „OWL-Referenz-Pilot“ (1.500 € netto, max. 3 Betriebe, 50/50 Split) | Kap. 3 | `index.html`, `leistungen.html`, `anfrage.html` | Pilot-Angebot mit ehrlichen Bedingungen, kein Fake-Countdown | Preis- und Buchungstests | `[IMPLEMENTIERT]` | Akquise der 3 Betriebe |
| **REQ-09** | Angebot B: „SparrenWeb Meister-Auftrags-System“ (2.800 € netto, bis zu 6 Inhaltsseiten, 50/50 Split) | Kap. 3 | Alle Seiten | Standard-Paket mit Fachtexten, Vorabfilter, SEO, Google Profil | Preiskarten- & Leistungstests | `[IMPLEMENTIERT]` | Keine |
| **REQ-10** | Ratenzahlungs-Option im FAQ (1.400 € / 700 € / 700 €) ohne automatischen Kredit | Kap. 3, 5 | `index.html`, `leistungen.html`, `ablauf.html` | Im FAQ als individuelle Vereinbarungsmöglichkeit aufgeführt | FAQ-Test | `[IMPLEMENTIERT]` | Keine |
| **REQ-11** | Angebot C: „Regionaler Sichtbarkeits- & Systembetrieb“ (250 €/Mo netto, optional, 60 Min. Kontingent) | Kap. 3, 6 | `leistungen.html`, `index.html` | Kein Zwang, monatlich kündbar, 60 Min. Inhaltsänderung, Jahrespreis 2.700 € (10 % Rabatt) | Paket-Audit | `[IMPLEMENTIERT]` | Technische Infrastruktur |
| **REQ-12** | Angebot D: „60-Sekunden-Recruiting-Modul“ (1.200 € netto einmalig) | Kap. 3, 6 | `leistungen.html`, `index.html` | Als vereinfachtes Bewerbungskonzept (kein Versprechen exakter 60 Sek.), Social-Media-Vorlagen | Modul-Darstellung & Formular | `[IMPLEMENTIERT]` | Werbebudget durch Kunden |
| **REQ-13** | Angebot E: „Meister-System + Recruiting-Kombi“ (3.500 € netto, 500 € Vorteil) | Kap. 3, 5, 6 | `index.html`, `leistungen.html` | Paket 2.800 € + 1.200 € = 4.000 € $\rightarrow$ 3.500 € netto; Betreuung 250 € + 240 € Ads = 490 €/Mo | Rechen- und Textprüfung | `[IMPLEMENTIERT]` | Keine |
| **REQ-14** | Entfernung aller alten Preise (1.490 €, altes 490 € Einzelmodul, 1.990 €, pauschales 0 € Monatsabo) | Kap. 4 | Alle Dateien | Globaler Scan & Ersetzung alter Beträge und pauschaler Abo-Freiheits-Versprechen | Python-Grep-Validierung | `[IMPLEMENTIERT]` | Keine |
| **REQ-15** | Startseite: Neuer Hero, 14-Tage-Ziel mit Voraussetzungen, 90-Min.-Ziel, CTAs | Kap. 5 | `index.html` | Hero-Überarbeitung gemäß Vorgabe, keine Garantie ohne Mitwirkung | Playwright-Test | `[IMPLEMENTIERT]` | Keine |
| **REQ-16** | Startseite: Interaktive Vorabfilter-Demo als klare Demonstration | Kap. 5, 12 | `index.html#demo` | Echte bedienbare Demo mit klarem Hinweis „Demo – keine Anfrage wird versendet“ | Interaktiver Klicktest | `[IMPLEMENTIERT]` | Keine |
| **REQ-17** | Startseite: Ansprechpartner nur verifiziert (keine erfundenen Namen, Nummern, KI-Fotos) | Kap. 5.I | `index.html` | Saubere Vorbereitung der Kontaktkomponente, keine Fake-Nummer `0521 2580910`, Platzhalter gesperrt | Blockertabelle | `[BETREIBER_FEHLT]` | Echter Name, Foto, Telefon |
| **REQ-18** | Startseite: Vollständiges FAQ (13 Kernfragen zu Eigentum, Hosting, Pilot etc.) | Kap. 5.J | `index.html` | Alle 13 Fragen sachlich und transparent beantwortet | Accordion-Test | `[IMPLEMENTIERT]` | Keine |
| **REQ-19** | Leistungen-Seite: 12 Abschnitte inkl. Eigentum, Nutzungsrechte, Leistungsgrenzen | Kap. 6 | `generate_leistungen.py` $\rightarrow$ `leistungen.html` | Vollständige Darstellung, klare Abgrenzung (keine unbegrenzte Flatrate, keine Rechtsillusion) | Playwright-Test | `[IMPLEMENTIERT]` | Keine |
| **REQ-20** | Referenzen-Seite umwandeln in „System-Demos“ mit fiktiver Kennzeichnung | Kap. 7 | `generate_referenzen.py` $\rightarrow$ `referenzen.html` | Titel „Interaktive System-Demonstratoren“, Kennzeichnung „Fiktives Konzeptprojekt – keine Kundenreferenz“ | Vorher/Nachher- & Demo-Test | `[IMPLEMENTIERT]` | Echte Referenzen |
| **REQ-21** | Gewerke-Seite: Priorisierung 1–7, reparaturfreundlich, keine abwertenden Texte | Kap. 8 | `generate_gewerke.py` $\rightarrow$ `gewerke.html` | Gewerke-Tabs Dach, SHK, Elektro, Tischler, GaLaBau, Metall, Maler; Reparaturen wählbar | Gewerke-Tab-Tests | `[IMPLEMENTIERT]` | Keine |
| **REQ-22** | Ablauf-Seite: 12 Schritte detailliert (14 Tage Ziel, 90 Min Abstimmung) | Kap. 9 | `generate_ablauf.py` $\rightarrow$ `ablauf.html` | Realistischer 12-Stufen-Prozess von Anfrage bis Übergabe & Betreuung | Ablauf-Test | `[IMPLEMENTIERT]` | Keine |
| **REQ-23** | ROI- & Amortisationsrechner komplett nach Formel aus Kap. 10 | Kap. 10 | `generate_ablauf.py` $\rightarrow$ `ablauf.html` | Trennung von Umsatz & Deckungsbeitrag, Amortisation nur bei Überschuss, Disclaimer | Berechnungs-Unit-Tests | `[IMPLEMENTIERT]` | Keine |
| **REQ-24** | Anfrageformular für Vorab-Entwurf (neue Felder: MA-Zahl, Website/noch keine, Anliegen) | Kap. 11 | `generate_anfrage.py` $\rightarrow$ `anfrage.html` | 4-Stufen-Funnel mit allen Pflichtfeldern, keine vorausgewählte Betreuung, Demo-Schutz | Formularvalidierung | `[IMPLEMENTIERT]` | SMTP/Mail-Backend |
| **REQ-25** | Recruiting-Demo: Smartphone-orientiert, ohne Lebenslauf-Zwang | Kap. 12 | `leistungen.html`, `index.html` | Mobile Schnellbewerbungs-Demo mit Qualifikation & Kontaktweg | Interaktionsprüfung | `[IMPLEMENTIERT]` | Keine |
| **REQ-26** | Eigentum & Betreuung: „Einmal kaufen. Betreuung auf Wunsch.“ | Kap. 13 | Alle Seiten, `site-common.css` | Differenzierte Eigentums- und Kündigungsregelung ohne falsche „Alles kostenlos weiter“-Garantie | Text-Audit | `[IMPLEMENTIERT]` | AGB-Vertragsprüfung |
| **REQ-27** | Barrierefreiheit & Design: Tastaturbedienung, Kontraste, keine Slop-Animationen | Kap. 14 | `site-common.css`, HTML | Semantisches HTML, sichtbare Fokuszustände, reduced-motion Support | Barrierefreiheits-Check | `[IMPLEMENTIERT]` | Keine |
| **REQ-28** | SEO: Regionale Metadaten OWL/Bielefeld, Schema.org nur für echte Daten | Kap. 15 | Alle HTML-Dateien | Saubere Canonical, Title, Description, Alt-Texte, keine Fake-Reviews im JSON-LD | SEO-Validierung | `[IMPLEMENTIERT]` | Live-Domain-Bestätigung |
| **REQ-29** | Rechtliche Seiten: `impressum.html` und `datenschutz.html` ohne Fakedaten | Kap. 16 | `impressum.html`, `datenschutz.html` | Ehrlicher Aufbau mit Kennzeichnung fehlender Betreiberdaten als Launch-Blocker | Rechtsseiten-Test | `[BETREIBER_FEHLT]` | Name, Anschrift, USt-ID |
| **REQ-30** | Interne Unterlagen: Strategie & Modellannahmen | Kap. 17.A | `docs/intern/01_strategie_und_modellannahmen.md` | Solo-Start, 25h/Woche, Ziel 15k Überschuss, unvalidierte Annahmen vs. Realität | Datei-Prüfung | `[INTERN_GESCHUTZT]` | Validierung am Markt |
| **REQ-31** | Interne Unterlagen: Editierbares Finanzmodell (Python & CSV, 12/36 Monate) | Kap. 17.B | `docs/intern/02_finanzmodell_und_wirtschaftlichkeit.py` | 3 Szenarien (Vorsichtig, Standard, Kombi), Liquidität, USt getrennt, keine Doppelzählung | Skriptlauf & CSV-Ausgabe | `[INTERN_GESCHUTZT]` | Reale Verkaufszahlen |
| **REQ-32** | Interne Unterlagen: Akquise-Playbook mit 9 Vorlagen & 20-Min.-Leitfaden | Kap. 17.C | `docs/intern/03_akquise_playbook_und_vorlagen.md` | 9 konkrete Vorlagen, UWG-Hinweise, kein illegales Cold-Calling | Dokumenten-Audit | `[INTERN_GESCHUTZT]` | Juristische Freigabe |
| **REQ-33** | Interne Unterlagen: Lead- & KPI-Vorlagen als CSV | Kap. 17.D | `docs/intern/04_lead_und_kpi_vorlagen.csv` | Strukturierte Tabellenvorlagen ohne fingierte Personendaten | CSV-Validierung | `[INTERN_GESCHUTZT]` | Reale Kundendaten |
| **REQ-34** | Interne Unterlagen: 30-/60-/90-Tage-Plan mit Meilensteinen & Reviews | Kap. 17.E | `docs/intern/05_30_60_90_tage_plan.md` | Konkreter operativer Fahrplan inkl. Review-Tage 21, 45, 60, 90 | Datei-Prüfung | `[INTERN_GESCHUTZT]` | Operativer Start |
| **REQ-35** | Interne Unterlagen: Skalierungsregeln & Partnerintegration | Kap. 17.F | `docs/intern/06_skalierungsregeln_und_partnerintegration.md` | Arbeitsteilung, Kapazitätsgrenzen, Rollenverteilung, zukünftige Preisanpassung | Datei-Prüfung | `[INTERN_GESCHUTZT]` | Partnervertrag |
| **REQ-36** | Interne Unterlagen: Gründungs- & Steuercheckliste | Kap. 17.G | `docs/intern/07_gruendungs_und_steuer_checkliste.md` | Checkliste Gewerbeanmeldung, Ist-Versteuerung, Geschäftskonto, keine Steuerberatung | Checklisten-Audit | `[EXTERN_OFFEN]` | Steuerberater-Termin |
| **REQ-37** | Interne Unterlagen: Referenz-Freigabe-Checkliste | Kap. 17.H | `docs/intern/08_referenz_freigabe_checkliste.md` | Formular zur rechtssicheren Freigabe von Bild-, Text- und Kennzahlenmaterial | Checklisten-Audit | `[PRUEFUNG_OFFEN]` | Anwaltliche Prüfung |
| **REQ-38** | Interne Unterlagen: Launch-Blocker & Offene Betreiber-Freigaben | Kap. 16, 21 | `docs/intern/09_launch_blocker_und_offene_freigaben.md` | Vollständige Erfassung aller Punkte, die vor Veröffentlichung zwingend erledigt sein müssen | Dokumenten-Audit | `[BETREIBER_FEHLT]` | Betreiber-Rückmeldung |
| **REQ-39** | Umfassende automatisierte Tests (Desktop, Mobile 360/390/768/1280/1440, Rechner, Formulare) | Kap. 19 | `test_all_pages.py`, `test_extended_strategy.py` | End-to-End Playwright Tests für alle Seiten, Preise, Rechner & Responsive | Vollständiger Testlauf | `[IMPLEMENTIERT]` | Keine |
| **REQ-40** | Abschlussbericht gemäß Kapitel 21 | Kap. 21 | Chat-Antwort | Präzise Dokumentation aller Änderungen, Preise, Dokumente, Tests und Blocker | Abschlussprüfung | `[IMPLEMENTIERT]` | Keine |

---
*Ende der Umsetzungsmatrix.*
