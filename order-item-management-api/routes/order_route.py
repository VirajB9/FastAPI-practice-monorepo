from fastapi import APIRouter, Depends
from sql.database import get_db
from services.order_service import get_all_orders, create_order, update_close_order, delete_order


order_router = APIRouter(prefix="/order", tags=["Order"])

@order_router.get("", summary="Get all orders")
def all_orders(db= Depends(get_db)):
	return get_all_orders(db)


@order_router.post("", summary="Create a new order")
def make_order(order_data:dict, db= Depends(get_db)):
	return create_order(order_data, db)


@order_router.patch("/{order_id}/close", summary="Close an order")
def update_order(order_id:int, db= Depends(get_db)):
	return update_close_order(order_id, db)


@order_router.delete("/{order_id}", summary="Delete an order")
def remove_order(order_id:int, db= Depends(get_db)):
	return delete_order(order_id, db)