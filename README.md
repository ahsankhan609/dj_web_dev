# UDEMY - Python Django - The Practical Guide

- [Academind](https://academind.com/) - Maximilian Schwarzmüller
- [YouTube Course Link](https://www.youtube.com/playlist?list=PLBxwSeQlMDNiNt72UmSvKBLsxPgGY_Jy-)

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

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
uv run py manage.py runserver
```

## Database

```bash
# Apply migrations
uv run py manage.py migrate
```

## Testing the Application

```bash
# Run tests
uv run py manage.py test
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
