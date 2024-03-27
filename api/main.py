from fastapi import FastAPI

from routers.posts import router as posts_router

# Define an API object
app = FastAPI()

app.include_router(posts_router)

# Map a HTTP GET request to the root URL to a function
@app.get('/')
def read_root():
    """Given a list of integers, return the sum of all even numbers in the list."""

    return {'Hello': 'World'}
