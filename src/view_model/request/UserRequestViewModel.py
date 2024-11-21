from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserRequestViewModel(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    created_at: datetime
    updated_at: datetime
