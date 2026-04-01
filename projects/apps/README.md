# Apps

Web and mobile applications. This project uses a Python backend (FastAPI) with a clean HTML/JS frontend — no frameworks needed.

## What's Here

| Folder | Description |
|--------|-------------|
| `backend/` | Python API server (FastAPI) |
| `frontend/` | HTML + CSS + JavaScript UI |

## Quick Start

```bash
git clone https://github.com/v77vv/apps
cd apps

# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add your API keys

# Run the server
python main.py
```

Then open `frontend/index.html` in your browser, or visit `http://localhost:8000`.

## Project Structure

```
apps/
├── backend/
│   ├── main.py          # FastAPI app — API routes live here
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── index.html       # Main page
│   ├── style.css        # Styles
│   └── app.js           # Fetch calls to the backend
└── README.md
```

## How to Add a New Feature

1. Add a new route in `backend/main.py`
2. Call it from `frontend/app.js` using `fetch()`
3. Display the result in `frontend/index.html`

## Deploying

- **Backend:** Deploy to [Railway](https://railway.app), [Render](https://render.com), or any VPS
- **Frontend:** Deploy to [GitHub Pages](https://pages.github.com) or [Netlify](https://netlify.com)

## License

MIT
