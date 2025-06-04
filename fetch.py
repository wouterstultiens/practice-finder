"""
Networking helpers – focus on one thing: download & extract vacancy section.
"""
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_content(url: str, selector: str, get_full_html: bool, print_soup: bool = False) -> str:
    """
    Download *url* and return the text content of the first element
    that matches *selector*. Returns an empty string if nothing matched.
    """
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    if print_soup:
        print("\nSOUP:\n")
        print(soup.prettify())
    element = soup.select_one(selector)

    if get_full_html:
        return str(element) if element else ""
    else:
        return element.get_text(strip=True, separator=" ") if element else ""