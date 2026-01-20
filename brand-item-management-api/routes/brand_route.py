from fastapi import APIRouter, Depends
from sql.database import get_db
from services import brand_service


brand_router= APIRouter(prefix="/brand", tags=["Brands"])

@brand_router.post("", summary="")
def create_brand(brand_data:dict, db=Depends(get_db)):
	return 	brand_service.create_brand(brand_data, db)


@brand_router.get("", summary="")
def list_brands(db=Depends(get_db)):
	return brand_service.list_brands(db)


@brand_router.put("", summary="")
def update_brand(brand_id:int, brand_data: dict, db=Depends(get_db)):
	return brand_service.update_brand(brand_id, brand_data, db)


@brand_router.delete("", summary="")
def delete_item(brand_id:int, db=Depends(get_db)):
	return brand_service.delete_brand(brand_id, db)