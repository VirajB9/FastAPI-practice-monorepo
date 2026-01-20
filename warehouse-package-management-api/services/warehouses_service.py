from fastapi import HTTPException
from sqlalchemy.orm import Session
from sql.models import Warehouse
from sql import crud


def calculate_shipping_cost(weight: float, handling_fee: float) -> float:
    base_cost = weight * 50
    return base_cost + (base_cost * (handling_fee / 100))


def list_warehouses_service(db: Session):
    return crud.list_all_warehouses(db)


def create_warehouse_service(data: dict, db: Session):
    fee = data["handling_fee"]
    if fee < 0 or fee > 20:
        raise HTTPException(
            status_code=400,
            detail="Handling fee must be between 0 and 20"
        )

    warehouse = Warehouse(
        name=data["name"],
        city=data["city"],
        handling_fee=fee
    )

    return crud.add_warehouse(db, warehouse)


def update_warehouse_service(warehouse_id: int, data: dict, db: Session):
    warehouse = crud.get_warehouse_by_id(db, warehouse_id)
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")

    if "handling_fee" in data:
        fee = data["handling_fee"]
        if fee < 0 or fee > 20:
            raise HTTPException(
                status_code=400,
                detail="Handling fee must be between 0 and 20"
            )

    for field in ["name", "city", "handling_fee"]:
        if field in data:
            setattr(warehouse, field, data[field])

    # Sync denormalized package data
    for package in warehouse.packages:
        package.warehouse_name = warehouse.name
        package.handling_fee = warehouse.handling_fee
        package.shipping_cost = calculate_shipping_cost(
            package.weight,
            warehouse.handling_fee
        )

    db.commit()
    db.refresh(warehouse)
    return warehouse


def delete_warehouse_service(warehouse_id: int, db: Session):
    warehouse = crud.get_warehouse_by_id(db, warehouse_id)
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")

    crud.delete_warehouse(db, warehouse)
