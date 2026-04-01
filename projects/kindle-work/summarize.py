"""
Use Claude to summarize Kindle highlights for a book.
Usage: python summarize.py --book "Book Title"
       python summarize.py  (lists available books)
"""

import os
import json
import argparse
import anthropic
from dotenv import load_dotenv

load_dotenv()


def load_book(title: str) -> list[dict]:
    path = "output/clippings.json"
    if not os.path.exists(path):
        print("Run parse_clippings.py first.")
        return []
    with open(path) as f:
        data = json.load(f)
    matches = [k for k in data if title.lower() in k.lower()]
    if not matches:
        print(f"No book found matching '{title}'")
        print("Available books:")
        for k in data:
            print(f"  {k}")
        return []
    book_title = matches[0]
    print(f"Using: {book_title}")
    return data[book_title]


def summarize(book_title: str):
    highlights = load_book(book_title)
    if not highlights:
        return

    texts = [h["text"] for h in highlights if h["type"] == "Highlight"]
    if not texts:
        print("No highlights found for this book.")
        return

    combined = "\n\n---\n\n".join(texts[:100])  # cap at 100 highlights

    client = anthropic.Anthropic()
    print(f"\nSummarizing {len(texts)} highlights...\n")

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Below are my Kindle highlights from the book '{book_title}'.\n"
                    "Please give me:\n"
                    "1. A concise summary of the book's main ideas\n"
                    "2. The 5-7 most important insights from my highlights\n"
                    "3. Any actionable takeaways\n\n"
                    f"Highlights:\n{combined}"
                ),
            }
        ],
    )

    summary = message.content[0].text
    print(summary)

    os.makedirs("output", exist_ok=True)
    safe_name = book_title[:50].replace("/", "-").replace(":", "")
    out_path = f"output/{safe_name}_summary.md"
    with open(out_path, "w") as f:
        f.write(f"# Summary: {book_title}\n\n")
        f.write(summary)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", type=str, default="", help="Book title (partial match)")
    args = parser.parse_args()

    if not args.book:
        path = "output/clippings.json"
        if os.path.exists(path):
            with open(path) as f:
                data = json.load(f)
            print("Available books:")
            for k in sorted(data.keys()):
                print(f"  {k}")
        else:
            print("Run parse_clippings.py first.")
    else:
        summarize(args.book)
