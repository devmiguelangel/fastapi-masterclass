## Dive into FastAPI

### 👉 Handling HTTP Requests
FastAPI simplifies the process of handling HTTP requests by allowing you to define Python functions known as request handlers. These functions are executed when a client sends an HTTP request that matches the specified HTTP method and path. FastAPI automatically manages incoming requests and passes the relevant data to the corresponding request handler function.

### 👉 Request Parameters and Query Parameters
Request parameters and query parameters are crucial for extracting data from incoming requests. Request parameters are part of the URL path, while query parameters are specified in the URL query string. FastAPI makes it effortless to work with both types of parameters.

### 👉 Request Parameters [🔗](https://fastapi.tiangolo.com/tutorial/path-params/)
Request parameters are included in the URL path by enclosing them in curly braces. FastAPI parses the values from the URL and passes them to the request handler function automatically.

### 👉 Query Parameters[🔗](https://fastapi.tiangolo.com/tutorial/query-params/)
Query parameters are typically used to filter or provide additional information to a request. To access query parameters, you can define additional parameters in your request handler function with default values.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

### 🔗 Resources
- [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [Request body](https://fastapi.tiangolo.com/tutorial/body/)
