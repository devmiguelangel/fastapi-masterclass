from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import auth, posts, users, votes

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

API_VERSION = '/api/v1'

app.include_router(auth.router, prefix=API_VERSION)
app.include_router(users.router, prefix=API_VERSION)
app.include_router(posts.router, prefix=API_VERSION)
app.include_router(votes.router, prefix=API_VERSION)

@app.get('/')
def root():
    return {'Hello': 'World'}
