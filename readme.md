# Vacancy Monitor

A lightweight Python scraper that tracks configured vacancy (job listing) pages, detects changes, and sends Telegram notifications. Designed to run as a Google Cloud Function (Gen 2) on an hourly schedule, with a local CLI mode for development.

---

## Prerequisites

* Python 3.11+ (3.12 tested)
* Google Cloud SDK (`gcloud`)
* Telegram Bot Token & Chat ID(s)
* A Google Cloud Storage bucket for state & snapshots

---

## Quick Start

1. **Clone & Install**

   ```bash
   git clone https://github.com/your-org/vacancy-monitor.git
   cd vacancy-monitor
   python3 -m venv .venv   # optional
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**

   Create a `.env` file or export on your shell:

   ```bash
   export BOT_TOKEN=<your-telegram-bot-token>
   export CHAT_IDS=<comma-separated-chat-ids>
   export STATE_BUCKET=<your-gcs-bucket-name>
   export OPENAI_API_KEY=<your-openai-api-key>
   ```

3. **Local Testing (CLI Mode)**

   * Run without notifications (prints to stdout):

     ```bash
     python main.py
     ```

   * Run and send to Telegram (requires `BOT_TOKEN` & `CHAT_IDS`):

     ```bash
     python main.py --notify
     ```

---

## Configuration

* **Vacancy Definitions**:  
  Edit `config.py` → `PRACTICES` list. Each item has:

  ```python
  {
      "name":        "Friendly Clinic",
      "url":         "https://example.com/vacatures",
      "selector":    "div.vacancy-list",
      "get_full_html": False
  }
  ```

* **State & Snapshots**:

  * `state.json` (in GCS): last-seen HTML per URL.
  * `snapshots/YYYYMMDD_HHMMSS.json`: full state archive.
  * `snapshots/failed/YYYYMMDD_HHMMSS.json`: failed URLs.

---

## Deployment

1. **Reload `.env` (if needed)**

   ```bash
   export $(grep -v '^#' .env | xargs)
   ```

2. **(Re)Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Deploy Cloud Function**

   ```bash
   gcloud functions deploy vacancy-monitor \
     --gen2 \
     --runtime python312 \
     --region europe-west4 \
     --entry-point main \
     --source=. \
     --trigger-http \
     --timeout=180s \
     --set-env-vars "BOT_TOKEN=${BOT_TOKEN},CHAT_IDS=${CHAT_IDS},STATE_BUCKET=${STATE_BUCKET},OPENAI_API_KEY=${OPENAI_API_KEY}"
   ```

4. **Update Cloud Scheduler Job (if URL changed)**

   ```bash
   FUNCTION_URL=$(gcloud functions describe vacancy-monitor \
     --region=europe-west4 \
     --format='value(serviceConfig.uri)')

   gcloud scheduler jobs update http vacancy-monitor-hourly \
     --location=europe-west1 \
     --schedule "0 * * * *" \
     --uri "${FUNCTION_URL}" \
     --http-method=GET \
     --time-zone "Europe/Amsterdam"
   ```

5. **Manual Invocation (Verify)**

   ```bash
   gcloud functions call vacancy-monitor --region=europe-west4
   ```

6. **Tail Logs**

   ```bash
   gcloud functions logs read vacancy-monitor --region=europe-west4 --limit=20

   gcloud logging read \
     'resource.type="cloud_run_revision" AND \
      resource.labels.service_name="vacancy-monitor"' \
     --project=<YOUR_PROJECT_ID> \
     --limit=20 \
     --format="table(timestamp, severity, textPayload)"
   ```

---

## Repository Structure

```
├── .gcloudignore
├── .gitignore
├── config.py
├── debug.py
├── fetch.py
├── main.py
├── monitor.py
├── notifier.py
├── readme.md
├── requirements.txt
├── state.py
├── storage.py
└── data/             (local cache for CSV snapshots, ignored by Git)
```

---

## Usage

1. **Monitoring Flow**

   * `monitor.run_once()` fetches all URLs (concurrently), diffs against `state.json` in GCS, archives a new snapshot, logs failures, updates `state.json`, and returns a list of human-readable messages.
   * `notifier.send(messages)` either prints (CLI mode) or sends to Telegram.
   * In Cloud Function mode, `main(request)` calls `run_once()` on each HTTP trigger (hourly via Scheduler).

2. **Debugging a Single Vacancy Fetch**

   ```bash
   python debug.py <index>
   ```

   Where `<index>` is the zero-based index of a practice in `config.py`.
   Prints the extracted content for troubleshooting your CSS selector.

3. **Automatic Encoding Detection**

   Pages served in encodings like ISO-8859-1 or Windows-1252 are handled seamlessly:

   * It first attempts to decode the response body as UTF-8.
   * If that fails, it feeds the raw bytes into BeautifulSoup, which auto-detects the correct charset via `<meta charset>` or other heuristics.
   * This means you no longer need to worry about `'utf-8' codec can't decode byte …` errors when hitting pages in Latin-1, etc.

   Just make sure you're using the latest version of `fetch.py`.

---

## Development

* Add or update entries in `config.py` → `PRACTICES` to watch new vacancy pages.
* Use `python main.py` locally to verify before deploying.
* If you modify `requirements.txt`, re-run `pip install -r requirements.txt` before deployment.
* Logging uses `logging.INFO` by default—check Cloud Function logs for details.

---

## Dependencies

* `aiohttp` – asynchronous HTTP requests  
* `beautifulsoup4` – HTML parsing & CSS selectors  
* `requests` – synchronous HTTP for CLI/debug  
* `python-telegram-bot` – Telegram notifications  
* `google-cloud-storage` – state & snapshot persistence in GCS  
* `functions-framework` – Cloud Function entry point

---

## License

This project is released under the MIT License.
