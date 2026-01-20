from sql.database import Base
from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.orm import relationship


class Brand(Base):
    __tablename__ = "Brand"


    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    country = Column(String, nullable=False)
    rating = Column(Float, nullable=False)

    items = relationship("Item", back_populates="brands", cascade="all, delete-orphan")


class Item(Base):
    __tablename__ = "Item"


    id = Column(Integer, primary_key=True, nullable=True)
    name = Column(String, nullable=False)
    base_price = Column(Float, nullable=False)
    final_price = Column(Float, nullable=False)
    brand_name = Column(String, nullable=False)
    brand_rating = Column(Float, nullable=False)

    brand_id = Column(Integer, ForeignKey("Brand.id", ondelete="CASCADE"))

    brands = relationship("Brand", back_populates="items")
