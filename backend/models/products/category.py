from pydantic import BaseModel, constr
from typing import Optional, List

class Category(BaseModel):
    id: Optional[int] = None
    name: constr(min_length=1)
    parent_id: Optional[int] = None

class ProductCategory(BaseModel):
    product_id: int
    category_id: int