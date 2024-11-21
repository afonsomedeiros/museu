from fastapi import FastAPI

from .controllers.User import UserController

def main():
    app = FastAPI()

    # configurations.
    include_routes(app)

    return app


def include_routes(app: FastAPI):
    controllers = [
        UserController()
    ]

    for controller in controllers:
        app.include_router(controller.router)




# @app.get("/")
# def read_root():
#     x = 2
#     y = 5
#     w = x**2 + y**3
#     return {"message": f"Olá mundo!, {w}"}


# @app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserRequestViewModel)
# def create_user(user: UserRequestViewModel) -> UserRequestViewModel:
#     return user

# Running.

app = main()