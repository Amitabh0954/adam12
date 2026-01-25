from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    category = relationship('Category', backref='products')

#### 3. Create `CategorySchema`