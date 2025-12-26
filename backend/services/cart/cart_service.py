from repositories.cart.cart_repository import CartRepository
from models.cart import Cart

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()
    
    def add_to_cart(self, data: dict):
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        
        if not user_id or not product_id:
            return {"message": "User ID and Product ID are required", "status": 400}
        
        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            cart = Cart(user_id=user_id)
            self.cart_repository.save(cart)
        
        cart.add_item(product_id)
        self.cart_repository.update(cart)
        
        return {"message": "Product added to cart", "status": 200}
    
    def view_cart(self, user_id: int):
        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            return {"message": "Cart not found", "status": 404}
        
        return {"cart": cart.items, "status": 200}
    
    def remove_from_cart(self, user_id: int, product_id: int):
        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            return {"message": "Cart not found", "status": 404}
        
        cart.remove_item(product_id)
        self.cart_repository.update(cart)
        
        return {"message": "Product