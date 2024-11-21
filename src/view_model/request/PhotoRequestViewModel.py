from .PieceRequestViewModel import PieceRequestViewModel
from pydantic import BaseModel


class PhotoRequestViewModel(BaseModel):
    description: str
    captured_at: str
    author_name: str # Who shot the photo.
    piece: PieceRequestViewModel