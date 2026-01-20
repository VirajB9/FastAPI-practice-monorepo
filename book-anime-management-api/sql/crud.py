from sqlalchemy.orm import Session
from sql.models import Book,Anime


# ---------------- BOOK CRUD ----------------

def get_all_books(db: Session):
    return db.query(Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book_data: Book):
    db.add(book_data)
    db.commit()
    db.refresh(book_data)
    return book_data


def update_book_by_id(db: Session, book_id: int, book_data: dict):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None

    for key, value in book_data.items():
            setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book: Book):
    db.delete(book)
    db.commit()
    return True




# ---------------- ANIME CRUD ----------------

def get_all_anime(db: Session):
    return db.query(Anime).all()


def create_anime(db: Session, anime_data: Anime):
    db.add(anime_data)
    db.commit()
    db.refresh(anime_data)
    return anime_data


def get_anime_by_id(db: Session, anime_id: int):
    return db.query(Anime).filter(Anime.id == anime_id).first()


def delete_anime(db: Session, anime_data: Anime):
    db.delete(anime_data)
    db.commit()


def update_anime_by_id(db: Session, anime_id: int, anime_data: dict):
    anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if not anime:
        return None

    for key, value in anime_data.items():  # Applying only keys provided in the incoming anime data dict
            setattr(anime, key, value)

    db.commit()
    db.refresh(anime)
    return anime
