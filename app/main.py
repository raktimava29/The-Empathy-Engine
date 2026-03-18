from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.router import router

app = FastAPI(
    title="Empathy Engine",
    description="Emotion-aware speech synthesis API",
    version="1.0"
)

app.mount("/audio", StaticFiles(directory="generated_audio"), name="audio")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(router)