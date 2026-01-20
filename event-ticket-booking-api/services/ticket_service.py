from fastapi import HTTPException
from sql import crud
from sqlalchemy.orm import Session


def list_ticket(db: Session):
    return crud.get_tickets(db)


def create_ticket(ticket_data: dict, db: Session):
    event = crud.get_event_by_id(ticket_data.get("event_id"), db)

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    if event.category != "public":
        raise HTTPException(status_code=400, detail="Tickets can only be created for public events")

    book_seats = crud.count_tickets_for_event(event.id, db)
    if book_seats >= event.max_seats:
        raise HTTPException(status_code=400, detail="No seats available")

    return crud.create_ticket(ticket_data, db)
