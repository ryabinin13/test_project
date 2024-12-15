from app.schemas import BorrowBody
from app.models import Book, Borrow
from app.repositories.base_repository import BaseRepository

class BorrowRepository(BaseRepository):
    def __init__(self):
        super().__init__(Borrow)

    def create(self, borrowbody: BorrowBody):
        book = self.db.query(Book).where(Book.id == borrowbody.book_id).first()
        borrow = Borrow(name_reader = borrowbody.name_reader, date_issue = borrowbody.date_issue, date_return = borrowbody.date_return, book = book)
        self.db.add(borrow)
        #book.number_of_instances -= 1
        self.db.commit()
        return borrow
    
    def update(self, id, borrowbody: BorrowBody):
        pass

    def delete(self, id):
        borrow = self.db.query(Borrow).where(Borrow.id == id).first()
        #book.number_of_instances += 1
        self.db.delete(borrow)
        self.db.commit()
        return id