## Database Migrations

Database migrations are a way to manage changes to the database schema over time. It allows you to keep track of changes to the database schema and apply them to the database in a controlled manner.

### 👉 Why Migrations?

- **Version Control**: Keep track of changes to the database schema.
- **Collaboration**: Share and apply changes across multiple environments.
- **Rollback**: Revert changes to the previous state.
- **Consistency**: Ensure that all environments have the same database schema.
- **Automation**: Automate the process of applying changes to the database.
- **Documentation**: Document changes to the database schema.
- **Testing**: Test changes before applying them to the production database.
- **Security**: Ensure that the database schema is secure and up-to-date.
- **Performance**: Optimize the database schema for better performance.
- **Data Integrity**: Maintain data integrity during schema changes.
- **Reproducibility**: Reproduce the database schema across different environments.
- **Scalability**: Scale the database schema as the application grows.
- **Maintenance**: Maintain the database schema over time.

## Alembic [🔗](https://alembic.sqlalchemy.org/)

Alembic is a lightweight database migration tool for SQLAlchemy. It provides a way to generate and apply schema migration scripts to an existing database.

### 👉 Installation

```bash
poetry add alembic
```

### 👉 Initialize Alembic

```bash
alembic init alembic
```

### 👉 Configuration

```python
# env.py
from app.models.database import SQLALCHEMY_DATABASE_URL, Base
from app.models.posts import Post

config.set_main_option('sqlalchemy.url', SQLALCHEMY_DATABASE_URL)

target_metadata = Base.metadata
```

### 👉 Generate Migration

```bash
alembic revision --autogenerate -m "create users table"
```

### 👉 Apply Migration

```bash
alembic upgrade head
```
