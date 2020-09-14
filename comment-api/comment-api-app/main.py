import os
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_root():
    body = os.environ.get('COMMENT_BODY')

    return {
        'title': 'My Comment',
        'body': body,
    }
