'''main.py'''
from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from services import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")



# Users Routes
@app.get("/users")
def list_users(request: Request, db: Session = Depends(get_db)):
    users = get_users(db)
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/users/create")
def create_user_form(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})

@app.post("/users/create")
def create_user_action(username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    create_user(db, username, email, password)
    return RedirectResponse(url="/users", status_code=303)

@app.get("/users/edit/{user_id}")
def edit_user_form(request: Request, user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("edit_user.html", {"request": request, "user": user})

@app.post("/users/edit/{user_id}")
def edit_user_action(user_id: int, username: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    update_user(db, user_id, username, email)
    return RedirectResponse(url="/users", status_code=303)

@app.get("/users/delete/{user_id}")
def delete_user_action(user_id: int, db: Session = Depends(get_db)):
    delete_user(db, user_id)
    return RedirectResponse(url="/users", status_code=303)

# Posts Routes
@app.get("/posts")
def list_posts(request: Request, db: Session = Depends(get_db)):
    posts = get_posts(db)
    return templates.TemplateResponse("posts.html", {"request": request, "posts": posts})

@app.get("/posts/create")
def create_post_form(request: Request, db: Session = Depends(get_db)):
    users = get_users(db)
    return templates.TemplateResponse("create_post.html", {"request": request, "users": users})

@app.post("/posts/create")
def create_post_action(title: str = Form(...), content: str = Form(...), user_id: int = Form(...), db: Session = Depends(get_db)):
    create_post(db, title, content, user_id)
    return RedirectResponse(url="/posts", status_code=303)

@app.get("/posts/edit/{post_id}")
def edit_post_form(request: Request, post_id: int, db: Session = Depends(get_db)):
    post = get_post_by_id(db, post_id)
    users = get_users(db)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return templates.TemplateResponse("edit_post.html", {"request": request, "post": post, "users": users})

@app.post("/posts/edit/{post_id}")
def edit_post_action(post_id: int, title: str = Form(...), content: str = Form(...), user_id: int = Form(...), db: Session = Depends(get_db)):
    update_post(db, post_id, title, content, user_id)
    return RedirectResponse(url="/posts", status_code=303)

@app.get("/posts/delete/{post_id}")
def delete_post_action(post_id: int, db: Session = Depends(get_db)):
    delete_post(db, post_id)
    return RedirectResponse(url="/posts", status_code=303)
