from sqlalchemy.orm import Session
from sql.models import Brand, Item


# CRUD for Brands

def add_brand(brand_data: dict, db: Session):
    brand = Brand(**brand_data)
    db.add(brand)
    db.commit()
    db.refresh(brand)
    return brand


def list_all_brand(db: Session):
    return db.query(Brand).all()


def update_brand(brand_data: Brand, db: Session):
    db.commit()
    return True


def delete_brand(brand_id: int, db: Session):
    brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if not brand:
        return {"message": "Brand not found"}
    db.delete(brand)
    db.commit()
    return {"message": "Brand is deleted"}


# CRUD for Items

def add_item(item_data: Item, db: Session):
    db.add(item_data)
    db.commit()
    db.refresh(item_data)
    return item_data


def list_all_item(db: Session):
    return db.query(Item).all()


def update_item(item_data: Item, db: Session):
    db.commit()
    return True


def delete_item(item_id: int, db: Session):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        return {"message": "Item not found"}
    db.delete(item)
    db.commit()
    return {"message": "Item is deleted"}


