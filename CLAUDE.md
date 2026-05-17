# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A Django learning project following the Udemy course "Python Django - The Practical Guide" by Maximilian Schwarzmüller. The project uses **uv** for dependency management.

## Commands

```bash
# Install dependencies (first time setup)
uv sync

# Run development server
uv run python manage.py runserver

# Run all tests
uv run python manage.py test

# Run tests for a specific app
uv run python manage.py test challenges

# Run Django system checks
uv run python manage.py check

# Apply migrations
uv run python manage.py migrate

# Add a dependency
uv add <package>
```

## Architecture

- `main/` — Django project config: `settings.py`, root `urls.py`, `wsgi.py`, `asgi.py`
- `challenges/` — the only app; contains function-based views returning plain `HttpResponse` strings, no models or templates yet

URL routing: `main/urls.py` includes `challenges/urls.py` under the `/challenges/` prefix with namespace `challenges`. Each month maps to its own path (e.g. `/challenges/jan/`).

## Environment

Secrets are kept out of `settings.py` and loaded from a `.env` file via `python-dotenv`. Copy `.env.example` to `.env` and fill in values before running the project. Required variables:

- `SECRET_KEY` — Django secret key
- `DEBUG` — `True` or `False`

## Type hints

Views use Django's `HttpRequest` / `HttpResponse` type hints and `list[...]` / `dict[...]` annotations throughout `settings.py`.
