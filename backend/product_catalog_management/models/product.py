from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=False)

#### 2. Implement a service to handle the logic for adding new products

##### ProductService