from sql.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, nullable=False)
    customer_name = Column(String, nullable=False)
    status = Column(String, nullable=False)

    items = relationship("Item", back_populates = "order", cascade = "all, delete-orphan")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, nullable=False)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    order = relationship("Order", back_populates = "items")
