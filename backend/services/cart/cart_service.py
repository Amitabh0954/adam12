from repositories.cart.cart_repository import CartRepository
from repositories.products.product_repository import ProductRepository
from models.cart import Cart

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()
        self.product_repository = ProductRepository()
    
    def add_to_cart(self, data: dict):
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        
        if not user_id or not product_id:
            return {"message": "User ID and Product ID are required", "status": 400}
        
        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            cart = Cart(user_id=user_id)
            self.cart_repository.save(cart)
        
        product = self.product_repository.find_by_id(product_id)
        if not product:
            return {"message": "Product not found", "status": 404}

        cart.add_item(product)
        self.cart_repository.update(cart)
        
        return {"message": "Product added to cart", "total_price": cart.total_price, "status": 200}
    
    def view_cart(self, user_id: int):
        cart = self.cart_repository.find_by_user_id(user_id