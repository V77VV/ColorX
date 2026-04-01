"""
Export Kindle highlights to markdown files (one per book).
Usage: python export.py
"""

import os
import json


def export_markdown():
    path = "output/clippings.json"
    if not os.path.exists(path):
        print("Run parse_clippings.py first.")
        return

    with open(path) as f:
        data = json.load(f)

    os.makedirs("output/books", exist_ok=True)

    for book_title, highlights in sorted(data.items()):
        safe_name = book_title[:60].replace("/", "-").replace(":", "").strip()
        out_path = f"output/books/{safe_name}.md"

        author = highlights[0]["author"] if highlights else "Unknown"

        with open(out_path, "w") as f:
            f.write(f"# {book_title}\n")
            f.write(f"*by {author}*\n\n")
            f.write(f"_{len(highlights)} highlights_\n\n---\n\n")

            for h in highlights:
                if h["type"] == "Note":
                    f.write(f"> **Note:** {h['text']}\n\n")
                elif h["type"] == "Highlight":
                    f.write(f"> {h['text']}\n\n")
                    if h.get("location"):
                        f.write(f"*{h['location']}*\n\n")

        print(f"  Exported: {safe_name}.md")

    print(f"\nDone. {len(data)} books saved to output/books/")


if __name__ == "__main__":
    export_markdown()
