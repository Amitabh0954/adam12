from sqlalchemy.orm import Session
from backend.shopping_cart_functionality.models.shopping_cart import ShoppingCart, ShoppingCartItem
from backend.product_catalog_management.models.product import Product
from typing import Dict

class ShoppingCartService:
    def __init__(self, session: Session):
        self.session = session

    def create_or_get_cart(self, user_id: int = None, session_id: str = None) -> ShoppingCart:
        if user_id:
            cart = self.session.query(ShoppingCart).filter_by(user_id=user_id).first()
        else:
            cart = self.session.query(ShoppingCart).filter_by(session_id=session_id).first()

        if not cart:
            cart = ShoppingCart(user_id=user_id, session_id=session_id)
            self.session.add(cart)
            self.session.commit()

        return cart

    def add_product_to_cart(self, cart: ShoppingCart, product_id: int, quantity: int) -> ShoppingCartItem:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        
        product = self.session.query(Product).get(product_id)
        if not product:
            raise ValueError("Product not found")

        cart_item = self.session.query(ShoppingCartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = ShoppingCartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
            self.session.add(cart_item)

        self.session.commit()
        return cart_item

    def modify_product_quantity(self, cart: ShoppingCart, product_id: int, quantity: int) -> ShoppingCartItem:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        
        cart_item = self.session.query(ShoppingCartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if not cart_item:
            raise ValueError("Product not found in cart")

        cart_item.quantity = quantity
        self.session.commit()
        return cart_item

    def remove_product_from_cart(self, cart: ShoppingCart, product_id: int) -> None:
        cart_item = self.session.query(ShoppingCartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if not cart_item:
            raise ValueError("Product not found in cart")

        self.session.delete(cart_item)
        self.session.commit()

    def get_cart_items(self, cart: ShoppingCart) -> Dict:
        items = self.session.query(ShoppingCartItem).filter_by(cart_id=cart.id).all()
        total_price = sum(item.product.price * item.quantity for item in items)
        return {
            "cart_id": cart.id,
            "items": [{"product_id": item.product_id, "quantity": item.quantity, "price": item.product.price} for item in items],
            "total_price": total_price
        }

#### 2. Implement a controller to expose the API for modifying quantities in the shopping cart

##### ShoppingCartController