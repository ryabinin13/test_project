from app import app
from app.schemas import BookBody
from fastapi import APIRouter
from app.services.book_service import BookService

router = APIRouter(prefix="/books", tags=["books"])

@app.post('/books')
def add_book(bookbody: BookBody):
    return BookService().add_book(bookbody)

@app.get('/books')
def get_all_books():
    return BookService().get_all_book()

@app.get('/books/{id}')
def get_book(id):
    return BookService().get_book(id)

@app.put('/books/{id}')
def update_book(id, bookbody: BookBody):
    return BookService().update_book(id, bookbody)

@app.delete('/books/{id}')
def delete_book(id):
    return BookService().delete_book(id)