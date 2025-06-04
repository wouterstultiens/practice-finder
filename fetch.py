"""
Networking helpers – focus on one thing: download & extract vacancy section.
Now supports both sync and async usage.
"""

from __future__ import annotations

import re
import requests
import aiohttp
from bs4 import BeautifulSoup
from typing import Optional

HEADERS = {"User-Agent": "Mozilla/5.0"}
_TIMEOUT = aiohttp.ClientTimeout(total=15)

# ---------------------------------------------------------------------------- #
# Internal helpers                                                             #
# ---------------------------------------------------------------------------- #

def _extract_content(
    html: str, selector: str, get_full_html: bool, *, print_soup: bool = False
) -> str:
    """Return the requested section from *html*."""
    soup = BeautifulSoup(html, "html.parser")

    if print_soup:
        print("\nSOUP:\n")
        print(soup.prettify())

    element = soup.select_one(selector)
    if not element:
        raise ValueError("HTML element not found")

    if get_full_html:
        return str(element).replace("\n", "")

    return re.sub(
        r"[\u200B-\u200D\uFEFF]|\s+", " ", element.get_text(separator=" ").strip()
    )

# ---------------------------------------------------------------------------- #
# Public API                                                                   #
# ---------------------------------------------------------------------------- #

def fetch_content(  # kept for CLI debugging
    url: str, selector: str, get_full_html: bool, print_soup: bool = False
) -> str:
    """
    Download *url* and return the text content of the first element
    that matches *selector*. Returns an empty string if nothing matched.
    """
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return _extract_content(resp.text, selector, get_full_html, print_soup=print_soup)

async def fetch_content_async(
    session: aiohttp.ClientSession, url: str, selector: str, get_full_html: bool
) -> str:
    """
    Asynchronously download *url* and return the text content of the first element
    that matches *selector*. Exceptions propagate to caller.
    """
    async with session.get(url, timeout=_TIMEOUT) as resp:
        resp.raise_for_status()
        text = await resp.text()
    return _extract_content(text, selector, get_full_html)

# Re-export for convenience -------------------------------------------------- #

__all__ = [
    "fetch_content",
    "fetch_content_async",
    "HEADERS",
]
