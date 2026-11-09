import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 900})

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: console_errors.append(str(err)))

        print("Navigating to http://localhost:8081/leistungen.html ...")
        await page.goto("http://localhost:8081/leistungen.html", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # 1. Verify text requirements & sections
        body_text = await page.inner_text("body")
        
        required_phrases = [
            "1.490 €",
            "Vollständig schlüsselfertige Website",
            "Interaktiver Vorabfilter mit Foto-Upload",
            "Überzeugende Projekt- & Referenz-Darstellung",
            "1-Klick-Kontaktwege",
            "Lokale Basis-SEO",
            "Rechtssicheres Impressum & DSGVO-Setup",
            "Modul 3 · Im 1.490 € Fundament fest integriert",
            "Google- & Bewertungs-Booster",
            "490 €",
            "Betriebs-Automation & Telefon-Assistenz",
            "2.990 €",
            "Warum kein WordPress-Baukasten? Der direkte Vergleich",
            "100 % Ihr Eigentum: Was passiert nach dem Go-Live?",
            "100 % Eigentum an Code & Domain",
            "0 € laufende Pflichtkosten – Sie entscheiden",
            "Schnelle Hilfe bei Änderungen auf Zuruf",
            "Direkter Praxisnutzen für Sie"
        ]

        for phrase in required_phrases:
            assert phrase in body_text, f"Missing required phrase: '{phrase}'"
        print("✓ All required copy & pricing phrases present.")

        # 2. Test interactive 3-step demo in Modul 2
        # Verify initial step 1 is visible
        assert await page.is_visible("#demo-step-1"), "Step 1 should be visible initially"
        
        # Click on second service option
        service_btn = page.locator(".demo-service-btn").nth(1)
        await service_btn.click()
        await page.wait_for_timeout(200)

        # Click next button to step 2
        next_btn = page.locator("#demo-next-btn")
        await next_btn.click()
        await page.wait_for_timeout(300)

        assert await page.is_visible("#demo-step-2"), "Step 2 should be visible"
        assert "2 / 3" in await page.inner_text("#demo-step-indicator"), "Indicator should show 2 / 3"

        # Simulate photo upload
        await page.locator("button:has-text('Klicken, um Foto-Upload zu simulieren')").click()
        await page.wait_for_timeout(200)
        assert "Dateien erfolgreich hochgeladen" in await page.inner_text("#demo-photo-status")

        # Advance to step 3
        await next_btn.click()
        await page.wait_for_timeout(300)
        assert await page.is_visible("#demo-step-3"), "Step 3 should be visible"
        assert "3 / 3" in await page.inner_text("#demo-step-indicator"), "Indicator should show 3 / 3"

        # Click send demo request
        await page.locator("button:has-text('Anfrage absenden (Demo)')").click()
        await page.wait_for_timeout(400)
        assert await page.is_visible("#demo-success-alert"), "Success alert should be visible after submit"

        # Check chef view on master's phone
        chef_service_text = await page.inner_text("#chef-preview-service")
        assert "Teilerneuerung" in chef_service_text, f"Chef preview should show selected service, got: {chef_service_text}"
        assert await page.is_visible("a:has-text('Kunden mit 1 Klick anrufen')"), "Chef call button should exist"
        print("✓ Interactive 3-step demo & live chef smartphone view fully functional.")

        # Test reset
        await page.locator("button:has-text('Zurücksetzen')").click()
        await page.wait_for_timeout(300)
        assert await page.is_visible("#demo-step-1"), "Step 1 should be visible after reset"
        print("✓ Demo reset works properly.")

        # 3. Check for horizontal overflow on desktop
        scroll_width = await page.evaluate("() => document.documentElement.scrollWidth")
        client_width = await page.evaluate("() => document.documentElement.clientWidth")
        assert scroll_width <= client_width, f"Desktop horizontal overflow detected: {scroll_width} > {client_width}"
        print(f"✓ Desktop horizontal fit: {scroll_width} <= {client_width}")

        # Capture Desktop Screenshots with AOS settle
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(800)
        await page.screenshot(path="scratch/leistungen_desktop_hero.png")

        # Scroll to Modul 1 & 2
        await page.locator("#vorqualifizierung").scroll_into_view_if_needed()
        await page.wait_for_timeout(800)
        await page.screenshot(path="scratch/leistungen_desktop_vorqualifizierung.png")

        # Scroll to comparison & 100% Eigentum
        await page.locator("#vergleich").scroll_into_view_if_needed()
        await page.wait_for_timeout(800)
        await page.screenshot(path="scratch/leistungen_desktop_vergleich.png")

        await browser.close()

        # 4. Mobile Responsiveness Test (390x844 - iPhone 14/15)
        page_mobile = await (await p.chromium.launch(headless=True)).new_page(
            viewport={"width": 390, "height": 844},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15"
        )
        await page_mobile.goto("http://localhost:8081/leistungen.html", wait_until="networkidle")
        await page_mobile.wait_for_timeout(1000)

        m_scroll_width = await page_mobile.evaluate("() => document.documentElement.scrollWidth")
        m_client_width = await page_mobile.evaluate("() => document.documentElement.clientWidth")
        assert m_scroll_width <= m_client_width, f"Mobile horizontal overflow: {m_scroll_width} > {m_client_width}"
        print(f"✓ Mobile horizontal fit (390px): {m_scroll_width} <= {m_client_width}")

        # Test mobile tab switcher for chef view
        assert await page_mobile.is_visible("#tab-btn-chef"), "Mobile chef tab button should be visible"
        await page_mobile.locator("#tab-btn-chef").click()
        await page_mobile.wait_for_timeout(400)
        assert await page_mobile.is_visible("#demo-chef-column"), "Chef column should be visible on mobile tab switch"

        # Mobile screenshots
        await page_mobile.locator("#vorqualifizierung").scroll_into_view_if_needed()
        await page_mobile.wait_for_timeout(800)
        await page_mobile.screenshot(path="scratch/leistungen_mobile_vorqualifizierung.png")

        await page_mobile.locator("#vergleich").scroll_into_view_if_needed()
        await page_mobile.wait_for_timeout(800)
        await page_mobile.screenshot(path="scratch/leistungen_mobile_vergleich.png")

        print("✓ Mobile tab switching & responsiveness verified.")

        # Check console errors
        print(f"Console errors recorded: {len(console_errors)}")
        if console_errors:
            print("Errors:", console_errors)
        assert len(console_errors) == 0, f"Found {len(console_errors)} console errors: {console_errors}"

        print("ALL TESTS PASSED WITH 0 ERRORS!")

if __name__ == "__main__":
    asyncio.run(run())
