from __future__ import annotations

import factory
import factory.django
from django.contrib.auth.models import User
from django.utils.text import slugify

from blog.models import Author, Post, Tag


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username: str = factory.Sequence(lambda n: f'user_{n}')
    first_name: str = factory.Faker('first_name')
    last_name: str = factory.Faker('last_name')
    email: str = factory.Faker('email')


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name: str = factory.Sequence(lambda n: f'tag-{n}')
    slug: str = factory.LazyAttribute(lambda obj: slugify(obj.name))


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    user: User = factory.SubFactory(UserFactory)
    bio: str = factory.Faker('paragraph')
    city: str = factory.Faker('city')
    state: str = factory.Faker('state')
    country: str = factory.Faker('country')
    website: str = factory.Faker('url')
    twitter_handle: str = factory.Sequence(lambda n: f'handle_{n}')


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
        skip_postgeneration_save = True

    title: str = factory.Sequence(lambda n: f'Post Title {n}')
    slug: str = factory.LazyAttribute(lambda obj: slugify(obj.title))
    author: Author = factory.SubFactory(AuthorFactory)
    body: str = factory.Faker('paragraphs')
    status: str = Post.Status.DRAFT

    @factory.post_generation
    def tags(self, create: bool, extracted: list[Tag] | None, **kwargs: object) -> None:
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.tags.add(tag)
