# FastAPI
from fastapi import FastAPI

# Models

app = FastAPI()


@app.get(path='/', tags=['home'])
def home():
    return {'Twitter API': 'Working!'}
