from fastapi import FastAPI
from sql.database import Base, engine  # <-- important
from routes.book_route import book_router
from routes.anime_route import anime_router

app = FastAPI(title="Book & Anime Management API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Welcome to the Book & Anime Management API. Visit /docs to explore!"}


# Register routes
app.include_router(book_router)
app.include_router(anime_router)
