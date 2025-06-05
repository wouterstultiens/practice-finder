"""
Networking helpers – focus on one thing: download & extract vacancy section.
Now supports both sync and async usage.
"""

from __future__ import annotations

import re
import requests
import aiohttp
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}
# Slower sites needed a longer total timeout
_TIMEOUT = aiohttp.ClientTimeout(total=90)

# ---------------------------------------------------------------------------- #
# Internal helpers                                                             #
# ---------------------------------------------------------------------------- #
def _extract_content(html: str, selector: str, get_full_html: bool, print_soup: bool) -> str:
    """Return the requested section from *html*."""
    soup = BeautifulSoup(html, "html.parser")
    if print_soup:
        print("SOUP:\n")
        print(soup.prettify())

    element = soup.select_one(selector)
    if not element:
        raise ValueError("HTML element not found")

    if get_full_html:
        return str(element).replace("\n", "")

    return re.sub(
        r"[\u200B-\u200D\uFEFF]|\s+",
        " ",
        element.get_text(separator=" ").strip(),
    )

# ---------------------------------------------------------------------------- #
# Public sync helper (still used by debug CLI)                                 #
# ---------------------------------------------------------------------------- #
def fetch_content(url: str, selector: str, get_full_html: bool, print_soup: bool = False) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    raw = resp.content

    try:
        return _extract_content(raw.decode("utf-8"), selector, get_full_html, print_soup)
    except UnicodeDecodeError:
        # Fallback to BS-detected encoding
        soup = BeautifulSoup(raw, "html.parser")
        if print_soup:
            print("SOUP:\n")
            print(soup.prettify())
        element = soup.select_one(selector)
        if not element:
            raise ValueError("HTML element not found")
        return str(element) if get_full_html else re.sub(
            r"[\u200B-\u200D\uFEFF]|\s+", " ", element.get_text(separator=" ").strip()
        )

# ---------------------------------------------------------------------------- #
# Async version (used by Cloud Function)                                       #
# ---------------------------------------------------------------------------- #
async def fetch_content_async(
    session: aiohttp.ClientSession, url: str, selector: str, get_full_html: bool
) -> str:
    async with session.get(url, timeout=_TIMEOUT) as resp:
        resp.raise_for_status()
        raw = await resp.read()

    try:
        return _extract_content(raw.decode("utf-8"), selector, get_full_html, False)
    except UnicodeDecodeError:
        soup = BeautifulSoup(raw, "html.parser")
        element = soup.select_one(selector)
        if not element:
            raise ValueError("HTML element not found")
        return str(element) if get_full_html else re.sub(
            r"[\u200B-\u200D\uFEFF]|\s+", " ", element.get_text(separator=" ").strip()
        )

__all__ = ["fetch_content", "fetch_content_async", "HEADERS"]
