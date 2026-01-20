from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sql.db import get_db
from services.packages_service import (
    create_package_service,
    list_packages_service,
    update_package_service,
    delete_package_service
)

package_router = APIRouter(prefix="/packages", tags=["Packages"])


@package_router.post("/")
def create_package(data: dict, db: Session = Depends(get_db)):
    return create_package_service(data, db)


@package_router.get("/")
def list_packages(db: Session = Depends(get_db)):
    return list_packages_service(db)


@package_router.put("/{package_id}")
def update_package(package_id: int, data: dict, db: Session = Depends(get_db)):
    return update_package_service(package_id, data, db)


@package_router.delete("/{package_id}")
def delete_package(package_id: int, db: Session = Depends(get_db)):
    delete_package_service(package_id, db)
    return {"message": "Package deleted successfully"}
