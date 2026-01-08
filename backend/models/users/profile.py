from pydantic import BaseModel, EmailStr, constr, Field

class ProfileUpdate(BaseModel):
    email: EmailStr
    password: Optional[constr(min_length=8)] = Field(None)
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)