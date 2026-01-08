from typing import Optional
from pydantic import BaseModel, constr, condecimal

class Product(BaseModel):
    id: Optional[int] = None
    name: constr(min_length=1)
    description: constr(min_length=1)
    price: condecimal(gt=0)