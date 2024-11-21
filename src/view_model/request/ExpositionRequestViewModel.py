from .UserRequestViewModel import UserRequestViewModel
from pydantic import BaseModel


class ExpositionResponseViewModel(BaseModel):
    title: str
    description: str
    started_at: str
    finish_at: str
    user: UserRequestViewModel