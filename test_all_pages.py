import time
from playwright.sync_api import sync_playwright

pages_to_test = [
    ("index.html", "Startseite"),
    ("gewerke.html", "Lösungen nach Gewerk"),
    ("leistungen.html", "Leistungen & Funktionen"),
    ("referenzen.html", "Referenzen"),
    ("ablauf.html", "Ablauf & FAQ"),
    ("anfrage.html", "Projekt-Konfigurator")
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    # 1. Desktop tests (1440x900)
    print("=== DESKTOP SUITE (1440x900) ===")
    for path, name in pages_to_test:
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        
        url = f"http://localhost:8081/{path}"
        res = page.goto(url)
        assert res.status == 200, f"Failed to load {url}, status: {res.status}"
        page.wait_for_timeout(800)
        
        # Check title and navbar
        title = page.title()
        has_nav = page.locator("#navbar").is_visible()
        has_footer = page.locator("footer").is_visible()
        print(f"[{path}] Status 200, Title: '{title[:35]}...', Nav: {has_nav}, Footer: {has_footer}")
        
        # Check no errors
        assert len(errors) == 0, f"Errors on {path}: {errors}"
        page.close()

    # 2. Mobile tests (390x844) & Overflow verification
    print("\n=== MOBILE SUITE (390x844) & OVERFLOW ===")
    for path, name in pages_to_test:
        page_m = browser.new_page(viewport={"width": 390, "height": 844})
        errors = []
        page_m.on("pageerror", lambda err: errors.append(str(err)))
        page_m.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        
        url = f"http://localhost:8081/{path}"
        page_m.goto(url)
        page_m.wait_for_timeout(800)
        
        # Check overflow
        overflow = page_m.evaluate("""() => {
            return {
                scrollWidth: document.documentElement.scrollWidth,
                clientWidth: document.documentElement.clientWidth
            };
        }""")
        print(f"[{path}] Mobile scrollWidth: {overflow['scrollWidth']}, clientWidth: {overflow['clientWidth']}")
        assert overflow["scrollWidth"] <= overflow["clientWidth"], f"Horizontal overflow on {path}!"
        assert len(errors) == 0, f"Mobile errors on {path}: {errors}"
        page_m.close()

    # 3. Functional tests for interactive elements
    print("\n=== INTERACTIVE COMPONENT TESTS ===")
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    
    # Test Gewerke tabs
    page.goto("http://localhost:8081/gewerke.html")
    page.wait_for_timeout(500)
    page.locator("#tab-shk").click()
    page.wait_for_timeout(300)
    shk_visible = page.locator("#pane-shk").is_visible()
    dach_visible = page.locator("#pane-dach").is_visible()
    print("Gewerke tab switch: SHK visible =", shk_visible, ", Dach visible =", dach_visible)
    assert shk_visible and not dach_visible, "Gewerke tab switch failed!"

    # Test Leistungen demo
    page.goto("http://localhost:8081/leistungen.html")
    page.wait_for_timeout(500)
    page.locator("#demo-next-btn").click()
    page.wait_for_timeout(300)
    step2_visible = page.locator("#demo-step-2").is_visible()
    print("Leistungen demo step 2 visible:", step2_visible)
    assert step2_visible, "Leistungen demo step transition failed!"

    # Test Referenzen diff slider
    page.goto("http://localhost:8081/referenzen.html")
    page.wait_for_timeout(500)
    slider_visible = page.locator("#diff-container").is_visible()
    print("Referenzen diff slider visible:", slider_visible)
    assert slider_visible, "Diff slider missing!"

    # Test Ablauf ROI Calculator
    page.goto("http://localhost:8081/ablauf.html")
    page.wait_for_timeout(500)
    val_roi = page.locator("#res-roi").text_content()
    print("Ablauf ROI initial text:", val_roi)
    assert "%" in val_roi, "ROI Calculator failed to initialize!"

    # Test Ablauf FAQ Accordion
    first_faq_btn = page.locator("button[onclick='toggleSubpageFAQ(this)']").first
    first_faq_btn.click()
    page.wait_for_timeout(300)
    first_ans_visible = page.locator(".faq-answer").first.is_visible()
    print("Ablauf FAQ accordion toggle: answer visible =", first_ans_visible)
    assert first_ans_visible, "FAQ accordion failed to open!"

    # Test Anfrage Funnel
    page.goto("http://localhost:8081/anfrage.html")
    page.wait_for_timeout(500)
    # Pick trade in step 1
    page.locator(".funnel-card").first.click()
    page.locator("#funnel-next-btn").click()
    page.wait_for_timeout(300)
    step2_f_visible = page.locator("#step-2").is_visible()
    print("Anfrage Funnel step 2 visible:", step2_f_visible)
    assert step2_f_visible, "Funnel step 1->2 failed!"

    # Pick challenge in step 2
    page.locator("#step-2 .funnel-card").first.click()
    page.locator("#funnel-next-btn").click()
    page.wait_for_timeout(300)
    step3_f_visible = page.locator("#step-3").is_visible()
    print("Anfrage Funnel step 3 visible:", step3_f_visible)
    assert step3_f_visible, "Funnel step 2->3 failed!"

    # Pick package in step 3
    page.locator("#step-3 .funnel-card").first.click()
    page.locator("#funnel-next-btn").click()
    page.wait_for_timeout(300)
    step4_f_visible = page.locator("#step-4").is_visible()
    print("Anfrage Funnel step 4 visible:", step4_f_visible)
    assert step4_f_visible, "Funnel step 3->4 failed!"

    # Fill form in step 4
    page.fill("#f-name", "Meister Brinkmann")
    page.fill("#f-company", "Elektro Brinkmann GmbH")
    page.fill("#f-phone", "0521 1234567")
    page.fill("#f-email", "info@brinkmann-elektro.de")
    page.locator("#funnel-submit-btn").click()
    page.wait_for_timeout(300)
    success_visible = page.locator("#step-success").is_visible()
    print("Anfrage Funnel success view visible:", success_visible)
    assert success_visible, "Funnel submission failed!"

    # Test Mobile Menu Open / Close
    page_m = browser.new_page(viewport={"width": 390, "height": 844})
    page_m.goto("http://localhost:8081/gewerke.html")
    page_m.wait_for_timeout(500)
    m_menu_btn = page_m.locator("#mobile-menu-btn")
    m_menu_btn.click()
    page_m.wait_for_timeout(300)
    m_menu_visible = page_m.locator("#mobile-menu").is_visible()
    print("Mobile menu opened:", m_menu_visible)
    assert m_menu_visible, "Mobile menu failed to open!"
    m_menu_btn.click()
    page_m.wait_for_timeout(300)
    m_menu_closed = not page_m.locator("#mobile-menu").is_visible()
    print("Mobile menu closed:", m_menu_closed)
    assert m_menu_closed, "Mobile menu failed to close!"

    browser.close()
    print("\nALL AUTOMATED TESTS PASSED WITH 100% SUCCESS!")
