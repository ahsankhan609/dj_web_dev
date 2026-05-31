from django.urls import path

from .views import BlogIndexView, PostDetailView, PostListView

app_name = 'blog'

urlpatterns = [
    path('', BlogIndexView.as_view(), name='index'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
