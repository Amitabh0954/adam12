# Epic Title: Product Catalog Management

class Category:
    category_id: int
    name: str
    parent_id: int

    def __init__(self, category_id: int, name: str, parent_id: int = None):
        self.category_id = category_id
        self.name = name
        self.parent_id = parent_id
    
    def update_category(self, name: str):
        self.name = name