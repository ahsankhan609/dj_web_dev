from django.contrib import admin

from .models import Author, Post, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'city', 'country']
    search_fields = ['user__username', 'user__first_name',
                     'user__last_name', 'user__email']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_on', 'updated_on']
    list_filter = ['status', 'tags', 'created_on']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    filter_horizontal = ['tags']
    date_hierarchy = 'created_on'
