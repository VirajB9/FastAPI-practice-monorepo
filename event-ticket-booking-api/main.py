from fastapi import FastAPI
from sql.database import engine, Base
from routes.event_route import event_router
from routes.ticket_route import ticket_router

app = FastAPI(title="Event & Ticket Booking API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Welcome to the Event & Ticket Booking API. Visit /docs to explore!"}


app.include_router(event_router)
app.include_router(ticket_router)
