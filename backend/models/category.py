from datetime import datetime

class Category:
    def __init__(self, name: str, parent_id: int = None):
        self.name = name
        self.parent_id = parent_id
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()