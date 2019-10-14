from pathlib import Path

from fastapi import FastAPI, File
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.utils.test_utils import generate_test_roster_heresy, get_parser_and_parse_roster

app = FastAPI(
    title="Dataslate",
    description="Parsing tool to make more clean and easily printable outputs for battlescribe",
    version="1.0.0",
    redoc_url=None,
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app//static/templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/render/kt/example")
def example(request: Request):
    return templates.TemplateResponse("40k_example.html", {"request": request})


@app.get("/render/heresy/example")
def heresy_example(request: Request):
    test_roster = generate_test_roster_heresy()

    return templates.TemplateResponse(
        "sandbox.html", {"request": request, "roster": test_roster}
    )


@app.post("/files/")
async def create_file(request: Request, file: bytes = File(...)):
    data = get_parser_and_parse_roster(roster=file)
    parsed_roster = data.get("roster")
    template = data.get("template")

    return templates.TemplateResponse(
        template, {"request": request, "roster": parsed_roster}
    )


@app.get("/render/kt")
async def render_kt(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})


@app.get("/render/kt/roster")
async def render_kt_roster(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})


@app.get("/render/30k")
async def render_heresy(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})


@app.get("/render/40k")
async def render_40k(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})
