from fastapi import APIRouter, Depends
from sql.database import get_db
from services.ticket_service import list_ticket, create_ticket

ticket_router = APIRouter(prefix="/tickets", tags=["Tickets"])


@ticket_router.get("", summary="Get all tickets")
def get_all_ticket(db=Depends(get_db)):
    return list_ticket(db)


@ticket_router.post("", summary="Create a ticket for a public event")
def make_ticket(ticket_data: dict, db=Depends(get_db)):
    return create_ticket(ticket_data, db)
