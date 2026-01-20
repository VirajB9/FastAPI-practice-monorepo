from sqlalchemy.orm import Session
from sql.models import Book, Anime
from sql import crud
from fastapi import HTTPException


def list_book(db: Session):
    return crud.get_all_books(db)


def get_book_by_id(db: Session, book_id: int):
    return crud.get_book_by_id(db, book_id)


def create_book(db: Session, book_data: dict):
    book = Book(**book_data)
    book = crud.create_book(db, book)

                        # Business logic : If a book of genre "X" is created, automatically create an associated anime.
    if book_data.get("genre") == "X":
        anime = Anime(title=f"{book.title} Anime",
                      genre="X",
                      book_id=book.id)
        crud.create_anime(db, anime)
    return book


def update_book(db: Session, book_id: int, book_update_data: dict):
    return crud.update_book_by_id(db, book_id, book_update_data)


def delete_book(db: Session, book_id: int):
    book = crud.get_book_by_id(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    crud.delete_book(db, book)
    return True
