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