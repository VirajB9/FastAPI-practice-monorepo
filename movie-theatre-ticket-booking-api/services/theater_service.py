from fastapi import HTTPException
from sqlalchemy.orm import Session
from sql.models import Theater
from sql import crud


def calculate_final_price(base_price: float, seat_type: str, premium_charge: float) -> float:
    if seat_type == "normal":
        multiplier = 1.0
    elif seat_type == "premium":
        multiplier = 1.5
    else:
        multiplier = 1.0

    seat_price = base_price * multiplier
    premium_amount = seat_price * (premium_charge / 100)
    return seat_price + premium_amount

def list_theater_service(db: Session):
    return crud.list_all_theaters(db)

def create_theater_service(data: dict, db: Session):
    fee = data["premium_charge"]
    if fee < 0 or fee > 30:
        raise HTTPException(status_code=400, detail="Premium charge must be between 0 and 30")

    theater = Theater(
        name=data["name"],
        city=data["city"],
        premium_charge=fee
    )
    return crud.add_theater(theater, db)

def update_theater_service(theater_id: int, data: dict, db: Session):
    theater = crud.get_theater_by_id(theater_id, db)
    if not theater:
        raise HTTPException(status_code=404, detail="Theater not found")

    if "premium_charge" in data:
        fee = data["premium_charge"]
        if fee < 0 or fee > 30:
            raise HTTPException(status_code=400, detail="Premium charge must be between 0 and 30")

    for field in ["name", "city", "premium_charge"]:
        if field in data:
            setattr(theater, field, data[field])

    for ticket in theater.tickets:
        ticket.theater_name = theater.name
        ticket.premium_charge = theater.premium_charge
        ticket.final_price = calculate_final_price(ticket.base_price, ticket.seat_type, theater.premium_charge)

    db.commit()
    db.refresh(theater)
    return theater

def delete_theater_service(theater_id: int, db: Session):
    theater = crud.get_theater_by_id(theater_id, db)
    if not theater:
        raise HTTPException(status_code=404, detail="Theater not found")

    crud.delete_theater(theater, db) 
