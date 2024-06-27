## Testing

Testing is an essential part of software development. It helps to ensure that the application works as expected and that new changes do not break existing functionality. In this chapter, we will explore how to write tests for FastAPI applications.

### Pytest 👉 [🔗](https://docs.pytest.org)

To get started with testing, you need to install `pytest`

```bash
poetry add pytest
```

Let's create a simple FastAPI application and write tests for it. Create a new file called `main.py` and add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_root():
    return {"Hello": "World"}
```

Next, create a new file called `test_main.py` and add the following code:

```python
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

To run the tests, use the following command:

```bash
pytest -v
```

**Most common options**

- `-v` for verbose output
- `--disable-warnings` to disable warnings
- `-x` to stop after first failure
- `--pdb` to enter debugger on failure
- `--lf` to run only the tests that failed last time
- `--ff` to run only the tests that failed last time first
- `--maxfail=2` to stop after 2 failures
- `--durations=3` to show the 3 slowest tests
- `--cov=app` to check test coverage
- `--cov-report=term-missing` to show missing lines in coverage report
- `--cov-report=html` to generate HTML coverage report
- `-s` to print output to console
- `-k test_read_root` to run only tests that match the given substring
- `-m "not slow"` to skip tests marked as slow

**Parameterized Tests**

```python
import pytest

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

**Fixtures**

```python
import pytest

@pytest.fixture
def data():
    return {"name": "Alice", "age": 30}

def test_data(data):
    assert data["name"] == "Alice"
    assert data["age"] == 30
```

### Testing Basics [🔗](https://fastapi.tiangolo.com/tutorial/testing/)

Testing in FastAPI is similar to testing in other Python web frameworks. You can use the built-in `unittest` module or third-party libraries like `pytest`. In this chapter, we will use `pytest` for writing tests.

**TestClient**

FastAPI provides a `TestClient` class that you can use to test your application. It simulates requests to your FastAPI application and allows you to test the responses.

https://requests.readthedocs.io/en/latest/

```python

**Setup**

```bash
poetry add httpx
```

**Example**

```python
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

```bash
# run tests verbose
pytest -v
# disable warnings
pytest -v --disable-warnings
# stop after first failure
pytest -v --disable-warnings -x

```

- **Fixture scope**

Fixtures can have different scopes:

- `function`: The default scope. The fixture is destroyed at the end of the test.
- `class`: The fixture is destroyed at the end of the test class.
- `module`: The fixture is destroyed at the end of the test module.
- `package`: The fixture is destroyed at the end of the test package.
- `session`: The fixture is destroyed at the end of the test session.

```python
import pytest

@pytest.fixture(scope="module")
def data():
    return {"name": "Alice", "age": 30}

def test_data(data):
    assert data["name"] == "Alice"
    assert data["age"] == 30
```
