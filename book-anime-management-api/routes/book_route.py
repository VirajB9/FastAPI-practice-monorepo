from fastapi import APIRouter, Depends, HTTPException
from sql.database import get_db
from services.book_service import list_book, get_book_by_id, create_book, update_book, delete_book

book_router = APIRouter(prefix="/book", tags=["books"])


@book_router.get("/", summary="List all books")
def list_all(db=Depends(get_db)):
    return list_book(db)


@book_router.get("/{book_id}", )
def single_book(book_id: int, db=Depends(get_db)):
    book = get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.post("/", summary="Create a new book")
def add_book(book_data: dict, db=Depends(get_db)):
    return create_book(db, book_data)


@book_router.put("/{book_id}", summary="Update a book")
def modify_book(book_id: int, update_data: dict, db=Depends(get_db)):
    updated_book = update_book(db, book_id, update_data)
    if updated_book:
        return updated_book
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@book_router.delete("/{book_id}", summary="Delete a book")
def remove_book(book_id: int, db=Depends(get_db)):
    deleted = delete_book(db, book_id)
    if deleted:
        return {"message": "Book deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")
