from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShoppingCart(Base):
    __tablename__ = 'shopping_carts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    session_id = Column(String(255), nullable=True)

    items = relationship('ShoppingCartItem', back_populates='cart')

class ShoppingCartItem(Base):
    __tablename__ = 'shopping_cart_items'

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('shopping_carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    cart = relationship('ShoppingCart', back_populates='items')
    product = relationship('Product')

#### 2. Implement services to handle adding and managing items in the shopping cart

##### ShoppingCartService