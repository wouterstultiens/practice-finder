# Vacancy Monitor

A lightweight, asynchronous Python scraper that tracks configured job listing pages for changes, summarizes them with an LLM, and sends notifications via Telegram.

This project is designed to run locally for development and be deployed as a serverless Google Cloud Function, triggered hourly by Cloud Scheduler.

## Features

- **Asynchronous Scraping**: Fetches dozens of websites concurrently using `aiohttp`.
- **Configurable Targets**: Easily add or modify target websites, CSS selectors, and content type (HTML vs. Text) in `config.py`.
- **Content Filtering**: A new `ignore_selectors` option allows you to remove unwanted parts (like ads or timestamps) from the scraped content before comparison.
- **Change Detection**: Compares the latest scrape against the last known version stored in Google Cloud Storage.
- **AI-Powered Summaries**: When a change is detected, OpenAI's GPT-4 generates a concise summary of what's new.
- **Telegram Notifications**: Sends alerts for new sites, updated vacancies, and fetch errors to one or more Telegram chats.
- **Robust Debugging**: Includes tools to test CSS selectors and LLM prompts locally before deploying.
- **Cloud-Native**: Designed for easy deployment on Google Cloud Functions (Gen 2).

---

## Prerequisites

- Python 3.11+
- A Google Cloud Platform project with:
  - Google Cloud SDK (`gcloud`) installed and authenticated.
  - A Google Cloud Storage (GCS) bucket.
- An OpenAI API Key.
- A Telegram Bot Token and the desired Chat ID(s).

---

## 1. Local Setup

**1.1. Clone and Install Dependencies**

```bash
git clone <your-repository-url>
cd vacancy-monitor
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**1.2. Configure Environment Variables**

Create a file named `.env` in the project root and add your secrets. The application will load this file automatically during local development.

```ini
# .env
# Google Cloud
STATE_BUCKET="your-gcs-bucket-name"
GCP_PROJECT_ID="your-gcp-project-id" # Optional, but good practice

# Services
OPENAI_API_KEY="sk-..."
TELEGRAM_BOT_TOKEN="12345:ABC..."
TELEGRAM_CHAT_IDS="chat_id_1,chat_id_2" # Comma-separated
```

---

## 2. Configuration

All target websites are defined in the `PRACTICES` list in `config.py`.

Each entry is a dictionary with the following keys:

- `name` (str): The human-readable name of the practice.
- `url` (str): The full URL of the vacancy page.
- `selector` (str): The CSS selector for the main content area to monitor.
- `get_html` (bool):
  - `True`: Monitor the raw HTML of the selected element.
  - `False`: Monitor only the extracted text content.
- `ignore_selectors` (list[str], optional): A list of CSS selectors within the main `selector` to remove before processing. This is perfect for ignoring dynamic content like "Last updated" timestamps, cookie banners, or ads.

**Example Entry in `config.py`:**

```python
{
    "name": "De Deventer Tandartspraktijk",
    "url": "https://www.dedeventertandartspraktijk.nl/vacatures",
    "selector": "article#post-131",
    "get_html": False,
    "ignore_selectors": ["div.cookie-notice", "span.timestamp"] # Optional
}
```

---

## 3. Usage and Debugging

When running scripts located within the `src/` directory (like the debug tools), you must run them as Python modules from the project root directory using `python -m`.

### 3.1. Running a Full Scan Locally

You can simulate a full monitoring cycle from your command line.

**Dry Run (prints notifications to console):**
```bash
# Run from the project root
python main.py
```

**Live Run (sends notifications to Telegram):**
```bash
# Run from the project root
python main.py --notify
```

### 3.2. Debugging a CSS Selector

Before adding a new practice to `config.py`, you need to find the correct CSS selector. This tool helps you test it.

```bash
# Run from the project root directory:
# The index corresponds to the practice's position in the PRACTICES list in config.py
python -m src.tools.debug_selector <index>
```
The script will fetch the page, show you the full HTML (for inspection if `--html` is used), and print the exact content it extracted using your selector. This lets you quickly verify and refine your selectors.

- If the specified `selector` is not found on the page, the script will output a specific error message.
- If the extracted content is empty, a warning will be shown, suggesting you double-check your selector or `ignore_selectors`.

Add `--html` flag to also print the full page HTML before extraction:
```bash
# Run from the project root directory:
python -m src.tools.debug_selector <index> --html
```


### 3.3. Debugging the LLM Prompt

If you want to improve the quality of the AI-generated summaries, you can test the prompt against real-world changes stored in GCS.

```bash
# Run from the project root directory:
# Fetches a random change from GCS and shows the summary
python -m src.tools.debug_prompt

# Fetches a change from a specific run timestamp (e.g., 20231027_153000)
python -m src.tools.debug_prompt --ts 20231027_153000
```
This script will download a random or specified change pair (old vs. new content) from your GCS bucket, pass it to the LLM, and print the old content, new content, and the resulting summary. This allows you to tweak the prompt in `src/services/llm.py` and immediately see the result.

---

## 4. Deployment to Google Cloud

**4.1. Create an `env.yaml` for Deployment**

GCP Functions read environment variables from a YAML file. Create `env.yaml` in the project root with the same keys as your `.env` file.

```yaml
# env.yaml
STATE_BUCKET: "your-gcs-bucket-name"
OPENAI_API_KEY: "sk-..."
TELEGRAM_BOT_TOKEN: "12345:ABC..."
TELEGRAM_CHAT_IDS: "chat_id_1,chat_id_2"
```
*Note: Do NOT commit `env.yaml` to Git as it contains secrets.*

**4.2. Deploy the Cloud Function**

Run the following `gcloud` command from the project root:

```bash
gcloud functions deploy vacancy-monitor \
  --gen2 \
  --runtime=python312 \
  --region=europe-west1 \
  --source=. \
  --entry-point=main_http \
  --trigger-http \
  --allow-unauthenticated \
  --timeout=300s \
  --env-vars-file=env.yaml
```
**Note:** `--allow-unauthenticated` is typically required for Cloud Scheduler to invoke the function via an HTTP trigger. Ensure your function trigger URL is protected appropriately if needed for production.

**4.3. Set up Cloud Scheduler**

Create a scheduler job to trigger the function every hour.

1. Go to the Cloud Scheduler page in the Google Cloud Console.
2. Click "Create Job".
3. **Frequency**: `0 * * * *` (for every hour at minute 0).
4. **Timezone**: Your preferred timezone (e.g., `Europe/Amsterdam`).
5. **Target type**: `HTTP`.
6. **URL**: The trigger URL of the function you just deployed (you can find this on the Cloud Functions page under the "Trigger" tab).
7. **HTTP Method**: `GET`.
8. Click "Create".

Your vacancy monitor is now live!

**4.4. Verify Deployment and Logs**

You can manually test the deployed function and check logs:

```bash
# Manually trigger the function
gcloud functions call vacancy-monitor --region=europe-west1

# Tail function logs
gcloud functions logs read vacancy-monitor --region=europe-west1 --limit=50
```


---

## 5. Repository Structure

```
.
├── .gcloudignore        # Files/dirs to exclude from deployment
├── .gitignore           # Files/dirs to exclude from Git
├── config.py            # Practice definitions (names, URLs, selectors)
├── main.py              # Cloud Function entry point & local CLI runner
├── readme.md            # This file
├── requirements.txt     # Python dependencies
└── src/                 # Main source code package
    ├── core/            # Core logic (monitoring, scraping)
    │   ├── monitor.py   # Orchestrates fetching, diffing, saving
    │   └── scraper.py   # Handles async HTTP fetching and content extraction/filtering
    ├── services/        # External integrations (GCS, LLM, Telegram)
    │   ├── gcs.py       # Google Cloud Storage operations
    │   ├── llm.py       # OpenAI LLM integration
    │   └── telegram.py  # Telegram notification sending
    └── tools/           # Local development/debugging tools
        ├── debug_prompt.py   # Debug LLM prompt with real data
        └── debug_selector.py # Debug CSS selectors for a single URL
```
*(Note: `__init__.py` files exist within directories but are not listed explicitly here for brevity).*

---

## 6. Dependencies

- `aiohttp`: Asynchronous HTTP client for efficient parallel fetching.
- `beautifulsoup4`: Robust HTML parsing and CSS selector engine.
- `openai`: Official Python library for interacting with the OpenAI API.
- `python-dotenv`: Loads environment variables from a `.env` file locally.
- `google-cloud-storage`: Client library for interacting with GCS.
- `functions-framework`: Library for writing serverless functions that run on Google Cloud.
- `python-telegram-bot`: Library for interacting with the Telegram Bot API.

---

## 7. License

This project is released under the MIT License.