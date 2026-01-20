from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sql.database import get_db
from services.theater_service import (
    create_theater_service,
    list_theater_service,
    update_theater_service,
    delete_theater_service,
)

theater_router= APIRouter(prefix="/theaters", tags=["Theaters"])

@theater_router.post("/")
def create_theater(data: dict, db: Session = Depends(get_db)):
    return create_theater_service(data, db)

@theater_router.get("/")
def list_theaters(db: Session = Depends(get_db)):
    return list_theater_service(db)

@theater_router.put("/{theater_id}")
def update_theater(theater_id: int, data: dict, db: Session = Depends(get_db)):
    return update_theater_service(theater_id, data, db)

@theater_router.delete("/{theater_id}")
def delete_theater(theater_id: int, db: Session = Depends(get_db)):
    delete_theater_service(theater_id, db)
    return {"message": "Theater deleted successfully"}
