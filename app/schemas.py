from pydantic import BaseModel
from datetime import date

class AuthorBody(BaseModel):
    name: str
    lastname: str
    birthday: date

class BookBody(BaseModel):
    title: str
    description: str
    number_of_instances: int
    author_id: int

class BorrowBody(BaseModel):
    name_reader: str
    date_issue: date
    date_return: date
    book_id: int