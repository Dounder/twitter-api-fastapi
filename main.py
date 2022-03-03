from fastapi import FastAPI

app = FastAPI()


@app.get(path='/', tags=['home'])
def home():
    return {'Twitter API': 'Working!'}
