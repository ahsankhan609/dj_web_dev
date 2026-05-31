from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='author_profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='authors/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    twitter_handle = models.CharField(max_length=50, blank=True)

    @property
    def name(self) -> str:
        return self.user.get_full_name() or self.user.username

    @property
    def email(self) -> str:
        return self.user.email

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=250)
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
    )
    body = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: list[str] = ['-created_on']

    def __str__(self) -> str:
        return self.title
