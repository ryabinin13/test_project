from app import app
from app.schemas import BorrowBody
from fastapi import APIRouter
from app.services.borrow_service import BorrowService


router = APIRouter(prefix="/borrows", tags=["borrows"])

@app.get('/borrows')
def get_all_borrows():
    return BorrowService().get_all_borrows()

@app.get('/borrows/{id}')
def get_borrow(id):
    return BorrowService().get_borrow(id)


@app.post('/borrows')
def create_borrow(borrowbody:BorrowBody):
    return BorrowService().add_borrow(borrowbody)


@app.delete('/borrows/{id}')
def delete_borrow(id):
    return BorrowService().delete_borrow(id)

