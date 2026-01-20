from fastapi import HTTPException
from sqlalchemy.orm import Session
from sql.models import Package
from sql import crud
from services.warehouses_service import calculate_shipping_cost


def list_packages_service(db: Session):
    return crud.list_all_packages(db)


def create_package_service(data: dict, db: Session):
    if data["weight"] <= 0:
        raise HTTPException(
            status_code=400,
            detail="Weight must be greater than 0"
        )

    warehouse = crud.get_warehouse_by_id(db, data["warehouse_id"])
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")

    shipping_cost = calculate_shipping_cost(
        data["weight"],
        warehouse.handling_fee
    )

    package = Package(
        description=data["description"],
        weight=data["weight"],
        shipping_cost=shipping_cost,
        warehouse_id=warehouse.id,
        warehouse_name=warehouse.name,
        handling_fee=warehouse.handling_fee
    )

    return crud.add_package(db, package)


def update_package_service(package_id: int, data: dict, db: Session):
    package = crud.get_package_by_id(db, package_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")

    if "weight" in data:
        if data["weight"] <= 0:
            raise HTTPException(
                status_code=400,
                detail="Weight must be greater than 0"
            )

        package.weight = data["weight"]
        package.shipping_cost = calculate_shipping_cost(
            package.weight,
            package.handling_fee
        )

    if "description" in data:
        package.description = data["description"]

    db.commit()
    db.refresh(package)
    return package


def delete_package_service(package_id: int, db: Session):
    package = crud.get_package_by_id(db, package_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")

    crud.delete_package(db, package)
