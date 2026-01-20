from sqlalchemy.orm import Session
from sql.models import Event, Ticket


# CRUD of event

def get_events(db: Session):
    return db.query(Event).all()


def get_event_by_id(event_id: int, db: Session):
    return db.query(Event).filter(Event.id == event_id).first()


def create_event(event_data: dict, db: Session):
    event = Event(**event_data)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def delete_event(event_id: int, db: Session):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        return {"message": "Event not found"}

    db.delete(event)
    db.commit()
    return {"message": "Event deleted successfully"}


# CRUD of ticket

def get_tickets(db: Session):
    return db.query(Ticket).all()


def create_ticket(ticket_data: dict, db: Session):
    ticket = Ticket(**ticket_data)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def count_tickets_for_event(event_id: int, db: Session):
    return db.query(Ticket).filter(Ticket.event_id == event_id).count()
