from sql.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)

    # One book can have multiple anime
    anime = relationship("Anime", back_populates="book", cascade="all, delete-orphan")


class Anime(Base):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    author = Column(String, nullable=True)
    genre = Column(String, nullable=True)
    studio = Column(String, nullable=True)
    imdb_rating = Column(Integer, nullable=True)
    episodes = Column(Integer, nullable=True)
    ongoing = Column(Boolean, default=True)

    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=True)

    # mapper to book
    book = relationship("Book", back_populates="anime")
