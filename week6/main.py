import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import database

load_dotenv()

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ["SECRET_KEY"])
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
class MessageInput(BaseModel):
    content: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/member", response_class=HTMLResponse)
def member(request: Request):
    current = request.session.get("member")
    if current is None:
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse(request, "member.html", {"name": current["name"]})

@app.get("/ohoh", response_class=HTMLResponse)
def error(request: Request, msg: str = ""):
    return templates.TemplateResponse(request, "error.html", {"msg": msg})

@app.post("/signup")
def signup(name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    if database.get_member_by_email(email):
        return RedirectResponse(url="/ohoh?msg=重複的電子郵件", status_code=303)
    database.create_member(name, email, password)
    return RedirectResponse(url="/", status_code=303)

@app.post("/login")
def login(request: Request, email: str = Form(...), password: str = Form(...)):
    current = database.get_member_by_login(email, password)
    if current is None:
        return RedirectResponse(url="/ohoh?msg=電子郵件或密碼錯誤", status_code=303)
    request.session["member"] = current
    return RedirectResponse(url="/member", status_code=303)

@app.get("/logout")
def logout(request: Request):
    request.session.pop("member", None)
    return RedirectResponse(url="/", status_code=303)

@app.get("/api/message")
def list_messages(request: Request):
    current = request.session.get("member")
    if current is None:
        return JSONResponse({"error": True}, status_code=403)
    data = [
        {
            "id": row["id"],
            "name": row["name"],
            "content": row["content"],
            "self": row["member_id"] == current["id"],
        }
        for row in database.get_all_messages()
        ]
    return {"ok": True, "data": data}

@app.post("/api/message")
def add_message(request: Request, payload: MessageInput):
    current = request.session.get("member")
    if current is None:
        return JSONResponse({"error": True}, status_code=403)
    database.create_message(current["id"], payload.content)
    return {"ok": True}

@app.delete("/api/message/{message_id}")
def remove_message(request: Request, message_id: int):
    current = request.session.get("member")
    if current is None:
        return JSONResponse({"error": True}, status_code=403)
    if not database.delete_message(message_id, current["id"]):
        return JSONResponse({"error": True}, status_code=400)
    return {"ok": True}