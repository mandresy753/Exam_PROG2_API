import json
from fastapi import FastAPI, Request, status
from starlette.responses import Response
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def get_ping():
    return Response(content="pong", media_type="text/plain", status_code=200)

@app.get("/home")
def home():
    with open("home.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return Response(content=html_content, media_type="text/html", status_code=200)


@app.get("/{full_path:path}")
def catch_all(full_path: str):
    with open("404.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return Response(content=html_content, media_type="text/html", status_code=404)
class Post(BaseModel):
    author: str
    title: str
    content: str
    
posts_db = []
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    posts_db.append(post)
    json_content = json.dumps(posts_db, default=str, ensure_ascii=False, indent=4)
    return Response(content=json_content, media_type="application/json", status_code=201)

