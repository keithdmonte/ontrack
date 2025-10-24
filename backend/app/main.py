from fastapi import FastAPI

app = FastAPI(title="OnTrack API")

@app.get("/health")
def health():
    return {"status": "ok"}
