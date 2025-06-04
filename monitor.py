"""
Main entry point – iterate over all practices defined in config.py
and append their current vacancy section to the CSV.
Run this every hour via cron or Task Scheduler.
"""
from datetime import datetime
from config import PRACTICES, CSV_PATH
from fetch import fetch_content
from storage import save_snapshot


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