from repositories.auth.user_repository import UserRepository
from datetime import datetime

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def save_cart_state(self, user_id: int, cart_state: dict):
        user = self.user_repository.find_by_id(user_id)
        if not user:
            return {"message": "User not found", "status": 404}
            
        user.cart_state = cart_state
        user.updated_at = datetime.utcnow()
        self.user_repository.update(user)
        return {"message": "Cart state saved successfully", "status": 200}
    
    def retrieve_cart_state(self, user_id: int):
        user = self.user_repository.find_by_id(user_id)
        if not user:
            return {"message": "User not found", "status": 404}
            
        cart_state = user.cart_state
        return {"cart_state": cart_state, "status": 200}