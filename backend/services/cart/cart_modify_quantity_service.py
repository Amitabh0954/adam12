from repositories.cart.cart_repository import CartRepository
from repositories.products.product_repository import ProductRepository

class CartModifyQuantityService:
    def __init__(self):
        self.cart_repository = CartRepository()
        self.product_repository = ProductRepository()

    def modify_quantity(self, user_id: int, product_id: int, quantity: int):
        if quantity <= 0:
            return {"message": "Quantity must be a positive integer", "status": 400}

        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            return {"message": "Cart not found", "status": 404}

        if not self.product_repository.find_by_id(product_id):
            return {"message": "Product not found", "status": 404}

        for item in cart.items:
            if item.product_id == product_id:
                item.quantity = quantity
                self.cart_repository.save(cart)
                return {"message": "Quantity modified successfully", "status": 200}
        
        return {"message": "Product not found in cart", "status": 404}