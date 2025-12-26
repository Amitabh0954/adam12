from repositories.cart.cart_repository import CartRepository
from repositories.products.product_repository import ProductRepository

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()
        self.product_repository = ProductRepository()

    def add_to_cart(self, user_id: int, product_id: int, quantity: int):
        if not self.product_repository.find_by_id(product_id):
            return {"message": "Product not found", "status": 404}

        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            cart = Cart(user_id)
            self.cart_repository.save(cart)
        
        cart.add_item(product_id, quantity)
        self.cart_repository.save(cart)

        return {"message": "Product added to cart successfully", "status": 200}

    def get_cart(self, user_id: int):
        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            return {"message": "Cart not found", "status": 404}

        return {"message": "Cart retrieved successfully", "status": 200, "cart": [item.__dict__ for item in cart.items]}