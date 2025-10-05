import time
from playwright.sync_api import sync_playwright, expect

def run_verification(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    try:
        # Assuming the app is running on localhost:5000
        page.goto("http://localhost:5000/", timeout=60000)

        # Wait for the page to redirect and load the dashboard
        # This might involve an OAuth flow in a real scenario,
        # but for this test, we'll assume we land on the dashboard.
        # We will wait for the tabs to be visible.
        expect(page.locator(".tabs .tab")).to_have_count(3, timeout=30000)

        # Take a screenshot of the initial tab (NIFTY FUT)
        page.screenshot(path="jules-scratch/verification/verification_nifty.png")

        # Click on the BANKNIFTY FUT tab
        banknifty_tab = page.locator(".tab", has_text="BANKNIFTY FUT")
        banknifty_tab.click()

        # Wait for the content of the second tab to be active
        expect(page.locator(".tab-content[data-symbol='NSE:BANKNIFTY24JULFUT']")).to_be_visible()

        # Give a moment for data to potentially load
        time.sleep(2)

        # Take a screenshot of the second tab
        page.screenshot(path="jules-scratch/verification/verification_banknifty.png")

        print("Successfully captured screenshots of both tabs.")

    except Exception as e:
        print(f"An error occurred during verification: {e}")
        # Take a screenshot of the error state
        page.screenshot(path="jules-scratch/verification/verification_error.png")

    finally:
        browser.close()

with sync_playwright() as playwright:
    run_verification(playwright)