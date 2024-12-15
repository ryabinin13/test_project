from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    lastname = Column(String, index=True)
    birthday = Column(Date)
    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f'name: {self.name} lastname: {self.lastname} books: {self.books}'



class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    number_of_instances = Column(Integer)
    author = relationship("Author", back_populates="books")
    borrows = relationship("Borrow", back_populates="book")

    def __repr__(self):
        return f'title: {self.title} description: {self.description}'


class Borrow(Base):
    __tablename__ = "borrows"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    name_reader = Column(String, index=True)
    date_issue = Column(Date)
    date_return = Column(Date) 
    book = relationship("Book", back_populates="borrows")

    def __repr__(self):
        return f'<name_reader: {self.name_reader} date_issue: {self.date_issue} date_return: {self.date_return}'
