from fastapi import FastAPI

# Define an API object
app = FastAPI()

# Map a HTTP GET request to the root URL to a function
@app.get('/')
def read_root():
    """Given a list of integers, return the sum of all even numbers in the list."""

    return {'Hello': 'World'}


@app.get('/posts')
async def get_posts():
    return [{'id': 1, 'title': 'First Post'}, {'id': 2, 'title': 'Second Post'}]


@app.post('/posts')
async def create_posts():
    return {'message': 'Post created'}
