from typing import Optional
from pydantic import BaseModel, EmailStr, constr

class User(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    password: constr(min_length=8)