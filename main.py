import requests
import time

APPS = [
    "https://spelling-homelearning.streamlit.app/",
    "https://reading-generator.streamlit.app/",
    "https://spelling-shed-app-create.streamlit.app/",
    "https://wfa-handwriting-tool.streamlit.app/",
    "https://word-puzzles.streamlit.app/",
    "https://wfa-reports.streamlit.app/",
    "https://spelling-tracker-home-learning.streamlit.app/",
]

for url in APPS:
    try:
        response = requests.get(url, timeout=30)
        print(f"✓ {url} — {response.status_code}")
    except Exception as e:
        print(f"✗ {url} — {e}")
    time.sleep(5)
