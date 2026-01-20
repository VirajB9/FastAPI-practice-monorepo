from sql.models import Anime
from sqlalchemy.orm import Session
from sql import crud
from fastapi import HTTPException


def list_anime(db: Session):
    return crud.get_all_anime(db)


def get_anime(db: Session, anime_id: int):
    return crud.get_anime_by_id(db, anime_id)


def create_anime(db: Session, anime_data: dict):
    anime = Anime(**anime_data)
    return crud.create_anime(db, anime)


def update_anime(db: Session, anime_id: int, anime_update_data: dict):
                            # Business logic: imdb rating decides the book availability and the anime's no of episodes
    if "imdb_rating" in anime_update_data and anime_update_data["imdb_rating"] is not None:
        rating = anime_update_data["imdb_rating"]
        anime = crud.get_anime_by_id(db, anime_id)

        if not anime:
            raise HTTPException(status_code=404, detail="Anime not found")

        book = anime.book
        updated_aval_book = 0

        if rating < 5:              # book's available status becomes false if rating is below 5
            if book:
                updated_aval_book = dict(available=False)
        elif 5 < rating <= 8:
            if book:                 # book's available status becomes true if rating is between 5 and 8
                updated_aval_book = dict(available=True)
        else:
            if anime.episodes is not None:          # if rating is above 8, increase no of episodes by 100%
                anime_update_data["episodes"] = anime.episodes * 2

        if updated_aval_book:
            crud.update_book_by_id(db, book.id, updated_aval_book)

    return crud.update_anime_by_id(db, anime_id, anime_update_data)


def delete_anime(db: Session, anime_id: int):
    anime = crud.get_anime_by_id(db, anime_id)

    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")

    if anime.genre == "X" and anime.book:       # Business logic: When deleting an anime, also delete the associated book if it exists.
        crud.delete_book(db, anime.book)
        return True

    crud.delete_anime(db, anime)
    return True
