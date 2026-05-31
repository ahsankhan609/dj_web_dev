from __future__ import annotations

import pytest
from django.db import IntegrityError

from blog.models import Author, Post, Tag
from blog.tests.factories import AuthorFactory, PostFactory, TagFactory, UserFactory


# ---------------------------------------------------------------------------
# Tag
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_tag_str_returns_name(tag: Tag) -> None:
    # Arrange
    expected: str = tag.name

    # Act
    result: str = str(tag)

    # Assert
    assert result == expected


@pytest.mark.django_db
def test_tag_slug_must_be_unique(tag: Tag) -> None:
    # Arrange
    duplicate_slug: str = tag.slug

    # Act / Assert
    with pytest.raises(IntegrityError):
        TagFactory(slug=duplicate_slug)


# ---------------------------------------------------------------------------
# Author
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_author_name_returns_full_name() -> None:
    # Arrange
    user = UserFactory(first_name='Ada', last_name='Lovelace')
    author: Author = AuthorFactory(user=user)

    # Act
    result: str = author.name

    # Assert
    assert result == 'Ada Lovelace'


@pytest.mark.django_db
def test_author_name_falls_back_to_username() -> None:
    # Arrange
    user = UserFactory(first_name='', last_name='')
    author: Author = AuthorFactory(user=user)

    # Act
    result: str = author.name

    # Assert
    assert result == user.username


@pytest.mark.django_db
def test_author_email_property(author: Author) -> None:
    # Arrange
    expected_email: str = author.user.email

    # Act
    result: str = author.email

    # Assert
    assert result == expected_email


@pytest.mark.django_db
def test_author_str_equals_name(author: Author) -> None:
    # Arrange
    expected: str = author.name

    # Act
    result: str = str(author)

    # Assert
    assert result == expected


# ---------------------------------------------------------------------------
# Post
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_post_str_returns_title(published_post: Post) -> None:
    # Arrange
    expected: str = published_post.title

    # Act
    result: str = str(published_post)

    # Assert
    assert result == expected


@pytest.mark.django_db
def test_post_default_status_is_draft() -> None:
    # Arrange / Act
    post: Post = PostFactory()

    # Assert
    assert post.status == Post.Status.DRAFT


@pytest.mark.django_db
def test_post_status_choices_exist() -> None:
    # Arrange / Act / Assert
    assert Post.Status.DRAFT == 'draft'
    assert Post.Status.PUBLISHED == 'published'


@pytest.mark.django_db
def test_post_ordering_newest_first() -> None:
    # Arrange
    older_post: Post = PostFactory(status=Post.Status.PUBLISHED)
    newer_post: Post = PostFactory(status=Post.Status.PUBLISHED)

    # Act
    posts: list[Post] = list(Post.objects.all())

    # Assert — default Meta ordering is ['-created_on']
    assert posts[0].pk == newer_post.pk
    assert posts[1].pk == older_post.pk


@pytest.mark.django_db
def test_post_author_nullable() -> None:
    # Arrange / Act
    post: Post = PostFactory(author=None)

    # Assert
    assert post.author is None


@pytest.mark.django_db
def test_post_tags_many_to_many(published_post: Post, tag: Tag) -> None:
    # Arrange
    published_post.tags.add(tag)

    # Act
    result: list[Tag] = list(published_post.tags.all())

    # Assert
    assert tag in result


@pytest.mark.django_db
def test_post_published_filter_excludes_drafts(
    published_post: Post,
    draft_post: Post,
) -> None:
    # Arrange
    expected_slug: str = published_post.slug

    # Act
    published_slugs: list[str] = list(
        Post.objects.filter(status=Post.Status.PUBLISHED).values_list('slug', flat=True)
    )

    # Assert
    assert expected_slug in published_slugs
    assert draft_post.slug not in published_slugs
