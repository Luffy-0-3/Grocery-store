from sqlalchemy import Column,String,Integer,Float
from db import Base

class Grocery(Base):
    __tablename__ = "groceries"
    
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    description = Column(String,nullable=False)
    price = Column(Float,nullable=False)
    quantity = Column(Integer,nullable=False)