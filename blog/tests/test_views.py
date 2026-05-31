from __future__ import annotations

import pytest
from django.test import Client
from django.urls import reverse

from blog.models import Author, Post, Tag
from blog.tests.factories import PostFactory


# ---------------------------------------------------------------------------
# BlogIndexView  —  GET /blog/
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_blog_index_status_200(client: Client) -> None:
    # Arrange
    url: str = reverse('blog:index')

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_blog_index_template(client: Client) -> None:
    # Arrange
    url: str = reverse('blog:index')

    # Act
    response = client.get(url)

    # Assert
    template_names: list[str] = [t.name for t in response.templates]
    assert 'blog/index.html' in template_names


@pytest.mark.django_db
def test_blog_index_context_keys(client: Client) -> None:
    # Arrange
    url: str = reverse('blog:index')

    # Act
    response = client.get(url)

    # Assert
    for key in ('title', 'heading', 'description'):
        assert key in response.context


# ---------------------------------------------------------------------------
# PostListView  —  GET /blog/posts/
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_post_list_status_200(client: Client) -> None:
    # Arrange
    url: str = reverse('blog:post-list')

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_list_template(client: Client) -> None:
    # Arrange
    url: str = reverse('blog:post-list')

    # Act
    response = client.get(url)

    # Assert
    template_names: list[str] = [t.name for t in response.templates]
    assert 'blog/post_list.html' in template_names


@pytest.mark.django_db
def test_post_list_shows_only_published(
    client: Client,
    published_post: Post,
    draft_post: Post,
) -> None:
    # Arrange
    url: str = reverse('blog:post-list')

    # Act
    response = client.get(url)
    posts_in_context: list[Post] = list(response.context['posts'])

    # Assert
    assert published_post in posts_in_context
    assert draft_post not in posts_in_context


@pytest.mark.django_db
def test_post_list_context_keys(client: Client) -> None:
    # Arrange
    url: str = reverse('blog:post-list')

    # Act
    response = client.get(url)

    # Assert
    for key in ('posts', 'title', 'heading', 'description'):
        assert key in response.context


# ---------------------------------------------------------------------------
# PostDetailView  —  GET /blog/posts/<slug>/
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_post_detail_status_200(client: Client, published_post: Post) -> None:
    # Arrange
    url: str = reverse('blog:post-detail', kwargs={'slug': published_post.slug})

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail_404_for_unknown_slug(client: Client) -> None:
    # Arrange
    url: str = reverse('blog:post-detail', kwargs={'slug': 'does-not-exist'})

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 404


@pytest.mark.django_db
def test_post_detail_template(client: Client, published_post: Post) -> None:
    # Arrange
    url: str = reverse('blog:post-detail', kwargs={'slug': published_post.slug})

    # Act
    response = client.get(url)

    # Assert
    template_names: list[str] = [t.name for t in response.templates]
    assert 'blog/post_detail.html' in template_names


@pytest.mark.django_db
def test_post_detail_related_posts_from_same_author(
    client: Client,
    author: Author,
    published_post: Post,
) -> None:
    # Arrange — second published post by the same author
    related: Post = PostFactory(author=author, status=Post.Status.PUBLISHED)
    url: str = reverse('blog:post-detail', kwargs={'slug': published_post.slug})

    # Act
    response = client.get(url)
    related_posts: list[Post] = list(response.context['related_posts'])

    # Assert
    assert related in related_posts


@pytest.mark.django_db
def test_post_detail_related_posts_empty_when_no_author(client: Client) -> None:
    # Arrange — post with no author
    post: Post = PostFactory(author=None, status=Post.Status.PUBLISHED)
    url: str = reverse('blog:post-detail', kwargs={'slug': post.slug})

    # Act
    response = client.get(url)
    related_posts = list(response.context['related_posts'])

    # Assert
    assert related_posts == []
