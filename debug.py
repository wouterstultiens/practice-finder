"""
Quick‑and‑dirty helper to experiment with selectors.
Example:
    python debug.py "https://example.com/jobs" "div#vacancies"
"""
import argparse, textwrap
from .fetch import fetch_content

def main() -> None:
    parser = argparse.ArgumentParser(description="Debug CSS selector for a vacancy page.")
    parser.add_argument("url", help="Vacancy page URL")
    parser.add_argument("selector", help="CSS selector to isolate vacancy content")
    args = parser.parse_args()

    content = fetch_content(args.url, args.selector)
    preview = textwrap.shorten(content, width=500, placeholder=" …")
    print(f"🔍 Extracted ({len(content)} chars):\\n")
    print(preview)

if __name__ == "__main__":
    main()