# UDEMY - Python Django - The Practical Guide

- [Academind](https://academind.com/) - Maximilian Schwarzmüller
- [YouTube Course Link](https://www.youtube.com/playlist?list=PLBxwSeQlMDNiNt72UmSvKBLsxPgGY_Jy-)

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
# Install dependencies
uv sync

# Copy environment file and fill in values
cp .env.example .env
```

## Running the Development Server

```bash
uv run python manage.py runserver
```

## Other Commands

```bash
# Apply migrations
uv run python manage.py migrate

# Run tests
uv run python manage.py test

# Add a new dependency
uv add <package>
```
