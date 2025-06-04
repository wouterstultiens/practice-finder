"""
Networking helpers – focus on one thing: download & extract vacancy section.
"""
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "VacancyMonitor/1.0 (+https://github.com/your-org/vacancy-monitor)"
}

def fetch_content(url: str, selector: str) -> str:
    """
    Download *url* and return the text content of the first element
    that matches *selector*. Returns an empty string if nothing matched.
    """
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    element = soup.select_one(selector)
    return element.get_text(strip=True, separator=" ") if element else ""