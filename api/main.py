from fastapi import FastAPI

# Define an API object
app = FastAPI()

# Map a HTTP GET request to the root URL to a function
@app.get('/')
def read_root():
    """Given a list of integers, return the sum of all even numbers in the list."""

    return {'Hello': 'World'}
