from django.http import HttpRequest, HttpResponse
from django.http import Http404
from django.shortcuts import render

# List of all posts
# Each post is a dictionary with the following keys:
# - title: str
# - slug: str
# - content: str
# - created_at: str
# - updated_at: str
POSTS: list[dict[str, str]] = [
    {
        'title': 'Post 1',
        'slug': 'post-1',
        'content': 'This is the content of the first post.',
        'created_at': '2021-01-01',
        'updated_at': '2021-01-01',
    },
    {
        'title': 'Post 2',
        'slug': 'post-2',
        'content': 'This is the content of the second post.',
        'created_at': '2021-01-01',
        'updated_at': '2021-01-01',
    },
    {
        'title': 'Post 3',
        'slug': 'post-3',
        'content': 'This is the content of the third post.',
        'created_at': '2021-01-01',
        'updated_at': '2021-01-01',
    },
    {
        'title': 'Post 4',
        'slug': 'post-4',
        'content': 'This is the content of the fourth post.',
        'created_at': '2021-01-01',
        'updated_at': '2021-01-01',
    },
]


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Blog Homepage',
        'heading': 'Welcome to the Blog',
        'description': 'This is the home page of the blog. Here you can find all the latest posts and updates.',
    }
    return render(request, 'blog/index.html', context=context)


def post_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/post_list.html', context={
        'title': 'Blog Posts',
        'heading': 'Blog Posts',
        'description': 'This is the list of all the blog posts.',
        'posts': POSTS,
    })


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    post = next((post for post in POSTS if post['slug'] == slug), None)
    if post is None:
        raise Http404("Post not found")
    return render(request, 'blog/post_detail.html', context={
        'title': post['title'],
        'heading': post['title'],
        'description': post['content'],
        'content': post['content'],
        'created_at': post['created_at'],
        'updated_at': post['updated_at'],
    })
