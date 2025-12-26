from models.cart import Cart

class CartRepository:
    def __init__(self):
        self.carts = []

    def find_by_user_id(self, user_id: int) -> Cart:
        return next((cart for cart in self.carts if cart.user_id == user_id), None)

    def save(self, cart: Cart) -> None:
        self.carts.append(cart)

    def update(self, cart: Cart) -> None:
        index = next((i for i, c in enumerate(self.carts) if c.user_id == cart.user_id), None)
        if index is not None:
            self.carts[index] = cart
    
    def delete(self, cart: Cart) -> None:
        self.carts.remove(cart)