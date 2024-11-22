from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select

from .ControllerBase import ControllerBase
from src.view_model.request import UserRequestViewModel
from src.view_model.response import UserResponseViewModel
from src.database import get_session
from src.models.User import Users


class UserController(ControllerBase):
    __URL = "/user"

    def __init__(self) -> None:
        self.router = APIRouter()
        self.create_routes()

    def create_routes(self):
        self.router.add_api_route(f"{self.__URL}/create/", self.create, methods=["POST"], name="Create User", response_model=UserResponseViewModel)
        

    def create(self, userRequest: UserRequestViewModel, session = Depends(get_session)) -> UserResponseViewModel:
        user = session.scalar(
            select(Users).where(
                (Users.email == userRequest.email)
            )
        )

        if user:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="E-mail already exists.")
        
        user = Users(**dict(userRequest))
        session.add(user)
        session.commit()
        return UserResponseViewModel(id=user.id, name=user.name, email=user.email, created_at=user.created_at, updated_at=user.updated_at)
