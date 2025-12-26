from repositories.auth.user_repository import UserRepository
from repositories.cart.cart_repository import CartRepository

class CartSaveService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.cart_repository = CartRepository()

    def save_cart(self, user_id: int):
        user = self.user_repository.find_by_id(user_id)
        if not user:
            return {"message": "User not found", "status": 404}

        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            return {"message": "Cart not found", "status": 404}

        user.cart = cart
        self.user_repository.save(user)
        return {"message": "Cart saved successfully", "status": 200}

    def retrieve_cart(self, user_id: int):
        user = self.user_repository.find_by_id(user_id)
        if not user or not user.cart:
            return {"message": "No saved cart found", "status": 404}

        return {"message": "Cart retrieved successfully", "status": 200, "cart": [item.__dict__ for item in user.cart.items]}