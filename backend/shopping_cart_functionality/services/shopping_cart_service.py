from sqlalchemy.orm import Session
from backend.shopping_cart_functionality.models.shopping_cart import ShoppingCart
from backend.shopping_cart_functionality.models.shopping_cart_item import ShoppingCartItem
from backend.shopping_cart_functionality.schemas.shopping_cart_schema import ShoppingCartSchema, ShoppingCartItemSchema
from marshmallow import ValidationError

class ShoppingCartService:
    def __init__(self, session: Session):
        self.session = session

    def get_cart(self, user_id: int) -> ShoppingCart:
        cart = self.session.query(ShoppingCart).filter_by(user_id=user_id).first()
        if not cart:
            cart = ShoppingCart(user_id=user_id)
            self.session.add(cart)
            self.session.commit()
        return cart

    def add_item_to_cart(self, user_id: int, data: dict) -> ShoppingCart:
        cart = self.get_cart(user_id)
        try:
            item_data = ShoppingCartItemSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        item = self.session.query(ShoppingCartItem).filter_by(cart_id=cart.id, product_id=item_data['product_id']).first()
        if item:
            item.quantity += item_data['quantity']
        else:
            item = ShoppingCartItem(cart_id=cart.id, **item_data)
            self.session.add(item)

        self.session.commit()
        self.session.refresh(cart)
        return cart

    def remove_item_from_cart(self, user_id: int, product_id: int) -> ShoppingCart:
        cart = self.get_cart(user_id)
        item = self.session.query(ShoppingCartItem).filter_by(cart_id=cart.id, product_id=product_id).first()
        if not item:
            raise ValueError("Item not found in cart")

        self.session.delete(item)
        self.session.commit()
        self.session.refresh(cart)
        return cart

#### 2. Update ShoppingCartItem schema if necessary

#### 3. Implement remove item endpoint in the shopping cart controller