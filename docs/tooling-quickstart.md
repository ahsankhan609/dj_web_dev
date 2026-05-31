# Tooling Quickstart (Django + uv + Ruff + Pyright)

This is a copy-paste command reference for daily use.

## 1) First-time setup

```bash
uv sync
```

If you still need Django typing support:

```bash
uv add --dev django-stubs
```

## 2) Environment file

Create `.env` from `.env.example` and set:

- `SECRET_KEY`
- `DEBUG`

PowerShell example:

```powershell
Copy-Item .env.example .env
```

## 3) Run the project

```bash
uv run python manage.py runserver
```

## 4) Database commands

```bash
uv run python manage.py migrate
```

## 5) Tests

```bash
uv run python manage.py test
```

## 6) Code quality checks

Lint:

```bash
uv run ruff check .
```

Format:

```bash
uv run ruff format .
```

Type check:

```bash
uv run pyright
```

## 7) Typical daily flow

```bash
uv run ruff check .
uv run ruff format .
uv run pyright
uv run python manage.py test
```

## 8) Add new dependencies

Runtime dependency:

```bash
uv add <package-name>
```

Dev dependency:

```bash
uv add --dev <package-name>
```

---

If type checker shows warnings like missing Django stubs, confirm IDE is using your project `.venv`.
