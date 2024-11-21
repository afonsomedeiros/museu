from .ExpositionResponseViewModel import ExpositionResponseViewModel
from pydantic import BaseModel


class PieceResponseViewModel(BaseModel):
    title: str
    description: str
    exposition: ExpositionResponseViewModel