# Blog Test Suite — Practices & Reference

## Coding standards enforced throughout

### PEP 8 compliance

- Line length is capped at **100 characters**, matching the project-wide `ruff` configuration.
- Single quotes are used for all strings, consistent with `[tool.ruff.format] quote-style = "single"`.
- One blank line between top-level fixtures/functions inside a module; two blank lines between
  logical sections marked with comment banners (`# ---`).
- Imports are grouped and sorted by `ruff` (standard library → third-party → local), with
  `from __future__ import annotations` always first when present.

### Type annotations (ANN style)

Every function and fixture carries explicit return and parameter type hints:

```python
# Test functions always return None
def test_tag_str_returns_name(tag: Tag) -> None: ...

# Fixtures return the concrete model type
@pytest.fixture()
def published_post(db: None, author: Author) -> Post: ...
```

`from __future__ import annotations` is used at the top of each file so forward references
resolve lazily — required when annotating `list[Tag]` or similar generics on Python 3.12.

### Arrange / Act / Assert (AAA) pattern

Every test body is divided into three explicit phases using inline comments:

```python
def test_post_default_status_is_draft() -> None:
    # Arrange / Act
    post: Post = PostFactory()

    # Assert
    assert post.status == Post.Status.DRAFT
```

When Arrange and Act collapse into a single step (e.g. creating an object), they are combined
as `# Arrange / Act`. When an action is expected to raise an exception, Act and Assert merge
inside a `pytest.raises` block:

```python
def test_tag_slug_must_be_unique(tag: Tag) -> None:
    # Arrange
    duplicate_slug: str = tag.slug

    # Act / Assert
    with pytest.raises(IntegrityError):
        TagFactory(slug=duplicate_slug)
```

### Test naming convention

Tests follow the `test_<subject>_<condition>_<expected_outcome>` pattern in snake_case:

| Good | Reason |
|---|---|
| `test_author_name_falls_back_to_username` | Subject + condition + outcome all clear |
| `test_post_list_shows_only_published` | Describes the exact behaviour being verified |
| `test_post_detail_404_for_unknown_slug` | HTTP status code is part of the expected outcome |

Avoid generic names like `test_post_1` or `test_view` — they give no signal when they fail.

### One assertion concept per test

Each test verifies **one behavior**. A test may contain multiple `assert` statements when
they are logically part of the same concept (e.g. asserting both sides of a filter):

```python
# Acceptable — both assertions verify the same filter behavior
assert published_post in posts_in_context
assert draft_post not in posts_in_context
```

Avoid testing multiple unrelated properties in a single test — split them instead.

### factory_boy over raw ORM

Test data is created through `factories.py`, not raw `Model.objects.create()` calls.
Factories provide sensible defaults, sequential uniqueness, and realistic fake data via `Faker`.
Only override fields that are relevant to the specific test being written:

```python
# Clear intent: this test only cares about the author and status
PostFactory(author=author, status=Post.Status.PUBLISHED)
```

### Database access

- Model tests use `@pytest.mark.django_db`.
- View tests rely on `client` (pytest-django built-in), which implicitly enables DB access.
- URL tests need **no** `@pytest.mark.django_db` — `resolve()` and `reverse()` are pure
  Django URL machinery with no DB interaction.

---

## Running the suite

### Prerequisites

Ensure the `.env` file exists with at least `SECRET_KEY` set (Django settings require it).
Install all dependencies (including dev group) with:

```bash
uv sync
```

### Common commands

```bash
# Run the entire test suite
uv run pytest

# Run only the blog app tests
uv run pytest blog/tests/

# Run a single test module
uv run pytest blog/tests/test_models.py
uv run pytest blog/tests/test_views.py
uv run pytest blog/tests/test_urls.py

# Run tests whose name matches a keyword
uv run pytest -k 'post_list'
uv run pytest -k 'tag or author'

# Stop immediately on the first failure
uv run pytest -x

# Show a shorter traceback (useful in CI logs)
uv run pytest --tb=short -q

# Run with coverage report (requires pytest-cov)
uv run pytest --cov=blog --cov-report=term-missing

# Re-run only the tests that failed last time
uv run pytest --lf
```

### Reading output

`-v` (verbose) is enabled by default via `addopts` in `pyproject.toml`, so every test name
is printed with its PASSED / FAILED status. A typical passing run looks like:

```
blog/tests/test_models.py::test_tag_str_returns_name PASSED
blog/tests/test_models.py::test_tag_slug_must_be_unique PASSED
...
13 passed in 0.42s
```
