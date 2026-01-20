from sqlalchemy.orm import Session
from sql.models import Brand, Item
from fastapi import HTTPException
from sql import crud


def calculate_final_price(base_price: float, rating: float):
    if rating < 3.0:
        return base_price * 0.9
    if rating > 4.5:
        return base_price * 1.1
    return base_price


def list_items(db: Session):
    return crud.list_all_item(db)


def create_item(item_data: dict, db: Session):
    if item_data["base_price"] <= 0:
        raise HTTPException(status_code=400, detail= "Base price must be positive")

    brand = db.query(Brand).filter(Brand.id == item_data["brand_id"]).first()
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")

    final_price = calculate_final_price(item_data["base_price"], brand.rating)

    item = Item(
        name=item_data["name"],
        base_price=item_data["base_price"],
        final_price=final_price,
        brand_id=brand.id,
        brand_name=brand.name,
        brand_rating=brand.rating)

    crud.add_item(item, db)
    return item


def update_item(item_id: int, item_data: dict, db: Session):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if "base_price" in item_data:
        if item_data["base_price"] < 0:
            raise HTTPException(status_code=400, detail="Base price must be positive")

        item.base_price = item_data["base_price"]
        item.final_price = calculate_final_price(item.base_price, item.brand_rating)

    if "name" in item_data:
        item.name = item_data["name"]

    crud.update_item(item, db)
    return item


def delete_item(item_id: int, db: Session):
    crud.delete_item(item_id, db)
    return True