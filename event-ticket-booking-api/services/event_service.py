from fastapi import HTTPException
from sql import crud
from sqlalchemy.orm import Session


def list_event(db: Session):
    return crud.get_events(db)


def create_event(event_data: dict, db: Session):
    return crud.create_event(event_data, db)


def delete_event(event_id: int, db: Session):
    event = crud.get_event_by_id(event_id, db)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    crud.delete_event(event_id, db)
    return {"message": "Event deleted successfully"}
