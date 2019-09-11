from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI(
    title="Dataslate",
    description="Parsing tool to make more clean and easily printable outputs for battlescribe",
    version="1.0.0",
    redoc_url=None
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def root():
    return {"msg": "Hello World"}


@app.get("/render/kt")
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})


@app.get("/render/kt/roster")
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})


@app.get("/render/30k")
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})


@app.get("/render/40k")
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})
