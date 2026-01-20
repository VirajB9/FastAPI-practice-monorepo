from sqlalchemy.orm import Session
from sql import crud
from sql.models import Order, Item



def get_items(db: Session):
    return crud.get_all_items(db)


def create_item(item_data: dict, db: Session):
    order_id = item_data["order_id"]
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        return {"Order not found"}

    if order.status != "open":
        return {"Cannot add item to closed order"}

    crud.create_item(item_data, db)
    return {"Item is created"}


def delete_item(item_id: int, db: Session):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        return {"Item not found"}

    if item.order.status == "closed":
        return {"Cannot delete item"}

    crud.delete_item(item, db)
    return {"Item is deleted"}
