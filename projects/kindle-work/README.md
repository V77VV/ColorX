# Kindle Work

Tools for managing, analyzing, and processing Kindle books and e-book collections.

## What This Does

- Export and parse Kindle highlights & notes
- Organize your reading library
- Generate summaries of highlights using AI
- Convert and manage e-book formats

## Setup

```bash
git clone https://github.com/v77vv/kindle-work
cd kindle-work
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set up your API key if using AI summaries:
```
cp .env.example .env
# edit .env and add your ANTHROPIC_API_KEY
```

## Usage

```bash
# Parse your Kindle clippings file
python parse_clippings.py "My Clippings.txt"

# Summarize highlights for a specific book using AI
python summarize.py --book "Book Title"

# Export all highlights to markdown
python export.py --format markdown
```

Your Kindle clippings file is usually found at:
- Connect Kindle via USB → `Kindle/documents/My Clippings.txt`

## Output

Highlights are saved to `output/` as individual markdown files per book, ready to use in Obsidian, Notion, or any note-taking app.

## Project Structure

```
kindle-work/
├── parse_clippings.py   # Parse "My Clippings.txt" from Kindle
├── summarize.py         # AI-powered highlight summarization
├── export.py            # Export to markdown / JSON / CSV
├── requirements.txt
├── .env.example
├── data/
│   └── My Clippings.txt # Put your Kindle clippings file here
└── output/              # Generated files appear here
```

## License

MIT
