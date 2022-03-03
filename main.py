# Python
import json
from typing import List
# FastAPI
from fastapi import Body, FastAPI, status
# Models
from models.user import User
from models.tweet import Tweet

app = FastAPI()

# * Path Operations
# ? Users


@app.post(
    path='/auth/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude=['password'],
    summary='Register a new user in the app',
    tags=['users']
)
def signup(user: User = Body(...)):

    with open('users.json', 'r+', encoding='utf-8') as f:
        users = json.load(f)
        user_dict = user.dict()
        user_dict['user_id'] = str(user_dict['user_id']),
        user_dict['birth_date'] = str(user_dict['birth_date'])
        user_dict['password'] = str(user_dict['password'])
        users.append(user_dict)
        f.seek(0)
        json.dump(users, f)
        
    return user


@app.post(
    path='/auth/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    response_model_exclude=['password'],
    summary='Login a user in the app',
    tags=['users']
)
def login():
    pass


@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    response_model_exclude=['password'],
    summary='Get all users',
    tags=['users']
)
def get_users():
    pass


@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    response_model_exclude=['password'],
    summary='Get a specific user',
    tags=['users']
)
def get_user():
    pass


@app.put(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    response_model_exclude=['password'],
    summary='Update a specific user',
    tags=['users']
)
def update_user():
    pass


@app.delete(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    response_model_exclude=['password'],
    summary='Delete a specific user',
    tags=['users']
)
def delete_user():
    pass

# ? Tweets


@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Get all tweets',
    tags=['Tweets']
)
def get_tweets():
    pass


@app.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Get a specific tweet',
    tags=['Tweets']
)
def get_tweet():
    pass


@app.post(
    path='/tweet',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Create a tweet',
    tags=['Tweets']
)
def create_tweet():
    pass


@app.put(
    path='/tweet/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a tweet',
    tags=['Tweets']
)
def update_tweet():
    pass


@app.delete(
    path='/tweet/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a tweet',
    tags=['Tweets']
)
def delete_tweet():
    pass
