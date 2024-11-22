from datetime import datetime
from pydantic import BaseModel, EmailStr



class UserResponseViewModel(BaseModel):

    id: int
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
