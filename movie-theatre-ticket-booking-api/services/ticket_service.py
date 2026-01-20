from fastapi import HTTPException
from sqlalchemy.orm import Session
from sql.models import Ticket
from sql import crud
from services.theater_service import calculate_final_price

def list_ticket_service(db: Session):
    return crud.list_all_tickets(db)

def create_ticket_service(data: dict, db: Session):
    if data["base_price"] <= 0:
        raise HTTPException(status_code=400, detail="Base price must be greater than 0")

    if data["seat_type"] not in ["normal", "premium"]:
        raise HTTPException(status_code=400, detail="Seat type must be 'normal' or 'premium'")

    theater = crud.get_theater_by_id(data["theater_id"], db)
    if not theater:
        raise HTTPException(status_code=404, detail="Theater not found")

    final_price = calculate_final_price(data["base_price"], data["seat_type"], theater.premium_charge)

    ticket = Ticket(
        movie_name=data["movie_name"],
        seat_type=data["seat_type"],
        base_price=data["base_price"],
        final_price=final_price,
        theater_id=theater.id,
        theater_name=theater.name,
        premium_charge=theater.premium_charge
    )

    return crud.add_ticket(ticket, db)

def update_ticket_service(ticket_id: int, data:dict, db: Session):
    ticket = crud.get_ticket_by_id(ticket_id, db)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    if "base_price" in data:
        if data["base_price"] <= 0:
            raise HTTPException(status_code=400, detail="Base price must be greater than 0")
        ticket.base_price = data["base_price"]

    if "seat_type" in data:
        if data["seat_type"] not in ["normal", "premium"]:
            raise HTTPException(status_code=400, detail="Seat type must be 'normal' or 'premium'")
        ticket.seat_type = data["seat_type"]

    ticket.final_price = calculate_final_price(ticket.base_price, ticket.seat_type, ticket.premium_charge)

    if "movie_name" in data:
        ticket.movie_name = data["movie_name"]

    db.commit()
    db.refresh(ticket)
    return ticket

def delete_ticket_service(ticket_id: int, db: Session):
    ticket = crud.get_ticket_by_id(ticket_id, db)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    crud.delete_ticket(ticket, db)
