from repositories.cart.cart_repository import CartRepository
from models.cart import Cart

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()

    def add_to_cart(self, user_id: int, product_id: int, quantity: int):
        if quantity <= 0:
            return {"message": "Quantity must be a positive number", "status": 400}
        
        cart_item = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
        self.cart_repository.save(cart_item)
        return {"message": "Product added to cart successfully", "status": 201}

    def get_cart(self, user_id: int):
        cart_items = self.cart_repository.find_by_user_id(user_id)
        total_price = sum(item.quantity * item.product.price for item in cart_items)  # assumes product has a price attribute
        return {
            "message": "Cart retrieved successfully",
            "status": 200,
            "cart": [{"user_id": item.user_id, "product_id": item.product_id, "quantity": item.quantity} for item in cart_items],
            "total_price": total_price
        }

    def remove_from_cart(self, user_id: int, product_id: int):
        self.cart_repository.remove_item(user_id, product_id)
        return {"message": "Product removed from cart successfully", "status": 200}