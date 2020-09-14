import os
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_root():
    body = os.environ.get('ARTICLE_BODY')

    return {
        'title': 'My Article',
        'body': body,
    }
