from fastapi import FastAPI
from routes.order_route import order_router
from routes.item_route import item_router
from sql.database import Base, engine




app = FastAPI(title="Order & Item Management API")


Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Welcome to the Order & Item Management API. Visit /docs to explore!"}

app.include_router(order_router)
app.include_router(item_router)