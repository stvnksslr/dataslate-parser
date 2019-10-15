from fastapi import FastAPI, File
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.utils.test_utils import get_parser_type_and_parse
from app.utils.zip_utils import unzip

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


@app.post("/files/")
def create_file(request: Request, file: bytes = File(...)):
    print("cats")
    data = get_parser_type_and_parse(roster=file)
    parsed_roster = data.get("roster")
    template = data.get("template")

    return templates.TemplateResponse(
        template, {"request": request, "roster": parsed_roster}
    )
