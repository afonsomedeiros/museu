from .ExpositionRequestViewModel import ExpositionResponseViewModel
from pydantic import BaseModel


class PieceRequestViewModel(BaseModel):
    title: str
    description: str
    exposition: ExpositionResponseViewModel