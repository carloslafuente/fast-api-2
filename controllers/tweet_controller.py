# Python
import json
from typing import List
# FastAPI
from fastapi import FastAPI, status, Body
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
            """
            Show all tweets.

            Show all tweets in the app.

            Returns a json with the basic Tweet information.
                - id: UUID
                - content: str
                - creation_date: date
                - update_date: date
                - user: User
            """
            path = 'C:\\Users\\BAIRESDEV\\Documents\\Platzi\\practices\\fast-api-avanzado\\project\\data\\tweets.json'
            with open(path, "r", encoding="utf-8") as f:
                tweets = json.load(f)

            return tweets

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
        def create_tweet(tweet: Tweet = Body(...)):
            """
            Create a tweet.

            Create a tweet in the app.

            Parameters:
                - content: Tweet content

            Returns a json with the basic Tweet information.
                - id: UUID
                - content: str
                - creation_date: date
                - update_date: date
                - user: User
            """
            path = 'C:\\Users\\BAIRESDEV\\Documents\\Platzi\\practices\\fast-api-avanzado\\project\\data\\tweets.json'
            tweet_dict = tweet.dict()
            with open(path, "r+", encoding="utf-8") as f:
                tweets = json.load(f)
                tweet_dict["id"] = str(tweet_dict["id"])
                tweet_dict["creation_date"] = str(tweet_dict["creation_date"])
                tweet_dict["update_date"] = str(tweet_dict["update_date"])

                user_dict = tweet_dict["user"]
                user_dict["id"] = str(user_dict["id"])
                user_dict["birth_date"] = str(user_dict["birth_date"])
                tweet_dict["user"] = user_dict

                tweets.append(tweet_dict)
                f.seek(0)
                f.write(json.dumps(tweets))

            return tweet_dict

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
