from repositories.cart.cart_repository import CartRepository
from models.cart_item import CartItem

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()

    def add_to_cart(self, user_id: int, product_id: int, quantity: int):
        if not user_id or not product_id or quantity <= 0:
            return {"message": "Invalid cart details", "status": 400}

        cart_item = self.cart_repository.find_by_user_and_product(user_id, product_id)
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(id=None, user_id=user_id, product_id=product_id, quantity=quantity)
        
        self.cart_repository.save(cart_item)
        return {"message": "Product added to cart", "status": 201, "cart_item": {"id": cart_item.id, "user_id": cart_item.user_id, "product_id": cart_item.product_id, "quantity": cart_item.quantity}}

    def get_cart(self, user_id: int):
        cart_items = self.cart_repository.find_all_by_user(user_id)
        return {"cart_items": [{"id": item.id, "user_id": item.user_id, "product_id": item.product_id, "quantity": item.quantity} for item in cart_items], "status": 200}