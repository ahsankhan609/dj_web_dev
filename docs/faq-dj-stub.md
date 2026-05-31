# FAQ: Django Stubs, Ruff, and Type Checking

This file summarizes our discussion so you can revisit it later.

## 1) What does `stub files not found for "django.http"` mean?

This warning comes from the type checker (Pylance/Pyright), not from Django runtime.

- Your app can still run normally.
- The checker is saying it cannot find type stub metadata (`.pyi`) for that import in the active environment.
- Runtime execution and static typing are separate concerns.

## 2) What is `django-stubs`?

`django-stubs` is a typing support package for Django.

- It provides type information for Django APIs.
- It improves autocomplete and static analysis quality.
- It does not change how your Django app runs at runtime.

Think of it like TypeScript definition files for Python libraries.

## 3) Why can my project run fine even with that warning?

Because Python runtime only needs executable `.py` code.
Type checkers need extra type metadata (annotations/stubs) to reason about code.
If metadata is missing, you get warnings, but runtime may still be perfect.

## 4) Install `django-stubs` with `uv`

Recommended:

```bash
uv add --dev django-stubs
```

Alternative if using mypy setup:

```bash
uv add --dev "django-stubs[compatible-mypy]"
```

## 5) Can I use Ruff instead of mypy?

Yes, but with an important distinction:

- Ruff is a linter/formatter.
- Pyright/Pylance is a type checker.

So the practical modern setup is:

- Ruff for lint + format
- Pyright for type checking
- django-stubs for Django typing metadata

## 6) Suggested tooling commands

```bash
uv run ruff check .
uv run ruff format .
uv run pyright
```

## 7) Recommended `pyproject.toml` improvements we discussed

1. Keep only one `[tool.django-stubs]` section (remove duplicates).
2. Avoid conflicting Ruff `select` settings (`ALL` vs curated list).
3. Prefer curated Ruff rules for learning (less noisy than `ALL`).
4. Use `[tool.django-stubs]` (correct table name).
5. Consider avoiding custom `tool.uv.sources` GitHub overrides unless needed.

## 8) README improvements we discussed

1. Use commands that work well on Windows/PowerShell.
2. Prefer `uv run python manage.py ...` for reliability.
3. Remove invalid command: `uv run django-stubs check .` (not a valid CLI).
4. Keep quality checks grouped and clear:
   - `uv run ruff check .`
   - `uv run ruff format .`
   - `uv run pyright`
5. Document required `.env` variables clearly:
   - `SECRET_KEY`
   - `DEBUG`

## 9) Example baseline config direction

- Keep `typeCheckingMode = "standard"` initially.
- Move to `"strict"` later when comfortable.
- Exclude noisy/generated directories (`.venv`, `migrations`, caches, static build output) from checks where appropriate.

---

If needed, convert this FAQ into a shorter "quick start" and a stricter "advanced setup" version later.
