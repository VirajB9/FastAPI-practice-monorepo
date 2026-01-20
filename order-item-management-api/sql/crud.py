from sqlalchemy.orm import Session
from sql.models import Order, Item


#CRUD of order

def list_all(db: Session):
    return db.query(Order).all()


def create_order(order_data:dict, db: Session):
    order = Order(**order_data)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def update_order(order_id: int, db: Session):
    return db.query(Order).filter(Order.id == order_id).first()


def delete_order(db: Session, order):
    db.delete(order)
    db.commit()



#CRUD of item

def get_all_items(db: Session):
    return db.query(Item).all()


def create_item(item_data: dict, db: Session):
    item = Item(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def delete_item(item_id: int, db: Session):
    db.delete(item_id)
    db.commit()

