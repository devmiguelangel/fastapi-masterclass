from fastapi import FastAPI

from api.routers import posts

app = FastAPI()

app.include_router(posts.router, prefix='/api/v1')

@app.get('/')
def root():
    return {'Hello': 'World'}
