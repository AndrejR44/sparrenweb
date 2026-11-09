# SparrenWeb – Launch-Blocker & Offene Betreiber-Freigaben
**Stand:** 06. November 2026  
**Dokumenttyp:** Internes Freigabedokument vor Livegang (Launch-Gatekeeper)

> [!CAUTION] STRIKTER LAUNCH-STOPP
> Die Website darf **erst dann öffentlich auf einer Live-Domain (z. B. sparrenweb.de) geschaltet werden**, wenn alle 9 nachfolgenden Blocker durch den Betreiber offiziell bestätigt und eingepflegt wurden.  
> Ein vorzeitiger Livegang ohne vollständiges Impressum und Gewerbeanmeldung verstößt gegen § 5 DDG und § 14 GewO und birgt akute Abmahnrisiken.

---

## Übersicht der 9 Launch-Blocker

| Blocker-ID | Gegenstand | Benötigte Betreiber-Eingabe | Risiko bei Nichtbeachtung | Status |
| :--- | :--- | :--- | :--- | :---: |
| **BLK-01** | **Vollständiger Name des Inhabers** | Vorname und Nachname des Betreibers | Impressumspflichtverletzung (§ 5 DDG), Abmahngefahr | `[OFFEN]` |
| **BLK-02** | **Ladefähige Postanschrift** | Echte Straße und Hausnummer in Bielefeld (kein Postfach) | Formeller Verstoß gegen Anbieterkennzeichnung | `[OFFEN]` |
| **BLK-03** | **Reale Telefonnummer** | Gültige Mobil- oder Festnetznummer (Entfernung der alten Fake-Nummer `0521 2580910` bereits erfolgt) | Erreichbarkeitspflicht nach DDG | `[OFFEN]` |
| **BLK-04** | **Reale E-Mail-Adresse** | Verbindliche Kontakt-E-Mail (z. B. `kontakt@sparrenweb.de`) | Schnelle elektronische Kontaktaufnahme | `[OFFEN]` |
| **BLK-05** | **Gewerbeanmeldung** | Durchgeführte Anmeldung beim Gewerbeamt Bielefeld | Ordnungsstrafe nach § 146 GewO | `[OFFEN]` |
| **BLK-06** | **Steuernummer / USt-ID** | Erteilung durch Finanzamt Bielefeld bzw. Bundeszentralamt | Pflichtangabe bei USt-Ausweis auf Rechnungen und Impressum | `[OFFEN]` |
| **BLK-07** | **Echtes Betreiber-Foto** | Professionelles Porträt des Gründers für die Ansprechpartner-Sektion | Irreführungsschutz; Verbot generierter Fake-Personen | `[OFFEN]` |
| **BLK-08** | **Mail-Versand-Backend** | SMTP-Zugangsdaten oder Mail-API (z. B. Resend/Postmark) für `anfrage.html` | Kontaktanfragen kommen nicht im Postfach an | `[OFFEN]` |
| **BLK-09** | **Fachanwaltliche AGB- & Datenschutzfreigabe** | Letztprüfung der Verträge und Datenschutzerklärung | Haftung für Leistungsstörungen und DSGVO-Bußgelder | `[OFFEN]` |

---

## Checkliste zur Entblockierung (Schritt-für-Schritt)

1. **Betreiberdaten eintragen:**
   - In `impressum.html` und `datenschutz.html` die Platzhalter `[VORNAME NACHNAME]`, `[STRASSE HAUSNUMMER]`, `[TELEFON]` und `[UST-ID]` ersetzen.
   - In `builder_helper.py` und `index.html` die Kontaktdaten in Fußzeile und Kontaktkomponente aktivieren.

2. **Formular-Backend aktivieren:**
   - In `anfrage.html` die Formular-Zieladresse (`action` / Serverless Function) einbinden.

3. **DNS & Hosting konfigurieren:**
   - A-Record und CNAME auf Webserver/CDN setzen, Let's Encrypt SSL-Zertifikat aktivieren.
   - Test auf Live-Domain durchführen.
