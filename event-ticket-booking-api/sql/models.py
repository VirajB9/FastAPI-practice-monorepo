from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sql.database import Base


class Event(Base):
    __tablename__ = "event"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    max_seats = Column(Integer, nullable=False)

    ticket = relationship("Ticket", back_populates="event", cascade="all, delete-orphan")


class Ticket(Base):
    __tablename__ = "ticket"
    id = Column(Integer, primary_key=True)
    attendee_name = Column(String, nullable=False)
    event_id = Column(Integer, ForeignKey("event.id", ondelete="CASCADE"), nullable=False)

    event = relationship("Event", back_populates="ticket")
