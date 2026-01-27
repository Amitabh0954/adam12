# Epic Title: Product Catalog Management

class ProductCategory:
    product_id: int
    category_id: int

    def __init__(self, product_id: int, category_id: int):
        self.product_id = product_id
        self.category_id = category_id