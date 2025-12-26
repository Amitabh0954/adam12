from repositories.cart.cart_repository import CartRepository
from repositories.products.product_repository import ProductRepository
from models.cart import ShoppingCart

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()
        self.product_repository = ProductRepository()

    def add_to_cart(self, user_id: int, data: dict):
        if not user_id:
            return {"message": "User is not logged in", "status": 401}
        
        product_id = data.get('product_id')
        quantity = data.get('quantity')
        
        if not product_id or quantity <= 0:
            return {"message": "Invalid product data", "status": 400}
        
        product = self.product_repository.find_by_id(product_id)
        if not product:
            return {"message": "Product not found", "status": 404}

        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            cart = ShoppingCart(user_id)
        
        cart.add_item(product_id, quantity)
        self.cart_repository.save(cart)
        
        return {"message": "Product added to cart", "status": 200}

    def view_cart(self, user_id: int):
        if not user_id:
            return {"message": "User is not logged in", "status": 401}

        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            return {"message": "Cart is empty", "status": 200, "cart": []}

        cart_view = [{"product_id": item.product_id, "quantity": item.quantity, "added_at": item.added_at} for item in cart.items]
        return {"message": "Cart retrieved successfully", "status": 200, "cart": cart_view}

    def remove_from_cart(self, user_id: int, data: dict):
        if not user_id:
            return {"message": "User is not logged in", "status": 401}
        
        product_id = data.get('product_id')
        if not product_id:
            return {"message": "Invalid product id", "status": 400}
        
        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            return {"message": "Cart is empty", "status": 200}
        
        cart.remove_item(product_id)
        self.cart_repository.save(cart)
        
        total_price = cart.calculate_total()
        
        return {"message": "Item removed from cart", "status": 200, "total_price": total_price}

    def update_cart_item(self, user_id: int, data: dict):
        if not user_id:
            return {"message": "User is not logged in", "status": 401}
        
        product_id = data.get('product_id')
        quantity = data.get('quantity')
        
        if not product_id or quantity <= 0:
            return {"message": "Invalid quantity", "status": 400}

        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            return {"message": "Cart is empty", "status": 200}
        
        cart.update_quantity(product_id, quantity)
        self.cart_repository.save(cart)
        
        total_price = cart.calculate_total()
        
        return {"message": "Cart item quantity updated", "status": 200, "total_price": total_price}

    def save_cart(self, user_id: int):
        if not user_id:
            return {"message": "User is not logged in", "status": 401}

        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            return {"message": "No cart to save", "status": 200}

        self.cart_repository.save(cart)

        return {"message": "Cart saved successfully", "status": 200}