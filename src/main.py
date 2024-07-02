from fastapi import FastAPI, File, Form, UploadFile
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run

from src.utils.battlescribe_meta import check_battlescribe_version
from src.utils.constants import BATTLESCRIBE_VERSION_ERROR
from src.utils.logger_manager import init_logging
from src.utils.test_utils import get_parser_type_and_parse
from src.utils.zip_utils import check_if_zipped

init_logging()

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
    return templates.TemplateResponse(request, "home.html")


@app.post("/files/")
async def upload_roster(
    request: Request,
    multiple_pages: bool = Form(...),
    summary_page: bool = Form(...),
    use_icons: bool = Form(...),
    file: UploadFile = File(...),
):
    upload_contents = await check_if_zipped(file)
    if not check_battlescribe_version(roster=upload_contents):
        return BATTLESCRIBE_VERSION_ERROR

    data = get_parser_type_and_parse(roster=upload_contents, summary_page=summary_page)
    template = "icons_" + data.get("template") if use_icons else data.get("template")

    return templates.TemplateResponse(
        request=request,
        name=template,
        context={
            "multiple_pages": multiple_pages,
            "rules_summary": data.get("rules_summary"),
            "roster": data.get("roster"),
        },
    )


if __name__ == "__main__":
    run("__main__:app", host="localhost", port=8080, reload=True)
