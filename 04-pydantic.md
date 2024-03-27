## FastAPI Models and Pydantic

### 👉 How to use Pydantic models [🔗](https://docs.pydantic.dev/latest/)
Pydantic models are used to define the structure of incoming and outgoing data in FastAPI. By creating a Pydantic model, you can specify the expected data types and constraints for request bodies, query parameters, and response payloads. FastAPI automatically validates incoming data against the defined model, ensuring that the data is correct and properly formatted.

### 👉 Defining a Pydantic model [🔗](https://fastapi.tiangolo.com/tutorial/body/)
To define a Pydantic model, you need to create a class that inherits from `pydantic.BaseModel`. Inside the class, you can define attributes that represent the fields of the model. Each attribute should specify the data type and any constraints that apply to the field.

```python
from typing import Optional

from pydantic import BaseModel


class PostSchema(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
```

### 👉 Data validation and serialization techniques [🔗](https://docs.pydantic.dev/latest/concepts/serialization/)
Serialization in FastAPI is primarily handled by Pydantic models. These models define the shape and types of data your API will accept and return. By default, Pydantic uses standard Python data types for serialization, but sometimes you might have more complex requirements.
