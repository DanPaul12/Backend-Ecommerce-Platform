from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from typing import List
from models.orderProduct import order_product
#from models.product import Product

class Order(Base):
    __tablename__ = "Orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime.date] = mapped_column(db.Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('Customers.id'))
    customer: Mapped["Customer"] = db.relationship(back_populates='orders')
    products: Mapped[List['Product']] = db.relationship(secondary=order_product)

