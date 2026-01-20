from sqlalchemy.orm import Session
from sql.models import Theater, Ticket


# ---------- Theater CRUD ----------

def list_all_theaters(db: Session):
    return db.query(Theater).all()

def get_theater_by_id(theater_id: int, db: Session):
    return db.query(Theater).filter(Theater.id == theater_id).first()

def add_theater(theater: Theater, db: Session):
    db.add(theater)
    db.commit()
    db.refresh(theater)
    return theater

def delete_theater(theater: Theater, db: Session):
    db.delete(theater)
    db.commit()


# ---------- Ticket CRUD ----------

def list_all_tickets(db: Session):
    return db.query(Ticket).all()

def get_ticket_by_id(ticket_id: int, db: Session):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def add_ticket(ticket: Ticket, db: Session):
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def delete_ticket(ticket: Ticket, db: Session):
    db.delete(ticket)
    db.commit()
