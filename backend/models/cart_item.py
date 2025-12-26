class CartItem:
    def __init__(self, id: int, user_id: int, product_id: int, quantity: int):
        self.id = id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity