from fastapi import APIRouter, Depends
from sql.database import get_db
from services.event_service import list_event, create_event, delete_event

event_router = APIRouter(prefix="/events", tags=["Events"])


@event_router.get("", summary="Get all events")
def all_events(db=Depends(get_db)):
    return list_event(db)


@event_router.post("", summary="Create a new event")
def make_event(event_data: dict, db=Depends(get_db)):
    return create_event(event_data, db)


@event_router.delete("/{event_id}", summary="Delete an event and its tickets")
def remove_event(event_id: int, db=Depends(get_db)):
    return delete_event(event_id, db)
