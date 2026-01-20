from sqlalchemy.orm import Session
from sql.models import Warehouse, Package


# ---------- Warehouse CRUD ----------

def list_all_warehouses(db: Session):
    return db.query(Warehouse).all()


def get_warehouse_by_id(db: Session, warehouse_id: int):
    return db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()


def add_warehouse(db: Session, warehouse: Warehouse):
    db.add(warehouse)
    db.commit()
    db.refresh(warehouse)
    return warehouse


def delete_warehouse(db: Session, warehouse: Warehouse):
    db.delete(warehouse)
    db.commit()


# ---------- Package CRUD ----------

def list_all_packages(db: Session):
    return db.query(Package).all()


def get_package_by_id(db: Session, package_id: int):
    return db.query(Package).filter(Package.id == package_id).first()


def add_package(db: Session, package: Package):
    db.add(package)
    db.commit()
    db.refresh(package)
    return package


def delete_package(db: Session, package: Package):
    db.delete(package)
    db.commit()
