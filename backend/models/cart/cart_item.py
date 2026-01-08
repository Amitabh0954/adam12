from pydantic import BaseModel, conint
from backend.models.products.product import Product

class CartItem(BaseModel):
    product: Product
    quantity: conint(gt=0)