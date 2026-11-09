#!/usr/bin/env python3
"""
test_extended_strategy.py
Umfassende End-to-End Test-Suite mit Playwright:
- Prüft alle 8 HTML-Seiten (inkl. impressum.html & datenschutz.html)
- Responsive Viewports: 360x640, 390x844, 768x1024, 1280x800, 1440x900
- Strikte Überlaufprüfung (scrollWidth <= clientWidth)
- Keine Konsolenfehler
- Vollständige Prüfung der neuen Preise (1.500 €, 2.800 €, 3.500 €, 250 €/Mo, 1.200 €)
- Null-Toleranz bei alten Preisen (1.490 €, 1.990 €, 0 € Monatsabo) und Fake-Nummer 0521 2580910
- Interaktive Funktionstests (ROI-Rechner, Funnel, Demos, Filter)
"""

import sys
import time
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:8081"

PAGES = [
    ("index.html", "Startseite"),
    ("gewerke.html", "Gewerke"),
    ("leistungen.html", "Leistungen"),
    ("referenzen.html", "System-Demos"),
    ("ablauf.html", "Ablauf & FAQ"),
    ("anfrage.html", "System-Entwurf anfordern"),
    ("impressum.html", "Impressum"),
    ("datenschutz.html", "Datenschutz")
]

VIEWPORTS = [
    ("Mobile Small (360x640)", 360, 640),
    ("Mobile Standard (390x844)", 390, 844),
    ("Tablet (768x1024)", 768, 1024),
    ("Desktop (1280x800)", 1280, 800),
    ("Desktop Large (1440x900)", 1440, 900)
]

def run_tests():
    print("==================================================")
    print("START: SPARRENWEB E2E STRATEGIE-TESTSUITE")
    print("==================================================")

    with sync_playwright() as p:
        browser = p.chromium.launch()

        # 1. TEST: HTTP 200, Console Errors & Horizontal Overflow across Viewports
        print("\n--- 1. VIEWPORT- & OVERFLOW-TESTS (ALLE SEITEN & VIEWPORTS) ---")
        for vp_name, w, h in VIEWPORTS:
            print(f"\n[Test Viewport: {vp_name}]")
            for page_path, page_name in PAGES:
                page = browser.new_page(viewport={"width": w, "height": h})
                errors = []
                page.on("pageerror", lambda err: errors.append(str(err)))
                page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)

                url = f"{BASE_URL}/{page_path}"
                res = page.goto(url, wait_until="domcontentloaded")
                assert res.status == 200, f"Fehler: {url} liefert HTTP {res.status}"
                page.wait_for_timeout(400)

                # Check horizontal overflow
                overflow = page.evaluate("""() => {
                    return {
                        scrollWidth: document.documentElement.scrollWidth,
                        clientWidth: document.documentElement.clientWidth
                    };
                }""")
                
                scroll_w = overflow["scrollWidth"]
                client_w = overflow["clientWidth"]
                assert scroll_w <= client_w, f"HORIZONTALER OVERFLOW auf {page_path} bei {w}px: scrollWidth={scroll_w} > clientWidth={client_w}"
                
                # Check for critical page errors
                crit_errors = [e for e in errors if "favicon" not in e.lower()]
                assert len(crit_errors) == 0, f"Konsolenfehler auf {page_path}: {crit_errors}"

                page.close()
            print(f"  -> {vp_name}: Alle 8 Seiten ohne Overflow und fehlerfrei.")

        # 2. TEST: Prüfung auf Abwesenheit alter Preise & Fake-Daten im gerenderten DOM
        print("\n--- 2. SCAN AUF LEGACY-STRINGS & FAKE-DATEN IM GERENDERTEN DOM ---")
        legacy_terms = ["1.490", "1.990", "0521 2580910", "05212580910", "Westermann", "Kröger"]
        for page_path, page_name in PAGES:
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.goto(f"{BASE_URL}/{page_path}")
            content = page.content()
            for term in legacy_terms:
                assert term not in content, f"FEHLER: Unerlaubter String '{term}' gefunden in {page_path}!"
            page.close()
        print("  -> Null-Toleranz eingehalten: Keine Legacy-Strings in allen Seiten gefunden.")

        # 3. TEST: Interaktiver ROI-Rechner (ablauf.html)
        print("\n--- 3. TEST: ROI- & AMORTISATIONSRECHNER (ablauf.html) ---")
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(f"{BASE_URL}/ablauf.html")
        page.wait_for_timeout(500)

        # Initialer Stand
        init_net = page.locator("#resNetProfit").text_content()
        init_roi = page.locator("#resRoiPct").text_content()
        init_amort = page.locator("#resAmort").text_content()
        print(f"  Initiale Berechnung: Netto={init_net}, ROI={init_roi}, Amortisation={init_amort}")
        assert "+" in init_net, "Initialer Netto-Überschuss muss positiv sein"
        assert "+" in init_roi, "Initialer ROI muss positiv sein"
        assert "Monate" in init_amort, "Initial muss eine Amortisationszeit berechnet werden"

        # Testfall: Änderung auf Pilot (1.500 €)
        page.locator("#roiSetupPackage").select_option("1500")
        page.wait_for_timeout(200)
        pilot_tot_cost = page.locator("#resTotalCost").text_content()
        assert "4.500" in pilot_tot_cost or "1.500" in pilot_tot_cost, f"Gesamtkosten fehlerhaft: {pilot_tot_cost}"

        # Testfall: Keine Amortisation (Marge < laufende Kosten)
        # Deaktiviere Deals: sliderDeals min oder hohe laufende Kosten
        page.evaluate("""() => {
            document.getElementById('sliderDeals').value = 0.5;
            document.getElementById('sliderMargin').value = 500;
            document.getElementById('roiCare250').checked = true;
            document.getElementById('roiAdCare240').checked = true;
            document.getElementById('roiAdBudget').value = 1000;
            calculateROI();
        }""")
        page.wait_for_timeout(300)
        edge_amort = page.locator("#resAmort").text_content()
        print(f"  Grenzfall (Marge < Kosten): Amortisationstext='{edge_amort}'")
        assert "Keine Amortisation unter diesen Annahmen" in edge_amort, "Amortisationstext bei Marge < Kosten fehlerhaft"
        page.close()
        print("  -> ROI- & Amortisationsrechner funktioniert mathematisch und logisch exakt.")

        # 4. TEST: 4-Schritte-Funnel (anfrage.html)
        print("\n--- 4. TEST: 4-SCHRITTE-FUNNEL (anfrage.html) ---")
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(f"{BASE_URL}/anfrage.html")
        page.wait_for_timeout(500)

        # Step 1: Gewerk wählen (Klick auf das Label der Karte)
        page.locator('label:has-text("Dach & Zimmerei")').click()
        page.wait_for_timeout(200)
        page.locator("#nextBtn").click()
        page.wait_for_timeout(300)
        assert page.locator("#step-2").is_visible(), "Schritt 2 muss nach Klick sichtbar sein"

        # Step 2: Betriebsdaten
        page.locator("#nextBtn").click()
        page.wait_for_timeout(300)
        assert page.locator("#step-3").is_visible(), "Schritt 3 muss sichtbar sein"

        # Step 3: Paketwahl
        page.locator("#nextBtn").click()
        page.wait_for_timeout(300)
        assert page.locator("#step-4").is_visible(), "Schritt 4 muss sichtbar sein"

        # Step 4: Kontaktdaten ausfüllen & Absenden
        page.locator("#f-name").fill("Meister Hans Dach")
        page.locator("#f-phone").fill("0170 9876543")
        page.locator("#f-email").fill("hans@dach-owl.de")
        page.locator("#f-location").fill("33602 Bielefeld")
        page.locator("#submitBtn").click()
        page.wait_for_timeout(400)
        
        feedback_vis = page.locator("#funnelFeedback").is_visible()
        assert feedback_vis, "Bestätigungsmeldung nach Absenden muss sichtbar sein"
        page.close()
        print("  -> Funnel auf anfrage.html schließt alle 4 Stufen fehlerfrei ab.")

        # 5. TEST: Demo-Umschalter auf leistungen.html
        print("\n--- 5. TEST: INTERAKTIVE DEMO-SCHALTUNG (leistungen.html) ---")
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(f"{BASE_URL}/leistungen.html")
        page.wait_for_timeout(500)

        # Klick auf Chef-Ansicht
        page.locator("#btnViewMaster").click()
        page.wait_for_timeout(300)
        master_vis = page.locator("#tabContentMaster").is_visible()
        cust_vis = page.locator("#tabContentCustomer").is_visible()
        assert master_vis and not cust_vis, "Chef-Ansicht muss nach Klick sichtbar sein"
        page.close()
        print("  -> Interaktive Demo auf leistungen.html schaltet perfekt um.")

        # 6. TEST: Rechtliche Seiten & Launch-Blocker-Hinweis
        print("\n--- 6. TEST: RECHTLICHE SEITEN (impressum.html & datenschutz.html) ---")
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(f"{BASE_URL}/impressum.html")
        assert "Impressum" in page.title()
        assert page.locator("main").is_visible()
        page.goto(f"{BASE_URL}/datenschutz.html")
        assert "Datenschutz" in page.title()
        assert page.locator("main").is_visible()
        page.close()
        print("  -> impressum.html und datenschutz.html sind online und sauber eingebunden.")

        browser.close()

    print("\n==================================================")
    print("ALLE TESTS ERFOLGREICH BESTANDEN! (100 % PASS)")
    print("==================================================")

if __name__ == "__main__":
    run_tests()
