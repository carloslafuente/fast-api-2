# FastAPI
from fastapi import FastAPI
# Controllers
from controllers.user_controller import UserController
from controllers.tweet_controller import TweetController


app = FastAPI()


# Path Operations


# Users


UserController(app).set_controllers()


# Tweets


TweetController(app).set_controllers()
