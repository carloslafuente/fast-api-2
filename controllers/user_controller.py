# Python
from typing import List
import json
# FastAPI
from fastapi import FastAPI, status, Body
# Models
from models.user import User, UserSignup


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
        def sign_up(user: UserSignup = Body(...)):
            """
            Sign Up an user.

            Register an user in the app.

            Parameters:
                - user: UserSignup

            Returns a json with the basic User information.
                - id: UUID
                - email: EmailStr
                - names: str
                - lastname: str
                - birth_date: date
            """
            path = 'C:\\Users\\BAIRESDEV\\Documents\\Platzi\\practices\\fast-api-avanzado\\project\\data\\users.json'
            user_dict = user.dict()
            with open(path, "r+", encoding="utf-8") as f:
                users = json.load(f)
                user_dict["id"] = str(user_dict["id"])
                user_dict["birth_date"] = str(user_dict["birth_date"])
                users.append(user_dict)
                f.seek(0)
                f.write(json.dumps(users))

            return user_dict

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
            response_model=List[User],
            status_code=status.HTTP_200_OK,
            summary="Get all users",
            tags=["User"]
        )
        def get_users():
            """
            Show all users.

            Show all users in the app.

            Returns a json with the basic User information.
                - id: UUID
                - email: EmailStr
                - names: str
                - lastname: str
                - birth_date: date
            """
            path = 'C:\\Users\\BAIRESDEV\\Documents\\Platzi\\practices\\fast-api-avanzado\\project\\data\\users.json'
            with open(path, "r", encoding="utf-8") as f:
                users = json.load(f)
                
            return users

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
