from app.repositories.borrow_repository import BorrowRepository
from app.repositories.book_repository import BookRepository
from app.schemas import BorrowBody, BookBody

class BorrowService:

    def add_borrow(self, borrowbody: BorrowBody):

        book = BookRepository().get(borrowbody.book_id)

        bookbody = BookBody(
            title = book.title,
            description = book.description,
            number_of_instances = book.number_of_instances - 1,
            author_id = book.author_id  
        )

        BookRepository().update(book.id, bookbody)

        borrow = BorrowRepository().create(borrowbody)
        return borrow
    
    def get_borrow(self, id):
        return BorrowRepository().get(id)
    
    def get_all_borrows(self):
        return BorrowRepository().get_all()
    
    def delete_borrow(self, id):
        borrow = BorrowRepository().get(id)
        book = BookRepository().get(borrow.book_id)

        bookbody = BookBody(
            title = book.title,
            description = book.description,
            number_of_instances = book.number_of_instances + 1,
            author_id = book.author_id  
        )

        BookRepository().update(book.id, bookbody)

        return BorrowRepository().delete(id)
    
    # def update_book(self, id, bookbody: BookBody):
    #     return BookRepository().update(bookbody, id)