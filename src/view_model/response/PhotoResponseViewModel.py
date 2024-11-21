from .PieceResponseViewModel import PieceResponseViewModel
from pydantic import BaseModel


class PhotoResponseViewModel(BaseModel):
    description: str
    captured_at: str
    author_name: str # Who shot the photo.
    piece: PieceResponseViewModel