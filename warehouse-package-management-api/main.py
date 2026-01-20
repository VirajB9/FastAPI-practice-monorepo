from fastapi import FastAPI
from sql.db import Base, engine
from routes.packages_route import package_router
from routes.warehouses_route import warehouse_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Warehouse & Package Management API")

@app.get("/")
def home():
    return {"message": "Welcome to the Warehouse & Package Management API. Visit /docs to explore!"}

app.include_router(warehouse_router)
app.include_router(package_router)

