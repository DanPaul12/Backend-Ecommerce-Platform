from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
#from models.customer import Customer
#from models.role import Role

class CustomerAccount(Base):
    __tablename__ = 'Customer_Accounts'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('Customers.id', ondelete='CASCADE'))

    #role: Mapped[int] = mapped_column(db.ForeignKey('Customer_Management_Roles.id'))

    
    customer: Mapped['Customer'] = db.relationship(back_populates='customer_account', lazy='noload')
    roles: Mapped[List['Role']] = db.relationship(secondary='Customer_Management_Roles')
    

    #what is back_populates and how does it relate to foreign key