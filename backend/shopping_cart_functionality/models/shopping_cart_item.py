from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShoppingCartItem(Base):
    __tablename__ = 'shopping_cart_item'

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('shopping_cart.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    cart = relationship('ShoppingCart', back_populates='items')
    product = relationship('Product')

#### 2. Creating schemas for managing shopping carts

##### ShoppingCart Schema