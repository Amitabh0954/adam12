class Category:
    def __init__(self, name: str, parent_id: int = None):
        self.id = None  # This should be set by the repository when saved
        self.name = name
        self.parent_id = parent_id