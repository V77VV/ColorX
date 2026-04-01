import os
import anthropic
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="My App")

# Allow the frontend to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


# --- Models ---

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


# --- Routes ---

@app.get("/")
def root():
    return {"status": "ok", "message": "API is running"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    """Send a message and get a reply from Claude."""
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": req.message}],
    )
    return ChatResponse(reply=response.content[0].text)


# --- Run ---

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
