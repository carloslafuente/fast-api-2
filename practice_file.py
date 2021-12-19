# Python
from typing import Optional
from datetime import datetime
from enum import Enum

# Pydantinc
from pydantic import BaseModel, Field, EmailStr

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path, Form, Header, Cookie, File, UploadFile
from fastapi import status
from fastapi import HTTPException


app = FastAPI()

# Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"


class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=100
        )
    state: str = Field(
        ...,
        min_length=1,
        max_length=100
        )
    country: str = Field(
        ...,
        min_length=1,
        max_length=100
        )


class BaseUser(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    age: int = Field(
        ...,
        gt=0,
        le=120
        )
    birthday: datetime
    hair_color: Optional[HairColor] = Field(
            default=None
        )
    is_married: Optional[bool] = Field(
        default=None,
        )
    email: EmailStr = Field(
        ...,
        )


class User(BaseUser):
    password: str = Field(
        ...,
        min_length=8
        )

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Carlos",
                "last_name": "La Fuente",
                "age": 25,
                "birthday": datetime.now(),
                "hair_color": HairColor.blonde,
                "is_married": False,
                "email": "user@example.com",
                "password": "P@$$w0rd"
            }
        }


class UserResponse(BaseUser):
    pass


class BaseLogin(BaseModel):
    username: str = Field(..., max_length=20)


class UserLogin(BaseLogin):
    password: str = Field(...)


class LoginResponse(BaseLogin):
    pass

# Controllers - Path Operations

@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return { "data": "Hello World!" }


@app.post("/user", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["User"], summary="Create new user in the APP")
def create_user(user: User = Body(...)):
    """
    Create new user in the APP
    
    This path operation creates a new user in the app and saves the information in the database
    
    Parameters:
    - Request body parameters:
        - **user: User** -> A user model with first nme, last name, age, hair color and marital status.
    
    Returns an user model with with first nme, last name, age, hair color and marital status.
    """
    return user


@app.get("/user/detail", status_code=status.HTTP_200_OK, tags=["User"], deprecated=True)
def get_user_detail(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="User name",
        description="This is the user name. It's between 1 and 50 characters.",
        example="Carlos"
        ), 
    age: int = Query(
        ..., 
        title="User age", 
        description="This is the user age. It's a required query parameter.",
        example=25
        )
    ):
    return { 
        "name": name, 
        "age": age 
    }


users = [1, 2, 3, 4, 5]

@app.get("/user/detail/{user_id}", status_code=status.HTTP_200_OK, tags=["User"])
def get_user_detail(
    user_id: int = Path(
        ..., 
        gt=0,
        title="User ID",
        description="This is the user ID. It's greater than 0.",
        example=123
        )
    ):
    if user_id not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user you are looking for does not exist."
        )
    return { 
        "name": "Carlos", 
        "age": 25, 
        "id": user_id 
    }


@app.put("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["User"])
def update_user(
        user_id: int = Path(
        ..., 
        gt=0,
        title="User ID",
        description="This is the user ID. It's greater than 0.",
        example=123
        ),
        user: User = Body(...),
        location: Location = Body(...)
    ):
    return user


@app.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK, tags=["Login"])
def login(username: str = Form(..., example="carlosrlfs"), password: str = Form(...)):
    user = UserLogin(username=username, password=password)
    return LoginResponse(username=user.username)


@app.post("/contact", status_code=status.HTTP_200_OK, tags=["Contact"])
def contact(
    first_name: str = Form(..., max_length=20, min_length=1),
    last_name: str = Form(..., max_length=20, min_length=1),
    email: EmailStr = Form(...),
    message: str = Form(..., min_length=20),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
    ):
    return { 
        "user_agent": user_agent,
        "ads": ads
    }


@app.post("/post-image", tags=["Posts"])
def post_image(
    image: UploadFile = File(...)
    ):
    return {
        "filename": image.filename,
        "format": image.content_type,
        "size(kb)": round(len(image.file.read()) / 1024, ndigits=2)
    }