import argparse, json, os, random
from google.cloud import storage
from diff_summary import summarize_change

BUCKET = os.environ["STATE_BUCKET"]

def _pick_blob(ts: str | None):
    client = storage.Client()
    bucket = client.bucket(BUCKET)
    prefix = f"diffs/{ts}/" if ts else "diffs/"
    blobs = [b for b in bucket.list_blobs(prefix=prefix) if b.name.endswith(".json")]
    if not blobs:
        raise SystemExit("❌  No diff JSON files found.")
    blob = random.choice(blobs)
    return blob.name, json.loads(blob.download_as_text())

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ts", help="specific timestamp folder (YYYYMMDD_HHMMSS)")
    args = ap.parse_args()

    path, data = _pick_blob(args.ts)
    print(f"📄  Picked: gs://{BUCKET}/{path}")
    print(f"🏷   {data['practice']} – {data['url']}\n")
    summary = summarize_change(data["old"], data["new"])
    print("🔎  Current prompt result:\n")
    print(summary)

if __name__ == "__main__":
    main()
