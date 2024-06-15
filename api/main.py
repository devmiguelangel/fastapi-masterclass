from fastapi import FastAPI

from api.routers import auth, posts, users

app = FastAPI()

API_VERSION = '/api/v1'

app.include_router(auth.router, prefix=API_VERSION)
app.include_router(users.router, prefix=API_VERSION)
app.include_router(posts.router, prefix=API_VERSION)

@app.get('/')
def root():
    return {'Hello': 'World'}
