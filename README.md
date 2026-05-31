# UDEMY - Python Django - The Practical Guide

- [Academind](https://academind.com/) - Maximilian Schwarzmüller
- [YouTube Course Link](https://www.youtube.com/playlist?list=PLBxwSeQlMDNiNt72UmSvKBLsxPgGY_Jy-)

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- [Django](https://www.djangoproject.com/)
- [MySQL](https://www.mysql.com/)
- [MySQL Connector/Python](https://dev.mysql.com/downloads/connector/python/)
- [Connector/Python Django Back End - MySQL Documentation](https://dev.mysql.com/doc/connector-python/en/connector-python-django-backend.html)
- [Django Database Configuration - Django Documentation](https://docs.djangoproject.com/en/6.0/ref/databases/)
- [How to Integrate MySQL Database with Django - GeeksforGeeks](https://www.geeksforgeeks.org/python/how-to-integrate-mysql-database-with-django/)

## Setup Project

```bash
# Install dependencies
uv sync

# Add a new dependency
uv add <package_name>

# Copy environment file and fill in values(Windows)
Copy-Item .env.example .env

# Copy environment file and fill in values(Linux)
cp .env.example .env

# Copy environment file and fill in values(MacOS)
cp .env.example .env
```

## Running the Development Server

```bash
uv run python manage.py runserver
```

## Database

```bash
# Apply migrations
uv run python manage.py migrate
```

## MySQL with dotenv (Best Practice)

Use dotenv variables to switch between SQLite and MySQL.

- Local learning/dev: keep `DB_ENGINE=sqlite3`
- MySQL: set `DB_ENGINE=mysql` and provide MySQL credentials in `.env`

```python
import os
from typing import Any

# settings.py
DB_ENGINE = os.environ.get('DB_ENGINE', 'sqlite3').lower()

if DB_ENGINE == 'mysql':
    DATABASES: dict[str, dict[str, Any]] = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
            'PORT': os.environ.get('DB_PORT', '3306'),
            'OPTIONS': {'charset': 'utf8mb4'},
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

```bash
# Install recommended MySQL driver for Django
uv add mysqlclient

# If mysqlclient build fails on your OS, use:
# uv add mysql-connector-python

# Then run migrations
uv run python manage.py migrate
```

## Testing the Application

```bash
# Run tests
uv run python manage.py test
```

## Quality Checks

```bash
# Run Ruff linter
uv run ruff check
```

```bash
# Run Ruff formatter
uv run ruff format
```

```bash
uv run pyright
```
