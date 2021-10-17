from uvicorn import run
from fastapi import FastAPI, File, UploadFile, Form
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.utils.battlescribe_meta import check_battlescribe_version
from src.utils.constants import BATTLESCRIBE_VERSION_ERROR
from src.utils.test_utils import get_parser_type_and_parse
from src.utils.zip_utils import check_if_zipped

app = FastAPI(
    title="Dataslate",
    description="Parsing tool to make more clean and easily printable outputs for battlescribe",
    version="1.1.10",
    redoc_url=None,
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src//static/templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/files/")
async def upload_roster(
    request: Request,
    multiple_pages: bool = Form(...),
    summary_page: bool = Form(...),
    use_icons: bool = Form(...),
    file: UploadFile = File(...)
):
    upload_contents = await check_if_zipped(file)
    supported_battlescribe_version = check_battlescribe_version(roster=upload_contents)

    if not supported_battlescribe_version:
        return BATTLESCRIBE_VERSION_ERROR

    data = get_parser_type_and_parse(roster=upload_contents, summary_page=summary_page)

    parsed_roster = data.get("roster")
    template = data.get("template")
    rules_summary = data.get("rules_summary")

    if use_icons:
        template = "icons_" + template

    return templates.TemplateResponse(
        template,
        {"request": request, "multiple_pages": multiple_pages, "rules_summary": rules_summary, "roster": parsed_roster},
    )


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
