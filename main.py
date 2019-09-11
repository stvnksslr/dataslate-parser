from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def root():
    return {"msg": "Hello World"}


@app.get("/render/killteam")
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})


@app.get("/render/30k")
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})


@app.get("/render/40k")
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})
