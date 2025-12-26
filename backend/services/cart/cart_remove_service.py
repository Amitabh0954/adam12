from repositories.cart.cart_repository import CartRepository
from repositories.products.product_repository import ProductRepository

class CartRemoveService:
    def __init__(self):
        self.cart_repository = CartRepository()
        self.product_repository = ProductRepository()

    def remove_from_cart(self, user_id: int, product_id: int):
        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            return {"message": "Cart not found", "status": 404}

        if not self.product_repository.find_by_id(product_id):
            return {"message": "Product not found", "status": 404}

        cart.items = [item for item in cart.items if item.product_id != product_id]
        self.cart_repository.save(cart)

        return {"message": "Product removed from cart successfully", "status": 200}