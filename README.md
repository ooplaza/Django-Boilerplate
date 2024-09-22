# Django JWT Authentication with HttpOnly Cookies

This project is a Django application that implements JWT authentication using HttpOnly cookies for secure token management. It provides endpoints for user registration, login, logout, and token refreshing.

## Features

- User registration with email and password.
- Login and logout functionality.
- JWT tokens issued as HttpOnly cookies for enhanced security.
- Token refresh mechanism.
- User model customization.

## Technologies Used

- Django
- Django REST Framework
- Django REST Auth
- Simple JWT
- PostgreSQL (or any other database you choose)
- Boto3 (for S3 storage, if used)

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later
- PostgreSQL or preferred database

### Steps to Install

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ooplaza/Django-Boilerplate.git

   ```

2. **Create a virtual environment::**

   ```bash
   cd Django-Boilerplate
   python -m virtualenv <env-name>
   source <env-name>/bin/activate  # On Windows use `<env-name>\Scripts\activate`

   ```

3. **Set up environment variables: Create a .env file in the root directory and add your configuration:**

   ```bash
    DEBUG=True
    ENGINE=django.db.backends.postgresql
    NAME=your_db_name
    USER=your_db_user
    PASSWORD=your_db_password
    HOST=localhost
    PORT=5432

   ```

4. **Run migration:**

   ```bash
   python manage.py migrate

   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
