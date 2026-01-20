from fastapi import APIRouter, Depends
from sql.database import get_db
from services import item_service


item_router= APIRouter(prefix="/item", tags=["Items"])

@item_router.post("", summary="")
def create_item(item_data:dict, db=Depends(get_db)):
	return 	item_service.create_item(item_data, db)


@item_router.get("", summary="")
def list_items(db=Depends(get_db)):
	return item_service.list_items(db)


@item_router.put("", summary="")
def update_item(item_id:int, item_data:dict, db=Depends(get_db)):
	return item_service.update_item(item_id, item_data, db)


@item_router.delete("", summary="")
def delete_item(item_id:int, db=Depends(get_db)):
	return item_service.delete_item(item_id, db)