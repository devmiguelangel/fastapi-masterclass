## Authentication

Authentication is the process of verifying the identity of a user. It is a common requirement for most web applications. FastAPI provides a simple way to implement authentication using OAuth2.

### 👉 Password Hashing [🔗](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#password-hashing)

Storing passwords in plain text is a security risk. FastAPI provides a simple way to hash passwords using the `bcrypt` library.

```bash
poetry add "passlib[bcrypt]"
```

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
```

### JWT [🔗](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#handle-jwt-tokens)

JSON Web Token (JWT) is an open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed.

![JWT](./images/jwt.png)

```bash
poetry add "python-jose[cryptography]"

openssl rand -hex 32
3c76b72f80f4f9378910ca5b644c68afe3ef4ad74077352ab3709136f5bcbfe9
```

```python
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

SECRET_KEY
ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
```

### 👉 OAuth2 [🔗](https://oauth.net/2/)

OAuth2 is an authorization framework that enables a third-party application to obtain limited access to an HTTP service, either on behalf of a resource owner or by allowing the third-party application to obtain access on its own behalf.

### 👉 OAuth2 Flows

- **Authorization Code**: Used by web applications.
- **Implicit**: Used by mobile apps.
- **Password**: Used by trusted applications.
- **Client Credentials**: Used by confidential clients.
- **Device Code**: Used by devices that have limited input capabilities.

- **JWT Bearer Token**: Used to access resources.
- **Refresh Token**: Used to obtain a new access token.

## Authorization

Authorization is the process of determining whether a user has permission to perform a specific action. FastAPI provides a simple way to implement authorization using OAuth2.

### 👉 OAuth2 Scopes

Scopes are used to limit the access of an access token. They are strings that represent a specific permission. For example, `read:users` or `write:users`.

### 👉 Resources

[Routers in FastAPI](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
[SQLALchemy Relationship](https://docs.sqlalchemy.org/en/20/orm/relationships.html)
[Settings and Environment Variables](https://fastapi.tiangolo.com/advanced/settings/)
