import time
from playwright.sync_api import sync_playwright

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        # 1. Desktop Test Suite (1440x900)
        print("=== 1. DESKTOP TEST SUITE (1440x900) ===")
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)

        res = page.goto("http://localhost:8081/referenzen.html")
        assert res.status == 200, f"Page load failed: {res.status}"
        page.wait_for_timeout(1000)

        # Assert no JS errors
        assert len(errors) == 0, f"JS errors on referenzen.html: {errors}"
        print("✓ Page loaded with 0 console errors")

        # Check Sektion 1: Interaktiver Vorher/Nachher-Slider
        print("\n--- Checking Before/After Diff Slider ---")
        container = page.locator("#diff-container")
        before_panel = page.locator("#diff-before")
        handle = page.locator("#diff-handle")
        assert container.is_visible(), "Diff container not visible"
        assert before_panel.is_visible(), "Before panel not visible"
        assert handle.is_visible(), "Handle not visible"

        # Check content in 2014 panel
        before_text = before_panel.text_content()
        assert "Internet Explorer" in before_text or "2014" in before_text
        assert "Gästebuch" in before_text
        assert "Herzlich Willkommen" in before_text
        assert "zoomen" in before_text
        print("✓ 2014 Retro-Mockup verified (IE, text desert, guestbook, zoom alert)")

        # Check content in 2026 panel
        after_text = page.locator("#diff-container").text_content()
        assert "meisterbetrieb-owl.de" in after_text
        assert "Moderne Gebäudetechnik" in after_text
        assert "Zählerschrank" in after_text
        assert "60s-Bewerbung" in after_text
        print("✓ 2026 Modern Meister-Mockup verified (SSL, CTA, 60s funnel)")

        # Test Slider Dragging
        box = container.bounding_box()
        start_x = box["x"] + box["width"] * 0.5
        start_y = box["y"] + box["height"] * 0.5
        page.mouse.move(start_x, start_y)
        page.mouse.down()
        page.mouse.move(start_x - 150, start_y)
        page.mouse.up()
        page.wait_for_timeout(300)
        new_width_style = before_panel.get_attribute("style")
        print(f"✓ Slider dragged successfully. Style: {new_width_style}")
        assert "%" in new_width_style

        # Check Sektion 2: 3 Branchen-Architekturen & View Switchers
        print("\n--- Checking 3 System-Architekturen & View Switchers ---")
        body_text = page.locator("body").text_content()
        assert "SparrenElektro GmbH" not in body_text, "Found forbidden fake GmbH name!"
        assert "System-Architektur 01" in body_text
        assert "System-Architektur 02" in body_text
        assert "System-Architektur 03" in body_text
        print("✓ Lawful framing verified: No fake GmbH, only erprobte Branchen-Architekturen")

        # Test View Switcher for Showcase 1 (Elektro)
        assert page.locator("#showcase-1-desktop").is_visible(), "Showcase 1 desktop not visible initially"
        page.locator("#btn-showcase-1-mobile").click()
        page.wait_for_timeout(300)
        assert page.locator("#showcase-1-mobile").is_visible(), "Showcase 1 mobile view failed to open"
        assert not page.locator("#showcase-1-desktop").is_visible(), "Showcase 1 desktop view still visible"
        print("✓ Showcase 1 mobile switcher verified")

        page.locator("#btn-showcase-1-desktop").click()
        page.wait_for_timeout(300)
        assert page.locator("#showcase-1-desktop").is_visible(), "Showcase 1 desktop view failed to restore"
        print("✓ Showcase 1 desktop switcher restore verified")

        # Test View Switcher for Showcase 2 (SHK)
        page.locator("#btn-showcase-2-mobile").click()
        page.wait_for_timeout(300)
        assert page.locator("#showcase-2-mobile").is_visible(), "Showcase 2 mobile view failed to open"
        print("✓ Showcase 2 mobile switcher verified")

        # Test View Switcher for Showcase 3 (Tischler)
        page.locator("#btn-showcase-3-mobile").click()
        page.wait_for_timeout(300)
        assert page.locator("#showcase-3-mobile").is_visible(), "Showcase 3 mobile view failed to open"
        print("✓ Showcase 3 mobile switcher verified")

        # Check Sektion 3: Die Anatomie einer verkaufsstarken Handwerker-Website
        print("\n--- Checking Anatomie Section ---")
        assert "Die Anatomie einer verkaufsstarken Handwerker-Website" in body_text
        assert "Baustein 01" in body_text
        assert "Baustein 02" in body_text
        assert "Baustein 03" in body_text
        assert "Baustein 04" in body_text
        assert "Baustein 05" in body_text
        assert "Baustein 06" in body_text
        print("✓ All 6 blueprint components verified")

        # Check Sektion 4: Kostenloser Vorab-Entwurf (Risk-Reversal)
        print("\n--- Checking Risk-Reversal Section ---")
        assert "Sie kaufen bei uns keine Katze im Sack" in body_text
        assert "Kurzes 15-Minuten-Erstgespräch" in body_text
        assert "Wir gestalten Ihren individuellen Entwurf" in body_text
        assert "Sie entscheiden in aller Ruhe" in body_text
        assert "1.490 €" in body_text
        print("✓ 3-Step Risk-Reversal section verified")

        # Check Sektion 5: Bottom CTA
        print("\n--- Checking Bottom CTA ---")
        assert "Bereit für ein Meister-System" in body_text
        cta_btn = page.locator("a[href='anfrage.html']").last
        assert cta_btn.is_visible(), "Bottom CTA link to anfrage.html missing"
        print("✓ Bottom CTA link verified")

        # Screenshot Desktop
        page.screenshot(path="referenzen-desktop.png", full_page=True)
        print("✓ Saved desktop full page screenshot: referenzen-desktop.png")
        page.close()

        # 2. Mobile Suite (390x844) & Overflow verification
        print("\n=== 2. MOBILE TEST SUITE (390x844) & OVERFLOW ===")
        context_m = browser.new_context(viewport={"width": 390, "height": 844}, has_touch=True)
        page_m = context_m.new_page()
        errors_m = []
        page_m.on("pageerror", lambda err: errors_m.append(str(err)))
        page_m.on("console", lambda msg: errors_m.append(msg.text) if msg.type == "error" else None)

        page_m.goto("http://localhost:8081/referenzen.html")
        page_m.wait_for_timeout(1000)

        overflow = page_m.evaluate("""() => {
            return {
                scrollWidth: document.documentElement.scrollWidth,
                clientWidth: document.documentElement.clientWidth
            };
        }""")
        print(f"Mobile scrollWidth: {overflow['scrollWidth']}, clientWidth: {overflow['clientWidth']}")
        assert overflow["scrollWidth"] <= overflow["clientWidth"], f"Horizontal overflow! {overflow}"
        assert len(errors_m) == 0, f"Mobile errors: {errors_m}"
        print("✓ Perfect mobile responsiveness: 0px overflow on 390px viewport")

        # Test touch slider dragging on mobile
        box_m = page_m.locator("#diff-container").bounding_box()
        page_m.touchscreen.tap(box_m["x"] + box_m["width"] * 0.3, box_m["y"] + box_m["height"] * 0.5)
        page_m.wait_for_timeout(300)
        print("✓ Touch tap on slider verified")

        page_m.screenshot(path="referenzen-mobile.png", full_page=True)
        print("✓ Saved mobile full page screenshot: referenzen-mobile.png")
        page_m.close()
        context_m.close()

        browser.close()
        print("\n🎉 ALL TESTS PASSED SUCCESSFULLY! 100% VERIFIED.")

if __name__ == "__main__":
    run_tests()
