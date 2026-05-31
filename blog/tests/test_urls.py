from __future__ import annotations

from django.urls import resolve, reverse

from blog.views import BlogIndexView, PostDetailView, PostListView


# ---------------------------------------------------------------------------
# resolve()  —  path string → view callable
# ---------------------------------------------------------------------------


def test_resolve_blog_index() -> None:
    # Arrange
    path: str = '/blog/'

    # Act
    match = resolve(path)

    # Assert
    assert match.func.view_class is BlogIndexView  # type: ignore[attr-defined]


def test_resolve_post_list() -> None:
    # Arrange
    path: str = '/blog/posts/'

    # Act
    match = resolve(path)

    # Assert
    assert match.func.view_class is PostListView  # type: ignore[attr-defined]


def test_resolve_post_detail() -> None:
    # Arrange
    path: str = '/blog/posts/my-post/'

    # Act
    match = resolve(path)

    # Assert
    assert match.func.view_class is PostDetailView  # type: ignore[attr-defined]


# ---------------------------------------------------------------------------
# reverse()  —  named URL → path string
# ---------------------------------------------------------------------------


def test_reverse_blog_index() -> None:
    # Arrange
    expected: str = '/blog/'

    # Act
    result: str = reverse('blog:index')

    # Assert
    assert result == expected


def test_reverse_post_list() -> None:
    # Arrange
    expected: str = '/blog/posts/'

    # Act
    result: str = reverse('blog:post-list')

    # Assert
    assert result == expected


def test_reverse_post_detail() -> None:
    # Arrange
    slug: str = 'my-post'
    expected: str = f'/blog/posts/{slug}/'

    # Act
    result: str = reverse('blog:post-detail', kwargs={'slug': slug})

    # Assert
    assert result == expected
