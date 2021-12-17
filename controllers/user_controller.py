# Python
from typing import List
# FastAPI
from fastapi import FastAPI, status
# Models
from models.user import User


class UserController():
    def __init__(self, app: FastAPI) -> None:
        self.app = app

    def set_controllers(self):
        @self.app.post(
            "/user",
            response_model=User,
            status_code=status.HTTP_201_CREATED,
            summary="Create new user",
            tags=["User"]
        )
        def create_user():
            pass

        @self.app.post(
            "/login",
            response_model=User,
            status_code=status.HTTP_200_OK,
            summary="Log in an existent user",
            tags=["User"]
        )
        def login():
            pass

        @self.app.get(
            "/users",
            response_model=List,
            status_code=status.HTTP_200_OK,
            summary="Get all users",
            tags=["User"]
        )
        def get_users():
            pass

        @self.app.get(
            "/users/{user_id}",
            response_model=User,
            status_code=status.HTTP_200_OK,
            summary="Get a specific user by id",
            tags=["User"]
        )
        def get_user_by_id():
            pass

        @self.app.delete(
            "/users/{user_id}",
            response_model=User,
            status_code=status.HTTP_200_OK,
            summary="Delete a specific user by id",
            tags=["User"]
        )
        def delete_user_by_id():
            pass

        @self.app.put(
            "/users/{user_id}",
            response_model=User,
            status_code=status.HTTP_200_OK,
            summary="Update a specific user by id",
            tags=["User"]
        )
        def update_user_by_id():
            pass
