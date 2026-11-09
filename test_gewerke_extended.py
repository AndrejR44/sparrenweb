import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    # 1. Desktop Test (1440x900)
    print("=== DESKTOP TEST GEWERKE.HTML ===")
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    
    res = page.goto("http://localhost:8081/gewerke.html")
    assert res.status == 200, "Status not 200"
    page.wait_for_timeout(800)
    
    # Test all 4 mockups interactivity
    trades = ["dach", "shk", "elektro", "tischler"]
    for trade in trades:
        print(f"\nTesting trade mockup: {trade.upper()}...")
        # Activate tab
        page.locator(f"#tab-{trade}").click()
        page.wait_for_timeout(300)
        
        # Verify step 1 is visible
        s1 = page.locator(f"#mock-{trade}-s1")
        assert s1.is_visible(), f"Step 1 not visible for {trade}"
        
        # Click first button in step 1
        first_btn = s1.locator("button").first
        btn_text = first_btn.inner_text().split("\n")[0]
        print(f"  Clicking option: '{btn_text}'...")
        first_btn.click()
        page.wait_for_timeout(300)
        
        # Verify step 2 is visible
        s2 = page.locator(f"#mock-{trade}-s2")
        assert s2.is_visible(), f"Step 2 not visible for {trade}"
        print(f"  Step 2 visible for {trade} ✓")
        
        # Click advance to step 3
        next_to_3 = s2.locator("button", has_text="Schritt 3")
        next_to_3.click()
        page.wait_for_timeout(300)
        
        # Verify step 3 is visible
        s3 = page.locator(f"#mock-{trade}-s3")
        assert s3.is_visible(), f"Step 3 not visible for {trade}"
        print(f"  Step 3 visible for {trade} ✓")
        
        # Reset mockup
        reset_btn = s3.locator("button", has_text="Demo neu starten")
        reset_btn.click()
        page.wait_for_timeout(300)
        assert s1.is_visible() and not s3.is_visible(), f"Reset failed for {trade}"
        print(f"  Reset to Step 1 verified for {trade} ✓")

    # Verify New Section 2: Weitere Gewerke (6 cards)
    print("\nVerifying Section 2 (Weitere Gewerke in OWL)...")
    body_text = page.inner_text("body")
    has_galabau = "GaLaBau, Pflaster- & Erdarbeiten" in body_text
    has_maler = "Maler, Putz, WDVS & Fassade" in body_text
    has_fliesen = "Fliesen-, Platten- & Natursteinleger" in body_text
    has_metall = "Metall-, Geländer- & Stahlbau" in body_text
    has_maurer = "Maurer, Beton- & Sanierungsbau" in body_text
    has_boden = "Raumausstatter, Boden- & Parkettleger" in body_text
    assert all([has_galabau, has_maler, has_fliesen, has_metall, has_maurer, has_boden]), "Missing cards in section 2"
    print("  All 6 trade cards verified ✓")

    # Verify New Section 3: Zwei Probleme, eine Lösung
    print("\nVerifying Section 3 (Zwei Probleme, eine Lösung)...")
    has_sec3 = "Zwei Probleme, eine Lösung: Lukrative Aufträge & gute Fachkräfte" in body_text
    assert has_sec3, "Section 3 headline missing"
    print("  Section 3 verified ✓")

    # Verify New Section 4: Auftrags-Magnet bei Google
    print("\nVerifying Section 4 (Auftrags-Magnet bei Google)...")
    has_sec4 = "Auftrags-Magnet bei Google: Wonach Ihre Wunschkunden in OWL suchen" in body_text
    assert has_sec4, "Section 4 headline missing"
    print("  Section 4 verified ✓")

    # Verify New Section 5: 100% schlüsselfertig
    print("\nVerifying Section 5 (100 % schlüsselfertig)...")
    has_sec5 = "100 % schlüsselfertig: Sie müssen keine einzige Zeile Fachtext selbst schreiben" in body_text
    assert has_sec5, "Section 5 headline missing"
    print("  Section 5 verified ✓")

    page.screenshot(path="scratch/gewerke_desktop_updated.png", full_page=True)
    assert len(errors) == 0, f"Console/page errors found: {errors}"
    print("\nDesktop check: 0 errors! Screenshot saved.")
    page.close()

    # 2. Mobile Test (390x844)
    print("\n=== MOBILE TEST (390x844) ===")
    page_m = browser.new_page(viewport={"width": 390, "height": 844})
    page_m.goto("http://localhost:8081/gewerke.html")
    page_m.wait_for_timeout(800)
    
    overflow = page_m.evaluate("""() => {
        return {
            scrollWidth: document.documentElement.scrollWidth,
            clientWidth: document.documentElement.clientWidth
        };
    }""")
    print(f"Mobile overflow: scrollWidth={overflow['scrollWidth']}, clientWidth={overflow['clientWidth']}")
    assert overflow["scrollWidth"] <= overflow["clientWidth"], "Horizontal overflow detected on mobile!"
    page_m.screenshot(path="scratch/gewerke_mobile_updated.png", full_page=True)
    page_m.close()

    browser.close()
    print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
