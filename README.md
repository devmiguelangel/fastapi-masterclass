## FastAPI masterclass

This repository contains the code and notes for the FastAPI course.

> #### If you find this resource useful, support it by giving it a "★ Star" in the repository. Thank you!

## Summary
### Introduction and Basics
- [x] [Introduction to FastAPI](./docs/01-introduction.md)
- Overview of FastAPI
- Installation and project setup
- Creating your first FastAPI application

- [x] [Managing Dependencies with Poetry and API Testing with Ruff](./docs/02-poetry-ruff.md)
- Introduction to Poetry
- Managing Project Dependencies with Poetry
- Creating a FastAPI Project with Poetry
- Introduction to API Testing with Ruff
- Writing API Tests with Ruff

### Dive into FastAPI
- [x] [Request and Response Handling](./docs/03-request-handling.md)
- Dive into handling HTTP requests and responses in FastAPI
- Handling different types of requests (GET, POST, PUT, DELETE)
- Path parameters, query parameters, and request bodies
- JSON and form data
- Dependency injection and its use in FastAPI

- [ ] [Exception Handling and Custom Responses](#)
- Handling errors and exceptions
- Customizing response formats
- Exception handling best practices

- [x] [FastAPI Models and Pydantic](./docs/04-pydantic.md)
- Understand how to use Pydantic models in FastAPI applications.
- Validate and parse incoming request data with Pydantic models.
- Explore data validation and serialization techniques.

### Database Integration
- [x] [SQLAlchemy Integration](./docs/05-sqlalchemy.md)
- Integrating SQLAlchemy with FastAPI
- CRUD operations with SQLAlchemy models
- Handling database sessions and transactions

- [ ] [MongoDB Integration](#)
- Working with MongoDB in FastAPI
- CRUD operations with Pydantic and MongoDB models
- Asynchronous database operations

- [x] [Database Migrations and Alembic](./docs/06-migrations.md)
- Managing database migrations with Alembic
- Applying schema changes and versioning
- Automating database migration workflows

### Intermediate FastAPI Concepts
- [x] [Authentication and Authorization](./docs/07-auth.md)
Introduction to authentication in FastAPI
OAuth2, JWT, and API key authentication
Role-based authorization and permissions
Secure your endpoints with authorization checks.
External authentication with services like Google, GitHub, etc.

- [ ] [Background Tasks and Periodic Jobs](#)
Implementing background tasks in FastAPI
Scheduling periodic jobs with FastAPI
Using libraries like Celery for asynchronous tasks

- [ ] [File Uploads and Static Files](#)
Handling file uploads in FastAPI
Serving static files and assets
Working with FormData and file uploads

### Advanced FastAPI Topics
- [ ] [WebSocket Support](#)
Introduction to WebSocket in FastAPI
Create WebSocket endpoints and handle real-time communication
Implement WebSocket authentication and security.
Broadcasting messages with WebSocket

- [ ] [Custom Middleware and Extensions](#)
Implementing custom middleware in FastAPI
Logging, monitoring, and request/response manipulation with middleware
Applying middleware to specific routes or globally
Creating custom extensions and plugins
Integrating with third-party middleware

- [ ] [Rate Limiting and Security](#)
Implementing rate limiting to prevent abuse
Protecting against common security threats (SQL injection, XSS, CSRF)
Using security headers for enhanced security

- [ ] [Caching and Performance Optimization](#)
Caching strategies in FastAPI
Adding caching to FastAPI applications
Performance optimization techniques
Profiling and debugging FastAPI applications

### Optimization and Deployment
- [x] [Testing and Documentation](./docs/08-testing.md)
Learn the basics of testing FastAPI applications.
Writing unit tests for FastAPI applications
Using pytest for testing FastAPI endpoints
Test client for simulating HTTP requests
Generating API documentation using Swagger and ReDoc
Best practices for testing and documentation
Strategies for API versioning
Handling backward and forward compatibility
Versioning best practices in FastAPI

- [ ] Performance Optimization
Identifying performance bottlenecks in FastAPI applications
Techniques for optimizing database queries
Caching and lazy loading for improved performance

- [ ] Docker and Containerization
Containerize your FastAPI application using Docker
Deploy your containerized FastAPI app locally

- [ ] Deployment to Production
Explore deployment options for FastAPI applications
Deploy your FastAPI application to a cloud platform (e.g., AWS, Heroku)
Configure production-ready settings and optimizations
Scaling FastAPI applications horizontally

- [x] [Continuous Integration and Deployment (CI/CD)](./docs/09-ci-cd.md)
Setting up CI/CD pipelines for FastAPI projects
Automated testing and deployment with tools like GitHub Actions or GitLab CI
Deploying FastAPI applications to cloud platforms (AWS, Azure, GCP)

- [ ] Monitoring and Logging
Implementing logging in FastAPI applications
Integrating with logging services like ELK stack or Splunk
Monitoring application health and performance metrics

- [ ] API Security Best Practices
Securing FastAPI applications against common vulnerabilities
Rate limiting and throttling strategies
Implementing HTTPS and CORS correctly

