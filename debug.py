import argparse
from fetch import fetch_content
from config import PRACTICES

def main() -> None:
    parser = argparse.ArgumentParser(description="Debug CSS selector for a vacancy page.")
    parser.add_argument("id", help="Index of practice")
    args = parser.parse_args()

    practice = PRACTICES[int(args.id)]
    content = fetch_content(practice["url"], practice["selector"], True)
    print(f"\nCONTENT:\n{content}")

if __name__ == "__main__":
    main()