from sql.database import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Theater(Base):
    __tablename__= "theaters"
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String, unique= True, nullable=False)
    city= Column(String,  nullable=False)
    premium_charge= Column(Float,  nullable=False)

    tickets= relationship("Ticket", back_populates="theater", cascade="all, delete-orphan")

class Ticket(Base):
    __tablename__= "tickets"
    id= Column(Integer, primary_key=True, index=True)
    movie_name= Column(String, nullable=False)
    seat_type= Column(String, nullable=False)
    base_price= Column(Float,  nullable=False)
    final_price= Column(Float,  nullable=False)

    theater_id= Column(Integer, ForeignKey("theaters.id", ondelete="CASCADE"), nullable=False)

    theater_name= Column(String, nullable=False)
    premium_charge= Column(Float, nullable=False)

    theater= relationship("Theater", back_populates="tickets")
