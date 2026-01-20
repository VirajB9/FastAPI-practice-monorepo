from sql.db import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    city = Column(String, nullable=False)
    handling_fee = Column(Float, nullable=False)

    packages = relationship(
        "Package",
        back_populates="warehouse",
        cascade="all, delete-orphan"
    )


class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    shipping_cost = Column(Float, nullable=False)

    warehouse_id = Column(
        Integer,
        ForeignKey("warehouses.id", ondelete="CASCADE"),
        nullable=False
    )

    warehouse_name = Column(String, nullable=False)
    handling_fee = Column(Float, nullable=False)

    warehouse = relationship("Warehouse", back_populates="packages")
