from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sql.database import get_db
from services.ticket_service import (
    create_ticket_service,
    list_ticket_service,
    update_ticket_service,
    delete_ticket_service,
)

ticket_router= APIRouter(prefix="/tickets", tags=["Tickets"])

@ticket_router.post("/")
def create_ticket(data: dict, db: Session = Depends(get_db)):
    return create_ticket_service(data, db)


@ticket_router.get("/")
def list_tickets(db: Session = Depends(get_db)):
    return list_ticket_service(db)


@ticket_router.put("/{ticket_id}")
def update_ticket(ticket_id: int, data: dict, db: Session = Depends(get_db)):
    return update_ticket_service(ticket_id, data, db)


@ticket_router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    delete_ticket_service(ticket_id, db)
    return {"message": "Ticket deleted successfully"}
