from playwright.sync_api import sync_playwright
import time

APPS = [
    "https://spelling-homelearning.streamlit.app/",
    "https://reading-generator.streamlit.app/",
    "https://spelling-shed-app-create.streamlit.app/",
    "https://wfa-handwriting-tool.streamlit.app/",
    "https://word-puzzles.streamlit.app/",
    "https://wfa-reports.streamlit.app/",
    "https://menu-publisher-new.streamlit.app/",
    "https://maths-reasoning.streamlit.app/",
]

def wake_app(page, url):
    print(f"Visiting {url} ...")
    try:
        page.goto(url, timeout=60000)
        page.wait_for_timeout(5000)  # let the page settle

        # Click the wake-up button if it appears
        wake_button = page.locator("text=Yes, get this app back up!")
        if wake_button.count() > 0:
            wake_button.click()
            print(f"  → Clicked wake button, waiting for app to start...")
            page.wait_for_timeout(15000)
        else:
            print(f"  → App already awake")

        print(f"✓ {url} — done")
    except Exception as e:
        print(f"✗ {url} — {e}")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for url in APPS:
        wake_app(page, url)
        time.sleep(3)

    browser.close()
