from fastapi import APIRouter
from .ControllerBase import ControllerBase
from src.view_model.request import UserRequestViewModel
from src.view_model.response import UserResponseViewModel


class UserController(ControllerBase):
    __URL = "/user"

    def __init__(self) -> None:
        self.router = APIRouter()
        self.create_routes()

    def create_routes(self):
        self.router.add_api_route(f"{self.__URL}/create/", self.create, methods=["POST"], name="Create User", response_model=UserResponseViewModel)
        

    def create(self, user: UserRequestViewModel) -> UserResponseViewModel:
        return user
