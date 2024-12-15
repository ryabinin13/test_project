from app.schemas import BookBody
from app.repositories.book_repository import BookRepository

class BookService:

    def add_book(self, bookbody: BookBody):
        return BookRepository().create(bookbody)
    
    def get_book(self, id):
        return BookRepository().get(id)
    
    def get_all_book(self):
        return BookRepository().get_all()
    
    def delete_book(self, id):
        return BookRepository().delete(id)
    
    def update_book(self, id, bookbody: BookBody):
        return BookRepository().update(id, bookbody)