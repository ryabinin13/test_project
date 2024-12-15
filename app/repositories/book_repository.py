from app.schemas import BookBody
from app.models import Book, Author
from app.repositories.base_repository import BaseRepository

class BookRepository(BaseRepository):
    def __init__(self):
        super().__init__(Book)
    
    def create(self, bookbody: BookBody):
        author = self.db.query(Author).where(Author.id == bookbody.author_id).first()
        book = Book(title=bookbody.title, description=bookbody.description, number_of_instances=bookbody.number_of_instances, author=author)
        self.db.add(book)
        self.db.commit()
        return author.id
    
    def update(self, id, bookbody: BookBody):
        book = self.db.query(Book).where(Book.id == id).first()
        if book:
            book.title = bookbody.title
            book.description = bookbody.description
            book.author_id = bookbody.author_id
            book.number_of_instances = bookbody.number_of_instances

        self.db.commit()
        return book.id
    
    def delete(self, id):
        book = self.db.query(Book).where(Book.id == id).first()
        self.db.delete(book)
        self.db.commit()
        return id