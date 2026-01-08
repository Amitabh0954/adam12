from pydantic import BaseModel, constr, condecimal, Field

class ProductUpdate(BaseModel):
    name: Optional[constr(min_length=1)] = Field(None)
    description: constr(min_length=1)
    price: Optional[condecimal(gt=0)] = Field(None)