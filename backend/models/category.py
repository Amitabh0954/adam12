class Category:
    def __init__(self, id: int, name: str, description: str = '', parent_id: int = None):
        self.id = id
        self.name = name
        self.description = description
        self.parent_id = parent_id