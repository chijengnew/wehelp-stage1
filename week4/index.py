import csv
from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key-change-me")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

HOTELS_CSV = Path(__file__).parent / "hotels.csv"
with open(HOTELS_CSV, encoding="utf-8", newline="") as f:
    hotels = list(csv.reader(f))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/login")
def login(request: Request, email: str = Form(""), password: str = Form("")):
    if not email or not password:
        return RedirectResponse(url="/ohoh?msg=請輸入信箱和密碼", status_code=303)
    if email == "abc@abc.com" and password == "abc":
        request.session["logged_in"] = True
        return RedirectResponse(url="/member", status_code=303)
    return RedirectResponse(url="/ohoh?msg=信箱或密碼輸入錯誤", status_code=303)


@app.get("/member", response_class=HTMLResponse)
def member(request: Request):
    if not request.session.get("logged_in"):
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse(request, "member.html")


@app.get("/logout")
def logout(request: Request):
    request.session["logged_in"] = False
    return RedirectResponse(url="/", status_code=303)


@app.get("/ohoh", response_class=HTMLResponse)
def ohoh(request: Request, msg: str = ""):
    return templates.TemplateResponse(request, "ohoh.html", {"msg": msg})


@app.get("/hotel/{hotel_id}", response_class=HTMLResponse)
def hotel(request: Request, hotel_id: int):
    if 1 <= hotel_id <= len(hotels):
        row = hotels[hotel_id - 1]
        info = {"chinese": row[0], "english": row[1], "phone": row[4]}
        return templates.TemplateResponse(request, "hotel.html", {"hotel": info})
    return templates.TemplateResponse(request, "hotel.html", {"hotel": None})