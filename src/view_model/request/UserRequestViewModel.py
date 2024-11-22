from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserRequestViewModel(BaseModel):
    name: str
    email: EmailStr
    password: str
