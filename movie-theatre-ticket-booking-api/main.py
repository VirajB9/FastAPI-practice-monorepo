from fastapi import FastAPI
from sql.database import Base, engine
from routes.theater_route import theater_router
from routes.ticket_route import ticket_router
app = FastAPI(title= "Theater and Ticket Management API")

Base.metadata.create_all(engine)

@app.get("/")
def home():
    return {"message": "Welcome to the Theater and Ticket Management API. Visit /docs to explore!"}

app.include_router(theater_router)
app.include_router(ticket_router)