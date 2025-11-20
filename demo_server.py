from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class JournalEntry(BaseModel):
    text: str

@app.post("/journal")
def journal(entry: JournalEntry):
    print("Received journal:", entry.text)
    return {"status": "ok", "received": entry.text}

@app.get("/")
def root():
    return {"status": "server running"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

