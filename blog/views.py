from django.views.generic import DetailView, ListView, TemplateView

from .models import Post


class BlogIndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs: object) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog Homepage'
        context['heading'] = 'Welcome to the Blog'
        context['description'] = (
            'This is the home page of the blog. '
            'Here you can find all the latest posts and updates.'
        )
        return context


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = (
        Post.objects.filter(status=Post.Status.PUBLISHED)
        .select_related('author__user')
        .prefetch_related('tags')
        .order_by('-created_on')
    )

    def get_context_data(self, **kwargs: object) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog Posts'
        context['heading'] = 'Blog Posts'
        context['description'] = 'This is the list of all the blog posts.'
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs: object) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        post: Post = self.object  # type: ignore[assignment]
        if post.author is not None:
            context['related_posts'] = (
                post.author.posts.filter(status=Post.Status.PUBLISHED)
                .exclude(pk=post.pk)
                .order_by('-created_on')[:5]
            )
        else:
            context['related_posts'] = Post.objects.none()
        return context
