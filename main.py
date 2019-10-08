from pathlib import Path

from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.utils.test_utils import fetch_and_parse_roster

app = FastAPI(
    title="Dataslate",
    description="Parsing tool to make more clean and easily printable outputs for battlescribe",
    version="1.0.0",
    redoc_url=None,
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app//static/templates")


@app.get("/")
async def root():
    return {"msg": "Hello World"}


@app.get("/render/kt/example")
def example(request: Request):
    return templates.TemplateResponse("40k_example.html", {"request": request})


@app.get("/render/sandbox")
def sandbox(request: Request):
    test_roster = generate_test_roster_heresy()

    return templates.TemplateResponse(
        "sandbox.html", {"request": request, "roster": test_roster}
    )


def generate_test_roster_heresy():
    base_path = Path.cwd() / "test_rosters" / "horus_heresy"
    chaos_kill_team_standard = str(base_path / "parser_test_full_list.ros")
    gametype = "heresy"
    parsed_roster = fetch_and_parse_roster(
        roster_file=chaos_kill_team_standard, gametype=gametype
    )
    return parsed_roster


def generate_test_roster():
    base_path = Path.cwd() / "test_rosters" / "kill_team"
    chaos_kill_team_standard = str(base_path / "test_roster_commander.ros")
    gametype = "killteam"
    parsed_roster = fetch_and_parse_roster(
        roster_file=chaos_kill_team_standard, gametype=gametype
    )
    return parsed_roster


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
