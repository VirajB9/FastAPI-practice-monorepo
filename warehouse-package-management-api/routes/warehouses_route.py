from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sql.db import get_db
from services.warehouses_service import (
    create_warehouse_service,
    list_warehouses_service,
    update_warehouse_service,
    delete_warehouse_service
)

warehouse_router = APIRouter(prefix="/warehouses", tags=["Warehouses"])


@warehouse_router.post("/")
def create_warehouse(data: dict, db: Session = Depends(get_db)):
    return create_warehouse_service(data, db)


@warehouse_router.get("/")
def list_warehouses(db: Session = Depends(get_db)):
    return list_warehouses_service(db)


@warehouse_router.put("/{warehouse_id}")
def update_warehouse(warehouse_id: int, data: dict, db: Session = Depends(get_db)):
    return update_warehouse_service(warehouse_id, data, db)


@warehouse_router.delete("/{warehouse_id}")
def delete_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    delete_warehouse_service(warehouse_id, db)
    return {"message": "Warehouse deleted successfully"}
