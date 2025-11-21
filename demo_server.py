from ai import analyze_text_with_ollama
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from storage import init_db, save_journal_entry, get_all_entries
from ai import analyze_text_with_ollama 

app = FastAPI()

# Run DB setup when FastAPI starts
@app.on_event("startup")
def startup_event():
    init_db()

class JournalInput(BaseModel):
    content: str

@app.post("/journal")
async def journal(input: JournalInput):
    save_journal_entry(input.content)
    return {"status": "saved"}

@app.get("/journal")
async def get_journal():
    entries = get_all_entries()
    return {"entries": entries}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

