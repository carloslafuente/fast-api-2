# Python
from typing import List
# FastAPI
from fastapi import FastAPI, status
# Models
from models.tweet import Tweet


class TweetController():
    def __init__(self, app: FastAPI) -> None:
        self.app = app

    def set_controllers(self):
        @self.app.get(
            "/tweet",
            response_model=List,
            status_code=status.HTTP_200_OK,
            summary="Get all tweets",
            tags=["Tweet"]
        )
        def get_tweets():
            pass

        @self.app.get(
            "/tweet/{tweet_id}",
            response_model=Tweet,
            status_code=status.HTTP_200_OK,
            summary="Get a specific tweet by id",
            tags=["Tweet"]
        )
        def get_tweet_by_id():
            pass

        @self.app.post(
            "/tweet",
            response_model=Tweet,
            status_code=status.HTTP_201_CREATED,
            summary="Create new tweet",
            tags=["Tweet"]
        )
        def create_tweet():
            pass

        @self.app.delete(
            "/tweet/{tweet_id}",
            response_model=Tweet,
            status_code=status.HTTP_200_OK,
            summary="Delete an existent tweet by id",
            tags=["Tweet"]
        )
        def delete_tweet():
            pass

        @self.app.put(
            "/tweet/{tweet_id}",
            response_model=Tweet,
            status_code=status.HTTP_200_OK,
            summary="Update an existent tweet by i",
            tags=["Tweet"]
        )
        def update_tweet():
            pass
