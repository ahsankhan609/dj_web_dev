from __future__ import annotations

import pytest
from django.contrib.auth.models import User

from blog.models import Author, Post, Tag
from blog.tests.factories import AuthorFactory, PostFactory, TagFactory, UserFactory


@pytest.fixture()
def user(db: None) -> User:
    return UserFactory()


@pytest.fixture()
def author(db: None) -> Author:
    return AuthorFactory()


@pytest.fixture()
def tag(db: None) -> Tag:
    return TagFactory()


@pytest.fixture()
def published_post(db: None, author: Author) -> Post:
    return PostFactory(author=author, status=Post.Status.PUBLISHED)


@pytest.fixture()
def draft_post(db: None, author: Author) -> Post:
    return PostFactory(author=author, status=Post.Status.DRAFT)
