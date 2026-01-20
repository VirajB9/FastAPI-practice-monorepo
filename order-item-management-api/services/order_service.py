from sqlalchemy.orm import Session
from sql import crud
from sql.models import Order


def get_all_orders(db: Session):
    return crud.list_all(db)


def create_order(order_data: dict, db: Session):
    return crud.create_order(order_data, db)


def update_close_order(order_id: int, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        return {"Not Found"}

    if order.status != "closed":
        order.status = "closed"
        db.commit()
    return {"Order is closed"}


def delete_order(order_id: int, db: Session):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        return {"Order not found"}

    crud.delete_order(db, order)
    return {"Order is deleted"}
