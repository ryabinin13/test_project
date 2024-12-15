from app import app
from app.schemas import AuthorBody
from fastapi import APIRouter
from app.services.author_service import AuthorService

router = APIRouter(prefix="/authors", tags=["authors"])

@app.post("/authors")
def add_author(authorbody: AuthorBody):
    return AuthorService().add_author(authorbody)

@app.get("/authors")
def get_author():
    return AuthorService().get_all_author()

@app.get("/authors/{id}")
def get_author_id(id):
    return AuthorService().get_author(id)

@app.put("/authors/{id}")
def update_author(id, authorbody: AuthorBody):
    return AuthorService().update_author(id, authorbody)

@app.delete("/authors/{id}")
def delete_author(id):
    return AuthorService().delete_author(id)