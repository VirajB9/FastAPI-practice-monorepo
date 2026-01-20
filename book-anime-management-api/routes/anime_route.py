from fastapi import APIRouter, Depends, HTTPException
from sql.database import get_db
from services.anime_service import get_anime, create_anime, update_anime, delete_anime, list_anime

anime_router = APIRouter(prefix="/anime", tags=["anime"])


@anime_router.get("/", summary="List all anime")
def list_all(db=Depends(get_db)):
    return list_anime(db)


@anime_router.get("/{anime_id}", )
def single_anime(anime_id: int, db=Depends(get_db)):
    anime = get_anime(db, anime_id)
    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    return anime


@anime_router.post("/", summary="Create a new anime")
def add_anime(anime_data: dict, db=Depends(get_db)):
    return create_anime(db, anime_data)


@anime_router.put("/{anime_id}", summary="Update a anime")
def modify_anime(anime_id: int, update_data: dict, db=Depends(get_db)):
    updated_anime = update_anime(db, anime_id, update_data)
    if updated_anime:
        return updated_anime
    else:
        raise HTTPException(status_code=404, detail="Anime not found")


@anime_router.delete("/{anime_id}", summary="Delete a anime")
def remove_anime(anime_id: int, db=Depends(get_db)):
    deleted = delete_anime(db, anime_id)
    if deleted:
        return {"message": "Anime deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Anime not found")
