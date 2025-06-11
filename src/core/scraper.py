import asyncio
import re
from typing import Any

import aiohttp
from bs4 import BeautifulSoup, Tag

# Set a reasonable user agent and timeout
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
CLIENT_TIMEOUT = aiohttp.ClientTimeout(total=45)


def _extract_content(
    html_content: bytes,
    config: dict[str, Any],
    debug_mode: bool = False
) -> str:
    """
    Parses HTML content and extracts the relevant part based on the config.

    Args:
        html_content: The raw HTML bytes of the page.
        config: A dictionary containing 'selector', 'get_html', and optional 'ignore_selectors'.
        debug_mode: If True, prints the full prettified HTML.

    Returns:
        The cleaned content (either HTML or text).

    Raises:
        ValueError: If the main selector does not find any element.
    """
    soup = BeautifulSoup(html_content, "html.parser")

    if debug_mode:
        print("--- FULL HTML SOUP ---\n")
        print(soup.prettify())
        print("\n--- END OF SOUP ---")

    element = soup.select_one(config["selector"])
    if not isinstance(element, Tag):
        raise ValueError(f"CSS selector '{config['selector']}' not found on page {config['url']}.")

    # Remove ignored sub-elements before processing
    if config.get("ignore_selectors"):
        for ignored_selector in config["ignore_selectors"]:
            for unwanted_element in element.select(ignored_selector):
                unwanted_element.decompose()

    if config["get_html"]:
        # Return cleaned HTML string
        return str(element).strip()
    else:
        # Return cleaned, normalized text
        text = element.get_text(separator=" ", strip=True)
        return re.sub(r"\s+", " ", text).strip()


async def fetch_and_parse(
    session: aiohttp.ClientSession,
    config: dict[str, Any],
    debug_mode: bool = False
) -> str:
    """
    Asynchronously fetches a URL and parses its content using specified selectors.

    Args:
        session: The aiohttp client session.
        config: A dictionary for the practice, including URL and selectors.
        debug_mode: Flag to enable verbose printing for debugging.

    Returns:
        The extracted content.
    """
    async with session.get(config["url"], timeout=CLIENT_TIMEOUT) as response:
        response.raise_for_status()
        raw_html = await response.read()
        return _extract_content(raw_html, config, debug_mode)