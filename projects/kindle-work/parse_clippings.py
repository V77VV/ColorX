"""
Parse Kindle's "My Clippings.txt" into structured data.
Usage: python parse_clippings.py "data/My Clippings.txt"
"""

import sys
import json
import os
from dataclasses import dataclass, asdict
from collections import defaultdict


SEPARATOR = "=========="


@dataclass
class Highlight:
    book: str
    author: str
    type: str       # Highlight / Note / Bookmark
    location: str
    date: str
    text: str


def parse(filepath: str) -> dict[str, list[Highlight]]:
    with open(filepath, encoding="utf-8-sig") as f:
        raw = f.read()

    entries = [e.strip() for e in raw.split(SEPARATOR) if e.strip()]
    books: dict[str, list[Highlight]] = defaultdict(list)

    for entry in entries:
        lines = entry.splitlines()
        if len(lines) < 3:
            continue

        # Line 1: "Title (Author)"
        title_line = lines[0].strip()
        if "(" in title_line and title_line.endswith(")"):
            author = title_line[title_line.rfind("(") + 1 : -1].strip()
            book = title_line[: title_line.rfind("(")].strip()
        else:
            book, author = title_line, "Unknown"

        # Line 2: "- Your Highlight on Location X | Added on ..."
        meta = lines[1].strip("- ").strip()
        h_type = "Highlight"
        if "Note" in meta:
            h_type = "Note"
        elif "Bookmark" in meta:
            h_type = "Bookmark"

        location = ""
        date = ""
        if "Location" in meta:
            parts = meta.split("|")
            location = parts[0].strip()
            date = parts[1].strip() if len(parts) > 1 else ""

        text = "\n".join(lines[2:]).strip()
        if not text:
            continue

        books[book].append(Highlight(book, author, h_type, location, date, text))

    return books


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data/My Clippings.txt"
    if not os.path.exists(path):
        print(f"File not found: {path}")
        print("Put your Kindle clippings file at data/My Clippings.txt")
        return

    books = parse(path)
    total = sum(len(h) for h in books.values())
    print(f"Found {len(books)} books, {total} highlights/notes\n")

    for title, highlights in sorted(books.items()):
        print(f"  [{len(highlights):3d}]  {title}")

    # Save to JSON
    os.makedirs("output", exist_ok=True)
    data = {book: [asdict(h) for h in hl] for book, hl in books.items()}
    with open("output/clippings.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("\nSaved to output/clippings.json")


if __name__ == "__main__":
    main()
