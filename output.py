# Define project structure and file contents
project_root = Path("/mnt/data/vacancy_monitor")
project_root.mkdir(parents=True, exist_ok=True)

# requirements.txt
(project_root / "requirements.txt").write_text("requests\nbeautifulsoup4\n")

# README.md
readme = """\
# Vacancy Monitor

Minimalistic hourly scraper that snapshots vacancy sections of up to 100 dental‑practice web pages.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

Edit **`vacancy_monitor/config.py`** and add your practices:

```python
PRACTICES = [
    {
        "name": "Smile Dental",
        "url": "https://example.com/jobs",
        "selector": "main div#vacancies"
    },
    # … add up to 100
]
```

Run the monitor once:

```bash
python vacancy_monitor/monitor.py
```

### Continuous hourly run (Linux cron)

```
0 * * * * /usr/bin/python /path/to/vacancy_monitor/monitor.py
```

### One‑off selector test

```bash
python vacancy_monitor/debug.py "https://example.com/jobs" "main div#vacancies"
```

The script appends snapshots to **`data/vacancy_snapshots.csv`** with columns:

* `practice`
* `url`
* `date`
* `hour`
* `content`

---

*Principles applied:*

* **KISS** – tiny codebase (~100 LOC), standard libs only.
* **DRY** – one fetch function reused everywhere, shared config.
* **YAGNI** – no databases, frameworks or diff logic until you need it.
"""
(project_root / "README.md").write_text(readme)

# make package dir
pkg_dir = project_root / "vacancy_monitor"
pkg_dir.mkdir(exist_ok=True)

# __init__.py
(pkg_dir / "__init__.py").write_text("# package marker\n")

# config.py
config_code = '''\
"""
Configuration file – list your practices here.

Each entry needs:
    name     – Friendly practice name
    url      – Vacuum page URL
    selector – CSS selector that isolates the element to snapshot
"""

from pathlib import Path

# Where CSV snapshots live (created automatically)
CSV_PATH = Path(__file__).with_suffix("").parent.parent / "data" / "vacancy_snapshots.csv"

PRACTICES = [
    # Example:
    # {
    #     "name": "Smile Dental",
    #     "url": "https://example.com/jobs",
    #     "selector": "main div#vacancies"
    # },
]
'''
(pkg_dir / "config.py").write_text(config_code)

# fetch.py
fetch_code = '''\
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
'''
(pkg_dir / "fetch.py").write_text(fetch_code)

# storage.py
storage_code = '''\
"""
CSV persistence – append one row per snapshot.
"""
import csv
from pathlib import Path
from typing import Dict

def save_snapshot(csv_path: Path, row: Dict[str, str]) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    file_exists = csv_path.exists()

    with csv_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
'''
(pkg_dir / "storage.py").write_text(storage_code)

# monitor.py
monitor_code = '''\
"""
Main entry point – iterate over all practices defined in config.py
and append their current vacancy section to the CSV.
Run this every hour via cron or Task Scheduler.
"""
from datetime import datetime
from .config import PRACTICES, CSV_PATH
from .fetch import fetch_content
from .storage import save_snapshot


def run_once() -> None:
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    hour_str = now.strftime("%H:00")

    for practice in PRACTICES:
        content = fetch_content(practice["url"], practice["selector"])
        row = {
            "practice": practice["name"],
            "url": practice["url"],
            "date": date_str,
            "hour": hour_str,
            "content": content,
        }
        save_snapshot(CSV_PATH, row)


if __name__ == "__main__":
    run_once()
'''
(pkg_dir / "monitor.py").write_text(monitor_code)

# debug.py
debug_code = '''\
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
'''
(pkg_dir / "debug.py").write_text(debug_code)

# data directory placeholder
(project_root / "data").mkdir(exist_ok=True)

# create zip
zip_path = Path("/mnt/data/vacancy_monitor_project.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for file in project_root.rglob("*"):
        if file.is_file():
            zf.write(file, file.relative_to(project_root.parent))

zip_path