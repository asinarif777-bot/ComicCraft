from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/create")
def create_comic(request: Request, story: str = Form(...)):
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={"story": story}
    )