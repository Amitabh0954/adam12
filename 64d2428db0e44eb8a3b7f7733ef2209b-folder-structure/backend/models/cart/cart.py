# Epic Title: Shopping Cart Functionality

class Cart:
    cart_id: int
    user_id: int
    is_guest: bool

    def __init__(self, cart_id: int, user_id: int = None, is_guest: bool = False):
        self.cart_id = cart_id
        self.user_id = user_id
        self.is_guest = is_guest