from sqlalchemy.orm import Session
from sql.models import Brand, Item
from fastapi import HTTPException
from sql import crud
from services.item_service import calculate_final_price

def list_brands(db: Session):
    return crud.list_all_brand(db)


def create_brand(brand_data: dict, db: Session):
    rating = brand_data["rating"]
    if not 1.0 < rating <= 5.0:
        raise HTTPException(status_code=400, detail="Rating must be between 1.0 to 5.0")
    brand = crud.add_brand(brand_data, db)
    return brand


def update_brand(brand_id: int, brand_data: dict, db: Session):
    brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")

    if "rating" in brand_data:
        if not 1.0 < brand_data["rating"] <= 5.0:
            raise HTTPException(status_code=400, detail="Rating must be between 1.0 to 5.0")

    for key, value in brand_data.items():
        setattr(brand, key, value)

    for item in brand.items:
        item.brand_name = brand.name
        item.brand_rating = brand.rating
        item.final_price = calculate_final_price(item.base_price, brand.rating)

    crud.update_brand(brand, db)
    return brand


def delete_brand(brand_id: int, db: Session):
    crud.delete_brand(brand_id, db)
    return True 