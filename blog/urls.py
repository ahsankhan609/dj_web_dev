from django.urls import path
from . import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('', blog_views.index, name='index'),
    path('posts/', blog_views.post_list, name='post-list'),
    path('posts/<slug:slug>/', blog_views.post_detail, name='post-detail'),
]
