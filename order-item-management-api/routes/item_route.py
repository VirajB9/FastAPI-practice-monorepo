from fastapi import APIRouter, Depends
from sql.database import get_db
from services.item_service import get_items, create_item, delete_item

item_router = APIRouter(prefix="/item", tags=["Item"])


@item_router.get("", summary="Get all items")
def list_items(db=Depends(get_db)):
    return get_items(db)


@item_router.post("", summary="Create a new item")
def make_item(item_data: dict, db=Depends(get_db)):
    return create_item(item_data, db)


@item_router.delete("/{item_id}", summary="Delete an item")
def remove_item(item_id: int, db=Depends(get_db)):
    return delete_item(item_id, db)
