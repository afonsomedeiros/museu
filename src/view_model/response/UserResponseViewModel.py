from pydantic import BaseModel, EmailStr

from src.view_model.request import UserRequestViewModel


class UserResponseViewModel(BaseModel):

    id: int
    name: str
    email: EmailStr
    created_at: str
    updated_at: str

    # def __init__(self, user: UserRequestViewModel):
    #     self.id = user.id
    #     self.name = user.name
    #     self.email = user.email
    #     self.created_at = user.created_at
    #     self.updated_at = user.updated_at


    
